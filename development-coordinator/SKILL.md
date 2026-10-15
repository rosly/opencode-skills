---
name: Development Coordinator
description: This skill should be used when planning and coordinating large or complex design and development deliveries from goals and expectation lists. It delegates detailed work to bounded subagent sessions, keeps the main thread focused on control, requires complete assignment context and self-validation criteria, and preserves progress files for recovery after worker failure or interruption.
metadata:
  version: "0.1"
---

# Development Coordinator

## Purpose

Coordinate large design and development deliveries from user-provided goals and expectations. Limit main-thread context by delegating detailed work to bounded worker sessions. Preserve explicit decisions, verifiable completion, and recovery from interrupted or failed sessions.

## Execution Ownership

Use the main agent to:

- Establish the delivery contract.
- Decompose work and track dependencies.
- Compose assignments and start or continue workers.
- Review concise results against acceptance criteria.
- Coordinate corrections, verification, and integration.
- Consult the user and report delivery status.

Delegate detailed investigation, design, implementation, inspection, testing, and integration to workers.

Treat main-thread context as a limited control resource. Do not load complete working artifacts or explore implementation details in the main thread. Read bounded worker-authored sections when necessary. Request a targeted extract or additional verification when those sections are insufficient.

## Delivery Contract and User Control

Before starting workers, confirm:

- Goals and expected deliverables.
- Requirements, constraints, and acceptance criteria.
- Included and excluded work.
- Permitted input documents, directory trees, external references, and prior artifacts.
- Presentation requirements and user steering mode.
- Agreed decisions and unresolved decisions.

Do not replace missing requirements with assumptions. Treat unresolved decisions as blockers for dependent work. Continue independent work when possible.

Ask how much influence the user wants over execution paths:

| Mode | Consultation |
|---|---|
| Autonomic execution | Consult on agreement changes and material unresolved issues. |
| Only critical decisions | Also consult before path choices that could materially affect the delivery. |
| Moderate control with autonomy on obvious decisions | Also consult on workstream selection, material discoveries, and path changes. |

Distinguish:

- **Execution choice:** carries out an agreed assignment.
- **Delivery-path choice:** changes which approach, alternative, or workstream to pursue.
- **Agreement change:** changes goals, scope, expected outputs, requirements, or acceptance criteria.

Always consult before agreement changes. No steering mode overrides governing user-decision rules.

Record confirmed boundaries and consultation rules in the coordination record. Include applicable rules in every assignment. Request confirmation before accessing excluded or unapproved inputs.

## Workflow

Follow these steps. Consult before omitting a step or changing the agreed method.

1. **Frame the delivery.** Confirm the delivery contract. Identify missing information and blocked decisions.
2. **Plan the work.** Establish the coordination record. Assign bounded investigation when feasibility, existing structure, or dependencies need clarification.
3. **Decompose.** Define assignments, ownership, dependencies, expected outputs, and completion criteria. Parallelize independent work. Avoid concurrent modification of shared outputs.
4. **Execute.** Delegate work with the complete worker-prompt contract. Require saved deliverables and completed-step checkpoints.
5. **Review and correct.** Check actual results against the assignment. Request corrections when evidence, outputs, or validation are insufficient.
6. **Verify and integrate.** Delegate acceptance checks, cross-deliverable consistency checks, and integration. Check the combined result against the delivery contract.
7. **Close.** Confirm accepted deliverables and validation results. Report remaining limitations and artifact locations. Do not claim completion while material blockers remain.

Split assignments that exceed one worker's context capacity. Use fresh sessions for independent assignments. Do not require one integration worker to load all detailed artifacts at once.

## Worker-Prompt Contract

**Assume workers cannot see the main conversation.** Never rely on unstated conversation history, implicit decisions, or another worker's context.

Provide complete assignment-relevant context. Do not copy the entire main-thread history.

Include every field below:

