# SocratiCode Use and Limits

## Applicability

Use the installed MCP tool catalog and documentation as the operational contract. Discover exact tool paths and argument schemas before calling them.

Treat the findings below as version-anchored guidance. The underlying research examined runtime 1.16.1 and release source `eb94e073cb8aa80d08fd56c8aecfe7f2fa065be8`. It did not establish byte equality between them.

Recheck relevant behavior when the installed version differs. Do not assume that a limitation or API shape is permanent.

## Project Access and First Indexing

Use an explicit project path that identifies the intended repository or worktree. Discover the available search and analysis tools and their argument schemas.

If SocratiCode reports that the project has no index, use the installed equivalent of `codebase_index` to start its first indexing operation. Observe completion through the installed status mechanism before dependent searches. Do not treat an existing but malfunctioning index as permission to index the project again.

Leave subsequent index and graph maintenance to SocratiCode. Do not perform installation or infrastructure checks, request refreshes or rebuilds, control watchers or indexing concurrency, or change configuration, services, or processes.

If MCP malfunctions, stop work and report the attempted operation and observed problem to the user. Do not diagnose or repair it. Do not infer a malfunction solely from an irrelevant or empty search result; assess the query and source evidence as part of ordinary research.

## Project Knowledge Retrieval

Treat durable project-relative `research/**/*.md` content, including `README.md` and `project-guide.md`, as project knowledge for semantic search alongside code. Leave automatic inclusion of these files and their changes to SocratiCode. Do not create a separate indexing configuration or procedure for this corpus.

After publication or an update, search for new and changed topics and compare useful results with their current source files. Check retrieved paths when topics move or are removed. Record actual queries, useful results, original-source checks, and the verification date in the corpus map.

Keep temporary execution files outside `research/`. Do not accept a tool status label as evidence that a particular explanation can be retrieved.

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

## Retrieval Acceptance

Use questions grounded in the agreed coverage. Do not introduce fabricated marker content into the durable corpus.

Require representative checks for:

- A code definition or contract.
- An English corpus explanation retrieved by its meaning.
- A cross-perspective question leading to linked topics and their evidence.
- A historical rationale, or an explicit explanation of the permitted-source limitation.
- A question in the guide's language when it differs from English.

Record the actual query, mechanism, useful result, and original-source check. Link the retrieved topic or source. Do not copy entire tool responses into the corpus map.

Report unmet retrieval acceptance criteria to the user. Do not substitute direct file access for a failed contextual-search acceptance criterion without consulting the user. If the failure reveals an MCP malfunction, stop work under the rule above instead of investigating it.

Do not claim measured recall, multilingual quality, or graph completeness from these representative checks.

## Version-Anchored Sources

- [Release tool schemas](https://github.com/giancarloerra/SocratiCode/blob/eb94e073cb8aa80d08fd56c8aecfe7f2fa065be8/src/index.ts)
- [Hybrid retrieval and filters](https://github.com/giancarloerra/SocratiCode/blob/eb94e073cb8aa80d08fd56c8aecfe7f2fa065be8/src/services/qdrant.ts#L919-L1015)
- [Search-result renderer](https://github.com/giancarloerra/SocratiCode/blob/eb94e073cb8aa80d08fd56c8aecfe7f2fa065be8/src/tools/query-tools.ts#L204-L209)
- [Flow traversal](https://github.com/giancarloerra/SocratiCode/blob/eb94e073cb8aa80d08fd56c8aecfe7f2fa065be8/src/services/graph-impact.ts#L497-L520)
- [Impact traversal](https://github.com/giancarloerra/SocratiCode/blob/eb94e073cb8aa80d08fd56c8aecfe7f2fa065be8/src/services/graph-impact.ts#L340-L374)
- [Context reading and concatenation](https://github.com/giancarloerra/SocratiCode/blob/eb94e073cb8aa80d08fd56c8aecfe7f2fa065be8/src/services/context-artifacts.ts#L254-L358)
