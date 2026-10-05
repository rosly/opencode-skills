# 01 — MCP Overview and Architecture

Research file for an MCP-server-creation report.
- Scan date: **2026-10-02**
- Current protocol revision: **2026-07-28**
- Status of this document: primary-source extracts + labelled synthesis. Every externally sourced statement carries an exact, short quotation and an inline descriptive link to the source URL on the same line.

## Notation key (mandatory)

- **SOURCE FACT** — official specification/docs/code; quoted exactly.
- **SOURCE CLAIM** — lower-tier pages, marketing, blogs; quoted exactly, with rank noted.
- **AI INFERENCE** — synthesis by this agent, naming the quoted facts it follows from.
- **PLAUSIBLE, NOT VERIFIED** — possible but not established by retrieved evidence.
- **UNKNOWN** — cannot be decided from the available evidence.

Where this file reports a failed retrieval, that is recorded as a *result* (evidence about tooling), not as proof of absence.

---

## 1. Definition and purpose

**SOURCE FACT** — MCP is defined as a standard: "MCP (Model Context Protocol) is an open-source standard for connecting AI applications to external systems." — [What is the Model Context Protocol (MCP)?](https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro.md)

**SOURCE FACT** — its intended subject matter spans "data sources (e.g. local files, databases), tools (e.g. search engines, calculators) and workflows (e.g. specialized prompts)—enabling them to access key information and perform tasks." — [What is the Model Context Protocol (MCP)?](https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro.md)

**SOURCE FACT** — the protocol's own analogy is "Think of MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect electronic devices, MCP provides a standardized way to connect AI applications to external systems." — [What is the Model Context Protocol (MCP)?](https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro.md)

**SOURCE FACT** — the protocol has an explicit scope boundary: "MCP focuses solely on the protocol for context exchange—it does not dictate how AI applications use LLMs or manage the provided context." — [Architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture.md)

