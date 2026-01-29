"""F-4E-45MC Expanded Weapons Pack extension.

Defines expanded weapon data for pydcs and provides helpers to inject/remove
additional F-4E-45MC pylon loadouts.
"""

from __future__ import annotations

from typing import Dict, Iterable

from dcs.planes import F_4E_45MC
from dcs.weapons_data import Weapons, weapon_ids

from pydcs_extensions.pylon_injector import inject_pylon, eject_pylon
from pydcs_extensions.weapon_injector import inject_weapons

MISSING_WEAPON_DEFS: Dict[str, Dict[str, object]] = {
    "AGM_45B_Shrike_ARM__LAU_34_": {
        "clsid": "{LAU_34_AGM_45B}",
        "name": "AGM-45B Shrike ARM (LAU-34)",
        "weight": 224,
    },
    "AGM_65E2_L___Maverick_E2_L__Laser_ASM___Lg_Whd___LAU_117_": {
        "clsid": "{HB_F4E_AGM-65L_LAU117}",
        "name": "AGM-65E2/L - Maverick E2/L (Laser ASM - Lg Whd) (LAU-117)",
        "weight": 351,
    },
    "AGM_65F___Maverick_F__IIR_ASM___Lg_Whd___LAU_117_": {
        "clsid": "{HB_F4E_AGM-65K_LAU117}",
        "name": "AGM-65F - Maverick F (IIR ASM - Lg Whd) (LAU-117)",
        "weight": 360,
    },
    "AGM_65H___Maverick_H__CCD_Imp_ASM___LAU_117_": {
        "clsid": "{HB_F4E_AGM-65H_LAU117}",
        "name": "AGM-65H - Maverick H (CCD Imp ASM) (LAU-117)",
        "weight": 267,
    },
    "AGM_78A_Standard_ARM_": {
        "clsid": "{LAU_77_AGM_78A}",
        "name": "AGM-78A Standard ARM",
        "weight": 654,
    },
    "AGM_78B_Standard_ARM_": {
        "clsid": "{LAU_77_AGM_78B}",
        "name": "AGM-78B Standard ARM",
        "weight": 659,
    },
    "AIM_4D_Falcon": {
        "clsid": "{AIM-4D}",
        "name": "AIM-4D Falcon",
        "weight": 60.770975056689,
    },
    "AIM_9D_Sidewinder_IR_AAM": {
        "clsid": "{AIM-9D}",
        "name": "AIM-9D Sidewinder IR AAM",
        "weight": 88.45,
    },
    "AIM_9G_Sidewinder_IR_AAM": {
        "clsid": "{AIM-9G}",
        "name": "AIM-9G Sidewinder IR AAM",
        "weight": 88.45,
    },
    "AIM_9H_Sidewinder_IR_AAM": {
        "clsid": "{AIM-9H}",
        "name": "AIM-9H Sidewinder IR AAM",
        "weight": 88.45,
    },
    "ALQ_184_Long___ECM_Pod_Rack": {
        "clsid": "{HB_ALQ-184_ON_ADAPTER_IN_AERO7}",
        "name": "ALQ-184 Long - ECM Pod Rack",
        "weight": 240.9,
    },
    "AN_AAQ_28_Litening___Targeting_Pod_Rack": {
        "clsid": "{HB_LITENING_ON_ADAPTER_IN_AERO7}",
        "name": "AN/AAQ-28 Litening - Targeting Pod Rack",
        "weight": 217.9,
    },
    "CATM_65K___Captive_Trg_Round_for_Mav_K__CCD___LAU_117_": {
        "clsid": "{HB_F4E_CATM-65K_LAU117}",
        "name": "CATM-65K - Captive Trg Round for Mav K (CCD) (LAU-117)",
        "weight": 356,
    },
    "GPU_5": {
        "clsid": "{GPU_5_POD}",
        "name": "GPU-5",
        "weight": 845.9498,
    },
    "TGM_65D___Trg_Round_for_Mav_D__IIR___LAU_117_": {
        "clsid": "{HB_F4E_TGM-65D_LAU117}",
        "name": "TGM-65D - Trg Round for Mav D (IIR) (LAU-117)",
        "weight": 277,
    },
    "TGM_65G___Trg_Round_for_Mav_G__IIR___LAU_117_": {
        "clsid": "{HB_F4E_TGM-65G_LAU117}",
        "name": "TGM-65G - Trg Round for Mav G (IIR) (LAU-117)",
        "weight": 360,
    },
    "TGM_65H___Trg_Round_for_Mav_H__CCD___LAU_117_": {
        "clsid": "{HB_F4E_TGM-65H_LAU117}",
        "name": "TGM-65H - Trg Round for Mav H (CCD) (LAU-117)",
        "weight": 267,
    },
    "_1x_AGM_65A___Maverick_A__TV_Guided___LAU_88_": {
        "clsid": "{HB_F4EAGM-65A_LAU88_1x}",
        "name": "1x AGM-65A - Maverick A (TV Guided) (LAU-88)",
        "weight": 421.5,
    },
    "_1x_AGM_65B___Maverick_B__TV_Guided___LAU_88_": {
        "clsid": "{HB_F4EAGM-65B_LAU88_1x}",
        "name": "1x AGM-65B - Maverick B (TV Guided) (LAU-88)",
        "weight": 421.5,
    },
    "_1x_AGM_65D___Maverick_D__IIR_ASM___LAU_88_": {
        "clsid": "{HB_F4EAGM-65D_LAU88_1x}",
        "name": "1x AGM-65D - Maverick D (IIR ASM) (LAU-88)",
        "weight": 421.5,
    },
    "_1x_AGM_65H___Maverick_H__CCD_Imp_ASM___LAU_88_": {
        "clsid": "{HB_F4EAGM-65H_LAU88_1x}",
        "name": "1x AGM-65H - Maverick H (CCD Imp ASM) (LAU-88)",
        "weight": 419,
    },
    "_1x_TGM_65D___Trg_Round_for_Mav_D__IIR___LAU_88_": {
        "clsid": "{HB_F4ETGM-65D_LAU88_1x}",
        "name": "1x TGM-65D - Trg Round for Mav D (IIR) (LAU-88)",
        "weight": 429,
    },
    "_1x_TGM_65H___Trg_Round_for_Mav_H__CCD___LAU_88_": {
        "clsid": "{HB_F4ETGM-65H_LAU88_1x}",
        "name": "1x TGM-65H - Trg Round for Mav H (CCD) (LAU-88)",
        "weight": 419,
    },
    "_2x_AGM_65H___Maverick_H__CCD_Imp_ASM___LAU_88_": {
        "clsid": "{HB_F4EAGM-65H_LAU88_2x_Right}",
        "name": "2x AGM-65H - Maverick H (CCD Imp ASM) (LAU-88)",
        "weight": 627,
    },
    "_2x_AGM_65H___Maverick_H__CCD_Imp_ASM___LAU_88__": {
        "clsid": "{HB_F4EAGM-65H_LAU88_2x_Left}",
        "name": "2x AGM-65H - Maverick H (CCD Imp ASM) (LAU-88)",
        "weight": 627,
    },
    "_2x_GBU_12___500lb_Laser_Guided_Bomb__TER__": {
        "clsid": "{HB_F4E_GBU-12_2x}",
        "name": "2x GBU-12 - 500lb Laser Guided Bomb (TER)",
        "weight": 682,
    },
    "_2x_LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT__TER___": {
        "clsid": "{HB_F4E_LAU-68_MK5_2x_Right}",
        "name": '2x LAU-68 pod - 7 x 2.75" FFAR, UnGd Rkts Mk5, HEAT (TER)',
        "weight": 348.6,
    },
    "_2x_LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT__TER____": {
        "clsid": "{HB_F4E_LAU-68_MK5_2x_Left}",
        "name": '2x LAU-68 pod - 7 x 2.75" FFAR, UnGd Rkts Mk5, HEAT (TER)',
        "weight": 348.6,
    },
    "_2x_M117___750lb_GP_Bomb_LD__TER___": {
        "clsid": "{HB_F4E_M117_2x_Left}",
        "name": "2x M117 - 750lb GP Bomb LD (TER)",
        "weight": 808,
    },
    "_2x_M117___750lb_GP_Bomb_LD__TER____": {
        "clsid": "{HB_F4E_M117_2x_Right}",
        "name": "2x M117 - 750lb GP Bomb LD (TER)",
        "weight": 808,
    },
    "_2x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets__TER___": {
        "clsid": "{HB_F4E_ROCKEYE_2x}",
        "name": "2x Mk-20 Rockeye - 490lbs CBU, 247 x HEAT Bomblets (TER)",
        "weight": 572,
    },
    "_2x_Mk_81___250lb_GP_Bomb_LD__TER___": {
        "clsid": "{HB_F4E_MK-81_2x}",
        "name": "2x Mk-81 - 250lb GP Bomb LD (TER)",
        "weight": 364,
    },
    "_2x_Mk_82_Snakeye___500lb_GP_Bomb_HD__TER___": {
        "clsid": "{HB_F4E_MK-82_Snakeye_2x}",
        "name": "2x Mk-82 Snakeye - 500lb GP Bomb HD (TER)",
        "weight": 627,
    },
    "_2x_Mk_82___500lb_GP_Bomb_LD__TER___": {
        "clsid": "{HB_F4E_MK-82_2x}",
        "name": "2x Mk-82 - 500lb GP Bomb LD (TER)",
        "weight": 584,
    },
    "Mk_82_SWA_2x": {
        "clsid": "2x Mk-82 SWA",
        "name": "2x Mk-82 - 500lb GP Bomb LD (SWA)",
        "weight": 584,
    },
    "_2x_Mk_83___1000lb_GP_Bomb_LD__MER___": {
        "clsid": "{HB_F4E_MK-83_MER_2x}",
        "name": "2x Mk-83 - 1000lb GP Bomb LD (MER)",
        "weight": 1007.8,
    },
    "_2x_Mk_83___1000lb_GP_Bomb_LD__TER___": {
        "clsid": "{HB_F4E_MK-83_2x_Left}",
        "name": "2x Mk-83 - 1000lb GP Bomb LD (TER)",
        "weight": 1036,
    },
    "_2x_Mk_83___1000lb_GP_Bomb_LD__TER____": {
        "clsid": "{HB_F4E_MK-83_2x_Right}",
        "name": "2x Mk-83 - 1000lb GP Bomb LD (TER)",
        "weight": 1036,
    },
    "_2x_SUU_25_x_8_LUU_2___Target_Marker_Flares__MER____": {
        "clsid": "{HB_F4E_SUU-25_MER_2x_Right}",
        "name": "2x SUU-25 x 8 LUU-2 - Target Marker Flares (MER)",
        "weight": 553.4,
    },
    "_2x_SUU_25_x_8_LUU_2___Target_Marker_Flares__MER_____": {
        "clsid": "{HB_F4E_SUU-25_MER_2x}",
        "name": "2x SUU-25 x 8 LUU-2 - Target Marker Flares (MER)",
        "weight": 553.4,
    },
    "_2x_TGM_65D___Trg_Round_for_Mav_D__IIR___LAU_88_": {
        "clsid": "{HB_F4ETGM-65D_LAU88_2x_Right}",
        "name": "2x TGM-65D - Trg Round for Mav D (IIR) (LAU-88)",
        "weight": 647,
    },
    "_2x_TGM_65D___Trg_Round_for_Mav_D__IIR___LAU_88__": {
        "clsid": "{HB_F4ETGM-65D_LAU88_2x_Left}",
        "name": "2x TGM-65D - Trg Round for Mav D (IIR) (LAU-88)",
        "weight": 647,
    },
    "_2x_TGM_65H___Trg_Round_for_Mav_H__CCD___LAU_88_": {
        "clsid": "{HB_F4ETGM-65H_LAU88_2x_Right}",
        "name": "2x TGM-65H - Trg Round for Mav H (CCD) (LAU-88)",
        "weight": 627,
    },
    "_2x_TGM_65H___Trg_Round_for_Mav_H__CCD___LAU_88__": {
        "clsid": "{HB_F4ETGM-65H_LAU88_2x_Left}",
        "name": "2x TGM-65H - Trg Round for Mav H (CCD) (LAU-88)",
        "weight": 627,
    },
    "_3x_AGM_65H___Maverick_H__CCD_Imp_ASM___LAU_88_": {
        "clsid": "{HB_F4EAGM-65H_LAU88_3x_Right}",
        "name": "3x AGM-65H - Maverick H (CCD Imp ASM) (LAU-88)",
        "weight": 835,
    },
    "_3x_AGM_65H___Maverick_H__CCD_Imp_ASM___LAU_88__": {
        "clsid": "{HB_F4EAGM-65H_LAU88_3x_Left}",
        "name": "3x AGM-65H - Maverick H (CCD Imp ASM) (LAU-88)",
        "weight": 835,
    },
    "_3x_BDU_33___25lb_Practice_Bomb_LD__TER__": {
        "clsid": "{HB_F4E_BDU-33_3x}",
        "name": "3x BDU-33 - 25lb Practice Bomb LD (TER)",
        "weight": 161.9,
    },
    "_3x_LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT__TER__": {
        "clsid": "{HB_F4E_LAU-68_MK5_3x}",
        "name": '3x LAU-68 pod - 7 x 2.75" FFAR, UnGd Rkts Mk5, HEAT (TER)',
        "weight": 458.9,
    },
    "_3x_M117___750lb_GP_Bomb_LD__TER__": {
        "clsid": "{HB_F4E_M117_3x}",
        "name": "3x M117 - 750lb GP Bomb LD (TER)",
        "weight": 1148,
    },
    "_3x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets__TER__": {
        "clsid": "{HB_F4E_ROCKEYE_3x}",
        "name": "3x Mk-20 Rockeye - 490lbs CBU, 247 x HEAT Bomblets (TER)",
        "weight": 794,
    },
    "_3x_Mk_81___250lb_GP_Bomb_LD__TER__": {
        "clsid": "{HB_F4E_MK-81_3x}",
        "name": "3x Mk-81 - 250lb GP Bomb LD (TER)",
        "weight": 482,
    },
    "_3x_Mk_82_Snakeye___500lb_GP_Bomb_HD__TER__": {
        "clsid": "{HB_F4E_MK-82_Snakeye_3x}",
        "name": "3x Mk-82 Snakeye - 500lb GP Bomb HD (TER)",
        "weight": 876.5,
    },
    "_3x_Mk_82___500lb_GP_Bomb_LD__TER__": {
        "clsid": "{HB_F4E_MK-82_3x}",
        "name": "3x Mk-82 - 500lb GP Bomb LD (TER)",
        "weight": 812,
    },
    "_3x_Mk_83___1000lb_GP_Bomb_LD__MER___": {
        "clsid": "{HB_F4E_MK-83_MER_3x}",
        "name": "3x Mk-83 - 1000lb GP Bomb LD (MER)",
        "weight": 1461.8,
    },
    "_3x_Mk_83___1000lb_GP_Bomb_LD__TER__": {
        "clsid": "{HB_F4E_MK-83_3x}",
        "name": "3x Mk-83 - 1000lb GP Bomb LD (TER)",
        "weight": 1490,
    },
    "_3x_TGM_65D___Trg_Round_for_Mav_D__IIR___LAU_88_": {
        "clsid": "{HB_F4ETGM-65D_LAU88_3x_Right}",
        "name": "3x TGM-65D - Trg Round for Mav D (IIR) (LAU-88)",
        "weight": 865,
    },
    "_3x_TGM_65D___Trg_Round_for_Mav_D__IIR___LAU_88__": {
        "clsid": "{HB_F4ETGM-65D_LAU88_3x_Left}",
        "name": "3x TGM-65D - Trg Round for Mav D (IIR) (LAU-88)",
        "weight": 865,
    },
    "_3x_TGM_65H___Trg_Round_for_Mav_H__CCD___LAU_88_": {
        "clsid": "{HB_F4ETGM-65H_LAU88_3x_Right}",
        "name": "3x TGM-65H - Trg Round for Mav H (CCD) (LAU-88)",
        "weight": 835,
    },
    "_3x_TGM_65H___Trg_Round_for_Mav_H__CCD___LAU_88__": {
        "clsid": "{HB_F4ETGM-65H_LAU88_3x_Left}",
        "name": "3x TGM-65H - Trg Round for Mav H (CCD) (LAU-88)",
        "weight": 835,
    },
    "_6x_BDU_33___25lb_Practice_Bomb_LD__MER__": {
        "clsid": "{HB_F4E_BDU-33_6x}",
        "name": "6x BDU-33 - 25lb Practice Bomb LD (MER)",
        "weight": 167.6,
    },
    "_6x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets__MER__": {
        "clsid": "{HB_F4E_ROCKEYE_6x}",
        "name": "6x Mk-20 Rockeye - 490lbs CBU, 247 x HEAT Bomblets (MER)",
        "weight": 1431.8,
    },
    "_6x_Mk_81___250lb_GP_Bomb_LD__MER__": {
        "clsid": "{HB_F4E_MK-81_6x}",
        "name": "6x Mk-81 - 250lb GP Bomb LD (MER)",
        "weight": 807.8,
    },
    "_6x_Mk_82_Snakeye___500lb_GP_Bomb_HD__MER__": {
        "clsid": "{HB_F4E_MK-82_Snakeye_6x}",
        "name": "6x Mk-82 Snakeye - 500lb GP Bomb HD (MER)",
        "weight": 1596.8,
    },
    "_6x_Mk_82___500lb_GP_Bomb_LD__MER__": {
        "clsid": "{HB_F4E_MK-82_6x}",
        "name": "6x Mk-82 - 500lb GP Bomb LD (MER)",
        "weight": 1467.8,
    },
    "_Special_Weapons_Adapter__AGM_45B_Shrike_ARM__LAU_34_": {
        "clsid": "{LAU_34_AGM_45B_SWA}",
        "name": "(Special Weapons Adapter) AGM-45B Shrike ARM (LAU-34)",
        "weight": 224,
    },
    "_Special_Weapons_Adapter__AGM_65H___Maverick_H__CCD_Imp_ASM___LAU_117__Special_Weapons_Adapter__": {
        "clsid": "{HB_F4E_AGM-65H_LAU117_SWA}",
        "name": "(Special Weapons Adapter) AGM-65H - Maverick H (CCD Imp ASM) (LAU-117)(Special Weapons Adapter) ",
        "weight": 267,
    },
    "_Special_Weapons_Adapter__TGM_65D___Trg_Round_for_Mav_D__IIR___LAU_117__Special_Weapons_Adapter__": {
        "clsid": "{HB_F4E_TGM-65D_LAU117_SWA}",
        "name": "(Special Weapons Adapter) TGM-65D - Trg Round for Mav D (IIR) (LAU-117)(Special Weapons Adapter) ",
        "weight": 277,
    },
    "_Special_Weapons_Adapter__TGM_65H___Trg_Round_for_Mav_H__CCD___LAU_117__Special_Weapons_Adapter__": {
        "clsid": "{HB_F4E_TGM-65H_LAU117_SWA}",
        "name": "(Special Weapons Adapter) TGM-65H - Trg Round for Mav H (CCD) (LAU-117)(Special Weapons Adapter) ",
        "weight": 267,
    },
}


