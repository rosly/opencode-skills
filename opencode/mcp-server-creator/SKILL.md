---
name: MCP Server Creator
description: This skill should be used when creating, extending, hardening, deploying, or publishing a Model Context Protocol (MCP) server. It covers choosing an SDK or framework, designing tools/resources/prompts, testing with the Inspector and in-memory clients, securing the server, deploying over stdio or Streamable HTTP, and publishing to the MCP Registry.
metadata:
  version: "1.0"
---

# MCP Server Creator

Build, test, secure, deploy, and publish MCP servers. This skill is language-agnostic: it presents
the options and lets the user choose, then guides the implementation.

The bundled knowledge base is anchored to MCP protocol revision **2026-07-28** and was researched on
**2026-10-03**. Before relying on version-specific behavior, confirm the current revision and the
target SDK's supported protocol versions.

## When to use

Use this skill when the user wants to:

- Create a new MCP server from scratch.
- Add or change tools, resources, or prompts on an existing server.
- Make an MCP server production-ready (testing, security, observability).
- Deploy an MCP server locally or remotely.
- Publish an MCP server to the MCP Registry or a marketplace.

## Non-negotiable rules

Apply these regardless of language or framework:

1. **Target the current revision.** As of this knowledge base that is 2026-07-28. Verify the SDK
   actually supports it; adoption is uneven.
2. **The protocol is stateless.** Do not rely on connection or process state. Carry cross-request
   state in explicit handles or integrity-protected `requestState`.
3. **Implement `server/discover`.** It is mandatory for servers.
4. **Never initiate server-to-client requests.** Use Multi Round-Trip Requests (MRTR) on
   `prompts/get`, `resources/read`, and `tools/call`.
5. **Keep stdout clean on stdio.** Never write logs or anything else to stdout; use stderr.
6. **Never accept or pass through tokens not issued for this server.** Validate audience.
7. **Do not build on deprecated features:** Roots, Sampling, Logging, HTTP+SSE, and the
   `includeContext` values `"thisServer"`/`"allServers"`.

## Workflow

### Phase 0 — Clarify requirements

Establish before writing code:

- What capabilities are needed: tools (model actions), resources (application context), prompts
  (user workflows)?
- Local (stdio) or remote (Streamable HTTP)? Single-user or multi-user?
- Does it need authorization? Which identity provider?
- Any language, runtime, or hosting constraints?
- Does it need long-running work (Tasks extension) or interactive input (elicitation)?

### Phase 1 — Choose the stack

Present the SDK tier and framework options and let the user decide. Do not silently pick a language.

- SDK tiers and per-language server APIs: `references/development/01-sdks-languages.md`
- Frameworks and what they add: `references/development/02-frameworks-libraries.md`
- Tier definitions and conformance requirements: `references/protocol/09-ecosystem-sdk-registry.md`

### Phase 2 — Scaffold

Follow the chosen SDK or framework's quickstart. Keep a clean layout (server instance, tool
definitions, tests). See `references/development/04-development-workflow-tooling.md`.

### Phase 3 — Design the primitives

Decide the primitive surface, then design schemas, names, errors, and caching before implementing.

- Primitive selection, naming, schemas, errors, annotations, state, caching, MRTR:
  `references/development/03-server-design-patterns.md`
- Wire-level details: `references/protocol/04-server-primitives.md`

### Phase 4 — Implement

Implement handlers with strict input validation. Return tool execution errors (`isError: true`) for
argument and business failures so the model can self-correct; reserve JSON-RPC errors for protocol
failures. Attach caching hints on complete list/read/discover results.

### Phase 5 — Test

Test at three levels: unit tests, in-memory client/server integration tests, and Inspector or
end-to-end checks. Run the Inspector CLI in CI with a pinned version.

- Test pyramid, in-memory transports, Inspector CLI, conformance:
  `references/development/05-testing-conformance-ci.md`
- Inspector and debugging: `references/development/04-development-workflow-tooling.md`

### Phase 6 — Secure

Apply the threat model: audience-bound tokens, no token passthrough, strict input validation, least
privilege, sandboxing, no secrets in logs, and supply-chain scanning.

