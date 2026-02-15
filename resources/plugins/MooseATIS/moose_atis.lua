env.info("-----DCSRetribution|Moose ATIS plugin - configuration start ------")

MooseATISOptions = {
    enableBlue = true,
    enableRed = false,
    includeFarps = false,
    blueFrequency = 251,
    redFrequency = 124,
    useFM = false,
    useDcsAirbaseAtcFrequencies = true,
    setMetricUnits = false,
    transmitOnlyWithPlayers = true,
    setMapMarks = false,
    reportRunwayLength = false,
    reportElevation = false,
    srsPort = 5002,
    queueUpdateSeconds = 90,
    startDelaySeconds = 3,
    debug = false,
}

if dcsRetribution and dcsRetribution.plugins and dcsRetribution.plugins.MooseATIS then
    local p = dcsRetribution.plugins.MooseATIS
    MooseATISOptions.enableBlue = p.enableBlue
    MooseATISOptions.enableRed = p.enableRed
    MooseATISOptions.includeFarps = p.includeFarps
    MooseATISOptions.blueFrequency = p.blueFrequency
    MooseATISOptions.redFrequency = p.redFrequency
    MooseATISOptions.useFM = p.useFM
    MooseATISOptions.useDcsAirbaseAtcFrequencies = p.useDcsAirbaseAtcFrequencies
    MooseATISOptions.setMetricUnits = p.setMetricUnits
    MooseATISOptions.transmitOnlyWithPlayers = p.transmitOnlyWithPlayers
    MooseATISOptions.setMapMarks = p.setMapMarks
    MooseATISOptions.reportRunwayLength = p.reportRunwayLength
    MooseATISOptions.reportElevation = p.reportElevation
    MooseATISOptions.srsPort = p.srsPort
    MooseATISOptions.queueUpdateSeconds = p.queueUpdateSeconds
    MooseATISOptions.startDelaySeconds = p.startDelaySeconds
    MooseATISOptions.debug = p.debug
else
    env.info("-----dcsRetribution.plugins.MooseATIS NOT FOUND; using defaults")
end

local MOD_AM = (radio and radio.modulation and radio.modulation.AM) or 0
local MOD_FM = (radio and radio.modulation and radio.modulation.FM) or 1
local fallback_modulation = MooseATISOptions.useFM and MOD_FM or MOD_AM

local function modulation_name(mod)
    if mod == MOD_FM then
        return "FM"
    end
    return "AM"
end

local function hz_to_mhz(hz)
    local n = tonumber(hz)
    if not n or n <= 0 then
        return nil
    end
    return n / 1000000.0
end

local function get_modulation_for_band(band)
    if band == "atc_vhf_low_hz" or band == "atc_hf_hz" then
        return MOD_FM
    end
    return MOD_AM
end

local airbase_data_by_name = {}
if dcsRetribution and dcsRetribution.Airbases then
    for _, data in pairs(dcsRetribution.Airbases) do
        if data.name then
            airbase_data_by_name[data.name] = data
        end
    end
end

MooseATISInstances = MooseATISInstances or {}

local function atis_log(message)
    env.info("[MooseATIS] " .. tostring(message))
end

local function atis_debug(message)
    if MooseATISOptions.debug then
        atis_log(message)
    end
end

local function coalition_name(coalition_id)
    if coalition_id == coalition.side.BLUE then
        return "blue"
    elseif coalition_id == coalition.side.RED then
        return "red"
    elseif coalition_id == coalition.side.NEUTRAL then
        return "neutral"
    end
    return "unknown"
end

local function should_create_atis(airbase)
    local category = airbase:GetAirbaseCategory()
    if category == Airbase.Category.SHIP then
        return false
    end

    if category == Airbase.Category.HELIPAD and not MooseATISOptions.includeFarps then
        return false
    end

    local airbase_coalition = airbase:GetCoalition()
    if airbase_coalition == coalition.side.BLUE then
        return MooseATISOptions.enableBlue
    elseif airbase_coalition == coalition.side.RED then
        return MooseATISOptions.enableRed
    end

    return false
end

local function get_frequency_for_airbase(airbase)
    local airbase_name = airbase:GetName()

    if MooseATISOptions.useDcsAirbaseAtcFrequencies then
        local data = airbase_data_by_name[airbase_name]
        if data then
            local ordered_fields = {
                "atc_uhf_hz",
                "atc_vhf_high_hz",
                "atc_vhf_low_hz",
                "atc_hf_hz",
            }
            for _, field_name in ipairs(ordered_fields) do
                local mhz = hz_to_mhz(data[field_name])
                if mhz then
                    return mhz, get_modulation_for_band(field_name), "dcs." .. field_name
                end
            end
            atis_debug(string.format("No usable DCS ATC frequency for %s", airbase_name))
        else
            atis_debug(string.format("No DCS airbase data exported for %s", airbase_name))
        end
    end

    local airbase_coalition = airbase:GetCoalition()
    if airbase_coalition == coalition.side.BLUE then
        return tonumber(MooseATISOptions.blueFrequency), fallback_modulation, "fallback.blue"
    elseif airbase_coalition == coalition.side.RED then
        return tonumber(MooseATISOptions.redFrequency), fallback_modulation, "fallback.red"
    end
    return nil, nil, "none"
