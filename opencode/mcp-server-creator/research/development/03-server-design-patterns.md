# MCP Server Design Patterns (Protocol Revision 2026-07-28)

Research file. Retrieved: 2026-10-03. Protocol revision referenced throughout: **2026-07-28**.

## Notation and evidence ranking

- **SOURCE FACT** — a normative statement quoted verbatim from an official specification/SEP or official documentation page.
- **SOURCE CLAIM (Rank N)** — a non-normative statement quoted verbatim. Ranks: **Rank A** = Final/Standards-Track SEP or normative specification text; **Rank B** = official documentation page (editorial guidance); **Rank C** = roadmap/project-status page.
- **AI INFERENCE** — my reasoning that names the specific quoted facts it is derived from.
- **PLAUSIBLE NOT VERIFIED** — a conjecture consistent with sources but not directly stated.
- **UNKNOWN** — no source retrieved or source is silent.

Quotations are short and exact. Every externally sourced fact carries an inline link to the source URL. No end-only bibliography is used. All nine requested URLs for this file were retrieved successfully; there are no failed retrievals for FILE 1.

## 1. Choosing between tool, resource, and prompt

**SOURCE FACT.** The three primitives have distinct control models. Tools are "**model-controlled**, meaning that the language model can discover and invoke tools automatically based on its contextual understanding and the user's prompts." ([Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md))

