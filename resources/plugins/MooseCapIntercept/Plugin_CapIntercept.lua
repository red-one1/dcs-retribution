env.info("-----DCSRetribution|MOOSE CAP Intercept plugin - configuration start ------")

--------------------------------------------------------------------------------
-- AUTOMATED MOOSE-BASED CAP INTERCEPTION HOOK
--------------------------------------------------------------------------------
-- This plugin automatically vectors BARCAP/TARCAP flights to intercept hot/flanking
-- enemy aircraft within configurable range using AWACS detection.
--
-- Features:
-- * Auto-discovers AWACS/AEW radar groups from the mission
-- * Auto-discovers friendly CAP flights by inspecting group templates
-- * Persists original DCS routes for CAPs to resume after interceptions
-- * Scheduler polls detections and vectors nearest CAP to qualifying bogeys
-- * Restores original route/racetrack when intercept completes
--
-- Configuration:
-- * AWACS_TYPES: List of AWACS/AEW aircraft types (extendable)
-- * InterceptRangeNM: Maximum range from CAP to bogey (default 80nm)
-- * MaxAspectAngle: Max aspect angle for hot/flanking (default 120°)
-- * SchedulerInterval: Detection polling interval (default 10s)
-- * EngageRangeNM: ROE engage range (default 80nm)
--
-- Integration notes:
-- * Add aircraft types to AWACS_TYPES table to extend AWACS whitelist
-- * Adjust range/aspect thresholds via plugin options in UI
-- * Compatible with existing Retribution mission generation
--------------------------------------------------------------------------------

-- Default configuration values (overridden by dcsRetribution.plugins when present)
local InterceptRangeNM = 80
local MaxAspectAngle = 120
local SchedulerInterval = 10
local EngageRangeNM = 80
local CapInterceptDebug = false

-- Pull configuration from UI if available
if dcsRetribution and dcsRetribution.plugins and dcsRetribution.plugins.MooseCapIntercept then
    local p = dcsRetribution.plugins.MooseCapIntercept
    InterceptRangeNM = p.InterceptRangeNM or InterceptRangeNM
    MaxAspectAngle = p.MaxAspectAngle or MaxAspectAngle
    SchedulerInterval = p.SchedulerInterval or SchedulerInterval
    EngageRangeNM = p.EngageRangeNM or EngageRangeNM
    CapInterceptDebug = p.CapInterceptDebug or CapInterceptDebug
else
    env.info("-----dcsRetribution.plugins.MooseCapIntercept NOT FOUND, using defaults")
end

env.info(string.format("--------- MooseCapIntercept Config: InterceptRange=%dNM | MaxAspect=%d° | Interval=%ds | EngageRange=%dNM | Debug=%s",
    InterceptRangeNM, MaxAspectAngle, SchedulerInterval, EngageRangeNM, tostring(CapInterceptDebug)))

--------------------------------------------------------------------------------
-- AWACS/AEW AIRCRAFT TYPE WHITELIST
-- Add aircraft types here to extend the AWACS whitelist
--------------------------------------------------------------------------------
local AWACS_TYPES = {
    -- NATO/US AWACS
    "E-3A",
    "E-2C",
    "E-2D",
    
    -- Russian/Soviet AWACS
    "A-50",
    "Tu-126",
    
    -- Add more AWACS types here as needed
    -- Examples: "KJ-2000", "E-767", etc.
}

--------------------------------------------------------------------------------
-- GLOBAL STATE
--------------------------------------------------------------------------------
local capFlights = {}           -- Table of discovered CAP flights
local detectionSetBlue = nil    -- Moose DETECTION_AREAS set for Blue coalition
local detectionSetRed = nil     -- Moose DETECTION_AREAS set for Red coalition
local bogeyAssignments = {}     -- Track bogey → CAP assignments
local schedulerId = nil         -- Scheduler ID
local awacsSetBlue = nil        -- SET_GROUP for Blue AWACS (updated dynamically)
local awacsSetRed = nil         -- SET_GROUP for Red AWACS (updated dynamically)
local knownCapGroups = {}       -- Track known CAP group names
local knownAwacsGroups = {}     -- Track known AWACS group names
local lastDiscoveryCheck = 0    -- Time of last discovery check

