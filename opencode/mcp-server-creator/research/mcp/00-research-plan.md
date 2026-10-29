# MCP (LLM Agent) Servers — Research Plan

Date of scan: 2026-10-02
Primary sources: official MCP documentation (modelcontextprotocol.io), official specification,
official GitHub repository/releases, SEP registry.

## Initial-scan findings that shape the plan

- The **current** protocol revision is **2026-07-28** (stable, released 28 Jul 2026); the previous
  stable was **2025-11-25**; earlier revisions: 2025-06-18, 2025-03-26, 2024-11-05, 2024-10-07.
- The 2026-07-28 revision is a **large architectural change**: stateless protocol, removal of the
  `initialize` handshake, `server/discover`, `subscriptions/listen`, Multi Round-Trip Requests
  (MRTR) replacing server-initiated requests, deprecation of Roots/Sampling/Logging, official
  extensions, JSON Schema 2020-12, error-code allocation policy.
- Most third-party material online still describes the 2025-06-18 model, so official sources are
  mandatory and version labels must be attached to every claim.

## Detailed research topics (each stored in its own temp file)

| # | File | Topic | Purpose for an MCP-server creator |
|---|------|-------|-----------------------------------|
| 1 | `01-overview-architecture.md` | What MCP is, design principles, host/client/server, current vs legacy architecture | Mental model and boundaries |
| 2 | `02-protocol-history.md` | Revision timeline + per-revision changelog (2024-10-07 → 2026-07-28) | Version targeting and migration |
| 3 | `03-base-protocol-transports.md` | JSON-RPC 2.0 base, `_meta`, statelessness, lifecycle, error codes, MRTR, stdio + Streamable HTTP (+ deprecated SSE) | Wire-level server implementation |
| 4 | `04-server-primitives.md` | Tools, Resources, Prompts, `server/discover`, completion, pagination, caching, logging | The server surface you expose |
| 5 | `05-client-features.md` | Roots, Sampling, Elicitation (all now deprecated / routed through MRTR) | Server→client behavior |
| 6 | `06-authorization-security.md` | OAuth 2.1 framework, resource-server role, PRM/RFC 9728, resource indicators/RFC 8707, client registration + CIMD, security best practices/attacks | Protecting remote servers |
| 7 | `07-extensions.md` | MCP Apps, Tasks, Skills, auth extensions, extension support model | Optional capability surface |
| 8 | `08-server-best-practices.md` | Build-a-server guidance, tool design/naming, client best practices, debugging, Inspector | How to build well |
| 9 | `09-ecosystem-sdk-registry.md` | SDKs + tiering, official Registry, publishing, examples | Distribution |
| 10 | `10-governance-seps-deprecations.md` | Governance, SEP process, feature lifecycle, deprecated features registry | Change tracking |

## Method

1. Fetch official `.md` endpoints (documentation and specification) to obtain exact text.
2. Each topic file records **SOURCE FACT / SOURCE CLAIM / AI INFERENCE / UNKNOWN** notation and
   carries exact quotations with inline descriptive Markdown links next to the claim they support.
3. Failed retrievals are recorded as results, not as absence of the feature.
4. Final deliverable: an extensive Markdown report with URLs, assembled from the topic files,
   with the separation between source evidence and model reasoning preserved.

## Assumed scope (stated, not silently chosen)

Focus is on **MCP servers for LLM agents**, with protocol history, best practices and security as
primary research axes, as requested. Governance/SEP detail is included only insofar as it explains
protocol change. This assumption can be narrowed or widened by the user.
