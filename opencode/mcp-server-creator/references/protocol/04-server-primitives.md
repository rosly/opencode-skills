# MCP Server Primitives and Server-Side Utilities (Revision 2026-07-28)

Research file for the report on MCP servers for LLM agents. All externally sourced facts below carry a short exact quotation and an inline link to the source URL in the same sentence. Notation used: **SOURCE FACT**, **SOURCE CLAIM (rank)**, **AI INFERENCE**, **PLAUSIBLE NOT VERIFIED**, **UNKNOWN**.

## 1. Overview: the three server primitives

**SOURCE FACT** — The server overview page states that servers expose three primitives: "**Prompts**: Pre-defined templates or instructions that guide language model interactions", "**Resources**: Structured data or content that provides additional context to the model", and "**Tools**: Executable functions that allow models to perform actions or retrieve information" ([server/index.md](https://modelcontextprotocol.io/specification/2026-07-28/server/index.md)).

**SOURCE FACT** — The control hierarchy is given as a table: "Prompts | User-controlled | Interactive templates invoked by user choice", "Resources | Application-controlled | Contextual data attached and managed by the client", and "Tools | Model-controlled | Functions exposed to the LLM to take actions" ([server/index.md](https://modelcontextprotocol.io/specification/2026-07-28/server/index.md)).

**AI INFERENCE** — Based on the quoted control hierarchy, the three primitives differ in *who decides invocation*: the user (prompts), the host application (resources), and the model (tools). This is a design framing, not a wire-level constraint.

## 2. `server/discover`

**SOURCE FACT** — Discovery is a mandatory server RPC: "`server/discover` lets a client query a server's supported protocol versions, capabilities, and identity before sending any other requests. Servers **MUST** implement it." ([server/discover.md](https://modelcontextprotocol.io/specification/2026-07-28/server/discover.md)).

**SOURCE FACT** — The request "carries no body parameters beyond the standard `_meta`", and the example `_meta` includes `"io.modelcontextprotocol/protocolVersion": "2026-07-28"`, `clientInfo`, and `clientCapabilities` ([server/discover.md](https://modelcontextprotocol.io/specification/2026-07-28/server/discover.md)).

**SOURCE FACT** — The response includes `supportedVersions`, `capabilities`, `_meta['io.modelcontextprotocol/serverInfo']`, `instructions`, and caching hints; the example shows `"ttlMs": 3600000` and `"cacheScope": "public"` ([server/discover.md](https://modelcontextprotocol.io/specification/2026-07-28/server/discover.md)).

**SOURCE FACT** — Calling it is optional for clients: "Calling `server/discover` is optional for clients — a client may invoke any RPC inline and handle `UnsupportedProtocolVersionError` if the server does not support the requested version." ([server/discover.md](https://modelcontextprotocol.io/specification/2026-07-28/server/discover.md)).

**SOURCE FACT** — It is recommended as a stdio backward-compatibility probe: "On stdio, there is no per-request HTTP status code to drive fallback. A client that supports both modern (per-request `_meta`) and legacy (`initialize` handshake) servers **SHOULD** send `server/discover` first" ([server/discover.md](https://modelcontextprotocol.io/specification/2026-07-28/server/discover.md)).

**SOURCE FACT** — `serverInfo` is untrusted: "`serverInfo` is self-reported by the server and is not verified by the protocol. It is intended for display, logging, and debugging. Clients **SHOULD NOT** use it to change their behavior, and **SHOULD NOT** rely on it for security decisions." ([server/discover.md](https://modelcontextprotocol.io/specification/2026-07-28/server/discover.md)).

**SOURCE FACT** — `DiscoverResult` fields are enumerated: "`supportedVersions`: Protocol versions the server supports", "`capabilities`: Capabilities the server supports (tools, resources, prompts, etc.)", "`_meta['io.modelcontextprotocol/serverInfo']`: Name and version of the server software. Servers **SHOULD** include this field.", and "`instructions`: Optional natural-language guidance for LLMs on how to use this server effectively" ([server/discover.md](https://modelcontextprotocol.io/specification/2026-07-28/server/discover.md)).

## 3. Tools

### 3.1 What it is and capability

**SOURCE FACT** — "The Model Context Protocol (MCP) allows servers to expose tools that can be invoked by language models. Tools enable models to interact with external systems, such as querying databases, calling APIs, or performing computations." ([server/tools.md](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md)).

**SOURCE FACT** — Tools are model-controlled: "Tools in MCP are designed to be **model-controlled**, meaning that the language model can discover and invoke tools automatically based on its contextual understanding and the user's prompts." ([server/tools.md](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md)).

**SOURCE FACT** — Capability declaration: "Servers that support tools **MUST** declare the `tools` capability", with `"listChanged": true` indicating "whether the server will emit notifications when the list of available tools changes" ([server/tools.md](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md)).

**SOURCE FACT** — Deterministic ordering is required: "Servers **SHOULD** return tools in a deterministic order (i.e., the same ordering across requests when the underlying set of tools has not changed). Deterministic ordering enables clients to reliably cache the tool list and improves LLM prompt cache hit rates when tools are included in model context." ([server/tools.md](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md)).

### 3.2 RPC methods

**SOURCE FACT** — Listing uses `tools/list` and "This operation supports pagination and caching." ([server/tools.md](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md)). The list response example includes `"nextCursor"`, `"ttlMs": 300000`, and `"cacheScope": "public"` ([server/tools.md](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md)).

**SOURCE FACT** — Invocation uses `tools/call`: "To invoke a tool, clients send a `tools/call` request" ([server/tools.md](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md)).

**SOURCE FACT** — Change notification is `notifications/tools/list_changed`, sent to clients that opened a `subscriptions/listen` stream with `toolsListChanged: true` ([server/tools.md](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md)).

### 3.3 Schema and shape

**SOURCE FACT** — A tool definition includes "`name`: Unique identifier for the tool", "`title`: Optional human-readable name of the tool for display purposes.", "`description`: Human-readable description of functionality", "`icons`: Optional array of icons for display in user interfaces", "`inputSchema`: JSON Schema defining expected parameters", "`outputSchema`: Optional JSON Schema defining expected output structure", and "`annotations`: Optional properties describing tool behavior" ([server/tools.md](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md)).

**SOURCE FACT** — `inputSchema` rules: "Defaults to 2020-12 if no `$schema` field is present", "**MUST** be a valid JSON Schema object (not `null`)", and for no-parameter tools the recommended form is `{ "type": "object", "additionalProperties": false }` ([server/tools.md](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md)).

**SOURCE FACT** — Tool names: "Tool names **SHOULD** be between 1 and 128 characters in length (inclusive)", "**SHOULD** be considered case-sensitive", and allowed characters are "uppercase and lowercase ASCII letters (A-Z, a-z), digits (0-9), underscore (\_), hyphen (-), and dot (.)" ([server/tools.md](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md)).

**SOURCE FACT** — Uniqueness is per-server: "Tool name uniqueness is scoped to a single server. Clients or proxies that aggregate tools from multiple servers **MAY** encounter naming collisions ... and **SHOULD** implement a disambiguation strategy such as prefixing tool names with a server identifier." ([server/tools.md](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md)).

### 3.4 `x-mcp-header`

**SOURCE FACT** — "The `x-mcp-header` extension property allows servers to designate specific tool parameters to be mirrored into HTTP headers when using the Streamable HTTP transport." ([server/tools.md](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md)).

**SOURCE FACT** — Constraints include "**MUST NOT** be empty", "**MUST** match HTTP field-name token syntax (`1*tchar`, RFC 9110 Section 5.1)", "**MUST** be case-insensitively unique among all `x-mcp-header` values in the `inputSchema`", and "**MUST** only be applied to parameters with primitive types (integer, string, boolean). Parameters with type `number` are not permitted." ([server/tools.md](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md)).

**SOURCE FACT** — Security warning: "Server developers **SHOULD NOT** mark sensitive parameters (passwords, API keys, tokens, PII) with `x-mcp-header`, as header values are visible to network intermediaries." ([server/tools.md](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md)).

### 3.5 Results, structured content, resource links

**SOURCE FACT** — "Tool results may contain **structured** or **unstructured** content." Unstructured content is returned in the `content` field and "can contain multiple content items of different types" ([server/tools.md](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md)).

**SOURCE FACT** — Content types include text, image, audio, resource links, and embedded resources; "All content types (text, image, audio, resource links, and embedded resources) support optional annotations that provide metadata about audience, priority, and modification times." ([server/tools.md](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md)).

**SOURCE FACT** — Resource links: "A tool **MAY** return links to Resources, to provide additional context or data. In this case, the tool will return a URI that can be subscribed to or fetched by the client" ([server/tools.md](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md)). The example uses `"type": "resource_link"` with `uri`, `name`, `description`, `mimeType` ([server/tools.md](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md)).

**SOURCE FACT** — "Resource links returned by tools are not guaranteed to appear in the results of a `resources/list` request." ([server/tools.md](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md)).

**SOURCE FACT** — Structured content: "**Structured** content is returned as a JSON value in the `structuredContent` field of a result. This can be any JSON value (object, array, string, number, boolean, or null) that conforms to the tool's `outputSchema` if one is defined." ([server/tools.md](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md)).

**SOURCE FACT** — Backward compatibility: "For backwards compatibility, a tool that returns structured content SHOULD also return the serialized JSON in a TextContent block." ([server/tools.md](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md)).

**SOURCE FACT** — Clarification: "`structuredContent` is server-produced result data and is unrelated to LLM 'structured outputs' (schema-constrained model generation)." ([server/tools.md](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md)).

**SOURCE FACT** — Output schema obligations: "Servers **MUST** provide structured results that conform to this schema." and "Clients **SHOULD** validate structured results against this schema." ([server/tools.md](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md)).

### 3.6 Annotations/hints

**SOURCE FACT** — "For trust & safety and security, clients **MUST** consider tool annotations to be untrusted unless they come from trusted servers." ([server/tools.md](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md)).

**SOURCE FACT** — The tools page describes `annotations` only as "Optional properties describing tool behavior" and does not enumerate specific hint keys on this page ([server/tools.md](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md)). **UNKNOWN** — The exact annotation keys (e.g. `readOnlyHint`, `destructiveHint`) are not quoted on the fetched tools page; they would need the schema page, which was not in the fetch list.

### 3.7 Input-required (MRTR) and errors

**SOURCE FACT** — "Servers **MAY** respond to `tools/call` with an `InputRequiredResult` to indicate that additional input is needed before the tool call can be completed." ([server/tools.md](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md)).

**SOURCE FACT** — "Note that the JSON-RPC `id` **MUST** be different between the initial request and the retry." ([server/tools.md](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md)).

**SOURCE FACT** — Two error mechanisms: "**Protocol Errors** indicate issues with the request structure itself" returned as standard JSON-RPC errors, and "**Tool Execution Errors** contain actionable feedback that language models can use to self-correct and retry with adjusted parameters" reported with `isError: true` ([server/tools.md](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md)).

**SOURCE FACT** — "Clients **SHOULD** provide tool execution errors to language models to enable self-correction." ([server/tools.md](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md)).

### 3.8 Stateful tools

**SOURCE FACT** — "MCP has no protocol-level session, so a server cannot rely on implicit per-connection state to relate one tool call to the next." Servers needing state "should do so by returning an explicit handle from a creation tool and accepting that handle as an argument on subsequent calls." ([server/tools.md](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md)).

**SOURCE FACT** — This section is explicitly non-normative: "This section is non-normative guidance for tool design. The protocol has no concept of a state handle; from the wire's perspective a handle is an ordinary string in a tool result and an ordinary argument to subsequent tool calls." ([server/tools.md](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md)).

## 4. Resources

### 4.1 What it is and capability

**SOURCE FACT** — "The Model Context Protocol (MCP) provides a standardized way for servers to expose resources to clients. Resources allow servers to share data that provides context to language models, such as files, database schemas, or application-specific information. Each resource is uniquely identified by a URI." ([server/resources.md](https://modelcontextprotocol.io/specification/2026-07-28/server/resources.md)).

**SOURCE FACT** — Resources are application-driven: "Resources in MCP are designed to be **application-driven**, with host applications determining how to incorporate context based on their needs." ([server/resources.md](https://modelcontextprotocol.io/specification/2026-07-28/server/resources.md)).

**SOURCE FACT** — Capability: "Servers that support resources **MUST** declare the `resources` capability", with optional `listChanged` and `subscribe` features; "Servers may advertise either feature independently, together or neither." ([server/resources.md](https://modelcontextprotocol.io/specification/2026-07-28/server/resources.md)).

### 4.2 RPC methods

**SOURCE FACT** — `resources/list` "supports pagination and caching"; `resources/read` "supports caching"; `resources/templates/list` "supports pagination and caching" ([server/resources.md](https://modelcontextprotocol.io/specification/2026-07-28/server/resources.md)).

**SOURCE FACT** — "Servers **MAY** return multiple resource contents in response to a single `resources/read` request. For example, a server could return the contents of several files when a directory resource is read." ([server/resources.md](https://modelcontextprotocol.io/specification/2026-07-28/server/resources.md)).

**SOURCE FACT** — "Servers **MAY** also respond to `resources/read` with an `InputRequiredResult` to indicate that additional input is needed before the resource can be read." ([server/resources.md](https://modelcontextprotocol.io/specification/2026-07-28/server/resources.md)).

**SOURCE FACT** — Change notification is `notifications/resources/list_changed`; subscriptions use `subscriptions/listen` with `notifications.resourceSubscriptions`, delivering `notifications/resources/updated` ([server/resources.md](https://modelcontextprotocol.io/specification/2026-07-28/server/resources.md)).

### 4.3 Schema and shape

**SOURCE FACT** — A resource definition includes "`uri`: Unique identifier for the resource", "`name`: The name of the resource.", "`title`: Optional human-readable name of the resource for display purposes.", "`description`: Optional description", "`icons`: Optional array of icons for display in user interfaces", "`mimeType`: Optional MIME type", and "`size`: Optional size in bytes" ([server/resources.md](https://modelcontextprotocol.io/specification/2026-07-28/server/resources.md)).

**SOURCE FACT** — Resource contents are text or binary: text uses `text`, binary uses `blob` with "base64-encoded-data" ([server/resources.md](https://modelcontextprotocol.io/specification/2026-07-28/server/resources.md)).

**SOURCE FACT** — Resource templates use URI templates: "Resource templates allow servers to expose parameterized resources using URI templates. Arguments may be auto-completed through the completion API." ([server/resources.md](https://modelcontextprotocol.io/specification/2026-07-28/server/resources.md)).

### 4.4 Annotations

**SOURCE FACT** — "Resources, resource templates and content blocks support optional annotations that provide hints to clients about how to use or display the resource" ([server/resources.md](https://modelcontextprotocol.io/specification/2026-07-28/server/resources.md)).

**SOURCE FACT** — Annotation keys: "**`audience`**: An array indicating the intended audience(s) for this resource. Valid values are `"user"` and `"assistant"`."; "**`priority`**: A number from 0.0 to 1.0 indicating the importance of this resource."; "**`lastModified`**: An ISO 8601 formatted timestamp indicating when the resource was last modified" ([server/resources.md](https://modelcontextprotocol.io/specification/2026-07-28/server/resources.md)).

### 4.5 URI schemes and errors

**SOURCE FACT** — Standard schemes include `https://`, `file://`, and `git://`; "Custom URI schemes **MUST** be in accordance with RFC3986" ([server/resources.md](https://modelcontextprotocol.io/specification/2026-07-28/server/resources.md)).

**SOURCE FACT** — Error handling: "If the requested resource does not exist, servers **MUST** return a JSON-RPC error with code `-32602` (Invalid Params). Servers **SHOULD** return `-32603` for internal errors." and "For backwards compatibility, clients **SHOULD** also accept `-32002` as a resource not found error" ([server/resources.md](https://modelcontextprotocol.io/specification/2026-07-28/server/resources.md)).

**SOURCE FACT** — "Servers **MUST NOT** return an empty `contents` array for a non-existent resource. An empty array is ambiguous—it could mean the resource exists but has no content, or that it doesn't exist at all." ([server/resources.md](https://modelcontextprotocol.io/specification/2026-07-28/server/resources.md)).

## 5. Prompts

### 5.1 What it is and capability

**SOURCE FACT** — "The Model Context Protocol (MCP) provides a standardized way for servers to expose prompt templates to clients. Prompts allow servers to provide structured messages and instructions for interacting with language models." ([server/prompts.md](https://modelcontextprotocol.io/specification/2026-07-28/server/prompts.md)).

**SOURCE FACT** — Prompts are user-controlled: "Prompts are designed to be **user-controlled**, meaning they are exposed from servers to clients with the intention of the user being able to explicitly select them for use. This refers to who decides when the prompt is used, not who authors its content. Prompt content is defined by the server." ([server/prompts.md](https://modelcontextprotocol.io/specification/2026-07-28/server/prompts.md)).

**SOURCE FACT** — Capability: "Servers that support prompts **MUST** declare the `prompts` capability in their `DiscoverResult`", with `listChanged` indicating change notifications ([server/prompts.md](https://modelcontextprotocol.io/specification/2026-07-28/server/prompts.md)).

### 5.2 RPC methods

**SOURCE FACT** — `prompts/list` "supports pagination and caching"; `prompts/get` retrieves a specific prompt and "Arguments may be auto-completed through the completion API." ([server/prompts.md](https://modelcontextprotocol.io/specification/2026-07-28/server/prompts.md)).

**SOURCE FACT** — "Servers **MAY** also respond to `prompts/get` with an `InputRequiredResult` to indicate that additional input is needed before the prompt can be resolved." ([server/prompts.md](https://modelcontextprotocol.io/specification/2026-07-28/server/prompts.md)).

**SOURCE FACT** — Change notification is `notifications/prompts/list_changed`, sent to clients with a `subscriptions/listen` stream with `promptsListChanged: true` ([server/prompts.md](https://modelcontextprotocol.io/specification/2026-07-28/server/prompts.md)).

### 5.3 Schema and shape

**SOURCE FACT** — A prompt definition includes "`name`: Unique identifier for the prompt", "`title`: Optional human-readable name of the prompt for display purposes.", "`description`: Optional human-readable description", "`icons`: Optional array of icons for display in user interfaces", and "`arguments`: Optional list of arguments for customization" ([server/prompts.md](https://modelcontextprotocol.io/specification/2026-07-28/server/prompts.md)).

**SOURCE FACT** — `PromptMessage` has "`role`: Either "user" or "assistant" to indicate the speaker" and `content`, which may be text, image, audio, resource links, or embedded resources ([server/prompts.md](https://modelcontextprotocol.io/specification/2026-07-28/server/prompts.md)).

**SOURCE FACT** — "All content types in prompt messages support optional annotations for metadata about audience, priority, and modification times." ([server/prompts.md](https://modelcontextprotocol.io/specification/2026-07-28/server/prompts.md)).

**SOURCE FACT** — Error handling: "Invalid prompt name: `-32602` (Invalid params)", "Missing required arguments: `-32602` (Invalid params)", "Internal errors: `-32603` (Internal error)" ([server/prompts.md](https://modelcontextprotocol.io/specification/2026-07-28/server/prompts.md)).

## 6. Server utility: Completion

**SOURCE FACT** — "The Model Context Protocol (MCP) provides a standardized way for servers to offer autocompletion suggestions for the arguments of prompts and resource templates." ([server/utilities/completion.md](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/completion.md)).

**SOURCE FACT** — Capability: "Servers that support completions **MUST** declare the `completions` capability" ([server/utilities/completion.md](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/completion.md)).

**SOURCE FACT** — RPC method is `completion/complete`, with two reference types: "`ref/prompt` | References a prompt by name" and "`ref/resource` | References a resource URI or URI template" ([server/utilities/completion.md](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/completion.md)).

**SOURCE FACT** — "Servers return an array of completion values ranked by relevance, with: Maximum 100 items per response, Optional total number of available matches, Boolean indicating if additional results exist" ([server/utilities/completion.md](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/completion.md)).

**SOURCE FACT** — `CompleteResult` contains `completion` with "`values`: Array of suggestions (max 100)", "`total`: Optional total matches", and "`hasMore`: Additional results flag" ([server/utilities/completion.md](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/completion.md)).

## 7. Server utility: Logging (deprecated)

**SOURCE FACT** — "**Deprecated**: The Logging feature is deprecated as of protocol version `2026-07-28` (SEP-2577). Under the feature lifecycle policy, it remains in the specification for at least twelve months after this revision's release before it becomes eligible for removal. New implementations **SHOULD NOT** adopt it; existing implementations **SHOULD** migrate to logging to `stderr` for stdio transports, or to OpenTelemetry for structured observability." ([server/utilities/logging.md](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/logging.md)).

**SOURCE FACT** — "The Model Context Protocol (MCP) provides a standardized way for servers to send structured log messages to clients. Clients control logging verbosity per-request via `_meta`, with servers sending notifications containing severity levels, optional logger names, and arbitrary JSON-serializable data." ([server/utilities/logging.md](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/logging.md)).

**SOURCE FACT** — Capability: "Servers that emit log message notifications **MUST** declare the `logging` capability" ([server/utilities/logging.md](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/logging.md)).

**SOURCE FACT** — Log levels follow syslog/RFC 5424: debug, info, notice, warning, error, critical, alert, emergency ([server/utilities/logging.md](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/logging.md)).

**SOURCE FACT** — Per-request level: "To receive log messages for a specific request, include `io.modelcontextprotocol/logLevel` in the request's `_meta`. The server **MUST NOT** emit `notifications/message` for a request that does not include this field." ([server/utilities/logging.md](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/logging.md)).

**SOURCE FACT** — Request scoping: "`notifications/message` is request-scoped: the server **MUST NOT** deliver it on a `subscriptions/listen` stream or on any stream other than the one carrying the response to the request that set the log level." ([server/utilities/logging.md](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/logging.md)).

**SOURCE FACT** — The notification method is `notifications/message` with `level`, `logger`, and `data` ([server/utilities/logging.md](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/logging.md)).

## 8. Server utility: Pagination

**SOURCE FACT** — "Pagination in MCP uses an opaque cursor-based approach, instead of numbered pages." with "The **cursor** is an opaque string token, representing a position in the result set" and "**Page size** is determined by the server, and clients **MUST NOT** assume a fixed page size" ([server/utilities/pagination.md](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/pagination.md)).

**SOURCE FACT** — Operations supporting pagination: "`resources/list` - List available resources", "`resources/templates/list` - List resource templates", "`prompts/list` - List available prompts", "`tools/list` - List available tools" ([server/utilities/pagination.md](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/pagination.md)).

**SOURCE FACT** — "Clients **MUST** treat cursors as opaque tokens: Don't make assumptions about cursor format, Don't attempt to parse or modify cursors, Don't make any determination based on cursor value other than whether a non-null value was provided (e.g. an empty string is a valid cursor and thus **MUST NOT** be treated as the end of results)" ([server/utilities/pagination.md](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/pagination.md)).

**SOURCE FACT** — "Invalid cursors **SHOULD** result in an error with code -32602 (Invalid params)." ([server/utilities/pagination.md](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/pagination.md)).

## 9. Server utility: Caching

**SOURCE FACT** — "Servers MUST include caching hints on results with `resultType: "complete"` returned by the following operations: `server/discover`, `tools/list`, `prompts/list`, `resources/list`, `resources/templates/list`, `resources/read`." ([server/utilities/caching.md](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching.md)).

**SOURCE FACT** — "Interim results with `resultType: "input_required"` ... are not cacheable and carry no caching hints." ([server/utilities/caching.md](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching.md)).

**SOURCE FACT** — Cache key: "A cached response is identified by the request method together with the request parameters that affect the result (for example, the `uri` for `resources/read`, or the `cursor` for paginated list requests). Clients **MUST NOT** serve a cached response for a request whose method or parameters differ from the request that produced it." ([server/utilities/caching.md](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching.md)).

**SOURCE FACT** — MRTR results are not cacheable: "Results produced by retrying a request through the multi round-trip requests mechanism—that is, requests carrying `inputResponses` or `requestState`—**MUST NOT** be cached, as they depend on inputs that are not part of the cache key." ([server/utilities/caching.md](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching.md)).

**SOURCE FACT** — `ttlMs`: "The **Time-to-live (TTL) Field**, `ttlMs`, is an integer value in milliseconds specifying how long the client MAY consider the result fresh." and "Semantics are analogous to HTTP `Cache-Control: max-age`." ([server/utilities/caching.md](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching.md)).

**SOURCE FACT** — TTL edge cases: "If `ttlMs` is `0`, the response **SHOULD** be considered immediately stale."; "If `ttlMs` is absent, clients **SHOULD** assume a default of `0` (immediately stale)"; "If `ttlMs` is negative, clients **SHOULD** ignore it and treat it as `0`."; "Servers **MUST** provide a `ttlMs` value that is `>= 0`." ([server/utilities/caching.md](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching.md)).

**SOURCE FACT** — "TTL is a **freshness hint**, not a guarantee. Servers MAY change the underlying data before the TTL expires." ([server/utilities/caching.md](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching.md)).

**SOURCE FACT** — Freshness formula: "A client records the local time at which the response was received (`t_received`). The response is considered **fresh** while: `now < t_received + ttlMs`" ([server/utilities/caching.md](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching.md)).

**SOURCE FACT** — `cacheScope`: "The **Cache Scope Field**, `cacheScope`, indicates the intended scope of the cached response, either `"public"` or `"private"`." ([server/utilities/caching.md](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching.md)).

**SOURCE FACT** — Scope meanings: "`"public"` | The response does not contain user-specific data. Any client, shared gateway, or caching proxy **MAY** store and serve the cached response to any user."; "`"private"` | The response contains private data that is not meant to be shared between callers. Cached responses **MAY** be reused for the same authorization context. Caches **MUST NOT** be shared across authorization contexts" ([server/utilities/caching.md](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching.md)).

**SOURCE FACT** — Notification interaction: "When a relevant notification is received while a cached response is still fresh, the notification **invalidates** the cached response and it should be considered immediately stale." ([server/utilities/caching.md](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching.md)).

**SOURCE FACT** — Pagination interaction: "When a list result is paginated, each page is an independently cacheable response"; "Servers **MUST** apply the same `cacheScope` to all response pages for a given list request." ([server/utilities/caching.md](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching.md)).

**SOURCE FACT** — Security: "Servers MUST be aware that responses with a `"public"` `cacheScope` may be shared between callers even if the Result is coming from an authenticated endpoint." and "MUST NOT rely on `cacheScope` alone to prevent unauthorized access to primitives." ([server/utilities/caching.md](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching.md)).

## 10. Cross-cutting summary table

| Primitive | Capability flag | List RPC | Get/Call RPC | Pagination | Caching | Change notification |
| - | - | - | - | - | - | - |
| Tools | `tools` (`listChanged`) | `tools/list` | `tools/call` | Yes | Yes | `notifications/tools/list_changed` |
| Resources | `resources` (`listChanged`, `subscribe`) | `resources/list`, `resources/templates/list` | `resources/read` | Yes | Yes | `notifications/resources/list_changed`, `notifications/resources/updated` |
| Prompts | `prompts` (`listChanged`) | `prompts/list` | `prompts/get` | Yes | Yes | `notifications/prompts/list_changed` |
| Completion | `completions` | — | `completion/complete` | No | No | — |
| Logging (deprecated) | `logging` | — | `notifications/message` | No | No | — |
| Discovery | — | — | `server/discover` | No | Yes | — |

**AI INFERENCE** — The table is assembled from the quoted capability, RPC, pagination, and caching statements above; it introduces no new facts.

## 11. Retrieval notes

All nine requested URLs were retrieved successfully as `.md` endpoints on 2026-10-02. No failed retrievals. The exact annotation hint keys for tools (e.g. `readOnlyHint`) were not present on the fetched `server/tools.md` page and are marked **UNKNOWN** above.
