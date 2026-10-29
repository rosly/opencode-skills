---
name: skill-creator
description: Guide for creating effective skills. Use when users want to create a new skill (or update an existing skill) that extends OpenCode's capabilities with specialized knowledge, workflows, or tool integrations.
metadata:
  version: "1.2"
license: Complete terms in LICENSE.txt
---

# Skill Creator

This skill provides guidance for creating effective skills.

## About Skills

Skills are modular, self-contained packages that extend OpenCode's capabilities by providing
specialized knowledge, workflows, and tools. Think of them as "onboarding guides" for specific
domains or tasks—they transform OpenCode from a general-purpose agent into a specialized agent
equipped with procedural knowledge that no model can fully possess.

### What Skills Provide

1. Specialized workflows - Multi-step procedures for specific domains
2. Tool integrations - Instructions for working with specific file formats or APIs
3. Domain expertise - Company-specific knowledge, schemas, business logic
4. Bundled resources - Scripts, references, and assets for complex and repetitive tasks

### Anatomy of a Skill

Every skill consists of a required SKILL.md file and optional bundled resources:

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter metadata (optional)
│   │   ├── name: (display label)
│   │   └── description: (required for discovery)
│   └── Markdown instructions (required)
└── Bundled Resources (optional)
    ├── scripts/          - Executable code (Python/Bash/etc.)
    ├── references/       - Documentation intended to be loaded into context as needed
    └── assets/           - Files used in output (templates, icons, fonts, etc.)
```

### Where Skills Live

OpenCode discovers skills from location-based sources. Choose the scope when creating a skill:

- **Project:** `.opencode/skills/<skill-id>/SKILL.md` — available only in the current project.
- **Global:** `~/.config/opencode/skills/<skill-id>/SKILL.md` — available to every project for the current user.

Each source accepts either form:

- A directory containing `SKILL.md`, such as `.opencode/skills/git-release/SKILL.md`.
- A root-level Markdown file, such as `.opencode/skills/review.md`.

The skill ID is derived from the path: the directory name for the `SKILL.md` form, or the file name without `.md` for the flat form. IDs are case-sensitive; use lowercase kebab-case. Paths written inside a skill are relative to the directory containing `SKILL.md`.

OpenCode also discovers compatibility sources such as `.claude/skills` and `.agents/skills`, but prefer the `.opencode/skills` locations for new skills.

A skill can be developed in place in a discovery location, in any other workspace or repository, or obtained from an external source such as a git repository. Developing directly in a discovery location is valid; OpenCode loads the skill as soon as it is valid. Skills developed elsewhere must be installed into a discovery location (see Step 5).

#### SKILL.md (required)

**Metadata Quality:** Only the `description` in YAML frontmatter drives discovery: OpenCode advertises a skill to the model when it has a description. The `name` is a display label and defaults to the path-derived ID. Write the `description` with this formula:

```
<capability statement>. Use when <triggers>. Don't use for <out-of-scope tasks> (use <other-skill>).
```

- The capability statement and the `Use when` clause are mandatory.
- The `Don't use for` clause is recommended only when another skill or task is likely to be confused with this one.
- Name concrete triggers: user requests, file types, tools, or tasks.

OpenCode-specific frontmatter fields:

- `metadata.opencode/autoinvoke: false` — hide the skill from the model's available list while keeping it loadable by ID.
- `disable-model-invocation: true` — same effect as `opencode/autoinvoke: false`; `opencode/autoinvoke` wins when both are set.

`metadata.version` is a quoted `MAJOR.MINOR` string (e.g. `"1.2"`) used by install and upgrade tooling to decide whether a skill can be safely overwritten. OpenCode ignores it. See "Install or Upgrade the Skill" below.

All frontmatter is optional at runtime; a skill without a description is not advertised.

#### Bundled Resources (optional)

##### Scripts (`scripts/`)

Executable code (Python/Bash/etc.) for tasks that require deterministic reliability or are repeatedly rewritten.

- **When to include**: When the same code is being rewritten repeatedly or deterministic reliability is needed
- **Example**: `scripts/rotate_pdf.py` for PDF rotation tasks
- **Benefits**: Token efficient, deterministic, may be executed without loading into context
- **Note**: Scripts may still need to be read by OpenCode for patching or environment-specific adjustments

##### References (`references/`)

