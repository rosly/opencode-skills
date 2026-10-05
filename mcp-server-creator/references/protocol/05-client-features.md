# MCP Client Features Servers Interact With: Roots, Sampling, Elicitation (Revision 2026-07-28)

Research file for the report on MCP servers for LLM agents. All externally sourced facts below carry a short exact quotation and an inline link to the source URL in the same sentence. Notation used: **SOURCE FACT**, **SOURCE CLAIM (rank)**, **AI INFERENCE**, **PLAUSIBLE NOT VERIFIED**, **UNKNOWN**.

## 1. The 2026-07-28 change: server-initiated requests replaced by MRTR

**SOURCE FACT** — The MRTR page states the breaking change: "Multi Round-Trip Requests (MRTR) was introduced in this version of the MCP specification. This replaces the previous approach of sending server-initiated requests. Servers **MUST** send server-to-client requests (such as `roots/list`, `sampling/createMessage`, or `elicitation/create`) using the MRTR pattern. The previous pattern of server-initiated requests is no longer supported. This is a breaking change." ([basic/patterns/mrtr.md](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr.md)).

**SOURCE FACT** — The high-level flow: "1. Client sends an initial request to the server with the parameters needed to perform the operation. 2. Server determines that additional information is required to fulfill the request and responds requesting more information. 3. Client gathers the requested information from the user or other sources, then retries the original request including the additional requested information. 4. Server determines it has sufficient information to complete the operation, and responds with the final result." ([basic/patterns/mrtr.md](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr.md)).

**SOURCE FACT** — Core types: "An `InputRequests` object is a map of server-client requests. Keys are server-assigned string identifiers; values are request objects (e.g., `ElicitRequest`, `CreateMessageRequest`, or `ListRootsRequest`)." ([basic/patterns/mrtr.md](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr.md)).

**SOURCE FACT** — "An `InputResponses` object is a map of client responses to the server requests. Keys correspond to the keys in the `InputRequests` map; values are the client's result for each request (e.g., `ElicitResult`, `CreateMessageResult`, or `ListRootsResult`)." ([basic/patterns/mrtr.md](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr.md)).

**SOURCE FACT** — `InputRequiredResult` fields: "`inputRequests` *(optional)*: An `InputRequests` map of server-initiated requests that the client must fulfill." and "`requestState` *(optional)*: An opaque string meaningful only to the server. Clients **MUST NOT** inspect, parse, modify, or make any assumptions about its contents." ([basic/patterns/mrtr.md](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr.md)).

**SOURCE FACT** — Supported requests: "Servers **MAY** send `InputRequiredResult` responses on the following client requests:" — `prompts/get` (Yes), `resources/read` (Yes), `tools/call` (Yes); "Servers **MUST NOT** send `InputRequiredResult` responses on any other client requests." ([basic/patterns/mrtr.md](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr.md)).

**SOURCE FACT** — Server requirement on capabilities: "Servers **MUST NOT** send an `inputRequests` that the client has not declared support for in its capabilities. For example, if a client does not declare support for `elicitation`, the server **MUST NOT** include any `elicitation/create` requests in the `inputRequests` field." ([basic/patterns/mrtr.md](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr.md)).

**SOURCE FACT** — Client retry rules: "The JSON-RPC `id` **MUST** be different between the initial request and the retry, as they are independent requests." and "If an `InputRequiredResult` contains the `requestState` field, the client **MUST** echo back the exact value of that field when retrying the original request." ([basic/patterns/mrtr.md](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr.md)).

**SOURCE FACT** — State security: "If a client request contains a `requestState` field, servers **MUST** treat `requestState` as an attacker-controlled input. If `requestState` influences authorization, resource access, or business logic, servers **MUST** protect its integrity (e.g. HMAC or AEAD) and **MUST** reject state that fails verification." ([basic/patterns/mrtr.md](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr.md)).

**SOURCE FACT** — Replay protection: "To prevent replay, servers **SHOULD** include the following inside the integrity-protected `requestState` payload and verify each on receipt: the authenticated principal ...; a short expiry (TTL) ...; an identifier for the originating request" ([basic/patterns/mrtr.md](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr.md)).

