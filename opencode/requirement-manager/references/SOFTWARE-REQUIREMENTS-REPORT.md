# Software Requirements Engineering — Practical Research Report

Date: 2026-10-05. Scope: practical software requirements engineering, supported by current standards and empirical literature, with automotive software as a brief special case. This is not legal advice or a compliance handbook.

## Executive conclusion

Effective requirements engineering is not document production. It is the continuing work of discovering needs and constraints, analyzing implications and conflicts, recording an agreed and testable representation, validating that it expresses the right need, and maintaining that agreement as evidence and circumstances change. SWEBOK describes the core distinction as reaching agreement on what software is to be constructed and then “maintaining that agreement over time” ([SWEBOK V4.0a](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf)).

The practical minimum is therefore a managed chain:

**source or need → analyzed requirement → agreed acceptance evidence → realization → verification result → operational outcome**, with rationale, status, version, and change impact retained where risk justifies them.

No sentence template, user-story format, tool, or traceability matrix can replace that chain. Good wording matters, but correctness ultimately depends on stakeholder need, domain context, feasibility, system interactions, and objective evidence. Automated language checks are useful as triage only: empirical work shows that ambiguity detectors can obtain high recall while still producing many false positives ([Bajceta et al., 2022](https://ceur-ws.org/Vol-3122/NLP4RE-paper-3.pdf)).

Automotive software uses the same engineering fundamentals, but assurance and supply-chain constraints intensify them. Automotive SPICE 4.1 supplies an assessable process spine; ISO 26262 adds functional-safety obligations; ISO/SAE 21434 adds lifecycle cybersecurity risk management; and ReqIF supports cross-tool exchange. None substitutes for the others.

## Version anchor and authority

| Source | Current state on 2026-10-05 | Proper use |
|---|---|---|
| ISO/IEC/IEEE 29148:2018 | Current published requirements-engineering standard; confirmed in 2024, now marked “to be revised.” Edition 3 is a DIS under ballot, not yet a replacement ([ISO 29148:2018](https://www.iso.org/standard/72089.html); [DIS 29148](https://www.iso.org/standard/94091.html)). | Normative baseline for requirements processes and information items, subject to project tailoring and access to the full standard. |
| ISO/IEC/IEEE 12207:2026 | Published April 2026 and replaces 12207:2017 ([ISO 12207:2026](https://www.iso.org/standard/90219.html)). | Encompassing software lifecycle process framework. |
| SWEBOK V4.0a | IEEE calls it the newest edition; the downloadable PDF says “Released August 2026” ([IEEE landing page](https://www.computer.org/education/bodies-of-knowledge/software-engineering/v4); [PDF](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf)). | Current body-of-knowledge and practical taxonomy, not a conformance standard. |
| IREB Foundation Level syllabus 3.3.0 | Current retrievable English syllabus dated 1 April 2026 ([IREB syllabus](https://hub.ireb.org/media/pages/resources/cpre-foundation-level-syllabus/9c084b1cfd-1787039954/cpre_foundationlevel_syllabus_en_v.3.3.0.pdf)). | Practitioner education and complementary methods. |
| Automotive SPICE 4.1 | Released August 2026; VDA now lists 4.0 as legacy ([VDA publications](https://vda-qmc.de/en/automotive-spice/automotive-spice-veroeffentlichungen/)). | Automotive process reference/assessment model. |
| ISO 26262:2018, especially Part 6 | Current published Edition 2; Part 6 was confirmed in 2024 and is under revision ([ISO 26262-6](https://www.iso.org/standard/68388.html)). | Functional-safety lifecycle and software-safety requirements. |
| ISO/SAE 21434:2021 | Current published Edition 1; marked for revision on 2 October 2026 ([ISO/SAE 21434](https://www.iso.org/standard/70918.html)). | Automotive cybersecurity engineering and risk management. |
| OMG ReqIF 1.2 | Current formal version, July 2016 ([OMG ReqIF](https://www.omg.org/spec/ReqIF/1.2/)). | Requirements interchange, not engineering or assurance. |

Two staleness cautions matter. SWEBOK V4.0a still maps to ISO/IEC/IEEE 12207:2017 even though ISO has replaced it with 12207:2026. Also, some VDA overview text still names Automotive SPICE 4.0, but the official publications page and released 4.1 PDF establish 4.1 as current. The dated primary publication takes precedence over stale navigation copy.

## Working model

A software requirement is a needed or imposed property, capability, condition, or constraint, not merely a feature request. SWEBOK’s compact definition is “a property that must be exhibited to solve a real-world problem” ([SWEBOK V4.0a, Software Requirements](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf)). Sources include stakeholders, laws and standards, contracts, organizational policies, existing systems, operational evidence, interfaces, and the computing environment.

Requirements engineering has five durable responsibilities:

1. **Elicit:** surface candidate needs, constraints, assumptions, and sources.
2. **Analyze:** determine meaning, implications, dependencies, conflicts, feasibility, and priority.
3. **Specify:** record requirements in forms their consumers can understand and use.
4. **Validate:** gain confidence that they represent the stakeholders’ true needs.
5. **Manage:** preserve agreement through traceability, status, versions, scope decisions, and controlled change.

ISO/IEC/IEEE 29148 applies these activities throughout the lifecycle and across methodologies ([ISO abstract](https://www.iso.org/standard/72089.html)). SWEBOK similarly says requirements are often refined over the software’s entire service life rather than completed in one front-end phase ([SWEBOK V4.0a](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf)).

### Smallest useful artifact set

The following is a practical synthesis, not a universally mandated document set:

- **Context and scope:** problem/outcome, boundary, external interfaces, assumptions, constraints, and decision owner.
- **Source and stakeholder map:** relevant people plus documentary, operational, regulatory, and technical sources.
- **Managed requirement items:** hierarchical identifier aligned with the owning module and requirement subgroup, obligation, source/parent, rationale, owner, priority, status, dependencies, acceptance or verification information, and change history only where each attribute serves a real decision or assurance need. Relocation to another module or subgroup requires a new identifier and a lifecycle mapping.
- **Shared vocabulary and models:** glossary plus scenarios, state/interface models, quality-attribute scenarios, or prototypes where prose is insufficient.
- **Decision and conflict record:** alternatives, affected parties, resolution, rationale, and unresolved items maintained in design or decision material rather than in the active requirement set.
- **Trace and evidence view:** links needed to answer source legitimacy, coverage, verification, and impact questions.
- **Change record:** proposed change, impact, accountable decision, affected baselines, implementation, revalidation, and closure.

Keep the authoritative active requirement set in its requirements document. Supporting models, verification evidence, decision records, and impact traces may reside in their appropriate repositories, but they do not replace the normative requirements or introduce implementation symbols into requirement text.

## Practical lifecycle

This workflow is a synthesis of SWEBOK, IREB, and the empirical literature. It is intentionally iterative and tailorable; no source prescribes this exact sequence.

1. **Frame the problem and decisions.** Record desired outcomes, boundaries, interfaces, assumptions, constraints, regulatory obligations, and who decides. Define what evidence is sufficient for the next commitment horizon.
2. **Map sources and stakeholders.** Include users, customers, operations, support, testers, maintainers, security/safety specialists, regulators, existing systems, contracts, standards, defect data, and affected or underrepresented parties. IREB warns that missing a relevant source leads to incomplete understanding ([IREB syllabus 3.3.0](https://hub.ireb.org/media/pages/resources/cpre-foundation-level-syllabus/9c084b1cfd-1787039954/cpre_foundationlevel_syllabus_en_v.3.3.0.pdf)).
3. **Elicit candidates with complementary techniques.** Combine techniques suited to uncertainty and access, such as interviews plus observation, workshops plus prototypes, or artifact analysis plus scenarios. Preserve source, rationale, assumptions, and open questions in design or decision material; do not mistake elicitation output for approved requirements.
4. **Analyze and negotiate.** Separate need from proposed solution; inspect clarity, atomicity, feasibility, dependencies, conflicts, quality attributes, failure behavior, and testability. Conflicts belong with affected decision-makers, not unilateral engineering guesses ([SWEBOK V4.0a](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf)).
5. **Specify for consumer and risk.** Use the lightest representation that communicates reliably: structured prose, user stories, use cases, acceptance examples, state/interface models, or formal models. Add detail where distribution, longevity, contracts, safety, security, or verification demand it.
6. **Validate before commitment and repeatedly.** Combine stakeholder review with prototype, simulation, model execution, scenario walkthrough, or acceptance-test design where document inspection is insufficient. SWEBOK identifies reviews, simulation/execution, and prototyping as common validation methods ([SWEBOK V4.0a](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf)).
7. **Prioritize and match scope to capacity.** Balance value, necessity, risk, urgency, dependencies, cost, and cost of delay without false numeric precision. At scale, coordinate system-level dependencies instead of relying only on each team’s local ordering.
8. **Establish purposeful traceability.** First define which questions links must answer: origin, allocation, design/test coverage, regulatory evidence, cross-team dependency, or change impact. Maintain and audit the links needed for those questions; maximal linking is not automatically valuable.
9. **Commit, baseline, and control change.** Version durable items. Route changes through impact analysis proportionate to risk, accountable accept/reject/defer decisions, notification, reprioritization, implementation, revalidation, and closure.
10. **Measure outcomes and improve.** Compare delivered behavior and operational results with requirements and acceptance evidence. Examine escaped misunderstandings, churn, stakeholder latency, trace gaps, and blocked verification, then adapt the process.

A compact state model can be **candidate → analyzed → specified → validated → committed → implemented/verified → accepted or changed**. Backward movement is expected when evidence changes; unresolved issues remain visible in design or decision material rather than being silently converted into active requirements.

## Writing requirements that can be used

SWEBOK says an individual requirement should be unambiguous and testable, while the set should be complete, concise, consistent, and feasible ([SWEBOK V4.0a](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf)). These labels are useful review prompts, not mechanical proof of quality. A systematic mapping study of 105 empirical papers found that ambiguity, completeness, consistency, and correctness dominate research, but few studies provide evidence-based definitions and evaluations of quality attributes ([Montgomery et al., 2022](https://link.springer.com/article/10.1007/s00766-021-00367-z/fulltext.html)).

### Statement checklist

- State one independently decidable obligation per identifier.
- Name the responsible entity and required observable behavior or property.
- State trigger or preconditions, object/output, operating conditions, limits, and explicit exceptions where relevant.
- Quantify thresholds, tolerance, timing, workload, population/statistic, confidence basis, and units when the obligation is scalar.
- Define domain terms and resolve pronouns, references, qualifier scope, and words with context-dependent meanings.
- Replace subjective or unbounded terms such as *quickly*, *adequate*, *normal*, *where possible*, *may*, and *can*, unless the project explicitly defines them.
- Keep rationale, source, priority, status, and verification method as attributes rather than mixing them into the normative obligation.
- Avoid imposing design unless technology or architecture is genuinely a sourced constraint.
- Check whether an objective and feasible method can distinguish compliance from noncompliance.

One sentence is only a heuristic. Atomicity concerns independent approval, change, implementation, and verification—not punctuation. Likewise, acceptance examples sharpen meaning but do not prove set-level completeness.

### Derived examples

These examples illustrate the synthesis; they are not copied from a standard and are not automatically correct outside their assumed context.

**Vague and compound**

- Weak: “The search page shall load quickly and be user-friendly.”
- Improved performance obligation: “For catalogues containing up to 1,000,000 indexed products, the Search Service shall return the first results page within 800 ms for at least 95% of requests measured over each 15-minute interval under workload PERF-WP-03.”
- Remaining issue: usability needs its own stakeholder-approved measure.

**Optional and unbounded**

- Weak: “The controller may log diagnostic information where appropriate.”
- Improved: “When the Controller rejects a command, the Controller shall append the command identifier, rejection code, and UTC timestamp to the diagnostic log before acknowledging the rejection.”

**Ambiguous reference**

- Weak: “When the gateway sends the report to the monitor, it shall archive it.”
- Improved: “After the Gateway sends a report to the Monitor, the Gateway shall archive that report.”

**Premature design**

- Potentially weak: “The system shall use PostgreSQL to retain audit events.”
- Need-focused alternative: “The Audit Service shall retain each audit event for seven years and return events by subject identifier and UTC time range.”
- Boundary: preserve PostgreSQL when regulation, interoperability, licensing, or enterprise architecture actually imposes it, and trace that constraint to its source.

**Acceptance example mistaken for a complete requirement**

- Incomplete alone: “Given a balance of $500, when $100 is withdrawn, then the balance is $400.”
- Better use: retain it as one case, then cover relevant boundaries, concurrent actions, insufficient funds, precision, limits, and failure recovery.

## Review, validation, and test readiness

Separate two questions. **Requirement verification** asks whether the statement and set are well formed, consistent, feasible, conforming, and objectively verifiable. **Requirement validation** asks whether they express the right stakeholder needs in the intended context. SWEBOK defines validation as gaining confidence that requirements represent stakeholders’ true needs and recommends multiple reviewer perspectives ([SWEBOK V4.0a](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf)).

Use need owners to check necessity and operational fit; requirements specialists to check clarity and set quality; downstream architecture, development, operations, safety, and security specialists to check sufficiency and feasibility; and testers to derive observable pass/fail evidence. Walk normal, boundary, degraded, misuse, and failure scenarios. Record each issue, owner, decision, and disposition, then re-review affected requirements.

Before commitment, attempt to define the item under test, initial state, stimulus, environment/configuration, observation point, expected result, threshold/tolerance, and any repeatability or statistical rule. Failure to sketch an objective test often reveals a missing threshold, undefined term, unavailable observation point, mixed obligation, or infeasible environment; it does not automatically invalidate the underlying need.

## Traceability and change

SWEBOK identifies two central purposes for traceability: consistency/coverage across related work products and change-impact analysis. It describes backward traces to source material and forward traces to design, requirements-based tests, and user documentation ([SWEBOK V4.0a](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf)).

Practical trace paths can include:

- need/source/constraint → requirement;
- parent system requirement → derived software requirement;
- requirement ↔ architecture or design element;
- requirement → risk, hazard, or threat treatment;
- requirement → verification method, test, and result in a separate impact or trace artifact;
- requirement → operational procedure or user documentation;
- change → impacted artifacts, decisions, and re-verification evidence.

Links need types and semantic review. “100% traced” is meaningless if every requirement points to one generic design document or end-to-end test. Automotive SPICE makes the same distinction explicitly: “Traceability alone, e.g., the existence of links, does not necessarily mean that the information is consistent” ([Automotive SPICE 4.1, p. 45](https://vda-qmc.de/wp-content/uploads/2026/09/Automotive-SPICE-PAM-v41.pdf)).

For each change, inspect both directions: sources and parents, children and dependencies, design, implementation, verification, risks, procedures, documentation, release baselines, cost, and schedule. Keep implementation locations and symbols in the separate impact trace. Preserve superseded normative text in version control, remove it from the active set, and retain lifecycle disposition, successor, and reason in the requirements document.

## Measurement without metric theatre

Useful measures expose decisions and risk; they should not become targets for cosmetic compliance. Candidate measures include review first-pass yield, requirement-defect classes, escaped requirement defects, validated backward-trace coverage, verification-evidence coverage, orphan realization rate, volatility by reason, review closure time, and verification states such as passed, failed, blocked, waived, or not run.

No inspected source establishes universal thresholds for statement length, trace coverage, defect density, or language-smell counts. Local thresholds need baselines, denominators, context by requirement class/risk, and periodic validation. In particular:

- link presence is not semantic coverage;
- planned tests are not passed evidence;
- change volume is not inherently bad;
- fewer review findings can indicate weaker review;
- smell counts are triage signals, not correctness scores.

The railway-domain ambiguity study reported recall up to 0.98 but best precision of 0.68 across four tools and 180 industrial requirements ([Bajceta et al., 2022](https://ceur-ws.org/Vol-3122/NLP4RE-paper-3.pdf)). A newer testability model reports promising results on 985 selected English requirements, but its authors limit external validity by language and domain ([Zakeri-Nasrabadi and Parsa, 2024](https://arxiv.org/html/2403.17479)). Automated checking should therefore show the flagged text and rule, retain human disposition, and be calibrated on an independently reviewed local sample.

## Agile and iterative development

Agile changes cadence and commitment horizon, not the responsibilities of requirements engineering. Run the lifecycle continuously at several horizons: product outcomes and major constraints; release/system coordination; near-term backlog refinement; in-iteration acceptance; and operational feedback. SWEBOK V4.0a explicitly incorporates Agile and DevOps across its knowledge areas ([IEEE SWEBOK overview](https://www.computer.org/education/bodies-of-knowledge/software-engineering)).

Empirical evidence cautions against “agile means no requirements discipline.” A survey covering representatives from 92 organizations found free-text documentation common, traces between requirements and code often explicitly managed, and testing aligned with requirements; unclear requirements and communication flaws remained important problems ([Wagner et al., 2017](https://arxiv.org/pdf/1703.08360)). A systematic review identified both problems mitigated by agile requirements practices and new challenges, while calling for more evidence on non-functional requirements and self-organizing teams ([Inayat et al., 2015](https://doi.org/10.1016/j.chb.2014.10.046)).

Practical implications:

- Refine near-term requirements just in time, but keep system-level constraints, interfaces, quality attributes, and long-lived rationale visible.
- Make acceptance examples and tester participation part of refinement.
- Treat change as backlog work while retaining explicit impact analysis and authorization where safety, security, contracts, shared interfaces, or cross-team effects require them.
- Preserve “just enough” documentation according to risk, distribution, longevity, and assurance—not ideology.
- Coordinate priorities and completeness across teams; local product-owner ordering alone does not resolve system-level dependencies.
- Use retrospectives and operational evidence to improve requirements work itself.

## Automotive software as a special case

Automotive requirements differ mainly in assurance context rather than sentence grammar. The same requirement set may simultaneously participate in an OEM/supplier contract chain, system–software–hardware decomposition, functional-safety reasoning, cybersecurity risk treatment, product variants, long-lived configuration management, and regulated release evidence.

| Instrument | Primary question | Requirements impact | Boundary |
|---|---|---|---|
| Automotive SPICE 4.1 | Are selected engineering and support processes capable and evidenced? | SYS.1/SYS.2 and SWE.1 cover elicitation, analysis, structure, feasibility, consistency, and bidirectional traceability; supporting processes cover configuration and change ([PAM 4.1](https://vda-qmc.de/wp-content/uploads/2026/09/Automotive-SPICE-PAM-v41.pdf)). | Process assessment is not proof of product safety or cybersecurity. |
| ISO 26262:2018 | Are malfunction-related functional-safety risks addressed through the safety lifecycle? | Part 6 includes software-safety requirements, architecture, implementation, unit verification, integration/verification, and embedded-software testing ([ISO 26262-6](https://www.iso.org/standard/68388.html)). | It does not address nominal performance and does not replace cybersecurity engineering. |
| ISO/SAE 21434:2021 | Are vehicle E/E cybersecurity risks managed across the lifecycle? | Adds cybersecurity goals, requirements, treatment, and evidence from concept through operation, maintenance, and decommissioning ([ISO/SAE 21434](https://www.iso.org/standard/70918.html)). | It complements rather than replaces ISO 26262. |
| ReqIF 1.2 | Can requirement information move between organizations and tools? | Serializes identifiable objects, attributes, hierarchy, and relationships in a tool-neutral XML format ([ReqIF specification](https://www.omg.org/spec/ReqIF/1.2/PDF)). | Exchange does not establish correctness, consistency, coverage, or compliance. |

Typical interaction: safety analysis and cybersecurity risk analysis create or constrain requirements; system and software processes analyze, allocate, agree, trace, and verify them; configuration/change processes preserve controlled evidence across releases; ReqIF may exchange snapshots and links across OEM and supplier repositories. These instruments overlap at artifacts and lifecycle activities but answer different questions.

Automotive practice consequently needs explicit provenance and classification, semantically checked cross-level traces, release/baseline identity, change-impact analysis that reaches safety and cybersecurity evidence, and agreed ReqIF profiles. Schema-valid exchange is not necessarily lossless: partners still need attribute mappings, relation semantics, identifier rules, and round-trip acceptance tests.

## Evidence limitations and unresolved conflicts

- The full normative texts of ISO/IEC/IEEE 29148, ISO 26262, and ISO/SAE 21434 were not publicly available during this research. Detailed clause-level conformance claims cannot be made from catalogue abstracts; organizations seeking compliance need licensed standards and qualified interpretation.
- ISO/IEC/IEEE 29148:2018 remains current, but Edition 3 is already at DIS ballot. The public abstract does not reveal substantive changes, so this report does not project draft requirements onto the current edition.
- IEEE labels SWEBOK V4.0a the newest edition and its PDF says released August 2026, while the landing page also calls it available for public review and feedback. Its exact editorial status is ambiguous, though it is the newest directly available guide.
- SWEBOK V4.0a’s standards appendix cites withdrawn ISO/IEC/IEEE 12207:2017. This report uses published 12207:2026 for current lifecycle status but does not assume mappings written for 2017 are unchanged.
- INCOSE’s Guide for Writing Requirements V4 was identified, but its full text required purchase or membership and the indexed summary returned HTTP 403. No detailed INCOSE rule is presented as directly verified here.
- The empirical requirements-quality literature is uneven. The 105-study mapping found only 9% of included studies applied in an industrial context ([Montgomery et al., 2022](https://link.springer.com/article/10.1007/s00766-021-00367-z/fulltext.html)). Tool results from a language, domain, or curated dataset should not be generalized without local validation.
- Automotive SPICE 4.1 is current, but customer-specific assessment scope and target capability levels remain contractual or organizational decisions. Neither the PAM nor this report establishes a universal target.

## Open questions for later project-specific processing

- Which regulatory, contractual, safety, cybersecurity, and audit obligations apply to the target product?
- Which lifecycle and requirements standards require formal conformance, and which are guidance only?
- Who owns requirement decisions and resolves conflicts among value, feasibility, safety, security, schedule, and cost?
- What is the required completeness horizon: story, iteration, release, contract milestone, integration event, or full product lifecycle?
- Which requirement classes need different templates, reviewers, approvals, baselines, and evidence?
- Which traceability questions justify ongoing maintenance cost, and which links can be generated reliably?
- What domain vocabulary, operational profiles, measurement procedures, and statistical acceptance rules must be defined?
- What is the authoritative repository and link schema for need → requirement → realization → verification evidence?
- For automotive work, which requirements are safety-related, cybersecurity-related, both, or neither, and what customer-specific Automotive SPICE scope applies?
- Which ReqIF profile, attribute mappings, relation types, identifier rules, and round-trip tests have exchange partners agreed?
- What transition dates will contracts or customers impose when the new editions of ISO/IEC/IEEE 29148, ISO 26262, and ISO/SAE 21434 are eventually published?

## Resources

- [ISO/IEC/IEEE 29148:2018 catalogue](https://www.iso.org/standard/72089.html)
- [ISO/IEC/IEEE DIS 29148 catalogue](https://www.iso.org/standard/94091.html)
- [ISO/IEC/IEEE 12207:2026 catalogue](https://www.iso.org/standard/90219.html)
- [ISO/IEC/IEEE 24765:2017 catalogue](https://www.iso.org/standard/71952.html)
- [IEEE Computer Society SWEBOK overview](https://www.computer.org/education/bodies-of-knowledge/software-engineering)
- [IEEE Computer Society SWEBOK V4 download page](https://www.computer.org/education/bodies-of-knowledge/software-engineering/v4)
- [SWEBOK Guide V4.0a PDF](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf)
- [IREB CPRE Foundation Level syllabus 3.3.0](https://hub.ireb.org/media/pages/resources/cpre-foundation-level-syllabus/9c084b1cfd-1787039954/cpre_foundationlevel_syllabus_en_v.3.3.0.pdf)
- [INCOSE Guide for Writing Requirements V4 store entry](https://portal.incose.org/Web/iCore/Store/StoreLayouts/Item_Detail.aspx?Category=EBOOKS&iProductCode=GUIDEWRITEREQ)
- [Montgomery et al., empirical research on requirements quality](https://link.springer.com/article/10.1007/s00766-021-00367-z/fulltext.html)
- [Bajceta et al., NLP ambiguity-tool comparison](https://ceur-ws.org/Vol-3122/NLP4RE-paper-3.pdf)
- [Zakeri-Nasrabadi and Parsa, requirements-testability preprint](https://arxiv.org/html/2403.17479)
- [Inayat et al., systematic review of agile requirements engineering](https://doi.org/10.1016/j.chb.2014.10.046)
- [Wagner et al., agile requirements practice survey](https://arxiv.org/pdf/1703.08360)
- [Kasauli et al., large-scale agile requirements study](https://research.chalmers.se/publication/522021/file/522021_Fulltext.pdf)
- [Automotive SPICE official publications](https://vda-qmc.de/en/automotive-spice/automotive-spice-veroeffentlichungen/)
- [Automotive SPICE PAM 4.1 PDF](https://vda-qmc.de/wp-content/uploads/2026/09/Automotive-SPICE-PAM-v41.pdf)
- [ISO 26262-1:2018 catalogue](https://www.iso.org/standard/68383.html)
- [ISO 26262-6:2018 catalogue](https://www.iso.org/standard/68388.html)
- [ISO/SAE 21434:2021 catalogue](https://www.iso.org/standard/70918.html)
- [OMG ReqIF 1.2 landing page](https://www.omg.org/spec/ReqIF/1.2/)
- [OMG ReqIF 1.2 specification](https://www.omg.org/spec/ReqIF/1.2/PDF)
