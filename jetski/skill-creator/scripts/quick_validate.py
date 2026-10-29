#!/usr/bin/env python3
"""
Quick validation script for Jetski skills.

Validates a skill directory (containing SKILL.md) against the Jetski skill
conventions.
"""

import argparse
import re
import sys
from pathlib import Path

import yaml


SKILL_ID_PATTERN = re.compile(r'^[a-z0-9]+(-[a-z0-9]+)*$')


def resolve_skill_file(skill_path):
    """
    Resolve the SKILL.md file and its directory-derived ID.

    Accepts a skill directory or a path to its SKILL.md file.
    Returns (skill_file, skill_id) or (None, None) when the path is not a
    valid skill target.
    """
    path = Path(skill_path).resolve()
    skill_md = path / 'SKILL.md' if path.is_dir() else path
    if skill_md.name != 'SKILL.md' or not skill_md.is_file():
        return None, None
    return skill_md, skill_md.parent.name


def validate_skill(skill_path):
    """
    Validate a skill.

    Returns (errors, warnings) as lists of human-readable messages.
    """
    errors = []
    warnings = []

    path = Path(skill_path)
    if not path.exists():
        return [f"Path not found: {path}"], warnings

    skill_md, skill_id = resolve_skill_file(path)
    if skill_md is None:
        return [f"Not a skill directory or SKILL.md file: {path}"], warnings

    content = skill_md.read_text(encoding='utf-8')
    content = content.replace('\r\n', '\n').replace('\r', '\n')

    if not content.startswith('---'):
        return ["No YAML frontmatter found"], warnings

    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return ["Invalid frontmatter format"], warnings

    # PyYAML docs (safe_load, YAMLError): https://pyyaml.org/wiki/PyYAMLDocumentation
    try:
        frontmatter = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        return [f"Invalid YAML in frontmatter: {exc}"], warnings
    if not isinstance(frontmatter, dict):
        return ["Frontmatter must be a YAML mapping"], warnings

    # Description is required for the skill to be advertised.
    if 'description' not in frontmatter:
        errors.append("Missing 'description' in frontmatter (required for the skill to be advertised)")
    else:
        description = frontmatter['description']
        if not isinstance(description, str) or not description.strip():
            errors.append("'description' must be a non-empty string")

    # Path-derived ID must be portable lowercase kebab-case.
    if not SKILL_ID_PATTERN.match(skill_id):
        errors.append(f"Skill ID '{skill_id}' should be lowercase kebab-case (letters, digits, single hyphens)")
    if not (1 <= len(skill_id) <= 64):
        errors.append(f"Skill ID '{skill_id}' must be 1-64 characters")

    # Name is required and must equal the skill directory name.
    if 'name' not in frontmatter:
        errors.append("Missing 'name' in frontmatter (required)")
    elif not isinstance(frontmatter['name'], str) or not frontmatter['name'].strip():
        errors.append("'name' must be a non-empty string")
    elif frontmatter['name'] != skill_id:
        errors.append(f"'name' ('{frontmatter['name']}') must equal the skill directory name ('{skill_id}')")

    metadata = frontmatter.get('metadata')

    if not isinstance(metadata, dict) or 'version' not in metadata:
        warnings.append("Missing 'metadata.version' (recommended for install/upgrade tracking)")
    elif not re.match(r'^\d+\.\d+$', str(metadata['version'])):
        warnings.append("'metadata.version' should be a MAJOR.MINOR string (e.g. \"1.2\")")

    return errors, warnings


def main():
    parser = argparse.ArgumentParser(description="Validate a Jetski skill.")
    parser.add_argument(
        "skill_path",
        help="Path to the skill directory or its SKILL.md file",
    )
    args = parser.parse_args()

    errors, warnings = validate_skill(args.skill_path)

    for warning in warnings:
        print(f"⚠️  {warning}")
    for error in errors:
        print(f"❌ {error}")

    if errors:
        sys.exit(1)

    print("✅ Skill is valid!")


if __name__ == "__main__":
    main()
