# Automotive software requirements: standards map

Retrieved 2026-10-05. Scope: a brief map of why automotive software requirements are distinctive and how Automotive SPICE, ISO 26262, ISO/SAE 21434, and ReqIF interact. This is not implementation or compliance guidance.

## Findings

### Primary-source evidence

- **Automotive SPICE is a process-capability assessment model, not a product safety or cybersecurity standard.** Automotive SPICE 4.1 states that it “can be used as the basis for conducting an assessment of process capability” and describes a two-dimensional process/capability framework ([Automotive SPICE PAM 4.1, pp. 12–13](https://vda-qmc.de/wp-content/uploads/2026/09/Automotive-SPICE-PAM-v41.pdf)). Its requirements processes nevertheless demand concrete engineering evidence: SWE.1's purpose is “to establish a structured and analyzed set of software requirements consistent with the system requirements, and the system architecture,” and its outcomes require correctness/feasibility analysis plus bidirectional traceability to both ([Automotive SPICE PAM 4.1, p. 44](https://vda-qmc.de/wp-content/uploads/2026/09/Automotive-SPICE-PAM-v41.pdf)).

- **Automotive SPICE treats links as necessary but insufficient.** The 4.1 PAM says: “Traceability alone, e.g., the existence of links, does not necessarily mean that the information is consistent” ([Automotive SPICE PAM 4.1, p. 45](https://vda-qmc.de/wp-content/uploads/2026/09/Automotive-SPICE-PAM-v41.pdf)). It also requires configuration integrity and controlled change: SUP.8's purpose is “to establish and maintain the integrity of relevant configuration items and baselines,” while SUP.10 requires changes to be recorded, analyzed, approved, implemented, and traced to affected work products ([Automotive SPICE PAM 4.1, pp. 81, 85–86](https://vda-qmc.de/wp-content/uploads/2026/09/Automotive-SPICE-PAM-v41.pdf)).

- **ISO 26262 contributes the functional-safety lifecycle and software-safety requirements.** Its scope concerns hazards “caused by malfunctioning behaviour of safety-related E/E systems” and a framework for integrating functional-safety activities into a company development framework ([ISO 26262-1:2018 official abstract](https://www.iso.org/standard/68383.html)). Part 6 is specifically software-level product development and includes “specification of the software safety requirements,” architecture, unit design/implementation, verification, integration, and embedded-software testing ([ISO 26262-6:2018 official page](https://www.iso.org/standard/68388.html)).

- **ISO/SAE 21434 contributes lifecycle cybersecurity risk management.** ISO describes it as defining “engineering requirements for cybersecurity risk management” over the E/E-system lifecycle “from concept and development to production, operation, maintenance, and decommissioning” ([ISO/SAE 21434:2021 official page](https://www.iso.org/standard/70918.html)). The same official page explicitly says ISO 26262 and ISO/SAE 21434 are “complementary and often implemented together.”

- **ReqIF is an interchange format, not a requirements-engineering or assurance process.** OMG says it serves organizations unable to share one repository and tool vendors implementing import/export interfaces ([ReqIF 1.2 official specification page](https://www.omg.org/spec/ReqIF/1.2/)). The normative specification defines “an open, non-proprietary exchange format” in which requirement information is transferred as conforming XML documents ([ReqIF 1.2 PDF, pp. 1–2](https://www.omg.org/spec/ReqIF/1.2/PDF)). Its model can preserve requirement identity and relationship structure: a `SpecObject` is “the smallest granularity by which requirements are referenced,” and a `SpecRelation` “Defines relations (links) between two SpecObject instances” ([ReqIF 1.2 PDF, pp. 74–76](https://www.omg.org/spec/ReqIF/1.2/PDF)).

### Synthesis / inference

- Automotive requirements are distinctive less because their prose follows a unique grammar than because one requirement set sits simultaneously in a **supplier/customer contract chain, a system–software–hardware decomposition, functional-safety reasoning, cybersecurity risk treatment, and long-lived configuration/change control**. The evidence expected is therefore not merely a requirements document: it includes analyzed attributes, cross-level consistency, traceability, verification/validation coverage, baselines, change impact, and communicated agreements.

- “The project is Automotive SPICE capable” cannot substitute for “the product's safety and cybersecurity obligations are satisfied.” Automotive SPICE assesses whether selected processes achieve and manage their purposes; ISO 26262 and ISO/SAE 21434 supply domain-specific safety and security obligations. Conversely, applying the ISO standards does not by itself state an Automotive SPICE capability level.

- ReqIF can transport requirement objects, attributes, hierarchy, and trace links across OEM/supplier tool boundaries. It does not decide whether a requirement is correct, whether a trace is semantically valid, whether a safety/security argument is sufficient, or whether a process is capable. Those judgments remain with the engineering and assurance processes.

## Standards interaction map

| Instrument | Primary role | Requirements contribution | Interaction / boundary |
|---|---|---|---|
| **Automotive SPICE 4.1** | Process reference and assessment model; capability determination | Elicitation/analysis, decomposition, architecture consistency, bidirectional traceability, verification, validation, configuration and change evidence | Provides the assessable engineering-process spine. Annex D references both ISO 26262:2018 and ISO/SAE 21434:2021 as standards supporting PAM/PRM implementation ([PAM 4.1, p. 159](https://vda-qmc.de/wp-content/uploads/2026/09/Automotive-SPICE-PAM-v41.pdf)); reference is not equivalence or automatic conformity. |
| **ISO 26262:2018, especially Part 6** | Functional safety for safety-related road-vehicle E/E systems | Derives and manages software safety requirements and verifies their implementation within a safety lifecycle | Adds hazard/malfunction-driven safety intent and rigor to requirements handled through the development processes. Its scope explicitly excludes nominal performance and certain non-malfunction hazards ([Part 6 official abstract](https://www.iso.org/standard/68388.html)). |
| **ISO/SAE 21434:2021** | Road-vehicle cybersecurity engineering and risk management | Adds cybersecurity goals/requirements and treatment across concept through decommissioning | Runs alongside functional safety where security threats can affect the same E/E item; it is complementary, not a replacement for ISO 26262 ([official ISO page](https://www.iso.org/standard/70918.html)). |
| **ReqIF 1.2** | Tool-neutral requirements interchange | Serializes identifiable requirement objects, attributes, hierarchy, and relations in XML | Carries artifacts and links between organizations/tools; does not impose Automotive SPICE, safety, or cybersecurity semantics. Transmission itself is outside ReqIF's scope ([ReqIF 1.2 PDF, p. 2](https://www.omg.org/spec/ReqIF/1.2/PDF)). |

**Typical interaction (inference):** safety analysis and cybersecurity risk analysis create or constrain requirements → system/software requirements processes analyze, allocate, trace, agree, and verify them → configuration/change processes preserve controlled evidence over releases → ReqIF may exchange snapshots and relationships between OEM and supplier repositories. The standards overlap at the artifacts and lifecycle activities, but they answer different questions: **process capability**, **functional safety**, **cybersecurity risk**, and **interoperable exchange**.

## Automotive-specific implications

1. **Requirements need provenance and classification.** Automotive SPICE defines stakeholder requirements broadly enough to include customer, internal, legal, regulatory, statutory, industry, and international-standard requirements ([PAM 4.1, p. 10](https://vda-qmc.de/wp-content/uploads/2026/09/Automotive-SPICE-PAM-v41.pdf)). **Inference:** repositories need to distinguish source and obligation type so safety/security and contractual requirements are not flattened into undifferentiated text.

2. **Cross-level traceability must be semantically reviewed.** SWE.1 requires consistency and bidirectional traceability from software requirements to system requirements and system architecture ([PAM 4.1, p. 44](https://vda-qmc.de/wp-content/uploads/2026/09/Automotive-SPICE-PAM-v41.pdf)). **Inference:** a generated trace matrix or imported ReqIF link is evidence of relationship, not evidence that allocation, meaning, or coverage is correct.

3. **Verification and change impact are first-class requirement concerns.** Automotive SPICE says bidirectional traceability facilitates impact analysis and demonstration of coverage ([PAM 4.1, p. 45](https://vda-qmc.de/wp-content/uploads/2026/09/Automotive-SPICE-PAM-v41.pdf)); ISO 26262-6 covers the chain through software verification and embedded-software testing ([official page](https://www.iso.org/standard/68388.html)). **Inference:** requirement quality includes verifiability, release/baseline identity, and the ability to re-evaluate affected safety/security evidence after change.

4. **The lifecycle extends beyond initial software delivery.** ISO/SAE 21434 expressly spans operation, maintenance, and decommissioning ([official page](https://www.iso.org/standard/70918.html)). **Inference:** requirements and their rationale cannot be treated as disposable design-phase paperwork, especially for vulnerability response, updates, and supplier hand-offs.

5. **Tool interoperability matters because organizational boundaries are normal.** ReqIF's stated motivation is exchange where companies rarely share a repository or authoring tool ([ReqIF 1.2 PDF, p. 1](https://www.omg.org/spec/ReqIF/1.2/PDF)). **Inference:** exchange profiles, attribute mappings, identifiers, and round-trip behavior must be agreed operationally; schema conformance alone does not guarantee lossless meaning.

## Version / staleness reconciliation

- **Automotive SPICE:** the controlling anchor is **4.1, released 2026-08-24**. The PDF title page records “Version: 4.1,” “Date: 2026-08-24,” and “Status: Released” ([PAM 4.1, p. 1](https://vda-qmc.de/wp-content/uploads/2026/09/Automotive-SPICE-PAM-v41.pdf)); its history says 4.1 removed MLE.2 BP5 and made editorial changes ([p. 3](https://vda-qmc.de/wp-content/uploads/2026/09/Automotive-SPICE-PAM-v41.pdf)). VDA's publications page lists “Version: 4.1 / August 2026” and places **4.0 under “Legacy versions”** ([official publications page](https://vda-qmc.de/en/automotive-spice/automotive-spice-veroeffentlichungen/)). Therefore, **4.0 material is superseded for current-model claims**. A separate VDA overview page still says “current version 4.0” ([overview page](https://vda-qmc.de/en/automotive-spice/)); this is stale website copy and is overridden by the dated 4.1 publication and released PDF.

- **ISO 26262:** ISO 26262-6:2018 remains the published Edition 2 and the page says it was “last reviewed and confirmed in 2024,” while also showing stage 90.92 and an ISO/DIS successor under development ([official Part 6 page](https://www.iso.org/standard/68388.html)). Use **2018** for current published requirements, while flagging that revision work exists; do not treat a DIS as the published replacement.

- **ISO/SAE 21434:** **2021 Edition 1** remains published, but ISO records stage 90.92 “to be revised” on 2026-10-02 and an AWI successor under development ([official page](https://www.iso.org/standard/70918.html)). The future revision is not yet a replacement.

- **ReqIF:** OMG identifies **1.2**, formal, published July 2016 ([official specification page](https://www.omg.org/spec/ReqIF/1.2/)). The normative PDF notes that its model and machine-readable documents are unchanged since 1.0.1 ([ReqIF 1.2 PDF, p. 1](https://www.omg.org/spec/ReqIF/1.2/PDF)); that is specification history, not evidence that 1.2 is obsolete.

## Retrieval log

| URL | Result on 2026-10-05 |
|---|---|
| [Automotive SPICE PAM 4.1 PDF](https://vda-qmc.de/wp-content/uploads/2026/09/Automotive-SPICE-PAM-v41.pdf) | Retrieved and text-inspected; title/version/status, SWE.1, SUP.8/SUP.10, history, and Annex D checked. |
| [VDA Automotive SPICE publications](https://vda-qmc.de/en/automotive-spice/automotive-spice-veroeffentlichungen/) | Retrieved; 4.1 current publication and 4.0 legacy classification checked. |
| [VDA Automotive SPICE overview](https://vda-qmc.de/en/automotive-spice/) | Retrieved; stale “current version 4.0” text recorded rather than relied upon. |
| [ISO 26262-1:2018](https://www.iso.org/standard/68383.html) | Retrieved; series scope and lifecycle status checked. |
| [ISO 26262-6:2018](https://www.iso.org/standard/68388.html) | Located and retrieved; software-level scope, current-publication statement, and revision status checked. |
| [ISO/SAE 21434:2021](https://www.iso.org/standard/70918.html) | Retrieved; lifecycle scope, complementarity statement, and revision status checked. |
| [OMG ReqIF 1.2 landing page](https://www.omg.org/spec/ReqIF/1.2/) | Retrieved; status, date, audience, and normative-document links checked. |
| [OMG ReqIF 1.2 normative PDF](https://www.omg.org/spec/ReqIF/1.2/PDF) | Retrieved and text-inspected; scope/objectives, exchange model, `SpecObject`, and `SpecRelation` checked. |

## Open questions

- Which exact customer-specific Automotive SPICE assessment scope and target capability levels apply? The PAM does not create one universal project target.
- Which requirements are safety-related, cybersecurity-related, both, or neither for the item under study? That classification requires project hazard and threat/risk analyses, not this standards map.
- What ReqIF profile, attribute vocabulary, relation types, identifier rules, and round-trip acceptance tests have the exchanging parties agreed? ReqIF 1.2 permits structure but does not settle a project's semantics.
- When the ISO 26262 and ISO/SAE 21434 revisions are published, what transition dates will customers, contracts, or regulators require? The current ISO pages establish revision activity but not those future adoption decisions.
