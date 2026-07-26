from dcs.planes import (
    F_14B,
    F_14A_95_GR,
    F_14A_135_GR_Early,
    F_14A_135_GR,
)
from dcs.weapons_data import Weapons

from pydcs_extensions.pylon_injector import inject_pylon, eject_pylon
from pydcs_extensions.weapon_injector import inject_weapons


class WeaponsF14Modern:
    AGM_123_Skipper_II = {
        "clsid": "{BRU-32 AGM-123}",
        "name": "AGM-123 Skipper II",
        "weight": 639.38,
    }
    AGM_88_HARM = {
        "clsid": "{SHOULDER_AGM_88}",
        "name": "AGM-88 HARM",
        "weight": 422.001,
    }
    AIM_120A = {
        "clsid": "{AIM_120A}",
        "name": "AIM-120A",
        "weight": 157.85,
    }
    AIM_120A_2 = {
        "clsid": "{SHOULDER AIM-120A}",
        "name": "AIM-120A",
        "weight": 203.21,
    }
    AIM_120C = {
        "clsid": "{SHOULDER AIM-120C}",
        "name": "AIM-120C",
        "weight": 206.84,
    }
    AIM_174B = {
        "clsid": "{SHOULDER AIM_174B L}",
        "name": "AIM-174B",
        "weight": 810.74,
    }
    AIM_174B_2 = {
        "clsid": "{SHOULDER AIM_174B R}",
        "name": "AIM-174B",
        "weight": 810.74,
    }
    AIM_54C_ECCM_Sealed_Mk47 = {
        "clsid": "{AIM_54C_ECCM_Mk47}",
        "name": "AIM-54C+ ECCM/Sealed-Mk47",
        "weight": 464.5,
    }
    AIM_54C_ECCM_Sealed_Mk47_2 = {
        "clsid": "{SHOULDER AIM_54C_ECCM_Mk47 L}",
        "name": "AIM-54C+ ECCM/Sealed-Mk47",
        "weight": 509.86,
    }
    AIM_54C_ECCM_Sealed_Mk47_3 = {
        "clsid": "{SHOULDER AIM_54C_ECCM_Mk47 R}",
        "name": "AIM-54C+ ECCM/Sealed-Mk47",
        "weight": 509.86,
    }
    AMBER_Rack_with_2x_AIM_120C_AMRAAM = {
        "clsid": "{AMBER_SHOULDER_2xAIM_120C}",
        "name": "AMBER Rack with 2x AIM-120C AMRAAM",
        "weight": 472.961,
    }
    AMBER_Rack_with_2x_AIM_120C_AMRAAM_2 = {
        "clsid": "{BRU32_AMBER_2xAIM_120C}",
        "name": "AMBER Rack with 2x AIM-120C AMRAAM",
        "weight": 472.961,
    }
    BRU_32_with_AGM_84D_Harpoon_Anti_Ship_Missile = {
        "clsid": "{SHOULDER_AGM_84D}",
        "name": "BRU-32 with AGM-84D Harpoon Anti-Ship Missile",
        "weight": 597.38,
    }
    Empty_LAU_7_Pylon_with_Adapter = {
        "clsid": "{HB_F14_EMPTY_LAU-7_WITH_ADAPTER}",
        "name": "Empty LAU-7 Pylon with Adapter",
        "weight": 15,
    }
    Empty_LAU_92_Adapter_Pylon = {
        "clsid": "{HB_F14_EMPTY_LAU-92_ADAPTER}",
        "name": "Empty LAU-92 Adapter Pylon",
        "weight": 54.4,
    }
    Empty_Phoenix_Adapter_Pylon = {
        "clsid": "{HB_F14_EMPTY_PHOENIX_ADAPTER_L}",
        "name": "Empty Phoenix Adapter Pylon",
        "weight": 45.36,
    }
    Empty_Phoenix_Adapter_Pylon_2 = {
        "clsid": "{HB_F14_EMPTY_PHOENIX_ADAPTER_R}",
        "name": "Empty Phoenix Adapter Pylon",
        "weight": 45.36,
    }
    LAU_10_4_Laser_Guided_Zuni_Mk_71 = {
        "clsid": "{BRU3242_LGZ_LAU10}",
        "name": "LAU-10 - 4 Laser Guided Zuni Mk 71",
        "weight": 474.28,
    }
    LAU_115_with_2x_LAU_127_AIM_120A_AMRAAM = {
        "clsid": "{SHOULDER_2xAIM_120A}",
        "name": "LAU-115 with 2x LAU-127 AIM-120A AMRAAM",
        "weight": 460.701,
    }
    LAU_115_with_2x_LAU_127_AIM_120A_AMRAAM_2 = {
        "clsid": "{BRU32_2xAIM_120A}",
        "name": "LAU-115 with 2x LAU-127 AIM-120A AMRAAM",
        "weight": 460.701,
    }
    LAU_115_with_2x_LAU_127_AIM_120C_AMRAAM = {
        "clsid": "{SHOULDER_2xAIM_120C}",
        "name": "LAU-115 with 2x LAU-127 AIM-120C AMRAAM",
        "weight": 467.961,
    }
    LAU_115_with_2x_LAU_127_AIM_120C_AMRAAM_2 = {
        "clsid": "{BRU32_2xAIM_120C}",
        "name": "LAU-115 with 2x LAU-127 AIM-120C AMRAAM",
        "weight": 467.961,
    }
    LAU_115_with_2x_LAU_127_AIM_9X_Sidewinder = {
        "clsid": "{SHOULDER_2xAIM_9X}",
        "name": "LAU-115 with 2x LAU-127 AIM-9X Sidewinder",
        "weight": 313.921,
    }
    LAU_117_with_AGM_65E_Maverick_E_Laser_ASM_Lg_Whd = {
        "clsid": "{SHOULDER_LAU_117_AGM_65E}",
        "name": "LAU-117 with AGM-65E - Maverick E (Laser ASM - Lg Whd)",
        "weight": 345.001,
    }
    LAU_138_AIM_9X = {
        "clsid": "{LAU-138 wtip - AIM-9X}",
        "name": "LAU-138 AIM-9X",
        "weight": 84.46,
    }
    LAU_138_Captive_AIM_9M_for_ACM = {
        "clsid": "{LAU-138 wtip - CATM-9M}",
        "name": "LAU-138 Captive AIM-9M for ACM",
        "weight": 85.73,
    }
    LAU_7_AIM_9L_2 = {
        "clsid": "{LAU-7 wtip - AIM-9L}",
        "name": "LAU-7 AIM-9L",
        "weight": 85.73,
    }
    LAU_7_AIM_9M_2 = {
        "clsid": "{LAU-7 wtip - AIM-9M}",
        "name": "LAU-7 AIM-9M",
        "weight": 85.73,
    }
    LAU_7_AIM_9X = {
        "clsid": "{LAU-7 - AIM-9X}",
        "name": "LAU-7 AIM-9X",
        "weight": 99.46,
    }
    LAU_7_AN_ASQ_T50_TCTS_Pod_ACMI_Pod = {
        "clsid": "{LAU-7 wtip - TCTS L}",
        "name": "LAU-7 AN/ASQ-T50 TCTS Pod - ACMI Pod",
        "weight": 62.6,
    }
    LAU_7_AN_ASQ_T50_TCTS_Pod_ACMI_Pod_2 = {
        "clsid": "{LAU-7 wtip - TCTS R}",
        "name": "LAU-7 AN/ASQ-T50 TCTS Pod - ACMI Pod",
        "weight": 62.6,
    }
    LAU_7_Captive_AIM_9M_for_ACM = {
        "clsid": "{LAU-7 wtip - CATM-9M}",
        "name": "LAU-7 Captive AIM-9M for ACM",
        "weight": 85.73,
    }
    MAK79_3_Mk_83AIR = {
        "clsid": "{MAK79_MK83AIR 3L}",
        "name": "MAK79 3 Mk-83AIR",
        "weight": 1458,
    }
    MAK79_3_Mk_83AIR_2 = {
        "clsid": "{MAK79_MK83AIR 3R}",
        "name": "MAK79 3 Mk-83AIR",
        "weight": 1458,
    }
    MAK79_Mk_83AIR = {
        "clsid": "{MAK79_MK83AIR 1R}",
        "name": "MAK79 Mk-83AIR",
        "weight": 486,
    }
    MAK79_Mk_83AIR_2 = {
        "clsid": "{MAK79_MK83AIR 1L}",
        "name": "MAK79 Mk-83AIR",
        "weight": 486,
    }
    Mk_83AIR = {
        "clsid": "{PHXBRU3242_MK83AIR RS}",
        "name": "Mk-83AIR",
        "weight": 661.38,
    }
    Mk_83AIR_2 = {
        "clsid": "{PHXBRU3242_MK83AIR LS}",
        "name": "Mk-83AIR",
        "weight": 661.38,
    }
    Mk_83_AIR = {
        "clsid": "{BRU-32 MK-83AIR}",
        "name": "Mk-83 AIR",
        "weight": 533.38,
    }
    _2_LAU_10_4_Laser_Guided_Zuni_Mk_71 = {
        "clsid": "{BRU3242_2xLGZLAU10 R}",
        "name": "2 LAU-10 - 4 Laser Guided Zuni Mk 71",
        "weight": 763.18,
    }
    _2_LAU_10_4_Laser_Guided_Zuni_Mk_71_2 = {
        "clsid": "{PHXBRU3242_2xLGZLAU10 RS}",
        "name": "2 LAU-10 - 4 Laser Guided Zuni Mk 71",
        "weight": 763.18,
    }
    _2_LAU_10_4_Laser_Guided_Zuni_Mk_71_3 = {
        "clsid": "{PHXBRU3242_2xLGZLAU10 LS}",
        "name": "2 LAU-10 - 4 Laser Guided Zuni Mk 71",
        "weight": 763.18,
    }


