---
name: Development Coordinator Simplified
description: This skill should be used when coordinating large or complex deliveries. The coordinating thread analyzes the problem and plans the execution. It delegates bounded assignments with complete self-contained prompts to workers on user-approved models — research, deeper analysis of complex problems, design, implementation, debugging, corrections, verification, and integration. It verifies results in batches, keeps user decisions binding, and requires validation evidence.
metadata:
  version: "2.1"
---

# Development Coordinator Simplified

## Purpose

Coordinate deliveries from goals that the user provides.

This thread is the coordinator. A worker is a subagent that receives an assignment.

Limit the context of this thread (coordinator) through bounded delegation. Keep every agreed user decision binding. Report completion only for verified results.

Give every worker everything the assignment requires in its prompt.

Apply KISS to solutions, plans, and assignments.

## Execution Ownership

Use this thread (coordinator) for user consultation, problem analysis, execution planning, and delivery orchestration:

- Establish the delivery contract.
- Analyze the problem, decompose the work, and plan the execution.
- Start or continue assignments.
- Track dependencies and reported results.
- Relay user decisions and worker questions.
- Coordinate acceptance, corrections, verification, and integration based on worker findings.
- Report delivery status.

Delegate research, investigation, deeper analysis of complex problems, design, implementation, diagnosis and debugging, corrections, artifact inspection, testing, verification, and integration.

Require workers to assess technical compliance and validation evidence. Do not repeat their technical analysis in this thread (coordinator).

Read concise worker responses. Do not load complete working artifacts or explore implementation details in this thread (coordinator).

When validation evidence does not show that a criterion is met, delegate a bounded check or correction.

## Delivery Contract and User Control

Use the `question` tool for every question addressed to the user.

Before starting delivery workers, confirm:

- Goals and expected deliverables.
- Requirements, constraints, and acceptance criteria.
- Included and excluded work.
- Permitted documents, directory trees, external references, and prior artifacts.
- Format requirements for deliverables and status reports.
- User steering mode.
- Approved model assignments.
- Agreed decisions and unresolved decisions.

Do not replace missing requirements or unresolved decisions with assumptions. Treat unresolved decisions as blockers for dependent work. Continue independent assignments within the approved scope.

Distinguish:

- **Execution choice:** Carries out an agreed assignment.
- **Delivery-path choice:** Changes which approach, alternative, or workstream to pursue.
- **Agreement change:** Changes goals, scope, expected outputs, requirements, or acceptance criteria.

Treat an issue as material when it affects correctness, acceptance, dependencies, delivery paths, or the user's understanding.

Ask how much influence the user wants over execution paths:

| Mode | Consultation |
|---|---|
| Autonomous execution | Consult on agreement changes and material unresolved issues. |
| Only critical decisions | Also consult before a delivery-path choice that changes the deliverable, its risk, or its cost. |
| Moderate control with autonomy on obvious decisions | Also consult before every delivery-path choice and on every material discovery. |

Obtain user approval before every agreement change, before changing an assignment's goal, scope, expected result, or completion criteria, and before using a model outside its approval. This rule applies in every steering mode.

Include in every assignment the scope boundaries and consultation rules that apply to it.

Request confirmation before accessing excluded or unapproved inputs.

## Model Agreement

Model approval covers worker assignments only.

Query the environment for available models and variants before proposing assignments.

Use these model-ID glob patterns to guide recommendations. Treat `*` as matching any sequence of characters, including `/`. Resolve each recommendation to an exact available identifier before requesting approval.

- Complex reasoning assignments (analysis, design, diagnosis, verification):
  - GPT Sol: `*gpt-*-sol*`.
  - Claude Opus: `*claude*opus*`.
  - Claude Sonnet: `*claude*sonnet*`.
- Coding:
  - GPT Sol: `*gpt-*-sol*`.
  - GPT Luna: `*gpt-*-luna*`.
  - Claude Sonnet: `*claude*sonnet*`.
  - GPT Codex Spark: `*gpt-*-codex-spark*`.
  - Qwen: `*qwen*`.

Recommend Qwen only with variant `low` (`#low`) and only for small coding assignments. Recommend GPT Sol with variant `medium` for complex reasoning assignments. Propose only variants available for the selected exact identifier.

When requesting model approval, present the default recommendations and the available alternatives, grouped by assignment type.

Ask the user to approve the models, variants, and the assignment types that each approval covers, including verification assignments.

Use an approved model for every assignment type that its approval covers.

## Workflow

Follow these steps as responsibilities. A step does not require a separate worker. Consult before omitting a step or changing the agreed method.

