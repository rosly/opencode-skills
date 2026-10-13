---
name: Requirement Manager
description: This skill should be used when creating, analyzing, changing, relocating, splitting, merging, retiring, or reviewing project requirements; when a feature, behavioral change, or defect may affect requirements; and when maintaining requirements.md identity, hierarchy, lifecycle mappings, quality, and downstream impact before implementation.
metadata:
  version: "1.2"
---

# Requirement Manager

## Purpose

Maintain authoritative `requirements.md` documents before implementation begins. Express approved directive intent, preserve requirement identity and lifecycle traceability, expose ambiguity and conflict, and identify downstream impact without inventing product decisions or embedding implementation details in requirements.

## Governing Boundary

- Treat the user as the decision authority.
- Distinguish explicit decisions from assumptions and recommendations.
- Ask focused questions whenever plausible answers would change requirement meaning, ownership, hierarchy, numbering, acceptance criteria, or lifecycle disposition.
- Stop and wait for answers until all material ambiguity and logical conflict is resolved.
- Never treat silence as approval.
- Never resolve an open, pending, deferred, provisional, or TODO decision.
- Keep deferred and unresolved matters in design work, not in active requirements.
- Permit an explicitly decided exclusion in requirements because it is a directive decision.
- Analyze requirements only unless implementation work is separately requested after requirement decisions are complete.
- Edit only requirements documents while performing the requirements-maintenance workflow.
- Request explicit confirmation before editing any requirements document.

## Load Research References

Load `references/SOFTWARE-REQUIREMENTS-REPORT.md` when assessing requirement quality, lifecycle practice, writing, validation, traceability, or change management.

Load topic evidence only when deeper support is needed:

- `references/01-foundations-and-standards.md` for terminology, scope, and current standards.
- `references/02-practical-lifecycle.md` for elicitation, analysis, validation, prioritization, traceability, change, and iterative practice.
- `references/03-writing-quality-and-validation.md` for statement quality, review checks, testability, examples, anti-patterns, and evidence limits.
- `references/04-automotive-special-case.md` only for automotive-specific work.
- `references/00-research-plan.md` for the research scope and method.

Treat externally sourced guidance as evidence, not as permission to introduce project rules. Identify any proposed convention as a proposal and obtain approval before adopting it.

## Rule Authority

Treat requirement identity, arbitrary-depth numbering, natural-number formatting, independent functional and non-functional counters, append-at-bottom allocation, semantic immutability, relocation identity, lifecycle forms, document shape, decided exclusions, and the prohibition on implementation details as approved skill rules.

Treat `shall` wording, singular obligations, functional and non-functional classification, objective verification, and requirement-set quality checks as research-backed quality defaults. Apply them unless an applicable approved requirement defines a different convention. Never present a quality default as an observed project fact.

## Trigger Conditions

Invoke this skill when a user:

- requests a feature, behavioral change, or defect correction;
- requests creation or modification of requirements;
- mentions specifications, acceptance criteria, intended behavior, constraints, exclusions, or requirement conflicts;
- asks whether implementation conforms to requirements;
- asks to add, clarify, relocate, replace, split, merge, or retire a requirement;
- asks to create or review a `requirements.md` document.

Do not assume that every implementation defect changes requirements. First classify the request.

## Classify the Request

Classify each affected obligation independently across all four dimensions. Permit multiple lifecycle transformations when the change requires them; for example, record both semantic replacement and relocation when changing meaning while moving an obligation.

### Intent relationship

- **Already required:** Preserve the active requirement and its ID.
- **Implementation deviation:** Preserve the requirement; report downstream correction impact.
- **New directive decision:** Add a new active requirement.
- **Changed directive:** Replace the active requirement according to semantic immutability.
- **Decided exclusion:** Record the exclusion as an active directive in the decided-exclusions section.
- **Open or deferred matter:** Exclude it from active requirements and return it as an open design question.
- **Implementation detail:** Exclude it from requirement text unless the user explicitly decides that the implementation constraint is itself directive intent.

### Lifecycle transformation

- none;
- clarification;
- replacement;
- relocation;
- split;
- merge;
- retirement.

### Identity effect

- same ID;
- new subgroup ID;
- new module ID;
- multiple successor IDs;
- no successor.

### Downstream effect

- requirement references;
- design;
- implementation;
- verification;
- documentation;
- operations.

## Discover Applicable Requirement Documents

