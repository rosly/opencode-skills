# MCP Base Protocol and Transports — Primary-Source Research

Research file for an MCP server implementer. Protocol revision under study: **2026-07-28**. Legacy comparison revision: **2025-11-25**. All facts below are drawn from the official Model Context Protocol specification site; every claim carries a short exact quotation and an inline link to the page it came from. Retrieval date: 2026-10-02.

## Notation legend

- **SOURCE FACT** — quoted directly from the official MCP specification or official MCP documentation. Highest tier.
- **SOURCE CLAIM** — lower-tier source (e.g., a changelog/issue/SEP) explicitly labeled with its rank.
- **AI INFERENCE** — a conclusion drawn by the researcher; names the quoted facts it follows from.
- **PLAUSIBLE** — consistent with sources but not directly stated.
- **NOT VERIFIED** — asserted somewhere but not confirmed against an official source.
- **UNKNOWN** — no source found or retrieval failed.

## Retrieval summary

All twelve target URLs were retrieved successfully as `.md` endpoints. **No failed retrievals.** The official documentation index note appears on every page: "Fetch the complete documentation index at: https://modelcontextprotocol.io/llms.txt" ([Overview, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md)).

---

## 1. What the base protocol comprises

**SOURCE FACT** — The specification enumerates the protocol layers as "**Base Protocol**: Core JSON-RPC message types", "**Versioning and Compatibility**: Protocol version negotiation, extension negotiation, and interoperability with earlier protocol revisions", and "**Message Patterns**: Messaging patterns supported by the core protocol including request and response, multi round-trip requests (MRTR), and subscribe and notify" ([Basic Protocol Overview, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md)).

**SOURCE FACT** — Support is mandatory for the core: "All implementations **MUST** support the base protocol, versioning, and the message patterns. Other components **MAY** be implemented based on the specific needs of the application." ([Basic Protocol Overview, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md)).

**SOURCE FACT** — Message encoding is fixed: "All messages between MCP clients and servers **MUST** follow the [JSON-RPC 2.0](https://www.jsonrpc.org/specification) specification." ([Basic Protocol Overview, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md)).

---

## 2. JSON-RPC 2.0 message types

### 2.1 Requests

**SOURCE FACT** — A request is defined as `{ jsonrpc: "2.0"; id: string | number; method: string; params?: {...} }`, and "Requests **MUST** include a string or integer ID. Unlike base JSON-RPC, the ID **MUST NOT** be `null`." ([Basic Protocol Overview, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md)).

**SOURCE FACT** — ID uniqueness is enforced by the sender: "The request ID **MUST NOT** match the ID of any other request the sender has issued and not yet received a response for." ([Basic Protocol Overview, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md)).

### 2.2 Result responses and `resultType`

**SOURCE FACT** — Result responses "**MUST** include the same ID as the request they correspond to", "**MUST** include a `result` field", and "The `result` **MUST** include a `resultType` field to indicate the type of the result." ([Basic Protocol Overview, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md)).

**SOURCE FACT** — The polymorphic `resultType` has two core values: "A `resultType` of `\"complete\"` indicates the request completed successfully and the result contains the final content" and "A `resultType` of `\"input_required\"` indicates the request is incomplete and more information is needed to process the request." ([Basic Protocol Overview, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md)).

**SOURCE FACT** — Backward compatibility rule for absent `resultType`: "For backward compatibility with servers implementing earlier protocol versions, which do not include `resultType`, clients **MUST** treat an absent `resultType` as `\"complete\"`." ([Basic Protocol Overview, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md)).

**SOURCE FACT** — Extensions may add `resultType` values but validation is strict: "Extensions **MAY** add additional `ResultType` values. The set of supported `ResultType` values **MUST** be created from the set defined in the core protocol and include any additional values of supported extensions that are advertised via capabilities" and "A `resultType` of any value unrecognized by the client **MUST** be considered invalid." ([Basic Protocol Overview, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md)).

### 2.3 Error responses

**SOURCE FACT** — "Error responses **MUST** include an `error` field with a `code` and `message`." and "Error codes **MUST** be integers." ([Basic Protocol Overview, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md)). The `data` member is optional: "Error responses **MAY** include a `data` member with additional information of any type, such as nested errors."

### 2.4 Notifications

**SOURCE FACT** — "Notifications **MUST NOT** include an ID." and "The receiver **MUST NOT** send a response." ([Basic Protocol Overview, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md)).

### 2.5 Directionality constraint (critical for server authors)

**SOURCE FACT** — "Servers **MUST NOT** initiate JSON-RPC requests, and clients do not send JSON-RPC responses." ([Message Patterns Overview, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/index.md)). The transports page repeats: "No other message direction exists: per the [message patterns](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns), servers do not initiate JSON-RPC requests and clients do not send JSON-RPC responses." ([Transports Overview, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/index.md)).

**AI INFERENCE** — A server cannot push a "question" to the client as a new JSON-RPC request. Instead it must use the MRTR pattern: the server replies to the client's request with an `InputRequiredResult` (the `input_required` resultType), and the client retries. This follows directly from the two SOURCE FACTS above plus the MRTR definition in §6.

---

## 3. `_meta` and reserved keys

**SOURCE FACT** — Purpose: "The `_meta` property/parameter is used by MCP to allow clients and servers to attach additional metadata to their interactions." ([Basic Protocol Overview, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md)).

### 3.1 Key-name structure

**SOURCE FACT** — "valid `_meta` key names have two segments: an optional **prefix**, and a **name**", where a prefix "MUST be a series of labels separated by dots (`.`), followed by a slash (`/`)" and "Implementations SHOULD use reverse DNS notation (e.g., `com.example/` rather than `example.com/`)." ([Basic Protocol Overview, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md)).

**SOURCE FACT** — Reserved-prefix rule: "Any prefix where the second label is `modelcontextprotocol` or `mcp` is **reserved** for MCP use" with examples "`io.modelcontextprotocol/`, `dev.mcp/`, `org.modelcontextprotocol.api/`, and `com.mcp.tools/` are all reserved" but "`com.example.mcp/` is NOT reserved, as the second label is `example`." ([Basic Protocol Overview, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md)).

### 3.2 Reserved keys table

