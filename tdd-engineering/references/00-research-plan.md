# Test-Driven Development — Research Plan

Date: 2026-10-05
Subject: Test-Driven Development (TDD) in software engineering
Current version/revision: TDD is a stable practice (Kent Beck, late 1990s); the evidence base and AI-era practice are moving. Anchored to 2026-10-05.
Scope: In scope — definition and history, cycle mechanics, test design/quality, test doubles/isolation, test levels and ATDD/BDD, design outcomes, empirical evidence, advanced techniques, and teaching/assessing TDD competency for AI agents. Out of scope — language-specific tooling (strictly language-agnostic), general software testing unrelated to TDD, and implementation of any TDD tooling.

## Initial-scan signals
- Canonical definition and Red-Green-Refactor: Martin Fowler bliki and Kent Beck's book.
- Cycle mechanics: Uncle Bob's "The Cycles of TDD" (nano/micro/milli cycles, Three Laws).
- Test doubles taxonomy: Gerard Meszaros (xUnit Test Patterns) and Fowler's "Test Double" / "Mocks Aren't Stubs".
- Test levels: Fowler's "The Practical Test Pyramid"; BDD from Dan North.
- Design outcomes: Feathers' *Working Effectively with Legacy Code*; Fowler's "Is Design Dead?".
- Empirical evidence: multiple systematic literature reviews with partly conflicting conclusions; a 2025 paper questions SLR reliability.
- Advanced techniques: property-based testing (fast-check docs), mutation testing, coverage limits.
- AI era: Kent Beck's augmented coding; arXiv "Tests as prompt" benchmark; TDAD (test-driven agentic development).
- The prior `tdd-planer` skill covers only atomic-increment planning and requirement→test traceability; it is treated as a lead, not a source.

## Topics
| # | File | Core question | Likely sources |
|---|------|---------------|----------------|
| 1 | 01-foundations-history.md | What is TDD, its origins, and the canonical definition? | martinfowler.com/bliki/TestDrivenDevelopment.html; Beck *TDD: By Example*; is-tdd-dead |
| 2 | 02-cycle-mechanics.md | How does red-green-refactor work (nano/micro/milli cycles, triangulation, transformation priority premise, baby steps)? | blog.cleancoder.com TheCyclesOfTDD; Fowler bliki; Beck |
| 3 | 03-test-design-quality.md | What makes a test good or bad (FIRST, AAA, naming, test smells, builders/object mothers)? | xunitpatterns.com; Fowler; test-smell literature |
| 4 | 04-test-doubles-isolation.md | Double taxonomy and when to use them; classical vs mockist; state vs interaction | martinfowler.com/bliki/TestDouble.html; mocksArentStubs; xunitpatterns.com |
| 5 | 05-levels-atdd-bdd.md | Unit/integration/acceptance, test pyramid, outside-in double-loop, BDD/ATDD | martinfowler.com/articles/practical-test-pyramid.html; dannorth.net; *GOOS* |
| 6 | 06-design-outcomes.md | Emergent design, testability, seams, legacy-code work | Feathers *WELC*; martinfowler.com/articles/designDead.html; Beck |
| 7 | 07-empirical-evidence.md | What the evidence shows for quality, defects, productivity; SLR disagreements | S0950584916300222; infsof.2025.107762; Microsoft Nagappan; s11219-011-9130-2 |
| 8 | 08-advanced-techniques.md | Property-based testing, mutation testing, coverage limits, contract/golden-master testing | fast-check.dev; mutation-testing literature; Fowler |
| 9 | 09-teaching-assessing-competency.md | How to teach and assess TDD competency for AI agents | Kent Beck augmented coding; arXiv 2505.09027; arXiv 2603.17973 |

## Method
- Prefer primary sources (books, original articles, peer-reviewed papers, official docs); quote exactly; link inline; record failed retrievals.
- Apply verify-deep-analysis notation in evidence files: SOURCE FACT (Rank 1), SOURCE CLAIM (Rank 2–6), AI INFERENCE, PLAUSIBLE NOT VERIFIED, UNKNOWN.
- Strictly language-agnostic: no Python/pytest specifics; xUnit-family concepts and paradigm-neutral examples only.
- Capture independent topics in parallel; reconcile conflicts (Is TDD Dead?, Ousterhout, SLR disagreement) rather than smoothing them.
- Final report: synthesis + agent-facing competency model + one deduplicated resource list; no raw evidence tags.

## Deliverables
- 00-research-plan.md (this file)
- 01..09 evidence files
- TDD-REPORT.md (synthesis + competency model + consolidated resources)