1. Determine the smallest clearly owned module scope from explicit project structure and user intent.
2. Find case-insensitive files named `requirements.md` within that scope and its parent scopes.
3. Read every applicable parent and module requirements document before analysis.
4. Read referenced requirement or design documents needed to understand existing decisions.
5. Report missing, stale, contradictory, or inaccessible references; never fill their contents by inference.
6. Ask for ownership clarification before allocating IDs when module ownership is ambiguous.

## Verify External References

- Retrieve an external source before citing or relying on it.
- Confirm that the retrieved source supports the specific assertion attributed to it.
- Prefer primary and official sources over summaries.
- Include a URL only when citing an external source.
- Record failed, restricted, stale, superseded, or contradictory retrieval rather than treating failed access as evidence of absence.
- Record the source version or publication date when it changes interpretation.
- Never invent a citation, quotation, version, or URL.
- Separate what a source states from agent inference or recommendation.
- Obtain user approval before turning external guidance into a project directive.

## Requirements Document Shape

Use this required structure while allowing functional areas and nested subgroups to expand as needed:

1. **Scope** — define covered responsibilities, boundaries, module abbreviation, applicable parent requirements, and authoritative references.
2. **Functional requirement areas** — organize active functional directives into nested requirement subgroups.
3. **Non-functional requirements** — organize active quality, architectural, methodological, process, environmental, or other constraints in an independent namespace.
4. **Decided exclusions** — include only exclusions explicitly decided by the user; exclude open and deferred matters.
5. **Requirement provenance** — map every active requirement to its stable source or parent, rationale, and decision authority without implementation references.
6. **Requirement lifecycle map** — record clarification, replacement, relocation, split, merge, and retirement.

Keep one active inline requirement set. Never create amendment, updated-requirements, version-two, or similar sidecar sections.

Use this required provenance table:

| Requirement ID | Source or parent | Rationale | Decision authority |
|---|---|---|---|

Permit source references to requirement IDs, approved decision records, external obligations, and named stakeholder decisions. Never use code paths, source symbols, test symbols, or implementation artifacts as requirement provenance. Require rationale when derivation is not self-evident. Treat a requirement without approved provenance as incomplete.

Keep stakeholder validation evidence in a separate approval record, not in `requirements.md`. Keep delivery priority outside this skill and outside the requirements document. When an ordering constraint is itself directive behavior, specify that behavior without treating it as delivery priority.

## Requirement ID Scheme

### Syntax

Use arbitrary-depth hierarchical IDs:

```text
REQ-<MODULE>-<O>.<P>.<R>...
REQ-NF-<MODULE>-<O>.<P>.<R>...
```

- Use a stable uppercase module abbreviation.
- Use natural numbers without zero padding: `1.2.3`, not `001.002.003`.
- Permit as many numeric levels as the requirement subgroup tree needs.
- Interpret the numeric path as the nested requirement-subgroup path, not as a fixed two-level family/leaf structure.
- Keep functional and non-functional counters independent.
- Never reuse, recycle, renumber, or backfill an allocated ID.
- Leave permanent gaps after supersession, relocation, or retirement.

### Ordering and allocation

- Number nested requirement groups in their order of introduction.
- Present groups and requirements in natural top-to-bottom hierarchical order.
- Allocate a new sibling with the greatest existing sibling number plus one at the applicable hierarchy level.
- Append every new requirement at the bottom of its proper subgroup.
- Append every semantic replacement at the bottom of its proper subgroup using the next free ID; never place it in the superseded requirement's old position merely to preserve reading position.
- Allocate a new ID when moving a requirement to another subgroup within the same module.
- Allocate a new ID under the destination module when moving a requirement to another module.
- Record every relocation as an old-to-new lifecycle mapping even when semantics remain unchanged.

## Semantic Immutability

Treat an ID as identifying one semantic directive within one module and subgroup location.

Retain the ID only when a change provably preserves meaning and acceptance criteria, such as:

- correcting spelling or formatting;
- replacing wording with an exactly equivalent defined term;
- clarifying grammar without changing subject, trigger, obligation, conditions, limits, exceptions, or acceptance criteria.

Allocate a new ID when changing any of the following:

- responsible subject;
- trigger or precondition;
- required behavior or property;
- result or output;
- operating condition;
- threshold, timing, unit, tolerance, or statistical basis;
- exception or prohibition;
- acceptance criteria;
- module or subgroup placement.

Treat uncertainty about semantic equivalence as a material ambiguity and ask the user. Do not retain an ID merely because wording changes appear small.

