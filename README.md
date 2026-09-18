# 机械革命 BIOS / EC 固件归档

[简体中文](README.md) | [English](README_EN.md)

机械革命（MECHREVO）BIOS / EC 固件归档仓库，按机型或 BIOS 平台整理官方固件、下载来源和相关版本信息。

> [!WARNING]
> 刷写 BIOS / EC 存在风险。请确认机型、固件版本及对应平台后再进行更新。

## 已收录机型

| 机型 / 平台 | BIOS | EC |
|---|---|---|
| [耀世 15 Pro](models/耀世15-Pro/) | `N.1.15MRO10` | `1.09` |
| [耀世 16 Ultra（X6AR5xxx）](models/耀世16-Ultra-X6AR5xxx/) | `N.1.33MRO63` | `unknown` |
| [蛟龙 16 Pro（2024–2026）](models/蛟龙16-Pro-2024-2026/) | `N.1.40MRO56` | `unknown` |
| [翼龙 15 Pro（2024）](models/翼龙15-Pro-2024/) | `N.1.10MRO28` | `unknown` |
| [XxRPxxxx 平台（旷世 / 极光系列）](models/XxRPxxxx/) | `N.1.35MRO58` | `unknown` |

## 仓库结构

```text
models/
└─ <机型或平台>/
   ├─ README.md
   ├─ README_EN.md
   ├─ manifest.yaml
   └─ firmware/
      └─ <官方固件文件>
```

每个条目保存机型/平台信息、BIOS/EC 版本、机械革命官方下载地址以及对应的官方固件文件。

## 固件文件

官方 BIOS / EC 固件统一保存在各条目的 `firmware/` 目录中，同时保留原始文件名和官方来源地址。若官方站点触发验证而无法自动抓取，需要手动补入原文件。

新增固件时，请优先保留厂商原始文件名，不对文件内容进行修改。

## 提交新的 BIOS / EC 信息

可以通过仓库 Issues 提交新的固件线索。建议提供：

- 机械革命具体机型；
- BIOS / EC 版本；
- 官方下载地址；
- 原始文件名；
- 适用年份或平台；
- 已知的 EC 配套信息。

## 免责声明

本项目为独立社区项目，与机械革命（MECHREVO）及其关联公司不存在官方关系。

详细内容见 [DISCLAIMER.md](DISCLAIMER.md)。

## License

仓库自行编写的代码与文档采用 MIT License。机械革命及其他厂商的 BIOS、EC、刷写工具、商标和其他第三方材料，其权利归对应权利人所有。
