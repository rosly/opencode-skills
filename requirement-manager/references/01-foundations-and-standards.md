# Software Requirements: Foundations and Standards

Retrieved: 2026-10-05. Current-state anchor: 2026-10-05. Scope: the meaning of a software requirement, the work included in requirements engineering, and the standards/body-of-knowledge baseline. This is an evidence file, not a synthesis report.

## Findings

### What a software requirement is

**Source evidence**

- SWEBOK V4.0a gives the shortest useful definition: “a software requirement is a property that must be exhibited to solve a real-world problem” ([SWEBOK V4.0a, PDF p. 45 / printed p. 1-3](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf)).
- Its fuller formal definition includes “a condition or capability needed by a user to solve a problem or achieve an objective” and one “that must be met or possessed by a system or system component to satisfy a contract, standard, specification or other formally imposed document” ([SWEBOK V4.0a, PDF p. 44 / printed p. 1-2](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf)). SWEBOK attributes this definition to ISO/IEC/IEEE 24765:2017.
- The concept covers both product and project constraints. “Software product requirements specify the software’s expected form, fit or function,” whereas project requirements “constrain the project that constructs the software” ([SWEBOK V4.0a, PDF p. 45 / printed p. 1-3](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf)).
- Requirement status is relative to system level: an architecture choice may be a design decision for overall-project stakeholders but “a requirement for the sub-teams” implementing it ([SWEBOK V4.0a, PDF p. 48 / printed p. 1-6](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf)).
- Requirements are not restricted to stakeholder utterances: SWEBOK lists “documentation,” “other systems,” “organizational policies and processes,” and the “computing environment” as non-person sources ([SWEBOK V4.0a, PDF pp. 49–50 / printed pp. 1-7–1-8](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf)).

**Inference**

- A requirement is not synonymous with a feature request or a requirements document. It is a needed or imposed property, condition, capability, or constraint; its documented statement is a representation of that underlying requirement.
- Whether a statement is a requirement or a design decision depends partly on the boundary and audience under consideration. Traceability should therefore retain the source, level, and rationale rather than classify statements only by wording.

### What belongs to requirements engineering

**Source evidence**