- Full security guidance: `references/development/07-security-engineering.md`
- Protocol authorization model: `references/protocol/06-authorization-security.md`

### Phase 7 — Deploy

Choose stdio for local single-user servers and Streamable HTTP for remote or multi-user servers.
Statelessness makes containers and serverless practical.

- Deployment and hosting: `references/development/06-deployment-hosting.md`
- Transport rules: `references/protocol/03-base-protocol-transports.md`

### Phase 8 — Publish

Package first, then publish metadata to the Registry. Match the ownership proof to the package type
and use immutable versions.

- Publishing and distribution: `references/development/09-publishing-distribution.md`
- Registry and ecosystem: `references/protocol/09-ecosystem-sdk-registry.md`

## Reference map

Load only what the current phase needs. The two summary reports are the entry points; the topic
files hold the full evidence and quotations.

| Need | File |
|------|------|
| Protocol overview and architecture | `references/mcp-protocol.md` §1, `references/protocol/01-overview-architecture.md` |
| Revision history and versioning | `references/mcp-protocol.md` §2, `references/protocol/02-protocol-history.md` |
| Base protocol, `_meta`, MRTR, transports | `references/mcp-protocol.md` §3, `references/protocol/03-base-protocol-transports.md` |
| Tools, resources, prompts, caching | `references/mcp-protocol.md` §4, `references/protocol/04-server-primitives.md` |
| Roots, Sampling, Elicitation | `references/mcp-protocol.md` §5, `references/protocol/05-client-features.md` |
| Authorization and security model | `references/mcp-protocol.md` §6, `references/protocol/06-authorization-security.md` |
| Extensions (Apps, Tasks, Skills, auth) | `references/mcp-protocol.md` §7, `references/protocol/07-extensions.md` |
| Protocol best practices | `references/mcp-protocol.md` §8, `references/protocol/08-server-best-practices.md` |
| SDKs, Registry, examples | `references/mcp-protocol.md` §9, `references/protocol/09-ecosystem-sdk-registry.md` |
| Governance, SEPs, deprecations | `references/mcp-protocol.md` §10, `references/protocol/10-governance-seps-deprecations.md` |
| Development overview | `references/mcp-development.md` |
| SDKs and languages | `references/development/01-sdks-languages.md` |
| Frameworks and libraries | `references/development/02-frameworks-libraries.md` |
| Server design patterns | `references/development/03-server-design-patterns.md` |
| Workflow and tooling | `references/development/04-development-workflow-tooling.md` |
| Testing, conformance, CI | `references/development/05-testing-conformance-ci.md` |
| Deployment and hosting | `references/development/06-deployment-hosting.md` |
| Security engineering | `references/development/07-security-engineering.md` |
| Observability and performance | `references/development/08-observability-performance.md` |
| Publishing and distribution | `references/development/09-publishing-distribution.md` |

The reports are long. Use grep to jump to a topic, for example:

- `grep -n "server/discover" references/mcp-protocol.md`
- `grep -n "token passthrough" references/development/07-security-engineering.md`
- `grep -n "Streamable HTTP" references/development/06-deployment-hosting.md`
- `grep -n "ttlMs\|cacheScope" references/protocol/04-server-primitives.md`

## Common pitfalls

- **Tool-name length conflict.** The current tools reference says 1–128 characters; SEP-986 says
  1–64. Use the safe intersection: 1–64 characters, no slash.
- **stdout corruption.** Any non-protocol write to stdout on a stdio server breaks the connection.
- **Token passthrough.** Accepting or forwarding tokens not issued for the server is forbidden.
- **State handle as authentication.** Possession of a handle must never authenticate a request.
- **Deprecated features.** Roots, Sampling, Logging, HTTP+SSE, and the `includeContext` values are
  deprecated; do not build new work on them.
- **Tool-count cost.** Loading every tool definition upfront is expensive; keep the always-loaded
  surface small and support progressive discovery.
- **Registry is preview.** It is metadata-only, permissively moderated, and not a security gate.
