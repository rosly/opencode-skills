# MCP Servers for LLM Agents — Deep Research Report

Research date: 2026-10-02
Current protocol revision at time of research: **2026-07-28**
Primary sources: official Model Context Protocol documentation, specification, SEP registry, and GitHub releases.

Sources are cited inline as links next to the statements they support. A single consolidated
list of all referenced URLs appears in the final "Resources" section. This report is a synthesis
of official material; where it draws a conclusion rather than restating a source, the sentence
says so explicitly (for example, "This implies…"). It does not use evidence tags.

Topic working files for each area are stored alongside this report in the same `research/` folder.

---

## 1. What MCP is, and where a server fits

MCP is defined by its own documentation as "an open-source standard for connecting AI applications
to external systems," spanning "data sources (e.g. local files, databases), tools (e.g. search
engines, calculators) and workflows (e.g. specialized prompts)" — [intro](https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro.md).
The protocol's own analogy is "a USB-C port for AI applications" — same source. Crucially, it sets
a scope boundary: "MCP focuses solely on the protocol for context exchange—it does not dictate how
AI applications use LLMs or manage the provided context" — [architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture.md).

MCP uses a host/client/server model. The host is "the AI application that coordinates and manages
one or multiple MCP clients"; a client "maintains a connection to an MCP server and obtains context
from an MCP server for the MCP host to use"; and a server is "a program that provides context to MCP
clients" — [architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture.md).
The host "creates and manages multiple client instances," "controls client connection permissions
and lifecycle," "enforces security policies and consent requirements," and "manages context
aggregation across clients" — [spec architecture](https://modelcontextprotocol.io/specification/2026-07-28/architecture/index.md).
A server "expose[s] resources, tools and prompts via MCP primitives," "operate[s] independently
with focused responsibilities," and "must respect security constraints" — same source.

MCP separates a **data layer** (the JSON-RPC based protocol: discovery, primitives, notifications)
from a **transport layer** (stdio or Streamable HTTP; connection establishment, framing,
authorization) — [architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture.md).
The transport layer "abstracts communication details from the protocol layer, enabling the same
JSON-RPC 2.0 message format across all transport mechanisms" — same source. A server's handler
logic is therefore transport-independent; only connection setup and framing differ.

