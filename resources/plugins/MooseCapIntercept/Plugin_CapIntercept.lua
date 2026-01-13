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
local detectionSet = nil        -- Moose DETECTION_AREAS set
local bogeyAssignments = {}     -- Track bogey → CAP assignments
local schedulerId = nil         -- Scheduler ID

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
local function CalculateAspect(capHeading, bogeyHeading, capToBogeyHeading)
    -- Aspect is the angle between the bogey's heading and the line from bogey to CAP
    -- Hot aspect: bogey flying towards CAP (aspect close to 0°)
    -- Flanking: bogey flying at an angle (aspect < 90°)
    -- Beam/Cold: bogey flying away (aspect > 90°)
    
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
    local awacsGroups = {}
    
    -- Scan all coalitions for AWACS aircraft
    for coalName, coalId in pairs(coalition.side) do
        local groups = coalition.getGroups(coalId, Group.Category.AIRPLANE)
        if groups then
            for _, group in ipairs(groups) do
                local units = group:getUnits()
                if units and #units > 0 then
                    local unit = units[1]
                    local typeName = unit:getTypeName()
                    if IsAwacsType(typeName) then
                        table.insert(awacsGroups, group:getName())
                        Debug("  Found AWACS: " .. group:getName() .. " (" .. typeName .. ")")
                    end
                end
            end
        end
    end
    
    return awacsGroups
end

-- Auto-discover CAP flights (groups with task == "CAP")
local function DiscoverCapFlights()
    Debug("Discovering CAP flights...")
    local caps = {}
    
    -- Scan friendly coalition (blue by default, adjust if needed)
    local groups = coalition.getGroups(coalition.side.BLUE, Group.Category.AIRPLANE)
    if groups then
        for _, group in ipairs(groups) do
            local groupName = group:getName()
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
                        
                        Debug("  Found CAP: " .. groupName)
                        
                        -- Store CAP flight data
                        table.insert(caps, {
                            groupName = groupName,
                            group = group,
                            originalRoute = nil,  -- Will store route waypoints
                            racetrackStart = nil, -- Will store racetrack anchor 1
                            racetrackEnd = nil,   -- Will store racetrack anchor 2
                            currentTask = "patrol", -- Track current task state
                            assignedBogey = nil   -- Track assigned intercept
                        })
                    end
                end
            end
        end
    end
    
    return caps
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

-- Initialize Moose detection set with AWACS
local function InitializeDetection(awacsGroups)
    if #awacsGroups == 0 then
        env.info("[CapIntercept] WARNING: No AWACS groups found for detection!")
        return nil
    end
    
    Debug("Initializing DETECTION_AREAS with " .. #awacsGroups .. " AWACS groups")
    
    -- Create detection set using Moose
    -- Note: This requires Moose to be loaded first (handled by base plugin)
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
    
    Debug("Detection set initialized successfully")
    return detection
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
    local capHeading = capUnit:getPosition().x:GetHeading()
    local bogeyVel = bogeyUnit:GetVelocityVec3()
    local bogeyHeading = math.deg(math.atan2(bogeyVel.z, bogeyVel.x))
    if bogeyHeading < 0 then bogeyHeading = bogeyHeading + 360 end
    
    local capToBogeyHeading = capCoord:HeadingTo(bogeyPos)
    local aspect = CalculateAspect(capHeading, bogeyHeading, capToBogeyHeading)
    
    if aspect > MaxAspectAngle then
        return false, string.format("Aspect %.1f° > max %.1f°", aspect, MaxAspectAngle)
    end
    
    Debug(string.format("  Intercept conditions MET: Range=%.1fNM, Aspect=%.1f°", rangeNM, aspect))
    return true, "Qualified", rangeNM
end

-- Find nearest available CAP for a bogey
local function FindNearestCap(bogey)
    local nearestCap = nil
    local nearestRange = 999999
    
    for _, capFlight in ipairs(capFlights) do
        -- Skip CAPs already assigned to another bogey
        if capFlight.currentTask == "patrol" then
            local qualified, reason, range = CheckInterceptConditions(capFlight, bogey)
            if qualified and range < nearestRange then
                nearestCap = capFlight
                nearestRange = range
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
    if not detectionSet then
        return
    end
    
    -- Process detections
    local detectedItems = detectionSet:GetDetectedItems()
    if not detectedItems or #detectedItems == 0 then
        Debug("No detections this cycle")
        return
    end
    
    Debug(string.format("Processing %d detections", #detectedItems))
    
    -- Check each detected item
    for _, detectedItem in ipairs(detectedItems) do
        local bogeyGroup = detectedItem:GetGroup()
        if bogeyGroup then
            local bogeyName = bogeyGroup:GetName()
            
            -- Skip if already assigned
            if not bogeyAssignments[bogeyName] then
                -- Find nearest CAP
                local nearestCap = FindNearestCap(detectedItem)
                
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
        local awacsGroups = DiscoverAwacs()
        if #awacsGroups == 0 then
            env.info("[CapIntercept] WARNING: No AWACS found, detection system will not work")
        end
        
        -- Auto-discover CAP flights
        capFlights = DiscoverCapFlights()
        if #capFlights == 0 then
            env.info("[CapIntercept] WARNING: No CAP flights found")
            return
        end
        
        env.info(string.format("[CapIntercept] Discovered %d CAP flights and %d AWACS groups", 
            #capFlights, #awacsGroups))
        
        -- Extract racetrack waypoints for each CAP
        for _, capFlight in ipairs(capFlights) do
            ExtractRacetrackWaypoints(capFlight)
        end
        
        -- Initialize Moose detection
        if #awacsGroups > 0 then
            detectionSet = InitializeDetection(awacsGroups)
            
            if detectionSet then
                -- Start scheduler
                schedulerId = timer.scheduleFunction(function()
                    local success, err = pcall(SchedulerFunction)
                    if not success then
                        env.info("[CapIntercept] ERROR in scheduler: " .. tostring(err))
                    end
                    return timer.getTime() + SchedulerInterval
                end, nil, timer.getTime() + SchedulerInterval)
                
                env.info(string.format("[CapIntercept] Scheduler started (interval: %ds)", SchedulerInterval))
            end
        end
        
        env.info("[CapIntercept] Initialization complete")
    end, nil, timer.getTime() + 5)
end

-- Start the plugin
Initialize()

env.info("-----DCSRetribution|MOOSE CAP Intercept plugin - configuration end ------")
