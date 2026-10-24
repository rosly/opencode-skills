# SocratiCode Operations and Limits

## Applicability

Use the installed MCP tool catalog and documentation as the operational contract. Discover exact tool paths and argument schemas before calling them.

Treat the findings below as version-anchored guidance. The underlying research examined runtime 1.16.1 and release source `eb94e073cb8aa80d08fd56c8aecfe7f2fa065be8`. It did not establish byte equality between them.

Recheck relevant behavior when the installed version differs. Do not assume that a limitation or API shape is permanent.

## Readiness

1. Discover the available SocratiCode tools.
2. Use the installed equivalents of `codebase_about` and `codebase_health` to identify the version and service readiness.
3. Use `codebase_status` and `codebase_graph_status` with the explicit target project path.
4. Inspect existing context-artifact configuration and exclusions before proposing changes.
5. Confirm that the project path identifies the intended repository or worktree.

Report unavailable MCP, storage, or embedding infrastructure as a blocker. Do not install or replace those services through this skill.

Do not assume a healthy infrastructure means that SocratiCode indexes the target project.

## Code Index

Use `codebase_index` when the project has no usable index. Wait for indexing completion through the installed status mechanism before searching.

Use `codebase_update` for an explicit incremental refresh. Check completion and reported failures. Do not start competing update or graph-build operations for the same project.

Use the installed graph-status and build operations when an assignment needs a missing dependency graph. Treat graph readiness separately from text-index readiness.

Inspect actual retrieval of a relevant source file. Do not accept readiness solely from a green status label.

## Durable Corpus Index

Include all durable project-relative `research/**/*.md` content, including `README.md` and `project-guide.md`.

First check whether ordinary project indexing already includes those files. Verify an actual corpus result. Do not create duplicate representations merely to add a context-artifact configuration.

If ordinary indexing excludes the corpus, use the installed context-artifact mechanism. Load the applicable configuration schema and documentation before editing it. Obtain approval for the required project configuration changes.

Preserve existing artifact definitions and project exclusions. Keep temporary paths outside the corpus. Do not change a global indexing policy to solve a project-local need.

In the studied release, `.socraticodecontextartifacts.json` defines context artifacts. Relevant operations include `codebase_context`, `codebase_context_index`, and `codebase_context_search`. Check the installed contract before constructing configuration entries.

After publication or an update:

- Verify which mechanism indexes each durable area.
- Check that new and changed topics return current content.
- Check moved and removed paths when the update includes them.
- Record the indexed scope, mechanism, version, and verification date in the corpus map.
- Verify that temporary execution files are outside the indexed knowledge scope.

Do not claim that a named directory reference in an agent environment configures SocratiCode indexing.

## Retrieval Modes

| Need | Operation or method | Required follow-up |
|---|---|---|
| Discover a mechanism by meaning | `codebase_search` or `codebase_context_search` | Open the source and confirm its scope and revision |
| Find definitions or named symbols | `codebase_symbols`, `codebase_symbol` | Resolve ambiguous names and inspect the actual definition |
| Explore imports and dependents | `codebase_graph_query` | Distinguish structural dependency from responsibility |
| Explore captured symbol relations | `codebase_flow` | Inspect relation kinds before describing execution |
| Find possible change impact | `codebase_impact` | Check local callers and other relevant evidence |
| Find an exact phrase or all occurrences | File search and direct reads | State the searched scope and relevant exclusions |
| Explain a historical choice | Git, versioned source, decisions, and author discussion | Compare before and after states and attribute rationale |

Use explicit project paths. Add file hints when symbols are ambiguous. Treat ranked results as discovery candidates, not an exhaustive inventory.

Do not assume that frontmatter fields or Markdown links become structured relation queries. The studied context API exposes artifact-name filtering, not arbitrary YAML predicates or link traversal.

## Evidence and Citation Limits

- Attach a source revision separately. The studied code-search renderer returns paths and lines without immutable revision anchors.
- Inspect the original child file before citing directory-artifact line ranges. The studied reader concatenates files into one text stream.
- Interpret `flow` as captured symbol relations. The studied traversal includes type references and does not constitute an execution trace.
- Inspect same-file callers when impact reports zero files. The studied algorithm excludes the definition file from newly impacted files.
- Check original sources after a context-artifact read failure. Source analysis indicates that a still-configured unreadable artifact can retain old chunks.

The stale-context conclusion is conditional and source-derived. The research did not run an end-to-end context read-failure experiment. Do not generalize it to every indexing mechanism.

## Retrieval Acceptance

Use questions grounded in the agreed coverage. Do not introduce fabricated marker content into the durable corpus.

Require representative checks for:

- A code definition or contract.
- An English corpus explanation retrieved by its meaning.
- A cross-perspective question leading to linked topics and their evidence.
- A historical rationale, or an explicit explanation of the permitted-source limitation.
- A question in the guide's language when it differs from English.

Record the actual query, mechanism, useful result, and original-source check. Link the retrieved topic or source. Do not copy entire tool responses into the corpus map.

Investigate material retrieval failures. Do not substitute direct file access for a failed contextual-search acceptance criterion without consulting the user.

Do not claim measured recall, multilingual quality, or graph completeness from these representative checks.

## Version-Anchored Sources

- [Release tool schemas](https://github.com/giancarloerra/SocratiCode/blob/eb94e073cb8aa80d08fd56c8aecfe7f2fa065be8/src/index.ts)
- [Hybrid retrieval and filters](https://github.com/giancarloerra/SocratiCode/blob/eb94e073cb8aa80d08fd56c8aecfe7f2fa065be8/src/services/qdrant.ts#L919-L1015)
- [Search-result renderer](https://github.com/giancarloerra/SocratiCode/blob/eb94e073cb8aa80d08fd56c8aecfe7f2fa065be8/src/tools/query-tools.ts#L204-L209)
- [Flow traversal](https://github.com/giancarloerra/SocratiCode/blob/eb94e073cb8aa80d08fd56c8aecfe7f2fa065be8/src/services/graph-impact.ts#L497-L520)
- [Impact traversal](https://github.com/giancarloerra/SocratiCode/blob/eb94e073cb8aa80d08fd56c8aecfe7f2fa065be8/src/services/graph-impact.ts#L340-L374)
- [Context reading and concatenation](https://github.com/giancarloerra/SocratiCode/blob/eb94e073cb8aa80d08fd56c8aecfe7f2fa065be8/src/services/context-artifacts.ts#L254-L358)
- [Context freshness and cleanup](https://github.com/giancarloerra/SocratiCode/blob/eb94e073cb8aa80d08fd56c8aecfe7f2fa065be8/src/services/context-artifacts.ts#L850-L918)
- [Context search after freshness checks](https://github.com/giancarloerra/SocratiCode/blob/eb94e073cb8aa80d08fd56c8aecfe7f2fa065be8/src/tools/context-tools.ts#L154-L169)
- [Incremental file updates](https://github.com/giancarloerra/SocratiCode/blob/eb94e073cb8aa80d08fd56c8aecfe7f2fa065be8/src/services/indexer.ts#L1734-L1913)
