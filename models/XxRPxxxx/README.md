# 机械革命 XxRPxxxx 平台（旷世 / 极光系列）

## 平台信息

| 项目 | 信息 |
|---|---|
| 厂商 | 机械革命（MECHREVO） |
| BIOS 平台标识 | `XxRPxxxx` |
| 官方驱动分类 | `Intel_RPLRefresh` |
| 已观察系统系列名 | `KUANGSHI-JIGUANG Series-X6xx55xW-B2` |
| 具体零售 SKU | `unknown` |

现有记录表明 `N.1.35MRO58` BIOS 出现在机械革命旷世 / 极光系列的 `KUANGSHI-JIGUANG Series-X6xx55xW-B2` 平台上。由于该平台可能对应多个具体 SKU，本页按 BIOS 平台维护，不强行归入单一零售型号。

## BIOS 记录

| 类型 | 版本 | 日期 | 原始文件名 | 官方下载 | 状态 |
|---|---|---|---|---|---|
| BIOS | `N.1.35MRO58` | `unknown` | `XxRPxxxxN135MRO58_CAP.EXE` | [机械革命官方](https://driver.mechrevo.com/d.mechrevo.com/driver/BIOS/Intel_RPLRefresh/XxRPxxxxN135MRO58_CAP.EXE) | `official`, `verified` |

## N.1.35MRO58 已分析信息

官方固件包：

```text
XxRPxxxxN135MRO58_CAP.EXE
```

官方直链：

```text
https://driver.mechrevo.com/d.mechrevo.com/driver/BIOS/Intel_RPLRefresh/XxRPxxxxN135MRO58_CAP.EXE
```

此前对该文件进行过 AMI UCP 结构分析，确认：

- 原始文件大小：`10,729,168 bytes`
- `@UAF` Offset：`0x119600`
- `@CMD` Offset：`0x11EF90`
- `@ROM` Offset：`0x11EFC0`
- 原始 AFU 参数：`/p /b /n /r /x /capsule`
- `@ROM` SHA-256：`514cce8bceb61fb57b8d3fdb15ef55fb41dd55555e3b72e9a3e2dba51dc2e16d`
- BIOS 内包含机械革命新版 800 × 600、60 帧开机动画资源

上面的 SHA-256 是固件包中 `@ROM` 模块的校验值，**不是整个 CAP.EXE 文件的 SHA-256**。

## EC

当前没有可靠的 EC 版本和配套信息，暂不录入。

## 备注

该 BIOS 曾用于 ROM Hole 更新程序的结构分析；当前记录不表示已在所有关联零售机型上实际刷写验证。
