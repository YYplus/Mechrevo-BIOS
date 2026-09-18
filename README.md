# 机械革命 BIOS / EC 固件索引

[简体中文](README.md) | [English](README_EN.md)

这是一个由社区维护的 **机械革命（MECHREVO）BIOS / EC 固件索引与归档项目**，用于整理不同机型的 BIOS、EC 版本信息、官方下载来源、文件校验值、已知兼容关系和相关维护记录。

> [!WARNING]
> **刷写 BIOS / EC 存在导致设备无法启动的风险。**
>
> 在进行任何固件更新前，请务必确认：
>
> - 具体机型与硬件配置；
> - 当前 BIOS / EC 版本；
> - 固件对应的目标机型；
> - BIOS 与 EC 是否存在配套要求；
> - 固件原始来源；
> - 文件 SHA-256 校验值。

## 项目维护内容

本仓库整理：

- 机械革命各机型 BIOS / EC 版本；
- 官方固件下载地址及来源记录；
- 固件原始文件名、文件大小与 SHA-256；
- BIOS 与 EC 的已知配套关系；
- 实际刷写验证记录；
- 官方更新日志与已知问题；
- 不同机械革命机型之间的模具 / ODM 平台关系；
- 与其他品牌同模具机型的关联信息；
- 固件校验和元数据检查工具。

当前阶段以**原厂固件资料整理**为主，不维护修改版 BIOS。

## 已收录机型

| 机型 | BIOS | EC | 记录 |
|---|---|---|---|
| [耀世 15 Pro](models/耀世15-Pro/) | `N.1.15MRO10` | `1.09` | 已录入 |
| [XxRPxxxx 平台（旷世 / 极光系列）](models/XxRPxxxx/) | `N.1.35MRO58` | `unknown` | 已录入 |
| [耀世 16 Ultra（X6AR5xxx）](models/耀世16-Ultra-X6AR5xxx/) | `N.1.33MRO63` | `unknown` | 已录入 |
| [蛟龙 16 Pro（2024–2026）](models/蛟龙16-Pro-2024-2026/) | `N.1.40MRO56` | `unknown` | 已录入 |
| [翼龙 15 Pro（2024）](models/翼龙15-Pro-2024/) | `N.1.10MRO28` | `unknown` | 已录入 |

## 状态说明

每条固件记录可以带有以下状态：

| 状态 | 含义 |
|---|---|
| `official` | 文件或信息来自机械革命官方来源 |
| `verified` | 来源、文件或校验值已经独立核实 |
| `tested` | 已在对应机型上实际刷写并验证 |
| `unverified` | 信息暂未完成独立核实 |
| `related` | 与某机型 / 模具 / ODM 平台存在关联，但尚未证明固件兼容 |

特别注意：

> **`related` ≠ `compatible`**

例如某款机械革命与 XMG、Tongfang 或其他品牌机型使用相同模具，只能说明它们存在平台关联，不能直接得出 BIOS 可以互刷的结论。

## 仓库结构

```text
Mechrevo-BIOS/
├─ README.md
├─ README_EN.md
├─ DISCLAIMER.md
├─ CONTRIBUTING.md
├─ LICENSE
├─ models/
│  ├─ _template/
│  │  ├─ README.md
│  │  └─ manifest.yaml
│  └─ <机型>/
│     ├─ README.md
│     └─ manifest.yaml
├─ docs/
│  ├─ naming.md
│  ├─ metadata.md
│  └─ firmware-policy.md
├─ tools/
│  ├─ checksum/
│  └─ validate/
└─ .github/
   ├─ ISSUE_TEMPLATE/
   └─ workflows/
```

## 机型与固件记录

每个机型单独建立目录，例如：

```text
models/<机型名称>/
├─ README.md
└─ manifest.yaml
```

机型页面主要用于展示：

- 机型名称；
- 硬件平台；
- 模具 / ODM 信息；
- BIOS 版本历史；
- EC 版本历史；
- BIOS / EC 配套关系；
- 官方下载来源；
- 已知问题；
- 相关同模具机型。

`manifest.yaml` 用于保存结构化固件元数据，方便后续自动生成索引和进行一致性检查。

## 固件文件

目前仓库采用 **metadata-first（元数据优先）** 的维护方式。

Git 历史中主要保存：

- 固件版本信息；
- 官方下载链接；
- 原始文件名；
- SHA-256；
- 机型适用信息；
- BIOS / EC 配套关系；
- 验证状态；
- 文档与工具。

BIOS / EC 二进制文件默认**不直接提交到 Git 历史**。

如果未来需要保存已经失效或难以获取的官方固件，并确认适合重新分发，优先考虑使用 GitHub Releases 单独归档，而不是直接提交到仓库。

## SHA-256 校验

Windows PowerShell：

```powershell
.\tools\checksum\sha256.ps1 "C:\path\to\firmware.exe"
```

Linux：

```bash
./tools/checksum/sha256.sh firmware.exe
```

建议任何固件记录都尽可能保留 SHA-256，以便确认不同来源的文件是否完全一致。

## 信息核验原则

本项目采用“证据优先”的维护原则：

- 不根据相似文件名推测兼容性；
- 不根据同模具关系直接推断 BIOS 可以互刷；
- 官方来源和第三方镜像明确区分；
- 保留厂商原始文件名；
- 尽可能记录 SHA-256；
- 无法确认的信息统一标记为 `unknown`；
- 用户实测与官方适配信息分别记录；
- 对存在风险或争议的兼容性结论保留证据来源。

## 如何提交新的 BIOS / EC 信息

可以通过仓库的 **Issues** 提交新的固件记录。

建议至少提供：

- 机械革命具体机型；
- BIOS 或 EC 类型；
- 固件版本；
- 原始文件名；
- 官方下载地址；
- SHA-256；
- 是否实际刷写；
- 刷写前后的 BIOS / EC 版本；
- 其他能够证明来源或适配关系的信息。

如果信息暂时无法确认，也可以提交，但请明确标记哪些内容尚未验证。

## 免责声明

本项目为独立社区项目，与机械革命（MECHREVO）及其关联公司不存在官方关系。

BIOS / EC 更新具有风险，任何刷写操作都应由使用者自行核对设备型号、固件来源和兼容性。

详细内容请参阅 [DISCLAIMER.md](DISCLAIMER.md)。

## License

仓库自行编写的代码与文档默认采用 MIT License。

机械革命及其他厂商的 BIOS、EC、刷写工具、商标和其他第三方材料，其权利仍归对应权利人所有。