class WeaponsF4EExpanded:
    pass


for weapon_name, weapon_def in MISSING_WEAPON_DEFS.items():
    setattr(WeaponsF4EExpanded, weapon_name, weapon_def)

WEAPON_ID_OVERRIDES: Dict[str, str] = {
    "{LAU_34_AGM_45B}": "AGM_45B_Shrike_ARM__LAU_34_",
    "{HB_F4E_AGM-65L_LAU117}": "AGM_65E2_L___Maverick_E2_L__Laser_ASM___Lg_Whd___LAU_117_",
    "{HB_F4E_AGM-65K_LAU117}": "AGM_65F___Maverick_F__IIR_ASM___Lg_Whd___LAU_117_",
    "{HB_F4E_AGM-65H_LAU117}": "AGM_65H___Maverick_H__CCD_Imp_ASM___LAU_117_",
    "{LAU_77_AGM_78A}": "AGM_78A_Standard_ARM_",
    "{LAU_77_AGM_78B}": "AGM_78B_Standard_ARM_",
    "{B06DD79A-F21E-4EB9-BD9D-AB3844618C93}": "AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_",
    "{C8E06185-7CD6-4C90-959F-044679E90751}": "AIM_120B_AMRAAM___Active_Radar_AAM",
    "{40EF17B7-F508-45de-8566-6FFECC0C1AB8}": "AIM_120C_AMRAAM___Active_Radar_AAM",
    "{AIM-4D}": "AIM_4D_Falcon",
    "{HB_F4E_AIM-7MH}": "AIM_7MH",
    "{HB_F4E_AIM-7P}": "AIM_7P",
    "{AIM-9D}": "AIM_9D_Sidewinder_IR_AAM",
    "{AIM-9G}": "AIM_9G_Sidewinder_IR_AAM",
    "{AIM-9H}": "AIM_9H_Sidewinder_IR_AAM",
    "{HB_ALQ-184_ON_ADAPTER_IN_AERO7}": "ALQ_184_Long___ECM_Pod_Rack",
    "{HB_LITENING_ON_ADAPTER_IN_AERO7}": "AN_AAQ_28_Litening___Targeting_Pod_Rack",
    "{AN_AXQ_14}": "AN_AXQ_14_Data_Link_Pod",
    "{HB_F4E_CATM-65K_LAU117}": "CATM_65K___Captive_Trg_Round_for_Mav_K__CCD___LAU_117_",
    "{GBU-15V1}": "GBU_15_V1___2000_lb_TV_Guided_Bomb",
    "{GPU_5_POD}": "GPU_5",
    "{SUU_23_POD}": "SUU_23",
    "{HB_F4E_TGM-65D_LAU117}": "TGM_65D___Trg_Round_for_Mav_D__IIR___LAU_117_",
    "{HB_F4E_TGM-65G_LAU117}": "TGM_65G___Trg_Round_for_Mav_G__IIR___LAU_117_",
    "{HB_F4E_TGM-65H_LAU117}": "TGM_65H___Trg_Round_for_Mav_H__CCD___LAU_117_",
    "{HB_F4EAGM-65A_LAU88_1x}": "_1x_AGM_65A___Maverick_A__TV_Guided___LAU_88_",
    "{HB_F4EAGM-65B_LAU88_1x}": "_1x_AGM_65B___Maverick_B__TV_Guided___LAU_88_",
    "{HB_F4EAGM-65D_LAU88_1x}": "_1x_AGM_65D___Maverick_D__IIR_ASM___LAU_88_",
    "{HB_F4EAGM-65H_LAU88_1x}": "_1x_AGM_65H___Maverick_H__CCD_Imp_ASM___LAU_88_",
    "{HB_F4ETGM-65D_LAU88_1x}": "_1x_TGM_65D___Trg_Round_for_Mav_D__IIR___LAU_88_",
    "{HB_F4ETGM-65H_LAU88_1x}": "_1x_TGM_65H___Trg_Round_for_Mav_H__CCD___LAU_88_",
    "{HB_F4EAGM-65H_LAU88_2x_Right}": "_2x_AGM_65H___Maverick_H__CCD_Imp_ASM___LAU_88_",
    "{HB_F4EAGM-65H_LAU88_2x_Left}": "_2x_AGM_65H___Maverick_H__CCD_Imp_ASM___LAU_88__",
    "{HB_F4E_GBU-12_2x}": "_2x_GBU_12___500lb_Laser_Guided_Bomb__TER__",
    "{HB_F4E_LAU-68_MK5_2x_Right}": "_2x_LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT__TER___",
    "{HB_F4E_LAU-68_MK5_2x_Left}": "_2x_LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT__TER____",
    "{HB_F4E_M117_2x_Left}": "_2x_M117___750lb_GP_Bomb_LD__TER___",
    "{HB_F4E_M117_2x_Right}": "_2x_M117___750lb_GP_Bomb_LD__TER____",
    "{HB_F4E_ROCKEYE_2x}": "_2x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets__TER___",
    "{HB_F4E_MK-81_2x}": "_2x_Mk_81___250lb_GP_Bomb_LD__TER___",
    "{HB_F4E_MK-82_Snakeye_2x}": "_2x_Mk_82_Snakeye___500lb_GP_Bomb_HD__TER___",
    "{HB_F4E_MK-82_2x}": "_2x_Mk_82___500lb_GP_Bomb_LD__TER___",
    "2x Mk-82 SWA": "Mk_82_SWA_2x",
    "{HB_F4E_MK-83_MER_2x}": "_2x_Mk_83___1000lb_GP_Bomb_LD__MER___",
    "{HB_F4E_MK-83_2x_Left}": "_2x_Mk_83___1000lb_GP_Bomb_LD__TER___",
    "{HB_F4E_MK-83_2x_Right}": "_2x_Mk_83___1000lb_GP_Bomb_LD__TER____",
    "{HB_F4E_SUU-25_MER_2x_Left}": "_2x_SUU_25_x_8_LUU_2___Target_Marker_Flares__MER___",
    "{HB_F4E_SUU-25_MER_2x_Right}": "_2x_SUU_25_x_8_LUU_2___Target_Marker_Flares__MER____",
    "{HB_F4E_SUU-25_MER_2x}": "_2x_SUU_25_x_8_LUU_2___Target_Marker_Flares__MER_____",
    "{HB_F4ETGM-65D_LAU88_2x_Right}": "_2x_TGM_65D___Trg_Round_for_Mav_D__IIR___LAU_88_",
    "{HB_F4ETGM-65D_LAU88_2x_Left}": "_2x_TGM_65D___Trg_Round_for_Mav_D__IIR___LAU_88__",
    "{HB_F4ETGM-65H_LAU88_2x_Right}": "_2x_TGM_65H___Trg_Round_for_Mav_H__CCD___LAU_88_",
    "{HB_F4ETGM-65H_LAU88_2x_Left}": "_2x_TGM_65H___Trg_Round_for_Mav_H__CCD___LAU_88__",
    "{HB_F4EAGM-65H_LAU88_3x_Right}": "_3x_AGM_65H___Maverick_H__CCD_Imp_ASM___LAU_88_",
    "{HB_F4EAGM-65H_LAU88_3x_Left}": "_3x_AGM_65H___Maverick_H__CCD_Imp_ASM___LAU_88__",
    "{HB_F4E_BDU-33_3x}": "_3x_BDU_33___25lb_Practice_Bomb_LD__TER__",
    "{HB_F4E_LAU-68_MK5_3x}": "_3x_LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT__TER__",
    "{HB_F4E_M117_3x}": "_3x_M117___750lb_GP_Bomb_LD__TER__",
    "{HB_F4E_ROCKEYE_3x}": "_3x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets__TER__",
    "{HB_F4E_MK-81_3x}": "_3x_Mk_81___250lb_GP_Bomb_LD__TER__",
    "{HB_F4E_MK-82_Snakeye_3x}": "_3x_Mk_82_Snakeye___500lb_GP_Bomb_HD__TER__",
    "{HB_F4E_MK-82_3x}": "_3x_Mk_82___500lb_GP_Bomb_LD__TER__",
    "{HB_F4E_MK-83_MER_3x}": "_3x_Mk_83___1000lb_GP_Bomb_LD__MER___",
    "{HB_F4E_MK-83_3x}": "_3x_Mk_83___1000lb_GP_Bomb_LD__TER__",
    "{HB_F4ETGM-65D_LAU88_3x_Right}": "_3x_TGM_65D___Trg_Round_for_Mav_D__IIR___LAU_88_",
    "{HB_F4ETGM-65D_LAU88_3x_Left}": "_3x_TGM_65D___Trg_Round_for_Mav_D__IIR___LAU_88__",
    "{HB_F4ETGM-65H_LAU88_3x_Right}": "_3x_TGM_65H___Trg_Round_for_Mav_H__CCD___LAU_88_",
    "{HB_F4ETGM-65H_LAU88_3x_Left}": "_3x_TGM_65H___Trg_Round_for_Mav_H__CCD___LAU_88__",
    "{HB_F4E_BDU-33_6x}": "_6x_BDU_33___25lb_Practice_Bomb_LD__MER__",
    "{HB_F4E_ROCKEYE_6x}": "_6x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets__MER__",
    "{HB_F4E_MK-81_6x}": "_6x_Mk_81___250lb_GP_Bomb_LD__MER__",
    "{HB_F4E_MK-82_Snakeye_6x}": "_6x_Mk_82_Snakeye___500lb_GP_Bomb_HD__MER__",
    "{HB_F4E_MK-82_6x}": "_6x_Mk_82___500lb_GP_Bomb_LD__MER__",
    "{LAU_34_AGM_45B_SWA}": "_Special_Weapons_Adapter__AGM_45B_Shrike_ARM__LAU_34_",
    "{HB_F4E_AGM-65H_LAU117_SWA}": "_Special_Weapons_Adapter__AGM_65H___Maverick_H__CCD_Imp_ASM___LAU_117__Special_Weapons_Adapter__",
    "{HB_F4E_TGM-65D_LAU117_SWA}": "_Special_Weapons_Adapter__TGM_65D___Trg_Round_for_Mav_D__IIR___LAU_117__Special_Weapons_Adapter__",
    "{HB_F4E_TGM-65H_LAU117_SWA}": "_Special_Weapons_Adapter__TGM_65H___Trg_Round_for_Mav_H__CCD___LAU_117__Special_Weapons_Adapter__",
}