## Requirement Writing Rules

- Express directive intent rather than implementation detail.
- Never include source-code symbols, source paths, test symbols, or implementation-specific references in requirement text.
- Use `shall` for an obligation and `shall not` for a prohibition.
- State one independently decidable obligation per requirement.
- Name the responsible subject.
- State the applicable trigger or condition when needed.
- Describe observable behavior or a verifiable property.
- State required results, limits, units, tolerances, and exceptions where applicable.
- Define domain terms that could carry multiple meanings.
- Replace subjective or unbounded terms with decided criteria.
- Separate rationale and explanation from normative wording.
- Avoid prescribing a solution unless the solution constraint is explicitly decided as intent.
- Incorporate the observable pass/fail conditions and measurable acceptance boundaries into the requirement wording.
- Express independently decidable acceptance conditions as nested requirements with their own IDs.
- Add a verification sub-element only when a detailed procedure materially supports the requirement; make that sub-element a reference to an external controlled verification document rather than embedding the procedure.
- Do not mistake an example for complete acceptance criteria.
- Treat acceptance criteria as part of requirement semantics. Allocate a new ID when they change.
- Permit a verification procedure reference to change without a new requirement ID only when the directive and acceptance criteria remain unchanged.
- Allocate a new ID when a verification change alters the observable pass/fail boundary.

Use this formulation as guidance, not as mandatory grammar:

```text
When <trigger or condition>, <subject> shall <observable obligation> <result and limits>.
```

## Functional and Non-functional Classification

- Classify externally observable capabilities, responses, and transformations as functional requirements.
- Classify quality, performance, reliability, security, architecture, methodology, process, compatibility, and environmental constraints as non-functional requirements.
- Select verification by the obligation, not by its prefix. Permit automated test, manual test, analysis, inspection, demonstration, audit, review, or a combination.
- Never automatically exclude all non-functional requirements from code-based verification.

## Quality Gates

### Check each requirement

- Confirm necessity and an identifiable decision or parent directive.
- Confirm one primary obligation.
- Confirm unambiguous subject, terms, scope, references, and qualifiers.
- Confirm sufficient conditions, bounds, units, and exceptions.
- Confirm feasibility within known constraints.
- Confirm an objective verification method can distinguish satisfaction from non-satisfaction.
- Confirm conformity with the document's ID, hierarchy, and wording rules.
- Confirm stable provenance identifies an approved source or parent, rationale when needed, and decision authority.

### Distinguish verification from validation

- **Verify the requirement:** determine whether its identity, placement, wording, completeness, feasibility, consistency, and observable pass/fail conditions conform to approved rules.
- **Validate the requirement:** determine whether it expresses the correct approved need in the intended context without unintended behavior or material omission.
- Obtain validation from the applicable decision authority after creating or semantically changing requirements.
- Record validation against a requirement-set baseline in a separate controlled approval record.
- Never treat wording review, test existence, or agent analysis as stakeholder validation.
- Never treat planned verification as executed evidence or executed evidence as automatic proof that the underlying need was correct.

### Check the active set

- Confirm scope and interface coverage.
- Check normal, boundary, failure, recovery, and prohibited behavior where applicable.
- Detect contradiction, duplication, orphan requirements, and missing parent directives.
- Confirm requirements are jointly feasible, not only individually feasible.
- Confirm no superseded or relocated definition remains active.
- Confirm no unresolved or deferred matter appears as an active directive.
- Confirm every referenced requirement ID exists and is active unless explicitly referenced as historical.
- Select applicable completeness views from actors, scenarios, boundaries, states and transitions, interfaces, failures and recovery, prohibited behavior, misuse or adverse conditions, quality constraints, external obligations, configuration variants, and operational phases.
- Explain any omitted completeness view that appears applicable; do not apply every view mechanically.

## Lifecycle Rules

Keep superseded normative text in version control only. Remove it from active sections after approval and retain only lifecycle metadata in the document.

Use a lifecycle table with these required columns:

| Previous ID | Disposition | Successor | Reason |
|---|---|---|---|

Support these dispositions:

- **Clarified:** retain the same ID; preserve semantics and acceptance criteria.
- **Replaced:** map one previous ID to one successor.
- **Relocated:** map an unchanged semantic directive to its new subgroup or module ID.
- **Split:** map one previous ID to multiple successors.
- **Merged:** map multiple previous IDs to one successor.
- **Retired:** identify no successor and state the approved reason.