inject_weapons(WeaponsF14Modern)


class F_14BPylon1:
    LAU_7_AIM_9M_2 = (1, Weapons.LAU_7_AIM_9M_2)
    LAU_7_AIM_9L_2 = (1, Weapons.LAU_7_AIM_9L_2)
    LAU_7_AN_ASQ_T50_TCTS_Pod_ACMI_Pod = (1, Weapons.LAU_7_AN_ASQ_T50_TCTS_Pod_ACMI_Pod)
    LAU_7_Captive_AIM_9M_for_ACM = (1, Weapons.LAU_7_Captive_AIM_9M_for_ACM)
    LAU_138_Captive_AIM_9M_for_ACM = (1, Weapons.LAU_138_Captive_AIM_9M_for_ACM)
    LAU_138_AIM_9X = (1, Weapons.LAU_138_AIM_9X)


class F_14BPylon2:
    AIM_120A_2 = (2, Weapons.AIM_120A_2)
    LAU_115_with_2x_LAU_127_AIM_120A_AMRAAM = (
        2,
        Weapons.LAU_115_with_2x_LAU_127_AIM_120A_AMRAAM,
    )
    AIM_120C = (2, Weapons.AIM_120C)
    LAU_115_with_2x_LAU_127_AIM_120C_AMRAAM = (
        2,
        Weapons.LAU_115_with_2x_LAU_127_AIM_120C_AMRAAM,
    )
    AMBER_Rack_with_2x_AIM_120C_AMRAAM = (2, Weapons.AMBER_Rack_with_2x_AIM_120C_AMRAAM)
    LAU_7_AIM_9X = (2, Weapons.LAU_7_AIM_9X)
    LAU_115_with_2x_LAU_127_AIM_9X_Sidewinder = (
        2,
        Weapons.LAU_115_with_2x_LAU_127_AIM_9X_Sidewinder,
    )
    AGM_88_HARM = (2, Weapons.AGM_88_HARM)
    LAU_117_with_AGM_65E_Maverick_E_Laser_ASM_Lg_Whd = (
        2,
        Weapons.LAU_117_with_AGM_65E_Maverick_E_Laser_ASM_Lg_Whd,
    )
    BRU_32_with_AGM_84D_Harpoon_Anti_Ship_Missile = (
        2,
        Weapons.BRU_32_with_AGM_84D_Harpoon_Anti_Ship_Missile,
    )
    AIM_54C_ECCM_Sealed_Mk47_2 = (2, Weapons.AIM_54C_ECCM_Sealed_Mk47_2)
    _2_LAU_10_4_Laser_Guided_Zuni_Mk_71_3 = (
        2,
        Weapons._2_LAU_10_4_Laser_Guided_Zuni_Mk_71_3,
    )
    AIM_174B = (2, Weapons.AIM_174B)
    Empty_LAU_7_Pylon_with_Adapter = (2, Weapons.Empty_LAU_7_Pylon_with_Adapter)
    Empty_LAU_92_Adapter_Pylon = (2, Weapons.Empty_LAU_92_Adapter_Pylon)
    Empty_Phoenix_Adapter_Pylon = (2, Weapons.Empty_Phoenix_Adapter_Pylon)
    Mk_83AIR_2 = (2, Weapons.Mk_83AIR_2)


