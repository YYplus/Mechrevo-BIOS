# Metadata fields

Each model/platform directory contains a `manifest.yaml`.

## Model-level fields

- `manufacturer`: vendor name.
- `model`: model or platform name.
- `model_aliases`: alternate names.
- `applicable_years`: model years when applicable.
- `platform`: BIOS platform identifier.
- `chassis`: chassis identifier when known.

## Firmware-level fields

- `type`: `BIOS` or `EC`.
- `version`: firmware version.
- `release_date`: release date or `unknown`.
- `original_filename`: original vendor filename.
- `binary_path`: path of the archived firmware file in this repository.
- `file_size`: file size in bytes when known.
- `sha256`: recorded file digest when available.
- `source_type`: source type such as `official`.
- `source_url`: original source URL.
- `status`: record status.
- `tested_on`: hardware used for an actual flashing test, or `unknown`.
- `paired_ec`: known EC pairing.
- `paired_bios`: known BIOS pairing for an EC record.
- `notes`: additional notes.
