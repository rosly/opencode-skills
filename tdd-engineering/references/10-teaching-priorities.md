# TDD Teaching Priorities for an LLM Agent

This file is the prioritized list of aspects an LLM agent should be taught for practical TDD. Priority reflects failure severity, not teaching order. Deep detail lives in the numbered evidence files (`01-` through `09-`) and the synthesis (`TDD-REPORT.md`).

## Prioritization principle

Tier 0 items are invariants: violating any one means the agent is not doing TDD, regardless of how good the code looks. Lower tiers add capability and calibration.

## Tier 0 — Invariants (must never be violated)

| # | Aspect | Why it matters | Reference |
|---|--------|----------------|-----------|
| 1 | Failing test before production code | The defining act of TDD; without it there is no red state to trust | `02-cycle-mechanics.md` §2; `09-teaching-assessing-competency.md` §1 |
| 2 | Observe red for the intended reason | A test that fails for the wrong reason proves nothing | `02` §2, §3 |
| 3 | Minimal code to pass | Prevents design work leaking into the green phase | `02` §2; `09` §1 |
| 4 | Never delete/skip/weaken tests without explicit approval | The dominant agent failure mode; silently corrupts red→green | `09` §4, §5 |
| 5 | No regressions | Green must mean the whole suite, not the new test | `09` §7 |
| 6 | Refactor only while green; separate structural from behavioral changes | Keeps the safety net valid | `02` §3; `09` §1 |

## Tier 1 — Core cycle execution

| # | Aspect | Why it matters | Reference |
|---|--------|----------------|-----------|
| 7 | Test list as the driver | Beck's canon step 1; prevents ad-hoc test writing | `02` §4 |
| 8 | Red-Green-Refactor micro-cycle | The per-test loop | `02` §3 |
| 9 | Three Laws / nano-cycle granularity | Enforces ~30-second, line-level steps | `02` §2 |
| 10 | Green-phase tactics: Fake It / Obvious Implementation / Triangulate | Choosing how to reach green by confidence | `02` §5, §6 |
| 11 | Step size / baby steps; downshift on surprise | Dynamic control knob tied to confidence | `02` §8 |
| 12 | Test selection: One Step Test, Starter Test | Which test next; where to start | `02` §4 |
| 13 | Specific→generic (milli-cycle) | Tests get more specific, code more general | `02` §1 |
| 14 | TPP as a heuristic, not an algorithm | Avoids impasses; author calls the order "rough" | `02` §7 |
| 15 | Backtracking when stuck | Delete tests back to a fork rather than forcing a big edit | `02` §1 |

## Tier 2 — Test design quality

| # | Aspect | Why it matters | Reference |
|---|--------|----------------|-----------|
| 16 | FIRST (Fast, Independent, Repeatable, Self-Validating, Timely) | Baseline quality criteria | `03-test-design-quality.md` §1 |
| 17 | Structure: Four-Phase / AAA / Given-When-Then | Same decomposition, three phrasings | `03` §2 |
| 18 | One condition per test (not literally one assertion) | First-failure abort destroys defect localization | `03` §4 |
| 19 | Naming for intent | Test name is the specification's headline | `03` §3 |
| 20 | Test smells — and which ones actually matter | Only Conditional Test Logic, Exception Catch/Throw, Mystery Guest showed defect association | `03` §5, §7 |
| 21 | Fixture construction: builders vs object mothers | Builders survive data variation; object mothers bloat | `03` §6 |
| 22 | Defect localization / assertion messages | A failure must say what broke | `03` §4 |

## Tier 3 — Isolation and doubles

| # | Aspect | Why it matters | Reference |
|---|--------|----------------|-----------|
| 23 | Double taxonomy (Dummy/Stub/Spy/Mock/Fake) | Vocabulary for the role a double plays | `04-test-doubles-isolation.md` §2 |
| 24 | State vs behavior verification | Determines what the test actually asserts | `04` §3 |
| 25 | Classical vs mockist (Chicago vs London) | Default isolation boundary and design stance | `04` §4 |
| 26 | When to use each double | Input control vs output capture vs interaction spec | `04` §5 |
| 27 | Over-specification / fragile tests | Doubles encoding incidental detail make tests brittle | `04` §6 |
| 28 | Keep at least one real-collaborator test | Guards against a suite that passes while the system is wrong | `04` §5 |

## Tier 4 — Scope and levels