class F_14BPylon4:
    Mk_83_AIR = (4, Weapons.Mk_83_AIR)
    MAK79_3_Mk_83AIR = (4, Weapons.MAK79_3_Mk_83AIR)
    AIM_120A = (4, Weapons.AIM_120A)
    LAU_115_with_2x_LAU_127_AIM_120A_AMRAAM_2 = (
        4,
        Weapons.LAU_115_with_2x_LAU_127_AIM_120A_AMRAAM_2,
    )
    LAU_115_with_2x_LAU_127_AIM_120C_AMRAAM_2 = (
        4,
        Weapons.LAU_115_with_2x_LAU_127_AIM_120C_AMRAAM_2,
    )
    AMBER_Rack_with_2x_AIM_120C_AMRAAM_2 = (
        4,
        Weapons.AMBER_Rack_with_2x_AIM_120C_AMRAAM_2,
    )
    AIM_54C_ECCM_Sealed_Mk47 = (4, Weapons.AIM_54C_ECCM_Sealed_Mk47)
    AGM_123_Skipper_II = (4, Weapons.AGM_123_Skipper_II)
    _2_LAU_10_4_Laser_Guided_Zuni_Mk_71 = (
        4,
        Weapons._2_LAU_10_4_Laser_Guided_Zuni_Mk_71,
    )


class F_14BPylon5:
    Mk_83_AIR = (5, Weapons.Mk_83_AIR)
    MAK79_Mk_83AIR_2 = (5, Weapons.MAK79_Mk_83AIR_2)
    AIM_120A = (5, Weapons.AIM_120A)
    AMBER_Rack_with_2x_AIM_120C_AMRAAM_2 = (
        5,
        Weapons.AMBER_Rack_with_2x_AIM_120C_AMRAAM_2,
    )
    AIM_54C_ECCM_Sealed_Mk47 = (5, Weapons.AIM_54C_ECCM_Sealed_Mk47)
    AGM_123_Skipper_II = (5, Weapons.AGM_123_Skipper_II)


class F_14BPylon6:
    Mk_83_AIR = (6, Weapons.Mk_83_AIR)
    MAK79_Mk_83AIR = (6, Weapons.MAK79_Mk_83AIR)
    AIM_120A = (6, Weapons.AIM_120A)
    AMBER_Rack_with_2x_AIM_120C_AMRAAM_2 = (
        6,
        Weapons.AMBER_Rack_with_2x_AIM_120C_AMRAAM_2,
    )
    AIM_54C_ECCM_Sealed_Mk47 = (6, Weapons.AIM_54C_ECCM_Sealed_Mk47)
    AGM_123_Skipper_II = (6, Weapons.AGM_123_Skipper_II)


class F_14BPylon7:
    Mk_83_AIR = (7, Weapons.Mk_83_AIR)
    MAK79_3_Mk_83AIR_2 = (7, Weapons.MAK79_3_Mk_83AIR_2)
    AIM_120A = (7, Weapons.AIM_120A)
    LAU_115_with_2x_LAU_127_AIM_120A_AMRAAM_2 = (
        7,
        Weapons.LAU_115_with_2x_LAU_127_AIM_120A_AMRAAM_2,
    )
    LAU_115_with_2x_LAU_127_AIM_120C_AMRAAM_2 = (
        7,
        Weapons.LAU_115_with_2x_LAU_127_AIM_120C_AMRAAM_2,
    )
    AMBER_Rack_with_2x_AIM_120C_AMRAAM_2 = (
        7,
        Weapons.AMBER_Rack_with_2x_AIM_120C_AMRAAM_2,
    )
    AIM_54C_ECCM_Sealed_Mk47 = (7, Weapons.AIM_54C_ECCM_Sealed_Mk47)
    AGM_123_Skipper_II = (7, Weapons.AGM_123_Skipper_II)
    LAU_10_4_Laser_Guided_Zuni_Mk_71 = (7, Weapons.LAU_10_4_Laser_Guided_Zuni_Mk_71)


class F_14BPylon9:
    AIM_120A_2 = (9, Weapons.AIM_120A_2)
    LAU_115_with_2x_LAU_127_AIM_120A_AMRAAM = (
        9,
        Weapons.LAU_115_with_2x_LAU_127_AIM_120A_AMRAAM,
    )
    AIM_120C = (9, Weapons.AIM_120C)
    LAU_115_with_2x_LAU_127_AIM_120C_AMRAAM = (
        9,
        Weapons.LAU_115_with_2x_LAU_127_AIM_120C_AMRAAM,
    )
    AMBER_Rack_with_2x_AIM_120C_AMRAAM = (9, Weapons.AMBER_Rack_with_2x_AIM_120C_AMRAAM)
    LAU_7_AIM_9X = (9, Weapons.LAU_7_AIM_9X)
    LAU_115_with_2x_LAU_127_AIM_9X_Sidewinder = (
        9,
        Weapons.LAU_115_with_2x_LAU_127_AIM_9X_Sidewinder,
    )
    AGM_88_HARM = (9, Weapons.AGM_88_HARM)
    LAU_117_with_AGM_65E_Maverick_E_Laser_ASM_Lg_Whd = (
        9,
        Weapons.LAU_117_with_AGM_65E_Maverick_E_Laser_ASM_Lg_Whd,
    )
    BRU_32_with_AGM_84D_Harpoon_Anti_Ship_Missile = (
        9,
        Weapons.BRU_32_with_AGM_84D_Harpoon_Anti_Ship_Missile,
    )
    AIM_54C_ECCM_Sealed_Mk47_3 = (9, Weapons.AIM_54C_ECCM_Sealed_Mk47_3)
    _2_LAU_10_4_Laser_Guided_Zuni_Mk_71_2 = (
        9,
        Weapons._2_LAU_10_4_Laser_Guided_Zuni_Mk_71_2,
    )
    AIM_174B_2 = (9, Weapons.AIM_174B_2)
    Empty_LAU_7_Pylon_with_Adapter = (9, Weapons.Empty_LAU_7_Pylon_with_Adapter)
    Empty_LAU_92_Adapter_Pylon = (9, Weapons.Empty_LAU_92_Adapter_Pylon)
    Empty_Phoenix_Adapter_Pylon_2 = (9, Weapons.Empty_Phoenix_Adapter_Pylon_2)
    Mk_83AIR = (9, Weapons.Mk_83AIR)


class F_14BPylon10:
    LAU_7_AIM_9M_2 = (10, Weapons.LAU_7_AIM_9M_2)
    LAU_7_AIM_9L_2 = (10, Weapons.LAU_7_AIM_9L_2)
    LAU_7_AN_ASQ_T50_TCTS_Pod_ACMI_Pod_2 = (
        10,
        Weapons.LAU_7_AN_ASQ_T50_TCTS_Pod_ACMI_Pod_2,
    )
    LAU_7_Captive_AIM_9M_for_ACM = (10, Weapons.LAU_7_Captive_AIM_9M_for_ACM)
    LAU_138_Captive_AIM_9M_for_ACM = (10, Weapons.LAU_138_Captive_AIM_9M_for_ACM)
    LAU_138_AIM_9X = (10, Weapons.LAU_138_AIM_9X)