Documentation and reference material intended to be loaded as needed into context to inform OpenCode's process and thinking.

- **When to include**: For documentation that OpenCode should reference while working
- **Examples**: `references/finance.md` for financial schemas, `references/mnda.md` for company NDA template, `references/policies.md` for company policies, `references/api_docs.md` for API specifications
- **Use cases**: Database schemas, API documentation, domain knowledge, company policies, detailed workflow guides
- **Benefits**: Keeps SKILL.md lean, loaded only when OpenCode determines it's needed
- **Best practice**: If files are large (>10k words), include grep search patterns in SKILL.md
- **Avoid duplication**: Information should live in either SKILL.md or references files, not both. Prefer references files for detailed information unless it's truly core to the skill—this keeps SKILL.md lean while making information discoverable without hogging the context window. Keep only essential procedural instructions and workflow guidance in SKILL.md; move detailed reference material, schemas, and examples to references files.

##### Assets (`assets/`)

Files not intended to be loaded into context, but rather used within the output OpenCode produces.

- **When to include**: When the skill needs files that will be used in the final output
- **Examples**: `assets/logo.png` for brand assets, `assets/slides.pptx` for PowerPoint templates, `assets/frontend-template/` for HTML/React boilerplate, `assets/font.ttf` for typography
- **Use cases**: Templates, images, icons, boilerplate code, fonts, sample documents that get copied or modified
- **Benefits**: Separates output resources from documentation, enables OpenCode to use files without loading them into context

### Progressive Disclosure Design Principle

Skills use a three-level loading system to manage context efficiently:

1. **Metadata (ID + name + description)** - Always in context (~100 words)
2. **SKILL.md body** - When skill triggers (<5k words)
3. **Bundled resources** - As needed by OpenCode (Unlimited*)

*Unlimited because scripts can be executed without reading into context window.

## Skill Creation Process

To create a skill, follow the "Skill Creation Process" in order, skipping steps only if there is a clear reason why they are not applicable.

Copy this checklist and track progress:

- [ ] Step 0: Check existing state
- [ ] Step 1: Understand the skill with concrete examples
- [ ] Step 2: Plan the reusable skill contents
- [ ] Step 3: Initialize the skill
- [ ] Step 4: Edit the skill
- [ ] Step 5: Install or upgrade the skill (optional)
- [ ] Step 6: Iterate
- [ ] Check every item in "Definition of done"

### Step 0: Check Existing State

Check whether a skill with the same ID exists in the target directory or in an OpenCode skill location, in either form:

```bash
ls -d <base-directory>/<skill-id> .opencode/skills/<skill-id> .opencode/skills/<skill-id>.md ~/.config/opencode/skills/<skill-id> ~/.config/opencode/skills/<skill-id>.md 2>/dev/null
```

- If no skill with that ID exists → create mode: continue with Step 1 and create the skill in Step 3.
- If the skill exists in the target directory → update mode:
  1. Read its SKILL.md (or `<skill-id>.md`) and bundled resources.
  2. Compare the new intent with the existing skill's scope: purpose, triggers, workflow, and resources.
  3. Ask the user about each conflict with the `question` tool, as a series of questions. Offer options to amend, remove, or update the conflicting part, and mark one option as recommended with its reason.
  4. Apply only the decisions the user approved, and skip Step 3.
- If a skill with the same ID exists in the other location → establish which skill wins under OpenCode's skill override hierarchy, and clarify the intent with the user through the `question` tool in the same way.

### Step 1: Understanding the Skill with Concrete Examples

Skip this step only when the skill's usage patterns are already clearly understood. It remains valuable even when working with an existing skill.

To create an effective skill, clearly understand concrete examples of how the skill will be used. This understanding can come from either direct user examples or generated examples that are validated with user feedback.

For example, when building an image-editor skill, relevant questions include:

- "What functionality should the image-editor skill support? Editing, rotating, anything else?"
- "Can you give some examples of how this skill would be used?"
- "I can imagine users asking for things like 'Remove the red-eye from this image' or 'Rotate this image'. Are there other ways you imagine this skill being used?"
- "What would a user say that should trigger this skill?"

To avoid overwhelming users, avoid asking too many questions in a single message. Start with the most important questions and follow up as needed for better effectiveness.

Conclude this step when there is a clear sense of the functionality the skill should support.

