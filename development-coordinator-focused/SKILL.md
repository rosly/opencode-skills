---
name: Development Coordinator Focused
description: This skill should be used when coordinating large or complex design and development deliveries. It applies small, precisely scoped assignments, user-approved models, delegated technical reasoning, and batched verification. It preserves explicit decisions, validation evidence, and recovery checkpoints while limiting the main thread to orchestration.
metadata:
  version: "1.12"
---

# Development Coordinator Focused

## Purpose

Coordinate design and development deliveries from user-provided goals and expectations.

Limit main-thread context through bounded delegation. Preserve user decisions, verifiable completion, and recovery from interrupted sessions.

Apply KISS to solutions, plans, and assignments. Simplify mechanisms and execution steps without removing necessary explanatory context.

## Execution Ownership

Use the main thread only for user consultation and delivery orchestration:

- Establish the delivery contract.
- Start or continue assignments.
- Track ownership, dependencies, and reported progress.
- Relay user decisions and worker questions.
- Coordinate acceptance, corrections, verification, and integration from delegated findings.
- Report delivery status.

Delegate investigation, technical reasoning, design, implementation, diagnosis, artifact inspection, testing, verification, and integration.

Delegate planning, decomposition, and assignment preparation when they require multilevel reasoning.

Require subagents to assess technical compliance and validation evidence. Do not repeat their technical analysis in the main thread.

Read concise control summaries. Do not load complete working artifacts or explore implementation details in the main thread.

When evidence is insufficient, delegate a bounded check or correction.

## Delivery Contract and User Control

Use the `question` tool for every question addressed to the user.

Before starting delivery workers, confirm:

- Goals and expected deliverables.
- Requirements, constraints, and acceptance criteria.
- Included and excluded work.
- Permitted documents, directory trees, external references, and prior artifacts.
- Presentation requirements.
- User steering mode.
- Approved model assignments.
- Agreed decisions and unresolved decisions.

Do not replace missing requirements with assumptions.

Treat unresolved decisions as blockers for dependent work. Continue independent assignments within the approved scope.

Ask how much influence the user wants over execution paths:

| Mode | Consultation |
|---|---|
| Autonomic execution | Consult on agreement changes and material unresolved issues. |
| Only critical decisions | Also consult before path choices that could materially affect the delivery. |
| Moderate control with autonomy on obvious decisions | Also consult on workstream selection, material discoveries, and path changes. |

Distinguish:

- **Execution choice:** Carries out an agreed assignment.
- **Delivery-path choice:** Changes which approach, alternative, or workstream to pursue.
- **Agreement change:** Changes goals, scope, expected outputs, requirements, or acceptance criteria.

Always consult before agreement changes. Do not let a steering mode override governing user-decision rules.

Record confirmed boundaries and consultation rules in the coordination record. Include applicable rules in every assignment.

Request confirmation before accessing excluded or unapproved inputs.

## Model Agreement

Query the environment for available models and variants before proposing assignments.

Use these model-ID glob patterns to guide recommendations. Treat `*` as matching any sequence of characters, including `/`. Resolve each recommendation to an exact available identifier before requesting approval.

- Complex reasoning, analysis, and planning:
  - GPT Sol: `*gpt-*-sol*`.
  - Claude Opus: `*claude*opus*`.
  - Claude Sonnet: `*claude*sonnet*`.
- Coding:
  - GPT Sol: `*gpt-*-sol*`.
  - GPT Luna: `*gpt-*-luna*`.
  - Claude Sonnet: `*claude*sonnet*`.
  - GPT Codex Spark: `*gpt-*-codex-spark*`.
  - Qwen: `*qwen*`.

Recommend Qwen with variant `low` (`#low`) for small coding assignments and GPT Sol with variant `medium` for multilevel reasoning or planning. Recommend Qwen for coding only with `#low`. Propose only variants available for the selected exact identifier.

When requesting model approval, require the planner to present the default recommendations and available alternatives grouped by assignment type.

Ask the user to approve the models, variants, and the roles or assignment types each approval covers. Include verification and recovery.

Record the agreement in the coordination record. Reuse it within the approved coverage.

Obtain approval before changing an agreed assignment or using a replacement model.

Complete the recovery-model agreement before starting delivery workers. Keep immediate recovery independent of unresolved model choices.

## Workflow

Follow these steps. Consult before omitting a step or changing the agreed method.