**SOURCE FACT** — The specification lists these reserved keys: "`progressToken` — Opts the request into progress notifications", "`io.modelcontextprotocol/protocolVersion` — Protocol version for a request", "`io.modelcontextprotocol/clientInfo` — Client name and version", "`io.modelcontextprotocol/clientCapabilities` — Client capabilities relevant to a request", "`io.modelcontextprotocol/logLevel` — Minimum log level the server should emit for a request", "`io.modelcontextprotocol/subscriptionId` — Correlates a notification with its originating subscription", and "`traceparent`, `tracestate`, `baggage` — OpenTelemetry trace context propagation" ([Basic Protocol Overview, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md)).

### 3.3 Per-request protocol fields (modern model)

**SOURCE FACT** — "Client requests carry the following `io.modelcontextprotocol/*` fields in `_meta`; fields marked as required **MUST** be included on every request. Servers use these to identify the protocol version and capabilities in use without relying on any prior connection state." ([Basic Protocol Overview, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md)).

| Key | Type | Required | Description |
| - | - | - | - |
| `io.modelcontextprotocol/protocolVersion` | `string` | Yes | "Protocol version for this request (e.g., `\"2026-07-28\"`)" |
| `io.modelcontextprotocol/clientInfo` | `Implementation` | No | "Client name and version" |
| `io.modelcontextprotocol/clientCapabilities` | `ClientCapabilities` | Yes | "Client capabilities relevant to this request" |
| `io.modelcontextprotocol/logLevel` | `LoggingLevel` | No | "Minimum log level the server should emit for this request" |

All four rows are quoted from [Basic Protocol Overview, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md).

**SOURCE FACT** — Malformed-request handling: "A request missing any required field is malformed; the server **MUST** reject it with JSON-RPC error code `-32602` (Invalid params). On HTTP, the response status **MUST** be `400 Bad Request`." ([Basic Protocol Overview, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md)).

**SOURCE FACT** — Client-info recommendation: "Clients **SHOULD** include `io.modelcontextprotocol/clientInfo` on every request unless specifically configured not to do so." ([Basic Protocol Overview, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md)).

**SOURCE FACT** — Undeclared-capability enforcement: "A server **MUST NOT** rely on capabilities the client has not declared. If processing a request requires a capability the client did not include in `io.modelcontextprotocol/clientCapabilities`, the server **MUST** return a `MissingRequiredClientCapabilityError` (`-32021`) whose `data.requiredCapabilities` lists the missing capabilities." ([Basic Protocol Overview, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md)).

### 3.4 Per-response protocol field

**SOURCE FACT** — "Servers **SHOULD** include the following `io.modelcontextprotocol/*` field in every result's `_meta`, unless specifically configured not to do so, to identify themselves without relying on any prior connection state: `io.modelcontextprotocol/serverInfo` (`Implementation`, not required, 'Server name and version')." ([Basic Protocol Overview, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md)).

**SOURCE FACT** — Trust caveat: "`io.modelcontextprotocol/clientInfo` and `io.modelcontextprotocol/serverInfo` are self-reported by the sender and are not verified by the protocol. They are intended for display, logging, and debugging. Implementations **SHOULD NOT** use them to change the behavior of the client or server, and **SHOULD NOT** rely on them for security decisions." ([Basic Protocol Overview, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md)).

### 3.5 Subscription correlation and trace context

**SOURCE FACT** — "On notifications delivered via a [`subscriptions/listen`](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/subscriptions) stream, the server **MUST** include `io.modelcontextprotocol/subscriptionId` in `_meta` so the client can correlate the notification with the originating subscription request." ([Basic Protocol Overview, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md)).

**SOURCE FACT** — Trace-context exception: "As an exception to the prefix requirement above, the keys `traceparent`, `tracestate`, and `baggage` are reserved for [OpenTelemetry](https://opentelemetry.io/) trace context propagation. When present, their values MUST follow [W3C Trace Context](https://www.w3.org/TR/trace-context/) and [W3C Baggage](https://www.w3.org/TR/baggage/) formats respectively." ([Basic Protocol Overview, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md)).

---

## 4. Error codes and the allocation policy

**SOURCE FACT** — "MCP uses the standard JSON-RPC 2.0 error codes (`-32700`, `-32600` to `-32603`) for general protocol failures." ([Basic Protocol Overview, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md)).

**SOURCE FACT** — Range partition: "JSON-RPC 2.0 reserves the range `-32000` to `-32099` for implementation-defined server errors. MCP partitions this range as follows: **`-32000` to `-32019` — legacy.** Codes in this sub-range were allocated by implementations before this policy was introduced. New codes **MUST NOT** be allocated in this sub-range, and new implementations **SHOULD NOT** use codes from this sub-range at all. ... **`-32020` to `-32099` — reserved for the MCP specification.**" ([Basic Protocol Overview, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md)).

**SOURCE FACT** — Spec-range constraint: "Implementations **MUST NOT** emit any code from this sub-range that is not defined by this specification and **MUST** use defined codes only with their specified meanings." ([Basic Protocol Overview, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md)).

**SOURCE FACT** — The three codes defined by this revision: "`-32020` | `HeaderMismatch`", "`-32021` | `MissingRequiredClientCapability`", "`-32022` | `UnsupportedProtocolVersion`" ([Basic Protocol Overview, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md)).

**SOURCE FACT** — Retired codes that MUST NOT be emitted by this revision: "Implementations of this protocol version **MUST NOT** emit these codes: `-32002` — resource not found (2025-11-25 and earlier; replaced by `-32602`). ... `-32042` — URL elicitation required (2025-11-25 only)." ([Basic Protocol Overview, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md)).

**SOURCE FACT** — Clients should still tolerate `-32002` from older servers: "Clients **SHOULD** still accept `-32002` from servers implementing earlier versions." ([Basic Protocol Overview, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md)).

**SOURCE FACT** — New, non-spec codes: "New error codes for purposes not defined by this specification **SHOULD** be allocated outside the JSON-RPC reserved range (`-32768` to `-32000`); the remainder of the integer space is available for application-defined errors." ([Basic Protocol Overview, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md)).

**AI INFERENCE** — For a 2026-07-28 server, the safe implementation-defined band from the old JSON-RPC custom range is effectively unavailable: any error a server needs to surface that is not a standard JSON-RPC or MCP-defined code should go below `-32768`, because `-32000..-32019` is legacy-only and `-32020..-32099` is spec-reserved. This follows from the `-32000..-32019` restriction, the `-32020..-32099` exclusivity rule, and the "allocate outside `-32768` to `-32000`" recommendation.

