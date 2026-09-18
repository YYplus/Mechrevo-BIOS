#!/usr/bin/env python3
from pathlib import Path
import sys

try:
    import yaml
except ImportError:
    print("PyYAML is required: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

ALLOWED_TYPES = {"BIOS", "EC"}
ALLOWED_STATUS = {"official", "verified", "tested", "unverified"}
ALLOWED_SOURCE_TYPES = {"official", "user-provided", "unknown"}
BINARY_EXTENSIONS = {".exe", ".bin", ".rom", ".cap", ".fd", ".efi"}


def is_unknown(value) -> bool:
    return value in (None, "", "unknown")


def validate_manifest(path: Path) -> tuple[list[str], set[str]]:
    errors: list[str] = []
    referenced_binaries: set[str] = set()

    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"cannot read YAML: {exc}"], referenced_binaries

    if not isinstance(data, dict):
        return ["manifest root must be a mapping"], referenced_binaries

    if data.get("schema_version") != 1:
        errors.append("schema_version must be 1")

    if data.get("manufacturer") != "MECHREVO":
        errors.append("manufacturer must be MECHREVO")

    if not data.get("model"):
        errors.append("model is required")

    firmware = data.get("firmware")
    if not isinstance(firmware, list):
        errors.append("firmware must be a list")
        return errors, referenced_binaries

    manifest_dir = path.parent

    for i, item in enumerate(firmware):
        prefix = f"firmware[{i}]"

        if not isinstance(item, dict):
            errors.append(f"{prefix} must be a mapping")
            continue

        if "sha256" in item:
            errors.append(f"{prefix}.sha256 is deprecated and must be removed")

        if item.get("type") not in ALLOWED_TYPES:
            errors.append(f"{prefix}.type must be BIOS or EC")

        if is_unknown(item.get("version")):
            # The template intentionally uses unknown values.
            if path.parent.name != "_template":
                errors.append(f"{prefix}.version is required")

        status = item.get("status", [])
        if not isinstance(status, list):
            errors.append(f"{prefix}.status must be a list")
        else:
            invalid = set(status) - ALLOWED_STATUS
            if invalid:
                errors.append(
                    f"{prefix}.status contains invalid values: {sorted(invalid)}"
                )

        source_type = item.get("source_type", "unknown")
        if source_type not in ALLOWED_SOURCE_TYPES:
            errors.append(
                f"{prefix}.source_type must be one of "
                f"{sorted(ALLOWED_SOURCE_TYPES)}"
            )

        if "official" in status and source_type != "official":
            errors.append(
                f"{prefix}: status official requires source_type official"
            )

        if source_type == "official" and is_unknown(item.get("source_url")):
            errors.append(
                f"{prefix}: official source requires source_url"
            )

        binary_path = item.get("binary_path")
        file_size = item.get("file_size")
        original_filename = item.get("original_filename")

        if is_unknown(binary_path):
            if not is_unknown(file_size):
                errors.append(
                    f"{prefix}.file_size must be unknown when binary_path is unknown"
                )
            continue

        rel = Path(str(binary_path))
        if rel.is_absolute() or ".." in rel.parts:
            errors.append(f"{prefix}.binary_path must be a safe relative path")
            continue

        if not rel.parts or rel.parts[0] != "firmware":
            errors.append(
                f"{prefix}.binary_path must be inside the firmware/ directory"
            )

        if is_unknown(original_filename):
            errors.append(
                f"{prefix}.original_filename is required for an archived binary"
            )
        elif rel.name != str(original_filename):
            errors.append(
                f"{prefix}.original_filename does not match binary_path filename"
            )

        binary = manifest_dir / rel
        binary_repo_path = binary.as_posix()
        referenced_binaries.add(binary_repo_path)

        if not binary.is_file():
            errors.append(
                f"{prefix}.binary_path does not exist: {binary_repo_path}"
            )
            continue

        if not isinstance(file_size, int) or isinstance(file_size, bool) or file_size < 0:
            errors.append(
                f"{prefix}.file_size must be the actual size in bytes"
            )
        elif binary.stat().st_size != file_size:
            errors.append(
                f"{prefix}.file_size mismatch: manifest={file_size}, "
                f"actual={binary.stat().st_size}"
            )

    return errors, referenced_binaries


def validate_repository() -> list[str]:
    errors: list[str] = []
    models_root = Path("models")
    manifest_paths = sorted(models_root.glob("*/manifest.yaml"))
    all_referenced: set[str] = set()

    if not manifest_paths:
        return ["no model manifests found"]

    for manifest in manifest_paths:
        model_dir = manifest.parent

        for required in ("README.md", "README_EN.md", "manifest.yaml"):
            if not (model_dir / required).is_file():
                errors.append(
                    f"{model_dir.as_posix()}: missing required file {required}"
                )

        manifest_errors, referenced = validate_manifest(manifest)
        all_referenced.update(referenced)

        if manifest_errors:
            errors.append(f"[{manifest.as_posix()}]")
            errors.extend(f"  {error}" for error in manifest_errors)

    archived_binaries: set[str] = set()

    for file in models_root.rglob("*"):
        if not file.is_file() or file.suffix.lower() not in BINARY_EXTENSIONS:
            continue

        repo_path = file.as_posix()
        archived_binaries.add(repo_path)

        if "firmware" not in file.parts:
            errors.append(
                f"{repo_path}: firmware binary must be inside a firmware/ directory"
            )

    for repo_path in sorted(archived_binaries - all_referenced):
        errors.append(
            f"{repo_path}: archived firmware is not referenced by any manifest"
        )

    for repo_path in sorted(all_referenced - archived_binaries):
        errors.append(
            f"{repo_path}: manifest references a missing firmware binary"
        )

    return errors


def main() -> int:
    errors = validate_repository()

    if errors:
        print("[FAIL] repository validation")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("[OK] repository structure and firmware metadata are consistent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
