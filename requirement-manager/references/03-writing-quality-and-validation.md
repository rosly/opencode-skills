# Requirements Writing, Quality, and Validation

**Evidence cut-off:** 2026-10-05. **Question:** How should requirements be written, reviewed, validated, tested, traced, and measured, and which anti-patterns matter?

This evidence file distinguishes **source evidence** (short exact quotations with inline links) from **derived guidance** (the synthesis and examples produced for this research). “Requirement” below means an individual requirement statement unless “set” or “specification” is stated.

## Findings

### 1. Current standards and guidance baseline

**Source evidence.** ISO identifies ISO/IEC/IEEE 29148:2018, edition 2, as the current published requirements-engineering standard. Its catalogue says, “This publication was last reviewed and confirmed in 2024. Therefore this version remains current,” while also saying it is “Expected to be replaced by ISO/IEC/IEEE DIS 29148 within the coming months” ([ISO catalogue](https://www.iso.org/standard/72089.html)). Its public abstract says the standard “specifies the required processes implemented in the engineering activities that result in requirements” and “specifies the required information items produced through the implementation of the requirements processes” ([ISO catalogue](https://www.iso.org/standard/72089.html)). The normative 92-page text was not publicly accessible in this research.

**Source evidence.** The current publicly downloadable IEEE Computer Society body of knowledge is SWEBOK Guide V4.0a. It states that each requirement should “be unambiguous (interpretable in only one way)” and “be testable (quantified), meaning that compliance or noncompliance can be clearly demonstrated”; the set should be “complete,” “concise,” “internally consistent,” “externally consistent,” and “feasible” ([SWEBOK V4.0a, Software Requirements §3.1, PDF pp. 1-8–1-9](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf)).

**Source evidence.** INCOSE’s official store describes Guide to Writing Requirements V4 as “a mature product” and dates it “V4, updated Jul 1 2023”; the full guide costs USD 25 for a non-member and USD 0 for a member ([INCOSE store](https://portal.incose.org/Web/iCore/Store/StoreLayouts/Item_Detail.aspx?Category=EBOOKS&iProductCode=GUIDEWRITEREQ)). The same page says a separate seven-page summary contains “definitions,” characteristics of well-formed statements and sets, rules, attributes, and cross-reference matrices. The publicly indexed summary identifies individual-statement characteristics including necessary, appropriate, unambiguous, complete, singular, feasible, verifiable, correct, and conforming ([INCOSE V4 summary-sheet search result URL](https://www.incose.org/docs/default-source/working-groups/requirements-wg/guidetowritingrequirements/incose_rwg_gtwr_v4_summary_sheet.pdf)). Direct retrieval of that summary failed with HTTP 403, so this report does not quote its body as directly inspected evidence.

**Derived conclusion.** Use ISO/IEC/IEEE 29148:2018 as the current normative baseline until its successor is published, but record the revision risk. Use SWEBOK and INCOSE as practical, non-normative elaboration. A project should name the exact baseline and version rather than saying only “follow best practices.”

### 2. Write requirements around observable obligation and context

**Source evidence.** SWEBOK says structured natural language “impose[s] constraints on how the requirements are expressed; the goal is to increase precision and conciseness.” Its actor-action example separates triggering event, actor, action, and condition/qualification ([SWEBOK V4.0a, §4.2, PDF p. 1-12](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf)). It also lists useful attributes: tag, rationale, source, dependencies, conflicts, acceptance criteria, priority, stability, supporting materials, and change history ([SWEBOK V4.0a, §4.5, PDF p. 1-15](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf)).

**Source evidence.** SWEBOK cautions that specification choices depend on risk, stakeholder involvement, “the degree of requirements-based testing expected,” and “extent of requirements tracing necessary” ([SWEBOK V4.0a, §4, PDF pp. 1-10–1-11](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf)). It therefore does not support one universal sentence template for every context.

**Derived guidance.** For each obligation, state: applicable trigger/precondition; responsible entity; required observable behavior or property; object/output; quantitative threshold and unit where the requirement is scalar; timing and operating conditions; and explicit exceptions. Keep rationale, source, priority, and verification method as attributes rather than prose inside the obligation. Use one obligation per hierarchical identifier so change, review, and verification status are independently controllable. Treat module and subgroup placement as part of identity and allocate a new identifier when either changes.

**Derived boundary.** “One sentence” is a useful heuristic, not proof of atomicity or testability. A short sentence can still contain several obligations; a longer structured statement can be singular. Split by independently decidable obligation, not punctuation alone.

### 3. Review and validate from multiple perspectives

**Source evidence.** SWEBOK defines validation as “gaining confidence that the requirements represent the stakeholders’ true needs as they are currently understood.” It asks whether all currently relevant requirements are present, whether any do not represent stakeholder needs, whether they are appropriately stated, understandable, consistent and complete, and whether documentation conforms to relevant standards ([SWEBOK V4.0a, §5, PDF p. 1-15](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf)).

**Source evidence.** For reviews, SWEBOK says reviewers look for “errors, omissions, invalid assumptions, lack of clarity and deviation from accepted practice.” It prefers multiple perspectives: customers/users assess accurate representation of needs; requirements specialists assess clarity and conformance; downstream engineers assess sufficiency for architecture, design, and construction. It also says, “Providing checklists, quality criteria or a ‘definition of done’ to the reviewers can guide them” ([SWEBOK V4.0a, §5.1, PDF pp. 1-15–1-16](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf)).

**Source evidence.** SWEBOK identifies three validation methods: “requirements reviews, simulation and execution, and prototyping” ([SWEBOK V4.0a, §5](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf)). Prototypes can expose assumptions, but “cosmetic issues or quality problems with the prototype can distract the reviewers’ attention from the core underlying functionality” ([SWEBOK V4.0a, §5.3, PDF p. 1-16](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf)).

**Derived guidance.** Separate two gates:

1. **Requirement verification:** Is the statement/set well formed, internally consistent, feasible, uniquely identified, conforming, and capable of objective verification?
2. **Requirement validation:** Does it express the right stakeholder need in the intended operational context?

Use role-specific review assignments and log disposition for every issue (accept, revise, reject, or explicitly defer with owner). Supplement document review with scenarios, simulation, executable models, or prototypes where stakeholders cannot reliably inspect abstractions. Do not let prototype appearance substitute for checking the underlying need.

### 4. Make test design part of requirements work

**Source evidence.** SWEBOK describes acceptance-test-driven development as agreement, before production design or construction, among software engineers, business-domain experts, and possibly test professionals on tests showing correct implementation ([SWEBOK V4.0a, §4.3, PDF pp. 1-12–1-13](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf)). It says ATDD test cases are “essentially precise, unambiguous statements of requirements,” but also warns that acceptance-criteria specification “does not inherently solve the incompleteness problem” ([SWEBOK V4.0a, §4.3, PDF pp. 1-13–1-14](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf)).

**Source evidence.** SWEBOK says acceptance testing’s “main goal is to verify that the SUT satisfies the requirements and the end-users’ expectations” and that defining acceptance tests before implementation is central to ATDD ([SWEBOK V4.0a, Software Testing §2.1.4, PDF p. 5-7](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf)). It further says precise, quantitative test objectives support “measurement and control of the test process” ([SWEBOK V4.0a, Software Testing §2.2, PDF p. 5-7](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf)).

**Derived guidance.** During review, require a reviewer to sketch at least one objective pass/fail observation and, where relevant, boundary, exception, and adverse-condition cases. Inability to do so is evidence of a missing threshold, undefined term, unavailable observation point, infeasible environment, or mixed obligation. It is not automatically evidence that the underlying stakeholder need is invalid. Acceptance examples complement—not replace—set-level completeness analysis.

### 5. Trace in both directions and control change

**Source evidence.** SWEBOK gives traceability two purposes: accounting for consistency between related work products and impact analysis. It asks whether each requirement has design elements intended to satisfy it and whether each design element has requirements that cause it to exist ([SWEBOK V4.0a, §7.3, PDF pp. 1-18–1-19](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf)). It says requirements can trace backward to source documentation and forward to design elements, requirements-based tests, and user-manual sections ([SWEBOK V4.0a, §7.3, PDF p. 1-19](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf)).

**Source evidence.** For change control, SWEBOK calls for a request mechanism, optional impact analysis, a decision authority, stakeholder notification, and tracking accepted changes to closure; stakeholders must understand that change affects schedule, resources, or scope ([SWEBOK V4.0a, §6.2, PDF p. 1-17](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf)).

**Derived guidance.** Maintain inspectable links from requirement to source/need and parent; to dependent requirements and risks; and forward to design realization and verification evidence. Keep implementation paths, code symbols, and test symbols in a separate impact or trace artifact rather than in normative requirement text. Before approving a change, follow links in both directions and assess impacted requirement text, design, implementation, verification, procedures, and user documentation. A link is not evidence of satisfaction: record link type and verify the linked artifact actually addresses the requirement.

### 6. Measure quality, but do not confuse proxies with truth

**Source evidence.** SWEBOK says functional-size measurement and story points can measure requirements volume, and that quality indicators can relate specification quality to cost, acceptance, performance, schedule, and reproducibility. It says indicators can be derived from the desirable properties used in requirements analysis ([SWEBOK V4.0a, §7.5, PDF p. 1-19](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf)).

**Source evidence.** The peer-reviewed systematic mapping study of 105 primary studies found that “empirical research on requirements quality focuses on improvement techniques, with very few primary studies addressing evidence-based definitions and evaluations of quality attributes.” It identified 12 attributes; “the most prominent in the field are ambiguity, completeness, consistency, and correctness” ([Montgomery et al., 2022](https://link.springer.com/article/10.1007/s00766-021-00367-z/fulltext.html)). The study also reports that only 9% (9/105) applied their work in an industrial context and that only 15 of 41 identified tools could be found online ([Montgomery et al., §§5.2–5.3](https://link.springer.com/article/10.1007/s00766-021-00367-z/fulltext.html)).

**Source evidence.** A railway-domain comparison evaluated four ambiguity tools against one expert’s labels on 180 industrial requirements. Two tools reached recall 0.85 and 0.98, while the best precision was 0.68; the authors conclude that high recall is possible with pattern detection but “increased precision is challenging” ([Bajceta et al., 2022, abstract and §§5–7](https://ceur-ws.org/Vol-3122/NLP4RE-paper-3.pdf)). They explicitly state that their dataset “might not be enough to evaluate the general usage” and that ambiguity assessment is subjective and usually benefits from multiple analysts ([Bajceta et al., §6](https://ceur-ws.org/Vol-3122/NLP4RE-paper-3.pdf)).

**Source evidence.** A 2024 arXiv preprint models natural-language requirement testability from nine smells, statement length, and domain. It defines testability using the ISO-derived phrase “extent to which an objective and feasible test can be designed to determine whether a requirement is met” ([Zakeri-Nasrabadi and Parsa, 2024, §1](https://arxiv.org/html/2403.17479)). On 985 selected English requirements it reports MAE 0.12 and MSE 0.03, and reports a 0.93 Spearman correlation with three experts on sampled requirements ([Zakeri-Nasrabadi and Parsa, abstract and §4.5.3](https://arxiv.org/html/2403.17479)). The authors nevertheless say vague pronouns and non-verifiable terms are harder to detect, and limit external validity to English and ten application domains ([Zakeri-Nasrabadi and Parsa, §§4.3, 5.3](https://arxiv.org/html/2403.17479)).

**Derived conclusion.** Use automated smell detection as triage, never as acceptance authority. Report precision and recall against a domain-relevant, independently reviewed truth set before setting a policy threshold. Count-based metrics should trigger investigation, not reward cosmetic rewriting.

## Quality model

The following is a **derived operational model**, synthesized from the cited evidence; it is not quoted from or claimed to conform fully to ISO/IEC/IEEE 29148 or INCOSE GtWR.

### Individual requirement

| Dimension | Review question | Objective evidence sought |
|---|---|---|
| Necessary/correct | Does an approved need, source, constraint, or higher-level requirement justify it? Does it state that source accurately? | Backward trace plus stakeholder/domain-owner confirmation |
| Appropriate | Is the statement at the right abstraction level and free of unnecessary design prescription? | Allocation/context and rationale |
| Singular/atomic | Can the obligation be approved, changed, implemented, and verified independently? | One independently decidable obligation per identifier |
| Unambiguous/understandable | Do intended readers assign one meaning to actor, terms, quantities, references, and scope? | Defined vocabulary; resolved pronouns/references; multidisciplinary review |
| Complete | Does the statement include enough trigger, behavior/property, object, conditions, bounds, units, and exceptions to stand on its own for its purpose? | Filled semantic fields and no reliance on unstated assumptions |
| Feasible | Can it be realized within technical, cost, schedule, legal, ethical, safety, and operational constraints? | Named feasibility analysis or expert assessment |
| Verifiable/testable | Can an objective and feasible method distinguish compliance from noncompliance? | Verification method, observable result, threshold/tolerance, environment, acceptance criteria |
| Conforming | Does it follow the project’s approved syntax, vocabulary, identifiers, units, and metadata rules? | Lint/style check and human review |
| Traceable/manageable | Can origin, realization, verification, status, owner, version, and change impact be followed? | Typed bidirectional links and change history |

### Requirement set/specification

| Dimension | Set-level question | Suggested evidence |
|---|---|---|
| Complete coverage | Are all in-scope capabilities, quality constraints, interfaces, states, failure/exception conditions, security needs, regulations, and boundaries covered? | Coverage model, scenario/state/interface matrix, source-to-child trace audit |
| Consistent | Do statements conflict internally or with source material, models, standards, or constraints? | Cross-requirement analysis and conflict log |
| Nonredundant/minimal | Are duplicate, unnecessary, obsolete, or out-of-scope obligations removed without losing needed coverage? | Duplicate/orphan review and disposition |
| Feasible as a set | Are individually feasible requirements jointly achievable within shared budgets and constraints? | Budgets, trade studies, architecture assessment |
| Structured and navigable | Can each consumer find the information and relationships needed? | Audience review, hierarchy, subgroup-aligned IDs, glossary, views |
| Validated | Do authorized stakeholders agree the set represents current needs in operational scenarios? | Recorded review/prototype/simulation outcomes and approvals |

## Practical checks

The checklist below is **derived guidance**. Tailor its rigor and required evidence to risk; SWEBOK explicitly makes specification choices context-dependent.

### Authoring check

- Give the requirement a unique hierarchical identifier aligned with its owning module and subgroup. Allocate a new identifier after relocation; otherwise retain the identifier for changes that preserve both semantics and placement.
- Identify its source/parent and rationale outside the normative sentence.
- State one independently decidable obligation, with an explicit responsible entity.
- State trigger/preconditions, action or property, object/output, applicable operating conditions, and exceptions.
- Quantify thresholds, tolerances, time windows, probability/confidence basis, and units where meaningful; define measurement method if different methods could change the result.
- Replace subjective or unbounded words—such as *user-friendly*, *adequate*, *quickly*, *normal*, *as appropriate*, *where possible*, *may*, or *can*—with domain-defined criteria, or explicitly define the term.
- Resolve pronouns, coordination, references, scope of qualifiers, and domain-specific polysemy.
- Keep implementation choices out unless the source genuinely imposes a constraint.
- Attach priority, owner, status, stability, dependencies, acceptance criteria, verification method, and change history as metadata when the project needs them.

### Review and validation check

- Have the need owner/user check necessity, correctness, operational fit, and missing scenarios.
- Have a requirements specialist check singularity, clarity, completeness, conformance, and set consistency.
- Have architecture/development/operations/security/safety specialists, as applicable, check feasibility and sufficiency.
- Have a tester or verifier derive pass/fail observations and boundary/exception cases without relying on private author knowledge.
- Walk representative normal, boundary, degraded, misuse, and failure scenarios; use simulation/execution/prototypes when document inspection is inadequate.
- Record every defect, question, decision, owner, and disposition; re-review changed requirements and impacted links.

### Trace and change check

- Audit backward coverage: every requirement has a valid need/source/parent, or a documented derivation rationale.
- Audit forward coverage: every applicable requirement has realization and verification links; every design/test element has a requirement or documented non-requirement rationale.
- Check semantic link validity, not only presence.
- For every proposed change, inspect linked parents/children, dependencies, architecture/design/code, tests, hazards/risks, procedures, documentation, cost, and schedule.
- Retain versioned decisions and verification evidence so status can be reconstructed.

### Test-readiness check

- Name the verification method: test, analysis, inspection, demonstration, or an approved combination.
- Define the item under test, initial state, inputs/stimulus, environment/configuration, observation point, expected result, threshold/tolerance, and repeatability/statistical rule where applicable.
- Include boundaries and exceptions; acceptance examples alone do not establish complete requirement coverage.
- Ensure required observations and environments are practically available and proportionate to risk.

### Measurement dashboard

These are **derived candidate measures**, not evidence-backed universal thresholds. Establish baselines, denominators, ownership, and interpretation before use.

| Measure | Definition | Guardrail |
|---|---|---|
| Review first-pass yield | Requirements passing the agreed checklist on first review / requirements reviewed | Never compare teams without controlling for requirement type, maturity, and risk |
| Defect density by class | Review findings by ambiguity, omission, conflict, infeasibility, unverifiability, trace defect, etc. / requirements or functional size | A falling count can mean weaker review; pair with escaped defects |
| Escaped requirement-defect rate | Requirement-origin defects found after the agreed gate / requirements baselined | Root-cause classification requires independent review |
| Backward trace coverage | Requirements with validated source/parent links / applicable requirements | Link existence alone is insufficient |
| Forward verification coverage | Requirements with approved verification method and linked evidence / applicable requirements | Distinguish planned tests from passed evidence |
| Orphan realization rate | Design/code/test elements lacking justified requirement links / sampled elements | Some infrastructure work may have legitimate non-feature rationale |
| Volatility | Added, changed, and deleted requirements per baseline interval, stratified by reason | Change is not inherently bad; late discovery and uncontrolled change are the concern |
| Review closure time | Median time from finding to accepted disposition | Do not incentivize premature closure |
| Smell-tool precision/recall | True positives among flags; true positives among independently labeled defects | Revalidate by domain/language/version; do not report “accuracy” alone on imbalanced data |
| Verification outcome | Passed, failed, blocked, waived, and not-run requirements by risk/priority | Never hide blocked/waived items inside “covered” |

## Derived examples and anti-patterns

All examples in this section are **derived examples created for this report**, not quotations from the sources. Whether a requirement is correct or feasible still depends on its real domain and approved source.

### Vague quality and missing measurement

- **Bad derived example:** “The search page shall load quickly and be user-friendly.”
- **Why it is bad:** two obligations; subjective and unbounded terms; no load, environment, population, percentile, or usability method.
- **Improved derived example:** “For catalogues containing up to 1,000,000 indexed products, the Search Service shall return the first results page within 800 ms for at least 95% of requests measured over each 15-minute interval under the workload profile PERF-WP-03.”
- **Remaining decision:** usability requires a separate, stakeholder-approved measure; do not invent one from prose.

### Optionality and loopholes

- **Bad derived example:** “The controller may log diagnostic information where appropriate.”
- **Why it is bad:** optional obligation; undefined decision authority and conditions; unverifiable extent.
- **Improved derived example:** “When the controller rejects a command, the controller shall append an event containing the command identifier, rejection code, and UTC timestamp to the diagnostic log before acknowledging the rejection.”

### Ambiguous pronoun/reference

- **Bad derived example:** “When the gateway sends the report to the monitor, it shall archive it.”
- **Why it is bad:** both occurrences of *it* have competing referents.
- **Improved derived example:** “After the Gateway sends a report to the Monitor, the Gateway shall archive that report.”

### Compound requirement

- **Bad derived example:** “The service shall validate the token and create the account and email the customer.”
- **Why it is bad:** three independently failing, changing, and verifiable obligations under one identifier.
- **Improved derived examples:** “REQ-ACCOUNT-1.1.1: Before accepting an account-creation request, the Account Service shall validate the request’s authorization token.” “REQ-ACCOUNT-1.1.2: After `REQ-ACCOUNT-1.1.1` succeeds and the request data passes validation, the Account Service shall create one account.” “REQ-ACCOUNT-1.1.3: After `REQ-ACCOUNT-1.1.2` succeeds, the Notification Service shall send the account-created notice to the customer email address.”

### Unbounded comparative

- **Bad derived example:** “Version 2 shall use less memory than Version 1.”
- **Why it is bad:** no configuration, workload, statistic, observation interval, or target; any tiny reduction could pass.
- **Improved derived example:** “During workload MEM-WP-02 on reference configuration RC-4, Version 2 shall keep peak resident memory at or below 400 MiB over a 30-minute run.”

### Negative-only statement

- **Bad derived example:** “The application shall not lose messages.”
- **Why it is bad:** absolute, unspecified scope and failure model, and no observable recovery semantics.
- **Improved derived example:** “After any single process restart during workload MSG-WP-01, the Message Service shall deliver every acknowledged message exactly once within 60 seconds of process availability.”
- **Caution:** a prohibition can be legitimate, especially for safety/security. The anti-pattern is an underspecified negative, not grammatical negation itself.

### Premature design disguised as need

- **Bad derived example:** “The system shall use PostgreSQL to retain audit events.”
- **Why it may be bad:** it prescribes a solution without showing that the technology itself is an approved constraint.
- **Improved derived example if no technology constraint exists:** “The Audit Service shall retain each audit event for seven years and return events by subject identifier and UTC time range.”
- **Boundary:** if regulation, enterprise architecture, licensing, or interoperability genuinely mandates PostgreSQL, preserve the constraint and trace it to that source.

### Acceptance example mistaken for completeness

- **Bad derived example:** “Given a balance of $500, when $100 is withdrawn, then the balance is $400.”
- **Why it is bad as the entire requirement set:** it covers one happy-path example but says nothing about insufficient funds, limits, concurrent withdrawals, currency precision, unavailable cash, or failure recovery.
- **Improved derived approach:** retain the example as one acceptance case, then model relevant partitions, boundaries, states, exceptions, and invariants and link each resulting criterion to the requirement.

### Traceability theatre

- **Bad derived example:** A dashboard reports 100% trace coverage because every requirement links to a generic “System Design” document and one end-to-end test.
- **Why it is bad:** syntactic links do not show that each requirement is realized or objectively verified.
- **Improved derived approach:** type links, audit semantic relevance on a risk-based sample, expose many-to-many coverage, and distinguish planned verification from executed passing evidence.

### Automated smell score used as a gate

- **Bad derived example:** Reject every requirement containing *may*, *and*, a passive construction, or more than 25 words.
- **Why it is bad:** lexical flags are context-sensitive; the cited railway evaluation shows high recall can coexist with low precision, and the empirical evidence does not establish universal thresholds.
- **Improved derived approach:** flag candidates, show the exact text and rule, let a domain-aware reviewer decide, capture dispositions, and periodically estimate precision/recall against an independently labeled sample.

## Evidence limitations

- The public ISO page establishes scope, status, and revision state, but the normative ISO/IEC/IEEE 29148:2018 body was paywalled. No detailed clause-level claim in this file is attributed to that standard.
- SWEBOK V4.0a is authoritative professional guidance and directly inspectable, but it synthesizes other sources rather than reporting controlled evidence for every recommendation.
- INCOSE GtWR V4’s full text was not publicly accessible to a non-member without purchase. The seven-page summary was indexed as free/public but returned HTTP 403 during direct retrieval; its search snippet informed discovery only, not detailed quotations.
- Montgomery et al. is a peer-reviewed systematic mapping study, but its corpus ended on 2020-03-27 and intentionally excluded standards, books, and non-empirical work. It maps what has been studied, not which universal practice is proven best.
- Bajceta et al. is a workshop comparison with 180 railway requirements and one expert ground truth. The authors reject broad generalization; its numerical results should not be transferred as expected tool performance in another domain.
- Zakeri-Nasrabadi and Parsa is arXiv v1 (a preprint). Its model embeds subjective/domain factors; the selected 985 English requirements were retained after consensus and difficult disagreements were removed, which can make deployment performance harder to infer. The authors themselves limit external validity by language, domains, and smell catalogue.
- No source inspected establishes universal numeric acceptance thresholds for statement length, review defect density, trace coverage, or smell counts. Thresholds in a local quality gate require project-specific validation.

## Retrieval log

| Source | Retrieval result on 2026-10-05 |
|---|---|
| [ISO/IEC/IEEE 29148:2018 catalogue](https://www.iso.org/standard/72089.html) | Retrieved public HTML: abstract, current status, confirmation in 2024, revision stage, and draft successor. Full standard listed at CHF 227 and not inspected. |
| [SWEBOK Guide V4 PDF](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf) | Retrieved and directly text-extracted. PDF identifies itself as SWEBOK Guide V4.0a. |
| [Montgomery et al., Springer article](https://link.springer.com/article/10.1007/s00766-021-00367-z) | Main fetch showed a script/load error; publisher full-text HTML was then retrieved directly from the `/fulltext.html` endpoint and inspected. Article is open access; Crossref records CC BY 4.0. |
| [Bajceta et al., CEUR PDF](https://ceur-ws.org/Vol-3122/NLP4RE-paper-3.pdf) | Retrieved and directly text-extracted. [Volume page](https://ceur-ws.org/Vol-3122/) confirms title, authors, venue, and CC BY 4.0. |
| [Zakeri-Nasrabadi and Parsa, arXiv HTML](https://arxiv.org/html/2403.17479) | Retrieved and inspected as arXiv:2403.17479v1, dated 2024-03-26, CC BY 4.0. |
| [INCOSE GtWR V4 store entry](https://portal.incose.org/Web/iCore/Store/StoreLayouts/Item_Detail.aspx?Category=EBOOKS&iProductCode=GUIDEWRITEREQ) | Retrieved. Full V4 guide dated 2023-07-01; non-member price USD 25, member price USD 0. |
| [INCOSE GtWR V4 summary sheet, legacy URL](https://www.incose.org/docs/default-source/working-groups/requirements-wg/guidetowritingrequirements/incose_rwg_gtwr_v4_summary_sheet.pdf) | Search-indexed as a seven-page June 2023 summary, but direct fetch and `curl` returned HTTP 403. |
| [INCOSE Requirements Working Group](https://www.incose.org/group/requirements-working-group) | Search result advertised “Guide to Writing Requirements (GtWR) – a practical application guide FREE DOWNLOAD”; direct fetch returned HTTP 403. This conflict with the store’s USD 25 non-member price remains unresolved. |
| [INCOSE GtWR V4 webinar](https://www.incose.org/resource/webinar-168-guide-to-writing-requirements-version-4) | Search-indexed with date 2023-10-25; direct page fetch returned HTTP 403. An indexed PDF URL was detectable, but direct byte retrieval returned HTTP 403. |

## Open questions

- When will ISO/IEC/IEEE DIS 29148 replace the confirmed 2018 edition, and which quality characteristics or process requirements will materially change?
- Is INCOSE’s seven-page V4 summary intentionally public, and what stable URL or access process resolves the current HTTP 403 response?
- Does the project need strict conformance to ISO/IEC/IEEE 29148, or only a tailored practice informed by it? Clause-level conformance cannot be assessed from the public abstract.
- Which requirement classes and risk levels need distinct templates, review roles, evidence, and quality thresholds?
- What domain-specific vocabulary, measurement procedures, operational profiles, and statistical acceptance rules must be defined before requirements can be objective?
- What is the project’s authoritative source-of-truth and link schema for need → requirement → design → implementation → verification evidence?
- Which local labeled corpus and reviewer protocol will be used to validate any automated smell checker, and what precision/recall trade-off is acceptable for triage?
- Which set-level completeness model—scenarios, states, interfaces, hazards, quality-attribute scenarios, regulation clauses, or a combination—fits the system and its assurance obligations?
