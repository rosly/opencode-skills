---
name: technical-research
description: This skill should be used when researching a technical topic to produce a defensible, traceable knowledge base. It applies to specification or literature surveys, codebase and API investigations, technology comparisons, and requests to "research X and report". It anchors findings to the version under study and the research date. It ranks sources and captures exact quotations with inline links. It isolates research execution in subagents. Each worker maintains paired research and progress Markdown files and returns a concise control summary. File-based checkpoints support recovery after provider interruptions or token limits. The main agent coordinates research under a user-selected steering mode. All research agents must apply @asd-ste100.
metadata:
  version: "1.11"
---

# Technical Research

## Overview

Produce a defensible, traceable knowledge base on a technical subject. Distinguish what sources establish from the conclusions drawn from them.

## When to Use

Use this skill for technical research, specification surveys, literature surveys, codebase investigations, API investigations, technology comparisons, and auditable reports. Do not use it for quick factual queries that need no traceability.

## Execution Ownership

Treat the context window of the main agent as a limited control resource. Source retrieval loads text into the calling agent's context. Repeated retrieval can cause uncontrolled context growth.

Use the main agent only to:

- define scope
- divide the work
- start and continue subagents
- review concise worker summaries
- resolve coordination questions
- request corrections or more research
- report progress to the user

The main agent must not perform discovery or evidence collection. This prohibition applies to every research phase, including the initial scan and verification.

The main agent must not:

- search the web
- retrieve web pages
- browse source pages
- inspect original research sources
- explore a codebase for research evidence
- extract quotations
- check claims against remote or local sources
- load complete evidence files

Delegate every discovery, retrieval, extraction, comparison, and verification operation to a subagent.

Use these terms throughout:

- **Research source:** an original web page, document, dataset, or source-code file.
- **Research artifact:** a worker-authored Markdown file containing findings and supporting evidence.
- **Progress file:** the paired execution-plan and checkpoint file.

Review only bounded sections of saved artifacts when worker summaries lack necessary detail. Request a worker extract or corrected summary when bounded review is insufficient.

Require each subagent to return only the information that the main agent needs for coordination. Do not return raw source text unless the main agent requests a specific passage.

After each worker finishes, verify its actual result against the assigned goal, expected output, and validity criteria. Do not accept a completion claim without this review. If the result falls short, rerun the assignment with more precise expectations and explicit self-verification steps. Provide a stricter output template or an example when needed. Review the new result against the same criteria before accepting it.

Record the confirmed source boundaries in the coordination plan. Include applicable boundaries in every worker prompt and progress file. Apply them throughout research and recovery. Access earlier research or other workers' artifacts only when explicitly permitted. Request clarification before accessing sources outside the confirmed boundaries.

## Controlled Language

Apply `@asd-ste100` to all research instructions and research artifacts. The main agent and every research subagent must apply this skill.

Limit STE linter calls to one per research, when returning the final artifact.

Preserve exact source quotations without changes. Apply `@asd-ste100` only to the text around each quotation.

Use short and direct sentences in worker briefs. Use one instruction per sentence.

## User Steering

Before discovery starts, use the questionnaire tool to ask about research direction, expected results, and presentation. Use the following steering question and three options. Ask about missing result or presentation requirements in the same questionnaire.

Before starting research workers, ask which sources are allowed and which are excluded. Identify local scope by directory and subdirectory tree. Ask about allowed and excluded web sources. Repeat clarification questions until the user confirms the final boundaries.

These boundaries limit worker context use and prevent temporary, conflicting, or earlier research from entering the current work unintentionally.

**Question:** How much influence do you want over research directions and result presentation?

| Option | Required behaviour |
|--------|--------------------|
| Autonomic research | Choose execution and research-path actions within the agreed scope. Consult on agreement changes and material unresolved evidence. |
| Only Critical decisions | Also consult before research-path choices that could materially affect the conclusion. |
| Moderate Control with autonomy on quite obvious decisions | Consult at topic selection, discoveries that materially affect conclusions, and research-path changes. Handle execution choices autonomously. |

Record the answers in the coordination plan. Include the selected mode and applicable consultation triggers in every worker brief.

Always consult before changing scope, goal, expected output, or validity criteria. No steering mode overrides this rule or governing user instructions.

Classify choices as follows:

- **Execution choice:** carries out an agreed assignment without changing its question, coverage, or validity criteria.
- **Research-path choice:** changes what evidence to pursue, which alternative to examine, or what topic to investigate next.
- **Agreement change:** changes scope, goal, expected output, or validity criteria.

