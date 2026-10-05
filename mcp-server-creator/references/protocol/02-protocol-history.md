# 02 — MCP Protocol History and Versioning

Research file for an MCP-server-creation report.
- Scan date: **2026-10-02**
- Current protocol revision: **2026-07-28**
- Every externally sourced statement carries an exact, short quotation plus an inline descriptive link to the source URL in the same line.

## Notation key (mandatory)

- **SOURCE FACT** — official specification/docs/code; quoted exactly.
- **SOURCE CLAIM** — lower-tier pages, marketing, blogs; quoted exactly, with rank noted.
- **AI INFERENCE** — synthesis by this agent, naming the quoted facts it follows from.
- **PLAUSIBLE, NOT VERIFIED** — possible but not established.
- **UNKNOWN** — cannot be decided from the available evidence.

Failed retrievals are recorded as results, not as proof of absence.

---

## 1. Revision timeline

**SOURCE FACT** — the official GitHub release list enumerates these releases (tags, in list order): `2026-07-28`, `2026-07-28 RC`, `2025-11-25`, `2025-11-25-RC`, `2025-06-18`, `2025-03-26`, `2024-11-05-final`, `2024-11-05`, `2024-10-07` — [Releases: modelcontextprotocol/modelcontextprotocol](https://github.com/modelcontextprotocol/modelcontextprotocol/releases). Note the list is reverse-chronological by release entry, not strictly by revision date.

**SOURCE FACT** — the GitHub release entries carry these exact descriptions and timestamps:

| Tag | Exact release-note text | Release label on page |
|---|---|---|
| `2024-10-07` | "Final update to version 2024-10-07 of the spec." — [release](https://github.com/modelcontextprotocol/modelcontextprotocol/releases) | — (released "06 Nov 10:59") |
| `2024-11-05` | "This release marks the initial 2024-11-05 revision of the Model Context Protocol." — [release](https://github.com/modelcontextprotocol/modelcontextprotocol/releases) | — (released "17 Jan 20:37") |
| `2024-11-05-final` | "This release marks the final 2024-11-05 revision of the Model Context Protocol, including all backwards compatible changes made since the initial 2024-11-05 release." — [release](https://github.com/modelcontextprotocol/modelcontextprotocol/releases) | — (released "26 Mar 13:53") |
| `2025-03-26` | "This release marks the initial 2025-03-26 revision of the Model Context Protocol." — [release](https://github.com/modelcontextprotocol/modelcontextprotocol/releases) | — (released "26 Mar 14:28") |
| `2025-06-18` | "This release marks the initial 2025-06-18 revision of the Model Context Protocol." — [release](https://github.com/modelcontextprotocol/modelcontextprotocol/releases) | — (released "18 Jun 20:09") |
| `2025-11-25-RC` | "This release marks the **release candidate (RC)** `2025-11-25` revision" — [release](https://github.com/modelcontextprotocol/modelcontextprotocol/releases) | Pre-release (released "15 Nov 06:06") |
| `2025-11-25` | "This release marks the **stable release** of the `2025-11-25` revision of the Model Context Protocol." — [release](https://github.com/modelcontextprotocol/modelcontextprotocol/releases) | — (released "25 Nov 21:17") |
| `2026-07-28-RC` | "This release marks the **release candidate (RC)** `2026-07-28` revision" — [release](https://github.com/modelcontextprotocol/modelcontextprotocol/releases) | Pre-release (released "29 May 12:51") |
| `2026-07-28` | "This release marks the **stable release** of the `2026-07-28` revision of the Model Context Protocol." — [release](https://github.com/modelcontextprotocol/modelcontextprotocol/releases) | Latest (released "28 Jul 16:47") |

**SOURCE FACT** — the RC notes warn against treating an RC as final: "**To users and implementers:** this specification is not final. Changes may be introduced between the RC and the final release." — [2026-07-28 RC release note](https://github.com/modelcontextprotocol/modelcontextprotocol/releases)

**SOURCE FACT** — the same RC note disclaims coordinated SDK adoption: "SDKs will adopt this version at their own pace, and the prior version of the spec may remain in use for an undetermined amount of time." — [2025-11-25-RC release note](https://github.com/modelcontextprotocol/modelcontextprotocol/releases)

**SOURCE FACT** — the 2025-03-26 and 2025-06-18 release notes state the negotiation intent: "The spec describes how clients and servers perform version negotiation with one another, permitting backwards and forwards compatibility." — [2025-03-26 release](https://github.com/modelcontextprotocol/modelcontextprotocol/releases)

### 1.1 Ordered revision list (protocol revisions only)

**AI INFERENCE** — deduplicating the release list above to protocol *revisions* (excluding RCs and the `-final` maintenance tag, which explicitly bundles backwards-compatible changes into `2024-11-05`), the ordered revisions named across the sources are:

1. `2024-10-07`
2. `2024-11-05` (plus `2024-11-05-final`, same protocol date)
3. `2025-03-26`
4. `2025-06-18`
5. `2025-11-25`
6. `2026-07-28` (current)

This ordering follows from the GitHub release list and the compare links embedded in each changelog (e.g. the `2025-03-26` changelog compares against `2024-11-05`, and the `2026-07-28` changelog against `2025-11-25`), both retrieved above.

---

## 2. Status labels: Draft / Current / Final

**SOURCE FACT** — "Revisions may be marked as: **Draft**: in-progress specifications, not yet ready for consumption. **Current**: the current protocol version, which is ready for use and may continue to receive backwards compatible changes. **Final**: past, complete specifications that will not be changed." — [Specification — Versioning](https://modelcontextprotocol.io/specification/versioning)

**SOURCE FACT** — "The **current** protocol version is [**2026-07-28**]." — [Specification — Versioning](https://modelcontextprotocol.io/specification/versioning)

**SOURCE FACT** — the GitHub releases page labels the `2026-07-28` tag "Latest" and the two RC tags "Pre-release" — [Releases](https://github.com/modelcontextprotocol/modelcontextprotocol/releases).

**AI INFERENCE** — `2026-07-28` is the **Current** revision (explicitly stated), and the RC tags are neither Current nor Final (labelled "Pre-release" and described as "not final"). For the earlier revisions, the fetched versioning page does **not** enumerate a per-revision status column, so applying "Final" to each individually is inference from the definition ("past, complete specifications"), not a direct quote. Only `2024-11-05-final` carries an explicit "final" label in its release note.

**UNKNOWN** — whether the specification site currently renders any *Draft* revision alongside `2026-07-28` is not determinable from the fetched pages. The versioning page names a single current version and does not link a draft.

---

## 3. Versioning scheme

**SOURCE FACT** — "The Model Context Protocol uses string-based version identifiers following the format `YYYY-MM-DD`, to indicate the last date backwards incompatible changes were made." — [Specification — Versioning](https://modelcontextprotocol.io/specification/versioning)

**SOURCE FACT** — backwards-compatible changes do not bump the date: "The protocol version will *not* be incremented when the protocol is updated, as long as the changes maintain backwards compatibility. This allows for incremental improvements while preserving interoperability." — [Specification — Versioning](https://modelcontextprotocol.io/specification/versioning)

**SOURCE FACT** — the `2024-11-05-final` release is the concrete example of this rule: a later tag for the same protocol date "including all backwards compatible changes made since the initial 2024-11-05 release." — [release](https://github.com/modelcontextprotocol/modelcontextprotocol/releases)

### 3.1 Feature lifecycle and deprecation

**SOURCE FACT** — "Individual features of the specification may additionally be marked as **Deprecated** under the feature lifecycle and deprecation policy: the feature remains part of the specification, but is scheduled for removal." — [Specification — Versioning](https://modelcontextprotocol.io/specification/versioning)

**SOURCE FACT** — the minimum deprecation window: deprecated features "remain in the specification for at least twelve months, or at least ninety days under the policy's expedited-removal exception, before they become eligible for removal, after which they may be **Removed** in a future revision." — [Specification — Versioning](https://modelcontextprotocol.io/specification/versioning)

**SOURCE FACT** — currently deprecated features are tracked: "Features that are currently Deprecated are listed in the [deprecated features registry]." — [Specification — Versioning](https://modelcontextprotocol.io/specification/versioning)

**SOURCE FACT** — the 2026-07-28 changelog records adoption of the policy: "Adopt a specification feature lifecycle and deprecation policy defining the Active, Deprecated, and Removed feature states, a minimum twelve-month deprecation window, and a registry of deprecated features." — [Key Changes (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/changelog.md)

---

## 4. How negotiation works now (2026-07-28, "modern")

### 4.1 Per-request `_meta` protocol version

**SOURCE FACT** — "Every request declares the protocol version it is using via the `io.modelcontextprotocol/protocolVersion` key in its `_meta` field, and the server accepts or rejects each request independently." — [Specification — Versioning](https://modelcontextprotocol.io/specification/versioning)

**SOURCE FACT** — "There is no negotiation handshake. Every request carries its protocol version, and the server accepts or rejects each request independently" — [Specification — Versioning and Compatibility](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md)

**SOURCE FACT** — multiple simultaneous versions are allowed: "Clients and servers **MAY** support multiple protocol versions simultaneously." — [Specification — Versioning](https://modelcontextprotocol.io/specification/versioning)

### 4.2 `MCP-Protocol-Version` header (Streamable HTTP)

**SOURCE FACT** — "On Streamable HTTP, the same value is also carried in the `MCP-Protocol-Version` header." — [Specification — Versioning](https://modelcontextprotocol.io/specification/versioning)

**SOURCE FACT** — restated at the basic-protocol level: "On HTTP, this is also carried in the `MCP-Protocol-Version` header." — [Specification — Versioning and Compatibility](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md)

### 4.3 `UnsupportedProtocolVersionError`

**SOURCE FACT** — "If the server does not implement the requested version (whether the version is unknown to the server, or is a known version the server has chosen not to support), it **MUST** respond with an `UnsupportedProtocolVersionError` listing the versions it does support:" — [Specification — Versioning and Compatibility](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md)

**SOURCE FACT** — the exact error shape uses JSON-RPC error code `-32022`:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": {
    "code": -32022,
    "message": "Unsupported protocol version",
    "data": {
      "supported": ["2026-07-28", "2025-11-25"],
      "requested": "1900-01-01"
    }
  }
}
```
— [Specification — Versioning and Compatibility](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md)

**SOURCE FACT** — "The client **SHOULD** select a mutually supported version from the `supported` list and retry the request, or surface an error to the user if no compatible version exists." — [Specification — Versioning and Compatibility](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md)

**SOURCE FACT** — error-code provenance: "Renumber the error codes introduced in this draft accordingly — `HeaderMismatch` `-32001` → `-32020`, `MissingRequiredClientCapability` `-32003` → `-32021`, `UnsupportedProtocolVersion` `-32004` → `-32022`." — [Key Changes (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/changelog.md)

### 4.4 `server/discover`

**SOURCE FACT** — "Servers **MUST** implement `server/discover`. Clients **MAY** call it before sending any other requests to learn the server's supported versions up front, but are not required to: a client is free to invoke any RPC inline and handle `UnsupportedProtocolVersionError` if its preferred version is not supported." — [Specification — Versioning and Compatibility](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md)

**SOURCE FACT** — "Clients that want to select a version up front can call `server/discover`, a mandatory RPC that returns the server's supported protocol versions, capabilities, and identity in a single request. Calling it is optional: a client is free to send any request directly and handle a version error if one comes back." — [Specification — Versioning](https://modelcontextprotocol.io/specification/versioning)

**SOURCE FACT** — the changelog frames `server/discover` as new in this revision: "Add `server/discover`: servers MUST implement this RPC to advertise their supported protocol versions, capabilities, and identity." — [Key Changes (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/changelog.md)

**SOURCE FACT** — discovery is separate from the handshake removal: "Make MCP stateless: remove the `initialize`/`notifications/initialized` handshake. Every request now carries its protocol version and client capabilities in `_meta`." — [Key Changes (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/changelog.md)

### 4.5 Extension negotiation

**SOURCE FACT** — "Clients and servers can negotiate support for optional extensions beyond the core protocol. Extensions are advertised in the `extensions` field of capabilities, which is a map of extension identifiers to per-extension settings objects." — [Specification — Versioning and Compatibility](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md)

**SOURCE FACT** — fallback rule: "If one party supports an extension but the other does not, the supporting party **MUST** either revert to core protocol behavior or reject the request with an appropriate error." — [Specification — Versioning and Compatibility](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md)

---

## 5. How negotiation worked under legacy (handshake) revisions

**SOURCE FACT** — "**Legacy**: protocol versions that establish a session with an `initialize` handshake (`2025-11-25` and earlier)." — [Specification — Versioning and Compatibility](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md)

**SOURCE FACT** — the 2025-06-18 revision required the negotiated version on later HTTP requests: "Require negotiated protocol version to be specified via `MCP-Protocol-Version` header in subsequent requests when using HTTP" — [Key Changes (2025-06-18)](https://modelcontextprotocol.io/specification/2025-06-18/changelog.md). This is an example of the handshake-first model: version first negotiated, then echoed on subsequent requests.

**SOURCE FACT** — legacy clients lack a forward path: "Legacy clients have no fall-forward mechanism." — [Specification — Versioning and Compatibility](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md)

**SOURCE FACT** — a modern-only server should help legacy clients diagnose: "A server that supports only modern versions **SHOULD** name the protocol versions it supports in any error it returns to an `initialize` request, on any transport: legacy clients have no fall-forward mechanism, and this message may be the only diagnostic they can surface to users." — [Specification — Versioning and Compatibility](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md)

**AI INFERENCE** — under legacy revisions the client and server first agree a version via the `initialize` handshake and then operate within that session; under 2026-07-28 there is no session and every request is independently versioned via `_meta`/header. This follows from the Legacy definition plus "There is no negotiation handshake" and the changelog's "remove the `initialize`/`notifications/initialized` handshake."

**UNKNOWN** — the exact legacy `initialize` request/response schema and version-selection algorithm for `2025-11-25` are not contained in the URLs fetched for this file (they live under the older revision's lifecycle/version-negotiation pages, which were not fetched).

---

## 6. Backward / forward compatibility and era detection

**SOURCE FACT** — "**Dual-era**: an implementation that supports both modern and legacy versions." — [Specification — Versioning and Compatibility](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md)

**SOURCE FACT** — detection mechanics on stdio: "probe with `server/discover` and fall back on any error that is not a recognized modern error." — [Specification — Versioning and Compatibility](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md)

**SOURCE FACT** — detection mechanics on Streamable HTTP: "attempt a modern request and inspect the body of a `400 Bad Request` before falling back." — [Specification — Versioning and Compatibility](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md)

**SOURCE FACT** — how to distinguish eras: "a recognized modern JSON-RPC error (such as `UnsupportedProtocolVersionError`) identifies a modern server: the client retries with a supported version rather than falling back. Anything else identifies a legacy server." — [Specification — Versioning and Compatibility](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md)

**SOURCE FACT** — "The era determination is a property of the server, not of an individual request. Clients **SHOULD** cache the result for the lifetime of the server process (stdio) or origin (HTTP), and **MAY** persist it across restarts of the same server configuration, re-probing if the cached assumption later fails." — [Specification — Versioning and Compatibility](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md)

### 6.1 Compatibility matrix (exact entries)

**SOURCE FACT** — the matrix states, for client/server eras:

- Modern ↔ Modern: "Works. `server/discover` is optional; version mismatches surface as `UnsupportedProtocolVersionError` and the client retries with a mutually supported version." — [Specification — Versioning and Compatibility](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md)
- Modern client / Legacy server: "Fails. The server may reject the request with an implementation-defined error, stay silent, or even process an era-ambiguous method under legacy semantics." — [Specification — Versioning and Compatibility](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md)
- Dual-era client / Modern server: "Works. The stdio probe returns a `DiscoverResult` (or `UnsupportedProtocolVersionError`); on HTTP, the first modern request succeeds or returns a modern error." — [Specification — Versioning and Compatibility](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md)
- Dual-era client / Legacy server: "Works. stdio: the probe returns a non-modern error or times out, and the client falls back to `initialize`." — [Specification — Versioning and Compatibility](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md)
- Legacy client / Modern server: "Fails. stdio: the server rejects `initialize` with a JSON-RPC error ... Legacy clients have no fall-forward mechanism." — [Specification — Versioning and Compatibility](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md)
- Legacy client / Dual-era server: "Works. The server answers `initialize` and serves the client according to the negotiated legacy revision." — [Specification — Versioning and Compatibility](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md)
- Legacy ↔ Legacy: "Works according to the legacy revision; out of scope for this document." — [Specification — Versioning and Compatibility](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md)

**SOURCE FACT** — dual-era server behavior: "A request carrying modern per-request `_meta` is served statelessly according to this revision. An `initialize` request selects legacy semantics, scoped to the stdio process (stdio) or the session (HTTP), as specified by the negotiated legacy protocol version." — [Specification — Versioning and Compatibility](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md)

**AI INFERENCE** — for a server author, the compatibility matrix implies supporting `2025-11-25` and `2026-07-28` at once requires a "dual-era" server that branches on whether an `initialize` handshake is present; a modern-only server is simpler but cannot serve un-upgraded legacy clients. This follows from the Dual-era definition and the Legacy/Modern failure rows.

---

## 7. Per-revision headline changes

### 7.1 `2026-07-28` (current; since `2025-11-25`)

**SOURCE FACT** — the changelog's major changes, quoted by item:

1. "Remove protocol-level sessions and the `Mcp-Session-Id` header from the Streamable HTTP transport." — [Key Changes (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/changelog.md)
2. "Make MCP stateless: remove the `initialize`/`notifications/initialized` handshake. Every request now carries its protocol version and client capabilities in `_meta`." — [Key Changes (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/changelog.md)
3. "Add `server/discover`: servers MUST implement this RPC to advertise their supported protocol versions, capabilities, and identity." — [Key Changes (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/changelog.md)
4. "Replace the HTTP GET endpoint and `resources/subscribe`/`resources/unsubscribe` with `subscriptions/listen`: a single long-lived POST-response stream for opted-in server-to-client change notifications." — [Key Changes (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/changelog.md)
5. "Remove `ping`, `logging/setLevel`, and `notifications/roots/list_changed`. Log level is now set per-request via `io.modelcontextprotocol/logLevel` in `_meta`." — [Key Changes (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/changelog.md)
6. "Move experimental tasks out of the core protocol and into an official extension (`io.modelcontextprotocol/tasks`)." — [Key Changes (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/changelog.md)
7. "Multi Round-Trip Requests (MRTR) pattern introduced which replaces the previous approach of sending server-initiated requests, such as `roots/list`, `sampling/createMessage`, or `elicitation/create`." — [Key Changes (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/changelog.md)
8. "All results now carry a required `resultType` field: `"complete"` for ordinary results and `"input_required"` for multi round-trip request interim results." — [Key Changes (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/changelog.md)
9. "Remove SSE stream resumability and message redelivery (the `Last-Event-ID` header and SSE event IDs) from the Streamable HTTP transport." — [Key Changes (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/changelog.md)

**SOURCE FACT** — notable minor changes include caching fields: "Require `ttlMs` and `cacheScope` fields on results returned by `tools/list`, `prompts/list`, `resources/list`, `resources/read`, and `resources/templates/list`." — [Key Changes (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/changelog.md); and deterministic listings: "Servers **SHOULD** return tools from `tools/list` in a deterministic order to enable client-side caching and improve LLM prompt cache hit rates." — [Key Changes (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/changelog.md)

**SOURCE FACT** — deprecations introduced: "Deprecate the Roots, Sampling, and Logging features" and "Reclassify the HTTP+SSE transport (deprecated since protocol version `2025-03-26`) as Deprecated under the feature lifecycle policy." — [Key Changes (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/changelog.md)

**SOURCE FACT** — the changelog's own comparison target: "This document lists changes made to the Model Context Protocol (MCP) specification since the previous revision, [2025-11-25]." — [Key Changes (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/changelog.md)

### 7.2 `2025-11-25` (since `2025-06-18`)

**SOURCE FACT** — major changes, quoted by item:

1. "Enhance authorization server discovery with support for OpenID Connect Discovery 1.0." — [Key Changes (2025-11-25)](https://modelcontextprotocol.io/specification/2025-11-25/changelog.md)
2. "Allow servers to expose icons as additional metadata for tools, resources, resource templates, and prompts." — [Key Changes (2025-11-25)](https://modelcontextprotocol.io/specification/2025-11-25/changelog.md)
3. "Enhance authorization flows with incremental scope consent via `WWW-Authenticate`" — [Key Changes (2025-11-25)](https://modelcontextprotocol.io/specification/2025-11-25/changelog.md)
4. "Provide guidance on tool names" — [Key Changes (2025-11-25)](https://modelcontextprotocol.io/specification/2025-11-25/changelog.md)
5. "Update `ElicitResult` and `EnumSchema` to use a more standards-based approach and support titled, untitled, single-select, and multi-select enums." — [Key Changes (2025-11-25)](https://modelcontextprotocol.io/specification/2025-11-25/changelog.md)
6. "Added support for URL mode elicitation" — [Key Changes (2025-11-25)](https://modelcontextprotocol.io/specification/2025-11-25/changelog.md)
7. "Add tool calling support to sampling via `tools` and `toolChoice` parameters" — [Key Changes (2025-11-25)](https://modelcontextprotocol.io/specification/2025-11-25/changelog.md)
8. "Add support for OAuth Client ID Metadata Documents as a recommended client registration mechanism" — [Key Changes (2025-11-25)](https://modelcontextprotocol.io/specification/2025-11-25/changelog.md)
9. "Add experimental support for tasks to enable tracking durable requests with polling and deferred result retrieval" — [Key Changes (2025-11-25)](https://modelcontextprotocol.io/specification/2025-11-25/changelog.md)

**SOURCE FACT** — a notable minor change: "Establish JSON Schema 2020-12 as the default dialect for MCP schema definitions." — [Key Changes (2025-11-25)](https://modelcontextprotocol.io/specification/2025-11-25/changelog.md)

**SOURCE FACT** — governance changes: "Formalize Model Context Protocol governance structure"; "Formalize Working Groups and Interest Groups in MCP governance"; "Establish SDK tiering system with clear requirements for feature support and maintenance commitments." — [Key Changes (2025-11-25)](https://modelcontextprotocol.io/specification/2025-11-25/changelog.md)

**SOURCE FACT** — comparison target: "changes made ... since the previous revision, [2025-06-18]." — [Key Changes (2025-11-25)](https://modelcontextprotocol.io/specification/2025-11-25/changelog.md)

### 7.3 `2025-06-18` (since `2025-03-26`)

**SOURCE FACT** — major changes, quoted by item:

1. "Remove support for JSON-RPC **batching**" — [Key Changes (2025-06-18)](https://modelcontextprotocol.io/specification/2025-06-18/changelog.md)
2. "Add support for structured tool output" — [Key Changes (2025-06-18)](https://modelcontextprotocol.io/specification/2025-06-18/changelog.md)
3. "Classify MCP servers as OAuth Resource Servers, adding protected resource metadata to discover the corresponding Authorization server." — [Key Changes (2025-06-18)](https://modelcontextprotocol.io/specification/2025-06-18/changelog.md)
4. "Require MCP clients to implement Resource Indicators as described in RFC 8707 to prevent malicious servers from obtaining access tokens." — [Key Changes (2025-06-18)](https://modelcontextprotocol.io/specification/2025-06-18/changelog.md)
5. "Clarify security considerations and best practices in the authorization spec and in a new security best practices page." — [Key Changes (2025-06-18)](https://modelcontextprotocol.io/specification/2025-06-18/changelog.md)
6. "Add support for **elicitation**, enabling servers to request additional information from users during interactions." — [Key Changes (2025-06-18)](https://modelcontextprotocol.io/specification/2025-06-18/changelog.md)
7. "Add support for **resource links** in tool call results." — [Key Changes (2025-06-18)](https://modelcontextprotocol.io/specification/2025-06-18/changelog.md)
8. "Require negotiated protocol version to be specified via `MCP-Protocol-Version` header in subsequent requests when using HTTP" — [Key Changes (2025-06-18)](https://modelcontextprotocol.io/specification/2025-06-18/changelog.md)
9. "Change **SHOULD** to **MUST** in Lifecycle Operation" — [Key Changes (2025-06-18)](https://modelcontextprotocol.io/specification/2025-06-18/changelog.md)

**SOURCE FACT** — comparison target: "changes made ... since the previous revision, [2025-03-26]." — [Key Changes (2025-06-18)](https://modelcontextprotocol.io/specification/2025-06-18/changelog.md)

### 7.4 `2025-03-26` (since `2024-11-05`)

**SOURCE FACT** — major changes, quoted by item:

1. "Added a comprehensive **authorization framework** based on OAuth 2.1" — [Key Changes (2025-03-26)](https://modelcontextprotocol.io/specification/2025-03-26/changelog.md)
2. "Replaced the previous HTTP+SSE transport with a more flexible **Streamable HTTP transport**" — [Key Changes (2025-03-26)](https://modelcontextprotocol.io/specification/2025-03-26/changelog.md)
3. "Added support for JSON-RPC **batching**" — [Key Changes (2025-03-26)](https://modelcontextprotocol.io/specification/2025-03-26/changelog.md)
4. "Added comprehensive **tool annotations** for better describing tool behavior, like whether it is read-only or destructive" — [Key Changes (2025-03-26)](https://modelcontextprotocol.io/specification/2025-03-26/changelog.md)

**SOURCE FACT** — other schema changes: "Added `message` field to `ProgressNotification`"; "Added support for audio data, joining the existing text and image content types"; "Added `completions` capability to explicitly indicate support for argument autocompletion suggestions" — [Key Changes (2025-03-26)](https://modelcontextprotocol.io/specification/2025-03-26/changelog.md)

**SOURCE FACT** — comparison target: "changes made ... since the previous revision, [2024-11-05]." — [Key Changes (2025-03-26)](https://modelcontextprotocol.io/specification/2025-03-26/changelog.md)

### 7.5 `2024-11-05` and `2024-10-07`

**SOURCE FACT** — `2024-10-07` is described only as "Final update to version 2024-10-07 of the spec." — [release](https://github.com/modelcontextprotocol/modelcontextprotocol/releases)

**SOURCE FACT** — `2024-11-05-final` "marks the final 2024-11-05 revision ... including all backwards compatible changes made since the initial 2024-11-05 release." — [release](https://github.com/modelcontextprotocol/modelcontextprotocol/releases)

**UNKNOWN** — a per-change changelog for `2024-11-05` or earlier was not among the fetched URLs and is not quoted here. The `2025-03-26` changelog only states what changed *since* `2024-11-05`, not what `2024-11-05` itself introduced.

---

## 8. Governance and cadence

**SOURCE FACT** — the protocol's SEP process: "Formalize PR-based SEP workflow with markdown files in `seps/` directory, PR-derived numbering, sponsor responsibilities, and status management via PR labels." — [Key Changes (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/changelog.md)

**SOURCE FACT** — the design-principles page explains that proposals are evaluated under those principles: "They are meant as guidance by and for the community when developing Spec Enhancement Proposals (SEPs) and extensions." — [Design Principles](https://modelcontextprotocol.io/community/design-principles.md)

**SOURCE FACT** — release candidates precede stable releases: the `2025-11-25-RC` note says the spec "is available in draft form" and warns "this specification is not final. Changes may be introduced between the RC and the final release." — [2025-11-25-RC release](https://github.com/modelcontextprotocol/modelcontextprotocol/releases); the `2026-07-28 RC` note uses the same wording — [2026-07-28 RC release](https://github.com/modelcontextprotocol/modelcontextprotocol/releases).

**SOURCE FACT** — the versioning page states the date-based rule that governs cadence, quoted in §3: the date "indicate[s] the last date backwards incompatible changes were made", and the version is not incremented for backwards-compatible changes. — [Specification — Versioning](https://modelcontextprotocol.io/specification/versioning)

**UNKNOWN** — no fetched source states a fixed *planned* release cadence (e.g., "every N months") or a scheduled date for the next revision. The observed revision dates (`2024-11-05`, `2025-03-26`, `2025-06-18`, `2025-11-25`, `2026-07-28`) are real but a formal cadence commitment could not be confirmed from the available evidence.

**AI INFERENCE** — the intervals between stable revisions (roughly: 2024-11 → 2025-03 → 2025-06 → 2025-11 → 2026-07) are consistent with a multi-month cadence punctuated by release candidates, but the sources do not declare this as policy; treat the cadence itself as unverified.

---

## 9. Retrieval log for this file

| URL | Result |
|---|---|
| https://modelcontextprotocol.io/specification/versioning | Retrieved |
| https://modelcontextprotocol.io/docs/2026-07-28/learn/versioning.md | Retrieved (identical content to the spec `versioning` page) |
| https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md | Retrieved |
| https://modelcontextprotocol.io/specification/2026-07-28/changelog.md | Retrieved |
| https://modelcontextprotocol.io/specification/2025-11-25/changelog.md | Retrieved |
| https://modelcontextprotocol.io/specification/2025-06-18/changelog.md | Retrieved |
| https://modelcontextprotocol.io/specification/2025-03-26/changelog.md | Retrieved |
| https://github.com/modelcontextprotocol/modelcontextprotocol/releases | Retrieved |

All required URLs for this file were retrieved successfully on 2026-10-02. No failed retrievals.

---

## 10. Open / undecided items (not resolved here)

- No fetched source states a formal planned release cadence. **UNKNOWN** (§8).
- Per-revision status labels beyond `2026-07-28` (Current) and `2024-11-05-final` (explicitly "final") are not directly quoted. **AI INFERENCE / UNKNOWN** (§2).
- The exact legacy `initialize` handshake schema and version-selection algorithm for `2025-11-25` and earlier were not fetched. **UNKNOWN** (§5).
- A changelog for `2024-11-05`/`2024-10-07` was not fetched. **UNKNOWN** (§7.5).
