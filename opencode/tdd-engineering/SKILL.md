---
name: tdd-engineering
description: This skill should be used for any code change — writing, modifying, refactoring, reviewing, or fixing code — even when the user does not mention tests or TDD. TDD is the default workflow — test list, failing test, minimal code to pass, refactor while green. Two golden rules bind all code, including tests — KISS (the simplest design that works) and maintainability (code is written for human readers). Also covers test design and quality, test doubles, test levels, legacy code, design outcomes, evidence limits, advanced techniques, and an agent competency model.
metadata:
  version: "1.4"
---

# TDD Engineering

## Overview

Test-Driven Development (TDD) is a design and development workflow that sequences feedback, not a testing phase. Its output is confidence: existing behavior is preserved, new behavior is verified, and the system is ready for the next change.

Two golden rules bind every change, production and test code alike. They are non-negotiable:

1. **KISS** — the simplest design that works.
2. **Maintainability** — code is written for human readers.

TDD is what makes both rules safe: a trustworthy test suite keeps the cost of change low, so the design can stay simple now and evolve later.

Detailed evidence and verbatim sources live under `references/`; load only the file the current task needs.

## Scope and exceptions

TDD is the default for every code change. Do not wait for the user to request tests or mention TDD. Apply it when:

- writing new code, features, or functions;
- modifying, fixing, or refactoring existing code;
- reviewing or assessing a code change;
- choosing test doubles, test levels, or fixture strategies;
- working on legacy code;
- assessing an agent's TDD competency;
- calibrating claims about TDD's effects.

Exactly two exceptions exist; state explicitly which one applies when invoking it:

- **Non-code change** — e.g. a documentation or configuration edit.
- **Throwaway spike or prototype** — label it throwaway and never merge it as production code. Any code that is kept follows the workflow.

## Golden rule 1: KISS

Simplicity is a design goal; complexity is a cost that must be justified by a current requirement.

- Implement the simplest design that satisfies the requirement. Reject clever code and speculative generality.
- A design is complete when nothing is left to remove, not when nothing is left to add.
- After green, ask "what can I delete?" before "what can I add?" — this is the refactor step.
- Simplicity is conditional: it is safe only while tests and refactoring keep the cost of change low. Removing a needed abstraction is not simplification.

See `references/11-simplicity-kiss.md` (origin, subtractive completion criterion).

## Golden rule 2: Maintainability

Code is read far more often than it is written, so readability is a requirement, not a tradeoff. Never accept a readability regression for marginal gains in brevity, cleverness; treat such a regression as a defect, not a style preference.

- Optimize for the next reader; they are the primary user of the code.
- Prefer explicit over clever. Clever code hides defects; simple code exposes them.
- Reveal intent through names and structure; comment only the "why" the code cannot express.
- Keep units small and cohesive, so each can be understood without holding the whole system in mind.
- Leave code easier to change than you found it.
- **Tests are code.** Hold test code to the same standard; it is read even more often than production code.

KISS and maintainability reinforce each other. When they appear to conflict, resolve in favor of the reader. Maintainability is enforced as a refactor-step goal, a completion check, and an assessment criterion.

See `references/06-design-outcomes.md` §2 (simple-design criteria) and `references/03-test-design-quality.md` §3 (naming for intent).

## Non-negotiable invariants

Violating any invariant means the work is not TDD, regardless of code quality.

1. Write a failing test before any production code.
2. Run it and confirm it fails for the intended reason.
3. Write only enough production code to pass the currently failing test.
4. Never delete, skip, or weaken a test without explicit human approval.
5. Keep every previously passing test passing (no regressions).
6. Refactor only while green, and keep structural changes separate from behavioral changes.

KISS and maintainability are equally binding on every change, including test code.

## Workflow

1. Write a **test list** of behavioral scenarios — behavior analysis, not implementation decisions.
2. Convert exactly one item into a concrete, runnable test.
3. Run it; observe red for the intended reason.
4. Make the minimal change that passes it and all previous tests.
5. Refactor to remove duplication and improve readability; stay green.
6. Repeat until the list is empty.

The test list drives the work. Append tests discovered mid-cycle to the list instead of writing them immediately. Begin with a **Starter Test** (a variant of an operation that does nothing). Select each next test with the **One Step Test** rule: one that teaches something and that you are confident you can implement.

