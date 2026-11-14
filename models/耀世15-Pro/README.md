# 机械革命 耀世 15 Pro

[简体中文](README.md) | [English](README_EN.md)

## 机型信息

耀世 15 Pro 当前记录两个硬件版本：

| 硬件版本 | BIOS 平台 | BIOS | EC |
|---|---|---|---|
| 255H | `X6AR45xU` | `N.1.15MRO10` | `1.09` |
| 155H | `XxMT4xxx` | `N.1.07MRO12` | `unknown` |

## BIOS

| 硬件版本 | 版本 | 文件 | 官方来源 |
|---|---|---|---|
| 255H | `N.1.15MRO10` | [`X6AR45xUN115MRO10_CAP.EXE`](firmware/X6AR45xUN115MRO10_CAP.EXE) | [机械革命官方](https://driver.mechrevo.com/d.mechrevo.com/driver/BIOS/Intel_ArrowH45/X6AR45xUN115MRO10_CAP.EXE) |
| 155H | `N.1.07MRO12` | [`XxMT4xxxN107MRO12_CAP.EXE`](firmware/XxMT4xxxN107MRO12_CAP.EXE) | `unknown` |

## 已知信息

- 255H 的 `N.1.15MRO10` 固件内部 `$FID`：`X6AR45xUNd`。
- 255H 的 `N.1.15MRO10` + EC `1.09` 有实际使用记录。
- 155H 对应 BIOS 平台 `XxMT4xxx`，当前记录 BIOS `N.1.07MRO12`。

## 已知问题（255H / `X6AR45xU`）

- **机械革命控制中心：** 较新版本的控制中心在该机型上无法正常使用；目前已确认最后一个可用版本为 `5.56.60.22`（基于 255H 机型实际使用反馈）。
- **Measured Boot / TPM PCR0：** 当前 BIOS `N.1.15MRO10`（EC `1.09`）下，Measured Boot 测量日志重建的 `PCR[0]` 与 TPM 实际读取的 `PCR[0]` 仍然不一致，待机械革命官方修复。
