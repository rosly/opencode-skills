# Observability, Performance, and Cost for MCP Servers (Protocol Revision 2026-07-28)

Research file. Retrieved: 2026-10-03. Protocol revision referenced throughout: **2026-07-28**.

## Notation and evidence ranking

- **SOURCE FACT** — a normative statement quoted verbatim from an official specification/SEP or official documentation page.
- **SOURCE CLAIM (Rank N)** — a non-normative statement quoted verbatim. Ranks: **Rank A** = Final/Standards-Track SEP or normative specification text; **Rank B** = official documentation page (editorial guidance); **Rank C** = vendor/engineering blog or third-party analysis.
- **AI INFERENCE** — my reasoning that names the specific quoted facts it is derived from.
- **PLAUSIBLE NOT VERIFIED** — a conjecture consistent with sources but not directly stated.
- **UNKNOWN** — no source retrieved or source is silent.

Quotations are short and exact. Every externally sourced fact carries an inline link to the source URL. No end-only bibliography is used. Retrieval status for this file: the MCP basic protocol, caching, client best-practices, debugging, SEP-414, and logging pages were retrieved; the OpenTelemetry semantic-conventions index and the GenAI MCP conventions page were retrieved; the FastMCP telemetry page was retrieved. One requested URL failed: `https://gofastmcp.com/servers/open-telemetry.md` returned HTTP 404; the correct page is `https://gofastmcp.com/servers/telemetry.md`, which was retrieved. The `https://opentelemetry.io/docs/specs/semconv/gen-ai/mcp/` URL now redirects to a "Moved" notice; the live content is at the `semantic-conventions-genai` repository, which was retrieved.

## 1. OpenTelemetry trace context propagation via `_meta`

**SOURCE FACT.** The base protocol reserves three keys for trace context: the reserved `_meta` keys table lists "`traceparent`, `tracestate`, `baggage` | OpenTelemetry trace context propagation". ([Basic Protocol](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md))

**SOURCE FACT.** The values must follow the W3C formats: "When present, their values MUST follow [W3C Trace Context](https://www.w3.org/TR/trace-context/) and [W3C Baggage](https://www.w3.org/TR/baggage/) formats respectively." ([Basic Protocol](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md))

**SOURCE FACT.** The protocol gives a non-normative example: `"_meta": { "traceparent": "00-0af7651916cd43dd8448eb211c80319c-00f067aa0ba902b7-01" }`. ([Basic Protocol](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md))

**SOURCE FACT.** The exception to DNS prefixing is deliberate: "This exception exists to maintain compatibility with existing implementations and [OpenTelemetry semantic conventions for MCP]." ([Basic Protocol](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md))