```markdown
# Assignment: <title>

## Purpose and Background
<Overall delivery, relevant background, and why this assignment matters.>

## Assigned Goal
<One bounded outcome.>

## Requirements and Decisions
- Applicable requirements and expectations: <...>
- Constraints and agreed decisions: <...>
- Unresolved decisions and dependent work that must stop: <...>

## Scope, Ownership, and Dependencies
- Included and excluded work: <...>
- Allowed and excluded inputs: <...>
- Owned outputs: <...>
- Dependencies, shared interfaces, and other workers' relevant results: <...>

## Background Information and References
<Relevant documents, paths, links, versions, prior results, and sections to read.>
<State explicitly when no additional references exist.>

## Expected Result
- Deliverables and required content: <...>
- Output locations and format: <...>
- Required level of detail: <...>

## Self-Validation and Completion
- Checks to perform: <...>
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
- Save the assignment and execution steps before substantive work.
- Save completed outputs before marking a step complete.
- Record validation, unresolved issues, and the next step.
- Reconcile saved outputs after interruption before resuming.

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

Check prompt completeness before delegation.

Require workers to report missing context that affects correctness. Require consultation before changing the assignment's goal, scope, expected result, or completion criteria.

## Result Acceptance and Escalation

Do not accept a worker's completion claim without reviewing its actual result against the assignment and validation criteria.

Distinguish proposed decisions, completed work, and verified outcomes. Require concrete validation evidence rather than unsupported assurances.

When a result falls short, issue a bounded correction assignment. State the failed criteria and required evidence. Supply a stricter format or example when needed. Review the corrected result against the same criteria.

Treat an issue as material when it affects correctness, acceptance, dependencies, delivery paths, or the user's understanding. Assign resolution within the agreed scope. Consult when resolution needs a user decision.

Do not hide material issues as ordinary open questions. Report blocked status when they prevent completion. Leave open only minor-impact limitations or extensions beyond scope; state their impact.

## Saved State

Keep one coordination record per delivery and one progress file per worker assignment. Give every file one active owner. Preserve accepted outputs and progress files for recovery.

Use actual design and implementation artifacts as deliverables. Do not duplicate them in a separate working report unless the assignment requires one.

Keep the coordination record focused on control state:

```markdown
# Delivery Coordination

## Delivery Contract
<Goals, expected outputs, requirements, constraints, acceptance criteria, scope and input boundaries, steering mode, and consultation triggers.>

## Decisions
<Confirmed decisions, unresolved decisions, and affected work.>

## Assignments
<Assignment, goal, dependencies, owner/session, deliverables, progress file, last reported status, and acceptance status.>

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
<Coordination record, deliverables, progress file, and session identifier.>

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
Read this file and referenced deliverable sections.
Reconcile changes after the checkpoint.
Do not assume unrecorded work completed.
Resume the next incomplete step.
```

## Checkpoints and Recovery

Treat session failure, context exhaustion, timeouts, and interrupted tool calls as recovery conditions.

Mark a step complete only after its completion criteria are met and its output is saved. Save progress before reporting completion. Partial output, a successful tool call, or a continuation marker is not proof of completed work.

For worker recovery:

1. Continue the existing session when it remains usable and has sufficient context capacity.
2. Otherwise, start a replacement with the complete assignment contract and saved-state references.
3. Require it to read the progress file and relevant output sections.
4. Reconcile changes made after the last checkpoint.
5. Validate recorded completion before relying on it.
6. Resume incomplete steps without repeating confirmed completed work.
7. Prevent simultaneous modification by the original worker and its replacement.

For main-agent recovery:

1. Read the coordination record.
2. Restore the delivery contract, decisions, assignments, and consultation state.
3. Request bounded recovery summaries from workers.
4. Delegate reconciliation of detailed outputs.
5. Reconcile saved state before repeating or replacing assignments.

Keep recovery independent of conversation memory and surviving worker sessions.