---

## 5. Stateless model vs legacy initialize/initialized lifecycle

### 5.1 Modern (2026-07-28): stateless, per-request metadata

**SOURCE FACT** — "The Model Context Protocol (MCP) is a **stateless protocol**: all the information needed to process a request is contained in the request itself. A server processes each request independently; no state should be inferred from previous requests, even those on the same connection or stream." ([Basic Protocol Overview, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md)).

**SOURCE FACT** — Concrete statelessness rules: "Servers **MUST NOT** rely on prior requests over the same connection to establish context (e.g., capabilities, protocol version, client identity). Every request supplies this metadata in its `_meta` field." and "Servers **SHOULD NOT** require that a client reuse the same connection or process to perform related operations." ([Basic Protocol Overview, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md)).

**SOURCE FACT** — State spanning requests must be explicit: "State that needs to span multiple requests (e.g., long-running tasks, application-level handles) **MUST** be referenced by an explicit identifier the client passes on each request." ([Basic Protocol Overview, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md)).

**SOURCE FACT** — A connection is not a session: "This implies that an open connection, such as a STDIO process, is not a conversation or session: clients may interleave unrelated requests on the same transport, and a server must not treat connection or process identity as a proxy for conversation or session continuity." ([Basic Protocol Overview, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md)).

**SOURCE FACT** — No handshake: "There is no negotiation handshake. Every request carries its protocol version, and the server accepts or rejects each request independently." ([Versioning and Compatibility, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md)).

**SOURCE FACT** — Terminology: "**Modern**: protocol versions that convey version, identity, and capabilities as per-request metadata (revision `2026-07-28` and later). **Legacy**: protocol versions that establish a session with an `initialize` handshake (`2025-11-25` and earlier). **Dual-era**: an implementation that supports both modern and legacy versions." ([Versioning and Compatibility, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md)).

### 5.2 Version negotiation (modern)

**SOURCE FACT** — "Every request declares the protocol version it is using in its `_meta` field. On HTTP, this is also carried in the `MCP-Protocol-Version` header." and unsupported versions yield an `UnsupportedProtocolVersionError` "listing the versions it does support." ([Versioning and Compatibility, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md)).

**SOURCE FACT** — Sample error payload: `"code": -32022, "message": "Unsupported protocol version", "data": { "supported": ["2026-07-28", "2025-11-25"], "requested": "1900-01-01" }` ([Versioning and Compatibility, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md)).

**SOURCE FACT** — "Servers **MUST** implement `server/discover`. Clients **MAY** call it before sending any other requests to learn the server's supported versions up front, but are not required to." ([Versioning and Compatibility, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md)).

### 5.3 Extension negotiation

**SOURCE FACT** — "Extensions are advertised in the `extensions` field of capabilities, which is a map of extension identifiers to per-extension settings objects. Extension identifiers **MUST** follow the `_meta` key naming rules, with a mandatory prefix." ([Versioning and Compatibility, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md)).

**SOURCE FACT** — Fallback rule: "If one party supports an extension but the other does not, the supporting party **MUST** either revert to core protocol behavior or reject the request with an appropriate error." ([Versioning and Compatibility, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md)).

### 5.4 Legacy (2025-11-25): stateful `initialize` / `initialized`

**SOURCE FACT** — "The initialization phase **MUST** be the first interaction between client and server." and the client "**MUST** initiate this phase by sending an `initialize` request containing: Protocol version supported, Client capabilities, Client implementation information." ([Lifecycle, 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/basic/lifecycle.md)).

**SOURCE FACT** — "After successful initialization, the client **MUST** send an `initialized` notification to indicate it is ready to begin normal operations." with payload `{ jsonrpc: "2.0", method: "notifications/initialized" }` ([Lifecycle, 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/basic/lifecycle.md)).

**SOURCE FACT** — Legacy version negotiation: "If the server supports the requested protocol version, it **MUST** respond with the same version. Otherwise, the server **MUST** respond with another protocol version it supports. ... If the client does not support the version in the server's response, it **SHOULD** disconnect." ([Lifecycle, 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/basic/lifecycle.md)).

**SOURCE FACT** — Legacy lifecycle phases are "1. **Initialization**: Capability negotiation and protocol version agreement 2. **Operation**: Normal protocol communication 3. **Shutdown**: Graceful termination of the connection", and "During the shutdown phase, one side (usually the client) cleanly terminates the protocol connection. No specific shutdown messages are defined." ([Lifecycle, 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/basic/lifecycle.md)).

### 5.5 Dual-era detection and compatibility

**SOURCE FACT** — "A server that wishes to support both legacy clients (which expect an `initialize` handshake) and modern clients (which use per-request metadata) **MAY** implement both behaviors." ([Versioning and Compatibility, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md)).

**SOURCE FACT** — Era detection differs by transport: stdio uses "probe with `server/discover` and fall back on any error that is not a recognized modern error"; Streamable HTTP uses "attempt a modern request and inspect the body of a `400 Bad Request` before falling back." ([Versioning and Compatibility, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md)).

**SOURCE FACT** — Era is per-server, not per-request: "The era determination is a property of the server, not of an individual request. Clients **SHOULD** cache the result for the lifetime of the server process (stdio) or origin (HTTP), and **MAY** persist it across restarts." ([Versioning and Compatibility, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md)).

**SOURCE FACT** — Dual-era server dispatch: "A request carrying modern per-request `_meta` is served statelessly according to this revision. An `initialize` request selects legacy semantics, scoped to the stdio process (stdio) or the session (HTTP), as specified by the negotiated legacy protocol version." ([Versioning and Compatibility, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md)).

**SOURCE FACT** — The matrix states the modern-client/legacy-server case "Fails. The server may reject the request with an implementation-defined error, stay silent, or even process an era-ambiguous method under legacy semantics." and the legacy-client/modern-server case "Fails. ... Legacy clients have no fall-forward mechanism." ([Versioning and Compatibility, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md)).

---

## 6. Multi Round-Trip Requests (MRTR)

**SOURCE FACT** — MRTR is new and replaces server-initiated requests: "Multi Round-Trip Requests (MRTR) was introduced in this version of the MCP specification. This replaces the previous approach of sending server-initiated requests. Servers **MUST** send server-to-client requests (such as `roots/list`, `sampling/createMessage`, or `elicitation/create`) using the MRTR pattern. The previous pattern of server-initiated requests is no longer supported. This is a breaking change." ([Multi Round-Trip Requests, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr.md)).

