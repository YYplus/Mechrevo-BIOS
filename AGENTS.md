# AI Agent Instructions — MECHREVO BIOS / EC Archive

This file is for AI coding agents and automated contributors working in this repository. Follow it together with the existing repository documentation. These instructions do not replace the README, contribution guide, firmware policy, naming rules, or metadata documentation.

## 1. Project purpose and scope

- This is an independent, community-maintained archive of MECHREVO BIOS / EC firmware and related model information. It is not an official MECHREVO repository.
- The repository's primary purpose is to make firmware files, official download sources, and model-to-firmware references easier to find.
- Keep changes focused on the archive. Do not turn the repository into a general laptop-driver collection, troubleshooting forum, or BIOS flashing utility.
- Treat user reports, official customer-service replies, official download URLs, firmware binaries, and cross-model compatibility reports as different kinds of evidence. Preserve who or what supplied a claim when that distinction matters.

## 2. Required reading before making changes

Before changing firmware records or model structure, read the relevant files:

- `README.md` and, when editing user-facing documentation, `README_EN.md`
- `CONTRIBUTING.md`
- `docs/firmware-policy.md`
- `docs/naming.md`
- `docs/metadata.md`
- The target model directory's `README.md`, `README_EN.md`, and `manifest.yaml`
- `models/_template/` when creating a new model entry

Do not assume that an earlier chat, an issue title, a filename, or a model-family name contains all the current repository details. Inspect the current files and directory structure first.

## 3. Pull request workflow

- Make changes on a dedicated feature branch and submit a Pull Request (PR) to `main`. Do not push directly to `main`, force-push, rewrite history, or delete branches unless the repository owner explicitly requests it.
- Keep each PR focused on one coherent task. Avoid bundling unrelated model updates, documentation redesigns, cleanup, or formatting changes.
- Before editing, inspect the current branch and working tree. Do not overwrite changes made by the repository owner or another contributor.
- In a PR, describe what changed, why it changed, which model/platform is affected, and the source of the information or firmware.
- Do not claim a PR, upload, test, or validation succeeded unless the corresponding operation actually completed and its result was checked.
- If the available tools cannot create a branch or PR, do not silently substitute direct commits to `main`. Explain the limitation and provide the proposed patch or ask the repository owner to perform that step.

### PR title and commit message conventions

Use concise, descriptive English prefixes consistently:

| Change | Prefix | Example |
|---|---|---|
| Add or update a firmware binary or firmware record | `firmware:` | `firmware: add Yaoshi 16 Pro BIOS N.1.07MRO15` |
| Add or update model information or directory structure | `models:` | `models: add Wujie 14X model entry` |
| Documentation-only changes | `docs:` | `docs: clarify firmware submission instructions` |
| Fix metadata, links, or repository validation issues | `fix:` | `fix: correct BIOS file path in manifest` |
| Maintenance or tooling changes | `chore:` | `chore: update metadata validation script` |

A PR should normally use one prefix and one concise title. Do not use vague titles such as `update`, `fix files`, or `BIOS update`.

### PR description

Use a short, factual description. Include the following when relevant:

- **Model / series:** the MECHREVO model name and hardware variant, if known.
- **Change:** firmware added, metadata changed, links corrected, or documentation updated.
- **Source:** official MECHREVO URL, customer-service-provided link, user-submitted file, or other specific source.
- **Compatibility:** state only what the available evidence supports; distinguish a confirmed model match from a reported or possible cross-model match.
- **Validation:** list checks actually performed. If none were run, say so.

Do not add empty checklist sections or ask submitters to provide information that is not available.

## 4. Firmware archive rules

- Archive only MECHREVO BIOS / EC firmware within this project's scope.
- Put firmware binaries in the relevant model/platform directory's `firmware/` subdirectory.
- Preserve the vendor's original filename exactly. Do not rename, repack, patch, edit, strip, or otherwise modify BIOS / EC binaries.
- When the original firmware file is supplied and can be added to the repository, include the binary itself rather than recording only a download URL. If the file is unavailable or cannot be committed, record the source URL and clearly leave the archive path unavailable.
- Keep the original vendor download URL in `manifest.yaml` and the model README whenever it is known.
- Do not invent firmware versions, release dates, CPU variants, motherboard IDs, platform IDs, EC pairings, file sizes, or compatibility claims.
- Use `unknown` for unavailable scalar metadata, following the existing schema. Do not fill unknown values by guessing from a filename or from a similar-looking model.
- A user report that a BIOS update succeeded is useful compatibility evidence, but it does not automatically prove universal compatibility across every configuration in the same product family.
- If the same firmware binary is intentionally shared by multiple model entries, avoid storing duplicate copies. Link to the canonical archived file and explain the relationship in the relevant model documentation and metadata. Do not assume two models share firmware merely because their names or chassis look similar.
- Do not add firmware unrelated to MECHREVO or unrelated utilities/drivers to a BIOS/EC archive directory.