**SOURCE FACT.** Resources are "**application-driven**, with host applications determining how to incorporate context based on their needs." ([Resources](https://modelcontextprotocol.io/specification/2026-07-28/server/resources.md))

**SOURCE FACT.** Prompts are "**user-controlled**, meaning they are exposed from servers to clients with the intention of the user being able to explicitly select them for use." ([Prompts](https://modelcontextprotocol.io/specification/2026-07-28/server/prompts.md))

**SOURCE FACT.** The protocol does not mandate a UI: for tools, "implementations are free to expose tools through any interface pattern that suits their needs—the protocol itself does not mandate any specific user interaction model." ([Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md))

**SOURCE FACT.** Resources are "uniquely identified by a [URI](https://datatracker.ietf.org/doc/html/rfc3986)." ([Resources](https://modelcontextprotocol.io/specification/2026-07-28/server/resources.md))

**AI INFERENCE (naming the three control-model facts).** The selection rule follows from who decides: if the model should decide when to act, expose a tool; if the host decides what context to attach, expose a resource; if the user explicitly invokes a workflow, expose a prompt. This is derived from the quoted "model-controlled", "application-driven", and "user-controlled" statements.

**SOURCE FACT (safety).** "For trust & safety and security, there **SHOULD** always be a human in the loop with the ability to deny tool invocations." ([Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md))

## 2. Tool naming and descriptions

**SOURCE FACT.** Current-spec naming rules: "Tool names **SHOULD** be between 1 and 128 characters in length (inclusive)."; "Tool names **SHOULD** be considered case-sensitive."; "The following **SHOULD** be the only allowed characters: uppercase and lowercase ASCII letters (A-Z, a-z), digits (0-9), underscore (\_), hyphen (-), and dot (.)"; "Tool names **SHOULD NOT** contain spaces, commas, or other special characters."; "Tool names **SHOULD** be unique within a server." ([Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md))

**SOURCE FACT.** Example valid names in the current spec: "`getUser`", "`DATA_EXPORT_v2`", "`admin.tools.list`". ([Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md))

**SOURCE FACT.** The originating SEP states a different length and character set: "tool names should be 1–64 characters, case-sensitive, and may include alphanumeric characters, underscores (\_), dashes (-), dots (.), and forward slashes (/)." ([SEP-986: Specify Format for Tool Names](https://modelcontextprotocol.io/seps/986-specify-format-for-tool-names))

**SOURCE FACT.** SEP-986's normative list: "Tool names SHOULD be between 1 and 64 characters in length (inclusive)."; "Allowed characters: uppercase and lowercase ASCII letters (A-Z, a-z), digits (0-9), underscore (\_), dash (-), dot (.), and forward slash (/)."; "Tool names SHOULD be unique within their namespace." ([SEP-986](https://modelcontextprotocol.io/seps/986-specify-format-for-tool-names))

**AI INFERENCE (naming the two naming-rule facts).** The current specification and SEP-986 disagree on two points: the maximum length (128 vs 64) and whether forward slash is allowed (current spec omits it; SEP-986 includes it). A server that stays within 1–64 characters and uses only `[A-Za-z0-9_.-]` satisfies both texts; a server relying on `/` or on lengths above 64 satisfies SEP-986 but not the current spec's character list. This is derived from the two quoted rule sets.

**SOURCE FACT (collisions).** "Tool name uniqueness is scoped to a single server. Clients or proxies that aggregate tools from multiple servers **MAY** encounter naming collisions ... and **SHOULD** implement a disambiguation strategy such as prefixing tool names with a server identifier." ([Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md))

**SOURCE FACT (determinism).** "Servers **SHOULD** return tools in a deterministic order (i.e., the same ordering across requests when the underlying set of tools has not changed). Deterministic ordering enables clients to reliably cache the tool list and improves LLM prompt cache hit rates when tools are included in model context." ([Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md))

**SOURCE FACT (description field).** A tool definition includes "`description`: Human-readable description of functionality" and an optional "`title`: Optional human-readable name of the tool for display purposes." ([Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md))

**SOURCE CLAIM (Rank B).** The TypeScript framework MCP-Framework enforces descriptions at build time: "All schema fields must have descriptions." and "This command checks that all tools using Zod schemas have descriptions for every field." ([MCP Framework README](https://github.com/QuantGeekDev/mcp-framework))

## 3. inputSchema and outputSchema design

**SOURCE FACT.** "`inputSchema`: JSON Schema defining expected parameters"; it "**MUST** be a valid JSON Schema object (not `null`)" and "Defaults to 2020-12 if no `$schema` field is present". ([Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md))

**SOURCE FACT.** For tools with no parameters the recommended form is "`{ "type": "object", "additionalProperties": false }` - **Recommended**: explicitly accepts only empty objects". ([Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md))

**SOURCE FACT.** "`outputSchema`: Optional JSON Schema defining expected output structure"; "If an output schema is provided: Servers **MUST** provide structured results that conform to this schema. Clients **SHOULD** validate structured results against this schema." ([Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md))

**SOURCE FACT.** SEP-2106 loosened the schema restrictions: "**`inputSchema`**: Keeps `type: "object"` required (since tool arguments are objects), but allows any additional JSON Schema properties to support powerful validation compositions (`anyOf`, `oneOf`, `allOf`, etc.)"; "**`outputSchema`**: Fully supports JSON Schema 2020-12 since MCP servers may return any valid JSON"; "**`structuredContent`**: Accepts any JSON value validated by `outputSchema`". ([SEP-2106: Tools inputSchema & outputSchema Conform to JSON Schema 2020-12](https://modelcontextprotocol.io/seps/2106-json-schema-2020-12))

**SOURCE FACT.** SEP-2106 gives a composition example: a tool can accept "either an ID-based or name-based lookup" via `oneOf`. ([SEP-2106](https://modelcontextprotocol.io/seps/2106-json-schema-2020-12))

**SOURCE FACT (security).** "Implementations **MUST NOT** automatically dereference `$ref` values that resolve to a network URI (i.e. anything that is not a same-document JSON Pointer such as `#/$defs/Foo` or an internal `$anchor`)." ([SEP-2106](https://modelcontextprotocol.io/seps/2106-json-schema-2020-12))

**SOURCE FACT (security).** "Composition keywords (`anyOf`, `oneOf`, `allOf`, `if`/`then`/`else`) and `$defs` enable expressive schemas, but pathological combinations can be expensive to validate. Implementations SHOULD apply reasonable bounds". ([SEP-2106](https://modelcontextprotocol.io/seps/2106-json-schema-2020-12))

**SOURCE FACT (HTTP header mirroring).** "The `x-mcp-header` extension property allows servers to designate specific tool parameters to be mirrored into HTTP headers when using the Streamable HTTP transport." ([Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md))

**SOURCE FACT (header safety).** "Server developers **SHOULD NOT** mark sensitive parameters (passwords, API keys, tokens, PII) with `x-mcp-header`, as header values are visible to network intermediaries." ([Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md))

## 4. structuredContent

**SOURCE FACT.** "**Structured** content is returned as a JSON value in the `structuredContent` field of a result. This can be any JSON value (object, array, string, number, boolean, or null) that conforms to the tool's `outputSchema` if one is defined." ([Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md))

**SOURCE FACT.** "For backwards compatibility, a tool that returns structured content SHOULD also return the serialized JSON in a TextContent block." ([Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md))

**SOURCE FACT.** SEP-2106 makes the fallback mandatory for non-object results: "servers using array or primitive `structuredContent` MUST also emit a `TextContent` block containing the serialized JSON". ([SEP-2106](https://modelcontextprotocol.io/seps/2106-json-schema-2020-12))

**SOURCE FACT.** "`structuredContent` is server-produced result data and is unrelated to LLM "structured outputs" (schema-constrained model generation)." ([Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md))

**SOURCE FACT (why output schemas matter).** Providing an output schema "Enabl[es] strict schema validation of responses", "Provid[es] type information for better integration with programming languages", and "Guid[es] clients and LLMs to properly parse and utilize the returned data". ([Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md))

**SOURCE CLAIM (Rank B).** Client best practices tie output schemas to code generation: "When an output schema is present, the host can produce precise return types (like `LogEntry` above)." and "The real fix is for server authors to provide `outputSchema`." ([Client Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices))

## 5. Error handling: protocol errors vs execution errors

**SOURCE FACT.** "Tools use two error reporting mechanisms:" — "**Protocol Errors** indicate issues with the request structure itself that models are less likely to be able to fix: Unknown tool; Malformed requests ...; Server errors"; "**Tool Execution Errors** contain actionable feedback that language models can use to self-correct and retry with adjusted parameters: API failures; Input validation errors ...; Business logic errors". ([Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md))

**SOURCE FACT.** Protocol errors are "returned as standard JSON-RPC errors", e.g. `{"code": -32602, "message": "Unknown tool: invalid_tool_name"}`; execution errors are "reported in tool results with `isError: true`". ([Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md))

**SOURCE FACT.** "Clients **MAY** provide protocol errors to language models, though these are less likely to result in successful recovery. Clients **SHOULD** provide tool execution errors to language models to enable self-correction." ([Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md))

**SOURCE FACT.** SEP-1303 is the origin of the split: "This SEP proposes treating tools input validation errors as Tool Execution Errors rather than Protocol Errors." ([SEP-1303: Input Validation Errors as Tool Execution Errors](https://modelcontextprotocol.io/seps/1303-input-validation-errors-as-tool-execution-errors))

**SOURCE FACT.** "Protocol Errors are catch at the application level by the MCP Client. Only Tool Execution Errors are forwarded back to the model as JSON-RPC responses." ([SEP-1303](https://modelcontextprotocol.io/seps/1303-input-validation-errors-as-tool-execution-errors))

**SOURCE FACT.** The SEP's worked example returns `"isError": true` with the text "Dates must be in the future. Current date is 08/08/2025", after which "Model understands the error and corrects itself". ([SEP-1303](https://modelcontextprotocol.io/seps/1303-input-validation-errors-as-tool-execution-errors))

**SOURCE FACT (resource errors).** "If the requested resource does not exist, servers **MUST** return a JSON-RPC error with code `-32602` (Invalid Params). Servers **SHOULD** return `-32603` for internal errors." and "Servers **MUST NOT** return an empty `contents` array for a non-existent resource." ([Resources](https://modelcontextprotocol.io/specification/2026-07-28/server/resources.md))

**SOURCE FACT (prompt errors).** "Invalid prompt name: `-32602` (Invalid params)"; "Missing required arguments: `-32602` (Invalid params)"; "Internal errors: `-32603` (Internal error)". ([Prompts](https://modelcontextprotocol.io/specification/2026-07-28/server/prompts.md))

**AI INFERENCE (naming the SEP-1303 and tools error facts).** The design rule is: reserve JSON-RPC errors for things the model cannot fix (unknown tool, malformed request, server fault), and return `isError: true` for anything the model could correct (bad date, out-of-range value, business rule). This is derived from the quoted "less likely to be able to fix" vs "self-correct and retry" distinction and the SEP-1303 forwarding statement.

## 6. Annotations and safety hints

**SOURCE FACT.** "`annotations`: Optional properties describing tool behavior". ([Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md))

**SOURCE FACT.** The `ToolAnnotations` interface defines: "`title`?: string"; "`readOnlyHint`?: boolean — If true, the tool does not modify its environment. Default: false"; "`destructiveHint`?: boolean — If true, the tool may perform destructive updates to its environment. If false, the tool performs only additive updates. (This property is meaningful only when readOnlyHint == false) Default: true"; "`idempotentHint`?: boolean — If true, calling the tool repeatedly with the same arguments will have no additional effect on its environment. ... Default: false"; "`openWorldHint`?: boolean — If true, this tool may interact with an "open world" of external entities. ... Default: true". ([Schema Reference — ToolAnnotations](https://modelcontextprotocol.io/specification/2026-07-28/schema.md))

**SOURCE FACT.** "NOTE: all properties in ToolAnnotations are hints. They are not guaranteed to provide a faithful description of tool behavior (including descriptive properties like title). Clients should never make tool use decisions based on ToolAnnotations received from untrusted servers." ([Schema Reference — ToolAnnotations](https://modelcontextprotocol.io/specification/2026-07-28/schema.md))

**SOURCE FACT.** "For trust & safety and security, clients **MUST** consider tool annotations to be untrusted unless they come from trusted servers." ([Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md))

**SOURCE FACT (resource annotations).** Resources, resource templates and content blocks support "**`audience`**: An array indicating the intended audience(s) ... Valid values are `"user"` and `"assistant"`"; "**`priority`**: A number from 0.0 to 1.0 indicating the importance"; "**`lastModified`**: An ISO 8601 formatted timestamp". ([Resources](https://modelcontextprotocol.io/specification/2026-07-28/server/resources.md))

**AI INFERENCE (naming the annotation facts).** The four tool hints map to a safety contract: `readOnlyHint` and `destructiveHint` describe side effects, `idempotentHint` describes retry safety, and `openWorldHint` describes whether inputs come from an unbounded external space. Because the spec calls them untrusted hints, a server should set them accurately but a client must not rely on them for authorization. This is derived from the quoted defaults and the "untrusted" statements.

## 7. State handles (stateful tools without protocol sessions)

**SOURCE FACT.** "MCP has no protocol-level session, so a server cannot rely on implicit per-connection state to relate one tool call to the next." ([Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md))

**SOURCE FACT.** "Servers that need to maintain state across calls — a shopping cart, an open browser context, a database transaction — should do so by returning an explicit handle from a creation tool and accepting that handle as an argument on subsequent calls." ([Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md))

**SOURCE FACT.** "The protocol has no concept of a state handle; from the wire's perspective a handle is an ordinary string in a tool result and an ordinary argument to subsequent tool calls." ([Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md))

**SOURCE FACT.** Handle design guidance: "**Authorization.** For authenticated servers, a handle is a name, not a capability. The server should validate the caller's authorization against the handle on every call."; "**Opacity.** Handles that encode internal structure invite parsing or guessing; opaque identifiers do not."; "**Lifetime.** ... the server's retention policy should be stated in the creation tool's description"; "**Expiry errors.** A call against an expired or unknown handle should return a tool execution error that says so". ([Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md))

**SOURCE FACT.** For unauthenticated servers "the handle is necessarily a bearer token, it should be generated with sufficient entropy (e.g., a UUIDv4) and given a bounded lifetime." ([Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md))

## 8. Pagination

**SOURCE FACT.** "Pagination in MCP uses an opaque cursor-based approach, instead of numbered pages." and "**Page size** is determined by the server, and clients **MUST NOT** assume a fixed page size". ([Pagination](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/pagination.md))

**SOURCE FACT.** Operations supporting pagination: "`resources/list`", "`resources/templates/list`", "`prompts/list`", "`tools/list`". ([Pagination](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/pagination.md))

**SOURCE FACT.** "Servers **SHOULD**: Provide stable cursors; Handle invalid cursors gracefully." and "Invalid cursors **SHOULD** result in an error with code -32602 (Invalid params)." ([Pagination](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/pagination.md))

**SOURCE FACT.** "Clients **MUST** treat cursors as opaque tokens: Don't make assumptions about cursor format; Don't attempt to parse or modify cursors; Don't make any determination based on cursor value other than whether a non-null value was provided (e.g. an empty string is a valid cursor and thus **MUST NOT** be treated as the end of results)". ([Pagination](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/pagination.md))

## 9. Caching (ttlMs and cacheScope)

**SOURCE FACT.** "Servers MUST include caching hints on results with `resultType: "complete"` returned by the following operations:" — `server/discover`, `tools/list`, `prompts/list`, `resources/list`, `resources/templates/list`, `resources/read`. ([Caching](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching.md))

**SOURCE FACT.** "The **Time-to-live (TTL) Field**, `ttlMs`, is an integer value in milliseconds specifying how long the client MAY consider the result fresh." and "Servers **MUST** provide a `ttlMs` value that is `>= 0`." ([Caching](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching.md))

**SOURCE FACT.** "The **Cache Scope Field**, `cacheScope`, indicates the intended scope of the cached response, either `"public"` or `"private"`." — `"public"` means "The response does not contain user-specific data"; `"private"` means "The response contains private data that is not meant to be shared between callers." ([Caching](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching.md))

**SOURCE FACT.** "Servers **MUST** apply the same `cacheScope` to all response pages for a given list request." ([Caching](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching.md))

**SOURCE FACT (security).** "Servers MUST be aware that responses with a `"public"` `cacheScope` may be shared between callers even if the Result is coming from an authenticated endpoint." and "MUST NOT rely on `cacheScope` alone to prevent unauthorized access to primitives." ([Caching](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching.md))

**SOURCE FACT (notifications).** "When a relevant notification is received while a cached response is still fresh, the notification **invalidates** the cached response and it should be considered immediately stale." ([Caching](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching.md))

**AI INFERENCE (naming the caching facts).** The caching model is HTTP-like: `ttlMs` is analogous to `Cache-Control: max-age` and `cacheScope` to `public`/`private`. A server that returns user-filtered lists must mark them `private`, and a server that returns identical lists for all callers may mark them `public`; the spec's warning means `public` is a data-classification claim, not an access-control mechanism. This is derived from the quoted field definitions and the "MUST NOT rely on cacheScope alone" statement.

## 10. Multi Round-Trip Requests (MRTR) and elicitation

**SOURCE FACT.** "Multi Round-Trip Requests (MRTR) was introduced in this version of the MCP specification. This replaces the previous approach of sending server-initiated requests. Servers **MUST** send server-to-client requests (such as `roots/list`, `sampling/createMessage`, or `elicitation/create`) using the MRTR pattern. The previous pattern of server-initiated requests is no longer supported. This is a breaking change." ([Multi Round-Trip Requests](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr.md))

**SOURCE FACT.** "it allows servers to request additional information without maintaining any server-side state. The server encodes any needed context into the `requestState` field, which the client echoes back on retry." ([MRTR](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr.md))

**SOURCE FACT.** Supported requests: "Servers **MAY** send `InputRequiredResult` responses on the following client requests:" — `prompts/get`, `resources/read`, `tools/call`; "Servers **MUST NOT** send `InputRequiredResult` responses on any other client requests." ([MRTR](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr.md))

**SOURCE FACT (security).** "If a client request contains a `requestState` field, servers **MUST** treat `requestState` as an attacker-controlled input. If `requestState` influences authorization, resource access, or business logic, servers **MUST** protect its integrity (e.g. HMAC or AEAD) and **MUST** reject state that fails verification." ([MRTR](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr.md))

**SOURCE FACT.** "Servers **MUST NOT** send an `inputRequests` that the client has not declared support for in its capabilities." ([MRTR](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr.md))

**SOURCE FACT.** "The JSON-RPC `id` **MUST** be different between the initial request and the retry, as they are independent requests." ([MRTR](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr.md))

**SOURCE FACT (tools).** "Servers **MAY** respond to `tools/call` with an [`InputRequiredResult`] to indicate that additional input is needed before the tool call can be completed." ([Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md))

**AI INFERENCE (naming the MRTR facts).** MRTR is the stateless replacement for server-initiated requests: instead of the server holding a pending request and pushing a `sampling`/`elicitation` call, it returns `input_required` with the request embedded, and the client retries with `inputResponses` plus an echoed `requestState`. Because `requestState` round-trips through the client, it must be integrity-protected whenever it carries authorization or business meaning. This is derived from the quoted "no longer supported", "without maintaining any server-side state", and "attacker-controlled input" statements.

## 11. Progressive discovery and code mode

**SOURCE FACT.** "Loading every tool definition into the model's context window upfront wastes tokens, increases latency, and degrades model performance." ([Client Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices))

**SOURCE FACT.** "The host provides a lightweight `search_tools` meta-tool to the model." and "The host loads full definitions into context only as needed." ([Client Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices))

**SOURCE FACT.** The three-layer pattern is "**Layer 1: Catalog.** ... a `search_tools` tool accepts a natural-language query and returns matching tool names with brief descriptions."; "**Layer 2: Inspect.** ... it fetches the full definition (input schema, output schema, documentation) for that tool only."; "**Layer 3: Execute.** The model calls the tool with full knowledge of its interface". ([Client Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices))

**SOURCE FACT.** "Programmatic tool calling (sometimes called "code mode") provides a way for clients to **compose tool calls** effectively. Instead of calling tools directly, the model writes code that calls tools. The code executes in a sandboxed environment, and only the final result returns to the model." ([Client Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices))

**SOURCE FACT.** "MCP tool errors arrive as a successful response with [`isError: true`] rather than a transport failure. Generated wrappers should convert this into a thrown exception so model-authored code can use `try`/`catch`." ([Client Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices))

**SOURCE FACT (server-side implication).** "MCP Servers can provide an optional `outputSchema` for each tool. When an output schema is present, the host can produce precise return types". ([Client Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices))

**SOURCE FACT (prompt caching).** "Adding or removing tool definitions mid-conversation invalidates that cache, and the resulting miss can cost more tokens than the definitions you removed." ([Client Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices))

**AI INFERENCE (naming the discovery and code-mode facts).** Progressive discovery and code mode are client-side patterns, but they impose server-side design constraints: accurate `description` fields make keyword/embedding search work, `outputSchema` makes typed code generation possible, and deterministic tool ordering plus stable definitions preserve prompt caching. This is derived from the quoted search-layer, output-schema, and prompt-cache statements.

## 12. Idempotency and safety hints (synthesis)

**SOURCE FACT.** `idempotentHint` is defined as "If true, calling the tool repeatedly with the same arguments will have no additional effect on its environment." with "Default: false". ([Schema Reference — ToolAnnotations](https://modelcontextprotocol.io/specification/2026-07-28/schema.md))

**SOURCE FACT.** `readOnlyHint` defaults to `false` and `destructiveHint` defaults to `true`. ([Schema Reference — ToolAnnotations](https://modelcontextprotocol.io/specification/2026-07-28/schema.md))

**SOURCE FACT.** "Servers **MUST**: Validate all tool inputs; Implement proper access controls; Rate limit tool invocations; Sanitize tool outputs." ([Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md))

**SOURCE FACT.** "Clients **SHOULD**: Prompt for user confirmation on sensitive operations; Show tool inputs to the user before calling the server ...; Validate tool results before passing to LLM; ... Implement timeouts for tool calls; Log tool usage for audit purposes." ([Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md))

**AI INFERENCE (naming the hint-default and security facts).** Because `readOnlyHint` defaults to `false` and `destructiveHint` to `true`, a server that omits annotations is signalling "assume this mutates and may destroy". A read-only server should therefore set `readOnlyHint: true` explicitly to avoid unnecessary confirmation friction, and a retry-safe mutating tool should set `idempotentHint: true`. This is derived from the quoted defaults and the client-confirmation guidance.

## Retrieval log

| URL | Result |
|-----|--------|
| https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md | Retrieved |
| https://modelcontextprotocol.io/specification/2026-07-28/server/resources.md | Retrieved |
| https://modelcontextprotocol.io/specification/2026-07-28/server/prompts.md | Retrieved |
| https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching.md | Retrieved |
| https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/pagination.md | Retrieved |
| https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr.md | Retrieved |
| https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices | Retrieved |
| https://modelcontextprotocol.io/seps/986-specify-format-for-tool-names | Retrieved |
| https://modelcontextprotocol.io/seps/1303-input-validation-errors-as-tool-execution-errors | Retrieved |
| https://modelcontextprotocol.io/seps/2106-json-schema-2020-12 | Retrieved |
| https://modelcontextprotocol.io/specification/2026-07-28/schema.md | Retrieved (used for ToolAnnotations) |