**SOURCE FACT** — Motivation: the pattern "provides a standardized way to handle these server-requests without requiring a shared storage layer across server instances or requiring stateful load balancing." ([Multi Round-Trip Requests, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr.md)).

**SOURCE FACT** — High-level flow: "1. Client sends an initial request ... 2. Server determines that additional information is required ... responds requesting more information. 3. Client gathers the requested information ... retries the original request including the additional requested information. 4. Server determines it has sufficient information to complete the operation, and responds with the final result." ([Multi Round-Trip Requests, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr.md)).

### 6.1 Core types

**SOURCE FACT** — "An `InputRequests` object is a map of server-client requests. Keys are server-assigned string identifiers; values are request objects (e.g., `ElicitRequest`, `CreateMessageRequest`, or `ListRootsRequest`)." ([Multi Round-Trip Requests, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr.md)).

**SOURCE FACT** — "An `InputResponses` object is a map of client responses to the server requests. Keys correspond to the keys in the `InputRequests` map; values are the client's result for each request." ([Multi Round-Trip Requests, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr.md)).

**SOURCE FACT** — `InputRequiredResult` shape: it is "a type of `Result`, indicating that additional input is needed before the request can be completed", with "`inputRequests` *(optional)*: An `InputRequests` map of server-initiated requests that the client must fulfill." and "`requestState` *(optional)*: An opaque string meaningful only to the server. Clients **MUST NOT** inspect, parse, modify, or make any assumptions about its contents." ([Multi Round-Trip Requests, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr.md)).

**SOURCE FACT** — Wire example: `"result": { "resultType": "input_required", "inputRequests": {...}, "requestState": "AEAD-protected blob" }` ([Multi Round-Trip Requests, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr.md)).

### 6.2 Which requests support MRTR

**SOURCE FACT** — "Servers **MAY** send `InputRequiredResult` responses on the following client requests:" `prompts/get` (Yes), `resources/read` (Yes), `tools/call` (Yes). "Servers **MUST NOT** send `InputRequiredResult` responses on any other client requests." ([Multi Round-Trip Requests, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr.md)).

### 6.3 Server requirements (selected, exact)

**SOURCE FACT** — "Servers **MUST** include at least one of `inputRequests` or `requestState` in every `InputRequiredResult` response." ([Multi Round-Trip Requests, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr.md)).

**SOURCE FACT** — Capability gating: "Servers **MUST NOT** send an `inputRequests` that the client has not declared support for in its capabilities." ([Multi Round-Trip Requests, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr.md)).

**SOURCE FACT** — No assumption of completion: "Servers **MUST NOT** assume that clients will fulfill the `inputRequests` or retry the original request." ([Multi Round-Trip Requests, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr.md)).

**SOURCE FACT** — State-integrity obligation: "If a client request contains a `requestState` field, servers **MUST** treat `requestState` as an attacker-controlled input. If `requestState` influences authorization, resource access, or business logic, servers **MUST** protect its integrity (e.g. HMAC or AEAD) and **MUST** reject state that fails verification." ([Multi Round-Trip Requests, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr.md)).

**SOURCE FACT** — Replay protection: "To prevent replay, servers **SHOULD** include the following inside the integrity-protected `requestState` payload and verify each on receipt: the authenticated principal ... a short expiry (TTL) ... an identifier for the originating request." ([Multi Round-Trip Requests, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr.md)).

### 6.4 Client requirements (selected, exact)

**SOURCE FACT** — "If an `InputRequiredResult` contains the `requestState` field, the client **MUST** echo back the exact value of that field when retrying the original request. Clients **MUST NOT** inspect, parse, modify, or make any assumptions about the `requestState` contents. If the `InputRequiredResult` does not contain a `requestState` field, the client **MUST NOT** include one in the retry." ([Multi Round-Trip Requests, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr.md)).

**SOURCE FACT** — New ID on retry: "The JSON-RPC `id` **MUST** be different between the initial request and the retry, as they are independent requests." ([Multi Round-Trip Requests, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr.md)).

**SOURCE FACT** — Isolation: "Both the `inputRequests` and `requestState` fields affect only the client's retry of the original request. They **MUST NOT** be used for any other request that the client may be sending in parallel." ([Multi Round-Trip Requests, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr.md)).

**AI INFERENCE** — For an MCP server author, MRTR means the server is fully responsible for preserving any cross-request state by encoding it into `requestState`, because "it allows servers to request additional information without maintaining any server-side state. The server encodes any needed context into the `requestState` field, which the client echoes back on retry." ([Multi Round-Trip Requests, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr.md)). This follows from the stateless-protocol rule in §5.1 and the `requestState` echo requirement above.

---

## 7. `subscriptions/listen` and notification categories

**SOURCE FACT** — Replacement scope: "`subscriptions/listen` opens a long-lived notification stream from the server to the client. Unlike one-off requests, the stream stays open and delivers notifications until the client cancels it. It replaces the former `resources/subscribe` RPC and the HTTP GET endpoint." ([Subscriptions, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/subscriptions.md)).

### 7.1 Notification filter

**SOURCE FACT** — "The client sends a `subscriptions/listen` request with a `notifications` filter specifying which event types it wants to receive. The server **MUST NOT** send notification types the client has not explicitly requested." ([Subscriptions, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/subscriptions.md)).

**SOURCE FACT** — Filter fields: "`toolsListChanged` — Receive `notifications/tools/list_changed` when tools change", "`promptsListChanged` — Receive `notifications/prompts/list_changed` when prompts change", "`resourcesListChanged` — Receive `notifications/resources/list_changed` when list changes", "`resourceSubscriptions` — Receive `notifications/resources/updated` for these resource URIs." ([Subscriptions, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/subscriptions.md)).

### 7.2 Acknowledgment and correlation

**SOURCE FACT** — "The server **MUST** send `notifications/subscriptions/acknowledged` as the first message carrying the subscription's ID in `_meta` under `io.modelcontextprotocol/subscriptionId`, and **MUST NOT** send any notification on the subscription before it." ([Subscriptions, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/subscriptions.md)).