PYLON_ADDITIONS: Dict[str, Iterable[str]] = {
    "Pylon1": [
        "AGM_45B_Shrike_ARM__LAU_34_",
        "AGM_78A_Standard_ARM_",
        "AGM_78B_Standard_ARM_",
        "AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_",
        "_2x_Mk_83___1000lb_GP_Bomb_LD__MER___",
        "_2x_SUU_25_x_8_LUU_2___Target_Marker_Flares__MER___",
        "_6x_BDU_33___25lb_Practice_Bomb_LD__MER__",
        "_6x_Mk_81___250lb_GP_Bomb_LD__MER__",
        "_6x_Mk_82_Snakeye___500lb_GP_Bomb_HD__MER__",
        "_6x_Mk_82___500lb_GP_Bomb_LD__MER__",
    ],
    "Pylon2": [
        "AIM_4D_Falcon",
        "AIM_9D_Sidewinder_IR_AAM",
        "AIM_9G_Sidewinder_IR_AAM",
        "AIM_9H_Sidewinder_IR_AAM",
    ],
    "Pylon3": [
        "AGM_45B_Shrike_ARM__LAU_34_",
        "AGM_65E2_L___Maverick_E2_L__Laser_ASM___Lg_Whd___LAU_117_",
        "AGM_65F___Maverick_F__IIR_ASM___Lg_Whd___LAU_117_",
        "AGM_65H___Maverick_H__CCD_Imp_ASM___LAU_117_",
        "AGM_78A_Standard_ARM_",
        "AGM_78B_Standard_ARM_",
        "AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_",
        "CATM_65K___Captive_Trg_Round_for_Mav_K__CCD___LAU_117_",
        "GBU_15_V1___2000_lb_TV_Guided_Bomb",
        "GPU_5",
        "SUU_23",
        "TGM_65D___Trg_Round_for_Mav_D__IIR___LAU_117_",
        "TGM_65G___Trg_Round_for_Mav_G__IIR___LAU_117_",
        "TGM_65H___Trg_Round_for_Mav_H__CCD___LAU_117_",
        "_1x_AGM_65A___Maverick_A__TV_Guided___LAU_88_",
        "_1x_AGM_65B___Maverick_B__TV_Guided___LAU_88_",
        "_1x_AGM_65D___Maverick_D__IIR_ASM___LAU_88_",
        "_1x_AGM_65H___Maverick_H__CCD_Imp_ASM___LAU_88_",
        "_1x_TGM_65D___Trg_Round_for_Mav_D__IIR___LAU_88_",
        "_1x_TGM_65H___Trg_Round_for_Mav_H__CCD___LAU_88_",
        "_2x_AGM_65H___Maverick_H__CCD_Imp_ASM___LAU_88__",
        "_2x_GBU_12___500lb_Laser_Guided_Bomb__TER__",
        "_2x_LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT__TER____",
        "_2x_M117___750lb_GP_Bomb_LD__TER___",
        "_2x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets__TER___",
        "_2x_Mk_81___250lb_GP_Bomb_LD__TER___",
        "_2x_Mk_82_Snakeye___500lb_GP_Bomb_HD__TER___",
        "_2x_Mk_82___500lb_GP_Bomb_LD__TER___",
        "_2x_Mk_83___1000lb_GP_Bomb_LD__TER___",
        "_2x_TGM_65D___Trg_Round_for_Mav_D__IIR___LAU_88__",
        "_2x_TGM_65H___Trg_Round_for_Mav_H__CCD___LAU_88__",
        "_3x_AGM_65H___Maverick_H__CCD_Imp_ASM___LAU_88__",
        "_3x_BDU_33___25lb_Practice_Bomb_LD__TER__",
        "_3x_LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT__TER__",
        "_3x_M117___750lb_GP_Bomb_LD__TER__",
        "_3x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets__TER__",
        "_3x_Mk_81___250lb_GP_Bomb_LD__TER__",
        "_3x_Mk_82_Snakeye___500lb_GP_Bomb_HD__TER__",
        "_3x_Mk_82___500lb_GP_Bomb_LD__TER__",
        "_3x_Mk_83___1000lb_GP_Bomb_LD__TER__",
        "_3x_TGM_65D___Trg_Round_for_Mav_D__IIR___LAU_88__",
        "_3x_TGM_65H___Trg_Round_for_Mav_H__CCD___LAU_88__",
        "_Special_Weapons_Adapter__AGM_45B_Shrike_ARM__LAU_34_",
        "_Special_Weapons_Adapter__AGM_65H___Maverick_H__CCD_Imp_ASM___LAU_117__Special_Weapons_Adapter__",
        "_Special_Weapons_Adapter__TGM_65D___Trg_Round_for_Mav_D__IIR___LAU_117__Special_Weapons_Adapter__",
        "_Special_Weapons_Adapter__TGM_65H___Trg_Round_for_Mav_H__CCD___LAU_117__Special_Weapons_Adapter__",
    ],
    "Pylon4": [
        "AIM_4D_Falcon",
        "AIM_9D_Sidewinder_IR_AAM",
        "AIM_9G_Sidewinder_IR_AAM",
        "AIM_9H_Sidewinder_IR_AAM",
    ],
    "Pylon5": [
        "AIM_120B_AMRAAM___Active_Radar_AAM",
        "AIM_120C_AMRAAM___Active_Radar_AAM",
        "AIM_7MH",
        "AIM_7P",
    ],
    "Pylon6": [
        "AIM_120B_AMRAAM___Active_Radar_AAM",
        "AIM_120C_AMRAAM___Active_Radar_AAM",
        "AIM_7MH",
        "AIM_7P",
        "ALQ_184_Long___ECM_Pod_Rack",
        "AN_AAQ_28_Litening___Targeting_Pod_Rack",
    ],
    "Pylon7": [
        "AN_AXQ_14_Data_Link_Pod",
        "GPU_5",
        "_2x_SUU_25_x_8_LUU_2___Target_Marker_Flares__MER_____",
        "_3x_Mk_83___1000lb_GP_Bomb_LD__MER___",
        "_6x_BDU_33___25lb_Practice_Bomb_LD__MER__",
        "_6x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets__MER__",
        "_6x_Mk_81___250lb_GP_Bomb_LD__MER__",
        "_6x_Mk_82_Snakeye___500lb_GP_Bomb_HD__MER__",
        "_6x_Mk_82___500lb_GP_Bomb_LD__MER__",
    ],
    "Pylon8": [
        "AIM_120B_AMRAAM___Active_Radar_AAM",
        "AIM_120C_AMRAAM___Active_Radar_AAM",
        "AIM_7MH",
        "AIM_7P",
    ],
    "Pylon9": [
        "AIM_120B_AMRAAM___Active_Radar_AAM",
        "AIM_120C_AMRAAM___Active_Radar_AAM",
        "AIM_7MH",
        "AIM_7P",
    ],
    "Pylon10": [
        "AIM_4D_Falcon",
        "AIM_9D_Sidewinder_IR_AAM",
        "AIM_9G_Sidewinder_IR_AAM",
        "AIM_9H_Sidewinder_IR_AAM",
    ],
    "Pylon11": [
        "AGM_45B_Shrike_ARM__LAU_34_",
        "AGM_65E2_L___Maverick_E2_L__Laser_ASM___Lg_Whd___LAU_117_",
        "AGM_65F___Maverick_F__IIR_ASM___Lg_Whd___LAU_117_",
        "AGM_65H___Maverick_H__CCD_Imp_ASM___LAU_117_",
        "AGM_78A_Standard_ARM_",
        "AGM_78B_Standard_ARM_",
        "AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_",
        "CATM_65K___Captive_Trg_Round_for_Mav_K__CCD___LAU_117_",
        "GBU_15_V1___2000_lb_TV_Guided_Bomb",
        "GPU_5",
        "SUU_23",
        "TGM_65D___Trg_Round_for_Mav_D__IIR___LAU_117_",
        "TGM_65G___Trg_Round_for_Mav_G__IIR___LAU_117_",
        "TGM_65H___Trg_Round_for_Mav_H__CCD___LAU_117_",
        "_1x_AGM_65A___Maverick_A__TV_Guided___LAU_88_",
        "_1x_AGM_65B___Maverick_B__TV_Guided___LAU_88_",
        "_1x_AGM_65D___Maverick_D__IIR_ASM___LAU_88_",
        "_1x_AGM_65H___Maverick_H__CCD_Imp_ASM___LAU_88_",
        "_1x_TGM_65D___Trg_Round_for_Mav_D__IIR___LAU_88_",
        "_1x_TGM_65H___Trg_Round_for_Mav_H__CCD___LAU_88_",
        "_2x_AGM_65H___Maverick_H__CCD_Imp_ASM___LAU_88_",
        "_2x_GBU_12___500lb_Laser_Guided_Bomb__TER__",
        "_2x_LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT__TER___",
        "_2x_M117___750lb_GP_Bomb_LD__TER____",
        "_2x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets__TER___",
        "_2x_Mk_81___250lb_GP_Bomb_LD__TER___",
        "_2x_Mk_82_Snakeye___500lb_GP_Bomb_HD__TER___",
        "_2x_Mk_82___500lb_GP_Bomb_LD__TER___",
        "_2x_Mk_83___1000lb_GP_Bomb_LD__TER____",
        "_2x_TGM_65D___Trg_Round_for_Mav_D__IIR___LAU_88_",
        "_2x_TGM_65H___Trg_Round_for_Mav_H__CCD___LAU_88_",
        "_3x_AGM_65H___Maverick_H__CCD_Imp_ASM___LAU_88_",
        "_3x_BDU_33___25lb_Practice_Bomb_LD__TER__",
        "_3x_LAU_68_pod___7_x_2_75_FFAR__UnGd_Rkts_Mk5__HEAT__TER__",
        "_3x_M117___750lb_GP_Bomb_LD__TER__",
        "_3x_Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets__TER__",
        "_3x_Mk_81___250lb_GP_Bomb_LD__TER__",
        "_3x_Mk_82_Snakeye___500lb_GP_Bomb_HD__TER__",
        "_3x_Mk_82___500lb_GP_Bomb_LD__TER__",
        "_3x_Mk_83___1000lb_GP_Bomb_LD__TER__",
        "_3x_TGM_65D___Trg_Round_for_Mav_D__IIR___LAU_88_",
        "_3x_TGM_65H___Trg_Round_for_Mav_H__CCD___LAU_88_",
        "_Special_Weapons_Adapter__AGM_45B_Shrike_ARM__LAU_34_",
        "_Special_Weapons_Adapter__AGM_65H___Maverick_H__CCD_Imp_ASM___LAU_117__Special_Weapons_Adapter__",
        "_Special_Weapons_Adapter__TGM_65D___Trg_Round_for_Mav_D__IIR___LAU_117__Special_Weapons_Adapter__",
        "_Special_Weapons_Adapter__TGM_65H___Trg_Round_for_Mav_H__CCD___LAU_117__Special_Weapons_Adapter__",
    ],
    "Pylon12": [
        "AIM_4D_Falcon",
        "AIM_9D_Sidewinder_IR_AAM",
        "AIM_9G_Sidewinder_IR_AAM",
        "AIM_9H_Sidewinder_IR_AAM",
    ],
    "Pylon13": [
        "AGM_45B_Shrike_ARM__LAU_34_",
        "AGM_78A_Standard_ARM_",
        "AGM_78B_Standard_ARM_",
        "AGM_88C_HARM___High_Speed_Anti_Radiation_Missile_",
        "_2x_Mk_83___1000lb_GP_Bomb_LD__MER___",
        "_2x_SUU_25_x_8_LUU_2___Target_Marker_Flares__MER____",
        "_6x_BDU_33___25lb_Practice_Bomb_LD__MER__",
        "_6x_Mk_81___250lb_GP_Bomb_LD__MER__",
        "_6x_Mk_82_Snakeye___500lb_GP_Bomb_HD__MER__",
        "_6x_Mk_82___500lb_GP_Bomb_LD__MER__",
    ],
}


