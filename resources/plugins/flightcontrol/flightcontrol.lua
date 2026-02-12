env.info("-----DCSRetribution|MOOSE FlightControl plugin - configuration start ------")

flightcontrol_options = {
    enableBlue = true,
    enableRed = false,
    useDcsAirbaseAtcFrequencies = true,
    blueFrequency = 251,
    redFrequency = 124,
    useFM = false,
    limitLanding = 2,
    limitLandingTakeoff = 0,
    landingIntervalSeconds = 180,
    limitTaxi = 2,
    taxiIncludeInbound = false,
    limitTaxiLanding = 0,
    taxiSpeedLimitKnots = 25,
    runwayRepairSeconds = 3600,
    markHoldingPatterns = true,
    radioOnlyIfPlayers = true,
    subtitles = true,
    disableDcsAtc = true,
    verbosity = 0,
}

if dcsRetribution and dcsRetribution.plugins and dcsRetribution.plugins.flightcontrol then
    local p = dcsRetribution.plugins.flightcontrol
    flightcontrol_options.enableBlue = p.enableBlue
    flightcontrol_options.enableRed = p.enableRed
    flightcontrol_options.useDcsAirbaseAtcFrequencies = p.useDcsAirbaseAtcFrequencies
    flightcontrol_options.blueFrequency = p.blueFrequency
    flightcontrol_options.redFrequency = p.redFrequency
    flightcontrol_options.useFM = p.useFM
    flightcontrol_options.limitLanding = p.limitLanding
    flightcontrol_options.limitLandingTakeoff = p.limitLandingTakeoff
    flightcontrol_options.landingIntervalSeconds = p.landingIntervalSeconds
    flightcontrol_options.limitTaxi = p.limitTaxi
    flightcontrol_options.taxiIncludeInbound = p.taxiIncludeInbound
    flightcontrol_options.limitTaxiLanding = p.limitTaxiLanding
    flightcontrol_options.taxiSpeedLimitKnots = p.taxiSpeedLimitKnots
    flightcontrol_options.runwayRepairSeconds = p.runwayRepairSeconds
    flightcontrol_options.markHoldingPatterns = p.markHoldingPatterns
    flightcontrol_options.radioOnlyIfPlayers = p.radioOnlyIfPlayers
    flightcontrol_options.subtitles = p.subtitles
    flightcontrol_options.disableDcsAtc = p.disableDcsAtc
    flightcontrol_options.verbosity = p.verbosity
else
    env.info("DCSRetribution|FlightControl plugin - settings block not found, using defaults")
end

local function _fc_coalition_enabled(side)
    if side == "blue" then
        return flightcontrol_options.enableBlue
    end
    if side == "red" then
        return flightcontrol_options.enableRed
    end
    return false
end

local function _fc_frequency_for_side(side)
    if side == "red" then
        return flightcontrol_options.redFrequency
    end
    return flightcontrol_options.blueFrequency
end

local function _fc_hz_to_mhz(hz)
    local f = tonumber(hz)
    if not f then
        return nil
    end
    return f / 1000000
end

local function _fc_modulation()
    if flightcontrol_options.useFM then
        return radio.modulation.FM
    end
    return radio.modulation.AM
end

local function _fc_pick_airbase_radio(airbase, side)
    if not flightcontrol_options.useDcsAirbaseAtcFrequencies then
        return _fc_frequency_for_side(side), _fc_modulation(), "fallback"
    end

    local mapping_rule = {
        { key = "atc_uhf_hz", label = "UHF" },
        { key = "atc_vhf_high_hz", label = "VHF-HIGH" },
        { key = "atc_vhf_low_hz", label = "VHF-LOW" },
        { key = "atc_hf_hz", label = "HF" },
    }

    for _, candidate in ipairs(mapping_rule) do
        local mhz = _fc_hz_to_mhz(airbase[candidate.key])
        if mhz then
            return mhz, radio.modulation.AM, candidate.label
        end
    end

    return _fc_frequency_for_side(side), _fc_modulation(), "fallback"
end

