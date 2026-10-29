# Writing MCP Servers — Professional Development Report

Research date: 2026-10-03
Current MCP protocol revision: **2026-07-28**
Scope: how to build, test, secure, deploy, and publish MCP servers efficiently.

This report synthesizes official MCP documentation, official SDK repositories, framework
documentation, and selected ecosystem sources. Inline links point to the source of each claim; a
single consolidated list of all referenced URLs appears in the final "Resources" section. Where the
report draws a conclusion rather than restating a source, it says so. It does not use evidence tags.

Per-topic detail files are in `development/` alongside this report. Round 1 (protocol knowledge) is
in `mcp-protocol.md` and `protocol/`.

---

## 1. Choosing a language and SDK

> Detail: [development/01-sdks-languages.md](development/01-sdks-languages.md)

The official SDKs are tiered "based on feature completeness, protocol support, and maintenance
commitment" — [SDKs](https://modelcontextprotocol.io/docs/2026-07-28/sdk). Tier 1 is TypeScript,
Python, C#, Go, Rust, and Ruby; Tier 2 is Java; Tier 3 is Swift, PHP, and Kotlin. Tier 1 requires a
"100% pass rate" on conformance tests and new features "Before new spec version release"; Tier 2
requires 80% and features within six months — [SDK tiering](https://modelcontextprotocol.io/community/sdk-tiers).
Conformance tests became available 2026-01-23 and official tiering was published 2026-02-23 — same
source. For a new production server, a Tier 1 SDK is the default choice; Java is the strongest
non-Tier-1 option.

The 2026-07-28 stateless model is a breaking change for SDKs, and adoption is uneven. The Python SDK
v2 "speaks the 2026-07-28 revision of MCP, which removes the connection handshake, the session, and
every server-initiated request," and "Over Streamable HTTP there is no `Mcp-Session-Id` on the 2026
path" — [Python SDK v2](https://py.sdk.modelcontextprotocol.io/whats-new/). The same SDK serves both
eras: "the same `streamable_http_app()` … answers a 2025-era client's `initialize` and a 2026-era
client's requests with nothing to configure" — same source. The TypeScript SDK states "v2 is the
stable release line, released alongside the 2026-07-28 spec. v1.x continues to receive bug fixes and
security updates for at least 6 months after v2's release" —
[typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk). The Go SDK documents an
explicit version map: "v1.7.0+ | 2026-07-28 | 2026-07-28, 2025-11-25*, 2025-06-18, 2025-03-26,
2024-11-05" — [go-sdk](https://github.com/modelcontextprotocol/go-sdk). The Rust SDK documents both
lifecycles and the new subscription model, noting that "Protocol `2026-07-28` replaces
`resources/subscribe` … with the transport-neutral, long-lived `subscriptions/listen` request" —
[rust-sdk](https://github.com/modelcontextprotocol/rust-sdk). The PHP SDK explicitly supports "both
protocol eras (the `initialize` handshake and the stateless `2026-07-28` revision)" —
[php-sdk](https://github.com/modelcontextprotocol/php-sdk). The Swift SDK is behind: it "implements
both client and server components according to the [2025-11-25] (latest) version" —
[swift-sdk](https://github.com/modelcontextprotocol/swift-sdk).

Practical selection guidance: pick a Tier 1 SDK whose protocol version matches your target; verify
the SDK's current supported protocol versions before committing, because Tier 3 SDKs and even some
Tier 1 SDKs may still be on 2025-11-25. If you must serve legacy clients, confirm the SDK supports
dual-era negotiation rather than assuming it.

## 2. Frameworks and libraries

> Detail: [development/02-frameworks-libraries.md](development/02-frameworks-libraries.md)

Frameworks add schema generation, validation, transport management, authentication, and protocol-era
negotiation on top of the raw SDK.

**FastMCP (Python)** is the dominant framework. "FastMCP created the high-level Python API
incorporated into the official MCP Python SDK in 2024" — [FastMCP welcome](https://gofastmcp.com/getting-started/welcome).
It is now a standalone project at v4: "FastMCP 4 is stable: the FastMCP release for the new MCP
protocol and the rewritten Python SDK v2, with old-protocol clients supported through per-connection
negotiation" — [FastMCP updates](https://gofastmcp.com/updates). It manages "schema generation,
validation, transport, authentication, and protocol compatibility around your application code," and
a server "starts with ordinary Python" — [FastMCP welcome](https://gofastmcp.com/getting-started/welcome).
It also offers a CLI, an Inspector extra, OpenTelemetry instrumentation, and provider types
(FileSystem, Skills, OpenAPI) — [FastMCP updates](https://gofastmcp.com/updates). Choose FastMCP for
most Python servers unless you need low-level control.

**MCP-Framework (TypeScript)** is a TypeScript framework with a CLI (`mcp create`, `mcp add tool`,
`mcp add resource`) and build-time schema validation that requires descriptions on all schema fields
— [mcp-framework](https://github.com/QuantGeekDev/mcp-framework). **mcp-use (TypeScript)** "builds on
the official TypeScript SDK v2 and adds first-class Views, typed tool-to-UI contracts, an optimized
stateless runtime, the Inspector" — [mcp-use](https://github.com/mcp-use/mcp-use). **Spring AI
(Java)** provides Spring-specific MCP transports; "Starting with Spring AI 2.0, the Spring-specific
MCP transport implementations … are no longer shipped by the MCP Java SDK. They have been moved into
the Spring AI project itself" — [Spring AI MCP](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-overview.html).
**MCP Toolbox (Go)** is "an open source Model Context Protocol (MCP) server that connects your AI
agents … directly to your enterprise databases," configured via `tools.yaml` —
[mcp-toolbox](https://github.com/googleapis/genai-toolbox). **mcp-agent** is a framework for building
agents that use MCP servers — [mcp-agent](https://github.com/lastmile-ai/mcp-agent).

Selection guidance: use a framework when it removes boilerplate you would otherwise write (schema
generation, auth, transport negotiation); use the raw SDK when you need precise control over the
wire behavior or are targeting a language without a mature framework. For Python, FastMCP is the
default; for TypeScript, the official SDK v2 plus a framework such as mcp-use or MCP-Framework is
reasonable.

---

## 3. Server design patterns

> Detail: [development/03-server-design-patterns.md](development/03-server-design-patterns.md)

### 3.1 Choose the right primitive

The three primitives differ by who decides invocation: tools are "model-controlled," resources are
"application-driven," and prompts are "user-controlled" —
[tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md),
[resources](https://modelcontextprotocol.io/specification/2026-07-28/server/resources.md),
[prompts](https://modelcontextprotocol.io/specification/2026-07-28/server/prompts.md). Use a tool
when the model should decide to act; a resource when the host application should attach context; a
prompt when the user should explicitly select a workflow. Do not expose everything as a tool.

### 3.2 Tool naming and descriptions

The current tools reference says "Tool names SHOULD be between 1 and 128 characters" and allows
`[A-Za-z0-9_.-]`, while SEP-986 says "1–64 characters … and forward slashes (/)" —
[tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md),
[SEP-986](https://modelcontextprotocol.io/seps/986-specify-format-for-tool-names). The safe
intersection is 1–64 characters with no slash. Names should be unique within a server; aggregating
clients may prefix them to disambiguate. Descriptions matter: they are what the model uses to choose
a tool, so write them for selection, not for humans.

### 3.3 Schemas and structured output

`inputSchema` defaults to JSON Schema 2020-12 and must be a valid schema object; `outputSchema` is
optional but recommended. When an output schema is present, code-mode clients can generate precise
return types — [tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md),
[client best practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices).
`structuredContent` may be any JSON value; SEP-2106 requires that "servers using array or primitive
`structuredContent` MUST also emit a `TextContent` block containing the serialized JSON" —
[SEP-2106](https://modelcontextprotocol.io/seps/2106-json-schema-2020-12). For backwards
compatibility, a tool returning structured content should also include the serialized JSON as text.

### 3.4 Error handling

There are two error channels. Protocol errors indicate a malformed request and are "less likely to
result in successful recovery"; tool execution errors are returned with `isError: true` so the model
can "self-correct and retry" — [tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md).
SEP-1303 states "Only Tool Execution Errors are forwarded back to the model" and that "Tool Execution
Errors should be used for all tool argument validation failures" —
[SEP-1303](https://modelcontextprotocol.io/seps/1303-input-validation-errors-as-tool-execution-errors).
In practice: return `isError: true` with an actionable message for bad arguments and business-logic
failures; reserve JSON-RPC errors for protocol-level problems.

### 3.5 Annotations and safety hints

Tool annotations are untrusted hints with unsafe defaults: `readOnlyHint` defaults to `false`,
`destructiveHint` to `true`, `idempotentHint` to `false`, and `openWorldHint` to `true`; "clients
MUST consider tool annotations to be untrusted unless they come from trusted servers" —
[schema](https://modelcontextprotocol.io/specification/2026-07-28/schema.md),
[tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md). Set them
accurately anyway: they inform host consent UI and safety decisions.

### 3.6 State, pagination, and caching

There is no protocol session: "MCP has no protocol-level session, so a server cannot rely on
implicit per-connection state." Servers needing state should return an explicit handle from a
creation tool and accept it as an argument later; handles should be opaque, authorized per call, and
bounded in lifetime — [tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md).
List operations use opaque cursors; clients must not assume a fixed page size, and invalid cursors
should yield `-32602` — [pagination](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/pagination.md).
Caching is HTTP-like and mandatory on complete results: `ttlMs` is "analogous to HTTP
`Cache-Control: max-age`," `cacheScope` is `public` or `private`, and "Servers MUST apply the same
`cacheScope` to all response pages" — [caching](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching.md).

### 3.7 Interactive and long-running work

Server→client input uses MRTR only, on `prompts/get`, `resources/read`, and `tools/call`; the server
returns an `InputRequiredResult` and the client retries. `requestState` is "attacker-controlled
input" and must be integrity-protected — [MRTR](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr.md).
For genuinely long-running work, the Tasks extension returns a durable handle instead of blocking —
[tasks](https://modelcontextprotocol.io/extensions/tasks/overview).

### 3.8 Scaling the tool surface

"Loading every tool definition into the model's context window upfront wastes tokens, increases
latency, and degrades model performance" — [client best practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices).
Two patterns help: progressive discovery (a `search_tools` meta-tool plus on-demand detail) and
programmatic tool calling or "code mode," where the model writes sandboxed code and "only the final
result returns to the model" — same source. Server-side prerequisites are accurate descriptions,
deterministic ordering, and `outputSchema` — same source.

---

## 4. Development workflow and tooling

> Detail: [development/04-development-workflow-tooling.md](development/04-development-workflow-tooling.md)

The official server quickstart follows: scaffold a project, instantiate the server, implement typed
tool handlers, run the server, and test it in a host — [build a server](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server).
Python uses decorators such as `@mcp.tool()` with type hints and docstrings; TypeScript uses
`server.registerTool(...)` with a Zod input schema — same source. A clean layout separates the server
instance, tool definitions, and tests; the CircleCI FastMCP walkthrough uses a `src/` layout with
`server.py` and `tests/` — [CircleCI](https://circleci.com/blog/building-and-deploying-a-python-mcp-server-with-fastmcp).

**The stdio rule.** "Never write to stdout. Writing to stdout will corrupt the JSON-RPC messages and
break your server." Use the standard logging module (Python) or `console.error()` (TypeScript) so
logs go to stderr; HTTP servers are exempt — [build a server](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server).

**The Inspector** is the reference developer tool: "three clients behind one binary" — Web
(`npx @modelcontextprotocol/inspector`), CLI (`--cli`), and TUI (`--tui`) — requiring Node 22.19.0 or
newer — [Inspector](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector). The CLI is
scriptable and machine-readable, which makes it usable in CI — same source.

**Debugging.** Common issues: an undefined working directory (use absolute paths), a limited
inherited environment for stdio servers, and the diagnostic error ladder `-32022`
(UnsupportedProtocolVersionError), `-32602` (malformed/missing `_meta`), and `-32021`
(MissingRequiredClientCapabilityError) — [debugging](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging).
For HTTP servers, stderr is not captured by the client, so use server-side log aggregation or
OpenTelemetry — same source.

**Connecting to hosts.** Local servers are configured in the host's MCP config (for example Claude
Desktop, VS Code, Cursor); remote servers are added by URL over Streamable HTTP —
[connect local](https://modelcontextprotocol.io/docs/2026-07-28/develop/connect-local-servers),
[connect remote](https://modelcontextprotocol.io/docs/2026-07-28/develop/connect-remote-servers).
Restart the host after server code changes; for Claude Desktop, fully quit and reopen — [debugging](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging).

## 5. Testing, conformance, and CI

> Detail: [development/05-testing-conformance-ci.md](development/05-testing-conformance-ci.md)

A practical test pyramid for MCP servers:

1. **Unit tests** for business logic and schema validation, including schema-violating inputs and
   error paths that must return proper MCP errors rather than crash —
   [Signadot](https://www.signadot.com/testing-mcp-servers).
2. **In-memory integration tests** that connect a real client to the real server without a
   subprocess or socket, exercising the protocol end to end against actual handlers. This catches
   schema drift, capability mismatches, and error-shape regressions quickly —
   [Hidekazu Konishi](https://hidekazu-konishi.com/entry/mcp_server_testing_and_debugging_guide.html).
   Both official SDKs ship an in-memory transport for this; TypeScript uses
   `InMemoryTransport.createLinkedPair()` and Python uses `Client(app)` — same source.
3. **Inspector manual/scripted checks** against the protocol surface —
   [Inspector](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector).
4. **End-to-end tests** with a real host and real dependencies —
   [Signadot](https://www.signadot.com/testing-mcp-servers).

For CI, the Inspector CLI is purpose-built: "Each CLI run connects to a server, invokes the single
request you name with `--method`, prints the result, and exits" —
[Inspector CLI](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/cli). Exit codes are
a stable contract (`3` auth, `4` unreachable, `5` tool error, `6` strict schema problem), and you
should pin the Inspector version because "A range like `@2` is not a pin" —
[smoke-testing guide](https://raw.githubusercontent.com/modelcontextprotocol/inspector/main/docs/cli-smoke-testing.md).

Conformance is now part of the specification process: "Before a Standards Track SEP that changes
observable protocol behavior can be marked `Final`, a conformance scenario … must be merged into the
conformance repository" — [SEP-2484](https://modelcontextprotocol.io/seps/2484-conformance-tests-required-for-final-seps).
SDK conformance is scored by tier (100% / 80% / none) — [SDK tiering](https://modelcontextprotocol.io/community/sdk-tiers).
The conformance repository also supports baselines that fail on stale entries —
[conformance](https://github.com/modelcontextprotocol/conformance).

Security testing is separate from functional testing: "MCP Inspector does not automatically determine
whether an implementation is secure" — [Aembit](https://aembit.io/blog/mcp-security-testing). Design
adversarial cases for token audience, token passthrough, per-client consent, scope minimization, and
SSRF, and verify them with custom harnesses and logs — same source.

---

## 6. Deployment and hosting

> Detail: [development/06-deployment-hosting.md](development/06-deployment-hosting.md)

### 6.1 Transport choice

Use **stdio** for local, single-user servers launched by a host; use **Streamable HTTP** for remote
or multi-user servers. Streamable HTTP is the current recommended transport for hosted servers —
[Docker remote MCP](https://docs.docker.com/ai/docker-agent/features/remote-mcp). The 2026-07-28
revision removed protocol-level sessions and the `Mcp-Session-Id` header, and made the protocol
stateless: "all the information needed to process a request is contained in the request itself" —
[base protocol](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md),
[Streamable HTTP](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md).
This is what makes horizontal scaling and serverless hosting practical: any replica can serve any
request.

### 6.2 Packaging local servers

TypeScript servers "can be used directly with `npx`"; Python servers "can be used with `uvx`
(recommended) or `pip`" — [examples](https://modelcontextprotocol.io/examples). For one-click
distribution, MCP Bundles are "zip archives containing a local MCP server and a `manifest.json`" —
[mcpb](https://github.com/modelcontextprotocol/mcpb). The MCPB guidance recommends Node.js over
Python "to reduce installation friction" — same source. The manifest spec is v0.3, with v0.4 adding
a `uv` server type — [MANIFEST.md](https://github.com/modelcontextprotocol/mcpb/blob/main/MANIFEST.md).

### 6.3 Containers and Kubernetes

Containerizing a Streamable HTTP server is straightforward: build an image, expose the MCP endpoint,
and point clients at the URL. Docker Agent supports remote MCP over Streamable HTTP, SSE, and Unix
domain sockets, with built-in OAuth handling — [Docker remote MCP](https://docs.docker.com/ai/docker-agent/features/remote-mcp).
On Kubernetes, ToolHive provides an operator that deploys an MCP server as a custom resource with the
transport set to Streamable HTTP and exposes a proxy URL —
[ToolHive](https://github.com/stacklok/toolhive). A gateway/proxy in front of MCP servers is a common
pattern for auth, rate limiting, and multi-tenant routing, but it introduces the confused-deputy risk
described in section 7.

### 6.4 Serverless

Statelessness makes serverless a natural fit. AWS documents building a "serverless remote MCP server"
using Streamable HTTP and Lambda — [AWS Builder](https://builder.aws.com/content/2s44xHTSbQgo2Ws2bJr6hZsECGr/building-a-serverless-remote-mcp-server-on-aws-part-1).
Serverless Framework v4 can deploy an MCP server to Lambda with a few lines of YAML, giving "a real
HTTPS endpoint, response streaming, and AWS Lambda's pay-per-request pricing" —
[Serverless Framework](https://www.serverless.com/blog/deploy-mcp-servers-on-aws-lambda-with-serverless-framework-v4).
Cloudflare Workers are positioned for edge/serverless MCP — [Cloudflare Agents](https://developers.cloudflare.com/agents/).
Azure Container Apps can host remote MCP servers with a container image and environment variables —
[Azure Container Apps](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550).
Google Cloud Run supports Streamable HTTP but "not MCP servers with stdio transport" —
[Cloud Run MCP](https://docs.cloud.google.com/run/docs/host-mcp-servers).

### 6.5 Operational concerns

Streaming has specific proxy requirements: servers "SHOULD include the `X-Accel-Buffering: no`
header," and "Resumable SSE streams via `Last-Event-ID` are not supported" —
[Streamable HTTP](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md).
Because a broken response stream loses the in-flight request, clients must re-issue it as a new
request — same source. Watch cold starts and request timeouts on serverless platforms, and use the
Tasks extension for work that exceeds a platform's timeout. For local HTTP servers, bind to
`127.0.0.1` and validate the `Origin` header — same source.

---

## 7. Security engineering

> Detail: [development/07-security-engineering.md](development/07-security-engineering.md)

### 7.1 Threat model

A server author should assume: the client may be malicious or compromised; tool descriptions and
results are untrusted data; the network is hostile; and the server may be reachable by many users.
The official security best-practices page "identifies security risks, attack vectors, and best
practices specific to MCP implementations" —
[security best practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md).

### 7.2 Authentication and authorization

Authorization is optional but strongly recommended for remote servers. A protected server acts as an
OAuth 2.1 resource server and MUST publish RFC 9728 Protected Resource Metadata with an
`authorization_servers` field — [authorization](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md),
[discovery](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/authorization-server-discovery.md).
Servers MUST validate that tokens were issued specifically for them as the intended audience, and
"MCP servers MUST NOT accept any tokens that were not explicitly issued for the MCP server" —
[security best practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md).
"MCP servers MUST NOT accept or transit any other tokens" — [authorization](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md).
Never pass the client's token to an upstream API; obtain a separate token for the upstream service —
[security considerations](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/security-considerations.md).

### 7.3 State handles and sessions

With protocol sessions removed, the current risk is state-handle hijacking. "MCP servers MUST NOT
treat possession of a state handle as authentication," should use secure random handles, and should
bind handles server-side to the authenticated user, for example as `<user_id>:<handle>` —
[security best practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md).

### 7.4 Input validation and injection

Validate all tool arguments against strict schemas and enforce path boundaries to prevent directory
traversal. Validation failures should be returned as tool execution errors so the model can correct
them: "Tool Execution Errors should be used for all tool argument validation failures" —
[SEP-1303](https://modelcontextprotocol.io/seps/1303-input-validation-errors-as-tool-execution-errors).
Never pass model-supplied strings to a shell; use argument arrays and allowlists. For SSRF, "Avoid
implementing IP validation manually. Attackers exploit encoding tricks (octal, hex, IPv4-mapped
IPv6) that custom parsers often miss" — [security best practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md).

### 7.5 Tool poisoning and prompt injection

Tool descriptions and tool results are untrusted input to the model. A documented attack is
description drift: "a malicious server can change the tool description after the client has already
approved it" — [Invariant Labs](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).
Mitigations include pinning the server and tool versions, treating tool output as untrusted, and
requiring user consent for sensitive actions — same source. Servers should also avoid embedding
instructions in tool results that could hijack the model.

### 7.6 Supply chain

Dependency and package provenance matter. A documented incident is CVE-2025-6514 in `mcp-remote`,
rated "CVSS score of 9.6 out of 10," in a package "downloaded more than 437,000 times" —
[Docker](https://www.docker.com/blog/mcp-horror-stories-the-supply-chain-attack/). Pin dependencies,
prefer official packages, verify hashes (MCPB clients validate `fileSha256`), and scan dependencies
in CI.

### 7.7 Local server consent and sandboxing

"If an MCP client supports one-click local MCP server configuration, it MUST implement proper consent
mechanisms prior to executing commands," showing the exact untruncated command —
[security best practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md);
SEP-1024 backs this requirement — [SEP-1024](https://modelcontextprotocol.io/seps/1024-mcp-client-security-requirements-for-local-server-.md).
For servers that execute code or access the filesystem, run with least privilege and sandbox the
process. In proxy architectures that spawn stdio servers, sandbox, restrict filesystem access, log
usage, and require extra authorization — same source.

### 7.8 Secrets and logging

Never embed credentials in code; use environment variables or a secret store —
[authorization tutorial](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization.md).
Do not log tokens or secrets, and remember that `x-mcp-header` values are visible to network
intermediaries, so sensitive parameters should not be mirrored into headers —
[tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md).

---

## 8. Observability, performance, and cost

> Detail: [development/08-observability-performance.md](development/08-observability-performance.md)

### 8.1 Tracing and logging

The 2026-07-28 base protocol reserves `traceparent`, `tracestate`, and `baggage` in `_meta` for
OpenTelemetry trace-context propagation — [base protocol](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md).
SEP-414 documents the conventions and warns that namespacing these keys "will break traces and log
correlation" — [SEP-414](https://modelcontextprotocol.io/seps/414-request-meta). Protocol logging is
deprecated: "New implementations SHOULD NOT adopt it; existing implementations SHOULD migrate to
logging to `stderr` … or to OpenTelemetry" —
[logging](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/logging.md).
FastMCP provides OpenTelemetry instrumentation — [FastMCP updates](https://gofastmcp.com/updates).
The OpenTelemetry MCP semantic conventions exist but are marked Development, so attribute names may
change — [semantic-conventions-genai](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/mcp.md).

### 8.2 Caching and cost

Caching hints are mandatory on complete results: "Servers MUST include caching hints on results with
`resultType: "complete"`" and "Servers MUST provide a `ttlMs` value that is `>= 0`" —
[caching](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching.md).
Deterministic tool ordering protects prompt caches: "Deterministic ordering enables clients to
reliably cache the tool list and improves LLM prompt cache hit rates," and "Adding or removing tool
definitions mid-conversation invalidates that cache" —
[tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md),
[client best practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices).

Tool count is a first-order cost driver. The client best-practices page contrasts loading every
definition (roughly "150,000 tokens on definitions alone") with progressive discovery (roughly
"2,000 tokens") — [client best practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices).
Anthropic reports a reduction "from 150,000 tokens to 2,000 tokens—a time and cost saving of 98.7%"
for code execution with MCP — [Anthropic](https://www.anthropic.com/engineering/code-execution-with-mcp).
Design implication: keep the always-loaded tool surface small, make descriptions precise, and let
clients discover the rest on demand.

### 8.3 Latency and backpressure

Progress notifications are opt-in via `progressToken` and must stop after completion; both parties
should rate-limit to prevent flooding — [progress](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/progress.md).
Implement timeouts for all requests and enforce a maximum even when progress resets the clock —
[cancellation](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/cancellation.md).
For long operations, prefer the Tasks extension over holding a request open.

## 9. Publishing and distribution

> Detail: [development/09-publishing-distribution.md](development/09-publishing-distribution.md)

The official MCP Registry is "the official centralized metadata repository for publicly accessible
MCP servers." It hosts metadata, not artifacts: "The MCP Registry hosts metadata that points to those
packages" — [Registry](https://modelcontextprotocol.io/registry/about). It is in preview, "does not
support private servers," is "not intended to be directly consumed by host applications," and its
codebase "is not designed for self-hosting" — same source. It also "does not provide uptime or data
durability guarantees" — [aggregators](https://modelcontextprotocol.io/registry/registry-aggregators).

Publishing uses `server.json` and the `mcp-publisher` CLI (`init`, `login`, `logout`, `publish`).
"The `name` property in `server.json` must match the `mcpName` property in `package.json`" —
[quickstart](https://modelcontextprotocol.io/registry/quickstart). Each package type has an ownership
proof: npm `mcpName`; PyPI/NuGet/Cargo an `mcp-name: $SERVER_NAME` token in the README; OCI an
`io.modelcontextprotocol.server.name` label; MCPB a URL containing "mcp" plus a `fileSha256` —
[package types](https://modelcontextprotocol.io/registry/package-types). A Cargo-specific trap:
"crates.io strips HTML comments during markdown→HTML conversion," so the hidden-comment token that
works for PyPI/NuGet does not work for Cargo — same source. The MCPB hash is client-verified, not
registry-verified — same source.

Remote servers must be publicly accessible and should use Streamable HTTP; SSE is deprecated —
[remote servers](https://modelcontextprotocol.io/registry/remote-servers). Versions are immutable
once published and version ranges are prohibited — [registry versioning](https://modelcontextprotocol.io/registry/versioning).
The authentication method determines the namespace: GitHub authentication yields `io.github.*`, while
DNS/HTTP authentication enables a custom reverse-DNS domain —
[registry authentication](https://modelcontextprotocol.io/registry/authentication). GitHub Actions
can publish on tag push, with OIDC recommended —
[GitHub Actions](https://modelcontextprotocol.io/registry/github-actions). Moderation is permissive:
"We only remove illegal content, malware, spam, and completely broken servers," and "consumers should
assume minimal-to-no moderation" — [moderation policy](https://modelcontextprotocol.io/registry/moderation-policy).
Downstream aggregators and marketplaces are the intended consumer of the Registry —
[aggregators](https://modelcontextprotocol.io/registry/registry-aggregators).

---

## 10. A practical build checklist (synthesis)

This checklist is the report's own synthesis from the sources above.

1. **Pick a Tier 1 SDK** whose supported protocol versions include 2026-07-28; verify before
   committing, because adoption is uneven.
2. **Choose a framework** if it removes boilerplate: FastMCP for Python; official SDK v2 plus
   mcp-use or MCP-Framework for TypeScript; Spring AI for Java.
3. **Design the primitive surface**: tools for model actions, resources for application context,
   prompts for user workflows. Keep the always-loaded tool set small.
4. **Write schemas and descriptions for the model**: valid JSON Schema 2020-12 `inputSchema`,
   optional `outputSchema`, precise descriptions, deterministic ordering.
5. **Handle errors in two channels**: `isError: true` for argument/business failures; JSON-RPC
   errors for protocol failures.
6. **Keep no implicit state**: explicit handles or integrity-protected `requestState`; never treat a
   handle as authentication.
7. **Attach caching hints** (`ttlMs`, `cacheScope`) on all complete list/read/discover results.
8. **Use MRTR** for server→client input; use the Tasks extension for long-running work.
9. **Test at three levels**: unit, in-memory client/server integration, and Inspector/end-to-end;
   run the Inspector CLI in CI with a pinned version.
10. **Secure the server**: audience-bound tokens, no token passthrough, strict input validation,
    least privilege, sandboxing, no secrets in logs, and supply-chain scanning.
11. **Instrument it**: OpenTelemetry trace context via `_meta`, structured logs to stderr or OTel,
    and metrics for latency, errors, and tool usage.
12. **Deploy appropriately**: stdio for local, Streamable HTTP for remote; containers or serverless
    now that the protocol is stateless; watch streaming/proxy and timeout behavior.
13. **Publish deliberately**: package first, then Registry; match the ownership proof to the package
    type; use immutable versions and OIDC-based CI.

## 11. Open questions and caveats

- **SDK protocol-version lag.** Some SDKs (notably Swift) still target 2025-11-25; always check the
  SDK's current supported versions before relying on 2026-07-28 features.
- **Tool-name length conflict.** The current tools reference says 1–128 characters; SEP-986 says
  1–64. The safe intersection is 1–64 with no slash.
- **OWASP MCP Top 10 wording** was quoted from a vendor guide rather than the primary OWASP project
  page; treat the exact category wording as unverified.
- **OpenTelemetry MCP semantic conventions** are Development status and may change.
- **Registry is preview** and may reset data; do not treat listing as durable or as a security
  endorsement.
- **Some deployment sources** (AWS Builder, Serverless Framework, Azure Container Apps) could not be
  fetched directly and were captured via search indexes; treat their specifics as lower confidence.
- **One retrieval failure** was recorded: a guessed FastMCP OpenTelemetry page returned 404; the
  correct page is `https://gofastmcp.com/servers/telemetry.md`.

---

## Resources

All source URLs referenced in this report, deduplicated.

**Official MCP documentation and specification**
- https://modelcontextprotocol.io/docs/2026-07-28/sdk
- https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server
- https://modelcontextprotocol.io/docs/2026-07-28/develop/connect-local-servers
- https://modelcontextprotocol.io/docs/2026-07-28/develop/connect-remote-servers
- https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices
- https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector
- https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/cli
- https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging
- https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md
- https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization.md
- https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md
- https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr.md
- https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/progress.md
- https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/cancellation.md
- https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio.md
- https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md
- https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md
- https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/authorization-server-discovery.md
- https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/security-considerations.md
- https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md
- https://modelcontextprotocol.io/specification/2026-07-28/server/resources.md
- https://modelcontextprotocol.io/specification/2026-07-28/server/prompts.md
- https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching.md
- https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/pagination.md
- https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/logging.md
- https://modelcontextprotocol.io/specification/2026-07-28/schema.md
- https://modelcontextprotocol.io/community/sdk-tiers
- https://modelcontextprotocol.io/extensions/tasks/overview
- https://modelcontextprotocol.io/examples

**Official SDKs**
- https://github.com/modelcontextprotocol/typescript-sdk
- https://github.com/modelcontextprotocol/python-sdk
- https://py.sdk.modelcontextprotocol.io/whats-new/
- https://github.com/modelcontextprotocol/csharp-sdk
- https://github.com/modelcontextprotocol/go-sdk
- https://github.com/modelcontextprotocol/rust-sdk
- https://github.com/modelcontextprotocol/ruby-sdk
- https://github.com/modelcontextprotocol/java-sdk
- https://github.com/modelcontextprotocol/kotlin-sdk
- https://github.com/modelcontextprotocol/swift-sdk
- https://github.com/modelcontextprotocol/php-sdk

**Frameworks and libraries**
- https://gofastmcp.com/getting-started/welcome
- https://gofastmcp.com/updates
- https://github.com/PrefectHQ/fastmcp
- https://github.com/QuantGeekDev/mcp-framework
- https://github.com/mcp-use/mcp-use
- https://docs.spring.io/spring-ai/reference/api/mcp/mcp-overview.html
- https://github.com/googleapis/genai-toolbox
- https://github.com/lastmile-ai/mcp-agent

**Testing, conformance, and tooling**
- https://github.com/modelcontextprotocol/inspector
- https://raw.githubusercontent.com/modelcontextprotocol/inspector/main/docs/cli-smoke-testing.md
- https://github.com/modelcontextprotocol/conformance
- https://hidekazu-konishi.com/entry/mcp_server_testing_and_debugging_guide.html
- https://www.signadot.com/testing-mcp-servers
- https://aembit.io/blog/mcp-security-testing

**Deployment and hosting**
- https://docs.docker.com/ai/docker-agent/features/remote-mcp
- https://github.com/stacklok/toolhive
- https://builder.aws.com/content/2s44xHTSbQgo2Ws2bJr6hZsECGr/building-a-serverless-remote-mcp-server-on-aws-part-1
- https://www.serverless.com/blog/deploy-mcp-servers-on-aws-lambda-with-serverless-framework-v4
- https://developers.cloudflare.com/agents/
- https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550
- https://docs.cloud.google.com/run/docs/host-mcp-servers
- https://github.com/modelcontextprotocol/mcpb
- https://github.com/modelcontextprotocol/mcpb/blob/main/MANIFEST.md

**Security**
- https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks
- https://www.docker.com/blog/mcp-horror-stories-the-supply-chain-attack/

**Observability and performance**
- https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/mcp.md
- https://www.anthropic.com/engineering/code-execution-with-mcp

**Registry and publishing**
- https://modelcontextprotocol.io/registry/about
- https://modelcontextprotocol.io/registry/quickstart
- https://modelcontextprotocol.io/registry/package-types
- https://modelcontextprotocol.io/registry/remote-servers
- https://modelcontextprotocol.io/registry/versioning
- https://modelcontextprotocol.io/registry/authentication
- https://modelcontextprotocol.io/registry/github-actions
- https://modelcontextprotocol.io/registry/moderation-policy
- https://modelcontextprotocol.io/registry/registry-aggregators

**Specification Enhancement Proposals**
- https://modelcontextprotocol.io/seps/414-request-meta
- https://modelcontextprotocol.io/seps/986-specify-format-for-tool-names
- https://modelcontextprotocol.io/seps/1024-mcp-client-security-requirements-for-local-server-.md
- https://modelcontextprotocol.io/seps/1303-input-validation-errors-as-tool-execution-errors
- https://modelcontextprotocol.io/seps/2106-json-schema-2020-12
- https://modelcontextprotocol.io/seps/2484-conformance-tests-required-for-final-seps

---

### Working files

Per-topic evidence files with full quotations and retrieval logs are in `development/`:

- [development/01-sdks-languages.md](development/01-sdks-languages.md)
- [development/02-frameworks-libraries.md](development/02-frameworks-libraries.md)
- [development/03-server-design-patterns.md](development/03-server-design-patterns.md)
- [development/04-development-workflow-tooling.md](development/04-development-workflow-tooling.md)
- [development/05-testing-conformance-ci.md](development/05-testing-conformance-ci.md)
- [development/06-deployment-hosting.md](development/06-deployment-hosting.md)
- [development/07-security-engineering.md](development/07-security-engineering.md)
- [development/08-observability-performance.md](development/08-observability-performance.md)
- [development/09-publishing-distribution.md](development/09-publishing-distribution.md)

Round 1 (protocol knowledge) is in [mcp-protocol.md](mcp-protocol.md) and `protocol/`.

Retrieval date for all sources: 2026-10-03.