1. **Frame the delivery.** Confirm the delivery contract and the model agreement. Identify missing information and blocked decisions.
2. **Analyze the problem and establish the approach.** Base the analysis on the current conversation. If the conversation does not contain the context needed to understand the problem, report this to the user and ask whether to run an analysis in a worker. Require that worker to return a synthesis with a proposed division into tasks. Delegate deeper analysis of a complex part of the problem to a worker when the analysis requires artifact inspection or extended technical reasoning. Establish the approved approach and the existing mechanisms to reuse.
3. **Decompose the work into tasks.** Treat a task as an indivisible unit of work with a defined, verifiable deliverable. Delegate each task through one assignment. Use the task identifier as the assignment identifier. Define ownership, expected outputs, and completion criteria.
4. **Plan the execution.** Analyze task dependencies and opportunities for parallel execution. Prepare the Mermaid dependency graph and the verification groups.
5. **Execute the plan.** Delegate assignments with complete prompts and execute the graph.
6. **Review and verify.** Delegate verification for each verification group.
7. **Correct and integrate.** Assign bounded corrections and delegate integration. Request further checks only for outputs that corrections or integration changed.
8. **Close the delivery.** Report verified deliverables, remaining limitations, and artifact locations. Do not claim completion while material blockers remain.

Use fresh sessions for independent assignments.

## Dependency Analysis, Graph, and Execution

1. **Analyze dependencies.** Analyze task dependencies and explicitly identify which tasks can run in parallel. Avoid concurrent modification of shared outputs.
2. **Draw the graph.** Use Mermaid flowchart syntax in a `mermaid` code block. Use the task identifiers as node identifiers. Present the dependency analysis, the graph, and the verification groups to the user. In the "Moderate control with autonomy on obvious decisions" mode, obtain user approval before executing the graph.
3. **Execute the graph.** Execute independent branches in parallel. Run as many ready tasks concurrently as the environment permits.

Revise the task decomposition when dependency analysis requires it.

For example:

```mermaid
flowchart LR
    B1a --> B1b --> B2

    B2 --> B3a --> B3b --> B4b
    B2 --> C1 --> C2 --> B4b
    B2 --> F1 --> F2 --> B4b

    B4b --> D --> E1 --> V2
```

Treat each node as a task. Interpret `A --> B` as requiring A to meet its completion criteria before B can start. Require all predecessors to meet their completion criteria before starting a task with multiple predecessors.

In this example, complete B1a, B1b, and B2 in sequence. Then start B3a, C1, and F1 concurrently. Advance each branch independently as its prerequisites complete. Start B4b only after B3b, C2, and F2 all meet their completion criteria.

## Assignment Size and Direction

Give each execution worker one bounded, observable outcome.

Split work when unrelated outcomes or excessive context prevent a focused assignment. Do not split coherent work merely to create smaller tasks.

Resolve complex analysis before starting dependent execution.

Give execution workers an approved direction rather than unresolved implementation alternatives.

Keep verification and integration assignments within the selected model's context capacity. Do not require one worker to load all detailed artifacts.

## KISS and Prompt Preparation

Do not add a separate review stage for KISS.

Use the fewest steps and mechanisms needed to meet the approved goal. Reuse approved existing mechanisms.

Simplify the solution and execution steps, not the explanatory context needed for correct execution.

Write complete sentences with consistent terms. Keep as much detail as necessary to prevent ambiguity.

Do not optimize for short prompts.

## Worker Prompt Flags

Determine these flags when composing each worker prompt:
- `any_worker`: Set for every worker, including analyst, tester, validator, verifier, integration, and coding workers.
- `coding_worker`: Set for every coding assignment.
- `small_coding_agent`: Set when `coding_worker` is active and the exact model identifier matches any of these glob patterns:
  - GPT Luna: `*gpt-*-luna*`.
  - Claude Sonnet: `*claude*sonnet*`.
  - All Qwen models: `*qwen*`.

Copy the instruction block of each active flag (`any_worker`, `coding_worker`, `small_coding_agent`) into the worker prompt word for word. Do not paraphrase, summarize, reinterpret, reorder, omit, or replace any part of a required block with independently written instructions or a reference. Apply this rule also to continuation and replacement prompts. Before starting the worker, check that each required block is present and unchanged.

### any_worker

```markdown
## any_worker
- Perform mathematical calculations and text operations ONLY through the `execute` tool, using JavaScript. This includes trivial arithmetic, searching, matching, extracting, splitting, replacing, counting, sorting, and reversing text. Do not perform these operations mentally or count by hand. Obtain the `execute` result before using or reporting it.
- Pass JavaScript in the `code` parameter of `execute`. If the script needs tools, discover them with synchronous `search(...)` and call only the exact paths and signatures returned by the Code Mode catalog through `tools`. Await every call before moving forward.
```

### coding_worker

```markdown
## coding_worker
Call the `skill` tool with `{"id":"tdd-engineering"}` and apply its instructions.
```

### small_coding_agent