class F_14A_95_GRPylon2:
    AIM_120A_2 = (2, Weapons.AIM_120A_2)
    LAU_115_with_2x_LAU_127_AIM_120A_AMRAAM = (
        2,
        Weapons.LAU_115_with_2x_LAU_127_AIM_120A_AMRAAM,
    )
    AIM_120C = (2, Weapons.AIM_120C)
    LAU_115_with_2x_LAU_127_AIM_120C_AMRAAM = (
        2,
        Weapons.LAU_115_with_2x_LAU_127_AIM_120C_AMRAAM,
    )
    AMBER_Rack_with_2x_AIM_120C_AMRAAM = (2, Weapons.AMBER_Rack_with_2x_AIM_120C_AMRAAM)
    LAU_7_AIM_9X = (2, Weapons.LAU_7_AIM_9X)
    LAU_115_with_2x_LAU_127_AIM_9X_Sidewinder = (
        2,
        Weapons.LAU_115_with_2x_LAU_127_AIM_9X_Sidewinder,
    )
    AGM_88_HARM = (2, Weapons.AGM_88_HARM)
    LAU_117_with_AGM_65E_Maverick_E_Laser_ASM_Lg_Whd = (
        2,
        Weapons.LAU_117_with_AGM_65E_Maverick_E_Laser_ASM_Lg_Whd,
    )
    BRU_32_with_AGM_84D_Harpoon_Anti_Ship_Missile = (
        2,
        Weapons.BRU_32_with_AGM_84D_Harpoon_Anti_Ship_Missile,
    )
    _2_LAU_10_4_Laser_Guided_Zuni_Mk_71_3 = (
        2,
        Weapons._2_LAU_10_4_Laser_Guided_Zuni_Mk_71_3,
    )
    AIM_174B = (2, Weapons.AIM_174B)
    Empty_LAU_7_Pylon_with_Adapter = (2, Weapons.Empty_LAU_7_Pylon_with_Adapter)
    Empty_LAU_92_Adapter_Pylon = (2, Weapons.Empty_LAU_92_Adapter_Pylon)
    Empty_Phoenix_Adapter_Pylon = (2, Weapons.Empty_Phoenix_Adapter_Pylon)
    Mk_83AIR_2 = (2, Weapons.Mk_83AIR_2)


class F_14A_95_GRPylon4:
    Mk_83_AIR = (4, Weapons.Mk_83_AIR)
    MAK79_3_Mk_83AIR = (4, Weapons.MAK79_3_Mk_83AIR)
    AIM_120A = (4, Weapons.AIM_120A)
    LAU_115_with_2x_LAU_127_AIM_120A_AMRAAM_2 = (
        4,
        Weapons.LAU_115_with_2x_LAU_127_AIM_120A_AMRAAM_2,
    )
    LAU_115_with_2x_LAU_127_AIM_120C_AMRAAM_2 = (
        4,
        Weapons.LAU_115_with_2x_LAU_127_AIM_120C_AMRAAM_2,
    )
    AMBER_Rack_with_2x_AIM_120C_AMRAAM_2 = (
        4,
        Weapons.AMBER_Rack_with_2x_AIM_120C_AMRAAM_2,
    )
    AGM_123_Skipper_II = (4, Weapons.AGM_123_Skipper_II)
    _2_LAU_10_4_Laser_Guided_Zuni_Mk_71 = (
        4,
        Weapons._2_LAU_10_4_Laser_Guided_Zuni_Mk_71,
    )


class F_14A_95_GRPylon5:
    Mk_83_AIR = (5, Weapons.Mk_83_AIR)
    MAK79_Mk_83AIR_2 = (5, Weapons.MAK79_Mk_83AIR_2)
    AIM_120A = (5, Weapons.AIM_120A)
    AMBER_Rack_with_2x_AIM_120C_AMRAAM_2 = (
        5,
        Weapons.AMBER_Rack_with_2x_AIM_120C_AMRAAM_2,
    )
    AGM_123_Skipper_II = (5, Weapons.AGM_123_Skipper_II)


class F_14A_95_GRPylon6:
    Mk_83_AIR = (6, Weapons.Mk_83_AIR)
    MAK79_Mk_83AIR = (6, Weapons.MAK79_Mk_83AIR)
    AIM_120A = (6, Weapons.AIM_120A)
    AMBER_Rack_with_2x_AIM_120C_AMRAAM_2 = (
        6,
        Weapons.AMBER_Rack_with_2x_AIM_120C_AMRAAM_2,
    )
    AGM_123_Skipper_II = (6, Weapons.AGM_123_Skipper_II)


class F_14A_95_GRPylon7:
    Mk_83_AIR = (7, Weapons.Mk_83_AIR)
    MAK79_3_Mk_83AIR_2 = (7, Weapons.MAK79_3_Mk_83AIR_2)
    AIM_120A = (7, Weapons.AIM_120A)
    LAU_115_with_2x_LAU_127_AIM_120A_AMRAAM_2 = (
        7,
        Weapons.LAU_115_with_2x_LAU_127_AIM_120A_AMRAAM_2,
    )
    LAU_115_with_2x_LAU_127_AIM_120C_AMRAAM_2 = (
        7,
        Weapons.LAU_115_with_2x_LAU_127_AIM_120C_AMRAAM_2,
    )
    AMBER_Rack_with_2x_AIM_120C_AMRAAM_2 = (
        7,
        Weapons.AMBER_Rack_with_2x_AIM_120C_AMRAAM_2,
    )
    AGM_123_Skipper_II = (7, Weapons.AGM_123_Skipper_II)
    LAU_10_4_Laser_Guided_Zuni_Mk_71 = (7, Weapons.LAU_10_4_Laser_Guided_Zuni_Mk_71)


class F_14A_95_GRPylon9:
    AIM_120A_2 = (9, Weapons.AIM_120A_2)
    LAU_115_with_2x_LAU_127_AIM_120A_AMRAAM = (
        9,
        Weapons.LAU_115_with_2x_LAU_127_AIM_120A_AMRAAM,
    )
    AIM_120C = (9, Weapons.AIM_120C)
    LAU_115_with_2x_LAU_127_AIM_120C_AMRAAM = (
        9,
        Weapons.LAU_115_with_2x_LAU_127_AIM_120C_AMRAAM,
    )
    AMBER_Rack_with_2x_AIM_120C_AMRAAM = (9, Weapons.AMBER_Rack_with_2x_AIM_120C_AMRAAM)
    LAU_7_AIM_9X = (9, Weapons.LAU_7_AIM_9X)
    LAU_115_with_2x_LAU_127_AIM_9X_Sidewinder = (
        9,
        Weapons.LAU_115_with_2x_LAU_127_AIM_9X_Sidewinder,
    )
    AGM_88_HARM = (9, Weapons.AGM_88_HARM)
    LAU_117_with_AGM_65E_Maverick_E_Laser_ASM_Lg_Whd = (
        9,
        Weapons.LAU_117_with_AGM_65E_Maverick_E_Laser_ASM_Lg_Whd,
    )
    BRU_32_with_AGM_84D_Harpoon_Anti_Ship_Missile = (
        9,
        Weapons.BRU_32_with_AGM_84D_Harpoon_Anti_Ship_Missile,
    )
    _2_LAU_10_4_Laser_Guided_Zuni_Mk_71_2 = (
        9,
        Weapons._2_LAU_10_4_Laser_Guided_Zuni_Mk_71_2,
    )
    AIM_174B_2 = (9, Weapons.AIM_174B_2)
    Empty_LAU_7_Pylon_with_Adapter = (9, Weapons.Empty_LAU_7_Pylon_with_Adapter)
    Empty_LAU_92_Adapter_Pylon = (9, Weapons.Empty_LAU_92_Adapter_Pylon)
    Empty_Phoenix_Adapter_Pylon_2 = (9, Weapons.Empty_Phoenix_Adapter_Pylon_2)
    Mk_83AIR = (9, Weapons.Mk_83AIR)