**SOURCE FACT** — "The `notifications` field in the acknowledgment reflects the subset the server agreed to honor. Notification types the server does not support are omitted." ([Subscriptions, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/subscriptions.md)).

**SOURCE FACT** — "All notifications delivered on the stream carry `io.modelcontextprotocol/subscriptionId` in `_meta`, identifying the `subscriptions/listen` request that opened the stream. The value is the JSON-RPC ID of the `subscriptions/listen` request." ([Subscriptions, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/subscriptions.md)).

**SOURCE FACT** — Multiple subscriptions: "A client **MAY** have multiple active subscriptions concurrently ... Each subscription is identified by the JSON-RPC request ID of its `subscriptions/listen` request, and every notification on the stream carries that ID in `io.modelcontextprotocol/subscriptionId` so clients can demultiplex them." ([Subscriptions, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/subscriptions.md)).

### 7.3 Stream termination

**SOURCE FACT** — "A subscription ends when: The **client** cancels it — close the SSE stream (HTTP) or send `notifications/cancelled` referencing the `subscriptions/listen` request ID (stdio). The **server** tears it down (e.g., during shutdown) — it **SHOULD** send a successful `subscriptions/listen` response to signal a graceful end ... then close the stream. The underlying transport closes." ([Subscriptions, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/subscriptions.md)).

**SOURCE FACT** — Graceful closure result: `{ "jsonrpc": "2.0", "id": 1, "result": { "resultType": "complete", "_meta": { "io.modelcontextprotocol/subscriptionId": 1 } } }` ([Subscriptions, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/subscriptions.md)).

**SOURCE FACT** — Re-establishment on stdio: "On **stdio**, if the connection is terminated and then re-established, the client **MUST** re-send `subscriptions/listen` to re-establish its subscriptions — the server holds no subscription state across reconnections." ([Subscriptions, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/subscriptions.md)).

### 7.4 Other notification categories (from base protocol and patterns)

**SOURCE FACT** — Long-lived requests stay request/response: "Long-lived requests like `subscriptions/listen` remain request/response; the response is just an open stream of notifications. Their state is scoped to the request itself, not to the connection underneath." ([Basic Protocol Overview, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md)).

**SOURCE FACT** — Request-scoped notifications include "`notifications/progress`" and "`notifications/message`", described as "notifications scoped to it" while a request is in flight ([Message Patterns Overview, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/index.md)). On Streamable HTTP, such request-scoped notifications "flow only on the response stream of the request they relate to" and are "**not** delivered on the listen stream" ([Streamable HTTP, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md)).

**SOURCE FACT** — Three composition patterns are enumerated: "1. **Request and Response** ... 2. **Multi Round-Trip Requests (MRTR)** ... 3. **Subscribe and Notify**" ([Message Patterns Overview, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/index.md)).

**AI INFERENCE** — Change notifications (list changes, resource updates) come only via `subscriptions/listen`; per-request progress/logging notifications come on the in-flight request's own stream. A server author therefore has two distinct notification channels to wire, and must not send progress notifications on a listen stream. This follows from the "not delivered on the listen stream" rule and the request/response pattern definition.

---

## 8. Cancellation

**SOURCE FACT** — "The Model Context Protocol (MCP) supports optional cancellation of in-progress requests through notification messages. A client **SHOULD** send a cancellation notification to indicate that a request it previously issued should be terminated." ([Cancellation, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/cancellation.md)).

**SOURCE FACT** — Server cancellation is narrowly scoped: "A server **MUST** send `notifications/cancelled` referencing a `subscriptions/listen` request ID when it tears down that subscription stream ... Servers **MUST NOT** send `notifications/cancelled` for any other purpose." ([Cancellation, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/cancellation.md)).

**SOURCE FACT** — Notification payload includes "The ID of the request to cancel" and "An optional reason string": `{ "jsonrpc": "2.0", "method": "notifications/cancelled", "params": { "requestId": "123", "reason": "User requested cancellation" } }` ([Cancellation, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/cancellation.md)).

**SOURCE FACT** — Transport-specific: "**Streamable HTTP**: Closing the SSE response stream is the cancellation signal. The server **MUST** treat a client disconnect as cancellation of that request. No `notifications/cancelled` message is required or expected." and "**stdio**: There is no per-request stream to close. The client **MUST** send a `notifications/cancelled` notification referencing the request ID." ([Cancellation, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/cancellation.md)).

**SOURCE FACT** — Server-side handling: "Servers receiving cancellation notifications **SHOULD**: Stop processing the cancelled request, Free associated resources, Not send a response for the cancelled request." ([Cancellation, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/cancellation.md)).

**SOURCE FACT** — Timeouts: "Implementations **SHOULD** establish timeouts for all sent requests, to prevent hung connections and resource exhaustion." and "Implementations **MAY** choose to reset the timeout clock when receiving a progress notification corresponding to the request ... However, implementations **SHOULD** always enforce a maximum timeout, regardless of progress notifications." ([Cancellation, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/cancellation.md)).

**SOURCE FACT** — Race handling: "Due to network latency, cancellation notifications may arrive after request processing has completed, and potentially after a response has already been sent. Both parties **MUST** handle these race conditions gracefully." ([Cancellation, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/cancellation.md)).

**SOURCE FACT** — The stdio transport page repeats the server rule with an added obligation: "Servers **SHOULD** stop work on a cancelled request as soon as practical and **MUST NOT** send any further messages for it." ([stdio, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio.md)).

---

## 9. Progress

**SOURCE FACT** — "The Model Context Protocol (MCP) supports optional progress tracking for long-running operations through notification messages. The server **MAY** send progress notifications to report the status of requests the client has issued." ([Progress, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/progress.md)).

**SOURCE FACT** — Opt-in: "When a client wants to *receive* progress updates for a request, it includes a `progressToken` in the request metadata. Progress tokens **MUST** be a string or integer value ... but **MUST** be unique across all active requests." ([Progress, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/progress.md)).

**SOURCE FACT** — Notification fields: "The original progress token, The current progress value so far, An optional \"total\" value, An optional \"message\" value", with example `"progressToken": "abc123", "progress": 50, "total": 100, "message": "Reticulating splines..."` ([Progress, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/progress.md)).

**SOURCE FACT** — Monotonicity and types: "The `progress` value **MUST** increase with each notification, even if the total is unknown. The `progress` and the `total` values **MAY** be floating point. The `message` field **SHOULD** provide relevant human readable progress information." ([Progress, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/progress.md)).

