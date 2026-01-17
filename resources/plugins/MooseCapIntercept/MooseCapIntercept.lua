local MOOSE_CAP_INTERCEPT_VERSION = "2026-01-17o"
env.info("-----DCSRetribution|MOOSE CAP Intercept plugin - configuration start (v" .. MOOSE_CAP_INTERCEPT_VERSION .. ") ------")

-- Defaults (overridden by dcsRetribution.plugins.MooseCapIntercept when present)
local NM_TO_M = 1852
MooseCapInterceptDebug              = false
MooseCapInterceptDebugToCoalition   = false
DetectionGroupingRadiusNM           = 16
DetectionAcceptRangeNM              = 108
CapInterceptRangeNM                 = 32
DetectionGroupingRadiusM            = DetectionGroupingRadiusNM * NM_TO_M
DetectionAcceptRangeM               = DetectionAcceptRangeNM * NM_TO_M
CapInterceptRangeM                  = CapInterceptRangeNM * NM_TO_M
HotAspectDeg                        = 35
FlankAspectMinDeg                   = 60
FlankAspectMaxDeg                   = 120
InterceptCooldownSec                = 60
InterceptMaxDurationSec             = 180
SchedulerIntervalSec                = 5

local __MooseCapInterceptConfigured = false
local __MooseCapInterceptNeedsRebuild = false
local blueState
local redState

local DebugLog
local LogConfig
local RebuildCoalition

DebugLog = function(message, coalitionName)
    if MooseCapInterceptDebug then
        env.info("[MooseCapIntercept] " .. message)
    end
    if MooseCapInterceptDebugToCoalition and MESSAGE and coalitionName then
        local coalitionId = (coalitionName == "blue") and coalition.side.BLUE or coalition.side.RED
        MESSAGE:New("[MooseCapIntercept] " .. message, 10, "C2", false):ToCoalition(coalitionId)
    end
end

LogConfig = function()
    env.info("--------- MooseCapInterceptDebug=" .. tostring(MooseCapInterceptDebug) ..
        " | DebugToCoalition=" .. tostring(MooseCapInterceptDebugToCoalition) ..
        " | DetectionGroupingRadiusNM=" .. tostring(DetectionGroupingRadiusNM) ..
        " | DetectionAcceptRangeNM=" .. tostring(DetectionAcceptRangeNM) ..
        " | CapInterceptRangeNM=" .. tostring(CapInterceptRangeNM) ..
        " | HotAspectDeg=" .. tostring(HotAspectDeg) ..
        " | FlankAspectMinDeg=" .. tostring(FlankAspectMinDeg) ..
        " | FlankAspectMaxDeg=" .. tostring(FlankAspectMaxDeg) ..
        " | InterceptCooldownSec=" .. tostring(InterceptCooldownSec) ..
        " | InterceptMaxDurationSec=" .. tostring(InterceptMaxDurationSec) ..
        " | SchedulerIntervalSec=" .. tostring(SchedulerIntervalSec)
    )
end

local function ApplyConfigFromUI()
    if dcsRetribution and dcsRetribution.plugins and dcsRetribution.plugins.MooseCapIntercept then
        local p                         = dcsRetribution.plugins.MooseCapIntercept
        MooseCapInterceptDebug          = p.MooseCapInterceptDebug
        MooseCapInterceptDebugToCoalition = p.MooseCapInterceptDebugToCoalition
        DetectionGroupingRadiusNM       = p.DetectionGroupingRadius
        DetectionAcceptRangeNM          = p.DetectionAcceptRange
        CapInterceptRangeNM             = p.CapInterceptRange
        HotAspectDeg                    = p.HotAspectDeg
        FlankAspectMinDeg               = p.FlankAspectMinDeg
        FlankAspectMaxDeg               = p.FlankAspectMaxDeg
        InterceptCooldownSec            = p.InterceptCooldownSec
        InterceptMaxDurationSec         = p.InterceptMaxDurationSec
        SchedulerIntervalSec            = p.SchedulerIntervalSec
        __MooseCapInterceptConfigured = true
    else
        env.info("-----dcsRetribution.plugins.MooseCapIntercept NOT FOUND")
    end

    DetectionGroupingRadiusM = DetectionGroupingRadiusNM * NM_TO_M
    DetectionAcceptRangeM = DetectionAcceptRangeNM * NM_TO_M
    CapInterceptRangeM = CapInterceptRangeNM * NM_TO_M

    LogConfig()
    if __MooseCapInterceptConfigured then
        __MooseCapInterceptNeedsRebuild = true
    end

    return __MooseCapInterceptConfigured