class F_14A_135_GR_EarlyPylon1:
    LAU_7_AIM_9M_2 = (1, Weapons.LAU_7_AIM_9M_2)
    LAU_7_AIM_9L_2 = (1, Weapons.LAU_7_AIM_9L_2)
    LAU_7_AN_ASQ_T50_TCTS_Pod_ACMI_Pod = (1, Weapons.LAU_7_AN_ASQ_T50_TCTS_Pod_ACMI_Pod)
    LAU_7_Captive_AIM_9M_for_ACM = (1, Weapons.LAU_7_Captive_AIM_9M_for_ACM)
    LAU_138_Captive_AIM_9M_for_ACM = (1, Weapons.LAU_138_Captive_AIM_9M_for_ACM)
    LAU_138_AIM_9X = (1, Weapons.LAU_138_AIM_9X)


class F_14A_135_GR_EarlyPylon2:
    AIM_120A_2 = (2, Weapons.AIM_120A_2)
    LAU_115_with_2x_LAU_127_AIM_120A_AMRAAM = (
        2,
        Weapons.LAU_115_with_2x_LAU_127_AIM_120A_AMRAAM,
    )
    AIM_120C = (2, Weapons.AIM_120C)
    LAU_115_with_2x_LAU_127_AIM_120C_AMRAAM = (
        2,
        Weapons.LAU_115_with_2x_LAU_127_AIM_120C_AMRAAM,
    )
    AMBER_Rack_with_2x_AIM_120C_AMRAAM = (2, Weapons.AMBER_Rack_with_2x_AIM_120C_AMRAAM)
    LAU_7_AIM_9X = (2, Weapons.LAU_7_AIM_9X)
    LAU_115_with_2x_LAU_127_AIM_9X_Sidewinder = (
        2,
        Weapons.LAU_115_with_2x_LAU_127_AIM_9X_Sidewinder,
    )
    AGM_88_HARM = (2, Weapons.AGM_88_HARM)
    LAU_117_with_AGM_65E_Maverick_E_Laser_ASM_Lg_Whd = (
        2,
        Weapons.LAU_117_with_AGM_65E_Maverick_E_Laser_ASM_Lg_Whd,
    )
    BRU_32_with_AGM_84D_Harpoon_Anti_Ship_Missile = (
        2,
        Weapons.BRU_32_with_AGM_84D_Harpoon_Anti_Ship_Missile,
    )
    AIM_54C_ECCM_Sealed_Mk47_2 = (2, Weapons.AIM_54C_ECCM_Sealed_Mk47_2)
    _2_LAU_10_4_Laser_Guided_Zuni_Mk_71_3 = (
        2,
        Weapons._2_LAU_10_4_Laser_Guided_Zuni_Mk_71_3,
    )
    AIM_174B = (2, Weapons.AIM_174B)
    Empty_LAU_7_Pylon_with_Adapter = (2, Weapons.Empty_LAU_7_Pylon_with_Adapter)
    Empty_LAU_92_Adapter_Pylon = (2, Weapons.Empty_LAU_92_Adapter_Pylon)
    Empty_Phoenix_Adapter_Pylon = (2, Weapons.Empty_Phoenix_Adapter_Pylon)
    Mk_83AIR_2 = (2, Weapons.Mk_83AIR_2)


class F_14A_135_GR_EarlyPylon4:
    Mk_83_AIR = (4, Weapons.Mk_83_AIR)
    MAK79_3_Mk_83AIR = (4, Weapons.MAK79_3_Mk_83AIR)
    AIM_120A = (4, Weapons.AIM_120A)
    LAU_115_with_2x_LAU_127_AIM_120A_AMRAAM_2 = (
        4,
        Weapons.LAU_115_with_2x_LAU_127_AIM_120A_AMRAAM_2,
    )
    LAU_115_with_2x_LAU_127_AIM_120C_AMRAAM_2 = (
        4,
        Weapons.LAU_115_with_2x_LAU_127_AIM_120C_AMRAAM_2,
    )
    AMBER_Rack_with_2x_AIM_120C_AMRAAM_2 = (
        4,
        Weapons.AMBER_Rack_with_2x_AIM_120C_AMRAAM_2,
    )
    AIM_54C_ECCM_Sealed_Mk47 = (4, Weapons.AIM_54C_ECCM_Sealed_Mk47)
    AGM_123_Skipper_II = (4, Weapons.AGM_123_Skipper_II)
    _2_LAU_10_4_Laser_Guided_Zuni_Mk_71 = (
        4,
        Weapons._2_LAU_10_4_Laser_Guided_Zuni_Mk_71,
    )


class F_14A_135_GR_EarlyPylon5:
    Mk_83_AIR = (5, Weapons.Mk_83_AIR)
    MAK79_Mk_83AIR_2 = (5, Weapons.MAK79_Mk_83AIR_2)
    AIM_120A = (5, Weapons.AIM_120A)
    AMBER_Rack_with_2x_AIM_120C_AMRAAM_2 = (
        5,
        Weapons.AMBER_Rack_with_2x_AIM_120C_AMRAAM_2,
    )
    AIM_54C_ECCM_Sealed_Mk47 = (5, Weapons.AIM_54C_ECCM_Sealed_Mk47)
    AGM_123_Skipper_II = (5, Weapons.AGM_123_Skipper_II)


class F_14A_135_GR_EarlyPylon6:
    Mk_83_AIR = (6, Weapons.Mk_83_AIR)
    MAK79_Mk_83AIR = (6, Weapons.MAK79_Mk_83AIR)
    AIM_120A = (6, Weapons.AIM_120A)
    AMBER_Rack_with_2x_AIM_120C_AMRAAM_2 = (
        6,
        Weapons.AMBER_Rack_with_2x_AIM_120C_AMRAAM_2,
    )
    AIM_54C_ECCM_Sealed_Mk47 = (6, Weapons.AIM_54C_ECCM_Sealed_Mk47)
    AGM_123_Skipper_II = (6, Weapons.AGM_123_Skipper_II)


