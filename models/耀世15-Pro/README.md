# 机械革命 耀世 15 Pro

[简体中文](README.md) | [English](README_EN.md)

## 机型信息

耀世 15 Pro 当前记录三个硬件版本：

| 硬件版本 | BIOS 平台 / 主板型号 | BIOS | EC |
|---|---|---|---|
| 255H | `X6AR45xU` | `N.1.15MRO10` | `1.09` |
| 155H | `XxMT4xxx` | `N.1.07MRO12` | `unknown` |
| i7-14650HX | `GM5IX0A`（主板） | `N.1.07MRO15`（实测） | `unknown` |

## BIOS

| 硬件版本 | 版本 | 文件 | 官方来源 |
|---|---|---|---|
| 255H | `N.1.15MRO10` | [`X6AR45xUN115MRO10_CAP.EXE`](firmware/X6AR45xUN115MRO10_CAP.EXE) | [机械革命官方](https://driver.mechrevo.com/d.mechrevo.com/driver/BIOS/Intel_ArrowH45/X6AR45xUN115MRO10_CAP.EXE) |
| 155H | `N.1.07MRO12` | [`XxMT4xxxN107MRO12_CAP.EXE`](firmware/XxMT4xxxN107MRO12_CAP.EXE) | `unknown` |
| i7-14650HX（`GM5IX0A`） | `N.1.07MRO15` | [`GMxIX7xN107MRO15_CAP.EXE`](../耀世16-Pro/firmware/GMxIX7xN107MRO15_CAP.EXE)（与耀世 16 Pro 共用） | [机械革命官方](https://driver.mechrevo.com/d.mechrevo.com/driver/MECHREVO2026/BIOS/GMxIX7xN107MRO15_CAP.EXE) |

## 实测与反馈

- 255H：`$FID` = `X6AR45xUNd`。
- i7-14650HX（`GM5IX0A`）：使用耀世 16 Pro 固件从 `N.1.07MRO13` 升级至 `N.1.07MRO15` 成功（用户反馈）。

## 海外参考

- **海外同平台机型（i7-14650HX / `GM5IX0A`）：** XMG FUSION 15 (E24 / `XFU15E24`)，对应主板系列 `GM5IXxA`：[XMG 官方驱动下载](https://download.schenker-tech.de/package/xmg-fusion-e24-xfu15e24/)。
- **海外相近平台参考（255H / `X6AR45xU`）：** XMG FUSION 15 (L25 / `XFU15L25`)，服务手册平台为 `X5AR45xS`，与本机编号不同：[XMG 官方驱动下载](https://download.schenker-tech.de/package/xmg-fusion-15-l25-xfu15l25/)。

## 已知问题（255H / `X6AR45xU`）

- **机械革命控制中心：** 较新版本的控制中心在该机型上无法正常使用；目前已确认最后一个可用版本为 `5.56.60.22`（基于 255H 机型实际使用反馈）。
- **Measured Boot / TPM PCR0：** 当前 BIOS `N.1.15MRO10`（EC `1.09`）下，Measured Boot 测量日志重建的 `PCR[0]` 与 TPM 实际读取的 `PCR[0]` 仍然不一致，待机械革命官方修复。
