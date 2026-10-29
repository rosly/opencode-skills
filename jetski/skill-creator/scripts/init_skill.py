#!/usr/bin/env python3
"""
Skill Initializer - Creates a new Jetski skill from a template

Usage:
    init_skill.py <skill-name> --scope <project|global|google3|piper> [--path <base-directory>]
                  [--with-scripts] [--with-references] [--with-assets]

Examples:
    init_skill.py my-new-skill --scope project
    init_skill.py my-api-helper --scope global
    init_skill.py my-team-helper --scope google3
    init_skill.py my-personal-helper --scope piper
    init_skill.py custom-skill --scope project --path /custom/location
"""

import argparse
import getpass
import re
import sys
from pathlib import Path


SKILL_NAME_PATTERN = re.compile(r'^[a-z0-9]+(-[a-z0-9]+)*$')

SKILL_TEMPLATE = """---
name: {skill_name}
description: "[TODO: Complete and informative explanation of what the skill does and when to use it. Include WHEN to use this skill - specific scenarios, file types, or tasks that trigger it.]"
metadata:
  version: "0.1"
---

# {skill_title}

## Overview

[TODO: 1-2 sentences explaining what this skill enables]

## Structuring This Skill

[TODO: Choose the structure that best fits this skill's purpose. Common patterns:

**1. Workflow-Based** (best for sequential processes)
- Works well when there are clear step-by-step procedures
- Example: DOCX skill with "Workflow Decision Tree" → "Reading" → "Creating" → "Editing"
- Structure: ## Overview → ## Workflow Decision Tree → ## Step 1 → ## Step 2...

**2. Task-Based** (best for tool collections)
- Works well when the skill offers different operations/capabilities
- Example: PDF skill with "Quick Start" → "Merge PDFs" → "Split PDFs" → "Extract Text"
- Structure: ## Overview → ## Quick Start → ## Task Category 1 → ## Task Category 2...

**3. Reference/Guidelines** (best for standards or specifications)
- Works well for brand guidelines, coding standards, or requirements
- Example: Brand styling with "Brand Guidelines" → "Colors" → "Typography" → "Features"
- Structure: ## Overview → ## Guidelines → ## Specifications → ## Usage...

**4. Capabilities-Based** (best for integrated systems)
- Works well when the skill provides multiple interrelated features
- Example: Product Management with "Core Capabilities" → numbered capability list
- Structure: ## Overview → ## Core Capabilities → ### 1. Feature → ### 2. Feature...

Patterns can be mixed and matched as needed. Most skills combine patterns (e.g., start with task-based, add workflow for complex operations).

Delete this entire "Structuring This Skill" section when done - it's just guidance.]

## [TODO: Replace with the first main section based on chosen structure]

[TODO: Add content here. See examples in existing skills:
- Code samples for technical skills
- Decision trees for complex workflows
- Concrete examples with realistic user requests
- References to scripts/templates/references as needed]

## Resources

Add bundled resources only when this skill references them directly. Do not create empty or speculative directories; a resource earns its place only when the skill's purpose, resource list, or instructions refer to it. Delete this section if the skill needs no bundled resources.

### scripts/
Executable code (Python/Bash/etc.) that can be run directly to perform specific operations.

**Examples from other skills:**
- PDF skill: `fill_fillable_fields.py`, `extract_form_field_info.py` - utilities for PDF manipulation
- DOCX skill: `document.py`, `utilities.py` - Python modules for document processing

**Appropriate for:** Python scripts, shell scripts, or any executable code that performs automation, data processing, or specific operations.

**Note:** Scripts may be executed without loading into context, but can still be read by Jetski for patching or environment adjustments.

### references/
Documentation and reference material intended to be loaded into context to inform Jetski's process and thinking.

**Examples from other skills:**
- Product management: `communication.md`, `context_building.md` - detailed workflow guides
- BigQuery: API reference documentation and query examples
- Finance: Schema documentation, company policies

**Appropriate for:** In-depth documentation, API references, database schemas, comprehensive guides, or any detailed information that Jetski should reference while working.

### assets/
Files not intended to be loaded into context, but rather used within the output Jetski produces.

**Examples from other skills:**
- Brand styling: PowerPoint template files (.pptx), logo files
- Frontend builder: HTML/React boilerplate project directories
- Typography: Font files (.ttf, .woff2)

**Appropriate for:** Templates, boilerplate code, document templates, images, icons, fonts, or any files meant to be copied or used in the final output.
"""

