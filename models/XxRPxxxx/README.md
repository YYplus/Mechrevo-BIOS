# 机械革命 XxRPxxxx 平台（旷世 / 极光系列）

[简体中文](README.md) | [English](README_EN.md)

## 平台信息

| 项目 | 信息 |
|---|---|
| 系列 | 旷世 / 极光 |
| BIOS 平台 | `XxRPxxxx` |
| 官方驱动分类 | `Intel_RPLRefresh` |
| 系列标识 | `KUANGSHI-JIGUANG Series-X6xx55xW-B2` |
| 已知客服提供记录 | 极光 X Pro |
| EC | `unknown` |

## BIOS

| 版本 | 文件 | 来源 |
|---|---|---|
| `N.1.35MRO58` | [`XxRPxxxxN135MRO58_CAP.EXE`](firmware/XxRPxxxxN135MRO58_CAP.EXE) | [机械革命官方 EXE](https://driver.mechrevo.com/d.mechrevo.com/driver/BIOS/Intel_RPLRefresh/XxRPxxxxN135MRO58_CAP.EXE) / [机械革命官方 ZIP](https://driver.mechrevo.com/d.mechrevo.com/driver/MECHREVO2026/BIOS/XxRPxxxxN135MRO58_CAP.zip) |

## 已知信息

- 机械革命官网存在正式的“极光 X Pro”产品及技术支持页面。
- 有用户反馈其 **极光 X Pro** 向机械革命客服咨询 BIOS 后，客服提供了 `XxRPxxxxN135MRO58_CAP.zip`。该信息来自用户评论转述，用作机型关联线索，不等同于机械革命公开发布的 BIOS 兼容列表。
- 固件内部系列标识为 `KUANGSHI-JIGUANG Series-X6xx55xW-B2`，因此本仓库继续以 `XxRPxxxx` 平台为主进行归档，不据此推断所有旷世 / 极光机型均可使用该 BIOS。

此前对该文件进行过 AMI UCP 结构分析：

- 文件大小：`10,729,168 bytes`
- `@UAF` Offset：`0x119600`
- `@CMD` Offset：`0x11EF90`
- `@ROM` Offset：`0x11EFC0`
- 原始 AFU 参数：`/p /b /n /r /x /capsule`
- BIOS 内包含 800 × 600、60 帧机械革命开机动画资源。