Four architecture design principles guide the protocol: servers "should be extremely easy to build,"
should be "highly composable," "should not be able to read the whole conversation, nor 'see into'
other servers," and "features can be added to servers and clients progressively" — [spec architecture](https://modelcontextprotocol.io/specification/2026-07-28/architecture/index.md).
The community adds eight more: convergence over choice, composability over specificity,
interoperability over optimization, stability over velocity, capability over compensation,
demonstration over deliberation, pragmatism over purity, and standardization over innovation —
[design principles](https://modelcontextprotocol.io/community/design-principles.md). The "stability
over velocity" principle states: "Removing from [a protocol as widely adopted as MCP] is nearly
impossible. Every addition is a permanent commitment" — same source.

A server can run locally or remotely: "MCP servers can execute locally or remotely"
— [architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture.md).
Connection cardinality differs by transport: local stdio servers "typically serve a single MCP
client," while remote Streamable HTTP servers "will typically serve many MCP clients" — same source.

---

## 2. Protocol history and revision matrix

The protocol is versioned by date in `YYYY-MM-DD` form, "to indicate the last date backwards
incompatible changes were made"; backwards-compatible changes do not bump the date —
[versioning](https://modelcontextprotocol.io/specification/versioning). Revisions carry one of three
states: Draft, Current, or Final; "The **current** protocol version is 2026-07-28" — same source.

The official GitHub release list enumerates: `2024-10-07`, `2024-11-05`, `2024-11-05-final`,
`2025-03-26`, `2025-06-18`, `2025-11-25-RC`, `2025-11-25`, `2026-07-28-RC`, `2026-07-28`, with
`2026-07-28` labelled "Latest" and released 28 Jul 16:47, and `2025-11-25` as the prior stable
release — [releases](https://github.com/modelcontextprotocol/modelcontextprotocol/releases).
Release candidates explicitly warn "this specification is not final" and that "SDKs will adopt this
version at their own pace" — same source.

Revision headline changes, drawn from each revision's official changelog:

**2024-11-05 / 2024-10-07** — the initial revision. The release notes describe only
"This release marks the initial 2024-11-05 revision"; a per-change changelog for this revision was
not fetched — [releases](https://github.com/modelcontextprotocol/modelcontextprotocol/releases).

**2025-03-26** — "Added a comprehensive **authorization framework** based on OAuth 2.1,"
"Replaced the previous HTTP+SSE transport with a more flexible **Streamable HTTP transport**,"
"Added support for JSON-RPC **batching**," and "Added comprehensive **tool annotations**" —
[2025-03-26 changelog](https://modelcontextprotocol.io/specification/2025-03-26/changelog.md).

**2025-06-18** — "Remove support for JSON-RPC batching"; "Add support for structured tool output";
"Classify MCP servers as OAuth Resource Servers"; "Require MCP clients to implement Resource
Indicators as described in RFC 8707"; "Add support for elicitation"; "Add support for resource links
in tool call results"; and "Require negotiated protocol version to be specified via
`MCP-Protocol-Version` header in subsequent requests when using HTTP" —
[2025-06-18 changelog](https://modelcontextprotocol.io/specification/2025-06-18/changelog.md).

**2025-11-25** — "Enhance authorization server discovery with support for OpenID Connect Discovery
1.0," incremental scope consent via `WWW-Authenticate`, icons for tools/resources/prompts, tool-name
guidance, URL mode elicitation, tool calling support in sampling, OAuth Client ID Metadata Documents,
and "experimental support for tasks" — [2025-11-25 changelog](https://modelcontextprotocol.io/specification/2025-11-25/changelog.md).
It also established JSON Schema 2020-12 as the default dialect and formalized governance, working
groups, and the SDK tiering system — same source.

**2026-07-28 (current)** — the largest architectural change. Its changelog's major changes:
remove protocol-level sessions and the `Mcp-Session-Id` header; "Make MCP stateless: remove the
`initialize`/`notifications/initialized` handshake"; add the mandatory `server/discover` RPC;
replace the HTTP GET endpoint and `resources/subscribe`/`unsubscribe` with `subscriptions/listen`;
remove `ping`, `logging/setLevel`, and `notifications/roots/list_changed`; move experimental tasks
into an official extension; introduce Multi Round-Trip Requests (MRTR) replacing server-initiated
requests; require a `resultType` on all results; and remove SSE stream resumability —
[2026-07-28 changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog.md).
This revision also deprecates Roots, Sampling, and Logging, and formalizes a feature lifecycle and
deprecation policy with a deprecated-features registry — same source.

The current revision uses the terms "Modern" (per-request metadata, 2026-07-28 and later) and
"Legacy" (session with an `initialize` handshake, 2025-11-25 and earlier); an implementation
supporting both is "Dual-era" — [versioning and compatibility](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md).
The compatibility matrix states modern-client/legacy-server "Fails," and legacy-client/modern-server
also "Fails" because "Legacy clients have no fall-forward mechanism" — same source.

---

## 3. The current protocol model (2026-07-28)

### 3.1 Statelessness and the base protocol

"All implementations MUST support the base protocol, versioning, and the message patterns," and
"All messages between MCP clients and servers MUST follow the JSON-RPC 2.0 specification" —
[basic protocol](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md).
The protocol is stateless: "all the information needed to process a request is contained in the
request itself… no state should be inferred from previous requests, even those on the same
connection or stream" — same source. "State that needs to span multiple requests (e.g., long-running
tasks, application-level handles) MUST be referenced by an explicit identifier the client passes on
each request" — same source.

A critical directionality rule: "Servers MUST NOT initiate JSON-RPC requests, and clients do not
send JSON-RPC responses" — [message patterns](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/index.md).
There is no handshake: "There is no negotiation handshake. Every request carries its protocol
version, and the server accepts or rejects each request independently" —
[versioning](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md).

### 3.2 `_meta` and per-request metadata

Every client request carries `_meta` fields: `io.modelcontextprotocol/protocolVersion` and
`io.modelcontextprotocol/clientCapabilities` are **required**; `clientInfo` is recommended; and
`io.modelcontextprotocol/logLevel` is optional — [basic protocol](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md).
A request missing a required field is "malformed; the server MUST reject it with JSON-RPC error code
`-32602` (Invalid params). On HTTP, the response status MUST be `400 Bad Request`" — same source.
Servers should include `io.modelcontextprotocol/serverInfo` in results, but both client and server
identity are "self-reported by the sender and are not verified by the protocol" and must not be used
for security decisions — same source. Reserved keys also include `progressToken` and
`io.modelcontextprotocol/subscriptionId`; OpenTelemetry `traceparent`, `tracestate`, and `baggage`
are reserved for trace-context propagation — same source.

### 3.3 Error codes

Standard JSON-RPC codes cover general failures. MCP partitions the JSON-RPC server-error range:
`-32000` to `-32019` is legacy (new codes MUST NOT be allocated there); `-32020` to `-32099` is
reserved for the specification — [basic protocol](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md).
This revision defines `-32020` HeaderMismatch, `-32021` MissingRequiredClientCapability, and
`-32022` UnsupportedProtocolVersion; implementations MUST NOT emit retired codes `-32002` or
`-32042`, though clients SHOULD still accept `-32002` from older servers — same source. New
application-defined codes SHOULD be allocated below `-32768` — same source.

### 3.4 Multi Round-Trip Requests (MRTR)

MRTR is the headline interaction change. "Servers MUST send server-to-client requests (such as
`roots/list`, `sampling/createMessage`, or `elicitation/create`) using the MRTR pattern. The previous
pattern of server-initiated requests is no longer supported. This is a breaking change" —
[MRTR](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr.md).
The flow: the client sends a request; the server replies with an `InputRequiredResult`
(`resultType: "input_required"`) containing `inputRequests`; the client gathers the information and
retries the original request with `inputResponses`; the server then returns the final result — same
source. MRTR is allowed only on `prompts/get`, `resources/read`, and `tools/call`; servers must
include at least one of `inputRequests` or `requestState`; and the retry must use a new JSON-RPC
`id` — same source.

The `requestState` field is the server's state carrier: it is "an opaque string meaningful only to
the server," clients must echo it exactly and must not inspect it, and "servers MUST treat
`requestState` as an attacker-controlled input… MUST protect its integrity (e.g. HMAC or AEAD) and
MUST reject state that fails verification" — [MRTR](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr.md).
Servers SHOULD embed the authenticated principal, a short expiry, and an originating-request
identifier inside the integrity-protected payload to prevent replay — same source. The design
motivation is to avoid a shared storage layer or stateful load balancing — same source.

### 3.5 Subscriptions and notifications

`subscriptions/listen` "opens a long-lived notification stream from the server to the client… It
replaces the former `resources/subscribe` RPC and the HTTP GET endpoint" —
[subscriptions](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/subscriptions.md).
The client names the event types it wants (`toolsListChanged`, `promptsListChanged`,
`resourcesListChanged`, `resourceSubscriptions`); the server MUST NOT send types not requested, MUST
first send `notifications/subscriptions/acknowledged`, and MUST tag every notification with
`io.modelcontextprotocol/subscriptionId` — same source. Request-scoped notifications such as
`notifications/progress` and `notifications/message` flow on the response stream of the request they
relate to, "not… on the listen stream" — same source. On stdio, subscriptions do not survive a
reconnect: "the server holds no subscription state across reconnections" — same source.

### 3.6 Cancellation and progress

Cancellation is transport-specific. On Streamable HTTP, "Closing the SSE response stream is the
cancellation signal. The server MUST treat a client disconnect as cancellation of that request. No
`notifications/cancelled` message is required or expected." On stdio, "the client MUST send a
`notifications/cancelled` notification referencing the request ID" —
[cancellation](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/cancellation.md).
A server may send `notifications/cancelled` only to tear down a `subscriptions/listen` stream —
same source. Progress is opt-in via a `progressToken` in request metadata; `progress` MUST increase
with each notification even if the total is unknown; notifications MUST stop after completion; and
both parties SHOULD rate-limit — [progress](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/progress.md).

### 3.7 Transports

**stdio** launches the server as a subprocess and communicates over standard streams. "Messages are
delimited by newlines, and MUST NOT contain embedded newlines"; "The server MUST NOT write anything
to its `stdout` that is not a valid MCP message"; the server MAY write UTF-8 logs to `stderr`; and
servers "SHOULD exit promptly when their standard input is closed" —
[stdio](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio.md).
There is no header layer; all metadata is inline in the JSON-RPC body — same source.

**Streamable HTTP** exposes one POST endpoint. The revision "changed the behavior of Streamable
HTTP": "Removal of the GET stream endpoint. Removal of protocol-level sessions" —
[streamable HTTP](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md).
"Every POST request to the MCP endpoint MUST include an `MCP-Protocol-Version` header," and the value
MUST match the body's `_meta` protocol version or the server rejects with `400` and a
HeaderMismatch error — same source. `Mcp-Method` and `Mcp-Name` headers are "REQUIRED for
compliance"; optional `x-mcp-header` mirrors primitive tool parameters into `Mcp-Param-{Name}`
headers using a case-sensitive `=?base64?…?=` sentinel — same source. Servers MUST validate the
`Origin` header and respond `403` to invalid origins to prevent DNS rebinding; when local they
SHOULD bind only to `127.0.0.1` — same source. Resumable SSE via `Last-Event-ID` is not supported;
GET/DELETE to the endpoint should return `405`; `Mcp-Session-Id` must be ignored and never minted —
same source.

**HTTP+SSE** (the 2024-11-05 transport) "has been deprecated since protocol version `2025-03-26`
and is classified as Deprecated under the feature lifecycle policy. New implementations SHOULD NOT
adopt it; existing implementations SHOULD migrate to Streamable HTTP" —
[streamable HTTP](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md).
Custom transports are allowed but "MUST preserve the JSON-RPC message format, the message patterns,
and the per-request metadata model" — [transports](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/index.md).

---

## 4. Server primitives

The server surface is three primitives plus discovery. The overview gives the control owner for
each: "Prompts | User-controlled," "Resources | Application-controlled," "Tools | Model-controlled"
— [server overview](https://modelcontextprotocol.io/specification/2026-07-28/server/index.md).

### 4.1 `server/discover` (mandatory)

"`server/discover` lets a client query a server's supported protocol versions, capabilities, and
identity before sending any other requests. Servers MUST implement it" —
[discover](https://modelcontextprotocol.io/specification/2026-07-28/server/discover.md). The response
carries `supportedVersions`, `capabilities`, `serverInfo`, optional `instructions`, and caching
hints (`ttlMs`, `cacheScope`) — same source. Calling it is optional for clients, so a client may
invoke any RPC directly and handle `UnsupportedProtocolVersionError` — same source. On stdio it
doubles as the backward-compatibility probe — same source. `serverInfo` is "self-reported by the
server and is not verified by the protocol" — same source.

### 4.2 Tools

"Tools enable models to interact with external systems, such as querying databases, calling APIs, or
performing computations" and are "model-controlled" — [tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md).
Servers supporting tools MUST declare the `tools` capability, optionally with `listChanged`.
A tool definition includes `name`, optional `title`, `description`, optional `icons`, `inputSchema`,
optional `outputSchema`, and optional `annotations` — same source. `inputSchema` defaults to JSON
Schema 2020-12 and must be a valid schema object — same source. Tool names SHOULD be 1–64
characters, case-sensitive, using `A-Z a-z 0-9 _ - .` (the current tools page lists these
characters) — same source. Because name uniqueness is scoped to a single server, aggregating
clients SHOULD prefix names to disambiguate — same source.

Servers SHOULD return tools in a deterministic order to enable client-side caching and improve LLM
prompt cache hit rates — [tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md).
`tools/list` supports pagination and caching; `tools/call` invokes a tool; change notifications use
`notifications/tools/list_changed` — same source. Results may be unstructured (`content`) or
structured (`structuredContent`); `structuredContent` "is server-produced result data and is
unrelated to LLM 'structured outputs'," and a tool returning structured content SHOULD also include
the serialized JSON in a TextContent block for backwards compatibility — same source. Tool
execution errors should be returned with `isError: true` so models can self-correct, distinct from
protocol errors — same source. Clients MUST treat tool annotations as untrusted unless the server is
trusted — same source.

The optional `x-mcp-header` property mirrors designated tool parameters into HTTP headers. It MUST
be non-empty, match HTTP token syntax, and "MUST only be applied to parameters with primitive types
(integer, string, boolean). Parameters with type `number` are not permitted"; sensitive values
SHOULD NOT be marked this way because headers are visible to intermediaries — [tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md).

For stateful tools, the server should return an explicit handle from a creation tool and accept it
as an argument on later calls; "The protocol has no concept of a state handle; from the wire's
perspective a handle is an ordinary string" — [tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md).

### 4.3 Resources

"Resources allow servers to share data that provides context to language models, such as files,
database schemas, or application-specific information. Each resource is uniquely identified by a
URI" — [resources](https://modelcontextprotocol.io/specification/2026-07-28/server/resources.md). They
are application-driven; servers MUST declare the `resources` capability, with optional `listChanged`
and `subscribe` features — same source. `resources/list` and `resources/templates/list` support
pagination and caching; `resources/read` supports caching and may return multiple content items —
same source. Resource contents are text or base64 `blob`; resource templates use URI templates —
same source. Annotations carry `audience`, `priority`, and `lastModified` — same source. If a
resource does not exist, servers MUST return `-32602` (Invalid Params); they SHOULD return `-32603`
for internal errors, and MUST NOT return an empty `contents` array for a non-existent resource —
same source.

### 4.4 Prompts

"Prompts allow servers to provide structured messages and instructions for interacting with language
models," and are "user-controlled… This refers to who decides when the prompt is used, not who
authors its content" — [prompts](https://modelcontextprotocol.io/specification/2026-07-28/server/prompts.md).
Servers MUST declare the `prompts` capability, optionally with `listChanged`. `prompts/list` supports
pagination and caching; `prompts/get` retrieves a prompt; change notifications use
`notifications/prompts/list_changed` — same source. A prompt has `name`, optional `title`,
`description`, `icons`, and `arguments`; messages have `role` and content (text, image, audio,
resource links, or embedded resources) — same source. Invalid names and missing arguments map to
`-32602`, internal errors to `-32603` — same source.

### 4.5 Server-side utilities

**Completion.** Servers may offer autocompletion for prompt and resource-template arguments via
`completion/complete`, declaring the `completions` capability. Results are ranked, capped at 100
items, with an optional total and a `hasMore` flag — [completion](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/completion.md).

**Logging (deprecated).** "The Logging feature is deprecated as of protocol version `2026-07-28`
(SEP-2577)… New implementations SHOULD NOT adopt it; existing implementations SHOULD migrate to
logging to `stderr` for stdio transports, or to OpenTelemetry" —
[logging](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/logging.md).
The log level is now per-request via `_meta`, and `notifications/message` is request-scoped: "the
server MUST NOT deliver it on a `subscriptions/listen` stream or on any stream other than the one
carrying the response to the request that set the log level" — same source.

**Pagination.** Pagination is cursor-based with an opaque cursor; "Page size is determined by the
server, and clients MUST NOT assume a fixed page size." Clients must treat cursors as opaque, and
invalid cursors SHOULD yield `-32602` — [pagination](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/pagination.md).

**Caching.** Servers MUST include caching hints on `resultType: "complete"` results from
`server/discover`, `tools/list`, `prompts/list`, `resources/list`, `resources/templates/list`, and
`resources/read` — [caching](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching.md).
`ttlMs` is a freshness hint in milliseconds (analogous to HTTP `Cache-Control: max-age`), and
`cacheScope` is `"public"` or `"private"`; interim `input_required` results are not cacheable, and
MRTR retries MUST NOT be cached — same source. A matching change notification invalidates a fresh
cached response; each paginated page is independently cacheable with the same `cacheScope` — same
source. Servers "MUST NOT rely on `cacheScope` alone to prevent unauthorized access to primitives"
— same source.

---

## 5. Client features a server can invoke

All three historical server→client features now travel through MRTR: the server returns an
`InputRequiredResult` on a client request, and the client retries.

### 5.1 Roots (deprecated)

Roots let clients expose filesystem roots so servers "can focus their operations accordingly. They
are informational guidance rather than an access-control mechanism. The protocol does not enforce
that servers stay within roots" — [roots](https://modelcontextprotocol.io/specification/2026-07-28/client/roots.md).
A server requests them via an `InputRequiredResult` containing a `roots/list` request; a root is a
`file://` URI with an optional name — same source. The feature is deprecated: "New implementations
SHOULD NOT adopt it; existing implementations SHOULD migrate to passing directories or files via
tool parameters, resource URIs, or server configuration" — same source. The deprecated registry
gives "Earliest removal: First revision released on or after 2027-07-28" —
[deprecated](https://modelcontextprotocol.io/specification/2026-07-28/deprecated.md).

### 5.2 Sampling (deprecated)

Sampling let servers "request LLM sampling ('completions' or 'generations') from language models via
clients… with no server API keys necessary," and enabled "agentic behaviors, by enabling LLM calls
to occur nested inside other MCP server features" — [sampling](https://modelcontextprotocol.io/specification/2026-07-28/client/sampling.md).
Under MRTR it is requested via `sampling/createMessage`. It is deprecated: "New implementations
SHOULD NOT adopt it; existing implementations SHOULD migrate to integrating directly with LLM
provider APIs" — same source. The `includeContext` values `"thisServer"` and `"allServers"` are also
deprecated; omit the field or use `"none"` — same source.

### 5.3 Elicitation (active)

Elicitation lets servers "request additional information from users through the client during
interactions" — [elicitation](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation.md).
It supports **form mode** (structured data with a flat, primitive-only JSON Schema) and **URL mode**
(external URLs for sensitive interactions that must not pass through the MCP client) — same source.
The three response actions are accept, decline, and cancel. URL mode is for auth flows, payment, and
other sensitive operations; "The MCP client's bearer token remains unchanged" — same source. Servers
"MUST NOT use form mode elicitation to request sensitive information such as passwords, API keys,
access tokens, or payment credentials" and MUST use URL mode for those — same source. Clients must
not pre-fetch the URL, must not open it without explicit consent, must display the full URL, and must
open it so the client or LLM cannot inspect the content — same source. In 2026-07-28 the earlier
`notifications/elicitation/complete` and `elicitationId` were removed; URL-mode completion is instead
inferred from the echoed `requestState` — same source.

---

## 6. Authorization and security

### 6.1 When authorization applies

"Authorization is OPTIONAL for MCP implementations." HTTP-based transports SHOULD conform to the
authorization spec, but STDIO implementations "SHOULD NOT follow this specification, and instead
retrieve credentials from the environment" — [authorization](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md).
The framework is a profile "based on established specifications," including OAuth 2.1
(draft-ietf-oauth-v2-1-13), RFC 6750, RFC 8414, RFC 7591, RFC 8707, RFC 9728, RFC 9207, and the
OAuth Client ID Metadata Documents draft — same source.

### 6.2 Roles and the resource-server model

"A protected MCP server acts as an OAuth 2.1 resource server, capable of accepting and responding to
protected resource requests using access tokens"; the MCP client acts as the OAuth client —
[authorization](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md).
Servers "MUST implement OAuth 2.0 Protected Resource Metadata (RFC 9728)" and the metadata document
"MUST include the `authorization_servers` field containing at least one authorization server" —
[authorization server discovery](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/authorization-server-discovery.md).
Servers support two discovery mechanisms: a `WWW-Authenticate` header with a `resource_metadata`
URL on `401`, or well-known URIs; clients "MUST support both… and use the resource metadata URL from
the parsed `WWW-Authenticate` headers when present; otherwise… fall back to constructing and
requesting the well-known URIs" — same source. The `issuer` in the authorization-server metadata
"MUST be identical to the issuer identifier used to construct the well-known URL. If they differ,
the client MUST NOT use the metadata" — same source.

### 6.3 Tokens, audience validation, and PKCE

Clients MUST use the `Authorization: Bearer` header and must not put tokens in the query string;
servers "MUST validate that access tokens were issued specifically for them as the intended
audience" and MUST reject tokens without them in the audience — [authorization](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md).
"Invalid or expired tokens MUST receive a HTTP 401 response" — same source. If the server calls an
upstream API it "MUST NOT pass through the token it received from the MCP client" —
[security considerations](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/security-considerations.md).
Clients MUST implement PKCE (S256 when capable) and MUST refuse to proceed if the authorization
server does not advertise `code_challenge_methods_supported` — same source.

### 6.4 Resource indicators and issuer validation

"MCP clients MUST implement Resource Indicators for OAuth 2.0 (RFC 8707) to explicitly specify the
target resource for which the token is being requested," and MUST send the `resource` parameter
"regardless of whether authorization servers support it" — [authorization](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md).
Clients MUST record the validated issuer before redirecting, and MUST validate a present `iss`
parameter (RFC 9207) against it; when the authorization server advertises support and `iss` is
missing, the client MUST reject the response — same source. "A future revision … is expected to
upgrade authorization server inclusion of `iss` from SHOULD to MUST" — same source.

### 6.5 Client registration

There are three mechanisms: Client ID Metadata Documents (CIMD), pre-registration, and Dynamic
Client Registration (DCR) — [client registration](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/client-registration.md).
Selection priority is pre-registration, then CIMD, then DCR, then prompting the user — same source.
CIMD uses an HTTPS URL as the `client_id` pointing to a JSON metadata document; authorization
servers "SHOULD fetch metadata documents" and "MUST validate that the fetched document's `client_id`
matches the URL exactly" — same source. DCR is deprecated: "New implementations should use Client ID
Metadata Documents instead. This option remains available for backwards compatibility" — same
source. Clients must also key persisted credentials by the authorization server's issuer and must
not reuse them across authorization servers — same source.

### 6.6 Machine-to-machine and enterprise extensions

SEP-1046 adds the OAuth client credentials flow for machine-to-machine scenarios, "intentionally
constrain[ed]… to two options: JWT Assertions as per RFC 7523 (RECOMMENDED) and Client Secrets via
HTTP Basic authentication"; "Other options, such as mTLS, are not included" —
[SEP-1046](https://modelcontextprotocol.io/seps/1046-support-oauth-client-credentials-flow-in-authoriza.md).
SEP-990 describes enterprise-managed authorization that exchanges an IdP token for an Identity
Assertion JWT Authorization Grant (ID-JAG), then exchanges the ID-JAG for an MCP access token —
[SEP-990](https://modelcontextprotocol.io/seps/990-enable-enterprise-idp-policy-controls-during-mcp-o.md).

### 6.7 Named risks and countermeasures

The security best-practices page "identifies security risks, attack vectors, and best practices
specific to MCP implementations" — [security best practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md).
The material risks for a server author:

- **Token passthrough.** Accepting tokens not issued for the server and passing them downstream is
  an anti-pattern with audience-validation and accountability risks. "MCP servers MUST NOT accept
  any tokens that were not explicitly issued for the MCP server" — same source.
- **Confused deputy.** A proxy server using a static client ID while allowing dynamic client
  registration can let malicious clients obtain authorization codes without consent. Proxies
  "MUST implement per-client consent" and maintain a registry of approved `client_id` values, show
  the client name/scopes/redirect URI, use CSRF protection, and validate redirect URIs with "exact
  string matching (not pattern matching or wildcards)" — same source.
- **State handle hijacking.** With protocol sessions removed, the current equivalent of session
  hijacking is guessing or stealing a server-minted state handle. "MCP servers MUST NOT treat
  possession of a state handle as authentication," SHOULD use secure random handles, and SHOULD bind
  handles server-side to the authenticated user (for example `<user_id>:<handle>`) — same source.
- **SSRF.** Clients that fetch OAuth metadata URLs can be steered to internal addresses, cloud
  metadata endpoints (`169.254.169.254`), localhost services, DNS rebinding, or redirect chains.
  Clients deployed to a server "MUST consider SSRF risks and implement appropriate mitigations,"
  should block private/loopback/link-local ranges, and should not implement IP validation manually
  because of encoding tricks — same source. Authorization servers fetching CIMD are exposed too —
  same source.
- **Local server compromise.** Malicious startup commands or payloads can run on a user's machine.
  "If an MCP client supports one-click local MCP server configuration, it MUST implement proper
  consent mechanisms prior to executing commands," showing the exact untruncated command — same
  source; SEP-1024 backs this requirement —
  [SEP-1024](https://modelcontextprotocol.io/seps/1024-mcp-client-security-requirements-for-local-server-.md).
- **Authorization URL validation.** Clients "MUST only allow `http://` and `https://` schemes for
  authorization URLs," reject `javascript:`, `data:`, `file:`, `vbscript:`, and avoid shell
  execution when opening URLs — same source.
- **Mix-up attacks.** An attacker-controlled authorization server tries to have the client redeem a
  code from an honest server; `iss` validation mitigates this, but "PKCE alone does not prevent this
  attack" and the defense "provides no protection against an honest server that does not" emit `iss`
  — same source.
- **Localhost redirect URI impersonation.** CIMD "cannot prevent `localhost` URL impersonation by
  themselves"; authorization servers SHOULD warn on localhost-only redirect URIs and MUST display
  the redirect URI hostname during authorization — same source.
- **Scope minimization.** Servers should use a progressive, least-privilege scope model and return
  `403` with `WWW-Authenticate error="insufficient_scope"` at runtime, while avoiding wildcard or
  omnibus scopes — same source.
- **stdio in proxy architectures.** The stdio transport is "not inherently vulnerable," but a proxy
  that can spawn child processes provides "a critical escalation path from web-based attacks to full
  system compromise"; such proxies should sandbox, restrict filesystem access, log usage, and
  require extra authorization — same source.

### 6.8 Staleness caution in the authorization tutorial

The authorization tutorial at the same revision still describes client registration as "two ways"
(pre-registration or DCR) and warns about `Mcp-Session-Id`, while the core specification now lists
three mechanisms with CIMD as a SHOULD, deprecates DCR, and has removed protocol-level sessions and
`Mcp-Session-Id` — compare [tutorial](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization.md)
with [client registration](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/client-registration.md)
and the [2026-07-28 changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog.md).
For a server implementer, the core specification is the authoritative source; the tutorial
illustration is partially behind it.

---

## 7. Extensions

Extensions are "optional additions to the specification that define capabilities beyond the core
protocol" and "evolve independently of the core protocol" —
[extensions overview](https://modelcontextprotocol.io/extensions/overview). Identifiers use
`{vendor-prefix}/{extension-name}` (for example `io.modelcontextprotocol/tasks`), follow `_meta` key
rules with a mandatory prefix, and official extensions use the `io.modelcontextprotocol` prefix —
same source. Capability negotiation is via an `extensions` map: clients advertise in
`_meta["io.modelcontextprotocol/clientCapabilities"]`, servers in their `server/discover` response;
"Extensions are always disabled by default and require explicit opt-in from the developer" — same
source. If only one side supports an extension, the supporting side "MUST either revert to core
protocol behavior or reject the request with an appropriate error"; breaking changes require a new
identifier (for example `…-v2`) — same source. Official extensions live in `ext-` repositories,
experimental ones in `experimental-ext-` repositories, and an extension SEP needs a reference
implementation in an official SDK plus an associated working or interest group — same source.

Four official extension areas exist:

- **MCP Apps (`io.modelcontextprotocol/ui`).** "MCP Apps let servers return interactive HTML
  interfaces (data visualizations, forms, dashboards) that render directly in the chat," combining a
  tool that declares a UI resource via `_meta.ui.resourceUri` and a `ui://` HTML resource. They run
  in a sandboxed iframe that blocks parent DOM, cookies, and parent-context script execution —
  [MCP Apps](https://modelcontextprotocol.io/extensions/apps/overview).
- **OAuth Client Credentials (`io.modelcontextprotocol/oauth-client-credentials`).** Adds the OAuth
  2.0 client credentials flow to MCP, with JWT bearer assertions recommended; it warns that client
  secrets are long-lived credentials — [OAuth client credentials](https://modelcontextprotocol.io/extensions/auth/oauth-client-credentials).
- **Enterprise-Managed Authorization (`io.modelcontextprotocol/enterprise-managed-authorization`).**
  Lets organizations control MCP server access centrally through their IdP via the ID-JAG exchange —
  [enterprise-managed authorization](https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization).
- **Tasks (`io.modelcontextprotocol/tasks`).** "MCP Tasks let servers return a durable handle
  instead of blocking, so clients can poll for progress, provide input when needed, and retrieve the
  final result after reconnecting." The server decides per-request whether to create a task;
  methods are `tasks/get`, `tasks/update`, and `tasks/cancel`; the result discriminator is
  `resultType: "task"`; a missing capability yields `-32021` —
  [tasks](https://modelcontextprotocol.io/extensions/tasks/overview).
- **Skills (`io.modelcontextprotocol/skills`).** "The Skills extension allows MCP servers to expose
  workflow instructions and supporting files to clients." A skill is a directory with a `SKILL.md`;
  servers declaring it MUST implement `skills/list` and `skills/get`, and skill files are served
  through `resources/read` — [skills](https://modelcontextprotocol.io/extensions/skills/overview).

The extension support matrix lists client support per extension and notes that a client uses an
extension only when both sides declare it — [client matrix](https://modelcontextprotocol.io/extensions/client-matrix).
The framework was established by SEP-2133 and Tasks and Skills are Extensions-Track SEPs
([SEP-2133](https://modelcontextprotocol.io/seps/2133-extensions),
[SEP-2663](https://modelcontextprotocol.io/seps/2663-tasks-extension),
[SEP-2640](https://modelcontextprotocol.io/seps/2640-skills-extension)).

---

## 8. Best practices for building servers and clients

The official server quickstart walks through scaffolding, implementing typed tool handlers, running
the server, and testing it in a host; the example uses `@mcp.tool()` decorators in Python and
`server.registerTool(...)` with a Zod schema in TypeScript —
[build an MCP server](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server).

**The single most important stdio rule:** "Never write to stdout. Writing to stdout will corrupt the
JSON-RPC messages and break your server." Use the standard logging module (Python) or
`console.error()` (TypeScript) so logs go to stderr; HTTP-based servers are exempt because stdout
does not carry protocol frames — same source.

**Tool naming (SEP-986).** Tool names "should be 1–64 characters, case-sensitive, and may include
alphanumeric characters, underscores, dashes, dots, and forward slashes," and SHOULD be unique within
their namespace; existing non-conforming names SHOULD be supported as aliases for at least one major
version — [SEP-986](https://modelcontextprotocol.io/seps/986-specify-format-for-tool-names). The
tools reference itself states 1–128 characters; where the two differ, the SEP is the narrower naming
guidance and the spec is the wire contract — compare
[SEP-986](https://modelcontextprotocol.io/seps/986-specify-format-for-tool-names) with
[tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md).

**Client scaling.** "Loading every tool definition into the model's context window upfront wastes
tokens, increases latency, and degrades model performance." Two patterns address it: *progressive
discovery* (defer definitions, expose a `search_tools` meta-tool, load details on demand) and
*programmatic tool calling* or "code mode" (the model writes sandboxed code that calls tools, and
"only the final result returns to the model") — [client best practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices).
The three-layer discovery pattern is catalog, inspect, execute; hosts should cache definitions and
refresh on `list_changed` — same source. Declaring an `outputSchema` lets code-mode clients generate
precise return types — same source.

**Debugging.** "This should be your first stop" is the MCP Inspector, an interactive,
transport-agnostic UI. Server logging should go to stderr (stdio) or OpenTelemetry (all transports);
`notifications/message` is deprecated. Connection issues to diagnose include `-32022` unsupported
version, `-32602` missing required `_meta` fields, and `-32021` missing required client capability.
Common pitfalls: an undefined working directory (use absolute paths) and a limited inherited
environment — [debugging](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging).

**Inspector.** The Inspector "provides three clients behind one binary" — Web
(`npx @modelcontextprotocol/inspector`), CLI (`--cli`), and TUI (`--tui`) — requires Node 22.19.0 or
newer, and shares one core so connections behave identically across modes, including protocol-era
negotiation — [inspector](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector).

**Roadmap (context).** The roadmap, last updated 2026-08-22, prioritizes agentic messaging
primitives, HTTP-native transport unification and hardening, agent identity and enterprise security,
improved primitives (a redesigned `tools/call` shape and progressive discovery), and SDK developer
experience. It states it "reflects current thinking rather than firm commitments" —
[roadmap](https://modelcontextprotocol.io/development/roadmap).

---

## 9. Distribution: SDKs and the official Registry

Official SDKs are tiered "based on feature completeness, protocol support, and maintenance
commitment." Tier 1: TypeScript, Python, C#, Go, Rust, Ruby. Tier 2: Java. Tier 3: Swift, PHP,
Kotlin — [SDKs](https://modelcontextprotocol.io/docs/2026-07-28/sdk). Tier 1 requires a 100%
conformance pass rate and new features before a spec release; Tier 2 requires 80% and features within
six months. Conformance is automated, and an SDK can be relegated after sustained conformance
failures — [SDK tiers](https://modelcontextprotocol.io/community/sdk-tiers). The tiering system
originates in SEP-1730, whose motivation was "no standardized way to know which SDKs support
specific MCP features" — [SEP-1730](https://modelcontextprotocol.io/seps/1730-sdks-tiering-system).

The official MCP Registry is "the official centralized metadata repository for publicly accessible
MCP servers." It hosts metadata, not artifacts: "Package registries — such as npm, PyPI, and Docker
Hub — host packages with code and binaries. The MCP Registry hosts metadata that points to those
packages" — [Registry](https://modelcontextprotocol.io/registry/about). It is in preview, does not
support private servers, is consumed primarily by downstream aggregators rather than host
applications, and "delegates security scanning" to package registries and aggregators — same source.
Moderation is permissive: it removes illegal content, malware, spam, and non-functioning servers, but
not low-quality servers or servers with vulnerabilities — [moderation policy](https://modelcontextprotocol.io/registry/moderation-policy).

Publishing uses the `mcp-publisher` CLI: publish the package first, add an ownership proof, then
publish `server.json`. Supported package types are npm, PyPI, NuGet, Cargo, Docker/OCI, and MCPB,
each with its own ownership proof (npm `mcpName`, README `mcp-name:` tokens, an OCI label, or an MCPB
URL plus `fileSha256`) — [package types](https://modelcontextprotocol.io/registry/package-types).
Versions are immutable once published and version ranges are prohibited — [registry versioning](https://modelcontextprotocol.io/registry/versioning).
Authentication method determines the namespace: GitHub authentication forces an `io.github.*`
namespace, while DNS/HTTP authentication enables a custom reverse-DNS domain — [registry authentication](https://modelcontextprotocol.io/registry/authentication).
GitHub Actions workflows can publish on tag push using OIDC (recommended), a PAT, or DNS —
[GitHub Actions](https://modelcontextprotocol.io/registry/github-actions). Remote servers must be
publicly accessible and "should use the Streamable HTTP transport. The SSE transport is deprecated" —
[remote servers](https://modelcontextprotocol.io/registry/remote-servers).

---

## 10. Governance, the SEP process, and deprecations

MCP is "Model Context Protocol a Series of LF Projects, LLC" with code under Apache 2.0 and
documentation under CC BY 4.0 — [governance](https://modelcontextprotocol.io/community/governance).
Its hierarchy is Lead Maintainers (BDFL, final authority), Core Maintainers (overall direction),
Maintainers (groups, SDKs, components), and Contributors; membership is individual, not
company-based, and the Core Maintainers meet every two weeks — same source.

Changes flow through Specification Enhancement Proposals. "A SEP is a design document providing
information to the MCP community, or describing a new feature for the Model Context Protocol or its
processes." Prior discussion in the relevant group is required, and "A SEP without a linked prior
discussion is not accepted." Statuses run `draft → in-review → accepted → final`, with `dormant`
reserved for SEPs that do not find a sponsor within six months — [SEP guidelines](https://modelcontextprotocol.io/community/sep-guidelines).
Standards-Track SEPs that change observable protocol behavior need a merged conformance test before
`Final` — same source. SEP-1850 formalized the PR-based workflow and made the SEP number equal to the
pull-request number — [SEP-1850](https://modelcontextprotocol.io/seps/1850-pr-based-sep-workflow).

Deprecation is governed by a formal lifecycle: features are **Active**, **Deprecated**, or
**Removed**. A deprecation is itself a SEP and must specify a minimum window of "at least twelve"
months, measured "from the release of the specification revision in which the feature is first
marked Deprecated, not from the date the SEP reaches Final"; the window can be shortened to at least
ninety days only for an active security risk — [feature lifecycle](https://modelcontextprotocol.io/community/feature-lifecycle).
Tier 1 SDKs must mark deprecated APIs with native deprecation mechanisms and emit runtime warnings —
same source.

The 2026-07-28 deprecated-features registry lists six entries:

| Feature | Deprecated in | Migration | Earliest removal |
|---|---|---|---|
| Roots | 2026-07-28 | Tool parameters, resource URIs, or server configuration | First revision on/after 2027-07-28 |
| Sampling | 2026-07-28 | Integrate directly with LLM provider APIs | First revision on/after 2027-07-28 |
| Logging | 2026-07-28 | `stderr` (stdio) or OpenTelemetry | First revision on/after 2027-07-28 |
| Dynamic Client Registration | 2026-07-28 | Client ID Metadata Documents | First revision on/after 2027-07-28 |
| `includeContext` "thisServer"/"allServers" | 2025-11-25 | Omit or use `"none"` | Follows Sampling |
| HTTP+SSE transport | 2025-03-26 | Streamable HTTP | Three months after SEP-2596 reaches Final |

Source: [deprecated features registry](https://modelcontextprotocol.io/specification/2026-07-28/deprecated).
The policy originates in SEP-2596; Roots/Sampling/Logging in SEP-2577
([SEP-2596](https://modelcontextprotocol.io/seps/2596-spec-feature-lifecycle-and-deprecation),
[SEP-2577](https://modelcontextprotocol.io/seps/2577-deprecate-roots-sampling-and-logging)).

Working Groups build concrete solutions (SEPs, implementations, code); Interest Groups identify and
discuss problems. Typical flow: discuss in an IG, form or join a WG, submit a SEP, implement.
Current WG examples include Registry, Inspector, Tool Filtering, and Server Identity; IG examples
include Security, Auth, enterprise usage, and client hosting —
[working and interest groups](https://modelcontextprotocol.io/community/working-interest-groups).
SEP-2596's own motivation notes that earlier retirements were inconsistent: JSON-RPC batching was
"added in revision `2025-03-26` and removed in `2025-06-18`, a single release later, with no
deprecation period" — [SEP-2596](https://modelcontextprotocol.io/seps/2596-spec-feature-lifecycle-and-deprecation).

---

## 11. Practical implications for an MCP server author (synthesis)

The following is the report's own synthesis from the sources above; each point names the source
facts it rests on.

1. **Target the current revision explicitly.** A 2026-07-28 server is stateless, exposes
   `server/discover`, and expects per-request `_meta`; a server that only implements the
   `initialize` handshake is a legacy server and will not serve modern clients
   ([changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog.md),
   [versioning](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md)).
2. **Serve both eras if you need broad reach.** A dual-era server branches on the presence of
   `initialize`; a modern-only server cannot serve un-upgraded legacy clients, and legacy clients
   have no fall-forward path ([versioning](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md)).
3. **Keep no implicit state.** Encode cross-call state in explicit handles or in integrity-protected
   `requestState`; do not treat a connection or process as a session, and never treat a state handle
   as authentication ([basic protocol](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md),
   [security best practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)).
4. **Do not initiate requests.** Server→client input goes only through MRTR on `prompts/get`,
   `resources/read`, and `tools/call` ([MRTR](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr.md)).
5. **Declare capabilities and caching.** Advertise `tools`/`resources`/`prompts` (and `completions`
   if used) in `server/discover`, return deterministic listings, and always attach `ttlMs` and
   `cacheScope` where required ([tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md),
   [caching](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching.md)).
6. **Prefer HTTP for remote, stdio for local.** For remote, use Streamable HTTP with mandatory
   version/method/name headers and Origin validation; for local processes, use stdio and keep stdout
   clean of logs ([streamable HTTP](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md),
   [stdio](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio.md)).
7. **If you are a protected remote server, implement the resource-server role.** Publish RFC 9728
   metadata, validate audience-bound tokens, never pass them through, and advertise scopes through
   `WWW-Authenticate` challenges ([authorization](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md)).
8. **Do not build on deprecated features.** Avoid Roots, Sampling, Logging, HTTP+SSE, and the
   `includeContext` values; prefer CIMD over DCR ([deprecated registry](https://modelcontextprotocol.io/specification/2026-07-28/deprecated)).
9. **Ship through a Tier 1 SDK and the Registry.** Tier 1 guarantees conformance and feature
   timing; publishing is package-first, registry-second, with a per-package-type ownership proof
   ([SDK tiers](https://modelcontextprotocol.io/community/sdk-tiers),
   [package types](https://modelcontextprotocol.io/registry/package-types)).

## 12. Contradictions, staleness, and open questions

- The **authorization tutorial** at 2026-07-28 still presents two client-registration mechanisms and
  warns about `Mcp-Session-Id`, while the core spec has three mechanisms with CIMD as the default and
  removed `Mcp-Session-Id`. Treat the core spec as authoritative
  ([tutorial](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization.md),
  [client registration](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/client-registration.md)).
- **Tool name length** is stated as 1–64 in SEP-986 and 1–128 in the current tools reference. The
  safer server-side choice is the narrower 1–64
  ([SEP-986](https://modelcontextprotocol.io/seps/986-specify-format-for-tool-names),
  [tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md)).
- **SEP-990 status** shows a "Final" badge while its body says "State: Ready to Review"; the
  discrepancy is recorded rather than resolved
  ([SEP-990](https://modelcontextprotocol.io/seps/990-enable-enterprise-idp-policy-controls-during-mcp-o.md)).
- **CIMD draft identifier** differs between SEP-991 (`draft-parecki-…-03`) and the current spec
  (`draft-ietf-…-00`); follow the current spec.
- **No formal release cadence** is stated in the fetched sources; the observed intervals are real
  but not declared policy.
- **Exact tool annotation hint keys** (for example `readOnlyHint`) were not present on the fetched
  tools page; the schema remains the source of truth for field-level detail
  ([basic protocol](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md)).
- **One retrieval failure** was recorded: a guessed SEP-2468 slug returned HTTP 404; the correct URL
  is `https://modelcontextprotocol.io/seps/2468-recommend-issuer-claim-for-auth`. This is a tooling
  result, not evidence about the protocol.
- **Working-group names.** The working/interest-groups page lists Registry, Inspector, Tool
  Filtering, and Server Identity as WG examples; Transports, Server Card, and Agents were not named
  on that page, though the `.io` index lists charters for Transports, Agents, Server Card, Registry,
  SDK, Inspector V2, and others ([groups](https://modelcontextprotocol.io/community/working-interest-groups),
  [documentation index](https://modelcontextprotocol.io/llms.txt)).

---

## Resources

All source URLs referenced in this report, deduplicated.

**MCP documentation (2026-07-28)**
- https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro.md
- https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture.md
- https://modelcontextprotocol.io/docs/2026-07-28/learn/server-concepts.md
- https://modelcontextprotocol.io/docs/2026-07-28/learn/client-concepts.md
- https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server
- https://modelcontextprotocol.io/docs/2026-07-28/develop/build-client
- https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices
- https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging
- https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector
- https://modelcontextprotocol.io/docs/2026-07-28/sdk
- https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization.md
- https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md

**MCP specification (current 2026-07-28, plus versioning and older changelogs)**
- https://modelcontextprotocol.io/specification/versioning
- https://modelcontextprotocol.io/specification/2026-07-28/changelog.md
- https://modelcontextprotocol.io/specification/2026-07-28/deprecated.md
- https://modelcontextprotocol.io/specification/2026-07-28/architecture/index.md
- https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md
- https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md
- https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/index.md
- https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr.md
- https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/subscriptions.md
- https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/cancellation.md
- https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/progress.md
- https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/index.md
- https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio.md
- https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md
- https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md
- https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/authorization-server-discovery.md
- https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/client-registration.md
- https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/security-considerations.md
- https://modelcontextprotocol.io/specification/2026-07-28/server/index.md
- https://modelcontextprotocol.io/specification/2026-07-28/server/discover.md
- https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md
- https://modelcontextprotocol.io/specification/2026-07-28/server/resources.md
- https://modelcontextprotocol.io/specification/2026-07-28/server/prompts.md
- https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/completion.md
- https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/logging.md
- https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/pagination.md
- https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching.md
- https://modelcontextprotocol.io/specification/2026-07-28/client/roots.md
- https://modelcontextprotocol.io/specification/2026-07-28/client/sampling.md
- https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation.md
- https://modelcontextprotocol.io/specification/2025-11-25/changelog.md
- https://modelcontextprotocol.io/specification/2025-06-18/changelog.md
- https://modelcontextprotocol.io/specification/2025-03-26/changelog.md

**Extensions**
- https://modelcontextprotocol.io/extensions/overview
- https://modelcontextprotocol.io/extensions/client-matrix
- https://modelcontextprotocol.io/extensions/apps/overview
- https://modelcontextprotocol.io/extensions/auth/oauth-client-credentials
- https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization
- https://modelcontextprotocol.io/extensions/tasks/overview
- https://modelcontextprotocol.io/extensions/skills/overview

**Registry and ecosystem**
- https://modelcontextprotocol.io/registry/about
- https://modelcontextprotocol.io/registry/quickstart
- https://modelcontextprotocol.io/registry/package-types
- https://modelcontextprotocol.io/registry/remote-servers
- https://modelcontextprotocol.io/registry/versioning
- https://modelcontextprotocol.io/registry/authentication
- https://modelcontextprotocol.io/registry/github-actions
- https://modelcontextprotocol.io/registry/moderation-policy
- https://modelcontextprotocol.io/examples

**Community, governance, roadmap**
- https://modelcontextprotocol.io/community/design-principles.md
- https://modelcontextprotocol.io/community/governance
- https://modelcontextprotocol.io/community/sep-guidelines
- https://modelcontextprotocol.io/community/feature-lifecycle
- https://modelcontextprotocol.io/community/working-interest-groups
- https://modelcontextprotocol.io/community/sdk-tiers
- https://modelcontextprotocol.io/development/roadmap
- https://modelcontextprotocol.io/llms.txt

**Specification Enhancement Proposals**
- https://modelcontextprotocol.io/seps/986-specify-format-for-tool-names
- https://modelcontextprotocol.io/seps/990-enable-enterprise-idp-policy-controls-during-mcp-o.md
- https://modelcontextprotocol.io/seps/1024-mcp-client-security-requirements-for-local-server-.md
- https://modelcontextprotocol.io/seps/1046-support-oauth-client-credentials-flow-in-authoriza.md
- https://modelcontextprotocol.io/seps/1730-sdks-tiering-system
- https://modelcontextprotocol.io/seps/1850-pr-based-sep-workflow
- https://modelcontextprotocol.io/seps/2133-extensions
- https://modelcontextprotocol.io/seps/2468-recommend-issuer-claim-for-auth
- https://modelcontextprotocol.io/seps/2577-deprecate-roots-sampling-and-logging
- https://modelcontextprotocol.io/seps/2596-spec-feature-lifecycle-and-deprecation
- https://modelcontextprotocol.io/seps/2640-skills-extension
- https://modelcontextprotocol.io/seps/2663-tasks-extension

**Official repository**
- https://github.com/modelcontextprotocol/modelcontextprotocol/releases

**Underlying standards referenced by the specification**
- https://www.jsonrpc.org/specification
- https://json-schema.org/draft/2020-12/schema
- https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-13
- https://datatracker.ietf.org/doc/html/rfc6750
- https://datatracker.ietf.org/doc/html/rfc8414
- https://datatracker.ietf.org/doc/html/rfc7591
- https://www.rfc-editor.org/rfc/rfc8707.html
- https://datatracker.ietf.org/doc/html/rfc9728
- https://datatracker.ietf.org/doc/html/rfc9207
- https://datatracker.ietf.org/doc/html/rfc7523
- https://datatracker.ietf.org/doc/html/draft-ietf-oauth-client-id-metadata-document-00

---

### Working files

The per-topic evidence files with full quotations and retrieval logs are in the same folder:
`00-research-plan.md`, `01-overview-architecture.md`, `02-protocol-history.md`,
`03-base-protocol-transports.md`, `04-server-primitives.md`, `05-client-features.md`,
`06-authorization-security.md`, `07-extensions.md`, `08-server-best-practices.md`,
`09-ecosystem-sdk-registry.md`, `10-governance-seps-deprecations.md`.

Retrieval date for all sources: 2026-10-02. All listed official pages returned successfully except
one guessed SEP-2468 slug (HTTP 404), which is noted in section 12.
