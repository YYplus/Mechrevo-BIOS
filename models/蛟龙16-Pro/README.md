# 机械革命 蛟龙 16 Pro

[简体中文](README.md) | [English](README_EN.md)

## 系列信息

蛟龙 16 Pro 为持续更新的机型系列，不同年份和配置可能使用不同 BIOS 平台。固件应以实际 BIOS 平台为准，不能仅凭“蛟龙 16 Pro”名称互刷。

| 平台 / 配置 | 当前已知 BIOS | EC |
|---|---|---|
| 2023 款 / `MRID6-23`（Ryzen 9 7945HX + RTX 4060） | `MRID6_23_V40` | `unknown` |
| `X6DR5xxK` | `N.1.49MRO58` | `unknown` |
| 2025 款 / `X6FR55xx` | `N.1.39MRO55` | `unknown` |

## BIOS

| 平台 | 版本 | 文件 | 官方来源 |
|---|---|---|---|
| `MRID6-23`（2023） | `MRID6_23_V40` | `MRID6_23_V40.exe`（尚未归档） | [机械革命官方](https://driver.mechrevo.com/d.mechrevo.com/driver/MECHREVO2023/JL16Pro/MRID6_23_V40.exe) |
| `X6DR5xxK` | `N.1.49MRO58` | [`X6DR5xxKN149MRO58_CAP.EXE`](firmware/X6DR5xxKN149MRO58_CAP.EXE) | [机械革命官方](https://driver.mechrevo.com/d.mechrevo.com/driver/BIOS/GX_AMDDragon/X6DR5xxKN149MRO58_CAP.EXE) |
| `X6DR5xxK` | `N.1.40MRO56` | [`X6DR5xxKN140MRO56_CAP.EXE`](firmware/X6DR5xxKN140MRO56_CAP.EXE) | [机械革命官方](https://driver.mechrevo.com/d.mechrevo.com/driver/MECHREVO2026/BIOS/X6DR5xxKN140MRO56_CAP.EXE) |
| `X6FR55xx` | `N.1.39MRO55` | `X6FR55xxN139MRO55_CAP.EXE` | [机械革命官方](https://driver.mechrevo.com/d.mechrevo.com/driver/MECHREVO2025/TBIOS/X6FR55xxN139MRO55_CAP.EXE) |

## 已知信息

- 2023 款蛟龙 16 Pro（Ryzen 9 7945HX + RTX 4060）有机械革命客服提供的 `MRID6_23_V40.exe` BIOS 更新包。更新后**首次重启可能较慢**，后续重启恢复正常（用户反馈）。
- 感谢 @Blackstone234 在 [Issue #1](https://github.com/YYplus/Mechrevo-BIOS/issues/1#issuecomment-6741848173) 提供新版 BIOS 线索：2025 款蛟龙 16 Pro，Ryzen 9 8945HX + GeForce RTX 5070 Ti 配置通过控制台收到了 `X6DR5xxKN149MRO58_CAP.EXE`（`N.1.49MRO58`）推送。
- 上述 8945HX + RTX 5070 Ti 仅作为已知推送配置记录，不据此推断所有 `X6DR5xxK` 配置均完全相同。
- 公开上市信息确认，2025 款蛟龙 16 Pro 包含 Ryzen 9 9955HX + GeForce RTX 5070 Ti 配置。
- `X6FR55xx` 是 BIOS 平台标识，不应据此推断该固件只对应 RTX 5070 Ti 配置。
- 不同平台的 BIOS 不应仅因同属“蛟龙 16 Pro”系列而视为可互刷。
