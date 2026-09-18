#!/usr/bin/env python3
from pathlib import Path
import sys

try:
    import yaml
except ImportError:
    print("PyYAML is required: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

ALLOWED_TYPES = {"BIOS", "EC"}
ALLOWED_STATUS = {"official", "verified", "tested", "unverified", "related"}


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    data = yaml.safe_load(path.read_text(encoding="utf-8"))

    if not isinstance(data, dict):
        return ["manifest root must be a mapping"]

    if data.get("schema_version") != 1:
        errors.append("schema_version must be 1")

    if not data.get("model"):
        errors.append("model is required")

    firmware = data.get("firmware")
    if not isinstance(firmware, list):
        errors.append("firmware must be a list")
        return errors

    for i, item in enumerate(firmware):
        prefix = f"firmware[{i}]"

        if not isinstance(item, dict):
            errors.append(f"{prefix} must be a mapping")
            continue

        if item.get("type") not in ALLOWED_TYPES:
            errors.append(f"{prefix}.type must be BIOS or EC")

        status = item.get("status", [])
        if not isinstance(status, list):
            errors.append(f"{prefix}.status must be a list")
        else:
            invalid = set(status) - ALLOWED_STATUS
            if invalid:
                errors.append(f"{prefix}.status contains invalid values: {sorted(invalid)}")

        sha256 = item.get("sha256")
        if sha256 not in (None, "unknown"):
            if (
                not isinstance(sha256, str)
                or len(sha256) != 64
                or any(c not in "0123456789abcdef" for c in sha256)
            ):
                errors.append(
                    f"{prefix}.sha256 must be lowercase 64-character hex or unknown"
                )

    return errors


def main() -> int:
    files = [Path(p) for p in sys.argv[1:]] or list(
        Path("models").rglob("manifest.yaml")
    )
    failed = False

    for path in files:
        errors = validate(path)
        if errors:
            failed = True
            print(f"[FAIL] {path}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"[OK]   {path}")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