def _inject_weapon_id_overrides() -> None:
    for clsid, name in WEAPON_ID_OVERRIDES.items():
        weapon = getattr(Weapons, name, None)
        if weapon is not None:
            weapon_ids[clsid] = weapon


def _build_pylon_class(pylon_number: int, additions: Iterable[str]) -> type:
    attrs: Dict[str, object] = {}
    for weapon_name in additions:
        weapon = getattr(Weapons, weapon_name, None)
        if weapon is None:
            continue
        attrs[weapon_name] = (pylon_number, weapon)
    return type(f"F4EExpandedPylon{pylon_number}", (), attrs)


def _build_pylon_additions() -> dict[str, type]:
    pylons: dict[str, type] = {}
    for pylon_name, additions in PYLON_ADDITIONS.items():
        pylon_number = int(pylon_name.replace("Pylon", ""))
        pylons[pylon_name] = _build_pylon_class(pylon_number, additions)
    return pylons


inject_weapons(WeaponsF4EExpanded)
_inject_weapon_id_overrides()
_F4E_EXPANDED_PYLONS = _build_pylon_additions()


def inject_F4EExpanded() -> None:
    """Inject expanded weapons into F-4E-45MC pylons."""
    for pylon_name, additions in _F4E_EXPANDED_PYLONS.items():
        target_pylon = getattr(F_4E_45MC, pylon_name, None)
        if target_pylon is None:
            continue
        inject_pylon(target_pylon, additions)


def eject_F4EExpanded() -> None:
    """Remove expanded weapons from F-4E-45MC pylons."""
    for pylon_name, additions in _F4E_EXPANDED_PYLONS.items():
        target_pylon = getattr(F_4E_45MC, pylon_name, None)
        if target_pylon is None:
            continue
        eject_pylon(target_pylon, additions)


__all__ = ["inject_F4EExpanded", "eject_F4EExpanded", "WeaponsF4EExpanded"]