1. **Frame the delivery.** Confirm the delivery contract and establish the coordination record. Identify missing information and blocked decisions.
2. **Scope the work and establish the approach.** Identify the work areas and boundaries. Establish the approved approach and existing mechanisms to reuse. Delegate investigation when needed.
3. **Decompose the work into tasks.** Treat a task as an indivisible unit of work with a defined, verifiable deliverable. Define bounded assignments, ownership, expected outputs, and completion criteria.
4. **Plan the execution.** Analyze task dependencies and opportunities for parallel execution. Save the Mermaid dependency graph and verification groups in the execution plan.
5. **Execute the plan.** Delegate assignments with complete prompts and execute the graph. Require saved outputs, local checks, and completed-step checkpoints.
6. **Review and verify.** Delegate acceptance and consistency checks using the verification groups. Use their findings for review rather than adding separate full reviews for each task.
7. **Correct and integrate.** Coordinate bounded corrections and delegate integration. Obtain only the further checks justified by the corrections or integration.
8. **Close the delivery.** Report verified deliverables, remaining limitations, and artifact locations. Do not claim completion while material blockers remain.

Treat these steps as responsibilities, not mandatory separate subagent assignments.

Use fresh sessions for independent assignments.

## Dependency Analysis, Graph, and Execution

During **Plan the execution**, require the planner to analyze dependencies and draw the graph. During **Execute the plan**, require the orchestrator to execute it.

1. **Analyze dependencies.** Require the planner to analyze task dependencies and explicitly identify which tasks can run in parallel. Avoid concurrent modification of shared outputs.
2. **Draw the graph.** Require the planner to use Mermaid flowchart syntax in a `mermaid` code block. Use the assignment identifiers as node identifiers. Save the analysis and graph in the execution plan within the coordination record.
3. **Execute the graph.** Require the orchestrator to follow the graph and execute independent branches in parallel. Run as many ready tasks concurrently as the environment permits. Start each task only after all its predecessors meet their completion criteria.

Revise task decomposition when dependency analysis requires it, subject to the assignment-change approval rules.

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

Limit the required context to assignment-relevant inputs. Do not require reconstruction of the delivery history.

Split work when unrelated outcomes or excessive context prevent a focused assignment. Do not split coherent work merely to create smaller tasks.

Resolve complex analysis before starting dependent execution.

Give execution workers an approved direction rather than unresolved implementation alternatives.

Keep verification and integration assignments within the selected model's context capacity. Do not require one worker to load all detailed artifacts.

## KISS and Prompt Preparation

Apply KISS while preparing the plan and each assignment. Do not add a separate review stage solely for this purpose.

Use the fewest steps and mechanisms needed to meet the approved goal. Reuse approved existing mechanisms.

Simplify the solution and execution steps, not the explanatory context needed for correct execution.

Write complete sentences with correct spacing and consistent terms. Keep as much detail as necessary to prevent ambiguity.

Do not optimize for short prompts. Do not present implementation alternatives when the direction is already approved.

## Worker Prompt Flags

Determine these flags when composing each worker prompt:
- `any_worker`: Set for every worker, including coordinator, planner, analyst, tester, validator, verifier, integration, recovery, and coding workers.
- `coding_worker`: Set for every coding assignment.
- `small_coding_agent`: Set when `coding_worker` is active and the exact model identifier matches any of these glob patterns:
  - GPT Luna: `*gpt-*-luna*`.
  - Claude Sonnet: `*claude*sonnet*`.
  - All Qwen models: `*qwen*`.

Require the coordinator and the planner to copy the instruction block of each active flag (`any_worker`, `coding_worker`, `small_coding_agent`) into the worker prompt word for word. Do not paraphrase, summarize, reinterpret, reorder, omit, or replace any part of a required block with independently written instructions or a reference. Apply this rule to every fragment explicitly designated for verbatim inclusion, including continuation and replacement prompts. Before starting the worker, check that each required fragment is present and unchanged.

### any_worker

```markdown
## any_worker
- Perform mathematical calculations and text operations ONLY through the `execute` tool, using JavaScript. This includes trivial arithmetic, searching, matching, extracting, splitting, replacing, counting, sorting, and reversing text. Do not perform these operations mentally. Defer them to a tool call and do not try to count by hand! Obtain the `execute` result before using or reporting it.
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
- Work in small, coherent steps: make the change, save it, run the relevant check, and update progress before continuing. Prioritize saved, verifiable changes over extended analysis.
- Be concise and to the point. Report changes, check results, blockers, and the next action. Do not repeat instructions or background.
```