**SOURCE FACT.** SEP-414 documents the convention: "When OTel trace context is propagated via `_meta`, the keys `traceparent`, `tracestate`, and `baggage` follow [W3C Trace Context] and [W3C Baggage] value formats." ([SEP-414](https://modelcontextprotocol.io/seps/414-request-meta))

**SOURCE FACT.** SEP-414 explains why the exception matters: "If we don't document this shared concern, differing interpretations could materialize, such as namespacing traceparent like `io.modelcontextprotocol.traceparent`, which will break traces and log correlation." ([SEP-414](https://modelcontextprotocol.io/seps/414-request-meta))

**SOURCE FACT.** The OpenTelemetry MCP conventions specify the injection point: "Instrumentations SHOULD propagate context using the configured [OpenTelemetry propagators] by injecting it into the MCP request [`params._meta`] property bag when creating a request or notification. The receiver extracts the context from `params._meta` and uses it as the remote parent." ([OTel MCP semantic conventions](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/mcp.md))

**SOURCE FACT.** The server-side default is stated: "MCP server instrumentation SHOULD, by default, use context extracted from MCP `params._meta` as a parent for MCP server span and SHOULD link current ambient context, if it's present." ([OTel MCP semantic conventions](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/mcp.md))

**SOURCE FACT.** MCP and transport contexts are independent: "MCP and underlying transport (such as HTTP) contexts are independent. One MCP request can be served by multiple HTTP requests (for example, because of retries) and one streamable HTTP request can serve more than one MCP request/notification." ([OTel MCP semantic conventions](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/mcp.md))

**SOURCE FACT.** The conventions also warn that trace context may carry correlation IDs: "Trace context in `_meta` may include correlation IDs. Implementations should follow existing data-handling guidance appropriate to their environment." ([SEP-414](https://modelcontextprotocol.io/seps/414-request-meta))

**AI INFERENCE (naming the trace-context facts).** The quoted reservation ("`traceparent`, `tracestate`, `baggage`") plus the quoted injection rule ("injecting it into the MCP request `params._meta` property bag") means a server should read these three keys from `_meta` and use them as the remote parent, not invent a namespaced variant — the quoted SEP-414 warning ("namespacing traceparent like `io.modelcontextprotocol.traceparent` ... will break traces") makes the unprefixed form mandatory for interoperability.

## 2. Structured logging to stderr and OpenTelemetry

**SOURCE FACT.** The debugging guide states the transport split: "**Server logging**: structured logs to stderr (stdio transport) or via [OpenTelemetry](https://opentelemetry.io/) (all transports)." ([Debugging](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging.md))

**SOURCE FACT.** stdout is forbidden for stdio servers: "Local MCP servers should not log messages to stdout (standard out), as this will interfere with protocol operation." ([Debugging](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging.md))

**SOURCE FACT.** HTTP servers need their own aggregation: "For servers using the [Streamable HTTP transport], stderr is not captured by the client. Use your own server-side log aggregation or [OpenTelemetry](https://opentelemetry.io/) for logs". ([Debugging](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging.md))

**SOURCE FACT.** The protocol logging feature is deprecated: "The `notifications/message` mechanism below is deprecated as of protocol version `2026-07-28`." ([Debugging](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging.md))

**SOURCE FACT.** The logging specification repeats the deprecation and the migration path: "New implementations **SHOULD NOT** adopt it; existing implementations **SHOULD** migrate to logging to `stderr` for stdio transports, or to [OpenTelemetry](https://opentelemetry.io/) for structured observability." ([Logging](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/logging.md))

**SOURCE FACT.** The debugging guide lists what to log: "Important events to log: Startup steps; Resource access; Tool execution; Error conditions; Performance metrics". ([Debugging](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging.md))

**SOURCE FACT.** It also recommends structured logging practice: "**Structured Logging**: Use consistent formats; Include context; Add timestamps; Track request IDs". ([Debugging](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging.md))

**SOURCE FACT.** The logging specification requires redaction: "Log messages **MUST NOT** contain: Credentials or secrets; Personal identifying information; Internal system details that could aid attacks". ([Logging](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/logging.md))

**SOURCE CLAIM (Rank B).** FastMCP describes its instrumentation as zero-cost when unused: "**On by default** - Instrumentation is active out of the box, no opt-in required" and "**No overhead when unused** - Without an SDK, all operations are no-ops". ([FastMCP OpenTelemetry](https://gofastmcp.com/servers/telemetry.md))

**SOURCE CLAIM (Rank B).** FastMCP warns against over-instrumenting: "Avoid wrapping every small helper function or simple in-memory transformation. That usually adds noise without making traces easier to interpret." ([FastMCP OpenTelemetry](https://gofastmcp.com/servers/telemetry.md))

**SOURCE CLAIM (Rank B).** FastMCP states the redaction rule for spans: "Do not record secrets, prompts with sensitive user data, or raw tokens as span attributes". ([FastMCP OpenTelemetry](https://gofastmcp.com/servers/telemetry.md))

**AI INFERENCE (naming the logging facts).** The quoted deprecation ("New implementations **SHOULD NOT** adopt it") plus the quoted transport split ("structured logs to stderr (stdio transport) or via OpenTelemetry (all transports)") means a new server should not build on `notifications/message`; it should emit structured logs to stderr for stdio and to OpenTelemetry for HTTP, applying the quoted redaction rule in both paths.

## 3. Metrics to track

**SOURCE FACT.** The OpenTelemetry MCP conventions define four metrics: `mcp.client.operation.duration`, `mcp.server.operation.duration`, `mcp.client.session.duration`, and `mcp.server.session.duration`. ([OTel MCP semantic conventions](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/mcp.md))

**SOURCE FACT.** The operation-duration metric is a histogram with explicit buckets: "This metric SHOULD be specified with [`ExplicitBucketBoundaries`] of `[ 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 30, 60, 120, 300 ]`." ([OTel MCP semantic conventions](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/mcp.md))

**SOURCE FACT.** The metric is defined as: "The duration of the MCP request or notification as observed on the sender from the time it was sent until the response or ack is received." ([OTel MCP semantic conventions](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/mcp.md))

**SOURCE FACT.** The required span attribute is `mcp.method.name`: "The name of the request or notification method." ([OTel MCP semantic conventions](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/mcp.md))

**SOURCE FACT.** Tool errors get a low-cardinality classification: "When [CallToolResult] is returned with `isError` set to `true`, this attribute SHOULD be set to `tool_error`." ([OTel MCP semantic conventions](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/mcp.md))

**SOURCE FACT.** The conventions define which JSON-RPC codes are not errors: "The following error codes indicate that the caller sent a request the receiver could not serve and SHOULD NOT be considered errors: `-32700` (`Parse error`); `-32600` (`Invalid Request`); `-32601` (`Method not found`); `-32602` (`Invalid params`) ... `-32002` (`Resource not found`)". ([OTel MCP semantic conventions](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/mcp.md))

**SOURCE FACT.** The debugging guide lists performance metrics to log: "**Performance Tracking**: Log operation timing; Monitor resource usage; Track message sizes; Measure latency". ([Debugging](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging.md))

**SOURCE CLAIM (Rank B).** FastMCP lists the attributes it emits, including `mcp.method.name`, `mcp.protocol.version`, `mcp.session.id`, `mcp.resource.uri`, `gen_ai.tool.name`, `gen_ai.prompt.name`, and `error.type`. ([FastMCP OpenTelemetry](https://gofastmcp.com/servers/telemetry.md))

**SOURCE CLAIM (Rank B).** FastMCP also emits auth attributes: "`enduser.id` | Client ID from access token (when authenticated)" and "`enduser.scope` | Space-separated OAuth scopes (when authenticated)". ([FastMCP OpenTelemetry](https://gofastmcp.com/servers/telemetry.md))

**AI INFERENCE (naming the metrics facts).** The quoted four metrics plus the quoted required attribute (`mcp.method.name`) define the minimum dashboard: latency histograms per method, session durations, and error counts keyed by `error.type` with `tool_error` as the tool-failure bucket. The quoted "SHOULD NOT be considered errors" list means a dashboard that counts all non-OK JSON-RPC codes as failures will over-report; `-32602` in particular is normal for unknown tools.

## 4. Caching: `ttlMs`, `cacheScope`, and invalidation

**SOURCE FACT.** Caching hints are mandatory on cacheable results: "Servers MUST include caching hints on results with `resultType: "complete"` returned by the following operations: `server/discover`; `tools/list`; `prompts/list`; `resources/list`; `resources/templates/list`; `resources/read`". ([Caching](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching.md))

**SOURCE FACT.** `ttlMs` is defined as: "The `ttlMs` field is a hint from the server indicating how long, in milliseconds, the client MAY consider the result fresh. Semantics are analogous to HTTP `Cache-Control: max-age`." ([Caching](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching.md))

**SOURCE FACT.** The default when absent is zero: "If `ttlMs` is absent, clients **SHOULD** assume a default of `0` (immediately stale)". ([Caching](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching.md))

**SOURCE FACT.** Servers must supply a non-negative value: "Servers **MUST** provide a `ttlMs` value that is `>= 0`." ([Caching](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching.md))

**SOURCE FACT.** `cacheScope` is defined as: "The `cacheScope` field controls who may cache a response, analogous to HTTP `Cache-Control: public` vs `Cache-Control: private`." ([Caching](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching.md))

**SOURCE FACT.** The two scope values are defined: "`"public"` | The response does not contain user-specific data. Any client, shared gateway, or caching proxy **MAY** store and serve the cached response to any user." and "`"private"` | The response contains private data that is not meant to be shared between callers. Cached responses **MAY** be reused for the same authorization context." ([Caching](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching.md))

**SOURCE FACT.** Notifications invalidate fresh caches: "When a relevant notification is received while a cached response is still fresh, the notification **invalidates** the cached response and it should be considered immediately stale." ([Caching](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching.md))

**SOURCE FACT.** Pagination pages are independently cacheable, but scope must be consistent: "Servers **MUST** apply the same `cacheScope` to all response pages for a given list request." ([Caching](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching.md))

**SOURCE FACT.** The security warning is explicit: "Servers MUST be aware that responses with a `"public"` `cacheScope` may be shared between callers even if the Result is coming from an authenticated endpoint." ([Caching](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching.md))

**SOURCE FACT.** The server must not rely on scope for access control: "MUST apply appropriate per-primitive access controls, and MUST NOT rely on `cacheScope` alone to prevent unauthorized access to primitives." ([Caching](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching.md))

**SOURCE FACT.** The client best-practices page restates the invalidation rule: "treat a cached list as stale once a `list_changed` notification arrives, even before its TTL expires." ([Client Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices))

**AI INFERENCE (naming the caching facts).** The quoted mandatory-hints rule ("Servers MUST include caching hints") plus the quoted default ("assume a default of `0`") means a server that omits `ttlMs` forces clients to re-fetch every time. The quoted security warning ("may be shared between callers even if the Result is coming from an authenticated endpoint") means `cacheScope: "public"` must be reserved for genuinely user-independent lists, and the quoted "MUST NOT rely on `cacheScope` alone" means access control stays server-side.

## 5. Reducing context and token cost

**SOURCE FACT.** The client best-practices page states the problem: "Loading every tool definition into the model's context window upfront wastes tokens, increases latency, and degrades model performance." ([Client Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices))

**SOURCE FACT.** Progressive discovery is defined: "The host fetches tool definitions via `tools/list` as normal, but defers injecting them into the model's context." and "The host provides a lightweight `search_tools` meta-tool to the model." ([Client Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices))

**SOURCE FACT.** The switch threshold is guidance: "Once the tool definitions take up a significant part of the available context window, clients should switch to progressive discovery. We recommend that clients implement thresholds to determine when to switch: Implement a threshold as a percentage of the context window. For example, 1%-5%." ([Client Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices))

**SOURCE FACT.** The three-layer pattern is catalog, inspect, execute: "**Layer 1: Catalog.** ... A `search_tools` tool accepts a natural-language query and returns matching tool names with brief descriptions."; "**Layer 2: Inspect.** ... it fetches the full definition ... for that tool only."; "**Layer 3: Execute.** The model calls the tool with full knowledge of its interface". ([Client Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices))

**SOURCE FACT.** Deterministic ordering is a server requirement: "Servers **SHOULD** return tools in a deterministic order (i.e., the same ordering across requests when the underlying set of tools has not changed). Deterministic ordering enables clients to reliably cache the tool list and improves LLM prompt cache hit rates when tools are included in model context." ([Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md))

**SOURCE FACT.** Prompt caching is fragile to tool changes: "Most providers cache the prompt prefix, including the `tools` array. Adding or removing tool definitions mid-conversation invalidates that cache, and the resulting miss can cost more tokens than the definitions you removed." ([Client Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices))

**SOURCE FACT.** The page gives two preservation strategies: "Append newly discovered definitions after the cache breakpoint rather than re-sorting the `tools` array, or route every call through a single stable `call_tool({name, args})` meta-tool so the array never changes." ([Client Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices))

**SOURCE FACT.** Programmatic tool calling keeps intermediate data out of context: "Instead of calling tools directly, the model writes code that calls tools. The code executes in a sandboxed environment, and only the final result returns to the model." ([Client Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices))

**SOURCE CLAIM (Rank C).** Anthropic quantifies the saving: "This reduces the token usage from 150,000 tokens to 2,000 tokens—a time and cost saving of 98.7%." ([Code execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp))

**SOURCE CLAIM (Rank C).** Anthropic names the two cost drivers: "As MCP usage scales, there are two common patterns that can increase agent cost and latency: 1. Tool definitions overload the context window; 2. Intermediate tool results consume additional tokens." ([Code execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp))

**SOURCE CLAIM (Rank C).** Anthropic gives a concrete intermediate-result figure: "For a 2-hour sales meeting, that could mean processing an additional 50,000 tokens." ([Code execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp))

**AI INFERENCE (naming the context-cost facts).** The quoted server requirement ("deterministic order ... improves LLM prompt cache hit rates") and the quoted client warning ("Adding or removing tool definitions mid-conversation invalidates that cache") together mean a server author can help clients preserve prompt caches simply by returning a stable tool order and stable schemas. The quoted progressive-discovery threshold ("1%-5%") is client-side, but it implies servers should keep tool descriptions concise so the threshold is reached later.

## 6. Latency and streaming

**SOURCE FACT.** The protocol supports progress notifications for long operations: the reserved `_meta` key `progressToken` "Opts the request into progress notifications". ([Basic Protocol](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md))

**SOURCE FACT.** Long-lived requests remain request/response: "Long-lived requests like [`subscriptions/listen`] remain request/response; the response is just an open stream of notifications. Their state is scoped to the request itself, not to the connection underneath." ([Basic Protocol](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md))

**SOURCE FACT.** The client best-practices page notes the latency cost of direct calls: "With direct tool calling, every tool invocation is a round trip: the model generates a tool call, the client executes it, and the full result flows back into the model's context." ([Client Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices))

**SOURCE CLAIM (Rank C).** Anthropic notes a latency benefit of code execution: "being able to write out a conditional tree that gets executed also saves on "time to first token" latency: rather than having to wait for a model to evaluate an if-statement, the agent can let the code execution environment do this." ([Code execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp))

**SOURCE FACT.** The debugging guide recommends measuring latency: "**Performance Tracking**: Log operation timing; Monitor resource usage; Track message sizes; Measure latency". ([Debugging](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging.md))

**SOURCE CLAIM (Rank B).** FastMCP recommends custom spans around expensive work: "Custom spans are most useful around work that is expensive or hard to debug: External calls such as databases, vector stores, HTTP APIs, or queue operations; Multi-step tool logic where one stage dominates latency". ([FastMCP OpenTelemetry](https://gofastmcp.com/servers/telemetry.md))

**SOURCE CLAIM (Rank B).** FastMCP recommends naming child spans by operation: "Use `{tool_name}.{operation}` or `{resource_name}.{operation}` for child spans such as `search.fetch`, `search.rank`, or `docs.render`". ([FastMCP OpenTelemetry](https://gofastmcp.com/servers/telemetry.md))

**AI INFERENCE (naming the latency facts).** The quoted progress-token mechanism plus the quoted "long-lived requests ... remain request/response" means a server should report progress via `progressToken` rather than holding a connection open as implicit state. The quoted FastMCP guidance ("Multi-step tool logic where one stage dominates latency") implies child spans should be placed at the stage boundaries that dominate latency, not around every helper.

## 7. Rate limiting and backpressure

**SOURCE FACT.** Rate limiting is a server requirement: "Servers **MUST**: ... Rate limit tool invocations". ([Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md))

**SOURCE FACT.** The logging specification requires rate limiting for log messages: "Implementations **SHOULD**: Rate limit messages; Validate all data fields; Control log access; Monitor for sensitive content". ([Logging](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/logging.md))

**SOURCE FACT.** The caching specification warns against polling without jitter: "Clients **SHOULD NOT** treat TTL as a polling interval that triggers automatic background refetches. ... Implementations that do choose to poll **MUST** apply jitter and backoff." ([Caching](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching.md))

**SOURCE FACT.** The client best-practices page recommends retry limits for scope upgrades: "Clients **SHOULD** implement retry limits and **SHOULD** track scope upgrade attempts to avoid repeated failures for the same resource and operation combination." ([Authorization](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md))

**SOURCE FACT.** The tools specification recommends client-side timeouts: "Clients **SHOULD**: ... Implement timeouts for tool calls". ([Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md))

**SOURCE CLAIM (Rank B).** FastMCP ships rate-limiting and response-limiting middleware: the documentation index lists "Rate Limiting" and "Response Limiting" middleware pages. ([FastMCP llms.txt](https://gofastmcp.com/llms.txt))

**SOURCE CLAIM (Rank C).** Docker describes resource limits as a backpressure control: "Resource limits prevent crypto miners" with the example `docker mcp gateway run --cpus 1 --memory 512Mb`. ([MCP Horror Stories: The Supply Chain Attack](https://www.docker.com/blog/mcp-horror-stories-the-supply-chain-attack/))

**AI INFERENCE (naming the rate-limiting facts).** The quoted server requirement ("Rate limit tool invocations") plus the quoted client timeout recommendation ("Implement timeouts for tool calls") means backpressure is a shared responsibility: the server bounds concurrency and the client bounds wait time. The quoted caching rule ("MUST apply jitter and backoff") applies to any server-side polling of upstream systems as well.

## 8. Cost of tool count

**SOURCE FACT.** The client best-practices page gives the scale: "As MCP host applications, such as agents, connect to more MCP servers and accumulate access to hundreds or thousands of tools, naive approaches to tool management break down." ([Client Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices))

**SOURCE FACT.** The page quantifies the naive cost in an image caption: "The upfront approach consumes ~150,000 tokens on definitions alone, while progressive discovery uses ~2,000 tokens by loading only what the task requires." ([Client Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices))

**SOURCE FACT.** The page recommends caching tool definitions host-side: "**Cache tool definitions** | Once fetched from a server, memoize the definition host-side so re-injecting it later doesn't need another `tools/list` round trip." ([Client Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices))

**SOURCE FACT.** The page recommends grouping tools by server: "**Group tools by server** | Present tools organized by their source server so the model can reason about related capabilities." ([Client Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices))

**SOURCE CLAIM (Rank C).** Anthropic states the definition-overload problem: "Tool descriptions occupy more context window space, increasing response time and costs. In cases where agents are connected to thousands of tools, they'll need to process hundreds of thousands of tokens before reading a request." ([Code execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp))

**SOURCE CLAIM (Rank C).** Anthropic describes the filesystem alternative: "The agent discovers tools by exploring the filesystem: listing the `./servers/` directory to find available servers ... then reading the specific tool files it needs ... This lets the agent load only the definitions it needs for the current task." ([Code execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp))

**SOURCE CLAIM (Rank B).** FastMCP provides a tool-search transform: the documentation index lists "Tool Search | Replace large tool catalogs with on-demand search". ([FastMCP llms.txt](https://gofastmcp.com/llms.txt))

**AI INFERENCE (naming the tool-count facts).** The quoted scale ("hundreds or thousands of tools") plus the quoted caption ("~150,000 tokens on definitions alone") means tool count is a first-order cost driver. The quoted server-side lever is deterministic ordering and concise descriptions; the quoted client-side levers are progressive discovery, host-side memoization, and grouping by server.

## 9. Consolidated observability and performance checklist

**AI INFERENCE (naming the facts above).** The following checklist is derived only from the quoted facts in this file:

1. Read `traceparent`, `tracestate`, and `baggage` from `_meta` and use them as the remote parent — from "injecting it into the MCP request `params._meta` property bag" and "use context extracted from MCP `params._meta` as a parent" ([OTel MCP semantic conventions](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/mcp.md)).
2. Do not namespace the trace keys — from "namespacing traceparent like `io.modelcontextprotocol.traceparent` ... will break traces and log correlation" ([SEP-414](https://modelcontextprotocol.io/seps/414-request-meta)).
3. Log to stderr for stdio and to OpenTelemetry for HTTP; never to stdout — from "structured logs to stderr (stdio transport) or via OpenTelemetry (all transports)" and "should not log messages to stdout" ([Debugging](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging.md)).
4. Do not build on `notifications/message` — from "New implementations **SHOULD NOT** adopt it" ([Logging](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/logging.md)).
5. Emit the four MCP metrics and key errors by `error.type`, with `tool_error` for tool failures — from the metric list and "this attribute SHOULD be set to `tool_error`" ([OTel MCP semantic conventions](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/mcp.md)).
6. Include `ttlMs` and `cacheScope` on every cacheable result — from "Servers MUST include caching hints on results with `resultType: "complete"`" ([Caching](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching.md)).
7. Use `cacheScope: "private"` for user-specific data and never rely on scope for access control — from "Cached responses **MAY** be reused for the same authorization context" and "MUST NOT rely on `cacheScope` alone" ([Caching](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching.md)).
8. Return tools in a deterministic order — from "Servers **SHOULD** return tools in a deterministic order" ([Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md)).
9. Keep tool descriptions concise and schemas stable to preserve prompt caches — from "Adding or removing tool definitions mid-conversation invalidates that cache" ([Client Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices)).
10. Rate limit tool invocations and log messages — from "Rate limit tool invocations" and "Rate limit messages" ([Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md), [Logging](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/logging.md)).
11. Never record secrets, tokens, or PII in logs or spans — from "Log messages **MUST NOT** contain: Credentials or secrets" and "Do not record secrets, prompts with sensitive user data, or raw tokens as span attributes" ([Logging](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/logging.md), [FastMCP OpenTelemetry](https://gofastmcp.com/servers/telemetry.md)).

## 10. Open questions and gaps

**UNKNOWN.** The retrieved MCP specification does not define a normative server-side rate-limit algorithm, quota unit, or backpressure signal; the requirement is only "Rate limit tool invocations". The concrete mechanism is left to the implementation.

**UNKNOWN.** No retrieved MCP source defines a normative token-budget or tool-count limit. The "1%-5%" threshold and the "~150,000 tokens" figure are client-side guidance and an illustrative caption, not protocol limits.

**PLAUSIBLE NOT VERIFIED.** The OpenTelemetry MCP semantic conventions are marked "Development" status in the retrieved document; the exact attribute set may change before stabilization. The retrieved page states the spans are "**Status:** ![Development]" and the metrics are "![Development]".

**PLAUSIBLE NOT VERIFIED.** The claim that FastMCP is "downloaded more than a million times a day, and some version of FastMCP powers 70% of MCP servers across all languages" appears on the FastMCP landing page but was not independently verified. ([FastMCP](https://gofastmcp.com/))
