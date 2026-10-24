---
name: Project Knowledge
description: This skill should be used to build or explicitly update a project's searchable knowledge corpus and onboarding guide. It combines an existing SocratiCode installation with durable Markdown in research/. It covers functional behavior, concepts, architecture, cross-component flows, data lifecycles, historical rationale, and development navigation. It extends development-coordinator-simplified for execution and verification.
metadata:
  version: "1.2"
---

# Project Knowledge

## Purpose and Boundaries

Build a durable knowledge corpus for a person and an agent learning or working on a project. Compose an onboarding guide from that corpus.

Support two modes: build and update. Run either mode only on explicit request. Do not start maintenance merely because another task changes code.

Require an existing, usable SocratiCode installation. Prepare project and corpus indexing through that installation. Report missing infrastructure as a blocker. Do not install services or select embedding infrastructure.

Keep the corpus in English. Write the onboarding guide in the user's language, unless the user specifies another language. Preserve original symbol names and exact quotations.

Limit project changes to approved knowledge files and indexing configuration. Do not implement application changes. Do not add a second code index, SQL database, or graph store.

## Coordinator Integration

Invoke `development-coordinator-simplified` before execution. Extend its delivery contract with the requirements below.

Use that skill for steering, model approval, assignment prompts, task dependencies, delegation, verification, corrections, integration, and interruptions. Do not duplicate its orchestration rules or introduce a separate checkpoint system.

Keep only durable knowledge in the project's `research/` directory. Place any temporary files under `/tmp/opencode/<project-name>/`. Use the project name agreed in the delivery contract. Keep temporary files outside the indexed knowledge corpus.

Do not invoke a second research workflow that introduces competing coordination or checkpoint requirements. Apply the evidence rules in this skill to research assignments.

## Required Resources

- Read [perspectives.md](references/perspectives.md) when defining research coverage and writing assignments.
- Read [socraticode.md](references/socraticode.md) before assigning infrastructure checks, indexing, or retrieval verification.
- Use [corpus-map-template.md](assets/corpus-map-template.md) for `research/README.md`.
- Use [topic-template.md](assets/topic-template.md) for perspective topics.
- Use [project-guide-template.md](assets/project-guide-template.md) for `research/project-guide.md`.

Resolve these paths relative to this skill. Include relevant resource contents or accessible paths in worker assignments.

## Delivery Contract

Confirm the following through the coordinator's consultation procedure. Reuse decisions already explicit in the conversation.

- Select build or update mode.
- Select the whole repository or a component scope.
- Establish the reader's background and the questions the guide must answer.
- Confirm the target revision and treatment of uncommitted changes.
- Confirm allowed repository trees, historical material, external sources, and earlier research.
- Confirm the local-language guide and English corpus.
- Confirm permitted indexing-configuration changes.
- Confirm steering and worker models through the coordinator.

Map the entire agreed scope. Deepen its main scenarios, cross-cutting mechanisms, and material uncertainties. Propose those subjects after reconnaissance. Consult when the proposal changes the agreed scope or deliverable.

Do not promise exhaustive analysis of every symbol or the project's complete history.

## Durable Output Contract

Use project-relative `research/`, not filesystem-root `/research`.

```text
research/
├── README.md
├── project-guide.md
├── concepts/
├── functionality/
├── flows/
├── architecture/
├── data/
├── history/
└── development/
```

Create a perspective directory only when it has content. Divide large perspectives into bounded topic files. Use descriptive lowercase kebab-case filenames. Retain existing useful documentation and links when updating a corpus.

Treat `README.md` as the corpus map, source-authority map, and coverage inventory. Keep detailed evidence in topics. Treat `project-guide.md` as a reader-oriented synthesis, not another independent evidence store.

Keep topic metadata limited to `id`, `perspective`, `revision`, and `reviewed_at`, as shown in the template. Use a project-unique topic ID that survives file moves. Use the corresponding directory name for `perspective`. Record a full revision and an ISO review date.

If the source is not versioned, record that limitation explicitly. For dirty working-tree sources, record the base revision and identify the actual cited content. Do not present HEAD as an identifier for uncommitted bytes.

Use ordinary relative Markdown links for corpus navigation. Give materially reused claims stable heading anchors. Preserve topic IDs and claim anchors during updates. Update inbound links when moving files.

Index all durable Markdown in `research/`, including its map and guide. Do not publish templates, execution logs, unfinished drafts, or checkpoint files there.

## Evidence and Cross-References

Apply these rules to every topic and synthesis assignment:

- Establish source authority by concern. Read applicable requirements before interpreting implementation.
- Distinguish required behavior, implemented behavior, test assertions, executed observations, author rationale, and agent inference.
- Inspect primary sources before relying on earlier summaries.
- Place a descriptive source link and precise locator beside each material source-backed claim.
- Identify the source revision independently of the topic's review revision.
- Capture a short exact quotation or code excerpt that supports the claim. Preserve its wording.
- Record retrieval dates for mutable web sources. Preserve the cited passage and identify its author when available.
- State how far the evidence supports the claim. Reading an assertion does not prove that its test passed.
- Put derived explanations in a separate inference section. Link their supporting facts and state material assumptions.
- Link concepts to behavior, flows, owners, data, relevant symbols, tests, and historical changes where those relationships explain the topic.
- Describe the meaning of a relationship. Do not treat an import or matching name as proof of ownership or execution.
- Resolve material contradictions or report a blocker through the coordinator. Record minor coverage gaps and their impact.