**SOURCE FACT** — "Progress notifications **MUST** stop after completion." and "Both parties **SHOULD** implement rate limiting to prevent flooding." ([Progress, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/progress.md)).

**SOURCE FACT** — Opt-ing in is by request metadata: "When a client wants to *receive* progress updates for a request, it includes a `progressToken` in the request metadata." and the reserved-key table lists "`progressToken` — Opts the request into progress notifications" ([Progress, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/progress.md); [Basic Protocol Overview, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md)).

---

## 10. stdio transport rules

**SOURCE FACT** — "In the **stdio** transport, the client launches the MCP server as a subprocess. The two ends communicate over the subprocess's standard streams: The server reads JSON-RPC messages from `stdin` and writes JSON-RPC messages to `stdout`." ([stdio, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio.md)).

**SOURCE FACT** — Framing: "Messages are delimited by newlines, and **MUST NOT** contain embedded newlines." ([stdio, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio.md)). The legacy page uses the identical sentence ([Transports, 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports.md)).

**SOURCE FACT** — Logging and channel purity: "The server **MAY** write UTF-8 strings to `stderr` for any logging purposes including informational, debug, and error messages" and "The server **MUST NOT** write anything to its `stdout` that is not a valid MCP message. The client **MUST NOT** write anything to the server's `stdin` that is not a valid MCP message." ([stdio, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio.md)).

**SOURCE FACT** — Direction: "The client **MUST NOT** write JSON-RPC *responses*." and "The server **MUST NOT** write JSON-RPC *requests* to `stdout`. Server-to-client interactions are carried in `InputRequiredResult` replies." ([stdio, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio.md)).

**SOURCE FACT** — Message kinds written by the server: "(1) *Responses* to client requests, correlated by JSON-RPC `id`. (2) *Notifications* that relate to an in-flight request, such as `notifications/progress` and `notifications/message`. (3) *Notifications* delivered for an active `subscriptions/listen` request." ([stdio, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio.md)).

**SOURCE FACT** — "All messages share this single channel; there are no per-request streams." ([stdio, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio.md)).

**SOURCE FACT** — Metadata layer: "All request metadata for the stdio transport is carried inline in the JSON-RPC message body. ... There is no header layer." ([stdio, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio.md)).

**SOURCE FACT** — Cancellation on stdio: "To cancel an in-flight request, the client **MUST** send a `notifications/cancelled` notification referencing the request's ID." ([stdio, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio.md)).

**SOURCE FACT** — Shutdown: "The client **SHOULD** initiate shutdown by: 1. Closing the input stream to the child process ... 2. Waiting for the server to exit. 3. If the server does not exit within a reasonable time, forcibly terminating the process." and "Servers **SHOULD** exit promptly when their standard input is closed or reads return end-of-file." ([stdio, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio.md)).

**SOURCE FACT** — Unexpected termination: "If the server process exits unexpectedly, the client **SHOULD** restart it. Because the protocol is stateless, any in-flight requests are simply lost and the client can retry them against the fresh process." ([stdio, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio.md)).

**SOURCE FACT** — stdio back-compat probe: "A client that supports both modern ... and a legacy version that requires an `initialize` handshake **SHOULD** probe with `server/discover` before sending any other request, setting its preferred modern version in `_meta`." and "The fallback **MUST NOT** be keyed to one specific error code." ([stdio, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio.md)).

---

## 11. Streamable HTTP rules

**SOURCE FACT** — Origin and era: "Streamable HTTP was introduced in protocol version 2025-03-26 as a replacement for the HTTP+SSE transport from protocol version 2024-11-05." and "Revision 2026-07-28 changed the behavior of Streamable HTTP." ([Streamable HTTP, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md)).

**SOURCE FACT** — The two changes: "Removal of the GET stream endpoint. Removal of protocol-level sessions." ([Streamable HTTP, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md)).

**SOURCE FACT** — Shape: "The server exposes a single HTTP endpoint (the **MCP endpoint**) that accepts POST." and "The client sends every JSON-RPC request or notification as its own HTTP POST." and "The server answers each request with either a single JSON object or a Server-Sent Events (SSE) stream scoped to that request." ([Streamable HTTP, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md)).

**SOURCE FACT** — Endpoint mandate: "The server **MUST** provide a single HTTP endpoint path (hereafter referred to as the **MCP endpoint**) that supports POST." ([Streamable HTTP, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md)).

### 11.1 Security and endpoint

**SOURCE FACT** — "Servers **MUST** validate the `Origin` header on all incoming connections to prevent DNS rebinding attacks. If the `Origin` header is present and invalid, servers **MUST** respond with HTTP 403 Forbidden." and "When running locally, servers **SHOULD** bind only to localhost (127.0.0.1) rather than all network interfaces (0.0.0.0)." ([Streamable HTTP, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md)).

### 11.2 Sending messages (POST rules)

**SOURCE FACT** — "Every JSON-RPC message sent from the client **MUST** be a new HTTP POST request to the MCP endpoint." and "The client **MUST** include an `Accept` header listing both `application/json` and `text/event-stream` as supported content types." ([Streamable HTTP, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md)).

**SOURCE FACT** — "If the body is a JSON-RPC *notification*: If the server accepts it, the server **MUST** return HTTP status code `202 Accepted` with no body." ([Streamable HTTP, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md)).

**SOURCE FACT** — "If the body is a JSON-RPC *request*, the server **MUST** return either `Content-Type: application/json` (a single JSON object) or `Content-Type: text/event-stream` (an SSE response stream). The client **MUST** support both." ([Streamable HTTP, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md)).

**SOURCE FACT** — No client notifications over HTTP in this revision: "This revision of the core protocol defines no client-to-server *notifications* over Streamable HTTP. The only client-sent notification in the core protocol, `notifications/cancelled`, is used only on the stdio transport; on Streamable HTTP, closing the SSE response stream is itself the cancellation signal." ([Streamable HTTP, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md)).

### 11.3 Response stream rules

**SOURCE FACT** — "The server **MAY** send JSON-RPC *notifications* — for example, `notifications/progress` or `notifications/message` — before the final response. These notifications **MUST** relate to the originating client request." ([Streamable HTTP, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md)).

