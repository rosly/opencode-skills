# MCP Server and Client Best Practices (Protocol Revision 2026-07-28)

Research file. Retrieved: 2026-10-02. Protocol revision referenced throughout: **2026-07-28**. Roadmap page last updated **2026-08-22**.

## Notation and evidence ranking

- **SOURCE FACT** — a normative statement quoted verbatim from an official specification/SEP or official documentation page.
- **SOURCE CLAIM (Rank N)** — a non-normative statement quoted verbatim. Ranks: **Rank A** = Final/Standards-Track SEP or normative specification text; **Rank B** = official documentation page (editorial guidance); **Rank C** = roadmap/project-status page.
- **AI INFERENCE** — my reasoning that names the specific quoted facts it is derived from.
- **PLAUSIBLE NOT VERIFIED** — a conjecture consistent with sources but not directly stated.
- **UNKNOWN** — no source retrieved or source is silent.

Quotations are short and exact. Every externally sourced fact carries an inline link to the source URL. No end-only bibliography is used. All eight requested URLs for this file were retrieved successfully; there are no failed retrievals for FILE 2.

## 1. Server development workflow and capability model

**SOURCE FACT.** "MCP servers can provide three main types of capabilities:" — "**[Resources](https://modelcontextprotocol.io/docs/2026-07-28/learn/server-concepts#resources)**: File-like data that can be read by clients (like API responses or file contents)"; "**[Tools](https://modelcontextprotocol.io/docs/2026-07-28/learn/server-concepts#tools)**: Functions that can be called by the LLM (with user approval)"; "**[Prompts](https://modelcontextprotocol.io/docs/2026-07-28/learn/server-concepts#prompts)**: Pre-written templates that help users accomplish specific tasks". ([Build an MCP server](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server))

**SOURCE FACT (workflow shape).** The official server quickstart walks through: install SDK and scaffold a project; import packages and instantiate the server object; write helper functions; "Implementing tool execution"; "Running the server"; then "Testing your server with Claude for Desktop". ([Build an MCP server](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server))

**SOURCE FACT.** The tutorial builds a weather server exposing two tools: "We'll build a server that exposes two tools: `get_alerts` and `get_forecast`." ([Build an MCP server](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server))

**SOURCE FACT.** Tool handlers in Python are declared with the decorator and type-hinted signature, e.g. `@mcp.tool()` above `async def get_alerts(state: str) -> str:`; the docs state "The MCPServer class uses Python type hints and docstrings to automatically generate tool definitions". ([Build an MCP server](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server))

**SOURCE FACT.** In TypeScript the tool registration pattern is `server.registerTool("get_alerts", { description: ..., inputSchema: z.object({...}) }, async ({ state }) => {...})`, using Zod for the input schema. ([Build an MCP server](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server))

## 2. Logging and stdout discipline (a central server rule)

**SOURCE FACT.** "**For STDIO-based servers:** Never write to stdout. Writing to stdout will corrupt the JSON-RPC messages and break your server." ([Build an MCP server](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server))

**SOURCE FACT.** "Use the standard library `logging` module, which writes to stderr." and "Create one logger per module with `logging.getLogger(__name__)` and call it from your tools." ([Build an MCP server](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server))

**SOURCE FACT.** The TypeScript variant states the same rule with different mechanisms: "Never use `console.log()`, as it writes to standard output (stdout) by default." and recommends "`console.error()` which writes to stderr". ([Build an MCP server](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server))

**SOURCE FACT.** "**For HTTP-based servers:** Standard output logging is fine since it doesn't interfere with HTTP responses." ([Build an MCP server](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server))

**AI INFERENCE (naming the stdout facts above).** The stdout prohibition is a transport artifact: stdio carries JSON-RPC on standard output, so any stray write interleaves with protocol frames, whereas HTTP carries messages in the response body and leaves stdout free. This follows directly from the quoted stdout-corruption statements.

## 3. Language and SDK choices

**SOURCE FACT.** The server quickstart provides parallel tabs for **Python**, **TypeScript**, **Java** (Spring AI), **Kotlin**, and **C#**. ([Build an MCP server](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server))

**SOURCE FACT.** "You must use the Python MCP SDK 2.0.0 or higher." and "For this tutorial, you'll need Node.js version 20 or higher." ([Build an MCP server](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server))