local function _fc_apply_common_options(fc)
    fc:SetLimitLanding(flightcontrol_options.limitLanding, flightcontrol_options.limitLandingTakeoff)
    fc:SetLandingInterval(flightcontrol_options.landingIntervalSeconds)
    fc:SetLimitTaxi(
        flightcontrol_options.limitTaxi,
        flightcontrol_options.taxiIncludeInbound,
        flightcontrol_options.limitTaxiLanding
    )
    fc:SetRunwayRepairtime(flightcontrol_options.runwayRepairSeconds)
    fc:SetMarkHoldingPattern(flightcontrol_options.markHoldingPatterns)
    fc:SetRadioOnlyIfPlayers(flightcontrol_options.radioOnlyIfPlayers)

    if flightcontrol_options.subtitles then
        fc:SwitchSubtitlesOn()
    else
        fc:SwitchSubtitlesOff()
    end

    if flightcontrol_options.taxiSpeedLimitKnots and flightcontrol_options.taxiSpeedLimitKnots > 0 then
        fc:SetSpeedLimitTaxi(flightcontrol_options.taxiSpeedLimitKnots)
    else
        fc:SetSpeedLimitTaxi(nil)
    end

    fc:SetVerbosity(flightcontrol_options.verbosity)
end

-- Hook for advanced mission-side customization.
-- If defined elsewhere, this receives every created FLIGHTCONTROL instance and
-- can use the full FLIGHTCONTROL API (holding patterns, parking guards, SRS voices, etc.).
--
-- function FlightControlRetributionConfigure(fc, airbaseName, side)
--     fc:AddHoldingPattern("Batumi Hold Alpha", 320, 15, 6, 12, 10)
-- end

FlightControlRetributionControllers = FlightControlRetributionControllers or {}

local function _fc_configure_airbase(airbase)
    local airbaseName = airbase.name
    local side = airbase.side
    local frequency, modulation, source = _fc_pick_airbase_radio(airbase, side)

    local fc = FLIGHTCONTROL:New(airbaseName, frequency, modulation)
    if not fc then
        env.info("DCSRetribution|FlightControl plugin - failed to create FLIGHTCONTROL for " .. tostring(airbaseName))
        return nil
    end

    _fc_apply_common_options(fc)

    if flightcontrol_options.disableDcsAtc and fc.airbase and fc.airbase.SetRadioSilentMode then
        fc.airbase:SetRadioSilentMode(true)
    end

    if FlightControlRetributionConfigure then
        local ok, err = pcall(FlightControlRetributionConfigure, fc, airbaseName, side)
        if not ok then
            env.info(
                "DCSRetribution|FlightControl plugin - FlightControlRetributionConfigure error for "
                    .. tostring(airbaseName)
                    .. ": "
                    .. tostring(err)
            )
        end
    end

    fc:Start()
    FlightControlRetributionControllers[airbaseName] = fc

    env.info(
        string.format(
            "DCSRetribution|FlightControl plugin - started at %s (side=%s, %.3f MHz %s, source=%s)",
            tostring(airbaseName),
            tostring(side),
            tonumber(frequency) or 0,
            modulation == radio.modulation.FM and "FM" or "AM",
            tostring(source)
        )
    )

    return fc
end

local function _fc_setup_from_retribution_data()
    local configured = 0

    if not dcsRetribution or not dcsRetribution.Airbases then
        env.info("DCSRetribution|FlightControl plugin - dcsRetribution.Airbases missing")
        return 0
    end

    for _, airbase in pairs(dcsRetribution.Airbases) do
        local name = airbase.name
        local side = airbase.side

        if name and side and _fc_coalition_enabled(side) then
            if not FlightControlRetributionControllers[name] then
                local fc = _fc_configure_airbase(airbase)
                if fc then
                    configured = configured + 1
                end
            end
        end
    end

    return configured
end

local configuredCount = _fc_setup_from_retribution_data()
env.info("DCSRetribution|FlightControl plugin - configured airbases: " .. tostring(configuredCount))

env.info("-----DCSRetribution|MOOSE FlightControl plugin - configuration complete ------")
