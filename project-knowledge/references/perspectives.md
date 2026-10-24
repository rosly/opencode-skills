# Knowledge Perspectives

## Use This Reference

Use these questions to define coverage and bounded research assignments. Adapt topic boundaries to the actual project.

Keep shared explanations in an owning topic. Link other perspectives to that topic. Do not create an empty document to satisfy a directory structure.

Distinguish breadth from depth in the corpus map. Mark a subject as mapped, examined in depth, or not examined. Explain important omissions.

## Project and Source Map — research/README.md

- Explain the system's purpose, users, external dependencies, and boundaries.
- Identify major areas and entry points.
- Identify authoritative sources for behavior, public contracts, data, execution, and historical decisions.
- Record source revisions, dirty-source qualifications, and limits of the available history.
- Link perspective topics and the onboarding guide.
- Record coverage, known gaps, and actual indexing verification.

Do not duplicate the detailed argument or evidence of a topic here.

## Concepts — concepts/

- Define terms in the project's context.
- Record aliases, abbreviations, historical names, and overloaded terms.
- Link user-facing terms to their relevant symbols and data representations.
- Distinguish a domain concept from a class or file that represents only part of it.
- Link related behavior, flows, owners, and decisions.

Use a glossary for short definitions. Create a separate concept topic only when its explanation needs more space.

## Functional Behavior — functionality/

- Explain the capability, its users, and observable result.
- Identify entry conditions, inputs, outputs, constraints, and exceptions.
- Explain relevant cancellation, failure, and retry behavior.
- Separate the required contract from observed or implemented behavior.
- Link scenarios, requirements, tests, owners, and historical policy changes.

Explain what the system does. Leave the detailed interaction sequence to flow topics.

## Cross-Component Flows — flows/

- Start from a concrete user action or external event.
- Trace entry, validation, dispatch, execution, state changes, and visible results where applicable.
- Identify the owner of each step and the exchanged data or event.
- Distinguish synchronous calls, queues, streams, callbacks, and background work when present.
- Explain meaningful failure, interruption, and recovery paths.
- Link the corresponding functional rules, architecture, data lifecycle, and tests.

Use sequence diagrams only for relationships checked against sources. Do not turn a static dependency tree into an execution sequence.

## Architecture and Responsibilities — architecture/

- Explain the necessary responsibilities and their owners.
- Describe component boundaries, contracts, and dependency directions.
- Identify ownership of policy, execution, persistence, and presentation where relevant.
- Explain where extension or substitution actually occurs.
- Record important constraints on interaction and dependency.
- Link behavior, flows, data ownership, and decisions that justify the design.

Explain why a boundary matters. Avoid a directory inventory without responsibilities.

## Data and State — data/

- Identify the owner and source of truth for important data.
- Distinguish public shapes, internal representations, stored state, caches, and derived views.
- Explain creation, transitions, persistence, retention, and reconstruction.
- Explain identifiers, units, ordering, consistency, and concurrency only where they affect the mechanism.
- Identify relevant restart, retry, and recovery behavior.
- Link contracts, state-changing flows, implementations, and tests.

Separate proposed state transitions from implemented ones. Do not infer durability from the presence of a data type.

## Evolution and Rationale — history/

- Identify the specific mechanism or policy that changed.
- Explain its prior form and the documented problem.
- Record contemporary constraints and alternatives actually evidenced by sources.
- Link the change, its resulting behavior, and the author's explanation.
- Explain documented trade-offs and subsequent corrections or reversals.
- Identify obsolete names and the limits of historical continuity.

Separate author rationale from present technical interpretation. Compare code and documentation at matching revisions. Check that a historical change belongs to the studied project's history.

Do not invent rejected alternatives. Record missing rationale as a limitation with its impact.

## Development Navigation — development/

- Map a functional or architectural area to its requirements, implementation, contracts, tests, and relevant history.
- Identify documented development and verification commands for that area.
- Distinguish a command found in documentation from a command actually executed during this analysis.
- Explain constraints a contributor must inspect before changing the area.
- Identify which corpus topics would need review after an area changes.
- Link the original contribution instructions instead of copying a competing procedure.

Provide navigation for future work. Do not perform application implementation through this skill.

## Guide — research/project-guide.md

Explain the system in the reader's learning order. Start with purpose and vocabulary. Introduce architecture through representative behavior.

Use the guide template. Link detailed topics and stable claim anchors. Keep its terminology aligned with the English corpus.

Do not silently add unsupported claims during synthesis or translation. Return such claims to topic research first.

## Useful Cross-Perspective Links

- Connect a user concept to a functional rule.
- Connect that rule to a scenario and its responsible components.
- Connect a component's state changes to the data lifecycle.
- Connect behavior to the relevant test assertions or executed observations.
- Connect a surprising policy to a historical decision.
- Connect an area of future work to its sources and verification instructions.

Use only links that help explain or verify the topic. Do not require every topic to link to every perspective.