**SOURCE FACT.** "SDKs are classified into tiers based on feature completeness, protocol support, and maintenance commitment." ([SDKs](https://modelcontextprotocol.io/docs/2026-07-28/sdk))

**SOURCE FACT.** Tier assignments listed: **Tier 1** — TypeScript, Python, C#, Go, Rust, Ruby; **Tier 2** — Java; **Tier 3** — Swift, PHP, Kotlin. ([SDKs](https://modelcontextprotocol.io/docs/2026-07-28/sdk))

**SOURCE FACT.** "Each SDK provides the same functionality but follows the idioms and best practices of its language. All SDKs support: Creating MCP servers that expose tools, resources, and prompts; Building MCP clients that can connect to any MCP server; Local and remote transport protocols; Protocol compliance with type safety." ([SDKs](https://modelcontextprotocol.io/docs/2026-07-28/sdk))

**AI INFERENCE (naming the tier and quickstart facts).** The quickstart's language coverage (Python, TypeScript, Java, Kotlin, C#) is a subset of the SDK list and does not include the other Tier 1 languages (Go, Rust, Ruby), so "official quickstart exists" is narrower than "official SDK exists". This is derived from the two quoted inventories.

## 4. Client development workflow

**SOURCE FACT.** "In this tutorial, you'll learn how to build an LLM-powered chatbot client that connects to MCP servers." ([Build an MCP client](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-client))

**SOURCE FACT.** The client quickstart also provides Python, TypeScript, Java, Kotlin, and C# tabs, and instructs connecting by launching the server as a subprocess over stdio and listing its tools. ([Build an MCP client](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-client))

**SOURCE FACT.** Connection lifecycle in Python is expressed with `async with Client(stdio_client(server_params(...))) as client:`; the docs state "That `async with` is the entire connection lifecycle." ([Build an MCP client](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-client))

**SOURCE FACT.** Client best practices listed in the quickstart: "**Error Handling** — Check `result.is_error` rather than expecting a failing tool to raise"; "**Resource Management** — Let the `async with` block own the connection"; "**Security** — Store API keys securely in `.env`"; "**Tool Names** — Tool names can be validated according to the format specified [here](https://modelcontextprotocol.io/specification/2026-07-28/server/tools#tool-names)". ([Build an MCP client](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-client))

**SOURCE FACT.** "If a tool name conforms to the specified format, it should not fail validation by an MCP client." ([Build an MCP client](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-client))

## 5. Tool design and naming (SEP-986)

**SOURCE FACT.** "This SEP proposes a clear, flexible standard for tool names: tool names should be 1–64 characters, case-sensitive, and may include alphanumeric characters, underscores (_), dashes (-), dots (.), and forward slashes (/)." ([SEP-986: Specify Format for Tool Names](https://modelcontextprotocol.io/seps/986-specify-format-for-tool-names))

**SOURCE FACT.** The normative list reads: "Tool names SHOULD be between 1 and 64 characters in length (inclusive)."; "Tool names are case-sensitive."; "Allowed characters: uppercase and lowercase ASCII letters (A-Z, a-z), digits (0-9), underscore (_), dash (-), dot (.), and forward slash (/)."; "Tool names SHOULD NOT contain spaces, commas, or other special characters."; "Tool names SHOULD be unique within their namespace." ([SEP-986](https://modelcontextprotocol.io/seps/986-specify-format-for-tool-names))

**SOURCE FACT.** "Example valid tool names: getUser; user-profile/update; DATA_EXPORT_v2; admin.tools.list". ([SEP-986](https://modelcontextprotocol.io/seps/986-specify-format-for-tool-names))

**SOURCE FACT.** Motivation includes "Allow for hierarchical and namespaced tool names (e.g., using / and .)." ([SEP-986](https://modelcontextprotocol.io/seps/986-specify-format-for-tool-names))

**SOURCE FACT.** Backward compatibility: "Existing non-conforming tool names SHOULD be supported as aliases for at least one major version, with a deprecation warning." ([SEP-986](https://modelcontextprotocol.io/seps/986-specify-format-for-tool-names))

**SOURCE CLAIM (Rank A).** SEP-986 metadata: **SEP** 986, **Title** "Specify Format for Tool Names", **Status Final**, **Type Standards Track**, **Created** 2025-07-16, **Author(s)** kentcdodds, **Sponsor** None, **PR** [#986](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/986). ([SEP-986](https://modelcontextprotocol.io/seps/986-specify-format-for-tool-names))

**SOURCE FACT.** "None. Standardizing tool name format does not introduce new security risks." (SEP-986 "Security Implications"). ([SEP-986](https://modelcontextprotocol.io/seps/986-specify-format-for-tool-names))

## 6. Client best practices for scaling across many servers and tools

**SOURCE FACT.** The problem statement: "As MCP host applications, such as agents, connect to more MCP servers and accumulate access to hundreds or thousands of tools, naive approaches to tool management break down. Loading every tool definition into the model's context window upfront wastes tokens, increases latency, and degrades model performance." ([Client Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices))

**SOURCE FACT.** "Two patterns address these challenges: **progressive discovery**, which controls *when* tool definitions enter context, and **programmatic tool calling**, which controls *how* tools are invoked." ([Client Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices))

### 6.1 Progressive tool discovery

**SOURCE FACT.** "The host fetches tool definitions via `tools/list` as normal, but defers injecting them into the model's context." The host "provides a lightweight `search_tools` meta-tool to the model" and "loads full definitions into context only as needed." ([Client Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices))

**SOURCE FACT.** Threshold guidance: "Implement a threshold as a percentage of the context window. For example, 1%-5%." ([Client Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices))

**SOURCE FACT.** Candidate search strategies: "**Keyword-based**: Keyword matching (BM25, regex)."; "**Embedding-based**: Vector-similarity retrieval over tool descriptions."; "**Subagent-based**: A secondary model, often a small and fast model such as Claude Haiku or Gemini Flash, selects tools for the task."; "**Hybrid**: Combine approaches." ([Client Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices))

**SOURCE FACT.** The three-layer pattern is "**Layer 1: Catalog.**" (`search_tools`), "**Layer 2: Inspect.**" (`get_tool_details`), and "**Layer 3: Execute.**". ([Client Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices))

**SOURCE FACT.** Dynamic server management: "Rather than connecting to every configured server at startup, a host can: 1. Maintain a registry of available servers and their high-level descriptions. 2. Connect to a server only when the model determines it needs that server's capabilities. 3. Disconnect servers that are no longer relevant to the current task, freeing context." ([Client Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices))

**SOURCE FACT.** Implementation guidelines include: "**Cache tool definitions**"; "**Refresh on `list_changed`** — Re-index the search catalog when a server sends `notifications/tools/list_changed`."; "**Group tools by server**". ([Client Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices))

**SOURCE FACT.** Caching: "Each list result (such as `tools/list`), as well as each `server/discover` and `resources/read` result, carries `ttlMs` and `cacheScope` hints." and "treat a cached list as stale once a `list_changed` notification arrives, even before its TTL expires." ([Client Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices))

**SOURCE FACT.** Prompt-caching interaction: "Adding or removing tool definitions mid-conversation invalidates that cache, and the resulting miss can cost more tokens than the definitions you removed." ([Client Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices))

### 6.2 Programmatic tool calling / code mode

**SOURCE FACT.** "Programmatic tool calling (sometimes called 'code mode') provides a way for clients to **compose tool calls** effectively. Instead of calling tools directly, the model writes code that calls tools. The code executes in a sandboxed environment, and only the final result returns to the model." ([Client Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices))

**SOURCE FACT.** "**The sandbox** runs model-generated code in an isolated environment with no direct network access." and "**The host** acts as a broker." and "**The model** sees only what the sandbox returns". ([Client Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices))

**SOURCE FACT.** Server-side enabler: "MCP Servers can provide an optional [`outputSchema`](https://modelcontextprotocol.io/specification/2026-07-28/server/tools#output-schema) for each tool. When an output schema is present, the host can produce precise return types". ([Client Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices))

**SOURCE FACT.** "MCP tool errors arrive as a successful response with [`isError: true`](https://modelcontextprotocol.io/specification/2026-07-28/server/tools#error-handling) rather than a transport failure. Generated wrappers should convert this into a thrown exception". ([Client Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices))

**SOURCE FACT.** Security considerations for code mode include: "**Per-call authorization**"; "**Cross-server data flow**: Tool results from one server are untrusted input to another."; "**Network isolation**: The sandbox should have no direct network access."; "**No credential exposure**"; "**Resource limits**: Set timeouts and memory limits". ([Client Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices))

**SOURCE FACT.** "Progressive discovery and programmatic tool calling work well together." ([Client Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices))

**AI INFERENCE (naming the outputSchema and code-mode facts).** Because the docs recommend producing precise return types from `outputSchema`, server authors who want to participate in code-mode clients have a concrete incentive to declare output schemas; the absence of one degrades the generated typed API. This follows from the quoted output-schema paragraph.

## 7. Debugging techniques

**SOURCE FACT.** "**MCP Inspector**: interactive, transport-agnostic testing UI. Connect to stdio or Streamable HTTP servers, invoke tools, prompts, and resources, and watch the notification stream. This should be your first stop." ([Debugging](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging))

**SOURCE FACT.** "Server logging: structured logs to stderr (stdio transport) or via OpenTelemetry (all transports)." ([Debugging](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging))

**SOURCE FACT.** "The [`notifications/message`] mechanism below is deprecated as of protocol version `2026-07-28`. It remains available during the deprecation window." ([Debugging](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging))

**SOURCE FACT.** "Local MCP servers should not log messages to stdout (standard out), as this will interfere with protocol operation." ([Debugging](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging))

**SOURCE FACT.** "For servers using the Streamable HTTP transport, stderr is not captured by the client. Use your own server-side log aggregation or OpenTelemetry for logs". ([Debugging](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging))

**SOURCE FACT.** Common issue — working directory: "The working directory for servers launched via the client's config may be undefined (like `/` on macOS) since the client could be started from anywhere. Always use absolute paths in your configuration and `.env` files". ([Debugging](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging))

**SOURCE FACT.** Common issue — environment variables: "MCP servers launched over stdio inherit only a limited subset of environment variables automatically (the exact set is platform-dependent)." ([Debugging](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging))

**SOURCE FACT.** Connection diagnosis: "call [`server/discover`] to see which protocol versions the server supports. An `UnsupportedProtocolVersionError` (`-32022`) lists the server's supported versions in its `data` field". ([Debugging](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging))

**SOURCE FACT.** "A request missing either required field is rejected with error `-32602` (Invalid params)" (the required fields being `io.modelcontextprotocol/protocolVersion` and `io.modelcontextprotocol/clientCapabilities`), and a missing capability yields "a `MissingRequiredClientCapabilityError` (`-32021`)". ([Debugging](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging))

**SOURCE FACT.** Claude Desktop logs are at macOS `~/Library/Logs/Claude` and Windows `%APPDATA%\Claude\logs`; client-side errors can be inspected via Chrome DevTools after creating a `developer_settings.json` with `{"allowDevTools": true}`. ([Debugging](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging))

**SOURCE FACT.** Testing changes: "**Server code changes**: Restart the client (for Claude Desktop, fully quit and reopen; closing the window is not enough)". ([Debugging](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging))

## 8. MCP Inspector usage

**SOURCE FACT.** "The MCP Inspector is the reference developer tool for testing and debugging MCP servers. It ships as a single package, `@modelcontextprotocol/inspector`, providing **three clients behind one binary**". ([MCP Inspector](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector))

**SOURCE FACT.** The three clients: "**Web** — `npx @modelcontextprotocol/inspector`"; "**CLI** — `npx @modelcontextprotocol/inspector --cli`"; "**TUI** — `npx @modelcontextprotocol/inspector --tui`". ([MCP Inspector](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector))

**SOURCE FACT.** "The Inspector requires **Node 22.19.0 or newer** and runs directly through `npx`. No installation is required". ([MCP Inspector](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector))

**SOURCE FACT.** CLI example: `npx @modelcontextprotocol/inspector --cli https://api.example.com/mcp --transport http --method tools/call --tool-name get_weather --tool-arg city=Boston --format json | jq .result`. ([MCP Inspector](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector))

**SOURCE FACT.** "`mcp-inspector` … owns only two things: 1. **The mode flag:** `--web` (default), `--cli`, or `--tui`. … 2. **`-h` / `--help`.**" and "Everything else (`--catalog`, `--config`, `--server-url`, `--transport`, `--method`, the OAuth flags) is defined by the *client*, not the launcher". ([MCP Inspector](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector))

**SOURCE FACT.** "All three are built on the same shared core, so a connection behaves identically across them: the same transports, the same configuration files, the same OAuth state on disk, and the same protocol-era negotiation (legacy vs. modern 2026-07-28)." ([MCP Inspector](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector))

**SOURCE FACT.** "Always read a server's own README first, since every server requires different commands and arguments." ([MCP Inspector](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector))

## 9. Roadmap priorities

**SOURCE CLAIM (Rank C).** Page freshness: "Last updated: **2026-08-22**". Scope: "This page outlines the Core Maintainers' vision for the protocol over the coming six to twelve months". Caveat: "This roadmap reflects current thinking rather than firm commitments. Priorities may shift". ([Roadmap](https://modelcontextprotocol.io/development/roadmap))

**SOURCE CLAIM (Rank C).** Review policy: "SEPs that fall within the priority areas below get expedited review and have the best chance of acceptance." ([Roadmap](https://modelcontextprotocol.io/development/roadmap))

**SOURCE CLAIM (Rank C).** Priority Area 1 — "**Agentic Messaging Primitives**": deliverables include "Server-initiated events: [Triggers & Events WG]. Channels and subscriptions for push delivery, including webhooks." and "A composition review". Also: "we expect continued work on Tasks ([SEP-2663](https://modelcontextprotocol.io/seps/2663-tasks-extension)) toward eventual inclusion of the extension in the core protocol." ([Roadmap](https://modelcontextprotocol.io/development/roadmap))

**SOURCE CLAIM (Rank C).** Priority Area 2 — "**HTTP-Native Transport Unification and Hardening**": deliverables include "**HTTP over stdio**: Transports WG. Streamable HTTP as the single binding, spoken over stdin/stdout for local servers." and "**Caching**: … extend our caching approach to support ETags". ([Roadmap](https://modelcontextprotocol.io/development/roadmap))

**SOURCE CLAIM (Rank C).** Priority Area 3 — "**Agent Identity and Enterprise-Ready Security**": deliverables include "**DPoP**: Agent Identity WG (forming during this roadmap period)." and "**Agent identity and delegation**: … Workload Identity Federation ([SEP-1933]) …, the Identity Assertion JWT Authorization Grant (ID-JAG) used by [Enterprise-Managed Authorization], and [RFC 8693] token exchange". ([Roadmap](https://modelcontextprotocol.io/development/roadmap))

**SOURCE CLAIM (Rank C).** Priority Area 4 — "**Improved Primitives**": deliverables include "**Tool result shape**: … Redesign the `tools/call` interface to resolve fidelity disparities among return types" and "**Progressive discovery**: Clients learn a server's tools and resources as they need them instead of ingesting the full catalog up front" and "**Primitive annotations**". ([Roadmap](https://modelcontextprotocol.io/development/roadmap))

**SOURCE CLAIM (Rank C).** Priority Area 5 — "**Improved SDK Developer Experience**": deliverables include "**The extension contract**: [SDK WG] … Which role an extension binds (host, client, server, agent) and what each does when the capability is declared" and "**The generated-artifacts experiment**: [SDK WG]. Generate a candidate [Tier 1 SDK] and its companion quickstart examples from the specification". ([Roadmap](https://modelcontextprotocol.io/development/roadmap))

**SOURCE CLAIM (Rank C).** Participation: "**Start an experimental extension**: [SEP-2133] lets any WG or IG experiment in an `experimental-ext-` repository before a formal SEP." ([Roadmap](https://modelcontextprotocol.io/development/roadmap))

**AI INFERENCE (naming the roadmap and client-best-practices facts).** The roadmap's "Progressive discovery" item under Improved Primitives is aimed at a server-side discovery mechanism, while the Client Best Practices page already documents client-side progressive discovery with a `search_tools` meta-tool; the two are complementary but not the same deliverable. This is derived from the quoted roadmap item ("define what an experimental server-side discovery mechanism would look like") and the quoted client pattern.

## 10. Key takeaways

- **SOURCE FACT.** The canonical server workflow is scaffold → implement typed tool handlers → run → test in a host; the same shape is repeated across Python, TypeScript, Java, Kotlin, and C#. ([Build an MCP server](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server))
- **SOURCE FACT.** For stdio servers, stdout is protocol territory and must never receive log output; HTTP servers are exempt. ([Build an MCP server](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server))
- **SOURCE FACT.** Tool names SHOULD be 1–64 characters, case-sensitive, using `A-Z a-z 0-9 _ - . /`, unique within their namespace. ([SEP-986](https://modelcontextprotocol.io/seps/986-specify-format-for-tool-names))
- **SOURCE FACT.** Scaling is addressed by progressive discovery (defer definitions, search meta-tool, three layers) and programmatic tool calling (sandboxed code, host broker, only final output returns). ([Client Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices))
- **SOURCE FACT.** The Inspector is three clients (Web/CLI/TUI) behind one binary, requires Node 22.19.0+, and is recommended as the first debugging stop. ([MCP Inspector](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector), [Debugging](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging))
- **SOURCE FACT.** Protocol-era errors to expect while debugging: `-32022` unsupported version, `-32602` missing required `_meta` fields, `-32021` missing required client capability. ([Debugging](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging))
- **SOURCE CLAIM (Rank C).** Roadmap priorities for the next six to twelve months are agentic messaging, HTTP-native transport unification, agent identity/security, improved primitives (notably `tools/call` shape and progressive discovery), and SDK developer experience. ([Roadmap](https://modelcontextprotocol.io/development/roadmap))
