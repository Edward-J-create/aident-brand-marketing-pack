#!/usr/bin/env python3
"""Dependency-free repository checks for the public Skill package."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "build-brand-marketing-pack"
SKILL = PACKAGE / "SKILL.md"
METADATA = ROOT / "loadout" / "metadata.json"
ALLOWED_EXTENSIONS = {".md", ".txt", ".json", ".yaml", ".yml"}
MAX_FILES = 50
MAX_PACKAGE_BYTES = 256 * 1024
MAX_SKILL_BYTES = 32 * 1024
ACTION_PATTERN = re.compile(r"<action-tag>([^<]+)</action-tag>")
LOCAL_LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def main() -> int:
    errors: list[str] = []

    if not SKILL.is_file():
        fail(errors, f"Missing {SKILL.relative_to(ROOT)}")
        return report(errors)

    skill_text = SKILL.read_text(encoding="utf-8")
    metadata = json.loads(METADATA.read_text(encoding="utf-8"))
    files = sorted(path for path in PACKAGE.rglob("*") if path.is_file())
    frontmatter = skill_text.split("---", 2)[1] if skill_text.startswith("---\n") else ""

    if not skill_text.startswith("---\n"):
        fail(errors, "SKILL.md must start with YAML frontmatter")
    if "name: build-brand-marketing-pack" not in frontmatter:
        fail(errors, "SKILL.md name must be build-brand-marketing-pack")
    if "description:" not in frontmatter:
        fail(errors, "SKILL.md frontmatter must include description")

    h2s = re.findall(r"^## .+$", skill_text, flags=re.MULTILINE)
    if not h2s or h2s[0] != "## **Aident Loadout Platform**":
        fail(errors, "The first H2 must be the exact Aident Loadout Platform heading")

    if len(files) > MAX_FILES:
        fail(errors, f"Package has {len(files)} files; maximum is {MAX_FILES}")
    package_bytes = sum(path.stat().st_size for path in files)
    if package_bytes > MAX_PACKAGE_BYTES:
        fail(errors, f"Package is {package_bytes} bytes; maximum is {MAX_PACKAGE_BYTES}")
    if SKILL.stat().st_size > MAX_SKILL_BYTES:
        fail(errors, f"SKILL.md is {SKILL.stat().st_size} bytes; maximum is {MAX_SKILL_BYTES}")

    for path in files:
        relative = path.relative_to(PACKAGE)
        if path.suffix.lower() not in ALLOWED_EXTENSIONS:
            fail(errors, f"Unsupported package file extension: {relative}")
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            fail(errors, f"Package file is not UTF-8 text: {relative}")
            continue
        if re.search(r"\b(?:TODO|TBD|FIXME)\b", text, flags=re.IGNORECASE):
            fail(errors, f"Unresolved placeholder in {relative}")

        if path.suffix.lower() == ".md":
            for target in LOCAL_LINK_PATTERN.findall(text):
                clean_target = target.split("#", 1)[0].strip()
                if not clean_target or "://" in clean_target or clean_target.startswith("mailto:"):
                    continue
                resolved = (path.parent / clean_target).resolve()
                if not resolved.exists():
                    fail(errors, f"Broken local link in {relative}: {target}")

    tags = sorted(set(ACTION_PATTERN.findall(skill_text)))
    references = sorted(ref.get("name") for ref in metadata.get("references", []))
    if tags != references:
        fail(errors, "SKILL.md action tags do not exactly match metadata references")

    return report(errors, len(files), package_bytes, len(tags))


def report(
    errors: list[str], file_count: int = 0, package_bytes: int = 0, action_count: int = 0
) -> int:
    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        "Validation passed: "
        f"{file_count} package files, {package_bytes} bytes, {action_count} capability tags."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