### Step 2: Planning the Reusable Skill Contents

To turn concrete examples into an effective skill, analyze each example by:

1. Considering how to execute on the example from scratch
2. Identifying what scripts, references, and assets would be helpful when executing these workflows repeatedly

Example: When building a `pdf-editor` skill to handle queries like "Help me rotate this PDF," the analysis shows:

1. Rotating a PDF requires re-writing the same code each time
2. A `scripts/rotate_pdf.py` script would be helpful to store in the skill

Example: When designing a `frontend-webapp-builder` skill for queries like "Build me a todo app" or "Build me a dashboard to track my steps," the analysis shows:

1. Writing a frontend webapp requires the same boilerplate HTML/React each time
2. An `assets/hello-world/` template containing the boilerplate HTML/React project files would be helpful to store in the skill

Example: When building a `big-query` skill to handle queries like "How many users have logged in today?" the analysis shows:

1. Querying BigQuery requires re-discovering the table schemas and relationships each time
2. A `references/schema.md` file documenting the table schemas would be helpful to store in the skill

To establish the skill's contents, analyze each concrete example to create a list of the reusable resources to include: scripts, references, and assets.

### Step 3: Initializing the Skill

At this point, it is time to actually create the skill.

Skip this step only if the skill being developed already exists, and iteration is needed. In this case, continue to the next step.

When creating a new skill from scratch, run the `init_skill.py` script. It generates a new skill directory with a SKILL.md template and creates only the resources the skill actually needs.

Usage:

```bash
scripts/init_skill.py <skill-name> --scope <project|global> [--path <base-directory>] [--with-scripts] [--with-references] [--with-assets]
```

The `--scope` argument is mandatory and selects the discovery location:

- `--scope project` creates the skill under `.opencode/skills/` in the current working directory.
- `--scope global` creates the skill under `~/.config/opencode/skills/`.

The `--scope` and `--path` arguments select where the skill is developed: `--scope` creates it in a discovery location for in-place development, while `--path` creates it in any other location, such as a separate workspace or repository.

By default the script creates only `SKILL.md`. Add resource directories only when the skill references them directly:

- `--with-scripts` creates `scripts/` with an example script.
- `--with-references` creates `references/` with an example reference.
- `--with-assets` creates `assets/` with an example asset.

After initialization, complete the SKILL.md TODO items and add only the resources the skill actually uses.

### Step 4: Edit the Skill

When editing the (newly-generated or existing) skill, remember that the skill is being created for another instance of OpenCode to use. Focus on including information that would be beneficial and non-obvious to OpenCode. Consider what procedural knowledge, domain-specific details, or reusable assets would help another OpenCode instance execute these tasks more effectively.

When editing an existing skill, increment `metadata.version` (see the Installation paragraph in Step 5).

#### Start with Reusable Skill Contents

Create only the reusable resources the skill references directly: `scripts/`, `references/`, and `assets/` files. Do not create empty or speculative directories; a resource earns its place only when the skill's purpose, resource list, or SKILL.md instructions refer to it. This step may require user input. For example, when implementing a `brand-guidelines` skill, the user may need to provide brand assets or templates to store in `assets/`, or documentation to store in `references/`.

#### Update SKILL.md

**Writing Style:** Write the entire skill using **imperative/infinitive form** (verb-first instructions), not second person. Use objective, instructional language (e.g., "To accomplish X, do Y" rather than "You should do X" or "If you need to do X"). This maintains consistency and clarity for AI consumption.

**Sentence rules:**

- Write one action per sentence or bullet.
- Write decisions as condition → action: "If X → do Y".
- Put exact commands in code blocks; do not describe a command in prose.
- Add a reason ("because …") only when the rule is not obvious.
- Use numbers instead of adjectives: "under 500 lines", not "short".
- Do not use "appropriate", "as needed", or "consider" without a criterion that decides the case.
- State each rule once. Refer to it from other places instead of repeating it.

To complete SKILL.md, answer the following questions:

1. What is the purpose of the skill, in a few sentences?
2. When should the skill be used?
3. In practice, how should OpenCode use the skill? All reusable skill contents developed above should be referenced so that OpenCode knows how to use them.

#### Add Checklists

Every skill ends with a `## Definition of done` checklist. Each item must be:

