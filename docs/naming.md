# 命名规则

## 机型 / 平台目录

优先使用公开机型名称；同一 BIOS 同时适用于多个机型时，可使用 BIOS 平台标识建立共享目录。

示例：

```text
models/耀世15-Pro/
models/GMxHGxx/
```

## 固件文件

固件文件始终保留机械革命原始文件名，不进行重新命名。

示例：

```text
models/耀世15-Pro/firmware/X6AR45xUN115MRO10_CAP.EXE
models/GMxHGxx/firmware/GMxHGxxN110MRO28_CAP.EXE
```

`manifest.yaml` 中的 `original_filename` 必须与实际归档文件名一致。