end

-- Pull from UI if available; if not, retry after 2 seconds.
if not ApplyConfigFromUI() then
    if timer and timer.scheduleFunction then
        timer.scheduleFunction(function()
            if not __MooseCapInterceptConfigured then
                env.info("[MooseCapIntercept] Retrying config load...")
                ApplyConfigFromUI()
            end
        end, {}, timer.getTime() + 2)
    end
end

-- Configure your name filters here if needed (string options are not supported in plugin UI)
-- Retribution group naming embeds flight type in the name (e.g., "Target TARCAP|...") or uses
-- support prefixes like "awacs|". Pretense uses "<cp>-<flight type>-<n>".
local BLUE_CAP_PATTERNS   = { "tarcap", "barcap", "intercept", "fighter sweep", "escort" }
local RED_CAP_PATTERNS    = { "tarcap", "barcap", "intercept", "fighter sweep", "escort" }
local BLUE_AWACS_PATTERNS = { "awacs|", "aew&c", "aewc" }
local RED_AWACS_PATTERNS  = { "awacs|", "aew&c", "aewc" }


local function Clamp(value, min, max)
    if value < min then return min end
    if value > max then return max end
    return value
end

local function HasValidDcsObject(obj)
    if not obj then return false end
    if obj.GetDCSObject then
        local dcs = obj:GetDCSObject()
        if not dcs then return false end
        if dcs.isExist and not dcs:isExist() then return false end
    end
    return true
end

local function SafeGetCoordinate(obj)
    if not HasValidDcsObject(obj) then return nil end
    return obj:GetCoordinate()
end

local function SafeGetHeading(obj)
    if not HasValidDcsObject(obj) then return nil end
    return obj:GetHeading()
end

local function AngleBetween(vec1, vec2)
    local dot = vec1.x * vec2.x + vec1.y * vec2.y
    local mag1 = math.sqrt(vec1.x * vec1.x + vec1.y * vec1.y)
    local mag2 = math.sqrt(vec2.x * vec2.x + vec2.y * vec2.y)
    if mag1 == 0 or mag2 == 0 then return 180 end
    local cos = Clamp(dot / (mag1 * mag2), -1, 1)
    return math.deg(math.acos(cos))
end

local function HeadingVector(unit)
    local heading = SafeGetHeading(unit)
    if not heading then return nil end
    return { x = math.sin(heading), y = math.cos(heading) }
end

local function VectorTo(fromCoord, toCoord)
    local fromVec2 = fromCoord:GetVec2()
    local toVec2 = toCoord:GetVec2()
    return { x = toVec2.x - fromVec2.x, y = toVec2.y - fromVec2.y }
end

local function IsHotOrFlanking(targetUnit, friendlyGroup)
    if not targetUnit or not friendlyGroup then return false, 180 end
    local targetCoord = SafeGetCoordinate(targetUnit)
    local friendlyCoord = SafeGetCoordinate(friendlyGroup)
    if not targetCoord or not friendlyCoord then return false, 180 end

    local targetHeadingVec = HeadingVector(targetUnit)
    if not targetHeadingVec then return false, 180 end
    local vectorToFriendly = VectorTo(targetCoord, friendlyCoord)
    local angle = AngleBetween(targetHeadingVec, vectorToFriendly)

    local isHot = angle <= HotAspectDeg
    local isFlank = angle >= FlankAspectMinDeg and angle <= FlankAspectMaxDeg
    return (isHot or isFlank), angle
end

local function GetDetectedAirGroups(detection)
    local groups = {}
    if not detection then return groups end

    local detectedItems = detection:GetDetectedItems() or {}
    for _, detectedItem in pairs(detectedItems) do
        local detectedSet = detection:GetDetectedItemSet(detectedItem)
        if detectedSet then
            detectedSet:ForEachUnit(function(unit)
                if unit and unit:IsAlive() then
                    local group = unit:GetGroup()
                    if group and group:IsAlive() then
                        groups[group:GetName()] = group
                    end
                end
            end)
        end
    end

    return groups
end

local function GetSkynetIADSForCoalition(coalitionName)
    if not dcsRetribution or not dcsRetribution.skynetIADS then return nil end
    if coalitionName == "blue" then
        return dcsRetribution.skynetIADS.blue
    end
    if coalitionName == "red" then
        return dcsRetribution.skynetIADS.red
    end
    return nil
end