- **Verifiable:** checked by a command, a file check, or an observable output, not by opinion.
- **Atomic:** one condition per item.
- **Not a copy of the body:** refer to the rule instead of restating it.
- **Not automatable:** if a script can check the condition, the script checks it and the checklist has one item for running that script.

If the skill has 3 or more ordered steps → start its workflow with a progress checklist that lists the steps, introduced by "Copy this checklist and track progress:".

#### Add Step 0 for Skills That Write Files

If the skill creates or modifies files → start its workflow with "Step 0: Check existing state":

- If the output does not exist → create mode: run all steps.
- If the output exists → update mode: read the existing files first, change only the affected parts, and do not regenerate unchanged files.

#### Add Subagent Prompt Templates and Structured Responses

If the skill delegates work to subagents → apply these rules:

1. Store each subagent prompt as a Markdown template in `assets/<role>-prompt-template.md`.
2. Mark every variable part of a template with a placeholder `<<FIELD_NAME>>` in uppercase snake case. Do not use any other placeholder syntax.
3. In SKILL.md, give each template a fill table `| Placeholder | Value source |` that lists every placeholder of that template.
4. Instruct the agent to pass the template to the subagent verbatim: replace only the placeholders; do not paraphrase, shorten, reorder, or add text.
5. Instruct the agent to verify that the filled prompt contains no `<<` before it launches the subagent.
6. End each template with a `## Response format` section that:
   - requires exactly one JSON object and no text before or after it;
   - shows the object with every field;
   - states each field's type and allowed values;
   - includes `status` (`ok`, `partial`, or `failed`) and `errors` (list of strings).
7. Instruct the agent to parse the JSON response and check the required fields. If this fails → resend the prompt once with the parse error appended. If it fails again → report the failure to the user.

### Step 5: Install or Upgrade the Skill (optional)

Skip this step when the skill was developed in place in a discovery location; OpenCode already loads it. Install only when the skill was developed elsewhere or obtained from an external source.

OpenCode loads skills from its discovery locations, so installing a skill means placing the skill directory there:

- Project: `.opencode/skills/<skill-id>/`
- Global: `~/.config/opencode/skills/<skill-id>/`

Keep development separate from the installation directory. Before copying a skill over an existing installation, compare the `metadata.version` in the source SKILL.md with the installed copy:

- Source version newer → deliberate upgrade; safe to overwrite.
- Source version equal or older → do not overwrite silently; investigate whether the installed copy is newer or has local changes.

Increment `metadata.version` (a quoted `MAJOR.MINOR` string) for every change to an existing skill, including fixes. Without an increment, an upgrade is indistinguishable from a file conflict. OpenCode itself does not compare versions; this check is performed by the install procedure or tooling.

### Step 6: Iterate

After testing the skill, users may request improvements. Often this happens right after using the skill, with fresh context of how the skill performed.

**Iteration workflow:**
1. Use the skill on real tasks
2. Notice struggles or inefficiencies
3. Identify how SKILL.md or bundled resources should be updated
4. Increment `metadata.version` in SKILL.md
5. Implement changes and test again

Increment `metadata.version` on every edit to an existing skill, not only when an iteration is complete. The skill may be installed at any time, so each edit must be recognizable as a deliberate upgrade rather than a file conflict (see the Installation paragraph in Step 5).

## Definition of done

- [ ] `scripts/quick_validate.py <skill-path>` passes.
- [ ] `grep -n '[[]TODO:' <skill-file>` prints nothing.
- [ ] The `description` follows the formula in "Metadata Quality".
- [ ] The skill file ends with a `## Definition of done` checklist that follows "Add Checklists".
- [ ] If the workflow has 3 or more ordered steps → it starts with a progress checklist.
- [ ] If the skill creates or modifies files → its workflow starts with "Step 0: Check existing state".
- [ ] If the skill uses subagents → every `<<FIELD_NAME>>` in each `assets/*-prompt-template.md` appears in that template's fill table in SKILL.md.
- [ ] If the skill uses subagents → each prompt template ends with `## Response format` that defines a JSON object with `status` and `errors`.
- [ ] Every file in `scripts/`, `references/`, and `assets/` is referenced from SKILL.md, and no empty directory exists.
- [ ] If the skill existed before → `metadata.version` is higher than the previous version.
- [ ] If the skill was installed (Step 5) → `diff -r <source-path> <installed-path>` prints nothing.