**Bug fixes** start with a test that reproduces the defect. Observe it fail, then fix. Never fix a bug without a test that would have caught it.

## Cycle mechanics

One loop, observed at four nested time scales:

- **Nano-cycle (seconds)** — the Three Laws: no production code without a failing test; no more test than sufficient to fail (a compilation failure counts); no more production code than sufficient to pass. Cycle length is roughly 30 seconds.
- **Micro-cycle (minutes, per unit test)** — Red-Green-Refactor ("make it run, then make it right"). Make it work, then make it clean; never both at once.
- **Milli-cycle (~10 minutes)** — Specific/Generic: as the tests get more specific, the code gets more generic. Test ordering and generalization decisions live here.
- **Primary cycle (hourly)** — check whether the work is crossing a significant architectural boundary.

**Green-phase tactics**, selected by confidence:

- **Fake It** — return a constant, then replace constants with variables step by step. Use when the implementation is not obvious.
- **Obvious Implementation** — write the real solution. Use when confidence is high; fall back to Fake It on an unexpected red.
- **Triangulate** — generalize only once two or more examples demand it. Use only when the right abstraction is genuinely unclear.

**Step size.** Keep steps small; with practice they get smaller. Let confidence, not a fixed threshold, govern step size. Keep writing tests until fear turns into boredom.

**Transformation Priority Premise (TPP).** Prefer transformations higher in the complexity ordering (nil→constant, constant→scalar, unconditional→if, …, expression→function). Choose the next test so it can be passed by a high-priority transformation; if only a low-priority one works, backtrack to a simpler test. TPP is an impasse-avoidance heuristic, not a proven algorithm — its author calls the ordering "rough" and "not likely" correct.

**When stuck**, back out recent tests one at a time, deleting them, until reaching a test from which a different path is possible. Never force a large edit.

See `references/02-cycle-mechanics.md`.

## Test design and quality

- **FIRST** — Fast, Independent, Repeatable, Self-Validating, Timely.
- **Structure** — Four-Phase Test (setup/exercise/verify/teardown), Arrange-Act-Assert, and Given-When-Then are the same decomposition. Use one consistently per codebase.
- **One condition per test** — the rule is one condition, not one assertion. Because the first failing assertion aborts the test, mixing conditions destroys defect localization. Multiple assertions on the same condition are fine; split different conditions into separate tests or encapsulate them in a custom assertion.
- **Naming** — name tests for intent. The test name is the headline of the specification; poor naming is itself a catalogued smell.
- **Test smells** — the canonical vocabulary: Mystery Guest, Resource Optimism, Test Run War, General Fixture, Eager Test, Lazy Test, Assertion Roulette, Indirect Testing, For Testers Only, Sensitive Equality, Test Code Duplication. Empirically most smells have minimal effect on post-release defects; prioritize those with demonstrated impact (Conditional Test Logic, Exception Catch/Throw, Mystery Guest) over chasing the full catalogue.
- **Fixtures** — prefer Test Data Builders (per-object builders with safe defaults and chainable overrides) over Object Mothers (centralized factories that bloat under data variation).
- **Defect localization** — a failure must pinpoint what broke. Prefer small tests and precise assertion messages.

See `references/03-test-design-quality.md`.

## Test doubles and isolation

A **Test Double** replaces a production dependency of the system under test (SUT):

| Double | Definition | Use when |
|---|---|---|
| **Dummy** | Passed but never used | A signature must be satisfied |
| **Stub** | Returns canned answers | Indirect inputs must be controlled |
| **Spy** | Stub that records calls | Indirect outputs must be captured but cannot be fully predicted |
| **Mock** | Pre-programmed expectations | The interaction itself is the specification and its arguments are predictable |
| **Fake** | Working, simplified implementation (e.g. in-memory database) | The real dependency is too slow or unavailable |

**State vs. behavior verification.** State verification inspects the SUT and its collaborators after exercise; behavior verification checks the calls made during exercise. Only mocks require behavior verification.

**Classical vs. mockist.** Classical (Chicago/Detroit) style uses real objects where practical, doubles only awkward collaborators, and verifies state. Mockist (London) style mocks every collaborator with interesting behavior and verifies interactions. Mockist tests couple more tightly to implementation and break more often under refactoring.