end

local function configure_atis(atis)
    if MooseATISOptions.setMetricUnits then
        atis:SetMetricUnits()
    end

    atis:SetTransmitOnlyWithPlayers(MooseATISOptions.transmitOnlyWithPlayers)

    if MooseATISOptions.setMapMarks then
        atis:SetMapMarks(true)
    end

    if MooseATISOptions.reportRunwayLength then
        atis:SetRunwayLength()
    end

    if MooseATISOptions.reportElevation then
        atis:SetElevation()
    end

    if MooseATISOptions.queueUpdateSeconds and MooseATISOptions.queueUpdateSeconds > 0 then
        atis:SetQueueUpdateTime(MooseATISOptions.queueUpdateSeconds)
    end

    atis:SetSRS("", nil, nil, nil, MooseATISOptions.srsPort)
end

local function _runway_or_nil(value)
    if value == nil then
        return nil
    end
    local text = tostring(value)
    if text == "" then
        return nil
    end
    return text
end

local function _add_frequency_runway_list(list_data, add_fn, value_key)
    if type(list_data) ~= "table" then
        return
    end
    for _, entry in pairs(list_data) do
        local value = tonumber(entry[value_key])
        if value then
            add_fn(value, _runway_or_nil(entry.runway))
        end
    end
end

local function configure_atis_navaids(atis, airbase_name)
    local data = airbase_data_by_name[airbase_name]
    if not data then
        return
    end

    local tacan_channel = tonumber(data.tacan_channel)
    if tacan_channel then
        atis:SetTACAN(tacan_channel)
    end

    local vor_mhz = tonumber(data.vor_mhz)
    if vor_mhz then
        atis:SetVOR(vor_mhz)
    end

    local rsbn_channel = tonumber(data.rsbn_channel)
    if rsbn_channel then
        atis:SetRSBN(rsbn_channel)
    end

    _add_frequency_runway_list(data.ils, function(frequency, runway)
        atis:AddILS(frequency, runway)
    end, "frequency_mhz")

    _add_frequency_runway_list(data.ndb_outer, function(frequency, runway)
        atis:AddNDBouter(frequency, runway)
    end, "frequency_khz")

    _add_frequency_runway_list(data.ndb_inner, function(frequency, runway)
        atis:AddNDBinner(frequency, runway)
    end, "frequency_khz")

    _add_frequency_runway_list(data.prmg, function(channel, runway)
        atis:AddPRMG(channel, runway)
    end, "channel")
end

local function create_atis_for_airbase(airbase)
    local airbase_name = airbase:GetName()
    local frequency, modulation, source = get_frequency_for_airbase(airbase)

    if not frequency then
        atis_debug(string.format("Skipping %s: no frequency for coalition %s", airbase_name, coalition_name(airbase:GetCoalition())))
        return
    end

    local atis = ATIS:New(airbase_name, frequency, modulation)
    if not atis then
        atis_log(string.format("Failed to create ATIS for %s", airbase_name))
        return
    end

    configure_atis(atis)
    configure_atis_navaids(atis, airbase_name)
    atis:__Start(MooseATISOptions.startDelaySeconds or 0)

    MooseATISInstances[airbase_name] = atis

    atis_log(string.format(
        "Started ATIS for %s (coalition=%s, freq=%.3f, modulation=%s, source=%s)",
        airbase_name,
        coalition_name(airbase:GetCoalition()),
        tonumber(frequency) or 0,
        modulation_name(modulation),
        source
    ))
end

local function start_moose_atis()
    local all_airbases = AIRBASE.GetAllAirbases()
    local count = 0

    for _, airbase in pairs(all_airbases) do
        if should_create_atis(airbase) then
            create_atis_for_airbase(airbase)
            count = count + 1
        else
            atis_debug(string.format(
                "Skipped %s (coalition=%s, category=%s)",
                airbase:GetName(),
                coalition_name(airbase:GetCoalition()),
                tostring(airbase:GetAirbaseCategory())
            ))
        end
    end

    atis_log(string.format("Moose ATIS startup complete (%d instance(s) created)", count))
end

start_moose_atis()