**SOURCE FACT** — the specification-level architecture page repeats the framing: "Built on JSON-RPC, MCP provides a protocol focused on context exchange and sampling coordination between clients and servers." — [Specification — Architecture](https://modelcontextprotocol.io/specification/2026-07-28/architecture/index.md)

**AI INFERENCE** — the definition ("connecting AI applications to external systems"), the USB-C analogy, and the "context exchange" scope statement together imply that a *server's* job is to expose external capabilities/data; it does not own the conversation or the model. This is reinforced by design principle 3 below ("Servers should not be able to read the whole conversation").

### 1.1 Why it exists (stated benefits)

**SOURCE FACT** — the documentation states developer benefits: "Developers: MCP reduces development time and complexity when building, or integrating with, an AI application or agent." — [What is the Model Context Protocol (MCP)?](https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro.md)

**SOURCE FACT** — for applications: "AI applications or agents: MCP gives them access to an ecosystem of data sources, tools and apps, which enhances their capabilities and improves the end-user experience." — [What is the Model Context Protocol (MCP)?](https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro.md)

**SOURCE FACT** — for end-users: "End-users: MCP results in more capable AI applications or agents that can access user data and take actions on the user's behalf when necessary." — [What is the Model Context Protocol (MCP)?](https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro.md)

**SOURCE FACT** — MCP is positioned as broadly supported: "MCP is an open protocol supported across a wide range of clients and servers." with named examples "Claude ... ChatGPT ... Visual Studio Code, Cursor, MCPJam" — [What is the Model Context Protocol (MCP)?](https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro.md)

> Note: the broad-client-support sentence is official documentation (SOURCE FACT) but functions partly as an ecosystem/marketing claim. Treated as SOURCE FACT per source tier; the specific third-party integrations are not independently verified in this file.

---

## 2. Core design principles

Two distinct lists exist: the *architecture* design principles and the *community* design principles. They are reported separately below.

### 2.1 Architecture design principles (spec-level)

**SOURCE FACT** — "MCP is built on several key design principles that inform its architecture and implementation" — [Specification — Architecture](https://modelcontextprotocol.io/specification/2026-07-28/architecture/index.md). The four principles are quoted exactly:

1. **SOURCE FACT** — "**Servers should be extremely easy to build**", with sub-points including "Host applications handle complex orchestration responsibilities" and "Servers focus on specific, well-defined capabilities" — [Specification — Architecture](https://modelcontextprotocol.io/specification/2026-07-28/architecture/index.md)
2. **SOURCE FACT** — "**Servers should be highly composable**", with sub-points including "Each server provides focused functionality in isolation" and "Multiple servers can be combined seamlessly" — [Specification — Architecture](https://modelcontextprotocol.io/specification/2026-07-28/architecture/index.md)
3. **SOURCE FACT** — "**Servers should not be able to read the whole conversation, nor "see into" other servers**", with sub-points including "Full conversation history stays with the host" and "Each server maintains isolation" — [Specification — Architecture](https://modelcontextprotocol.io/specification/2026-07-28/architecture/index.md)
4. **SOURCE FACT** — "**Features can be added to servers and clients progressively**", with sub-points including "Core protocol provides minimal required functionality" and "Backwards compatibility is maintained" — [Specification — Architecture](https://modelcontextprotocol.io/specification/2026-07-28/architecture/index.md)

**AI INFERENCE** — following from principle 3 ("Full conversation history stays with the host") and the scope statement that MCP "does not dictate how AI applications use LLMs", a server author should not assume access to the transcript; only the arguments/context passed per request are available. This motivates the statelessness of the 2026-07-28 revision described in §5.

### 2.2 Community design principles

**SOURCE FACT** — the community page frames these as evaluative guidance: "These principles guide how we evaluate protocol proposals, weigh tradeoffs, and evolve MCP." — [Design Principles](https://modelcontextprotocol.io/community/design-principles.md)

**SOURCE FACT** — eight principles are stated with their exact headings and lead sentences:

1. **Convergence over choice** — "There should be one way to solve a problem in MCP. Rather than supporting multiple approaches that fragment the ecosystem, we choose a single well-designed path — accepting harder decisions upfront to deliver a more cohesive protocol." — [Design Principles](https://modelcontextprotocol.io/community/design-principles.md)
2. **Composability over specificity** — "MCP provides foundational primitives: resources, tools, and prompts. We don't add protocol features for use cases that can be constructed from these existing building blocks." — [Design Principles](https://modelcontextprotocol.io/community/design-principles.md)
3. **Interoperability over optimization** — "We favor features that degrade gracefully over those that only work when every participant is equally capable. Capability negotiation makes this concrete: participants declare what they support, and the protocol adapts rather than assumes." — [Design Principles](https://modelcontextprotocol.io/community/design-principles.md)
4. **Stability over velocity** — "Adding to a protocol as widely adopted as MCP is easy. Removing from it is nearly impossible. Every addition is a permanent commitment and a cost for client implementers to support." — [Design Principles](https://modelcontextprotocol.io/community/design-principles.md)
5. **Capability over compensation** — "Models improve faster than protocols evolve. We avoid adding permanent structure to work around limitations that are likely temporary — the limitation fades, but the complexity remains." — [Design Principles](https://modelcontextprotocol.io/community/design-principles.md)
6. **Demonstration over deliberation** — "MCP values working implementations over theoretical debates. When evaluating proposals, we prioritize evidence from real usage over hypothetical arguments." — [Design Principles](https://modelcontextprotocol.io/community/design-principles.md)
7. **Pragmatism over purity** — "MCP makes practical tradeoffs in service of adoption and usability. We don't pursue theoretical elegance at the cost of real-world utility." — [Design Principles](https://modelcontextprotocol.io/community/design-principles.md)
8. **Standardization over innovation** — "MCP standardizes patterns that have already proven valuable. We look for conventions that work across multiple implementations and codify them, rather than inventing new paradigms and hoping they'll be adopted." — [Design Principles](https://modelcontextprotocol.io/community/design-principles.md)

**AI INFERENCE** — the "Stability over velocity" and "Capability over compensation" principles explain the 2026-07-28 deprecation of long-standing features (Roots/Sampling/Logging; see §5 and the changelog file): the project prefers to mark features deprecated with a long migration window rather than remove them abruptly.

---

## 3. Participants: host, client, server

**SOURCE FACT** — the architecture overview defines the participants: "MCP follows a client-server architecture where an MCP host — an AI application ... — establishes connections to one or more MCP servers. The MCP host accomplishes this by creating one MCP client for each MCP server. Each MCP client maintains a dedicated connection with its corresponding MCP server." — [Architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture.md)

**SOURCE FACT** — role definitions, quoted exactly:
- "**MCP Host**: The AI application that coordinates and manages one or multiple MCP clients"
- "**MCP Client**: A component that maintains a connection to an MCP server and obtains context from an MCP server for the MCP host to use"
- "**MCP Server**: A program that provides context to MCP clients"
— [Architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture.md)

**SOURCE FACT** — the spec architecture page calls this a "client-host-server architecture where each host can run multiple client instances." — [Specification — Architecture](https://modelcontextprotocol.io/specification/2026-07-28/architecture/index.md)

### 3.1 Host responsibilities

**SOURCE FACT** — the host "acts as the container and coordinator" and is listed as: "Creates and manages multiple client instances", "Controls client connection permissions and lifecycle", "Enforces security policies and consent requirements", "Handles user authorization decisions", "Coordinates AI/LLM integration and sampling", "Manages context aggregation across clients" — [Specification — Architecture](https://modelcontextprotocol.io/specification/2026-07-28/architecture/index.md)

### 3.2 Client responsibilities

**SOURCE FACT** — "Each client is created by the host and communicates with exactly one server", with the listed duties "Attaches protocol version and capabilities to every request", "Routes protocol messages bidirectionally", "Manages subscriptions and notifications", "Maintains security boundaries between servers" — [Specification — Architecture](https://modelcontextprotocol.io/specification/2026-07-28/architecture/index.md)

**SOURCE FACT** — the docs draw the host/client distinction explicitly: "the *host* is the application users interact with, while *clients* are the protocol-level components that enable server connections." — [Understanding MCP clients](https://modelcontextprotocol.io/docs/2026-07-28/learn/client-concepts.md)

### 3.3 Server responsibilities

**SOURCE FACT** — servers "provide specialized context and capabilities": "Expose resources, tools and prompts via MCP primitives", "Operate independently with focused responsibilities", "Request client input (sampling, elicitation, roots) via `InputRequiredResult` within a reply", "Must respect security constraints", "Can be local processes or remote services" — [Specification — Architecture](https://modelcontextprotocol.io/specification/2026-07-28/architecture/index.md)

**SOURCE FACT** — location is not part of the definition: "**MCP server** refers to the program that serves context data, regardless of where it runs. MCP servers can execute locally or remotely." — [Architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture.md)

**SOURCE FACT** — connection cardinality differs by transport: "Local MCP servers that use the STDIO transport typically serve a single MCP client, whereas remote MCP servers that use the Streamable HTTP transport will typically serve many MCP clients." — [Architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture.md)

**AI INFERENCE** — Combined with the deprecated-feature notes (Sampling/Roots listed as deprecated in 2026-07-28; see §6), the server-side pattern of "request client input via `InputRequiredResult`" is the current (MRTR-based) replacement for the old server-initiated requests. This follows from the architecture page's own wording and from the changelog's MRTR item.

---

## 4. Architecture layers: data layer vs transport layer

**SOURCE FACT** — "MCP consists of two layers: **Data layer**: Defines the JSON-RPC based protocol for client-server communication, including capability and version discovery, and core primitives, such as tools, resources, prompts and notifications. **Transport layer**: Defines the communication mechanisms and channels that enable data exchange between clients and servers, including transport-specific connection establishment, message framing, and authorization." — [Architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture.md)

**SOURCE FACT** — "Conceptually the data layer is the inner layer, while the transport layer is the outer layer." — [Architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture.md)

**SOURCE FACT** — data layer mechanics: "MCP uses [JSON-RPC 2.0] as its underlying RPC protocol. Client and servers send requests to each other and respond accordingly. Notifications can be used when no response is required." — [Architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture.md)

**SOURCE FACT** — the data layer's discovery component: "**Discovery**: Lets clients query a server's supported protocol versions, capabilities, and identity through the `server/discover` request" — [Architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture.md)

### 4.1 Transport layer

**SOURCE FACT** — "MCP supports two transport mechanisms:" with "**Stdio transport**: Uses standard input/output streams for direct process communication between local processes on the same machine, providing optimal performance with no network overhead." and "**Streamable HTTP transport**: Uses HTTP POST for client-to-server messages with optional Server-Sent Events for streaming capabilities." — [Architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture.md)

**SOURCE FACT** — auth guidance at the transport layer: "MCP recommends using OAuth to obtain authentication tokens." — [Architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture.md)

**SOURCE FACT** — "The transport layer abstracts communication details from the protocol layer, enabling the same JSON-RPC 2.0 message format across all transport mechanisms." — [Architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture.md)

**AI INFERENCE** — because the same JSON-RPC 2.0 data layer is used across stdio and Streamable HTTP, a server's tool/resource/prompt handler logic is transport-independent; only connection establishment and framing differ. This follows from the two quotes immediately above.

---

## 5. Capabilities negotiation: current (2026-07-28) vs legacy

### 5.1 Current (2026-07-28): stateless, per-request metadata + `server/discover`

**SOURCE FACT** — "MCP is a [stateless protocol]. Every request carries the protocol version and the capabilities relevant to that request in its `_meta` field, so the server can process each request on its own. Clients should also identify themselves in the same field unless configured not to. Servers advertise their supported versions and capabilities through the mandatory `server/discover` request, which clients may send before any other request." — [Architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture.md)

The inline tooltip is itself exact text: "Every request contains all the information needed to process it, so servers infer nothing from previous requests" — [Architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture.md)

**SOURCE FACT** — "MCP is a stateless protocol: every request is self-contained and carries its own protocol version and capabilities." — [Specification — Architecture](https://modelcontextprotocol.io/specification/2026-07-28/architecture/index.md)

**SOURCE FACT** — current capability-negotiation mechanics: "The Model Context Protocol uses a capability-based negotiation system where clients and servers declare their supported features on each request. Clients include their capabilities in `_meta.io.modelcontextprotocol/clientCapabilities` on every request. Servers advertise their capabilities in response to `server/discover` ... which clients may call before any other request for up-front capability discovery." — [Specification — Architecture](https://modelcontextprotocol.io/specification/2026-07-28/architecture/index.md)

**SOURCE FACT** — governing rule: "Both parties must respect declared capabilities throughout the interaction" — [Specification — Architecture](https://modelcontextprotocol.io/specification/2026-07-28/architecture/index.md)

**SOURCE FACT** — concrete unlocking examples: "Implemented server features must be advertised in the server's capabilities"; "Receiving resource update notifications requires opening a `subscriptions/listen` stream with the desired resource URIs"; "[Tool] invocation requires the server to declare tool capabilities" — [Specification — Architecture](https://modelcontextprotocol.io/specification/2026-07-28/architecture/index.md)

**SOURCE FACT** — the discovery round-trip is illustrated with an example request carrying `_meta` `"io.modelcontextprotocol/protocolVersion": "2026-07-28"`, `"io.modelcontextprotocol/clientInfo"`, and `"io.modelcontextprotocol/clientCapabilities"`, and a response result containing `"supportedVersions"`, `"capabilities"`, server `_meta`, `"ttlMs"`, and `"cacheScope"`. — [Architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture.md)

**SOURCE FACT** — discovery is optional for clients but mandatory for servers: "Calling `server/discover` is optional." — [Architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture.md); and "Servers **MUST** implement `server/discover`." — [Specification — Versioning and Compatibility](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md)

**SOURCE FACT** — version-conflict handling: "If a server does not support the requested version, it rejects the request with an `UnsupportedProtocolVersionError` listing the versions it does support, and the client retries with a mutually supported version." — [Architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture.md)

> Cross-reference: the precise wire-level negotiation rules (`_meta` key, `MCP-Protocol-Version` header, error code `-32022`, compatibility matrix) are covered in `02-protocol-history.md`.

### 5.2 Legacy (2025-11-25 and earlier): `initialize` handshake

**SOURCE FACT** — the spec's own terminology: "**Legacy**: protocol versions that establish a session with an `initialize` handshake (`2025-11-25` and earlier)." — [Specification — Versioning and Compatibility](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md)

**SOURCE FACT** — "A server that wishes to support both legacy clients (which expect an `initialize` handshake) and modern clients (which use per-request metadata) MAY implement both behaviors." — [Specification — Versioning and Compatibility](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning.md)

**SOURCE FACT** — the 2026-07-28 changelog describes the removal as a headline change: "Make MCP stateless: remove the `initialize`/`notifications/initialized` handshake. Every request now carries its protocol version and client capabilities in `_meta` (`io.modelcontextprotocol/protocolVersion`, `io.modelcontextprotocol/clientCapabilities`)." — [Key Changes (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/changelog.md)

**AI INFERENCE** — "current vs legacy" is therefore a data-layer/lifecycle distinction (per-request metadata vs session handshake), not a transport distinction: both eras run over the same stdio and Streamable HTTP transports, and a "dual-era" implementation can serve both. This follows from the terminology quotes above plus §4's statement that the data layer is independent of transport.

### 5.3 Design implication for capability negotiation

**SOURCE FACT** — the community principle states the intent directly: "Capability negotiation makes this concrete: participants declare what they support, and the protocol adapts rather than assumes." — [Design Principles](https://modelcontextprotocol.io/community/design-principles.md)

**AI INFERENCE** — because the server advertises capabilities only in `server/discover`, a client that skips discovery may call a method the server does not support; the design expects clients either to discover first or to handle errors. This follows from "Calling `server/discover` is optional." and the capability-unlocking examples.

---

## 6. What makes a "server"

**SOURCE FACT** — "MCP servers are programs that expose specific capabilities to AI applications through standardized protocol interfaces." — [Understanding MCP servers](https://modelcontextprotocol.io/docs/2026-07-28/learn/server-concepts.md)

**SOURCE FACT** — the server surface is built from three primitives: "**Tools**: Functions that your LLM can actively call ...", "**Resources**: Passive data sources that provide read-only access to information for context ...", "**Prompts**: Pre-built instruction templates ..." — [Understanding MCP servers](https://modelcontextprotocol.io/docs/2026-07-28/learn/server-concepts.md)

**SOURCE FACT** — control ownership per primitive, quoted from the table's "Who controls it" column: Tools are controlled by the "Model", Resources by the "Application", Prompts by the "User". — [Understanding MCP servers](https://modelcontextprotocol.io/docs/2026-07-28/learn/server-concepts.md)

**SOURCE FACT** — the core server primitives are also stated in the architecture overview: "MCP defines three core primitives that *servers* can expose: **Tools** ... **Resources** ... **Prompts** ..." — [Architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture.md)

**SOURCE FACT** — protocol operations for the primitives: `tools/list` "Discover available tools" and `tools/call` "Execute a specific tool"; `resources/list`, `resources/templates/list`, `resources/read`, and `subscriptions/listen`; `prompts/list` and `prompts/get`. — [Understanding MCP servers](https://modelcontextprotocol.io/docs/2026-07-28/learn/server-concepts.md)

**SOURCE FACT** — change notifications are opt-in and stream-based: "To watch specific resources for changes, a client sends a `subscriptions/listen` request with the resource URIs listed in the `resourceSubscriptions` filter. The server delivers `notifications/resources/updated` on the resulting stream whenever a watched resource changes." — [Understanding MCP servers](https://modelcontextprotocol.io/docs/2026-07-28/learn/server-concepts.md)

**SOURCE FACT** — the protocol overview adds real-time notifications: "Change notifications are opt-in: the client opens a long-lived `subscriptions/listen` stream naming the notification types it wants to receive, and the server delivers matching notifications on that stream." — [Architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture.md)

### 6.1 Client-side primitives that servers can rely on

**SOURCE FACT** — "MCP also defines primitives that *clients* can expose." with the active client primitive "**Elicitation**: Allows servers to request additional information from users ... Servers request user input with the `elicitation/create` method." — [Architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture.md)

**SOURCE FACT** — elicitation is delivered via MRTR: "Elicitation requests are delivered through the Multi Round-Trip Requests pattern" — [Architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture.md)

**SOURCE FACT** — deprecated client primitives: "**Deprecated**: The following client primitives are deprecated as of protocol version `2026-07-28`." followed by "**Sampling** ... New implementations should integrate directly with LLM provider APIs." and "**Logging** ... New implementations should log to `stderr` (stdio transport) or use OpenTelemetry." — [Architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture.md)

**SOURCE FACT** — roots deprecation: "Roots allow clients to specify which directories servers should focus on ... Roots are deprecated as of protocol version `2026-07-28`." — [Understanding MCP clients](https://modelcontextprotocol.io/docs/2026-07-28/learn/client-concepts.md)

**SOURCE FACT** — permission boundary on roots: "While roots communicate intended boundaries, they do not enforce security restrictions. Actual security must be enforced at the operating system level, via file permissions and/or sandboxing." — [Understanding MCP clients](https://modelcontextprotocol.io/docs/2026-07-28/learn/client-concepts.md)

**SOURCE FACT** — elicitation privacy rule relevant to server authors: "Servers must not use form mode to request sensitive information such as passwords, API keys, access tokens, or payment credentials." — [Understanding MCP clients](https://modelcontextprotocol.io/docs/2026-07-28/learn/client-concepts.md)

**AI INFERENCE** — a minimal "server" in 2026-07-28 therefore = a program that (a) speaks JSON-RPC 2.0 over stdio or Streamable HTTP, (b) implements `server/discover`, (c) declares capabilities, and (d) implements at least one of tools/resources/prompts. The "must implement `server/discover`" fact and the primitive definitions support this; the choice of which primitive to implement is the author's.

---

## 7. Retrieval log for this file

| URL | Result |
|---|---|
| https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro.md | Retrieved |
| https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture.md | Retrieved |
| https://modelcontextprotocol.io/docs/2026-07-28/learn/server-concepts.md | Retrieved |
| https://modelcontextprotocol.io/docs/2026-07-28/learn/client-concepts.md | Retrieved |
| https://modelcontextprotocol.io/specification/2026-07-28/architecture/index.md | Retrieved |
| https://modelcontextprotocol.io/community/design-principles.md | Retrieved |

All required URLs for this file were retrieved successfully on 2026-10-02. No failed retrievals.

---

## 8. Open / undecided items (not resolved here)

- The exact per-revision status labels (Draft/Current/Final) for each past revision are not enumerated on the fetched versioning page; see `02-protocol-history.md`.
- MCP Apps under `/extensions/` referenced by the fetched pages were not fetched for this file (out of scope of the listed URLs). **UNKNOWN** in this file.