EXAMPLE_SCRIPT = '''#!/usr/bin/env python3
"""
Example helper script for {skill_name}

This is a placeholder script that can be executed directly.
Replace with actual implementation or delete if not needed.

Example real scripts from other skills:
- pdf/scripts/fill_fillable_fields.py - Fills PDF form fields
- pdf/scripts/convert_pdf_to_images.py - Converts PDF pages to images
"""

def main():
    print("This is an example script for {skill_name}")
    # TODO: Add actual script logic here
    # This could be data processing, file conversion, API calls, etc.

if __name__ == "__main__":
    main()
'''

EXAMPLE_REFERENCE = """# Reference Documentation for {skill_title}

This is a placeholder for detailed reference documentation.
Replace with actual reference content or delete if not needed.

Example real reference docs from other skills:
- product-management/references/communication.md - Comprehensive guide for status updates
- product-management/references/context_building.md - Deep-dive on gathering context
- bigquery/references/ - API references and query examples

## When Reference Docs Are Useful

Reference docs are ideal for:
- Comprehensive API documentation
- Detailed workflow guides
- Complex multi-step processes
- Information too lengthy for main SKILL.md
- Content that's only needed for specific use cases

## Structure Suggestions

### API Reference Example
- Overview
- Authentication
- Endpoints with examples
- Error codes
- Rate limits

### Workflow Guide Example
- Prerequisites
- Step-by-step instructions
- Common patterns
- Troubleshooting
- Best practices
"""

EXAMPLE_ASSET = """# Example Asset File

This placeholder represents where asset files would be stored.
Replace with actual asset files (templates, images, fonts, etc.) or delete if not needed.

Asset files are NOT intended to be loaded into context, but rather used within
the output Jetski produces.

Example asset files from other skills:
- Brand guidelines: logo.png, slides_template.pptx
- Frontend builder: hello-world/ directory with HTML/React boilerplate
- Typography: custom-font.ttf, font-family.woff2
- Data: sample_data.csv, test_dataset.json

## Common Asset Types

- Templates: .pptx, .docx, boilerplate directories
- Images: .png, .jpg, .svg, .gif
- Fonts: .ttf, .otf, .woff, .woff2
- Boilerplate code: Project directories, starter files
- Icons: .ico, .svg
- Data files: .csv, .json, .xml, .yaml

Note: This is a text placeholder. Actual assets can be any file type.
"""


def title_case_skill_name(skill_name):
    """Convert hyphenated skill name to Title Case for display."""
    return ' '.join(word.capitalize() for word in skill_name.split('-'))


def validate_skill_name(skill_name):
    """Return an error message when the skill name is invalid, otherwise None."""
    if not SKILL_NAME_PATTERN.match(skill_name):
        return "must be lowercase kebab-case (letters, digits, single hyphens)"
    if not (1 <= len(skill_name) <= 64):
        return "must be 1-64 characters"
    return None