class F_14A_135_GR_EarlyPylon7:
    Mk_83_AIR = (7, Weapons.Mk_83_AIR)
    MAK79_3_Mk_83AIR_2 = (7, Weapons.MAK79_3_Mk_83AIR_2)
    AIM_120A = (7, Weapons.AIM_120A)
    LAU_115_with_2x_LAU_127_AIM_120A_AMRAAM_2 = (
        7,
        Weapons.LAU_115_with_2x_LAU_127_AIM_120A_AMRAAM_2,
    )
    LAU_115_with_2x_LAU_127_AIM_120C_AMRAAM_2 = (
        7,
        Weapons.LAU_115_with_2x_LAU_127_AIM_120C_AMRAAM_2,
    )
    AMBER_Rack_with_2x_AIM_120C_AMRAAM_2 = (
        7,
        Weapons.AMBER_Rack_with_2x_AIM_120C_AMRAAM_2,
    )
    AIM_54C_ECCM_Sealed_Mk47 = (7, Weapons.AIM_54C_ECCM_Sealed_Mk47)
    AGM_123_Skipper_II = (7, Weapons.AGM_123_Skipper_II)
    LAU_10_4_Laser_Guided_Zuni_Mk_71 = (7, Weapons.LAU_10_4_Laser_Guided_Zuni_Mk_71)


class F_14A_135_GR_EarlyPylon9:
    AIM_120A_2 = (9, Weapons.AIM_120A_2)
    LAU_115_with_2x_LAU_127_AIM_120A_AMRAAM = (
        9,
        Weapons.LAU_115_with_2x_LAU_127_AIM_120A_AMRAAM,
    )
    AIM_120C = (9, Weapons.AIM_120C)
    LAU_115_with_2x_LAU_127_AIM_120C_AMRAAM = (
        9,
        Weapons.LAU_115_with_2x_LAU_127_AIM_120C_AMRAAM,
    )
    AMBER_Rack_with_2x_AIM_120C_AMRAAM = (9, Weapons.AMBER_Rack_with_2x_AIM_120C_AMRAAM)
    LAU_7_AIM_9X = (9, Weapons.LAU_7_AIM_9X)
    LAU_115_with_2x_LAU_127_AIM_9X_Sidewinder = (
        9,
        Weapons.LAU_115_with_2x_LAU_127_AIM_9X_Sidewinder,
    )
    AGM_88_HARM = (9, Weapons.AGM_88_HARM)
    LAU_117_with_AGM_65E_Maverick_E_Laser_ASM_Lg_Whd = (
        9,
        Weapons.LAU_117_with_AGM_65E_Maverick_E_Laser_ASM_Lg_Whd,
    )
    BRU_32_with_AGM_84D_Harpoon_Anti_Ship_Missile = (
        9,
        Weapons.BRU_32_with_AGM_84D_Harpoon_Anti_Ship_Missile,
    )
    AIM_54C_ECCM_Sealed_Mk47_3 = (9, Weapons.AIM_54C_ECCM_Sealed_Mk47_3)
    _2_LAU_10_4_Laser_Guided_Zuni_Mk_71_2 = (
        9,
        Weapons._2_LAU_10_4_Laser_Guided_Zuni_Mk_71_2,
    )
    AIM_174B_2 = (9, Weapons.AIM_174B_2)
    Empty_LAU_7_Pylon_with_Adapter = (9, Weapons.Empty_LAU_7_Pylon_with_Adapter)
    Empty_LAU_92_Adapter_Pylon = (9, Weapons.Empty_LAU_92_Adapter_Pylon)
    Empty_Phoenix_Adapter_Pylon_2 = (9, Weapons.Empty_Phoenix_Adapter_Pylon_2)
    Mk_83AIR = (9, Weapons.Mk_83AIR)


class F_14A_135_GR_EarlyPylon10:
    LAU_7_AIM_9M_2 = (10, Weapons.LAU_7_AIM_9M_2)
    LAU_7_AIM_9L_2 = (10, Weapons.LAU_7_AIM_9L_2)
    LAU_7_AN_ASQ_T50_TCTS_Pod_ACMI_Pod_2 = (
        10,
        Weapons.LAU_7_AN_ASQ_T50_TCTS_Pod_ACMI_Pod_2,
    )
    LAU_7_Captive_AIM_9M_for_ACM = (10, Weapons.LAU_7_Captive_AIM_9M_for_ACM)
    LAU_138_Captive_AIM_9M_for_ACM = (10, Weapons.LAU_138_Captive_AIM_9M_for_ACM)
    LAU_138_AIM_9X = (10, Weapons.LAU_138_AIM_9X)


class F_14A_135_GRPylon1:
    LAU_7_AIM_9M_2 = (1, Weapons.LAU_7_AIM_9M_2)
    LAU_7_AIM_9L_2 = (1, Weapons.LAU_7_AIM_9L_2)
    LAU_7_AN_ASQ_T50_TCTS_Pod_ACMI_Pod = (1, Weapons.LAU_7_AN_ASQ_T50_TCTS_Pod_ACMI_Pod)
    LAU_7_Captive_AIM_9M_for_ACM = (1, Weapons.LAU_7_Captive_AIM_9M_for_ACM)
    LAU_138_Captive_AIM_9M_for_ACM = (1, Weapons.LAU_138_Captive_AIM_9M_for_ACM)
    LAU_138_AIM_9X = (1, Weapons.LAU_138_AIM_9X)


class F_14A_135_GRPylon2:
    AIM_120A_2 = (2, Weapons.AIM_120A_2)
    LAU_115_with_2x_LAU_127_AIM_120A_AMRAAM = (
        2,
        Weapons.LAU_115_with_2x_LAU_127_AIM_120A_AMRAAM,
    )
    AIM_120C = (2, Weapons.AIM_120C)
    LAU_115_with_2x_LAU_127_AIM_120C_AMRAAM = (
        2,
        Weapons.LAU_115_with_2x_LAU_127_AIM_120C_AMRAAM,
    )
    AMBER_Rack_with_2x_AIM_120C_AMRAAM = (2, Weapons.AMBER_Rack_with_2x_AIM_120C_AMRAAM)
    LAU_7_AIM_9X = (2, Weapons.LAU_7_AIM_9X)
    LAU_115_with_2x_LAU_127_AIM_9X_Sidewinder = (
        2,
        Weapons.LAU_115_with_2x_LAU_127_AIM_9X_Sidewinder,
    )
    AGM_88_HARM = (2, Weapons.AGM_88_HARM)
    LAU_117_with_AGM_65E_Maverick_E_Laser_ASM_Lg_Whd = (
        2,
        Weapons.LAU_117_with_AGM_65E_Maverick_E_Laser_ASM_Lg_Whd,
    )
    BRU_32_with_AGM_84D_Harpoon_Anti_Ship_Missile = (
        2,
        Weapons.BRU_32_with_AGM_84D_Harpoon_Anti_Ship_Missile,
    )
    AIM_54C_ECCM_Sealed_Mk47_2 = (2, Weapons.AIM_54C_ECCM_Sealed_Mk47_2)
    _2_LAU_10_4_Laser_Guided_Zuni_Mk_71_3 = (
        2,
        Weapons._2_LAU_10_4_Laser_Guided_Zuni_Mk_71_3,
    )
    AIM_174B = (2, Weapons.AIM_174B)
    Empty_LAU_7_Pylon_with_Adapter = (2, Weapons.Empty_LAU_7_Pylon_with_Adapter)
    Empty_LAU_92_Adapter_Pylon = (2, Weapons.Empty_LAU_92_Adapter_Pylon)
    Empty_Phoenix_Adapter_Pylon = (2, Weapons.Empty_Phoenix_Adapter_Pylon)
    Mk_83AIR_2 = (2, Weapons.Mk_83AIR_2)