Workers report discoveries that affect the agreed scope, conclusions, or next research action. The main agent classifies the required consultation under the selected steering mode. Do not silently choose a path that requires consultation.

Treat evidence as material when it affects research paths, decisions, conclusions, or the user's understanding. Investigate material uncertainty within the agreed scope. Consult the user when resolution requires a consequential decision, agreement change, or clarification.

Do not leave material evidence unresolved as an ordinary open question. If a blocker prevents resolution, report it and request consultation. Do not claim research completion while material issues remain unresolved.

Leave open only minor-impact questions or extensions beyond the existing scope. Explain the impact of each open question. Do not answer an undecided question by assumption.

## Evidence Rules

Apply these principles throughout:

1. **Anchor in time and version.** Record the research date before discovery. Use the version or revision specified in the agreed scope. If the scope specifies no version, assign version identification to the initial-scan worker. Record the resulting anchor in the coordination plan. Do not replace an explicitly requested version with the latest version. Record source versions when they affect applicability. If a version-dependent claim lacks an applicable source version, mark its applicability uncertain.
2. **Rank sources.** Require workers to inspect primary sources before secondary summaries. Prefer specifications, source code at a recorded revision, official documentation, and peer-reviewed work. Treat forums, marketing, and community posts as leads only. Do not base a material conclusion on a weak source alone.
3. **Quote and link.** Require workers to capture the shortest exact quotation that supports each externally sourced fact. Place descriptive supporting links beside every material claim. For a derived conclusion, link the evidence from which it follows. Never invent a quotation or a URL.
4. **Record failed retrieval.** Treat a retrieval failure as a limitation. Do not treat it as proof that a feature does not exist.
5. **Record conflicts.** Require workers to record disagreements and outdated sources. Require them to identify the authoritative source and explain why.
6. **Separate facts from inference.** Organize findings into `Source facts` sections followed by `LLM-inferred conclusions` sections. Repeat this pair for each topic or fact group when needed. Include only statements directly supported by cited evidence in source-fact sections. A quotation proves what its source states, not automatically that the assertion is true. Put interpretations, comparisons, causal explanations, and derived conclusions in inference sections. State their supporting facts, assumptions, and limits separately from source text.
7. **Retrieve actual sources.** Prefer machine-readable pages or raw files. Use a rendering browser only when simple retrieval returns a page shell.

## Research Workflow

Follow the workflow in order. Consult the user before omitting a phase or changing the agreed research method.

1. **Frame intent**
   - Main-agent action: Restate the question. Identify the facts the answer depends on. State assumptions explicitly. Ask when competing interpretations change the answer. Establish steering, expected output, and validity criteria.
   - Required worker output: None.
2. **Plan**
   - Main-agent action: Create the coordination plan. Define initial-scan assignments.
   - Required worker output: None.
3. **Initial scan**
   - Main-agent action: Delegate source-landscape and version-anchor discovery.
   - Required worker output: Authoritative sources, revision history, and proposed topic boundaries.
4. **Decompose**
   - Main-agent action: Use scan results to assign independent topic questions. Run independent assignments concurrently.
   - Required worker output: None.
5. **Capture**
   - Main-agent action: Delegate topic research using the worker-prompt template.
   - Required worker output: Findings and supporting evidence in topic artifacts.
6. **Verification**
   - Main-agent action: Assign decisive claims and cross-topic consistency checks to verification workers.
   - Required worker output: Primary-source checks, conflicts, outdated sources, and version drift.
7. **Synthesize**
   - Main-agent action: Delegate report sections and final assembly using relevant artifacts and source references.
   - Required worker output: A final report following the report template.
8. **Close**
   - Main-agent action: Review worker results against validity criteria. Request corrections or consultation as needed. Report the outcome and artifact paths.
   - Required worker output: Saved artifacts, progress files, and precise completion summaries.

Fill the worker prompt for every assignment. Include the applicable step's output requirements from the numbered workflow. Include the worker-result template and applicable artifact templates in the brief. Do not assume a worker can access the main conversation. Record assignments and available session identifiers in the coordination plan.

Use a fresh worker session for each independent topic. Keep each assignment within one worker's context capacity. Split oversized topics and synthesis inputs into smaller assignments. Do not require one synthesizer to load all evidence at once.

## Files and Recovery

### File Ownership and Layout