## 5. Model directories and metadata

- Prefer a directory named after the public MECHREVO model. A shared platform directory is acceptable when one firmware entry genuinely applies to multiple models and the repository already uses that arrangement.
- Follow the existing directory and filename conventions in `docs/naming.md`.
- Each model/platform entry should keep its model README files and `manifest.yaml` consistent with the actual archived files.
- Follow the field definitions and schema examples in `docs/metadata.md` and `models/_template/manifest.yaml`.
- In `manifest.yaml`:
  - `original_filename` must match the actual vendor filename.
  - `binary_path` must point to the actual file within the repository, or be `unknown` when no binary is archived.
  - `file_size` must match the actual file size in bytes, or be `unknown` when no binary is archived.
  - `source_type` should reflect the actual source, such as `official`, `user-provided`, or `unknown`.
  - `source_url` should be the original source URL, or `unknown`.
  - `status` must not imply testing or verification that did not happen.
  - `tested_on` should identify the reported/tested hardware configuration when known; otherwise use `unknown`.
- Keep the Chinese and English model documentation aligned when both are present. Preserve the repository's existing language and formatting conventions.

## 6. Homepage and navigation

- The root README model index is intentionally concise: organize models by product series and link to the corresponding second-level model directories.
- Do not restore large CPU/motherboard/BIOS tables to the homepage unless the repository owner explicitly asks for them.
- When adding a model or changing a model's directory, update the relevant Chinese and English homepage links and ensure they point to existing paths.
- Keep the six current series groupings consistent unless new reliable model information or an explicit maintainer decision requires a change.
- Do not change unrelated homepage sections when a task only asks for a model-index or submission-guidance edit.

## 7. Evidence, wording, and privacy

- Keep claims factual, concise, and traceable to the source available in the repository or the PR.
- Clearly distinguish official manufacturer information, customer-service-provided information, user-submitted information, and AI inference. Do not present an inference as an official statement.
- If a model name, product series, motherboard identifier, chassis relationship, or BIOS platform is uncertain, preserve the uncertainty and ask for clarification when it materially affects where firmware should be filed.
- Do not invent a product's official marketing name. Use the model name shown by MECHREVO or clearly label a community-reported alias.
- Do not copy personal serial numbers, account details, contact information, or other unnecessary personal data into public files, commits, PR descriptions, or issue references. If a user report contains such data, omit it from the archive.
- Do not add unsupported success stories, testimonials, or promotional language.

## 8. Explicitly avoid these actions

- Do not flash BIOS / EC, trigger a firmware updater, or instruct an automated agent to perform a firmware update on a physical device.
- Do not modify firmware binary contents.
- Do not generate or require SHA-256 checksums, checksum tables, or hash-verification procedures as part of routine archive contributions. The repository owner has intentionally removed that requirement.
- Do not introduce a mandatory information-verification checklist or raise the submission barrier for community members. A basic lead may consist only of a MECHREVO model name plus a firmware link or firmware file; maintainers can organize additional details later.
- Do not delete existing firmware, model records, discussions, workflows, or repository history as incidental cleanup.
- Do not make broad README, directory, metadata-schema, or workflow redesigns unless explicitly requested.

## 9. Checks before submitting a PR

Perform the checks that are applicable to the change:

1. Confirm every changed path is relevant to the task.
2. Confirm firmware filenames are unchanged and every referenced binary path exists.
3. Confirm `manifest.yaml` values match the files and source information actually available.
4. Confirm README links point to existing model directories and firmware files.
5. Confirm Chinese and English pages remain aligned when both are affected.
6. Review the final diff for unrelated edits, accidental binary changes, personal information, and unsupported claims.
7. Report exactly which checks were run and any checks that could not be performed.

When a check cannot be performed, state that limitation instead of implying the repository is fully validated.