Never leave both previous and successor definitions active. Never reuse the previous ID.

### Preserve provenance through lifecycle changes

- Preserve provenance for a clarification.
- Reassess provenance for every replacement or relocation.
- Require split successors collectively to preserve every retained source obligation unless the user explicitly removes one.
- Require a merged successor to retain every compatible source and expose source conflicts for decision.
- Treat an active requirement without an approved source or parent as an orphan requiring clarification.

### Migrate active requirement references

For every clarification, replacement, relocation, split, merge, or retirement:

1. Search all applicable requirements documents for the previous ID.
2. Classify each occurrence as an active normative reference, lifecycle-history reference, explanatory reference, or numeric range containing the ID.
3. Update active normative references to the correct successor or successors.
4. Preserve intentionally historical references.
5. Expand or replace ranges when a lifecycle change makes the range inaccurate or misleading.
6. Ask for a decision when split or merge semantics prevent deterministic migration.
7. Include unresolved migrations in the impact report.
8. Reject active references to superseded or retired IDs unless explicitly marked historical.

### Validate trace semantics

- Confirm that a parent actually justifies its child.
- Confirm that a child does not exceed its parent without another approved source.
- Confirm that a replacement covers the intended previous obligation.
- Confirm that split successors collectively cover every retained semantic obligation.
- Confirm that a merge preserves all compatible obligations and exposes conflicts.
- Confirm that a relocation preserves semantics unless also classified as a semantic change.
- Confirm that requirement wording makes complete verification observable rather than merely sharing terminology with a procedure.
- Confirm that a decided exclusion does not contradict an active directive.
- Treat link existence only as evidence that a relationship was recorded, never as proof of semantic consistency.

## Create Requirements from an Undeveloped Need

Tailor discovery effort to scope and risk; do not force a full elicitation exercise for a small, already-decided correction.

1. Frame the requested outcome, boundary, affected context, and decision authority.
2. Identify relevant human and non-human sources, including parent requirements, approved decisions, external obligations, existing behavior, interfaces, policies, and constraints.
3. Identify affected stakeholder classes and detect missing or unavailable sources.
4. Use complementary elicitation methods when one source or method cannot establish sufficient coverage.
5. Capture assumptions, candidate needs, conflicts, and unresolved questions separately from active requirements.
6. Analyze candidates for meaning, duplication, dependencies, conflicts, feasibility, missing conditions, and objective verification.
7. Separate need and directive intent from suggested implementation.
8. Obtain user decisions for every material alternative or unresolved conflict.
9. Convert only approved directive decisions into numbered active requirements.
10. Validate the resulting requirement-set baseline with the applicable decision authority and keep that approval in a separate record.

## Ordered Maintenance Workflow

1. **Frame scope.** Identify the request, owning module, applicable parent scopes, decision authority, and requirement documents.
2. **Read the active baseline.** Extract applicable requirements, hierarchy, highest allocated sibling numbers, provenance, decided exclusions, lifecycle mappings, and active references.
3. **Classify every dimension.** Record intent relationship, all lifecycle transformations, identity effects, and downstream effects.
4. **Analyze quality and impact.** Check provenance, consistency, completeness views, feasibility, objective verification, validation needs, semantic traces, reference migration, and downstream artifacts.
5. **Resolve ambiguity.** Ask the smallest focused question set needed, one round at a time when appropriate; stop until material ambiguity is resolved.
6. **Propose changes.** Show exact additions, removals, retained IDs, new IDs, subgroup placement, provenance changes, reference migrations, and lifecycle mappings. Label recommendations as proposals.
7. **Produce the impact report.** Keep implementation and test locations out of normative requirement text; report affected downstream artifacts separately.
8. **Request confirmation.** Ask whether to apply the exact scoped requirement updates and wait for explicit approval.
9. **Edit minimally.** Update only approved requirements documents. Keep the active set inline, append new IDs at the bottom of their proper subgroups, migrate active references, and update provenance and lifecycle tables.
10. **Validate integrity.** Run mechanical validation, then check semantic identity, trace consistency, completeness, validation requirements, reference integrity, wording quality, and absence of placeholders.

## Requirement Lifecycle Impact Report

Produce this report before every edit that adds, changes, relocates, splits, merges, or retires requirements:

