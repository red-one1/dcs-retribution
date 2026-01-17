-- Skynet IADS expose loader
-- Captures SkynetIADS instances to dcsRetribution.skynetIADS without modifying Skynet code.

if SkynetIADS and not _SkynetIADSExposeInstalled then
    env.info("DCSRetribution|Skynet-IADS expose - installing hooks")
    local originalCreate = SkynetIADS.create
    local originalSetCoalition = SkynetIADS.setCoalition

    SkynetIADS.create = function(self, name)
        local iads = originalCreate(self, name)
        if dcsRetribution then
            dcsRetribution.skynetIADS = dcsRetribution.skynetIADS or {}
            dcsRetribution.skynetIADS._all = dcsRetribution.skynetIADS._all or {}
            table.insert(dcsRetribution.skynetIADS._all, iads)
            env.info("DCSRetribution|Skynet-IADS expose - IADS instance created")
        end
        return iads
    end

    SkynetIADS.setCoalition = function(self, item)
        originalSetCoalition(self, item)
        if dcsRetribution and self.getCoalition then
            local coalitionId = self:getCoalition()
            if coalitionId == coalition.side.RED then
                dcsRetribution.skynetIADS = dcsRetribution.skynetIADS or {}
                dcsRetribution.skynetIADS.red = self
                env.info("DCSRetribution|Skynet-IADS expose - registered RED IADS")
            elseif coalitionId == coalition.side.BLUE then
                dcsRetribution.skynetIADS = dcsRetribution.skynetIADS or {}
                dcsRetribution.skynetIADS.blue = self
                env.info("DCSRetribution|Skynet-IADS expose - registered BLUE IADS")
            end
        end
    end

    _SkynetIADSExposeInstalled = true
elseif not SkynetIADS then
    env.info("DCSRetribution|Skynet-IADS expose - SkynetIADS not loaded yet")
end
