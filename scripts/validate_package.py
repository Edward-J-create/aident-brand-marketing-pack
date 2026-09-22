#!/usr/bin/env python3
"""Dependency-free repository checks for the public Skill package."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "aident-brand-marketing-pack"
SKILL = PACKAGE / "SKILL.md"
METADATA = ROOT / "loadout" / "metadata.json"
ALLOWED_EXTENSIONS = {".md", ".txt", ".json", ".yaml", ".yml"}
MAX_FILES = 50
MAX_PACKAGE_BYTES = 256 * 1024
MAX_SKILL_BYTES = 32 * 1024
ACTION_PATTERN = re.compile(r"<action-tag>([^<]+)</action-tag>")
LOCAL_LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
HTML_PATTERN = re.compile(r"<(?!/?action-tag\b)[A-Za-z][^>]*>")
BANNED_MEDIA_ACTION_FRAGMENTS = ("fal_", "text_to_image", "text_to_video", "image_generation", "video_generation")
PRIVATE_LARK_DOC_LINK_PATTERN = re.compile(
    r"https?://[^\s)]+\.(?:larksuite\.com|feishu\.cn)/(?:docx|wiki)/[A-Za-z0-9]+",
    flags=re.IGNORECASE,
)
REQUIRED_DEFAULT_MARKERS = (
    "`full-library`",
    "source-led",
    "idea-led",
    "one real editable cloud document",
    "reference-pack-blueprint.md",
    "document-delivery.md",
    "original-media-delivery.md",
    "full-quality result file",
    "Layered design and editing projects are excluded from the default pack",
)
REQUIRED_PACK_SECTIONS = (
    "English Copy",
    "Official Links and Social Channels",
    "Brand Assets",
    "Launch Video",
    "Video Clips Assets",
    "The Creative Rule",
    "Platform Template References",
    "Workflow Ideas",
    "Accuracy Guardrails",
    "中文 copy",
    "中文素材",
)


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def validate_yaml_when_available(path: Path, errors: list[str]) -> None:
    try:
        import yaml  # type: ignore
    except ImportError:
        return
    try:
        yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(errors, f"Invalid YAML in {path.relative_to(ROOT)}: {exc}")


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
    if "name: aident-brand-marketing-pack" not in frontmatter:
        fail(errors, "SKILL.md name must be aident-brand-marketing-pack")
    if "description:" not in frontmatter:
        fail(errors, "SKILL.md frontmatter must include description")

    for marker in REQUIRED_DEFAULT_MARKERS:
        if marker not in skill_text:
            fail(errors, f"Missing default pack contract marker: {marker}")
    blueprint = PACKAGE / "references" / "reference-pack-blueprint.md"
    if not blueprint.is_file():
        fail(errors, "Missing reference-pack blueprint")
    else:
        blueprint_text = blueprint.read_text(encoding="utf-8")
        for section in REQUIRED_PACK_SECTIONS:
            if section not in blueprint_text:
                fail(errors, f"Reference-pack blueprint omits {section}")
    brief_text = (PACKAGE / "assets" / "brief.yaml").read_text(encoding="utf-8")
    if "profile: full-library" not in brief_text or "destination: auto-cloud-document" not in brief_text:
        fail(errors, "Default brief must request the full library and an online document")
    if "media_delivery: final-files-first" not in brief_text:
        fail(errors, "Default brief must request full-quality final media files")
    if "editable_source_handoff_requested: false" not in brief_text:
        fail(errors, "Default brief must exclude editable source projects unless requested")
    media_reference = PACKAGE / "references" / "original-media-delivery.md"
    if not media_reference.is_file():
        fail(errors, "Missing final-result media delivery reference")
    else:
        media_text = media_reference.read_text(encoding="utf-8")
        if "finished result file" not in media_text or "5 MB" not in media_text:
            fail(errors, "Media delivery must define final results and dynamic file-size handling")
    for path in (PACKAGE / "assets" / "brief.yaml", ROOT / "examples" / "copy-pack.yaml"):
        if "destination: local-markdown" in path.read_text(encoding="utf-8"):
            fail(errors, f"Default or example may not route to local Markdown: {path.relative_to(ROOT)}")

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
        if path.suffix.lower() == ".md" and HTML_PATTERN.search(text):
            fail(errors, f"Unsupported HTML-like tag in {relative}")

        if path.suffix.lower() in {".yaml", ".yml"}:
            validate_yaml_when_available(path, errors)

        if path.suffix.lower() == ".md":
            for target in LOCAL_LINK_PATTERN.findall(text):
                clean_target = target.split("#", 1)[0].strip()
                if not clean_target or "://" in clean_target or clean_target.startswith("mailto:"):
                    continue
                resolved = (path.parent / clean_target).resolve()
                if not resolved.exists():
                    fail(errors, f"Broken local link in {relative}: {target}")

    for path in (ROOT / "README.md", *files):
        if path.suffix.lower() not in ALLOWED_EXTENSIONS:
            continue
        if PRIVATE_LARK_DOC_LINK_PATTERN.search(path.read_text(encoding="utf-8")):
            fail(errors, f"Public package contains a direct Lark document URL: {path.relative_to(ROOT)}")

    tags = sorted(set(ACTION_PATTERN.findall(skill_text)))
    references = sorted(ref.get("name") for ref in metadata.get("references", []))
    if tags != references:
        fail(errors, "SKILL.md action tags do not exactly match metadata references")
    for tag in tags:
        if any(fragment in tag.lower() for fragment in BANNED_MEDIA_ACTION_FRAGMENTS):
            fail(errors, f"Media-generation action is outside this Skill's boundary: {tag}")

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