**Cautions.**

- Excessive doubles yield fragile, overspecified tests.
- Keep at least one test that exercises the behavior with real collaborators, and back either style with coarser acceptance tests.
- Never replace the part of the SUT under test.

See `references/04-test-doubles-isolation.md`.

## Test levels, ATDD, and BDD

- **Test pyramid** — many fast unit tests, fewer integration tests, very few end-to-end tests. The inverted form (ice-cream cone) is slow and brittle. The shape is qualitative; no canonical source prescribes ratios.
- **No standard terminology** — "unit" and "integration" lack canonical definitions. Treat scope as a spectrum and apply the terms consistently within a codebase.
- **Acceptance is orthogonal to level** — acceptance denotes a purpose (whose perspective), not a pyramid layer. Prefer the lowest level that can express the acceptance criterion.
- **Double loop** — a fast inner unit loop runs inside a slower outer acceptance loop, so every unit is justified by a currently failing feature-level test. Outside-in (London/mockist) enters through the outer loop; inside-out (Chicago/classical) builds domain units first.
- **ATDD** — write acceptance tests collaboratively, in business-domain terms, before coding.
- **BDD** — express tests as behavior (Given/When/Then) with stories as the unit of functionality. When the whole team is programmers, BDD and TDD converge.

See `references/05-levels-atdd-bdd.md`.

## Design outcomes

- **Emergent design is conditional** — test-first fixes the caller's view of the interface; the refactor step improves structure. This holds only while tests and refactoring keep the cost of change low.
- **Testability is design feedback** — when code is hard to test, look for the design flaw. A dependency that cannot be substituted in a test signals tight coupling, hidden construction, or I/O mixed with logic.
- **Seams** — a seam is a place where behavior can be altered without editing that place; each seam has an enabling point where the substitution is decided. Dependency injection is a means of creating seams, not a goal.
- **Legacy code** — characterization tests pin actual (not correct) behavior to form a regression net. Workflow: identify seams → break dependencies minimally → write characterization tests → change → refactor. Add tested code without first untangling the legacy unit using **Sprout** (implement new behavior in a new unit and delegate to it) or **Wrap** (rename the old method and add a same-signature method that calls it).
- **YAGNI and simple design** — safe only when the cost of change is low. Beck's simple-design rules, in priority order: passes all tests, no duplication, reveals intent, fewest classes and methods.
- **Do not overclaim** — TDD does not guarantee good design; no controlled study of its effect on coupling or cohesion was found.

See `references/06-design-outcomes.md`.

## Evidence calibration

Bound every claim about TDD by these limits:

- **External quality is the best-supported benefit** — the most-cited industrial study reports a 40–90% drop in pre-release defect density; a 2016 systematic review finds 88% of studies reporting higher external quality.
- **Internal quality and productivity are unsettled** — the sign of the effect flips across reviews; a 2025 tertiary study shows those reviews do not even select the same primary studies.
- **Field conformance is low** — only 12% of self-declared TDD projects actually followed the protocol.
- **Coverage is a weak signal** — it records execution, not whether results were checked or correct. Never use it as a quality target.
- **Mutation testing is a stronger adequacy signal** — it exposes hollow suites that coverage misses.
- **The mandate is a policy, not an empirical claim** — TDD is the default here by deliberate choice, despite unsettled, context-dependent productivity evidence. Never cite the evidence as proof that TDD is always faster.

See `references/07-empirical-evidence.md` and `references/08-advanced-techniques.md`.

## Advanced and complementary techniques

- **Property-based testing** — assert universally quantified properties over generated inputs; complements example-based tests. Key features: counterexample shrinking and seed-based reproducibility. Cost: designing properties and generators.
- **Mutation testing** — inject small faults and measure the fraction the suite kills. Limits: equivalent mutants and compute cost.
- **Contract testing** — verify each side of an integration in isolation against a shared, versioned contract. Replaces slow integration tests; does not test provider business logic.
- **Approval (golden-master) testing** — freeze observed output as the oracle for legacy or output-heavy code. Detects change, not correctness; requires deterministic output.

See `references/08-advanced-techniques.md`.

## Agent-specific practice