Keep source authority in the original requirements, contracts, code, and decision records. Do not turn an explanatory note into a competing normative specification.

Avoid duplicating shared explanations. Select an owning topic and link to it from other perspectives. Use symbols to explain mechanisms. Do not reproduce a catalog of every function or local variable.

For history, compare the previous implementation, change, resulting implementation, and contemporary explanation. Attribute motivation to the actual author and decision. Do not infer an original design rationale from a later correction.

Distinguish current facts from historical facts. A rename alone does not establish continuity of a mechanism. A missing source or failed retrieval does not establish that a capability never existed.

## Build Procedure

Use these stages as dependencies for the coordinator's task graph. Group verification by shared outcomes. Do not assign one worker per perspective automatically.

### Establish Sources and Retrieval

Assign reconnaissance of the project, existing documentation, requirements, decision records, source history, and current corpus.

Require an explicit version anchor and a concern-based source-authority map. Check for shallow Git history. Use permitted upstream sources when local history is insufficient.

Assign the readiness and indexing checks in `references/socraticode.md`. Finish source-code indexing before dependent retrieval assignments.

Produce a durable corpus map and an initial glossary. Record the subjects selected for deeper analysis and the known coverage gaps.

### Research Complete Cross-Sections

Assign bounded scenarios or mechanisms with all necessary perspective questions. Allow independent subjects to run in parallel.

Trace externally visible behavior through owners, interactions, contracts, state, implementation, and tests. Research history where it explains current choices or resolves material uncertainty.

Write the results into their owning perspective topics. Connect the perspectives with explicit links. Keep temporary evidence extraction outside `research/`.

Require source and version checks before accepting a relationship into the corpus. Do not treat a successful search as proof of coverage.

### Reconcile and Compose

Assign integration of shared terms, responsibility boundaries, source authority, duplicate explanations, and cross-topic links.

Assign independent verification of material behavior, architectural boundaries, and historical rationale. Correct affected topics before composing dependent guide sections.

Compose the guide from reviewed topics. Explain the project in learning order, not directory order. Use examples and diagrams where they clarify a verified mechanism.

Link substantive guide sections to the relevant corpus topics and claim anchors. Preserve qualification and version limits during translation. Put newly discovered substantive facts into their owning topics before using them in the guide.

### Publish and Verify Retrieval

Index the durable corpus using the approved configuration. Follow the publication checks in `references/socraticode.md`.

Require representative questions about code, a corpus explanation, a cross-perspective mechanism, and a historical rationale. Record actual queries, relevant results, and original-source checks in the corpus map.

Report completion only after the acceptance criteria below pass.

## Update Procedure

Start only on a request to update the corpus. Read its current map and topic anchors before assigning work.

1. Establish the requested target revision and changed source range. Record gaps if the previous source state is unavailable.
2. Locate affected claims through their source links, symbols, concepts, and related topics. Treat dependency-tool results as discovery aids.
3. Reevaluate affected claims against current authoritative sources. Review unchanged linked topics when responsibility or terminology changes.
4. Preserve still-valid history. Replace outdated current explanations without presenting old behavior as current. Preserve topic IDs and reused claim anchors.
5. Update the affected guide sections and corpus map. Record the reviewed scope. Do not imply a new review of untouched topics.
6. Refresh code and corpus indexes through the installed tools. Handle removed or moved files explicitly.
7. Verify changed claims, cross-topic consistency, links, guide alignment, and retrieval for the affected scope.

Distinguish index refresh from semantic review. A changed source triggers reevaluation, not automatic rejection of every dependent claim. Do not rewrite a historical rationale merely because the current implementation changed.

## Acceptance and Delivery

Require verification evidence for all of the following:

- Map the agreed scope and identify source authority.
- Cover the selected main scenarios with linked behavior, ownership, state, implementation, tests, and relevant history.
- Support material claims with applicable, inspectable sources.
- Resolve material contradictions and state the impact of remaining coverage gaps.
- Keep perspective explanations and the translated guide consistent.
- Keep durable outputs in `research/` and temporary outputs outside its index.
- Confirm that SocratiCode indexes code and durable Markdown and returns them in search results.
- Demonstrate retrieval from representative questions to topics, claims, and original versioned sources.
- For updates, verify the changed scope and describe what was not reviewed.

Do not equate a green index, a set of generated files, or a worker's completion claim with acceptance.

Deliver the corpus and guide paths, version anchor, indexed scope, verification results, and remaining limitations. Report blocked indexing or material evidence gaps without claiming full completion.
