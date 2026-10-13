# Software Requirements Engineering — Research Plan

Date: 2026-10-05

Current versions/revisions: ISO/IEC/IEEE 29148:2018 is the published requirements-engineering baseline but is under revision, with Edition 3 at DIS stage in 2026; SWEBOK Guide V4.0a is the current IEEE Computer Society body-of-knowledge release; Automotive SPICE 4.1 was released 2026-08-24; ISO 26262:2018 Edition 2 is published but marked for revision; ISO/SAE 21434:2021 Edition 1 is published; OMG ReqIF 1.2 is the current formal version.

Scope: Practical software requirements engineering, including foundations, lifecycle/process, elicitation, analysis, specification, quality, validation, traceability, change management, agile application, examples and anti-patterns. Automotive software is treated as a brief special-case standards map. This is not an implementation guide, a tool comparison, legal advice, or a compliance handbook.

## Initial-scan signals

- ISO/IEC/IEEE 29148:2018 remains the published baseline, but ISO records it as “to be revised” and lists Edition 3 as a Draft International Standard in 2026.
- SWEBOK V4.0a organizes software requirements around fundamentals, elicitation, analysis, specification, validation, management, practical considerations, and tools; it incorporates Agile and DevOps across knowledge areas.
- Automotive SPICE 4.1 is newer than the frequently cited 4.0 release and explicitly separates stakeholder, system, software, hardware, machine-learning, verification, and validation processes.
- Automotive requirements are additionally shaped by functional-safety and cybersecurity lifecycle obligations and supply-chain exchange/traceability needs.
- Empirical literature cautions that requirements-quality terminology and automated smell detection have uneven evidence; ambiguity, completeness, consistency, and correctness receive most research attention.

## Topics

| # | File | Core question | Likely authoritative sources |
|---|------|---------------|------------------------------|
| 1 | `01-foundations-and-standards.md` | What is a software requirement, what belongs to requirements engineering, and what current standards/body-of-knowledge sources establish the baseline? | ISO/IEC/IEEE 29148 pages and draft status; IEEE SWEBOK V4.0a; ISO/IEC/IEEE 12207 catalogue material |
| 2 | `02-practical-lifecycle.md` | What repeatable workflow should practitioners use from discovery through change, including agile application? | IEEE SWEBOK V4.0a; IREB materials where retrievable; peer-reviewed agile RE surveys and systematic reviews |
| 3 | `03-writing-quality-and-validation.md` | How should requirements be written, reviewed, validated, tested, traced, and measured, and what anti-patterns matter? | ISO/IEC/IEEE 29148 public material; SWEBOK V4.0a; INCOSE public guidance where retrievable; peer-reviewed requirements-quality and ambiguity studies |
| 4 | `04-automotive-special-case.md` | What makes automotive requirements distinct, and how do Automotive SPICE, ISO 26262, ISO/SAE 21434, and ReqIF interact? | Automotive SPICE 4.1 official PAM; ISO official catalogue pages; OMG ReqIF 1.2; UNECE material where relevant |

## Synthesis outline

1. Executive conclusion and version anchor
2. Working model of requirements engineering
3. Practical lifecycle and minimum viable artifact set
4. Writing and quality rules with examples
5. Validation, traceability, and change control
6. Agile and iterative use
7. Automotive special case and standards map
8. Evidence limitations, open questions, and consolidated resources

## Method

- Prefer primary sources, inspect actual pages or documents, quote exactly, link inline, and record failed retrievals.
- Label quotations as source evidence and derived statements as inference in topic files.
- Treat standards catalogue abstracts as limited evidence when full normative text is paywalled.
- Flag stale versions and do not silently project older guidance onto current revisions.