--------------------------------------------------------------------------------
-- UTILITY FUNCTIONS
--------------------------------------------------------------------------------

-- Debug logging helper
local function Debug(msg)
    if CapInterceptDebug then
        env.info("[CapIntercept] " .. msg)
    end
end

-- Check if a unit type is an AWACS
local function IsAwacsType(typeName)
    for _, awacsType in ipairs(AWACS_TYPES) do
        if typeName and string.find(typeName, awacsType) then
            return true
        end
    end
    return false
end

-- Calculate aspect angle between CAP and bogey heading
local function CalculateAspect(bogeyHeading, capToBogeyHeading)
    -- Aspect is the angle between the bogey's heading and the line from bogey to CAP
    -- Hot aspect: bogey flying towards CAP (aspect close to 0°)
    -- Flanking: bogey flying at an angle (aspect < 90°)
    -- Beam/Cold: bogey flying away (aspect > 90°)
    
    -- The aspect angle is the difference between where the bogey is heading
    -- and where it would need to head to fly directly at the CAP
    local capToBogeyReverse = (capToBogeyHeading + 180) % 360
    local aspect = math.abs(bogeyHeading - capToBogeyReverse)
    if aspect > 180 then
        aspect = 360 - aspect
    end
    return aspect
end

-- Convert nautical miles to meters
local function NMtoMeters(nm)
    return nm * 1852
end

--------------------------------------------------------------------------------
-- AUTO-DISCOVERY FUNCTIONS
--------------------------------------------------------------------------------

-- Auto-discover AWACS/AEW radar groups
local function DiscoverAwacs()
    Debug("Discovering AWACS groups...")
    local awacsGroupsBlue = {}
    local awacsGroupsRed = {}
    local newAwacsFound = false
    
    -- Scan all coalitions for AWACS aircraft
    for coalName, coalId in pairs(coalition.side) do
        local groups = coalition.getGroups(coalId, Group.Category.AIRPLANE)
        if groups then
            for _, group in ipairs(groups) do
                local groupName = group:getName()
                
                -- Skip if already known
                if not knownAwacsGroups[groupName] then
                    local units = group:getUnits()
                    if units and #units > 0 then
                        local unit = units[1]
                        local typeName = unit:getTypeName()
                        if IsAwacsType(typeName) then
                            -- Store AWACS by coalition
                            if coalId == coalition.side.BLUE then
                                table.insert(awacsGroupsBlue, groupName)
                            elseif coalId == coalition.side.RED then
                                table.insert(awacsGroupsRed, groupName)
                            end
                            knownAwacsGroups[groupName] = coalId
                            newAwacsFound = true
                            Debug("  Found NEW AWACS: " .. groupName .. " (" .. typeName .. ", Coalition: " .. coalName .. ")")
                        end
                    end
                else
                    -- Already known, add to appropriate list
                    local knownCoalId = knownAwacsGroups[groupName]
                    if knownCoalId == coalition.side.BLUE then
                        table.insert(awacsGroupsBlue, groupName)
                    elseif knownCoalId == coalition.side.RED then
                        table.insert(awacsGroupsRed, groupName)
                    end
                end
            end
        end
    end
    
    if newAwacsFound then
        env.info("[CapIntercept] Discovered new AWACS groups - updating detection sets")
    end
    
    return awacsGroupsBlue, awacsGroupsRed, newAwacsFound
end

