# 机械革命 耀世 16 Super

[简体中文](README.md) | [English](README_EN.md)

## 机型信息

| 项目 | 信息 |
|---|---|
| 机型 | 耀世 16 Super（2024） |
| 已知配置 | Intel Core i9-14900HX + GeForce RTX 4080 Laptop GPU（12 GB） |
| 主板型号 | `GM6IX8B` |
| BIOS 平台 / 固件前缀 | `GMxIX9x`（实测 System ROM ID：`GMxIX9xN`） |
| 已知 BIOS 版本 | `N.1.10MRO09`（用户报告） |
| BIOS 日期 | 2025-01-07（用户报告） |
| EC | `unknown` |

## BIOS

| 版本 | 文件 | 官方来源 |
|---|---|---|
| `N.1.10MRO09` | `GMxIX9xN110MRO09_CAP.EXE`（用户报告实刷，尚未归档） | `unknown` |

## 已归档固件（毁灭者用户反馈）

| 文件名对应 BIOS 版本 | 固件文件 | 官方来源 | 状态 |
|---|---|---|---|
| `N.1.11MRO10` | [`GMxIX9xN111MRO10_CAP.exe`](firmware/GMxIX9xN111MRO10_CAP.exe) | [机械革命官方](https://driver.mechrevo.com/d.mechrevo.com/driver/MECHREVO2026/BIOS/GMxIX9xN111MRO10_CAP.EXE) | 已归档，与实测 ROM ID 同家族；新版未实刷验证 |

2026-11-26 收到耀世 16 Super 毁灭者（i9-14900HX + RTX 4080）的固件线索。据用户反馈，客服提供的更新解决了《影之刃》狂暴模式下的蓝屏重启问题。原帖记录的版本为 `N.1.10MRO10`。归档版本 `N.1.11MRO10` 根据官方文件名记录，与原帖的 `N.1.10MRO10` 不一致。目前没有可复核的解包结果确认镜像内版本及 `$FID` 字段；新版在 `GM6IX8B` 上的实际刷写结果尚未确认。微码更新情况未知。

## 用户实测补充（2026-11-26）

感谢 @Icather 在 [Issue #3 的补充反馈](https://github.com/YYplus/Mechrevo-BIOS/issues/3#issuecomment-7189742406) 提供实测数据：

- 本机 DMI System Model 为 `yaoshi16 Super Series GM6IX8B`，AFU `/S` 显示 System ROM ID 为 `GMxIX9xN`。主板标识和固件 ROM ID 不是同一字段，不能因前缀不同而判定不兼容。
- 2026-08-04 曾成功刷写 `GMxIX9xN110MRO09_CAP.EXE`，据报告 AFU 的 FFS、RomLayout 和 Secure Flash 检查均通过。新版文件属于同一 ROM 家族，但尚无该用户实刷新版的结果。
- 用户通过浏览器获取的官方新版 EXE 大小为 10,936,672 字节，与仓库归档文件大小一致（未独立比对全部内容）。官方链接的 Last-Modified 为 2026-11-06 10:00:41 GMT，据用户报告，不等同于 BIOS 内部日期或发布日期。
- 用户报告该 EXE 的 AFU overlay 为 `@UAFP` 结构，明文扫描未找到实际 BIOS 版本或 ROM ID；不能以直接搜索 EXE 字符串替代解包后的镜像检查，也不应仅为查看版本而运行刷写程序。
- 旧版实刷后 Windows 报告的微码为 `0x120`。新版微码未知。

**ROM 家族匹配已有用户实测证据，但不等于新版已实刷验证；更新前仍需确认具体硬件及固件适用性。**

## 已知信息

- 感谢 @Icather 在 [Issue #3](https://github.com/YYplus/Mechrevo-BIOS/issues/3) 提供机型、主板型号及 BIOS 版本信息。该机型已记录的装机 BIOS 为 `N.1.10MRO09`，无法确认该版本是否为最终版本。
- [机械革命官方驱动下载](https://www.mechrevo.com/cn/products/yao-shi-16-super/downloads/)：据提交者反馈，页面未提供 BIOS / EC 下载项。建议联系机械革命客服索取对应固件。
- **海外参考机型：** XMG NEO 16 (E24 / `XNE16E24`)，服务手册主板系列 `GM6IXxB`；RTX 4080 / 4090 固件分支已知版本为 `N1.10A13` / EC `1.15.00`：[XMG 官方驱动下载](https://download.schenker-tech.de/package/xmg-neo-16-17-e24-xne16e24-xne17e24/)。仅供平台与驱动参考，不代表海外 BIOS 可互刷。
