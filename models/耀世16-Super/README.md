# 机械革命 耀世 16 Super

[简体中文](README.md) | [English](README_EN.md)

## 机型信息

| 项目 | 信息 |
|---|---|
| 机型 | 耀世 16 Super（2024） |
| 已知配置 | Intel Core i9-14900HX + GeForce RTX 4080 Laptop GPU（12 GB） |
| 主板型号 | `GM6IX8B` |
| BIOS 平台 / 固件前缀 | `unknown` |
| 已知 BIOS 版本 | `N.1.10MRO09`（用户报告） |
| BIOS 日期 | 2025-01-07（用户报告） |
| EC | `unknown` |

## BIOS

| 版本 | 文件 | 官方来源 |
|---|---|---|
| `N.1.10MRO09` | 尚未取得 | `unknown` |

## 待核实固件线索

| 帖子所述版本 | 固件文件 | 官方来源 | 状态 |
|---|---|---|---|
| `N.1.10MRO10` | [`GMxIX9xN111MRO10_CAP.EXE`](firmware/GMxIX9xN111MRO10_CAP.EXE) | [机械革命官方](https://driver.mechrevo.com/d.mechrevo.com/driver/MECHREVO2026/BIOS/GMxIX9xN111MRO10_CAP.EXE) | 文件已归档，版本与适用平台待核实 |

2026-11-26 收到耀世 16 Super 毁灭者（i9-14900HX + RTX 4080）的固件线索。据用户反馈，客服提供的更新解决了《影之刃》狂暴模式下的蓝屏重启问题。帖子所述版本为 `N.1.10MRO10`，而文件名对应的版本标记为 `N.1.11MRO10`、前缀为 `GMxIX9x`。尚未检查固件内部信息，也未确认反馈设备的实际主板型号。**不能据此认定该固件适用于 `GM6IX8B`，请先向机械革命客服确认，勿直接刷写。** 微码更新情况未知。

## 已知信息

- 感谢 @Icather 在 [Issue #3](https://github.com/YYplus/Mechrevo-BIOS/issues/3) 提供机型、主板型号及 BIOS 版本信息。该机型已记录的装机 BIOS 为 `N.1.10MRO09`，无法确认该版本是否为最终版本。
- [机械革命官方驱动下载](https://www.mechrevo.com/cn/products/yao-shi-16-super/downloads/)：据提交者反馈，页面未提供 BIOS / EC 下载项。建议联系机械革命客服索取对应固件。
- **海外参考机型：** XMG NEO 16 (E24 / `XNE16E24`)，服务手册主板系列 `GM6IXxB`；RTX 4080 / 4090 固件分支已知版本为 `N1.10A13` / EC `1.15.00`：[XMG 官方驱动下载](https://download.schenker-tech.de/package/xmg-neo-16-17-e24-xne16e24-xne17e24/)。仅供平台与驱动参考，不代表海外 BIOS 可互刷。