def init_skill(skill_name, base_path, with_scripts=False, with_references=False, with_assets=False):
    """
    Initialize a new skill directory with a template SKILL.md.

    Args:
        skill_name: Name of the skill
        base_path: Base directory under which the skill directory is created
        with_scripts: Create scripts/ with an example script
        with_references: Create references/ with an example reference
        with_assets: Create assets/ with an example asset

    Returns:
        Path to created skill directory, or None if error
    """
    skill_dir = Path(base_path).resolve() / skill_name

    if skill_dir.exists():
        print(f"❌ Error: Skill directory already exists: {skill_dir}")
        return None

    try:
        skill_dir.mkdir(parents=True, exist_ok=False)
        print(f"✅ Created skill directory: {skill_dir}")
    except Exception as e:
        print(f"❌ Error creating directory: {e}")
        return None

    skill_title = title_case_skill_name(skill_name)
    skill_content = SKILL_TEMPLATE.format(
        skill_name=skill_name,
        skill_title=skill_title
    )

    skill_md_path = skill_dir / 'SKILL.md'
    try:
        skill_md_path.write_text(skill_content)
        print("✅ Created SKILL.md")
    except Exception as e:
        print(f"❌ Error creating SKILL.md: {e}")
        return None

    try:
        if with_scripts:
            scripts_dir = skill_dir / 'scripts'
            scripts_dir.mkdir(exist_ok=True)
            example_script = scripts_dir / 'example.py'
            example_script.write_text(EXAMPLE_SCRIPT.format(skill_name=skill_name))
            example_script.chmod(0o755)
            print("✅ Created scripts/example.py")

        if with_references:
            references_dir = skill_dir / 'references'
            references_dir.mkdir(exist_ok=True)
            example_reference = references_dir / 'api_reference.md'
            example_reference.write_text(EXAMPLE_REFERENCE.format(skill_title=skill_title))
            print("✅ Created references/api_reference.md")

        if with_assets:
            assets_dir = skill_dir / 'assets'
            assets_dir.mkdir(exist_ok=True)
            example_asset = assets_dir / 'example_asset.txt'
            example_asset.write_text(EXAMPLE_ASSET)
            print("✅ Created assets/example_asset.txt")
    except Exception as e:
        print(f"❌ Error creating resource directories: {e}")
        return None

    print(f"\n✅ Skill '{skill_name}' initialized successfully at {skill_dir}")
    print("\nNext steps:")
    print("1. Edit SKILL.md to complete the TODO items and update the description")
    print("2. Add only the resources the skill references directly")
    print("3. Run the validator when ready to check the skill structure")

    return skill_dir


def piper_skills_path(parser):
    """
    Return configs/users/<username>/_agents/skills at the root of the CitC
    workspace (/google/src/cloud/<user>/<workspace>/) that contains the current
    working directory. Exit with a usage error outside a CitC workspace.

    Docs:
    - https://docs.python.org/3/library/pathlib.html#pathlib.Path.cwd
    - https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.parts
    - https://docs.python.org/3/library/getpass.html#getpass.getuser
    """
    parts = Path.cwd().parts
    if parts[1:4] != ('google', 'src', 'cloud') or len(parts) < 6:
        parser.error("--scope piper requires running inside a CitC workspace (/google/src/cloud/<user>/<workspace>/)")
    return Path(*parts[:6]) / 'configs' / 'users' / getpass.getuser() / '_agents' / 'skills'


def main():
    parser = argparse.ArgumentParser(
        description="Initialize a new Jetski skill from a template."
    )
    parser.add_argument(
        "skill_name",
        help="Skill name (lowercase kebab-case, e.g. 'data-analyzer')",
    )
    parser.add_argument(
        "--scope",
        required=True,
        choices=["project", "global", "google3", "piper"],
        help=(
            "Where to create the skill: project (.agents/skills), global (~/.gemini/config/skills), "
            "google3 (_agents/skills), or piper (configs/users/<username>/_agents/skills at the CitC workspace root)"
        ),
    )
    parser.add_argument(
        "--path",
        help="Override the base directory (defaults to the location for --scope)",
    )
    parser.add_argument(
        "--with-scripts",
        action="store_true",
        help="Create scripts/ with an example script",
    )
    parser.add_argument(
        "--with-references",
        action="store_true",
        help="Create references/ with an example reference",
    )
    parser.add_argument(
        "--with-assets",
        action="store_true",
        help="Create assets/ with an example asset",
    )
    args = parser.parse_args()

    name_error = validate_skill_name(args.skill_name)
    if name_error:
        parser.error(f"invalid skill name '{args.skill_name}': {name_error}")

    if args.path:
        base_path = Path(args.path)
    elif args.scope == "project":
        base_path = Path.cwd() / '.agents' / 'skills'
    elif args.scope == "global":
        base_path = Path.home() / '.gemini' / 'config' / 'skills'
    elif args.scope == "google3":
        base_path = Path.cwd() / '_agents' / 'skills'
    else:
        base_path = piper_skills_path(parser)

    print(f"🚀 Initializing skill: {args.skill_name}")
    print(f"   Scope: {args.scope}")
    print(f"   Location: {base_path}")
    print()

    result = init_skill(
        args.skill_name,
        base_path,
        with_scripts=args.with_scripts,
        with_references=args.with_references,
        with_assets=args.with_assets,
    )

    sys.exit(0 if result else 1)


if __name__ == "__main__":
    main()