- Intent, lifecycle, identity, and downstream classifications.
- Applicable active requirements.
- Requirement sources and provenance effects.
- New requirement IDs and subgroup placement.
- Clarified IDs retaining identity.
- Previous-to-successor mappings.
- Retired IDs.
- Explicitly unchanged requirements.
- Active requirement-reference migrations, including ranges.
- Semantic trace findings for parent, replacement, split, merge, and relocation relationships.
- Downstream behavior, design, implementation, verification, documentation, and operational artifacts requiring review or change.
- Verification wording, external procedure references, acceptance criteria, and executed evidence affected.
- Separate approval records requiring validation or revalidation.
- External-reference retrieval, version, staleness, conflict, and accessibility status.
- Open questions and deferred design matters.

Search for direct requirement-ID references and behaviorally coupled artifacts. Keep all discovered implementation references in the impact report, never in normative requirement statements.

## Confirmation Prompt

Use an exact confirmation boundary:

> Proceed with the scoped requirements-document updates defined in the lifecycle impact report?

Treat approval as authorization only for the listed requirement-document edits. Do not infer approval for downstream implementation.

## Post-edit Validation

Verify all of the following after editing:

- Every active requirement has one unique valid ID.
- Every numeric path matches its requirement subgroup.
- Every new sibling uses the greatest prior sibling number plus one.
- Functional and non-functional counters remain independent.
- No allocated number was reused or backfilled.
- Every changed, relocated, split, merged, or retired requirement has a lifecycle record.
- Every lifecycle successor exists in the active set.
- No superseded definition remains active.
- Every active requirement has stable provenance with source or parent, rationale when needed, and decision authority.
- Every active normative reference resolves to an active requirement or is explicitly historical.
- Every parent-child, replacement, relocation, split, and merge relationship is semantically consistent.
- No code symbol, source path, or test symbol appears in normative requirement text.
- No open or deferred decision appears as an active requirement.
- Every decided exclusion is explicit and unambiguous.
- Every referenced document and requirement exists or is reported as unresolved.
- Every external citation was retrieved and supports its attributed assertion, or its retrieval limitation is recorded.
- Every requirement is singular, feasible, consistent, and worded with observable verification conditions.
- Every new or semantically changed requirement set identifies the separate approval record needed for validation.
- No delivery-priority metadata appears.

## Mechanical Validator

Run `scripts/validate_requirements.py` after editing requirements documents:

```bash
python scripts/validate_requirements.py <requirements.md> [<requirements.md> ...]
```

Use the validator only for deterministic checks: ID syntax, natural-number formatting, duplicate active IDs, top-to-bottom hierarchy order, required provenance and lifecycle columns, successor existence, active use of superseded IDs, and likely implementation references in normative lines. Review every warning manually. Never use script success as evidence of semantic equivalence, feasibility, completeness, correct validation, or stakeholder approval.

## Response Format

Always return:

- **Applicable requirements:** active IDs and concise relevance.
- **Classification:** intent relationship, lifecycle transformations, identity effects, and downstream effects.
- **Proposed or completed requirement changes:** additions, clarifications, replacements, relocations, splits, merges, retirements, exclusions, provenance, and active-reference migrations.
- **Lifecycle mapping:** previous ID, disposition, successor, and reason, or `none`.
- **Validation and verification:** wording or procedure-reference changes and separate approval records required.
- **Updated files:** requirement files changed, or `none` while awaiting clarification or confirmation.
- **Downstream impact:** affected artifacts and required actions, kept separate from normative requirements.
- **External references:** verified, stale, conflicting, inaccessible, or `none`.
- **Open questions:** unresolved or deferred matters, or `none`.

## Failure Modes

- Do not invent behavior to complete a partially specified request.
- Do not present a proposed convention as an observed or approved rule.
- Do not preserve an ID after semantic or structural identity changes.
- Do not create a fixed two-level interpretation for an arbitrary-depth numeric hierarchy.
- Do not place a replacement into an old position contrary to append-at-bottom allocation.
- Do not use amendment sections or dual-active definitions.
- Do not treat implementation as authoritative intent.
- Do not place implementation trace details in requirement text.
- Do not classify every defect as a requirement change.
- Do not force one exclusive classification when multiple lifecycle transformations apply.
- Do not treat link existence as proof of semantic consistency.
- Do not treat requirement verification as stakeholder validation.
- Do not store validation approval inside `requirements.md`.
- Do not move delivery priority into requirements management; it is out-of-scope planning.
- Do not embed detailed verification procedures; reference an external controlled document only when the detail materially supports the requirement.
- Do not claim script validation proves semantic quality.
