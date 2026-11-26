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

## 已归档固件（毁灭者用户反馈）

| 包内 BIOS 版本 | 固件文件 | 官方来源 | 状态 |
|---|---|---|---|
| `N.1.11MRO10` | [`GMxIX9xN111MRO10_CAP.exe`](firmware/GMxIX9xN111MRO10_CAP.exe) | [机械革命官方](https://driver.mechrevo.com/d.mechrevo.com/driver/MECHREVO2026/BIOS/GMxIX9xN111MRO10_CAP.EXE) | 已归档，`$FID` 与本机 ROM ID 同族；微码未知 |

2026-11-26 收到耀世 16 Super 毁灭者（i9-14900HX + RTX 4080）的固件线索。据用户反馈，客服提供的更新解决了《影之刃》狂暴模式下的蓝屏重启问题。原帖记录的版本为 `N.1.10MRO10`。归档的 BIOS 镜像内记录的版本为 `N.1.11MRO10`，`$FID` 项目标识为 `GMxIX9xN1`。

**关于 `GMxIX9x` 前缀与本机的关系：** `GM6IX8B` 是 DMI 中的主板备案名，AFU `/S` 打印的 `System ROM ID` 则为 `GMxIX9xN`。2026-08-04 同一台 GM6IX8B 机器曾实刷 `GMxIX9xN110MRO09_CAP.EXE` 并成功（FFS Pass / RomLayout Pass / Secure Flash 验证通过），因此 `GMxIX9x` 属于该机型的 ROM 家族，前缀差异不构成不兼容的理由。

**包内不含明文版本信息：** 对归档的 CAP.EXE 做了全文件 ASCII 与 UTF-16LE 扫描，`N.1.11MRO10`、`GMxIX9xN1`、`MRO10` 均无命中，`$FID` 只在 `.rdata` 段出现一次（AFU 自身常量）。版本信息来自解包后的镜像。包结构为 AMI AFU 5.15.03（PE32+ x64）+ `@UAF` 归档，overlay 自 `0x110000` 起，无数字签名。

**下载件校验：** `sha256 eeccef4a80cf47784d443f34fe80def73b7e950173e074d4d434eaf0cabb4edb`，10,936,672 B，厂商侧 `Last-Modified` 为 2026-11-06。

**仍不能认定为可直接执行的升级：** 微码更新情况未知，且本机型上一版 `N.1.10MRO09` 实刷后微码仍停留在 `0x120`。请先向机械革命客服确认适用范围，勿直接刷写。

## 已知信息

- 感谢 @Icather 在 [Issue #3](https://github.com/YYplus/Mechrevo-BIOS/issues/3) 提供机型、主板型号及 BIOS 版本信息。该机型已记录的装机 BIOS 为 `N.1.10MRO09`，无法确认该版本是否为最终版本。
- [机械革命官方驱动下载](https://www.mechrevo.com/cn/products/yao-shi-16-super/downloads/)：据提交者反馈，页面未提供 BIOS / EC 下载项。建议联系机械革命客服索取对应固件。
- **海外参考机型：** XMG NEO 16 (E24 / `XNE16E24`)，服务手册主板系列 `GM6IXxB`；RTX 4080 / 4090 固件分支已知版本为 `N1.10A13` / EC `1.15.00`：[XMG 官方驱动下载](https://download.schenker-tech.de/package/xmg-neo-16-17-e24-xne16e24-xne17e24/)。仅供平台与驱动参考，不代表海外 BIOS 可互刷。