- ISO/IEC/IEEE 29148:2018 covers “the engineering activities that result in requirements for systems and software products (including services) throughout the life cycle,” including required processes, resulting information items, required content, and format guidance ([ISO catalogue abstract](https://www.iso.org/standard/72089.html)).
- SWEBOK says requirements engineering is “the systematic handling of requirements” and defines the Software Requirements knowledge area as “developing software requirements and managing those requirements over the software’s service life” ([SWEBOK V4.0a, PDF p. 44 / printed p. 1-2](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf)).
- SWEBOK divides the work into requirements development—“reaching an agreement on what software is to be constructed”—and requirements management—“maintaining that agreement over time” ([SWEBOK V4.0a, PDF p. 48 / printed p. 1-6](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf)).
- The development activities shown are elicitation, analysis, specification, and validation ([SWEBOK V4.0a, Figure 1.3, PDF p. 48 / printed p. 1-6](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf)). Their stated purposes are:
  - elicitation: “to surface candidate requirements” ([PDF p. 48 / printed p. 1-6](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf));
  - analysis: to understand “the meaning and implications of candidate requirements” individually and as a set ([PDF p. 50 / printed p. 1-8](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf));
  - specification: “recording the requirements so they can be both remembered and communicated” ([PDF p. 52 / printed p. 1-10](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf));
  - validation: gaining confidence that requirements “represent the stakeholders’ true needs” ([PDF p. 57 / printed p. 1-15](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf)).
- SWEBOK places scrubbing, change control, and scope matching under requirements management ([SWEBOK V4.0a, Figure 1.3 and section 6, PDF pp. 48, 58–59 / printed pp. 1-6, 1-16–1-17](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf)). It separately treats iterative work, prioritization, tracing, stability/volatility, measurement, process quality/improvement, and requirements tools as practical considerations ([SWEBOK V4.0a, chapter contents and topic breakdown, PDF pp. 8–9, 46–47](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf)).
- Requirements work is life-cycle-spanning rather than necessarily a front-end phase: it is “initiated at a project’s beginning” and is often refined over the software’s “entire service life” ([SWEBOK V4.0a, PDF p. 44 / printed p. 1-2](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf)).

**Inference**

- The defensible minimum scope of requirements engineering is elicitation, analysis, specification, validation, and continuing management. Traceability, prioritization, change control, scope alignment, quality assessment, and tool support are part of or support that work; they are not optional synonyms for writing a specification.
- The baseline is methodology-neutral. Waterfall may schedule much requirements work as a phase, while iterative/agile work refines it incrementally; neither changes the underlying responsibilities.

### Standards and body-of-knowledge baseline

**Source evidence**

- **Requirements-engineering standard:** ISO/IEC/IEEE 29148:2018, Edition 2, is the published International Standard devoted to life-cycle requirements engineering. ISO says it was “last reviewed and confirmed in 2024” and “remains current” ([ISO catalogue](https://www.iso.org/standard/72089.html)).
- **Vocabulary:** ISO/IEC/IEEE 24765:2017 provides “a common vocabulary applicable to all systems and software engineering work”; ISO says it was confirmed in 2026 and remains current ([ISO catalogue](https://www.iso.org/standard/71952.html)). SWEBOK uses it for the formal requirement definition ([SWEBOK V4.0a, reference 28, PDF p. 67 / printed p. 1-24](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf)).
- **Software life-cycle framework:** ISO/IEC/IEEE 12207:2026 establishes “a common framework for software life cycle processes” and includes processes, activities, and tasks across acquisition, supply, development, operation, maintenance, and disposal ([ISO catalogue](https://www.iso.org/standard/90219.html)). ISO lists it as published in April 2026 and shows 12207:2017 as withdrawn.
- **Body of knowledge:** IEEE Computer Society identifies “SWEBOK V4.0a” as “the newest edition” ([IEEE CS landing page](https://www.computer.org/education/bodies-of-knowledge/software-engineering/v4)); the PDF itself says “Released August 2026” ([SWEBOK V4.0a, cover](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf)). Its Software Requirements KA supplies the practice taxonomy and explanatory baseline rather than conformance requirements.
- SWEBOK’s own standards map lists the Software Requirements KA’s cited standards as “24765, 12207, ISO/IEC 25010, 29148” ([SWEBOK V4.0a, Table B.2, PDF p. 402 / printed p. B-10](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf)).
- SWEBOK describes itself as a “foundational document” and notes that only its 2004 and 2014 versions were recognized as ISO/IEC TR 19759:2005 and ISO/IEC TR 19759:2015, respectively ([SWEBOK V4.0a, PDF p. 390 / printed p. A-2](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf)).

**Inference**

- For work dated 2026-10-05, the baseline stack is: 24765:2017 for shared terminology; 12207:2026 for the encompassing software life-cycle process framework; 29148:2018 for requirements-engineering processes and information items; and SWEBOK V4.0a for generally accepted knowledge, activities, techniques, and context. ISO/IEC 25010 belongs when requirements concern system/software product quality models, but its current revision was not independently investigated in this topic.
- Normative authority and body-of-knowledge guidance should not be conflated: 29148/12207/24765 are published standards; SWEBOK is an IEEE Computer Society guide. V4.0a is not shown by the inspected sources to be a replacement ISO/IEC TR 19759 edition.

## Version/status reconciliation

| Source | Status on 2026-10-05 | Reconciliation / caveat |
|---|---|---|
| ISO/IEC/IEEE 29148:2018 | Published, Edition 2; current; stage 90.92 (“to be revised”) | It remains the current published normative requirements-engineering standard until a successor is published. |
| ISO/IEC/IEEE DIS 29148, Edition 3 | Under development; enquiry stage 40.20; ballot initiated 2026-09-14 | ISO says it “will replace” 2018, but a DIS is not yet the published International Standard. Its catalogue abstract is materially the same as 2018’s abstract; changes in the inaccessible full draft were not assessed. |
| SWEBOK V4.0a | IEEE landing page calls it newest; PDF says released August 2026 | The landing page simultaneously says it is “available for public review and feedback.” That wording conflicts with the PDF’s “Released” label; treat V4.0a as the newest published/downloadable guide but record editorial/public-review status as ambiguous. |
| SWEBOK V4.0a standards appendix | Released August 2026 but cites ISO/IEC/IEEE 12207:2017 | This reference is stale as of the research date: ISO shows 12207:2026 published and 12207:2017 withdrawn. Use 12207:2026 for current baseline status; do not assume SWEBOK’s process mapping has been updated to the 2026 edition. |
| ISO/IEC/IEEE 24765:2017 | Published, Edition 2; confirmed 2026; current | Its lifecycle history also records a 2025 “to be revised” event and a deleted committee draft, but ISO’s current headline and latest dated event say confirmed on 2026-09-20. |
| Prior ISO-recognized SWEBOK editions | ISO/IEC TR 19759:2005 and ISO/IEC TR 19759:2015 | These establish historical recognition, not that SWEBOK V4.0a itself is an ISO technical report. Using TR 19759:2015 as the latest ISO-recognized SWEBOK would be standards-current but body-of-knowledge-stale. |

## Retrieval log

| URL | Result |
|---|---|
| https://www.iso.org/standard/72089.html | Retrieved 2026-10-05. Official catalogue page, abstract, status, lifecycle, and successor link inspected. Full 92-page standard is paywalled/not retrieved. |
| https://www.iso.org/standard/94091.html | Retrieved 2026-10-05. Official DIS catalogue page, abstract, status, and lifecycle inspected. Full 101-page draft is paywalled/not retrieved. |
| https://www.computer.org/education/bodies-of-knowledge/software-engineering/v4 | Retrieved 2026-10-05. Official landing page inspected; it contains little beyond newest-edition/public-review wording. |
| https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf | Direct text fetch failed because the retrieval tool does not support `application/pdf`; binary download then succeeded (6,015,672 bytes; SHA-256 `0c9db4da0b2425c58cf778b99131eb31bb6c188e98b67163a549a1366d96e511`). Text was locally extracted and relevant pages inspected. PDF reports V4.0a, released August 2026; server `Last-Modified` was 2026-08-04. Extraction emitted missing-font warnings, so quotations were limited to passages whose text was coherent. |
| https://www.iso.org/standard/71952.html | Retrieved 2026-10-05 as a needed authoritative status check for SWEBOK’s definition source, ISO/IEC/IEEE 24765:2017. Full standard not retrieved. |
| https://www.iso.org/standard/90219.html | Retrieved 2026-10-05 as a needed authoritative status check because SWEBOK cites superseded 12207:2017. Full ISO/IEC/IEEE 12207:2026 standard not retrieved. |

## Open questions

- What substantive changes does DIS 29148 Edition 3 make relative to 29148:2018? The catalogue abstracts do not expose them, and the draft text was not available for inspection.
- Is IEEE’s phrase “available for public review and feedback” stale landing-page copy, or does V4.0a retain a formal review/provisional status despite the PDF’s “Released August 2026” label?
- Will SWEBOK V4.0a be submitted or recognized as a newer ISO/IEC TR 19759 edition? No inspected source establishes that.
- How do the requirements processes and mappings change under ISO/IEC/IEEE 12207:2026 compared with the withdrawn 2017 edition cited by SWEBOK V4.0a?
- Which revision of ISO/IEC 25010 should be used for a current quality-requirements baseline, and how should it be reconciled with SWEBOK V4.0a’s explicit citation to the 2011 edition? This was outside the required-source investigation.