class F_14A_135_GRPylon4:
    Mk_83_AIR = (4, Weapons.Mk_83_AIR)
    MAK79_3_Mk_83AIR = (4, Weapons.MAK79_3_Mk_83AIR)
    AIM_120A = (4, Weapons.AIM_120A)
    LAU_115_with_2x_LAU_127_AIM_120A_AMRAAM_2 = (
        4,
        Weapons.LAU_115_with_2x_LAU_127_AIM_120A_AMRAAM_2,
    )
    LAU_115_with_2x_LAU_127_AIM_120C_AMRAAM_2 = (
        4,
        Weapons.LAU_115_with_2x_LAU_127_AIM_120C_AMRAAM_2,
    )
    AMBER_Rack_with_2x_AIM_120C_AMRAAM_2 = (
        4,
        Weapons.AMBER_Rack_with_2x_AIM_120C_AMRAAM_2,
    )
    AIM_54C_ECCM_Sealed_Mk47 = (4, Weapons.AIM_54C_ECCM_Sealed_Mk47)
    AGM_123_Skipper_II = (4, Weapons.AGM_123_Skipper_II)
    _2_LAU_10_4_Laser_Guided_Zuni_Mk_71 = (
        4,
        Weapons._2_LAU_10_4_Laser_Guided_Zuni_Mk_71,
    )


class F_14A_135_GRPylon5:
    Mk_83_AIR = (5, Weapons.Mk_83_AIR)
    MAK79_Mk_83AIR_2 = (5, Weapons.MAK79_Mk_83AIR_2)
    AIM_120A = (5, Weapons.AIM_120A)
    AMBER_Rack_with_2x_AIM_120C_AMRAAM_2 = (
        5,
        Weapons.AMBER_Rack_with_2x_AIM_120C_AMRAAM_2,
    )
    AIM_54C_ECCM_Sealed_Mk47 = (5, Weapons.AIM_54C_ECCM_Sealed_Mk47)
    AGM_123_Skipper_II = (5, Weapons.AGM_123_Skipper_II)


class F_14A_135_GRPylon6:
    Mk_83_AIR = (6, Weapons.Mk_83_AIR)
    MAK79_Mk_83AIR = (6, Weapons.MAK79_Mk_83AIR)
    AIM_120A = (6, Weapons.AIM_120A)
    AMBER_Rack_with_2x_AIM_120C_AMRAAM_2 = (
        6,
        Weapons.AMBER_Rack_with_2x_AIM_120C_AMRAAM_2,
    )
    AIM_54C_ECCM_Sealed_Mk47 = (6, Weapons.AIM_54C_ECCM_Sealed_Mk47)
    AGM_123_Skipper_II = (6, Weapons.AGM_123_Skipper_II)


class F_14A_135_GRPylon7:
    Mk_83_AIR = (7, Weapons.Mk_83_AIR)
    MAK79_3_Mk_83AIR_2 = (7, Weapons.MAK79_3_Mk_83AIR_2)
    AIM_120A = (7, Weapons.AIM_120A)
    LAU_115_with_2x_LAU_127_AIM_120A_AMRAAM_2 = (
        7,
        Weapons.LAU_115_with_2x_LAU_127_AIM_120A_AMRAAM_2,
    )
    LAU_115_with_2x_LAU_127_AIM_120C_AMRAAM_2 = (
        7,
        Weapons.LAU_115_with_2x_LAU_127_AIM_120C_AMRAAM_2,
    )
    AMBER_Rack_with_2x_AIM_120C_AMRAAM_2 = (
        7,
        Weapons.AMBER_Rack_with_2x_AIM_120C_AMRAAM_2,
    )
    AIM_54C_ECCM_Sealed_Mk47 = (7, Weapons.AIM_54C_ECCM_Sealed_Mk47)
    AGM_123_Skipper_II = (7, Weapons.AGM_123_Skipper_II)
    LAU_10_4_Laser_Guided_Zuni_Mk_71 = (7, Weapons.LAU_10_4_Laser_Guided_Zuni_Mk_71)


class F_14A_135_GRPylon9:
    AIM_120A_2 = (9, Weapons.AIM_120A_2)
    LAU_115_with_2x_LAU_127_AIM_120A_AMRAAM = (
        9,
        Weapons.LAU_115_with_2x_LAU_127_AIM_120A_AMRAAM,
    )
    AIM_120C = (9, Weapons.AIM_120C)
    LAU_115_with_2x_LAU_127_AIM_120C_AMRAAM = (
        9,
        Weapons.LAU_115_with_2x_LAU_127_AIM_120C_AMRAAM,
    )
    AMBER_Rack_with_2x_AIM_120C_AMRAAM = (9, Weapons.AMBER_Rack_with_2x_AIM_120C_AMRAAM)
    LAU_7_AIM_9X = (9, Weapons.LAU_7_AIM_9X)
    LAU_115_with_2x_LAU_127_AIM_9X_Sidewinder = (
        9,
        Weapons.LAU_115_with_2x_LAU_127_AIM_9X_Sidewinder,
    )
    AGM_88_HARM = (9, Weapons.AGM_88_HARM)
    LAU_117_with_AGM_65E_Maverick_E_Laser_ASM_Lg_Whd = (
        9,
        Weapons.LAU_117_with_AGM_65E_Maverick_E_Laser_ASM_Lg_Whd,
    )
    BRU_32_with_AGM_84D_Harpoon_Anti_Ship_Missile = (
        9,
        Weapons.BRU_32_with_AGM_84D_Harpoon_Anti_Ship_Missile,
    )
    AIM_54C_ECCM_Sealed_Mk47_3 = (9, Weapons.AIM_54C_ECCM_Sealed_Mk47_3)
    _2_LAU_10_4_Laser_Guided_Zuni_Mk_71_2 = (
        9,
        Weapons._2_LAU_10_4_Laser_Guided_Zuni_Mk_71_2,
    )
    AIM_174B_2 = (9, Weapons.AIM_174B_2)
    Empty_LAU_7_Pylon_with_Adapter = (9, Weapons.Empty_LAU_7_Pylon_with_Adapter)
    Empty_LAU_92_Adapter_Pylon = (9, Weapons.Empty_LAU_92_Adapter_Pylon)
    Empty_Phoenix_Adapter_Pylon_2 = (9, Weapons.Empty_Phoenix_Adapter_Pylon_2)
    Mk_83AIR = (9, Weapons.Mk_83AIR)


