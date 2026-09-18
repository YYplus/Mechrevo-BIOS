# Metadata fields

Each model uses a `manifest.yaml` file.

## Model-level fields

- `manufacturer`: normally `MECHREVO`.
- `model`: exact public model name.
- `model_aliases`: alternate names, if documented.
- `chassis`: ODM/chassis identifier, or `unknown`.
- `platform`: CPU/platform family, when useful and verified.
- `notes`: concise model-level notes.

## Firmware-level fields

- `type`: `BIOS` or `EC`.
- `version`: exact displayed/published version.
- `release_date`: ISO date (`YYYY-MM-DD`) or `unknown`.
- `original_filename`: exact vendor filename.
- `file_size`: bytes, or `unknown`.
- `sha256`: lowercase SHA-256 hex digest, or `unknown`.
- `source_type`: `official`, `mirror`, `user-provided`, or `unknown`.
- `source_url`: exact source URL when available.
- `status`: one or more of `official`, `verified`, `tested`, `unverified`, `related`.
- `tested_on`: matching hardware record if tested.
- `paired_ec`: required/observed EC version, or `unknown`.
- `paired_bios`: for EC records, corresponding BIOS if known.
- `notes`: evidence-based notes only.