Keep one folder per research round and one evidence artifact per topic. Combine topics only during synthesis. Give each worker separate research and progress files, including verification and report workers. Do not permit concurrent edits to one file. A verifier must write its own findings rather than silently changing another worker's evidence.

Keep only requirements, decisions, assignments, status, artifact references, and recovery state in the coordination plan. Keep retrieval logs and detailed working evidence in research artifacts. Put synthesis and supporting citations in the final report. Use section headings to distinguish facts from inference, rather than raw evidence tags.

Insert `-progress` before the research artifact's `.md` extension. Keep the plan at `00` and number artifacts in reading order. Name the report after the subject.

```text
<research-root>/
└── <round>/
    ├── 00-research-plan.md
    ├── 01-scan-<area>.md
    ├── 01-scan-<area>-progress.md
    ├── 10-topic-<name>.md
    ├── 10-topic-<name>-progress.md
    ├── 20-verify-<claim>.md
    ├── 20-verify-<claim>-progress.md
    ├── 90-synthesis-notes.md
    ├── 90-synthesis-notes-progress.md
    ├── <SUBJECT>-REPORT.md
    └── <SUBJECT>-REPORT-progress.md
```

Create synthesis notes or section artifacts only when needed for bounded assembly. Keep the report outline in its progress file or paired synthesis notes. Preserve artifacts after completion for inspection and later extension.

### Completed-Step Checkpoints

Treat provider token limits, session breaks, and interrupted tool calls as recovery conditions. Recovery must depend on saved files, not conversation memory or a surviving provider session.

A step is complete after the worker meets its stated completion criterion and saves its research output. Update execution progress only after that point. Record the result, artifact location, and next step. Report completion only after saving both files.

An output batch is not automatically a completed research step. Treat it as complete only when it meets a completion criterion recorded in the execution plan. Divide oversized work into smaller steps with explicit completion criteria. Checkpoint only completed steps.

### Worker Recovery

1. Continue the existing topic session if it remains usable and can accommodate the next step's inputs and output.
2. Otherwise, start a replacement worker with the paired file paths and the worker-prompt template.
3. Require the worker to read the progress file and relevant artifact sections.
4. Reconcile artifact changes after the last checkpoint.
5. Do not assume an unrecorded operation completed.
6. Resume incomplete work without repeating steps whose completion matches the saved evidence.

Reconcile any artifact changes after the last checkpoint before resuming or appending. Do not mark interrupted work complete merely because partial output exists. A continuation marker identifies partial output, not step completion.

### Main-Agent Recovery

Update `00-research-plan.md` after completed coordination steps. Preserve requirements, steering mode, user decisions, assignments, paired artifact paths, session identifiers, last reported status, consultation requests, and next coordination action.

After interruption, read the coordination plan. Restore control state from worker progress files using bounded reads or worker recovery summaries. Delegate evidence reconciliation to workers.

Reconcile saved state before repeating an assignment. Do not run an old worker and its replacement concurrently against the same files.

## Templates

Use these as starting points.

Plan file:

```markdown
# <Subject> — Research Plan

Date: <YYYY-MM-DD>
Version/revision under study: <agreed anchor or not yet established>
Purpose: <research purpose>
Goal: <agreed goal>
Scope: <in scope / out of scope>
Expected output: <deliverable and presentation requirements>
Validity criteria: <agreed conditions>
Steering mode: <selected mode>
Consultation triggers: <mandatory and mode-specific triggers>
Last coordination checkpoint: <date and time>

## Assignments
| Task | Research artifact | Progress file | Core question | Known sources | Last reported status | Session |
|------|-------------------|---------------|---------------|---------------|----------------------|---------|
| Initial scan | 01-scan-<area>.md | 01-scan-<area>-progress.md | <question> | <urls or unknown> | <status> | <identifier when available> |
| Topic capture | 10-topic-<name>.md | 10-topic-<name>-progress.md | <question> | <urls> | <status> | <identifier when available> |

## User Decisions and Consultation Answers
- <decision, reason, and affected assignment>

## Outstanding Material Issues
- <issue, impact, assigned resolution work, and consultation request>

## Next Coordination Action
<next action and relevant progress-file section>

## Recovery
- Restore requirements and steering from this plan.
- Request recovery summaries from workers using their paired files.
- Delegate evidence reconciliation.
- Reconcile each assignment before repeating or replacing it.

```

Topic evidence file:

```markdown
# <Topic>

Retrieved: <YYYY-MM-DD>. Version under study: <version>.

## Assignment
Question: <bounded question>
Progress file: <paired path>

## <Topic or Fact Group>

### Source facts
- <claim> — "<short exact quotation>" ([descriptive source title](<url>)).

### LLM-inferred conclusions
- <derived conclusion with links to supporting facts and sources>
- Assumptions and limits: <conditions and uncertainty>

## Retrieval log
| URL | Result |
|-----|--------|
| <url> | Retrieved / Failed (<reason>) |

## Material Issues and Resolution
- <issue, impact, supporting evidence, and resolution or blocker>

## Minor Open Questions and Scope Extensions
- <question and explanation of its impact>

## Control summary
<concise summary for the main agent>
```

Worker progress file:

```markdown
# <Topic> — Plan and Execution Progress

## Assignment
Goal: <specific question to answer>
Research artifact: <path>
Progress file: <same basename with -progress>
Parent coordination plan: <path>
Session identifier: <identifier when available>
Last checkpoint: <date and time>

## Required Context
- Research purpose: <why this topic matters>
- Scope: <included and excluded subjects>
- Version/date anchor: <agreed anchor or discovery task>
- Established facts and decisions: <necessary context>
- Prior artifacts: <paths and relevant sections>
- Steering mode: <selected mode>
- User consultation rules: <mandatory triggers>

## Expected Result
- Deliverable: <required findings or report section>
- Presentation: <required structure and level of detail>
- Required evidence: <sources, observations, or comparisons needed to answer the question>
- Validity criteria: <conditions that the result must satisfy>
- Language: Apply @asd-ste100. Preserve exact quotations.

## Execution Plan
| Step | Action | Completion criterion | Status |
|------|--------|----------------------|--------|
| 1 | <bounded action> | <observable result> | not started |
| 2 | <bounded action> | <observable result> | complete |

## Completed Work
| Step | Result | Artifact location |
|------|--------|-------------------|
| <step> | <concrete outcome> | <path and heading> |

## Material Issues
| Issue | Research impact | Resolution work | User consultation |
|-------|-----------------|-----------------|-------------------|
| <issue> | <affected conclusion or path> | <work needed> | <required/requested/answered> |

## Next Step
Action: <next bounded action>
Inputs: <source references or artifact sections>
Completion criterion: <observable result>

## Recovery Instructions
- Read this progress file.
- Inspect the artifact sections listed under completed work.
- Reconcile artifact changes after the last checkpoint.
- Do not assume that an unrecorded operation completed.
- Resume the next incomplete step.

## Latest Control Summary
<concise findings, material issues, and next action>
```

Worker prompt:

```markdown
# Research Assignment: <topic>

Invoke @asd-ste100 before work. Apply it to instructions, notes, analysis, status messages, and results. Preserve exact source quotations.

## Purpose
<overall research goal and why this assignment matters>

## Assigned Goal
<one bounded question>

## Necessary Context
- User requirements: <relevant requirements>
- Established decisions: <decisions that constrain this assignment>
- Version/date anchor: <anchor or instruction to establish it>
- Existing findings: <concise relevant facts>
- Prior work: <artifact paths and relevant headings>

## Scope
Included:
- <subject>

Excluded:
- <subject>

## Source Access
Allowed: <directory trees, web sources, and explicitly permitted research artifacts>
Excluded: <directory trees, web sources, and research artifacts>

## Execution Instructions
- Perform discovery and source inspection within this worker session.
- Inspect primary sources before secondary summaries.
- Prefer specifications, source code at a recorded revision, official documentation, and peer-reviewed work.
- Treat forums, marketing, and community posts as leads only.
- Do not base a material conclusion on a weak source alone.
- Record source versions when they affect applicability.
- Mark a version-dependent claim's applicability uncertain if its applicable source version is missing.
- Capture the shortest exact quotation supporting each externally sourced fact.
- Place descriptive supporting links beside every material claim, including links to evidence for derived conclusions.
- Never invent a quotation or URL.
- Present source facts first, followed by LLM-inferred conclusions in separate sections for each topic or fact group.
- Include only statements directly supported by cited evidence in source-fact sections.
- A quotation proves what its source states, not automatically that its assertion is true.
- Put interpretations, comparisons, causal explanations, and derived conclusions in inference sections.
- State their supporting facts, assumptions, and limits separately from source text.
- Record retrieval failures.
- Treat a retrieval failure as a limitation, not proof that a feature does not exist.
- Record source disagreements and outdated sources.
- Identify the authoritative source and explain why.
- Prefer machine-readable pages or raw files.
- Use a rendering browser only when simple retrieval returns a page shell.
- Investigate material uncertainty until resolved.
- Report material blockers to the main agent.
- Request main-agent consultation before changing scope, goal, expected output, or validity criteria.

## Files
Research artifact: <path>
Progress file: <same basename with -progress>
Coordination plan: <path>

## Execution and Recovery
- Save the assignment and execution plan before discovery.
- Work on one bounded step at a time.
- Divide oversized work into smaller steps with explicit completion criteria.
- Stop oversized reasoning. Save only completed results and continue with smaller steps or request a replacement session.
- Update progress only after meeting a step's completion criterion and saving its research output.
- Record the result, artifact location, and next step in each completed-step update.
- Keep detailed evidence in the research artifact.
- Write large outputs in batches of approximately 100 lines.
- Split longer sections across batches.
- Preserve earlier content when appending.
- End incomplete output with a continuation marker unique within the artifact.
- Replace only the trailing marker when appending the next batch.
- After a timeout, halve the output batch size.
- After interruption, reconcile the artifact with the last completed checkpoint.
- Do not assume an unrecorded operation completed.
- Do not treat partial output or a continuation marker as proof of step completion.
- If context cannot accommodate the next step, save completed work and return a continuation request.

## Expected Result
<required findings, structure, precision, and presentation>
Required evidence: <sources, observations, or comparisons needed to answer the question>

## Validity Criteria
- <specific condition that a satisfactory answer must meet>
- Every material claim has nearby supporting links.
- Findings apply to the agreed version and scope.
- No material evidence uncertainty or conflict remains unresolved.
- Open questions have minor impact or concern extensions beyond scope.
- State each open question's impact. Do not answer it by assumption.
- Research output and progress are saved.
- Final artifacts contain no unfinished placeholders or continuation markers.

## Steering and Escalation
Steering mode: <mode>
Consultation triggers: <applicable triggers>
Treat evidence as material when it affects research paths, decisions, conclusions, or the user's understanding.
Report discoveries that affect the agreed scope, conclusions, or next research action.
Return a blocked status when progress requires a user decision.

## Return Format
Use the worker-result template.
Return concise, concrete findings.
Keep detailed evidence in the artifact.
Return only information needed for the research goal and next coordination decision.
Do not return complete artifacts or raw source text unless a specific passage is requested.
Save reported findings in the research artifact before returning a complete, partial, or blocked response.
```

For a replacement worker, add this instruction:

> Recover from the paired files before new discovery. Reconcile unrecorded artifact changes before resuming incomplete steps.

Worker result:

```markdown
Use complete only after meeting every validity criterion.
Use blocked when resolution requires a user decision or unavailable evidence.
Use partial when work remains, including a continuation request.

Status: complete | partial | blocked
Research artifact: <path>
Progress file: <path>
Last completed step: <step>
Version/date anchor: <anchor>

## <Assigned Question or Fact Group>

### Source facts
- <directly supported answer or finding>
  Evidence location: <artifact heading>
  Source: <supporting link>
  Conditions and limitations: <applicability, limits, and uncertainty>

### LLM-inferred conclusions
- <derived answer with links to supporting facts and sources>
  Assumptions and limits: <conditions and uncertainty>

## Material Issues
- <issue or missing material evidence, affected conclusion, and required resolution, or none>

## Minor Open Questions and Scope Extensions
- <question and its impact, or none>

## User Decision Required
- Decision: <specific question or none>
- Reason: <why this decision affects the research>
- Recommendation: <recommended option and reasoning>

## Remaining Work
- <incomplete step or none>

## Next Action
<one concrete coordination action>
```

Final report:

Present the strongest discriminating evidence first. End the report with one deduplicated resource list.

Repeat the topic or fact-group sections as needed. Omit an inference section when no inference is necessary.

```markdown
# <Subject> — Research Report

Date: <YYYY-MM-DD>. Version: <version>. Scope: <...>.

## <Topic or Fact Group>

### Source facts
<directly supported findings with descriptive inline source links>

### LLM-inferred conclusions
<answer derived from the facts above, with links to supporting facts and sources>
<assumptions, limits, and uncertainty>
<why alternatives fail or remain unverified>

## Minor Open Questions, Scope Extensions, and Limitations
- <item and its impact>

## Resources
- <url>
```
