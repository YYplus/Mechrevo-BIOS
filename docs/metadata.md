# 元数据字段

每个机型或平台目录使用一个 `manifest.yaml`。

## 机型级字段

- `manufacturer`：厂商，当前统一为 `MECHREVO`。
- `model`：机型或平台名称。
- `model_aliases`：已知别名。
- `applicable_years`：适用年份（如适用）。
- `platform`：BIOS 平台标识。
- `chassis`：模具 / chassis 标识，未知时填写 `unknown`。
- `variants`：同一公开机型存在多个硬件版本时使用，例如耀世 15 Pro 的 255H / 155H。

## 固件级字段

- `type`：`BIOS` 或 `EC`。
- `variant`：对应硬件版本（如适用）。
- `platform`：该固件对应的平台标识（如需要）。
- `version`：固件版本。
- `release_date`：发布日期，未知时填写 `unknown`。
- `original_filename`：机械革命原始文件名。
- `binary_path`：仓库内固件路径；未归档文件时填写 `unknown`。
- `file_size`：实际文件大小（bytes）；未归档文件时填写 `unknown`。
- `source_type`：例如 `official`、`user-provided` 或 `unknown`。
- `source_url`：原始来源地址，未知时填写 `unknown`。
- `status`：记录状态，例如 `official`、`verified`、`tested`、`unverified`。
- `tested_on`：实际刷写验证机型，未知时填写 `unknown`。
- `paired_ec`：已知配套 EC。
- `paired_bios`：EC 条目对应的 BIOS。
- `notes`：其他已确认信息。
