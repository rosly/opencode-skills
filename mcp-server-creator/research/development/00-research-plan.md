# MCP Server Development — Research Plan (Round 2)

Date: 2026-10-03
Current MCP protocol revision: 2026-07-28
Focus: how to write MCP servers professionally and efficiently — libraries, frameworks,
best practices, rapid deployment, security.

Round 1 (protocol knowledge) lives in `research/mcp/`. This round lives in `research/development/`.
Final report: `research/development/MCP-DEVELOPMENT.md`.

## Initial-scan signals

- Python: FastMCP is the dominant framework (v3.x stable, v4 beta), maintained by Prefect; FastMCP 1.0
  was folded into the official Python SDK. It handles schema generation, validation, transport, auth,
  and protocol-era negotiation.
- TypeScript: official `@modelcontextprotocol/sdk` plus community frameworks such as MCP-Framework.
- .NET: `ModelContextProtocol.AspNetCore` for remote Streamable HTTP.
- Deployment: Streamable HTTP + statelessness (2026-07-28) makes serverless (AWS Lambda, Cloudflare
  Workers, Azure Container Apps, Cloud Run) and containers/Kubernetes viable; SSE is deprecated.
- Testing: MCP Inspector (Web/CLI/TUI) is the reference tool; CLI enables CI; in-memory client/server
  tests are the recommended automated layer.
- Security: official security best practices plus ecosystem guidance on tool poisoning, input
  validation, sandboxing, and supply chain.

## Topic groups and files

| # | File | Group | Core question |
|---|------|-------|---------------|
| 1 | `01-sdks-languages.md` | SDKs & languages | Which official SDK, and how do you build a server idiomatically in each? |
| 2 | `02-frameworks-libraries.md` | Frameworks & libraries | What frameworks exist, what do they add, and how do they compare? |
| 3 | `03-server-design-patterns.md` | Design patterns | How should tools/resources/prompts, schemas, state, errors, and caching be designed? |
| 4 | `04-development-workflow-tooling.md` | Workflow & tooling | Scaffolding, project layout, local dev, Inspector, debugging. |
| 5 | `05-testing-conformance-ci.md` | Testing & CI | Unit/integration/in-memory tests, conformance, CI gates. |
| 6 | `06-deployment-hosting.md` | Deployment & hosting | stdio packaging, containers, serverless, Kubernetes, gateways, scaling. |
| 7 | `07-security-engineering.md` | Security engineering | Auth implementation, validation, sandboxing, supply chain, tool poisoning. |
| 8 | `08-observability-performance.md` | Observability & performance | OTel, logging, metrics, caching, context/token cost, latency. |
| 9 | `09-publishing-distribution.md` | Publishing & distribution | Registry, package types, versioning, automation, marketplaces. |

## Method

- Prefer official documentation and source repositories; use web search to discover ecosystem
  projects, then fetch their actual docs/repos.
- Each topic file records exact short quotations with inline descriptive links, plus a retrieval log.
- Working files may use evidence notation; the final report will not use tags and will carry one
  consolidated resource list.
- Failed retrievals are recorded as results, not as absence of a feature.