class F_14A_135_GRPylon10:
    LAU_7_AIM_9M_2 = (10, Weapons.LAU_7_AIM_9M_2)
    LAU_7_AIM_9L_2 = (10, Weapons.LAU_7_AIM_9L_2)
    LAU_7_AN_ASQ_T50_TCTS_Pod_ACMI_Pod_2 = (
        10,
        Weapons.LAU_7_AN_ASQ_T50_TCTS_Pod_ACMI_Pod_2,
    )
    LAU_7_Captive_AIM_9M_for_ACM = (10, Weapons.LAU_7_Captive_AIM_9M_for_ACM)
    LAU_138_Captive_AIM_9M_for_ACM = (10, Weapons.LAU_138_Captive_AIM_9M_for_ACM)
    LAU_138_AIM_9X = (10, Weapons.LAU_138_AIM_9X)


def inject_F14ModernWeapons() -> None:
    inject_pylon(F_14B.Pylon1, F_14BPylon1)
    inject_pylon(F_14B.Pylon2, F_14BPylon2)
    inject_pylon(F_14B.Pylon4, F_14BPylon4)
    inject_pylon(F_14B.Pylon5, F_14BPylon5)
    inject_pylon(F_14B.Pylon6, F_14BPylon6)
    inject_pylon(F_14B.Pylon7, F_14BPylon7)
    inject_pylon(F_14B.Pylon9, F_14BPylon9)
    inject_pylon(F_14B.Pylon10, F_14BPylon10)
    inject_pylon(F_14A_95_GR.Pylon2, F_14A_95_GRPylon2)
    inject_pylon(F_14A_95_GR.Pylon4, F_14A_95_GRPylon4)
    inject_pylon(F_14A_95_GR.Pylon5, F_14A_95_GRPylon5)
    inject_pylon(F_14A_95_GR.Pylon6, F_14A_95_GRPylon6)
    inject_pylon(F_14A_95_GR.Pylon7, F_14A_95_GRPylon7)
    inject_pylon(F_14A_95_GR.Pylon9, F_14A_95_GRPylon9)
    inject_pylon(F_14A_135_GR_Early.Pylon1, F_14A_135_GR_EarlyPylon1)
    inject_pylon(F_14A_135_GR_Early.Pylon2, F_14A_135_GR_EarlyPylon2)
    inject_pylon(F_14A_135_GR_Early.Pylon4, F_14A_135_GR_EarlyPylon4)
    inject_pylon(F_14A_135_GR_Early.Pylon5, F_14A_135_GR_EarlyPylon5)
    inject_pylon(F_14A_135_GR_Early.Pylon6, F_14A_135_GR_EarlyPylon6)
    inject_pylon(F_14A_135_GR_Early.Pylon7, F_14A_135_GR_EarlyPylon7)
    inject_pylon(F_14A_135_GR_Early.Pylon9, F_14A_135_GR_EarlyPylon9)
    inject_pylon(F_14A_135_GR_Early.Pylon10, F_14A_135_GR_EarlyPylon10)
    inject_pylon(F_14A_135_GR.Pylon1, F_14A_135_GRPylon1)
    inject_pylon(F_14A_135_GR.Pylon2, F_14A_135_GRPylon2)
    inject_pylon(F_14A_135_GR.Pylon4, F_14A_135_GRPylon4)
    inject_pylon(F_14A_135_GR.Pylon5, F_14A_135_GRPylon5)
    inject_pylon(F_14A_135_GR.Pylon6, F_14A_135_GRPylon6)
    inject_pylon(F_14A_135_GR.Pylon7, F_14A_135_GRPylon7)
    inject_pylon(F_14A_135_GR.Pylon9, F_14A_135_GRPylon9)
    inject_pylon(F_14A_135_GR.Pylon10, F_14A_135_GRPylon10)


def eject_F14ModernWeapons() -> None:
    eject_pylon(F_14B.Pylon1, F_14BPylon1)
    eject_pylon(F_14B.Pylon2, F_14BPylon2)
    eject_pylon(F_14B.Pylon4, F_14BPylon4)
    eject_pylon(F_14B.Pylon5, F_14BPylon5)
    eject_pylon(F_14B.Pylon6, F_14BPylon6)
    eject_pylon(F_14B.Pylon7, F_14BPylon7)
    eject_pylon(F_14B.Pylon9, F_14BPylon9)
    eject_pylon(F_14B.Pylon10, F_14BPylon10)
    eject_pylon(F_14A_95_GR.Pylon2, F_14A_95_GRPylon2)
    eject_pylon(F_14A_95_GR.Pylon4, F_14A_95_GRPylon4)
    eject_pylon(F_14A_95_GR.Pylon5, F_14A_95_GRPylon5)
    eject_pylon(F_14A_95_GR.Pylon6, F_14A_95_GRPylon6)
    eject_pylon(F_14A_95_GR.Pylon7, F_14A_95_GRPylon7)
    eject_pylon(F_14A_95_GR.Pylon9, F_14A_95_GRPylon9)
    eject_pylon(F_14A_135_GR_Early.Pylon1, F_14A_135_GR_EarlyPylon1)
    eject_pylon(F_14A_135_GR_Early.Pylon2, F_14A_135_GR_EarlyPylon2)
    eject_pylon(F_14A_135_GR_Early.Pylon4, F_14A_135_GR_EarlyPylon4)
    eject_pylon(F_14A_135_GR_Early.Pylon5, F_14A_135_GR_EarlyPylon5)
    eject_pylon(F_14A_135_GR_Early.Pylon6, F_14A_135_GR_EarlyPylon6)
    eject_pylon(F_14A_135_GR_Early.Pylon7, F_14A_135_GR_EarlyPylon7)
    eject_pylon(F_14A_135_GR_Early.Pylon9, F_14A_135_GR_EarlyPylon9)
    eject_pylon(F_14A_135_GR_Early.Pylon10, F_14A_135_GR_EarlyPylon10)
    eject_pylon(F_14A_135_GR.Pylon1, F_14A_135_GRPylon1)
    eject_pylon(F_14A_135_GR.Pylon2, F_14A_135_GRPylon2)
    eject_pylon(F_14A_135_GR.Pylon4, F_14A_135_GRPylon4)
    eject_pylon(F_14A_135_GR.Pylon5, F_14A_135_GRPylon5)
    eject_pylon(F_14A_135_GR.Pylon6, F_14A_135_GRPylon6)
    eject_pylon(F_14A_135_GR.Pylon7, F_14A_135_GRPylon7)
    eject_pylon(F_14A_135_GR.Pylon9, F_14A_135_GRPylon9)
    eject_pylon(F_14A_135_GR.Pylon10, F_14A_135_GRPylon10)