| # | Aspect | Why it matters | Reference |
|---|--------|----------------|-----------|
| 29 | Unit/integration/acceptance as a scope spectrum | Terminology is not standardized; "unit" has no canonical answer | `05-levels-atdd-bdd.md` §1 |
| 30 | Test pyramid and ice-cream cone | Distribution of test granularity | `05` §2, §3 |
| 31 | Double loop / outside-in | Each unit justified by a failing acceptance test | `05` §4, §5 |
| 32 | Acceptance is orthogonal to level | Acceptance is a purpose, not a pyramid layer | `05` §1 |
| 33 | ATDD/BDD collaboration and Given-When-Then | Producing the outer-loop criteria in shared language | `05` §6, §7 |

## Tier 5 — Design outcomes

| # | Aspect | Why it matters | Reference |
|---|--------|----------------|-----------|
| 34 | Emergent design is conditional on refactoring + low change cost | Not an automatic product of test-first | `06-design-outcomes.md` §1 |
| 35 | Testability as design pressure | Hard-to-test signals a design problem | `06` §3 |
| 36 | Seams and enabling points | Where behavior can vary without editing that place | `06` §6 |
| 37 | Dependency injection as a means, not an end | Creates seams; not a goal in itself | `06` §5 |
| 38 | Characterization tests and the legacy workflow | Bootstrapping tests into untested code | `06` §7, §8 |
| 39 | YAGNI / simple design conditions | Safe only when change cost is low | `06` §2 |
| 40 | The design-causation counter-position (Seemann) | Prevents overclaiming that TDD guarantees good design | `06` open questions |

## Tier 6 — Evidence calibration

| # | Aspect | Why it matters | Reference |
|---|--------|----------------|-----------|
| 41 | External quality is the best-supported claim | Defect reduction 40–90% in the most-cited study | `07-empirical-evidence.md` §1 |
| 42 | Internal quality and productivity are unsettled | The sign flips across reviews | `07` §2, §3 |
| 43 | Low field conformance to TDD | Only 12% of self-declared TDD projects actually followed it | `07` §5 |
| 44 | Coverage is a weak quality signal | Executed ≠ checked ≠ correct | `08-advanced-techniques.md` §3 |
| 45 | Mutation testing as a stronger adequacy signal | Detects hollow suites coverage misses | `08` §2 |

## Tier 7 — Advanced / complementary techniques

| # | Aspect | Why it matters | Reference |
|---|--------|----------------|-----------|
| 46 | Property-based testing | Complements example-based tests; shrinking and seeds | `08` §1 |
| 47 | Contract testing | Replaces slow integration checks across a boundary | `08` §4 |
| 48 | Approval / golden-master testing | Oracle for legacy or output-heavy code; detects change, not correctness | `08` §5 |

## Tier 8 — Agent-specific practice

| # | Aspect | Why it matters | Reference |
|---|--------|----------------|-----------|
| 49 | Test tampering failure mode | Agents delete/weaken tests to reach green | `09` §4 |
| 50 | Environmental guardrails over procedural prompts | Immutable, discoverable, intent-bearing tests | `09` §5, §6 |
| 51 | The prompting paradox | Procedural TDD prompts alone increased regressions | `09` §3 |
| 52 | Withheld tests / mutation checks | Prevents satisfying the letter of a test while missing intent | `09` §3, §5 |
| 53 | Assessment criteria / observable behaviors | How to judge competency, not just outcome | `09` §7; `TDD-REPORT.md` competency model |

## Deprioritize (teach only as caveats, not as skills)

- Framework-specific APIs — out of scope by design; the research is strictly language-agnostic.
- Historical debate detail (`01-foundations-history.md`) — useful context, not a practical skill.
- TPP's exact ordering (`02` §7) — its author calls it "rough" and "not likely" correct; teach it as an impasse heuristic.
- The exhaustive smell catalogue (`03` §5) — teach the impactful subset, not all 13+.
- Numeric pyramid ratios (`05`) — no canonical source gives them; the shape is qualitative.
- "Double loop" attribution (`05` open questions) — unresolved; do not teach it as settled.

## Sequence vs priority

Priority is by failure severity. A practical teaching sequence differs: start with Tier 0 invariants and Tier 1 cycle, then Tier 2 test quality, then Tier 3 doubles, and introduce Tiers 4–8 as scope grows. Tier 6 (evidence calibration) is best taught late, as a guard against overclaiming.