local function GetDetectedAirGroupsFromSkynet(state)
    local groups = {}
    if not state or not state.iads or not state.iads.getContacts then return groups end

    local coalitionId = (state.coalition == "blue") and coalition.side.BLUE or coalition.side.RED
    local contacts = state.iads:getContacts() or {}
    for _, contact in ipairs(contacts) do
        if contact and contact.getDCSRepresentation then
            local unit = contact:getDCSRepresentation()
            if unit and unit.isExist and unit:isExist() and unit.getCategory then
                local unitCategory = unit:getCategory()
                if unitCategory == Unit.Category.AIRPLANE or unitCategory == Unit.Category.HELICOPTER then
                    if unit.getCoalition and unit:getCoalition() ~= coalitionId then
                        local dcsGroup = unit:getGroup()
                        if dcsGroup then
                            local name = dcsGroup:getName()
                            local mooseGroup = GROUP and GROUP:FindByName(name) or nil
                            if mooseGroup and mooseGroup:IsAlive() then
                                groups[name] = mooseGroup
                            end
                        end
                    end
                end
            end
        end
    end

    return groups
end

local function GetDetectedEnemyGroups(state)
    if state and state.useSkynet then
        return GetDetectedAirGroupsFromSkynet(state)
    end
    return GetDetectedAirGroups(state and state.detection)
end

local function GetEnemyPlayerGroups(coalitionName)
    local groups = {}
    if not coalition or not coalition.getPlayers then return groups end

    local enemyId = (coalitionName == "blue") and coalition.side.RED or coalition.side.BLUE
    local players = coalition.getPlayers(enemyId) or {}
    for _, unit in ipairs(players) do
        if unit and unit.isExist and unit:isExist() then
            local dcsGroup = unit:getGroup()
            if dcsGroup then
                local name = dcsGroup:getName()
                local mooseGroup = GROUP and GROUP:FindByName(name) or nil
                if mooseGroup and mooseGroup:IsAlive() then
                    groups[name] = mooseGroup
                end
            end
        end
    end

    return groups
end

local function CountMapEntries(map)
    local count = 0
    for _ in pairs(map or {}) do
        count = count + 1
    end
    return count
end

local function GetGroupLogName(group)
    if not group then return "(nil)" end
    local groupName = (group.GetName and group:GetName()) or "(unknown group)"
    local unitName = nil
    if group.GetUnit then
        local unit = group:GetUnit(1)
        if unit and unit.GetName then
            unitName = unit:GetName()
        end
    end
    if unitName and unitName ~= groupName then
        return groupName .. " | " .. unitName
    end
    return groupName
end

local function NameMatchesAny(name, patterns)
    if not name then return false end
    local lowered = string.lower(name)
    for _, pattern in ipairs(patterns or {}) do
        if pattern and string.find(lowered, string.lower(pattern), 1, true) then
            return true
        end
    end
    return false
end

local function BuildAwacsSet(coalitionName, patterns)
    local awacsSet = SET_GROUP:New():FilterCoalitions(coalitionName):FilterCategories("plane")
    if patterns and #patterns > 0 then
        awacsSet:FilterFunction(function(grp)
            return grp and NameMatchesAny(grp:GetName(), patterns)
        end)
    end
    awacsSet:FilterStart()
    return awacsSet
end

local function BuildCapSet(coalitionName, patterns)
    local capSet = SET_GROUP:New():FilterCoalitions(coalitionName):FilterCategories("plane")
    if patterns and #patterns > 0 then
        capSet:FilterFunction(function(grp)
            return grp and NameMatchesAny(grp:GetName(), patterns)
        end)
    end
    capSet:FilterStart()
    return capSet
end

