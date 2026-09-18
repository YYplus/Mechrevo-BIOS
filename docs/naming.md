# Naming convention

## Model directories

Use the public model name where possible.

Recommended format:

```text
models/<model-name>/
```

If a model name contains characters unsuitable for paths, normalize only what is necessary and record the exact marketing/model name inside the model README.

## Firmware records

Preserve the vendor's original firmware filename exactly in `original_filename`.

For local archival naming, use:

```text
<model>_<type>_<version>_<date-if-known>.<ext>
```

Examples:

```text
MODEL_BIOS_N.1.15MRO10_2026-08-01.exe
MODEL_EC_1.09_unknown.bin
```

Do not silently rename the original file without preserving its original name in metadata.