**SOURCE FACT** — "The server **MUST NOT** send independent JSON-RPC *requests* on this stream. Server-to-client interactions (sampling, elicitation, list-roots) are embedded as input requests inside an `InputRequiredResult` per MRTR (SEP-2322), not delivered as separate requests on this or any other stream." ([Streamable HTTP, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md)).

**SOURCE FACT** — "The final JSON-RPC *response* **SHOULD** terminate the stream." and "Resumable SSE streams via `Last-Event-ID` are not supported." ([Streamable HTTP, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md)).

**SOURCE FACT** — Buffering guidance: "When initiating an SSE stream, servers **SHOULD** include the `X-Accel-Buffering: no` header in the HTTP response." and long-lived streams should emit keep-alive comments "a line beginning with a colon, e.g. `:\r\n`" ([Streamable HTTP, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md)).

### 11.4 Protocol version header

**SOURCE FACT** — "Every POST request to the MCP endpoint **MUST** include an `MCP-Protocol-Version` header. For example: `MCP-Protocol-Version: 2026-07-28`" ([Streamable HTTP, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md)).

**SOURCE FACT** — "The header value **MUST** match the `io.modelcontextprotocol/protocolVersion` field carried in the request body's `_meta`. If the values do not match, the server **MUST** reject the request with `400 Bad Request` and a `HeaderMismatch` JSON-RPC error." ([Streamable HTTP, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md)).

**SOURCE FACT** — Unknown method: "If the server does not implement the requested RPC method, it **MUST** respond with `404 Not Found` and a JSON-RPC error with code `-32601` (`Method not found`)." ([Streamable HTTP, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md)).

**SOURCE FACT** — Pre-2025-06-18 tolerance: "A server that supports clients implementing protocol versions earlier than `2025-06-18` ... **MAY** treat a request that omits the header as protocol version `2025-03-26`." ([Streamable HTTP, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md)).

### 11.5 Standard request headers `Mcp-Method` / `Mcp-Name`

**SOURCE FACT** — Table: "`Mcp-Method` | `method` | All requests" and "`Mcp-Name` | `params.name` or `params.uri` | `tools/call`, `resources/read`, `prompts/get` requests", with the note "These headers are **REQUIRED** for compliance." ([Streamable HTTP, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md)).

**SOURCE FACT** — "If the `Mcp-Name` source value cannot be safely represented as a plain ASCII header value, clients **MUST** encode it using the Base64 sentinel format." ([Streamable HTTP, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md)).

### 11.6 Custom headers via `x-mcp-header`

**SOURCE FACT** — "MCP servers **MAY** designate specific tool parameters to be mirrored into HTTP headers using an `x-mcp-header` extension property in the parameter's schema within the tool's `inputSchema`." and "While the use of `x-mcp-header` is optional for servers, clients **MUST** support this feature." ([Streamable HTTP, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md)).

**SOURCE FACT** — Header naming: "The `x-mcp-header` property specifies the name portion used to construct the header name `Mcp-Param-{name}`." ([Streamable HTTP, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md)).

**SOURCE FACT** — Constraints include: "**MUST NOT** be empty", "**MUST** match HTTP field-name token syntax (`1*tchar`, [RFC 9110 Section 5.1](https://datatracker.ietf.org/doc/html/rfc9110#section-5.1))", "**MUST** only be applied to parameters with primitive types (integer, string, boolean). Parameters with type `number` are not permitted.", and "**MUST** only be applied to properties that are *statically reachable* from the schema root." ([Streamable HTTP, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md)).

**SOURCE FACT** — Client rejection: "Clients using the Streamable HTTP transport **MUST** reject tool definitions where any `x-mcp-header` value violates these constraints. Rejection means the client **MUST** exclude the invalid tool from the result of `tools/list`." ([Streamable HTTP, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md)).

**SOURCE FACT** — Value encoding sentinel: "`Mcp-Param-{Name}: =?base64?{Base64EncodedValue}?=`" and "The prefix `=?base64?` and suffix `?=` indicate that the value is Base64-encoded. These markers are case-sensitive and **MUST** appear exactly as shown (lowercase)." ([Streamable HTTP, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md)).

### 11.7 Server validation

**SOURCE FACT** — "Servers that process the request body **MUST** reject requests where the values specified in the headers do not match the corresponding values in the request body." with the rejection code "`-32020` | `HeaderMismatch` | The HTTP headers do not match the corresponding values in the request body, or required headers are missing/malformed." ([Streamable HTTP, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md)).

**SOURCE FACT** — Scenario table (selection): "Parameter value provided | Client MUST include the header | Server MUST validate header matches body"; "Parameter value is `null` | Client MUST omit the header | Server MUST NOT expect the header"; "Client omits header but value is in body | Non-conforming client | Server MUST reject the request". ([Streamable HTTP, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md)).

### 11.8 No sessions / no resumability / old-mechanism handling

**SOURCE FACT** — Previous shape (2025-03-26 through 2025-11-25): "servers could assign a session via the `Mcp-Session-Id` header (terminated with HTTP DELETE), clients could open a standalone SSE stream with HTTP GET to receive server-initiated messages, servers could send JSON-RPC *requests* on SSE streams, and streams were resumable via `Last-Event-ID`. None of these mechanisms are part of this revision." ([Streamable HTTP, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md)).

**SOURCE FACT** — Handling of old traffic: "HTTP GET or DELETE to the MCP endpoint: respond with `405 Method Not Allowed`. An `Mcp-Session-Id` header on a request: ignore it, and do not mint or echo session IDs. A `Last-Event-ID` header: ignore it; streams are not resumable." ([Streamable HTTP, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md)).

**SOURCE FACT** — HTTP back-compat detection: "A client that supports both modern ... and a legacy version that requires an `initialize` handshake **MAY** detect which era the server implements by attempting a modern request first. On `400 Bad Request`, the client **SHOULD** inspect the response body before falling back." ([Streamable HTTP, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md)).

### 11.9 Legacy Streamable HTTP (2025-11-25) — for contrast

**SOURCE FACT** — The legacy endpoint "**MUST** provide a single HTTP endpoint path ... that supports both POST and GET methods." ([Transports, 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports.md)).