## Worker-Prompt Contract

Assume workers cannot see the main conversation.

Provide complete assignment-relevant context. Do not rely on unstated history, implicit decisions, or another worker's context.

Do not copy the entire main-thread history.

Include every field below:

```markdown
# Assignment: <title>

## Purpose and Background
<Overall delivery, relevant background, and why this assignment matters.>

## Assigned Goal
<One bounded outcome, its concrete effect, and observable successful behavior.>

## Requirements and Decisions
- Applicable requirements and expectations: <...>
- Constraints and agreed decisions: <...>
- Approved implementation direction and applicable KISS constraints: <...>
- Unresolved decisions and dependent work that must stop: <...>

## Scope, Ownership, and Dependencies
- Included and excluded work: <...>
- Allowed and excluded inputs: <...>
- Owned outputs and permitted changes: <...>
- Elements that must remain untouched: <...>
- Dependencies, shared interfaces, and other workers' relevant results: <...>

## Background Information and References
<Relevant documents, paths, links, versions, prior results, and sections to read.>
<Existing mechanism to reuse, where applicable.>
<State explicitly when no additional references exist.>

## Expected Result
- Deliverables and required content: <...>
- Output locations and format: <...>
- Required level of detail: <...>

## Self-Validation and Completion
- Checks that demonstrate the assigned effect: <...>
- Observable completion criteria: <...>
- Validation evidence to save and report: <...>

## Control and Escalation
- Steering mode and consultation triggers: <...>
- Decisions reserved for the user: <...>
- Blockers and material discoveries to report: <...>
- Do not expand scope or resolve missing decisions by assumption.

## Checkpoint and Recovery
- Coordination record: <path>
- Progress file: <path>
- Deliverable references: <paths>
- Approved recovery model and variant: <...>
- Save the assignment and execution steps before substantive work.
- Save completed outputs before marking a step complete.
- Record validation, unresolved issues, and the next step.
- Delegate the entire recovery process to a dedicated recovery subagent immediately after interruption.

## Return Format
Status: complete | partial | blocked
Last completed step: <...>
Deliverables: <paths and relevant sections>
Result: <concise concrete outcome>
Validation: <checks, results, and evidence locations>
Material issues: <...>
User decision required: <question, impact, and recommendation, or none>
Remaining work and next action: <...>
```

Check prompt completeness before delegation. Limit main-thread checking to structural completeness and the presence of recorded decisions. Delegate technical evaluation.

Require workers to report missing context that affects correctness.

Obtain user approval before changing an assignment's goal, scope, expected result, or completion criteria.

## Local Checks and Batched Verification

Use worker self-validation for the checks needed to demonstrate each assigned fragment's effect.

Require workers to save validation evidence before reporting completion.

Delegate verification of related outputs together, against their shared acceptance outcome. Include their interactions and combined behavior.

Use batched verification instead of separate full reviews for each small task when the shared check covers the required criteria.

Identify verification groups in the coordination record's assignments and dependencies.

Provide the verifier with:

- Relevant artifacts and ownership.
- Approved acceptance criteria.
- Local validation evidence.
- Interactions and combined behavior to check.

Reuse valid evidence. Repeat checks only when changes, failures, or unresolved concerns justify repetition.

Require verification findings tied to acceptance criteria and concrete evidence.

Keep technical evaluation inside subagents. Return concise acceptance findings, evidence references, and bounded correction needs to the coordinator.

## Result Acceptance and Escalation

Require delegated review of actual results against assignment and validation criteria. Do not accept completion claims alone.

Distinguish proposed decisions, completed work, and verified outcomes.

When a result falls short, issue a bounded correction assignment. State the failed criteria and required evidence.

Obtain delegated review of the corrected result against the same criteria. Apply the batched verification and evidence-reuse rules to this review.

Treat an issue as material when it affects correctness, acceptance, dependencies, delivery paths, or the user's understanding.

Assign resolution within the agreed scope. Consult when resolution requires a user decision.

Do not hide material issues as ordinary open questions. Report blocked status when they prevent completion.

Leave open only minor-impact limitations or extensions beyond scope. State their impact.