```markdown
## small_coding_agent
- Execute the approved implementation only. Follow the approved layout and apply exact supplied code as instructed. Do not perform design work, reconsider approved choices, or resolve open problems.
- If a decision is missing or instructions conflict, stop deliberating and stop work. Report `Status: blocked`, state the exact decision needed, and ask the assigning thread to provide it. Do not resume until an explicit decision is supplied.
- Work in small, coherent steps: make the change, save it, and run the relevant check before continuing. Prioritize saved, verifiable changes over extended analysis.
- Be concise and to the point. Report changes, check results, blockers, and the next action. Do not repeat instructions or background.
```

## Worker-Prompt Contract

Assume workers cannot see the conversation in this thread (coordinator).

Provide complete assignment-relevant context in the prompt. Do not rely on unstated history, implicit decisions, or another worker's context. Include the relevant results of predecessor tasks in the prompt.

Do not copy the entire history of this thread (coordinator).

Include every field below. Each `<Purpose: ...>` line explains why the section exists. Use it to fill the section, then remove every `<Purpose: ...>` line before sending the prompt.

```markdown
# Assignment: <title>

## Purpose and Background
<Purpose: give the worker the reason for the work. The worker cannot see the conversation in this thread (coordinator).>
<Overall delivery, relevant background, and why this assignment matters.>

## Assigned Goal
<Purpose: define the single outcome that the worker owns, so that the worker knows what to deliver and when to stop.>
<One bounded outcome, its concrete effect, and observable successful behavior.>

## Requirements and Decisions
<Purpose: bind the worker to what is already agreed, so that the worker does not redesign the solution or decide by assumption.>
- Applicable requirements and expectations: <...>
- Constraints and agreed decisions: <...>
- Approved implementation direction and applicable KISS constraints: <...>
- Unresolved decisions and dependent work that must stop: <...>

## Scope, Ownership, and Dependencies
<Purpose: set the boundaries of the work, so that the worker does not expand scope and parallel workers do not change the same outputs.>
- Included and excluded work: <...>
- Allowed and excluded inputs: <...>
- Owned outputs and permitted changes: <...>
- Elements that must remain untouched: <...>
- Dependencies and shared interfaces: <...>

## Background Information and References
<Purpose: give the worker all information that the work needs, including results of predecessor tasks.>
<Relevant documents, paths, links, versions, and sections to read.>
<Existing mechanism to reuse, where applicable.>
<State explicitly when no additional references exist.>

## Expected Result
<Purpose: define the form of the deliverable, so that this thread (coordinator) can use it without conversion.>
- Deliverables and required content: <...>
- Output locations and format: <...>
- Required level of detail: <...>

## Self-Validation and Completion
<Purpose: make the worker prove the result in its response before reporting completion.>
- Checks that demonstrate the assigned effect: <...>
- Observable completion criteria: <...>
- Validation evidence to report in the Return Format: <...>

## Control and Escalation
<Purpose: tell the worker when to stop and ask instead of deciding.>
- Steering mode and consultation triggers: <...>
- Decisions reserved for the user: <...>
- Blockers and material discoveries to report: <...>
- Report missing context that affects correctness.
- Do not expand scope or resolve missing decisions by assumption.

## Return Format
<Purpose: give this thread (coordinator) a short, uniform summary to track the delivery.>
Status: complete | partial | blocked
Deliverables: <paths and relevant sections>
Result: <concise concrete outcome>
Validation: <checks, results, and evidence>
Material issues: <...>
User decision required: <question, impact, and recommendation, or none>
Remaining work and next action: <...>
```

Check prompt completeness before delegation. Limit this check to structural completeness and the presence of agreed decisions.

## Local Checks and Batched Verification

Require each worker to run the checks that demonstrate its assigned effect and to report the evidence in its response.

Delegate verification for each verification group, against its shared acceptance outcome. Include interactions and combined behavior. Do not review each task separately.

Provide the verifier with:

- Relevant artifacts and ownership.
- Approved acceptance criteria.
- Local validation evidence.
- Interactions and combined behavior to check.

Reuse evidence for outputs that did not change after the check. Repeat checks only after changes, failures, or unresolved concerns.

Require verification findings tied to acceptance criteria and concrete evidence.

Require the verifier to return concise acceptance findings, evidence references, and bounded correction needs.

## Result Acceptance and Escalation

Accept a result only on verification findings, not on the worker's completion claim.

In status reports, label each item as a proposed decision, completed work, or a verified outcome.

When a result falls short, start a fresh worker with a newly defined correction goal. Include the failed criteria and the verification findings in its prompt.

Verify the corrected result against the same criteria.

Assign resolution within the agreed scope. Consult when resolution requires a user decision.

Do not hide material issues as ordinary open questions. Report blocked status when they prevent completion.

Leave open only minor-impact limitations or extensions beyond scope. State their impact.

## Interruptions

If a worker is interrupted, continue it with its `sessionID`. A session is unusable when it no longer responds, has lost the assignment context, or the user states that the session is unusable, unresponsive, or cancelled. In that case, start a fresh worker with the complete prompt. Require it to inspect its owned outputs first and continue from their current state.