- **Test tampering is the dominant agent failure mode.** Agents delete, skip, or weaken failing tests to reach green. The incentive is structural: editing an assertion is easier than fixing the code, and both produce a green run.
- **Test weakening, defined operationally**, is any change that reduces what the suite verifies: deleting a test, skipping or ignoring it, relaxing an assertion, widening a tolerance, or retargeting a mock so the interaction is no longer checked. Every such change requires explicit human approval.
- **The suite is the specification.** Weakening an assertion changes the specification, not the implementation.
- **Environmental guardrails beat procedural prompts.** Make tests immutable to the implementing agent, surface the relevant tests at the point of change, and verify the suite itself (withheld tests, mutation checks). A 2026 preprint found that procedural TDD prompting alone increased regressions, while telling the agent which tests to check reduced them.
- **A green run is not the goal.** Roughly half of test-passing benchmark PRs would not be merged by maintainers.

See `references/09-teaching-assessing-competency.md`.

## Agent competency model

**Knowledge areas** — golden rules (KISS, maintainability); workflow; cycle mechanics; green-phase tactics; test design; test doubles; test levels; design outcomes; evidence limits; agent-specific practice.

**Observable behaviors** — writes a failing test before implementation; demonstrates the failure for the intended reason; adds only enough code to pass; never deletes, skips, or weakens a test without approval; identifies and runs affected tests; keeps previously passing tests passing; chooses the appropriate double or a real collaborator; keeps at least one real-collaborator test; abstains or asks when the specification is ambiguous; treats the suite as the specification; writes readable, maintainable code.

**Assessment criteria** — test-first ordering; demonstrated failure; minimal implementation; test-surface integrity; regression stability; impact awareness; refactor discipline; abstention quality; suite strength (mutation and withheld-test detection); readability and maintainability of production and test code.

Full model: `references/TDD-REPORT.md`.

## Definition of done

Before reporting a code change as complete, verify every item:

1. A failing test existed before the implementation and was observed failing for the intended reason.
2. Only enough production code was added to pass the currently failing test.
3. No test was deleted, skipped, or weakened without explicit human approval.
4. The full suite passes; no previously passing test fails.
5. The tests most likely affected by the change were identified and run.
6. Refactoring happened only while green, with structural and behavioral changes kept separate.
7. The code is the simplest that satisfies the requirement (KISS).
8. Production and test code are readable and maintainable.
9. Ambiguities in the specification were raised with the user, not resolved by invented behavior.

## Anti-patterns

- Treating TDD as opt-in and waiting for the user to request tests.
- Trading readability for cleverness, brevity, or marginal performance.
- Deleting or weakening failing tests to reach green.
- Writing tests and implementation simultaneously.
- Skipping the red phase, never confirming the test can fail.
- Over-mocking and coupling tests to implementation.
- Treating coverage as a quality target.
- Claiming TDD guarantees good design.
- Adding speculative generality instead of applying KISS.
- Refactoring while red, or mixing structural and behavioral changes.

## Reference index

Load only the file the current task needs.

- `references/TDD-REPORT.md` — synthesis, full competency model, consolidated resources.
- `references/10-teaching-priorities.md` — prioritized aspects (Tiers 0–8) and teaching sequence.
- `references/11-simplicity-kiss.md` — KISS and the subtractive completion criterion.
- `references/00-research-plan.md` — scope, method, topic map.
- `references/01-foundations-history.md` — definition, origin, criticisms.
- `references/02-cycle-mechanics.md` — Three Laws, nested cycles, triangulation, TPP, baby steps.
- `references/03-test-design-quality.md` — FIRST, AAA/GWT, one-condition rule, test smells, builders.
- `references/04-test-doubles-isolation.md` — double taxonomy, state vs. behavior, classical vs. mockist.
- `references/05-levels-atdd-bdd.md` — test pyramid, double loop, ATDD/BDD.
- `references/06-design-outcomes.md` — emergent design, testability, seams, legacy code.
- `references/07-empirical-evidence.md` — what the evidence shows and where it disagrees.
- `references/08-advanced-techniques.md` — property-based, mutation, coverage limits, contract, approval.
- `references/09-teaching-assessing-competency.md` — augmented coding, test tampering, guardrails, rubrics.