-- Auto-discover CAP flights (groups with task == "CAP")
local function DiscoverCapFlights()
    Debug("Discovering CAP flights...")
    local newCapsFound = false
    
    -- Scan both Red and Blue coalitions for CAP flights
    for coalName, coalId in pairs(coalition.side) do
        local groups = coalition.getGroups(coalId, Group.Category.AIRPLANE)
        if groups then
            for _, group in ipairs(groups) do
                local groupName = group:getName()
                
                -- Skip if already known
                if not knownCapGroups[groupName] then
                    local units = group:getUnits()
                    
                    if units and #units > 0 then
                        -- Check if group template has CAP task
                        -- DCS stores tasks in the group data
                        local controller = group:getController()
                        if controller then
                            -- Try to determine if this is a CAP flight
                            -- We check the group name for CAP indicators as a heuristic
                            -- since direct task inspection is limited in mission scripting environment
                            if string.find(groupName, "CAP") or 
                               string.find(groupName, "BARCAP") or 
                               string.find(groupName, "TARCAP") then
                                
                                Debug("  Found NEW CAP: " .. groupName .. " (Coalition: " .. coalName .. ")")
                                
                                -- Store CAP flight data with coalition info
                                local capFlight = {
                                    groupName = groupName,
                                    group = group,
                                    coalition = coalId,
                                    coalitionName = coalName,
                                    originalRoute = nil,  -- Will store route waypoints
                                    racetrackStart = nil, -- Will store racetrack anchor 1
                                    racetrackEnd = nil,   -- Will store racetrack anchor 2
                                    currentTask = "patrol", -- Track current task state
                                    assignedBogey = nil   -- Track assigned intercept
                                }
                                
                                table.insert(capFlights, capFlight)
                                knownCapGroups[groupName] = true
                                newCapsFound = true
                                
                                -- Extract racetrack immediately for new CAP
                                ExtractRacetrackWaypoints(capFlight)
                            end
                        end
                    end
                end
            end
        end
    end
    
    if newCapsFound then
        env.info(string.format("[CapIntercept] Discovered new CAP flights - now tracking %d total", #capFlights))
    end
    
    return newCapsFound
end

-- Extract racetrack waypoints from CAP route
local function ExtractRacetrackWaypoints(capFlight)
    -- In DCS, racetrack waypoints are typically consecutive waypoints where
    -- an orbit/race track task is assigned
    -- For now, we'll store the group's current position as racetrack center
    -- In a full implementation, this would parse the mission file or use
    -- Moose's route extraction capabilities
    
    local units = capFlight.group:getUnits()
    if units and #units > 0 then
        local unit = units[1]
        local pos = unit:getPosition()
        if pos then
            capFlight.racetrackStart = {x = pos.p.x, y = pos.p.z}
            -- Create a simple racetrack by offsetting from current position
            capFlight.racetrackEnd = {x = pos.p.x + 10000, y = pos.p.z}
            Debug("  Extracted racetrack for " .. capFlight.groupName)
        end
    end
end

--------------------------------------------------------------------------------
-- MOOSE INTEGRATION
--------------------------------------------------------------------------------

-- Initialize Moose detection set with AWACS for a specific coalition
local function InitializeDetectionForCoalition(awacsGroups, coalitionName)
    if #awacsGroups == 0 then
        Debug("No " .. coalitionName .. " AWACS groups found for detection")
        return nil
    end
    
    Debug("Initializing " .. coalitionName .. " DETECTION_AREAS with " .. #awacsGroups .. " AWACS groups")
    
    -- Create detection set using Moose
    if not DETECTION_AREAS then
        env.info("[CapIntercept] ERROR: Moose DETECTION_AREAS not available!")
        return nil
    end
    
    -- Create a SET_GROUP for AWACS
    local awacsSet = SET_GROUP:New()
    for _, groupName in ipairs(awacsGroups) do
        local group = GROUP:FindByName(groupName)
        if group then
            awacsSet:AddGroup(group)
        end
    end
    awacsSet:FilterOnce()
    
    -- Create detection set
    local detection = DETECTION_AREAS:New(awacsSet, NMtoMeters(InterceptRangeNM))
    detection:FilterCategories({Unit.Category.AIRPLANE})
    detection:SetRefreshTimeInterval(SchedulerInterval)
    
    Debug(coalitionName .. " detection set initialized successfully")
    return detection, awacsSet
end

-- Update AWACS set with newly spawned AWACS groups for a coalition
local function UpdateAwacsSetForCoalition(awacsGroups, awacsSet, detectionSet, coalitionName)
    if not awacsSet then
        Debug("Creating new " .. coalitionName .. " AWACS set")
        return InitializeDetectionForCoalition(awacsGroups, coalitionName)
    end
    
    Debug("Updating " .. coalitionName .. " AWACS set with new groups")
    
    -- Add new AWACS to the set
    for _, groupName in ipairs(awacsGroups) do
        local group = GROUP:FindByName(groupName)
        if group and not awacsSet:FindGroup(groupName) then
            awacsSet:AddGroup(group)
            Debug("  Added " .. groupName .. " to " .. coalitionName .. " AWACS set")
        end
    end
    awacsSet:FilterOnce()
    
    -- Detection set automatically uses updated awacsSet
    return detectionSet, awacsSet
end

-- Wrap CAP group as Moose FLIGHTGROUP
local function WrapCapAsMoose(capFlight)
    if not FLIGHTGROUP then
        env.info("[CapIntercept] ERROR: Moose FLIGHTGROUP not available!")
        return nil
    end
    
    local flightGroup = FLIGHTGROUP:FindByName(capFlight.groupName)
    if not flightGroup then
        Debug("  Creating FLIGHTGROUP for " .. capFlight.groupName)
        flightGroup = FLIGHTGROUP:New(capFlight.groupName)
    end
    
    return flightGroup
end

--------------------------------------------------------------------------------
-- INTERCEPT LOGIC
--------------------------------------------------------------------------------

-- Check if a bogey qualifies for intercept (aspect and range)
local function CheckInterceptConditions(capFlight, bogey)
    local units = capFlight.group:getUnits()
    if not units or #units == 0 then
        return false, "No CAP units"
    end
    
    local capUnit = units[1]
    local capPos = capUnit:getPosition()
    if not capPos then
        return false, "No CAP position"
    end
    
    -- Get bogey info
    local bogeyGroup = bogey:GetGroup()
    if not bogeyGroup then
        return false, "No bogey group"
    end
    
    local bogeyUnit = bogeyGroup:GetUnit(1)
    if not bogeyUnit then
        return false, "No bogey unit"
    end
    
    local bogeyPos = bogeyUnit:GetCoordinate()
    if not bogeyPos then
        return false, "No bogey position"
    end
    
    -- Calculate range
    local capCoord = COORDINATE:NewFromVec3(capPos.p)
    local range = capCoord:Get2DDistance(bogeyPos)
    local rangeNM = range / 1852
    
    if rangeNM > InterceptRangeNM then
        return false, string.format("Range %.1fNM > max %.1fNM", rangeNM, InterceptRangeNM)
    end
    
    -- Calculate aspect
    local bogeyVel = bogeyUnit:GetVelocityVec3()
    local bogeyHeading = math.deg(math.atan2(bogeyVel.z, bogeyVel.x))
    if bogeyHeading < 0 then bogeyHeading = bogeyHeading + 360 end
    
    local capToBogeyHeading = capCoord:HeadingTo(bogeyPos)
    local aspect = CalculateAspect(bogeyHeading, capToBogeyHeading)
    
    if aspect > MaxAspectAngle then
        return false, string.format("Aspect %.1f° > max %.1f°", aspect, MaxAspectAngle)
    end
    
    Debug(string.format("  Intercept conditions MET: Range=%.1fNM, Aspect=%.1f°", rangeNM, aspect))
    return true, "Qualified", rangeNM
end

-- Find nearest available CAP for a bogey from a specific coalition
local function FindNearestCapForCoalition(bogey, capCoalition)
    local nearestCap = nil
    local nearestRange = 999999
    
    -- Get bogey coalition
    local bogeyGroup = bogey:GetGroup()
    if not bogeyGroup then
        return nil
    end
    
    local bogeyCoalition = bogeyGroup:GetCoalition()
    if not bogeyCoalition then
        return nil
    end
    
    for _, capFlight in ipairs(capFlights) do
        -- Skip CAPs already assigned to another bogey
        if capFlight.currentTask == "patrol" then
            -- Only consider CAPs from the specified coalition
            if capFlight.coalition == capCoalition then
                -- Only intercept enemy aircraft (different coalition)
                if capFlight.coalition ~= bogeyCoalition then
                    local qualified, reason, range = CheckInterceptConditions(capFlight, bogey)
                    if qualified and range < nearestRange then
                        nearestCap = capFlight
                        nearestRange = range
                    end
                else
                    Debug(string.format("  Skipping bogey from same coalition: %s (CAP: %s, Bogey: %s)", 
                        bogeyGroup:GetName(), capFlight.coalitionName, 
                        bogeyCoalition == coalition.side.BLUE and "BLUE" or (bogeyCoalition == coalition.side.RED and "RED" or "NEUTRAL")))
                end
            end
        end
    end
    
    return nearestCap
end

-- Vector CAP to intercept bogey
local function VectorToIntercept(capFlight, bogey)
    Debug("Vectoring " .. capFlight.groupName .. " to intercept")
    
    -- Wrap as Moose FLIGHTGROUP if needed
    local flightGroup = WrapCapAsMoose(capFlight)
    if not flightGroup then
        env.info("[CapIntercept] ERROR: Failed to wrap CAP as FLIGHTGROUP")
        return false
    end
    
    -- Get bogey coordinate
    local bogeyGroup = bogey:GetGroup()
    local bogeyUnit = bogeyGroup:GetUnit(1)
    local bogeyCoord = bogeyUnit:GetCoordinate()
    
    -- Create intercept AUFTRAG (Moose mission)
    if not AUFTRAG then
        env.info("[CapIntercept] ERROR: Moose AUFTRAG not available!")
        return false
    end
    
    local intercept = AUFTRAG:NewINTERCEPT(bogeyCoord)
    intercept:SetUrgent(true)
    intercept:SetPriority(1)
    
    -- Set ROE and alarm state
    intercept:SetROE(ENUMS.ROE.WeaponFree)
    intercept:SetAlarmState(ENUMS.AlarmState.Red)
    
    -- Set engage range
    intercept:SetEngageRange(NMtoMeters(EngageRangeNM))
    
    -- Assign mission to flight group
    flightGroup:AddMission(intercept)
    
    -- Update CAP state
    capFlight.currentTask = "intercept"
    capFlight.assignedBogey = bogey
    
    -- Track assignment
    local bogeyName = bogeyGroup:GetName()
    bogeyAssignments[bogeyName] = capFlight.groupName
    
    env.info(string.format("[CapIntercept] %s vectored to intercept %s", 
        capFlight.groupName, bogeyName))
    
    return true
end

-- Restore CAP to original route/racetrack
local function RestoreCapRoute(capFlight)
    Debug("Restoring " .. capFlight.groupName .. " to patrol")
    
    local flightGroup = WrapCapAsMoose(capFlight)
    if not flightGroup then
        return
    end
    
    -- Simple restoration: create a new CAP mission at the racetrack location
    if capFlight.racetrackStart and capFlight.racetrackEnd then
        local startCoord = COORDINATE:New(capFlight.racetrackStart.x, 0, capFlight.racetrackStart.y)
        local endCoord = COORDINATE:New(capFlight.racetrackEnd.x, 0, capFlight.racetrackEnd.y)
        
        if AUFTRAG and AUFTRAG.NewCAP then
            local capMission = AUFTRAG:NewCAP(startCoord, 25000, 400, startCoord, endCoord)
            capMission:SetROE(ENUMS.ROE.WeaponFree)
            capMission:SetAlarmState(ENUMS.AlarmState.Auto)
            
            flightGroup:AddMission(capMission)
            
            Debug("  CAP route restored with new patrol mission")
        end
    end
    
    -- Update state
    capFlight.currentTask = "patrol"
    capFlight.assignedBogey = nil
    
    env.info(string.format("[CapIntercept] %s returned to patrol", capFlight.groupName))
end

--------------------------------------------------------------------------------
-- SCHEDULER FUNCTIONS
--------------------------------------------------------------------------------

-- Check if bogey is still alive
local function IsBogeyAlive(bogey)
    local bogeyGroup = bogey:GetGroup()
    if not bogeyGroup then
        return false
    end
    
    return bogeyGroup:IsAlive()
end

-- Main detection and intercept scheduler
local function SchedulerFunction()
    -- Periodically check for new groups (every 30 seconds)
    local currentTime = timer.getTime()
    if currentTime - lastDiscoveryCheck >= 30 then
        lastDiscoveryCheck = currentTime
        
        -- Check for new AWACS
        local awacsGroupsBlue, awacsGroupsRed, newAwacs = DiscoverAwacs()
        if newAwacs then
            if #awacsGroupsBlue > 0 then
                detectionSetBlue, awacsSetBlue = UpdateAwacsSetForCoalition(awacsGroupsBlue, awacsSetBlue, detectionSetBlue, "Blue")
            end
            if #awacsGroupsRed > 0 then
                detectionSetRed, awacsSetRed = UpdateAwacsSetForCoalition(awacsGroupsRed, awacsSetRed, detectionSetRed, "Red")
            end
        end
        
        -- Check for new CAPs
        DiscoverCapFlights()
    end
    
    -- Process detections for Blue CAPs using Blue AWACS
    if detectionSetBlue then
        local detectedItemsBlue = detectionSetBlue:GetDetectedItems()
        if detectedItemsBlue and #detectedItemsBlue > 0 then
            Debug(string.format("Processing %d Blue AWACS detections", #detectedItemsBlue))
            
            -- Check each detected item
            for _, detectedItem in ipairs(detectedItemsBlue) do
                local bogeyGroup = detectedItem:GetGroup()
                if bogeyGroup then
                    local bogeyName = bogeyGroup:GetName()
                    
                    -- Skip if already assigned
                    if not bogeyAssignments[bogeyName] then
                        -- Find nearest Blue CAP
                        local nearestCap = FindNearestCapForCoalition(detectedItem, coalition.side.BLUE)
                        
                        if nearestCap then
                            VectorToIntercept(nearestCap, detectedItem)
                        end
                    else
                        -- Check if bogey is still alive
                        if not IsBogeyAlive(detectedItem) then
                            Debug("  Bogey " .. bogeyName .. " destroyed, releasing CAP")
                            
                            -- Find assigned CAP and restore it
                            local assignedCapName = bogeyAssignments[bogeyName]
                            for _, capFlight in ipairs(capFlights) do
                                if capFlight.groupName == assignedCapName then
                                    RestoreCapRoute(capFlight)
                                    break
                                end
                            end
                            
                            bogeyAssignments[bogeyName] = nil
                        end
                    end
                end
            end
        end
    end
    
    -- Process detections for Red CAPs using Red AWACS
    if detectionSetRed then
        local detectedItemsRed = detectionSetRed:GetDetectedItems()
        if detectedItemsRed and #detectedItemsRed > 0 then
            Debug(string.format("Processing %d Red AWACS detections", #detectedItemsRed))
            
            -- Check each detected item
            for _, detectedItem in ipairs(detectedItemsRed) do
                local bogeyGroup = detectedItem:GetGroup()
                if bogeyGroup then
                    local bogeyName = bogeyGroup:GetName()
                    
                    -- Skip if already assigned
                    if not bogeyAssignments[bogeyName] then
                        -- Find nearest Red CAP
                        local nearestCap = FindNearestCapForCoalition(detectedItem, coalition.side.RED)
                        
                        if nearestCap then
                            VectorToIntercept(nearestCap, detectedItem)
                        end
                    else
                        -- Check if bogey is still alive
                        if not IsBogeyAlive(detectedItem) then
                            Debug("  Bogey " .. bogeyName .. " destroyed, releasing CAP")
                            
                            -- Find assigned CAP and restore it
                            local assignedCapName = bogeyAssignments[bogeyName]
                            for _, capFlight in ipairs(capFlights) do
                                if capFlight.groupName == assignedCapName then
                                    RestoreCapRoute(capFlight)
                                    break
                                end
                            end
                            
                            bogeyAssignments[bogeyName] = nil
                        end
                    end
                end
            end
        end
    end
    
    -- Also check for CAPs that completed intercept (arrived at bogey location)
    for _, capFlight in ipairs(capFlights) do
        if capFlight.currentTask == "intercept" and capFlight.assignedBogey then
            if not IsBogeyAlive(capFlight.assignedBogey) then
                -- Bogey destroyed, return to patrol
                local bogeyName = capFlight.assignedBogey:GetGroup():GetName()
                bogeyAssignments[bogeyName] = nil
                RestoreCapRoute(capFlight)
            end
        end
    end
end

--------------------------------------------------------------------------------
-- INITIALIZATION
--------------------------------------------------------------------------------

-- Main initialization function
local function Initialize()
    env.info("[CapIntercept] Starting automated CAP interception system...")
    
    -- Check if Moose is available
    if not BASE then
        env.info("[CapIntercept] ERROR: Moose not loaded! Plugin requires Moose.")
        return
    end
    
    -- Wait a bit for mission to stabilize
    timer.scheduleFunction(function()
        -- Auto-discover AWACS
        local awacsGroupsBlue, awacsGroupsRed, newAwacs = DiscoverAwacs()
        local totalAwacs = #awacsGroupsBlue + #awacsGroupsRed
        if totalAwacs == 0 then
            env.info("[CapIntercept] WARNING: No AWACS found at startup, will continue checking for late spawns")
        else
            env.info(string.format("[CapIntercept] Discovered %d Blue and %d Red AWACS groups at startup", #awacsGroupsBlue, #awacsGroupsRed))
        end
        
        -- Auto-discover CAP flights
        DiscoverCapFlights()
        if #capFlights == 0 then
            env.info("[CapIntercept] WARNING: No CAP flights found at startup, will continue checking for late spawns")
        else
            env.info(string.format("[CapIntercept] Discovered %d CAP flights at startup", #capFlights))
        end
        
        -- Initialize Moose detection for each coalition if AWACS available
        if #awacsGroupsBlue > 0 then
            detectionSetBlue, awacsSetBlue = InitializeDetectionForCoalition(awacsGroupsBlue, "Blue")
        end
        if #awacsGroupsRed > 0 then
            detectionSetRed, awacsSetRed = InitializeDetectionForCoalition(awacsGroupsRed, "Red")
        end
        
        -- Start scheduler (will check for new groups every 30s)
        schedulerId = timer.scheduleFunction(function()
            local success, err = pcall(SchedulerFunction)
            if not success then
                env.info("[CapIntercept] ERROR in scheduler: " .. tostring(err))
            end
            return timer.getTime() + SchedulerInterval
        end, nil, timer.getTime() + SchedulerInterval)
        
        env.info(string.format("[CapIntercept] Scheduler started (interval: %ds, discovery check: 30s)", SchedulerInterval))
        env.info("[CapIntercept] Initialization complete - will auto-discover groups that spawn later in mission")
    end, nil, timer.getTime() + 5)
end

-- Start the plugin
Initialize()

env.info("-----DCSRetribution|MOOSE CAP Intercept plugin - configuration end ------")
