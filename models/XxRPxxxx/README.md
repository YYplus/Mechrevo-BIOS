# 机械革命 XxRPxxxx 平台（旷世 / 极光系列）

[简体中文](README.md) | [English](README_EN.md)

## 平台信息

| 项目 | 信息 |
|---|---|
| 系列 | 旷世 / 极光 |
| BIOS 平台 | `XxRPxxxx` |
| 官方驱动分类 | `Intel_RPLRefresh` |
| 系列标识 | `KUANGSHI-JIGUANG Series-X6xx55xW-B2` |
| EC | `unknown` |

## BIOS

| 版本 | 文件 | 官方来源 |
|---|---|---|
| `N.1.35MRO58` | [`XxRPxxxxN135MRO58_CAP.EXE`](firmware/XxRPxxxxN135MRO58_CAP.EXE) | [机械革命官方](https://driver.mechrevo.com/d.mechrevo.com/driver/BIOS/Intel_RPLRefresh/XxRPxxxxN135MRO58_CAP.EXE) |

## 已知信息

此前对该文件进行过 AMI UCP 结构分析：

- 文件大小：`10,729,168 bytes`
- `@UAF` Offset：`0x119600`
- `@CMD` Offset：`0x11EF90`
- `@ROM` Offset：`0x11EFC0`
- 原始 AFU 参数：`/p /b /n /r /x /capsule`
- BIOS 内包含 800 × 600、60 帧机械革命开机动画资源。