**SOURCE FACT** — "Servers **MUST** include at least one of `inputRequests` or `requestState` in every `InputRequiredResult` response." ([basic/patterns/mrtr.md](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr.md)).

**AI INFERENCE** — Based on the quoted MRTR statements, the 2026-07-28 revision inverts the direction of server-to-client interaction: instead of the server pushing a request on its own stream, the server returns an `InputRequiredResult` on the client's original request and the client retries with `inputResponses`. This is why Roots, Sampling, and Elicitation are all described in terms of `InputRequiredResult` on the 2026-07-28 pages.

## 2. Roots

### 2.1 What it is and who initiates

**SOURCE FACT** — "The Model Context Protocol (MCP) provides a standardized way for clients to expose filesystem 'roots' to servers. Roots inform servers about the directories and files the client considers relevant, so that servers can focus their operations accordingly. They are informational guidance rather than an access-control mechanism. The protocol does not enforce that servers stay within roots. Servers can request the list of roots from supporting clients." ([client/roots.md](https://modelcontextprotocol.io/specification/2026-07-28/client/roots.md)).

**SOURCE FACT** — Roots are client-owned and server-requested: "To retrieve roots during the processing of a client request, servers send an `InputRequiredResult` containing a `roots/list` request" ([client/roots.md](https://modelcontextprotocol.io/specification/2026-07-28/client/roots.md)).

### 2.2 Deprecation

**SOURCE FACT** — "**Deprecated**: The Roots feature is deprecated as of protocol version `2026-07-28` (SEP-2577). Under the feature lifecycle policy, it remains in the specification for at least twelve months after this revision's release before it becomes eligible for removal. New implementations **SHOULD NOT** adopt it; existing implementations **SHOULD** migrate to passing directories or files via tool parameters, resource URIs, or server configuration." ([client/roots.md](https://modelcontextprotocol.io/specification/2026-07-28/client/roots.md)).

**SOURCE FACT** — The deprecated registry lists Roots with "Deprecated in `2026-07-28`", migration path "Pass directories or files via tool parameters, resource URIs, or server configuration", and "Earliest removal: First revision released on or after 2027-07-28" ([deprecated.md](https://modelcontextprotocol.io/specification/2026-07-28/deprecated.md)).

### 2.3 Capability flag

**SOURCE FACT** — "Clients that support roots **MUST** declare the `roots` capability in `_meta.io.modelcontextprotocol/clientCapabilities` on each request" ([client/roots.md](https://modelcontextprotocol.io/specification/2026-07-28/client/roots.md)).

### 2.4 Shape

**SOURCE FACT** — "A root definition includes: `uri`: Unique identifier for the root. This **MUST** be a `file://` URI in the current specification. `name`: Optional human-readable name for display purposes." ([client/roots.md](https://modelcontextprotocol.io/specification/2026-07-28/client/roots.md)).

**SOURCE FACT** — The client result is returned "inside `inputResponses` on the retried request" and contains a `roots` array ([client/roots.md](https://modelcontextprotocol.io/specification/2026-07-28/client/roots.md)).

**SOURCE FACT** — Error handling under MRTR: "If an error occurs, the client does not need to replay the initial call with an error message as the server is not waiting for a response with the `InputRequiredResult` pattern." ([client/roots.md](https://modelcontextprotocol.io/specification/2026-07-28/client/roots.md)).

## 3. Sampling

### 3.1 What it is and who initiates

**SOURCE FACT** — "The Model Context Protocol (MCP) provides a standardized way for servers to request LLM sampling ('completions' or 'generations') from language models via clients. This flow allows clients to maintain control over model access, selection, and permissions while enabling servers to leverage AI capabilities—with no server API keys necessary." ([client/sampling.md](https://modelcontextprotocol.io/specification/2026-07-28/client/sampling.md)).

**SOURCE FACT** — "Sampling in MCP allows servers to implement agentic behaviors, by enabling LLM calls to occur *nested* inside other MCP server features." ([client/sampling.md](https://modelcontextprotocol.io/specification/2026-07-28/client/sampling.md)).

**SOURCE FACT** — Under MRTR, "To request a language model generation during the processing of a client request, servers send an `InputRequiredResult` containing a `sampling/createMessage` request" ([client/sampling.md](https://modelcontextprotocol.io/specification/2026-07-28/client/sampling.md)).

### 3.2 Deprecation

**SOURCE FACT** — "**Deprecated**: The Sampling feature is deprecated as of protocol version `2026-07-28` (SEP-2577). Under the feature lifecycle policy, it remains in the specification for at least twelve months after this revision's release before it becomes eligible for removal. New implementations **SHOULD NOT** adopt it; existing implementations **SHOULD** migrate to integrating directly with LLM provider APIs." ([client/sampling.md](https://modelcontextprotocol.io/specification/2026-07-28/client/sampling.md)).

**SOURCE FACT** — The registry lists Sampling with migration path "Integrate directly with LLM provider APIs" and "Earliest removal: First revision released on or after 2027-07-28" ([deprecated.md](https://modelcontextprotocol.io/specification/2026-07-28/deprecated.md)).

### 3.3 Capability flags

**SOURCE FACT** — "Clients that support sampling **MUST** declare the `sampling` capability in `_meta.io.modelcontextprotocol/clientCapabilities` on each request" ([client/sampling.md](https://modelcontextprotocol.io/specification/2026-07-28/client/sampling.md)).

**SOURCE FACT** — Tool use requires a sub-capability: "Clients **MUST** declare support for tool use via the `sampling.tools` capability to receive tool-enabled sampling requests. Servers **MUST NOT** send tool-enabled sampling requests to Clients that have not declared support for tool use via the `sampling.tools` capability." ([client/sampling.md](https://modelcontextprotocol.io/specification/2026-07-28/client/sampling.md)).

**SOURCE FACT** — Context inclusion sub-capability is deprecated: "The `includeContext` parameter values `"thisServer"` and `"allServers"` are deprecated under the feature lifecycle policy (SEP-2596); they will be removed no later than the Sampling feature itself. Servers **SHOULD** avoid using these values (e.g. can just omit `includeContext` since it defaults to `"none"`), and **SHOULD NOT** use them unless the client declares `sampling.context` capability." ([client/sampling.md](https://modelcontextprotocol.io/specification/2026-07-28/client/sampling.md)).

**SOURCE FACT** — The registry lists `includeContext: "thisServer"` / `"allServers"` as "Deprecated in `2025-11-25`", migration "Omit the field or use `"none"`", earliest removal "Follows Sampling (SEP-2577)" ([deprecated.md](https://modelcontextprotocol.io/specification/2026-07-28/deprecated.md)).

### 3.4 Shape and parameters

**SOURCE FACT** — Sampling request parameters include `messages`, `modelPreferences` (with `hints`, `costPriority`, `intelligencePriority`, `speedPriority`), `temperature`, `systemPrompt`, `includeContext`, and `maxTokens` ([client/sampling.md](https://modelcontextprotocol.io/specification/2026-07-28/client/sampling.md)).

**SOURCE FACT** — "The client **MUST** respect the `maxTokens` parameter." and "The client **MAY** modify or ignore `temperature`, `stopSequences` and `metadata`." ([client/sampling.md](https://modelcontextprotocol.io/specification/2026-07-28/client/sampling.md)).

**SOURCE FACT** — Result fields: "`role`: The message role", "`content`: The message content", "`model`: The name of the model that generated the message", and "`stopReason`: The reason why sampling stopped, if known." ([client/sampling.md](https://modelcontextprotocol.io/specification/2026-07-28/client/sampling.md)).

**SOURCE FACT** — Defined stop reasons include `"endTurn"`, `"stopSequence"`, `"maxTokens"`, and `"toolUse"` ([client/sampling.md](https://modelcontextprotocol.io/specification/2026-07-28/client/sampling.md)).

**SOURCE FACT** — Tool choice modes: "`{mode: "auto"}`: Model decides whether to use tools (default)", "`{mode: "required"}`: Model MUST use at least one tool before completing", "`{mode: "none"}`: Model MUST NOT use any tools" ([client/sampling.md](https://modelcontextprotocol.io/specification/2026-07-28/client/sampling.md)).

**SOURCE FACT** — Tool result constraint: "When a user message contains tool results (type: "tool\_result"), it **MUST** contain ONLY tool results. Mixing tool results with other content types (text, image, audio) in the same message is not allowed." ([client/sampling.md](https://modelcontextprotocol.io/specification/2026-07-28/client/sampling.md)).

**SOURCE FACT** — Balance constraint: "every assistant message containing `ToolUseContent` blocks **MUST** be followed by a user message that consists entirely of `ToolResultContent` blocks, with each tool use ... matched by a corresponding tool result ... before any other message." ([client/sampling.md](https://modelcontextprotocol.io/specification/2026-07-28/client/sampling.md)).

## 4. Elicitation

### 4.1 What it is and who initiates

**SOURCE FACT** — "The Model Context Protocol (MCP) provides a standardized way for servers to request additional information from users through the client during interactions. This flow allows clients to maintain control over user interactions and data sharing while enabling servers to gather necessary information dynamically." ([client/elicitation.md](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation.md)).

**SOURCE FACT** — "Elicitation supports two modes: **Form mode**: Servers can request structured data from users with optional JSON schemas to validate responses; **URL mode**: Servers can direct users to external URLs for sensitive interactions that must *not* pass through the MCP client" ([client/elicitation.md](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation.md)).

**SOURCE FACT** — Under MRTR, "Servers **MAY** request information from a user during the processing of a client request, by sending an `InputRequiredResult` containing an `elicitation/create` request." ([client/elicitation.md](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation.md)).

### 4.2 Capability flags

**SOURCE FACT** — "Clients that support elicitation **MUST** declare the `elicitation` capability in `_meta.io.modelcontextprotocol/clientCapabilities` on each request", with `"form": {}` and `"url": {}` sub-objects ([client/elicitation.md](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation.md)).

**SOURCE FACT** — Backward compatibility: "an empty capabilities object is equivalent to declaring support for `form` mode only" and "Clients declaring the `elicitation` capability **MUST** support at least one mode (`form` or `url`)." ([client/elicitation.md](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation.md)).

**SOURCE FACT** — "Servers **MUST NOT** send elicitation requests with modes that are not supported by the client." ([client/elicitation.md](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation.md)).

### 4.3 Form mode shape

**SOURCE FACT** — "All elicitation requests **MUST** include the following parameters: `mode` ... `form`, `url` ... Optional for form mode (defaults to `"form"` if omitted); `message` ... A human-readable message explaining why the interaction is needed." ([client/elicitation.md](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation.md)).

**SOURCE FACT** — "Form mode elicitation requests **MUST** either specify `mode: "form"` or omit the `mode` field, and include these additional parameters: `requestedSchema` ... A JSON Schema defining the structure of the expected response." ([client/elicitation.md](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation.md)).

**SOURCE FACT** — Schema restriction: "To simplify client user experience, form mode elicitation schemas are limited to flat objects with primitive properties only." with primitive types string, number/integer, boolean, and enum ([client/elicitation.md](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation.md)).

**SOURCE FACT** — "Note that complex nested structures, arrays of objects (beyond enums), and other advanced JSON Schema features are intentionally not supported to simplify client user experience." ([client/elicitation.md](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation.md)).

### 4.4 Response actions

**SOURCE FACT** — "Elicitation responses use a three-action model": "**Accept** (`action: "accept"`): User explicitly approved and submitted with data"; "**Decline** (`action: "decline"`): User explicitly declined the request"; "**Cancel** (`action: "cancel"`): User dismissed without making an explicit choice" ([client/elicitation.md](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation.md)).

### 4.5 URL-mode elicitation (SEP-1036)

**SOURCE FACT** — "**New feature:** URL mode elicitation is introduced in the `2025-11-25` version of the MCP specification. Its design and implementation may change in future protocol revisions." ([client/elicitation.md](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation.md)).

**SOURCE FACT** — "URL mode elicitation enables servers to direct users to external URLs for out-of-band interactions that must not pass through the MCP client. This is essential for auth flows, payment processing, and other sensitive or secure operations." ([client/elicitation.md](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation.md)).

**SOURCE FACT** — URL mode parameters: "URL mode elicitation requests **MUST** specify `mode: "url"`, a `message`, and include these additional parameters: `url` ... The URL that the user should navigate to." ([client/elicitation.md](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation.md)).

**SOURCE FACT** — Security boundary: "URL mode elicitation is *not* for authorizing the MCP client's access to the MCP server (that's handled by MCP authorization). Instead, it's used when the MCP server needs to obtain sensitive information or third-party authorization on behalf of the user. The MCP client's bearer token remains unchanged." ([client/elicitation.md](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation.md)).

**SOURCE FACT** — Form-mode prohibition: "Servers **MUST NOT** use form mode elicitation to request sensitive information such as passwords, API keys, access tokens, or payment credentials" and "Servers **MUST** use URL mode for interactions involving such sensitive information" ([client/elicitation.md](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation.md)).

**SOURCE FACT** — Client URL handling: "MUST NOT automatically pre-fetch the URL or any of its metadata."; "MUST NOT open the URL without explicit consent from the user."; "MUST show the full URL to the user for examination before consent."; "MUST open the URL provided by the server in a secure manner that does not enable the client or LLM to inspect the content or user inputs." ([client/elicitation.md](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation.md)).

**SOURCE FACT** — The 2026-07-28 URL-mode flow uses `requestState` rather than `elicitationId`: "When the client retries the original request, the server determines from the echoed `requestState` (or its own stored state) whether the out-of-band interaction has completed, and either returns the final result or responds with another `InputRequiredResult`." ([client/elicitation.md](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation.md)).

**SOURCE FACT** — The 2026-07-28 URL-mode example request contains only `mode`, `url`, and `message` — no `elicitationId` ([client/elicitation.md](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation.md)).

### 4.6 Removal of `notifications/elicitation/complete` and `elicitationId`

**SOURCE FACT** — The 2025-11-25 elicitation page defines `elicitationId`: "URL mode elicitation requests **MUST** specify `mode: "url"`, a `message`, and include these additional parameters: `url` ... `elicitationId` ... A unique identifier for the elicitation." ([2025-11-25/client/elicitation.md](https://modelcontextprotocol.io/specification/2025-11-25/client/elicitation.md)).

**SOURCE FACT** — The 2025-11-25 page defines the completion notification: "Servers **MAY** send a `notifications/elicitation/complete` notification when an out-of-band interaction started by URL mode elicitation is completed." and "**MUST** include the `elicitationId` established in the original `elicitation/create` request." ([2025-11-25/client/elicitation.md](https://modelcontextprotocol.io/specification/2025-11-25/client/elicitation.md)).

**SOURCE FACT** — The 2025-11-25 page also defines `URLElicitationRequiredError` (code `-32042`) carrying a list of elicitations each with an `elicitationId` ([2025-11-25/client/elicitation.md](https://modelcontextprotocol.io/specification/2025-11-25/client/elicitation.md)).

**SOURCE FACT** — The 2026-07-28 elicitation page contains no `notifications/elicitation/complete` section and no `elicitationId` parameter; URL-mode completion is instead inferred from echoed `requestState` ([client/elicitation.md](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation.md)).

**AI INFERENCE** — Comparing the two quoted pages: the 2025-11-25 revision used a server-push `notifications/elicitation/complete` correlated by `elicitationId`; the 2026-07-28 revision removes both and replaces them with the MRTR `requestState` echo. This is consistent with the MRTR statement that "The previous pattern of server-initiated requests is no longer supported." ([basic/patterns/mrtr.md](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr.md)).

**SOURCE FACT** — The 2026-07-28 page still references a `URLElicitationRequiredError` in the URL-mode flow diagram, but the fetched 2026-07-28 elicitation page does not contain a dedicated "URL Elicitation Required Error" section or the `-32042` code (unlike the 2025-11-25 page) ([client/elicitation.md](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation.md)). **UNKNOWN** — Whether `URLElicitationRequiredError`/`-32042` remains normative in 2026-07-28 is not confirmed by the fetched page; it would require the schema page.

### 4.7 Statefulness and security

**SOURCE FACT** — "Elicitations do not require that the server maintain state about users with the multi round-trip requests mechanism." ([client/elicitation.md](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation.md)).

**SOURCE FACT** — "if state is stored, servers implementing elicitation **MUST** securely associate this state with individual users" and "For remote MCP servers, user identification **MUST** be derived from credentials acquired via MCP authorization when possible (e.g. `sub` claim)" ([client/elicitation.md](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation.md)).

**SOURCE FACT** — "Servers **MUST NOT** rely on client-provided user identification without server verification, as this can be forged." ([client/elicitation.md](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation.md)).

**SOURCE FACT** — Phishing mitigation: "the server **MUST** ensure that the user who started the elicitation request ... is the same user who completes the authorization flow." ([client/elicitation.md](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation.md)).

## 5. Deprecation registry (2026-07-28)

**SOURCE FACT** — "This page is the registry of specification features that are currently in the **Deprecated** state under the feature lifecycle and deprecation policy (SEP-2596)." ([deprecated.md](https://modelcontextprotocol.io/specification/2026-07-28/deprecated.md)).

**SOURCE FACT** — "A Deprecated feature remains part of the specification but is scheduled for removal: new implementations **SHOULD NOT** adopt it, and existing implementations **SHOULD** migrate before the feature's earliest removal." ([deprecated.md](https://modelcontextprotocol.io/specification/2026-07-28/deprecated.md)).

**SOURCE FACT** — The registry table lists: Roots (SEP-2577, deprecated `2026-07-28`, migrate to tool parameters/resource URIs/server configuration); Sampling (SEP-2577, deprecated `2026-07-28`, migrate to direct LLM provider APIs); Logging (SEP-2577, deprecated `2026-07-28`, migrate to `stderr`/OpenTelemetry); Dynamic Client Registration (PR #2858, deprecated `2026-07-28`, migrate to Client ID Metadata Documents); `includeContext` values (SEP-2596, deprecated `2025-11-25`); HTTP+SSE transport (SEP-2596, deprecated `2025-03-26`, migrate to Streamable HTTP) ([deprecated.md](https://modelcontextprotocol.io/specification/2026-07-28/deprecated.md)).

**SOURCE FACT** — "Earliest removal: First revision released on or after 2027-07-28" applies to Roots, Sampling, Logging, and Dynamic Client Registration ([deprecated.md](https://modelcontextprotocol.io/specification/2026-07-28/deprecated.md)).

**SOURCE FACT** — "No features have been removed under this policy yet. When a Deprecated feature is removed, its row moves to this section with a link to the changelog entry recording the removal." ([deprecated.md](https://modelcontextprotocol.io/specification/2026-07-28/deprecated.md)).

## 6. Cross-cutting summary

| Feature | Initiator | Capability flag | 2026-07-28 status | Migration path |
| - | - | - | - | - |
| Roots | Server requests via MRTR; client owns data | `roots` | Deprecated (SEP-2577) | Tool parameters, resource URIs, server configuration |
| Sampling | Server requests via MRTR; client executes LLM | `sampling` (+ `sampling.tools`, `sampling.context`) | Deprecated (SEP-2577) | Direct LLM provider APIs |
| Elicitation (form) | Server requests via MRTR | `elicitation.form` | Active | — |
| Elicitation (URL) | Server requests via MRTR | `elicitation.url` | Active (introduced 2025-11-25) | — |
| Logging | Server emits `notifications/message` | `logging` | Deprecated (SEP-2577) | `stderr` / OpenTelemetry |

**AI INFERENCE** — The table is assembled from the quoted capability, deprecation, and MRTR statements above; it introduces no new facts. Note that Roots, Sampling, and Logging are deprecated while Elicitation remains active, even though all four now use the MRTR pattern.

## 7. Retrieval notes

All six requested URLs were retrieved successfully as `.md` endpoints on 2026-10-02. No failed retrievals. Two points are marked **UNKNOWN**: (a) whether `URLElicitationRequiredError`/`-32042` remains normative in 2026-07-28 (the fetched elicitation page lacks the dedicated section present in 2025-11-25); (b) the exact tool annotation hint keys, which are outside this file's scope.