local function DebugListGroups(setGroup, label, coalitionName)
    if not MooseCapInterceptDebug or not setGroup then return end
    local names = {}
    setGroup:ForEachGroup(function(grp)
        if grp and grp:IsAlive() then
            names[#names + 1] = grp:GetName()
        end
    end)
    DebugLog(label .. " groups: [" .. table.concat(names, ", ") .. "]", coalitionName)
end

local function SetupDetection(awacsSet, coalitionName)
    if not awacsSet or awacsSet:Count() == 0 then
        return nil
    end

    local detection = DETECTION_AREAS:New(awacsSet, DetectionGroupingRadiusM)
    detection:SetAcceptRange(DetectionAcceptRangeM)
    detection:FilterCategories({ Unit.Category.AIRPLANE, Unit.Category.HELICOPTER })
    detection:Start()
    return detection
end

local function EnsureRouteStored(state, group)
    local name = group:GetName()
    if not state.routes[name] then
        state.routes[name] = group:GetTaskRoute()
        DebugLog("Stored original route for " .. name, state.coalition)
    end
end

local function ResumeRouteIfPossible(state, group)
    if not group or not group:IsAlive() then return end

    local name = group:GetName()
    local route = state.routes[name]
    if route then
        group:SetTask(group:TaskRoute(route), 1)
        state.lastIntercept[name] = timer.getTime()
        DebugLog("CAP returning to previous route: " .. name, state.coalition)
    else
        DebugLog("CAP returning but no stored route for " .. name .. "; cannot resume.", state.coalition)
    end
end

local function ForceIntercept(state, capGroup, targetGroup)
    if not capGroup or not targetGroup then return end
    if not capGroup:IsAlive() or not targetGroup:IsAlive() then return end

    local capName = capGroup:GetName()
    if state.active[capName] then
        return
    end
    local targetName = targetGroup:GetName()
    local now = timer.getTime()
    local last = state.lastIntercept[capName] or 0
    if now - last < InterceptCooldownSec then
        return
    end

    EnsureRouteStored(state, capGroup)

    local attackTask = capGroup:TaskAttackGroup(targetGroup)
    capGroup:SetTask(attackTask, 1)

    state.active[capName] = {
        target = targetName,
        start = now,
    }
    state.lastIntercept[capName] = now

    DebugLog("CAP directed to intercept: " .. capName .. " -> " .. targetName, state.coalition)

    -- Safety resume after a max duration
    SCHEDULER:New(nil, function()
        local active = state.active[capName]
        if not active then return end
        if active.target ~= targetName then return end
        state.active[capName] = nil
        ResumeRouteIfPossible(state, capGroup)
    end, {}, InterceptMaxDurationSec)
end

local function ProcessCoalition(state)
    local coalitionName = state.coalition

    if not state.useSkynet then
        local iads = GetSkynetIADSForCoalition(coalitionName)
        if iads then
            state.iads = iads
            state.useSkynet = true
            if state.detection and state.detection.Stop then
                state.detection:Stop()
            end
            state.detection = nil
            state.tracked = {}
            DebugLog("Detection source switched to Skynet IADS.", coalitionName)
        end
    end

    if not state.useSkynet and not state.detection then
        return
    end

    local enemyGroups = GetDetectedEnemyGroups(state)
    local playerGroups = GetEnemyPlayerGroups(coalitionName)
    for name, group in pairs(playerGroups) do
        enemyGroups[name] = group
    end
    local capGroups = {}
    state.capSet:ForEachGroup(function(capGroup)
        if capGroup and capGroup:IsAlive() and not capGroup:IsPlayer() and HasValidDcsObject(capGroup) then
            capGroups[#capGroups + 1] = capGroup
        end
    end)

    local newTracked = {}
    for _, enemyGroup in pairs(enemyGroups) do
        if enemyGroup and enemyGroup:IsAlive() and HasValidDcsObject(enemyGroup) then
            local enemyName = enemyGroup:GetName()
            local enemyCount = enemyGroup:GetSize() or 0
            local enemyUnit = enemyGroup:GetUnit(1)
            local bestRange = nil
            local bestQualifies = false

            if enemyUnit then
                for _, capGroup in ipairs(capGroups) do
                    local capCoord = SafeGetCoordinate(capGroup)
                    local enemyCoord = SafeGetCoordinate(enemyGroup)
                    if capCoord and enemyCoord then
                        local dist = capCoord:Get2DDistance(enemyCoord)
                        local ok = IsHotOrFlanking(enemyUnit, capGroup)
                        if bestRange == nil or dist < bestRange then
                            bestRange = dist
                            bestQualifies = (dist <= CapInterceptRangeM) and ok
                        end
                    end
                end
            end

            newTracked[enemyName] = { count = enemyCount, qualifies = bestQualifies }

            local prior = state.tracked and state.tracked[enemyName]
            if not prior then
                DebugLog(string.format(
                    "New enemy tracked: %s (x%d) qualifies=%s",
                    GetGroupLogName(enemyGroup), enemyCount, tostring(bestQualifies)
                ), coalitionName)
            else
                if enemyCount > (prior.count or 0) then
                    DebugLog(string.format(
                        "New aircraft detected in %s: now x%d",
                        GetGroupLogName(enemyGroup), enemyCount
                    ), coalitionName)
                end
                if prior.qualifies ~= bestQualifies then
                    DebugLog(string.format(
                        "Qualification change for %s: %s -> %s",
                        GetGroupLogName(enemyGroup), tostring(prior.qualifies), tostring(bestQualifies)
                    ), coalitionName)
                end
            end
        end
    end

    state.tracked = newTracked

    state.capSet:ForEachGroup(function(capGroup)
        if not capGroup or not capGroup:IsAlive() then return end
        if capGroup:IsPlayer() then return end

        local capName = capGroup:GetName()
        local active = state.active[capName]

        -- If currently intercepting, check if target still valid
        if active then
            local targetGroup = GROUP:FindByName(active.target)
            if not targetGroup or not targetGroup:IsAlive() then
                state.active[capName] = nil
                ResumeRouteIfPossible(state, capGroup)
            else
                local capCoord = capGroup:GetCoordinate()
                local targetCoord = targetGroup:GetCoordinate()
                if capCoord and targetCoord then
                    local dist = capCoord:Get2DDistance(targetCoord)
                    if dist > CapInterceptRangeM * 1.5 then
                        state.active[capName] = nil
                        ResumeRouteIfPossible(state, capGroup)
                    end
                end
            end
            return
        end

        -- Not intercepting: look for valid targets
        for _, enemyGroup in pairs(enemyGroups) do
            if enemyGroup and enemyGroup:IsAlive() then
                local capCoord = SafeGetCoordinate(capGroup)
                local enemyCoord = SafeGetCoordinate(enemyGroup)
                if capCoord and enemyCoord then
                    local dist = capCoord:Get2DDistance(enemyCoord)
                    if dist <= CapInterceptRangeM then
                        local enemyUnit = enemyGroup:GetUnit(1)
                        if enemyUnit then
                            local ok = IsHotOrFlanking(enemyUnit, capGroup)
                            if ok then
                                ForceIntercept(state, capGroup, enemyGroup)
                                break
                            end
                        end
                    end
                end
            end
        end
    end)
end

local function InitCoalition(coalitionName, capPatterns, awacsPatterns)
    local capSet = BuildCapSet(coalitionName, capPatterns)
    local iads = GetSkynetIADSForCoalition(coalitionName)
    local detection = nil
    local useSkynet = false
    if iads then
        useSkynet = true
        DebugLog("Detection source: Skynet IADS.", coalitionName)
    else
        local awacsSet = BuildAwacsSet(coalitionName, awacsPatterns)
        detection = SetupDetection(awacsSet, coalitionName)
        DebugLog("Detection source: MOOSE AWACS/EWR.", coalitionName)
    end

    return {
        coalition = coalitionName,
        capSet = capSet,
        detection = detection,
        iads = iads,
        useSkynet = useSkynet,
        routes = {},
        active = {},
        lastIntercept = {},
        tracked = {},
        capPatterns = capPatterns,
        awacsPatterns = awacsPatterns,
    }
end

local function RebuildCoalition(state)
    if state.detection and state.detection.Stop then
        state.detection:Stop()
    end
    state.capSet = BuildCapSet(state.coalition, state.capPatterns)
    state.iads = GetSkynetIADSForCoalition(state.coalition)
    state.useSkynet = state.iads ~= nil
    if not state.useSkynet then
        local awacsSet = BuildAwacsSet(state.coalition, state.awacsPatterns)
        state.detection = SetupDetection(awacsSet, state.coalition)
        DebugLog("Detection source: MOOSE AWACS/EWR.", state.coalition)
    else
        state.detection = nil
        DebugLog("Detection source: Skynet IADS.", state.coalition)
    end
    state.tracked = {}
end

if not SET_GROUP or not DETECTION_AREAS or not SCHEDULER then
    env.info("[MooseCapIntercept] MOOSE not available; plugin disabled.")
    return
end

blueState = InitCoalition("blue", BLUE_CAP_PATTERNS, BLUE_AWACS_PATTERNS)
redState = InitCoalition("red", RED_CAP_PATTERNS, RED_AWACS_PATTERNS)

if __MooseCapInterceptNeedsRebuild and RebuildCoalition and blueState and redState then
    DebugLog("Rebuilding detection sets after config load.", "blue")
    RebuildCoalition(blueState)
    RebuildCoalition(redState)
    __MooseCapInterceptNeedsRebuild = false
end

SCHEDULER:New(nil, function()
    ProcessCoalition(blueState)
    ProcessCoalition(redState)
end, {}, 2, SchedulerIntervalSec)

env.info("-----DCSRetribution|MOOSE CAP Intercept plugin - started ------")