**SOURCE FACT** — Legacy session management: "A server using the Streamable HTTP transport **MAY** assign a session ID at initialization time, by including it in an `MCP-Session-Id` header on the HTTP response containing the `InitializeResult`." and "If an `MCP-Session-Id` is returned by the server during initialization, clients ... **MUST** include it in the `MCP-Session-Id` header on all of their subsequent HTTP requests." ([Transports, 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports.md)).

**SOURCE FACT** — Legacy GET stream: "The client **MAY** issue an HTTP GET to the MCP endpoint. This can be used to open an SSE stream, allowing the server to communicate to the client, without the client first sending data via HTTP POST." ([Transports, 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports.md)).

**SOURCE FACT** — Legacy resumability: "If the client wishes to resume after a disconnection ... it **SHOULD** issue an HTTP GET to the MCP endpoint, and include the `Last-Event-ID` header to indicate the last event ID it received." ([Transports, 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports.md)).

**SOURCE FACT** — Legacy server-initiated requests: "The server **MAY** send JSON-RPC *requests* and *notifications* before sending the JSON-RPC *response*." ([Transports, 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports.md)).

**SOURCE FACT** — Legacy protocol version header: "If using HTTP, the client **MUST** include the `MCP-Protocol-Version: <protocol-version>` HTTP header on all subsequent requests to the MCP server" and "For backwards compatibility, if the server does *not* receive an `MCP-Protocol-Version` header ... the server **SHOULD** assume protocol version `2025-03-26`." ([Transports, 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports.md)).

**AI INFERENCE** — The 2026-07-28 Streamable HTTP binding drops the `Mcp-Session-Id` header, the GET SSE stream, server-initiated JSON-RPC requests on streams, and `Last-Event-ID` resumability, while adding mandatory `MCP-Protocol-Version`, `Mcp-Method`, and `Mcp-Name` headers plus optional `x-mcp-header` mirroring. This follows from the "Removal of the GET stream endpoint. Removal of protocol-level sessions." and "None of these mechanisms are part of this revision." SOURCE FACTS contrasted with the 2025-11-25 mechanisms above.

---

## 12. Deprecated HTTP+SSE transport

**SOURCE FACT** — Status: "**Deprecated**: The HTTP+SSE transport from protocol version 2024-11-05 has been deprecated since protocol version `2025-03-26` and is classified as Deprecated under the feature lifecycle policy ([SEP-2596](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2596)). New implementations **SHOULD NOT** adopt it; existing implementations **SHOULD** migrate to Streamable HTTP. It is eligible for removal in a future revision." ([Streamable HTTP, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md)).

**SOURCE FACT** — Server support approach: "Continue to host both the SSE and POST endpoints of the old transport, alongside the new \"MCP endpoint\" defined for the Streamable HTTP transport." ([Streamable HTTP, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md)).

**SOURCE FACT** — Client fallback: "Attempt to POST a request to the server URL ... If it fails with HTTP status code `400 Bad Request`, `404 Not Found`, or `405 Method Not Allowed` **and** the response body is not a recognized modern JSON-RPC error ... Issue a GET request to the server URL, expecting that this will open an SSE stream and return an `endpoint` event as the first event." ([Streamable HTTP, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md)).

**SOURCE FACT** — SEP reference for deprecation: the page cites "[SEP-2596](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2596)". ([Streamable HTTP, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md)). This is the only `SOURCE CLAIM` in this file, because it is a pull-request reference rather than the normative text itself; its rank is lower-tier than the surrounding specification prose.

---

## 13. Transport comparison (server-implementer view)

| Concern | stdio (2026-07-28) | Streamable HTTP (2026-07-28) |
| - | - | - |
| Framing | "Messages are delimited by newlines" ([stdio](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio.md)) | "a single JSON object or a request-scoped SSE stream" ([Streamable HTTP](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md)) |
| Metadata layer | "carried inline in the JSON-RPC message body ... There is no header layer." ([stdio](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio.md)) | mirrored to `MCP-Protocol-Version`, `Mcp-Method`, `Mcp-Name`, `Mcp-Param-*` ([Streamable HTTP](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md)) |
| Cancellation | "the client **MUST** send a `notifications/cancelled` notification" ([stdio](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio.md)) | "Closing the SSE response stream **MUST** be treated by the server as cancellation" ([Streamable HTTP](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md)) |
| Sessions | none; "the server holds no subscription state across reconnections" ([Subscriptions](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/subscriptions.md)) | "Removal of protocol-level sessions" ([Streamable HTTP](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md)) |
| Resumability | n/a (single shared channel) | "Resumable SSE streams via `Last-Event-ID` are not supported." ([Streamable HTTP](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md)) |
| Server→client input | only via `InputRequiredResult` ([stdio](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio.md)) | only via `InputRequiredResult` ([Streamable HTTP](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md)) |

**SOURCE FACT** — Custom transports: "Clients and servers **MAY** implement additional custom transport mechanisms" and "Implementers who choose to support custom transports **MUST** preserve the JSON-RPC message format, the message patterns, and the per-request metadata model." ([Transports Overview, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/index.md)).

**SOURCE FACT** — Reuse guidance: "Custom transports that run over a reliable bidirectional byte stream (e.g., Unix domain sockets or TCP) **SHOULD** reuse the stdio framing rather than defining a new one." ([Transports Overview, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/index.md)).

---

## 14. Failed retrievals and open items

- **UNKNOWN** — None of the twelve target URLs failed; every page was retrieved as its `.md` endpoint on 2026-10-02. There are therefore no UNKNOWN points attributable to retrieval failure in this file.
- **SOURCE FACT (scope reminder)** — The authoritative machine-readable definitions live in the schema, not only the prose pages: "The full specification of the protocol is defined as a TypeScript schema ... This is the source of truth for all protocol messages and structures." ([Basic Protocol Overview, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md)). Field-level details of `InputRequiredResult`, `InputRequests`, and `InputResponses` beyond the prose here were not fetched as separate schema pages and are **UNKNOWN** in this file.
- **NOT VERIFIED** — The exact SEP number embedded in the MRTR prose is "SEP-2322"; the page links it as `[SEP-2322](https://modelcontextprotocol.io/seps/2322-MRTR)` ([Streamable HTTP, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md)). The SEP document itself was not fetched, so its internal claims are **NOT VERIFIED** here.
- **SOURCE CLAIM** — The deprecated-transport classification cites the pull request [SEP-2596](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2596); the PR page was not fetched, so its contents beyond the specification's own reference are **NOT VERIFIED**.
