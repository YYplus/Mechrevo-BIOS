# MECHREVO Jiaolong 16 Pro

[简体中文](README.md) | [English](README_EN.md)

## Series information

Jiaolong 16 Pro is a continuously updated model series. Different model years and configurations may use different BIOS platforms. Firmware selection must follow the actual BIOS platform rather than the marketing model name alone.

| Platform / configuration | Current known BIOS | EC |
|---|---|---|
| 2023 / `MRID6-23` (Ryzen 9 7945HX + RTX 4060) | `MRID6_23_V40` | `unknown` |
| `X6DR5xxK` | `N.1.49MRO58` | `unknown` |
| 2025 / `X6FR55xx` | `N.1.39MRO55` | `unknown` |

## BIOS

| Platform | Version | File | Official source |
|---|---|---|---|
| `MRID6-23` (2023) | `MRID6_23_V40` | `MRID6_23_V40.exe` (not archived) | [MECHREVO](https://driver.mechrevo.com/d.mechrevo.com/driver/MECHREVO2023/JL16Pro/MRID6_23_V40.exe) |
| `X6DR5xxK` | `N.1.49MRO58` | [`X6DR5xxKN149MRO58_CAP.EXE`](firmware/X6DR5xxKN149MRO58_CAP.EXE) | [MECHREVO](https://driver.mechrevo.com/d.mechrevo.com/driver/BIOS/GX_AMDDragon/X6DR5xxKN149MRO58_CAP.EXE) |
| `X6DR5xxK` | `N.1.40MRO56` | [`X6DR5xxKN140MRO56_CAP.EXE`](firmware/X6DR5xxKN140MRO56_CAP.EXE) | [MECHREVO](https://driver.mechrevo.com/d.mechrevo.com/driver/MECHREVO2026/BIOS/X6DR5xxKN140MRO56_CAP.EXE) |
| `X6FR55xx` | `N.1.39MRO55` | `X6FR55xxN139MRO55_CAP.EXE` | [MECHREVO](https://driver.mechrevo.com/d.mechrevo.com/driver/MECHREVO2025/TBIOS/X6FR55xxN139MRO55_CAP.EXE) |

## Known information

- MECHREVO customer support provided `MRID6_23_V40.exe` for a 2023 Jiaolong 16 Pro with Ryzen 9 7945HX + RTX 4060. The **first restart after updating may be unusually slow**; subsequent restarts return to normal (user report).
- Thanks to @Blackstone234 for sharing the [new BIOS information in Issue #1](https://github.com/YYplus/Mechrevo-BIOS/issues/1#issuecomment-6741848173): a 2025 Jiaolong 16 Pro with Ryzen 9 8945HX + GeForce RTX 5070 Ti received `X6DR5xxKN149MRO58_CAP.EXE` (`N.1.49MRO58`) through the control-center update channel.
- The 8945HX + RTX 5070 Ti configuration is recorded only as a known update case and is not used to infer identical applicability across every `X6DR5xxK` configuration.
- Public launch information confirms a 2025 Jiaolong 16 Pro configuration with Ryzen 9 9955HX + GeForce RTX 5070 Ti.
- `X6FR55xx` is a BIOS platform identifier and should not be interpreted as exclusive to the RTX 5070 Ti configuration.
- BIOS packages for different platforms must not be treated as interchangeable solely because they share the Jiaolong 16 Pro series name.