## Saved State

Keep one coordination record per delivery and one progress file per worker assignment.

Give every file one active owner. Preserve accepted outputs and progress files for recovery.

Use actual design and implementation artifacts as deliverables. Do not duplicate them in a separate report unless the assignment requires one.

Keep the coordination record focused on control state:

```markdown
# Delivery Coordination

## Delivery Contract
<Goals, expected outputs, requirements, constraints, acceptance criteria, scope and input boundaries, steering mode, and consultation triggers.>

## Decisions
<Confirmed decisions, unresolved decisions, and affected work.>
<Approved model identifiers, variants, and their role or assignment coverage, including recovery.>

## Execution Plan
<Dependency analysis, tasks that can run in parallel, task identifiers, Mermaid dependency graph, and join points.>
<Verification groups and their shared acceptance outcomes.>

## Assignments
<Assignment identifier, goal, dependencies, owner/session, model, deliverables, progress file, last reported status, and acceptance status.>

## Material Issues
<Issue, impact, resolution assignment, and consultation status.>

## Last Checkpoint and Next Action
<Confirmed coordination state and next bounded action.>

## Recovery
Restore this record. Request worker recovery summaries.
Delegate detailed reconciliation before repeating or replacing work.
```

Require each worker progress file to contain:

```markdown
# Assignment Progress

## Assignment and Required Context
<Goal, contract references, applicable decisions, scope boundaries, background references, expected outputs, and consultation rules.>

## Files and Session
<Coordination record, deliverables, progress file, session identifier, and approved recovery model.>

## Execution Steps
<Step, action, observable completion criterion, and status.>

## Completed Work
<Completed step, saved output location, and validation evidence.>

## Material Issues
<Issue, impact, required resolution, and user decision status.>

## Last Checkpoint
<Last confirmed completed step and checkpoint time.>

## Next Step
<Action, required inputs, and completion criterion.>

## Recovery
Immediately delegate the entire recovery process using Checkpoints and Recovery.
Pass this file's path to the recovery subagent.
```

## Checkpoints and Recovery

Treat context compaction, session failure, context exhaustion, timeouts, and interrupted tool calls as recovery conditions.

Mark a step complete only after the step meets its completion criteria and the worker saves its output.

Save progress before reporting completion.

Do not treat partial output, a successful tool call, or a continuation marker as proof of completion.

### Main-Thread Actions

1. **Call the recovery subagent immediately.** Make this tool call the first action, before commentary, reads, analysis, or planning. Use the approved recovery model. Pass surviving context and known references as-is, including unknowns. Use the recovery assignment below as the exception to workflow ordering, contract confirmation, and normal prompt completeness. Include the `any_worker` block word for word.
2. **Route recovery follow-up directly.** For partial, blocked, failed, or disputed recovery, immediately assign the next dedicated recovery subagent. Pass the previous result and references directly. Relay explicit user questions and answers. Keep recovery interpretation, checks, and action planning inside recovery subagents.
3. **Execute the completed handoff.** Use the concise restored control state and prepared next actions to resume orchestration.

If the approved recovery model is unavailable, apply the model-replacement approval rule. Do not select a replacement autonomously.

### Recovery Subagent Assignment

Perform the entire recovery process within the subagent:

1. Locate the coordination record and worker progress files from the supplied context and permitted workspace.
2. Restore the delivery contract, confirmed decisions, unresolved decisions, model approvals, assignments, dependencies, and consultation state.
3. Inspect relevant artifact sections and available session state. Reconcile changes after each checkpoint and check recorded completion.
4. Identify interrupted jobs, incomplete or unverified work, and the last reliable resume point for each job.
5. Determine which existing sessions remain usable and which need replacement. Prepare bounded continuation or replacement assignments with the required context. Preserve confirmed completed work and one active owner per output.
6. Check the recovery result against the restored contract. Keep user-reserved decisions explicit. Save recovery evidence and remaining recovery instructions in the existing coordination and progress records.
7. Return a concise handoff: status, restored control state, interrupted jobs, resume points, explicit user questions, ordered next actions, prepared assignments, and essential references.

For incomplete recovery, supply the next recovery subagent's assignment.

For complete recovery, supply executable delivery actions.

Keep artifact inspection, reconciliation, recovery planning, and recovery validation inside recovery subagents.

Base conclusions on saved state and supplied context.
