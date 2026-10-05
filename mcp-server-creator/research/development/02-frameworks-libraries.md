# MCP Frameworks and Libraries

Research date: 2026-10-03. Current MCP protocol revision: **2026-07-28**.

This file surveys frameworks and libraries that speed up MCP server development, and how they compare. For each: what it adds over the raw SDK, language, license, maturity/version, and when to choose it. Evidence labels are the same as in `01-sdks-languages.md`: **SOURCE FACT**, **SOURCE CLAIM**, **AI INFERENCE**, **PLAUSIBLE NOT VERIFIED**, **UNKNOWN**.

## FastMCP (Python, and a TypeScript counterpart)

SOURCE FACT: The project describes itself as "a full framework for building Model Context Protocol (MCP) applications" that "manages schema generation, validation, transport, authentication, and protocol compatibility around your application code" ([FastMCP — Welcome](https://gofastmcp.com/getting-started/welcome)).

**Relationship to the official Python SDK.** SOURCE FACT: "FastMCP created the high-level Python API incorporated into the official MCP Python SDK in 2024. The actively maintained standalone project is now downloaded more than a million times a day, and some version of FastMCP powers 70% of MCP servers across all languages" ([FastMCP — Welcome](https://gofastmcp.com/getting-started/welcome)). AI INFERENCE: FastMCP is the upstream origin of the official Python SDK's high-level decorator API (now `MCPServer`), but the standalone project has diverged and is maintained separately by Prefect; the quoted origin statement is the basis.

**What it adds over the raw SDK.** SOURCE FACT: FastMCP provides three pillars — "Servers", "Clients", and "Apps" — where Apps "let tools return forms, tables, charts, and other interactive interfaces alongside ordinary MCP results" ([FastMCP — Welcome](https://gofastmcp.com/getting-started/welcome)). It also ships a CLI (`fastmcp list`, `fastmcp call`, `fastmcp discover`, `fastmcp generate-cli`, `fastmcp install`), provider/transform architecture, component versioning, session state, background tasks, and OpenTelemetry tracing ([FastMCP — Updates](https://gofastmcp.com/updates)).

**2026 releases and protocol era.** SOURCE FACT: "FastMCP 4 is stable: the FastMCP release for the new MCP protocol and the rewritten Python SDK v2, with old-protocol clients supported through per-connection negotiation" ([FastMCP — Updates, v4.0.0, August 31, 2026](https://gofastmcp.com/updates)). The same release notes list "Every protocol era — one deployment serves `2026-07-28` and legacy clients", "Interactive tools", "Background tasks", "Extensions", "Dependency injection", and "Client groups" ([FastMCP — Updates](https://gofastmcp.com/updates)). The most recent release recorded is "FastMCP 4.0.10" dated "September 25, 2026" ([FastMCP — Updates](https://gofastmcp.com/updates)).

**Language / license / maturity.** SOURCE FACT: Python (with an official TypeScript counterpart, `@prefecthq/fastmcp-ts`); the repository shows an MIT license badge; v4 is stable ([FastMCP — Welcome](https://gofastmcp.com/getting-started/welcome), [PrefectHQ/fastmcp README](https://github.com/PrefectHQ/fastmcp)).

**When to choose it.** AI INFERENCE: choose FastMCP when you want batteries-included Python MCP development (auth providers, OpenAPI/Proxy providers, middleware, CLI, interactive apps) and are willing to adopt a third-party framework rather than the official SDK; the quoted feature list is the basis.

Minimal server (SOURCE FACT, from the [FastMCP — Welcome](https://gofastmcp.com/getting-started/welcome)):

```python
from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

if __name__ == "__main__":
    mcp.run()
```

## MCP Framework (TypeScript)

SOURCE FACT: "MCP-Framework is a framework for building Model Context Protocol (MCP) servers elegantly in TypeScript" with "automatic directory-based discovery for tools, resources, and prompts" ([QuantGeekDev/mcp-framework README](https://github.com/QuantGeekDev/mcp-framework)).

**What it adds over the raw SDK.** SOURCE FACT: It is "Built on the official MCP SDK" and adds "Automatic discovery and loading of tools, resources, and prompts", "Multiple transport support (stdio, SSE, HTTP Stream)", "Easy-to-use base classes for tools, prompts, and resources", and "Out of the box authentication for SSE endpoints (OAuth 2.1, JWT, API Key)" ([QuantGeekDev/mcp-framework README](https://github.com/QuantGeekDev/mcp-framework)). It also ships a CLI (`mcp create`, `mcp add tool`, `mcp validate`) and enforces that "All schema fields must have descriptions" ([QuantGeekDev/mcp-framework README](https://github.com/QuantGeekDev/mcp-framework)).

**Language / license / maturity.** SOURCE FACT: TypeScript; MIT license; the README documents Zod-based schemas and a build-time validation step ([QuantGeekDev/mcp-framework README](https://github.com/QuantGeekDev/mcp-framework)). UNKNOWN: a specific stable version number or 2026-07-28 protocol support statement.

**When to choose it.** AI INFERENCE: choose MCP Framework when you want convention-over-configuration TypeScript servers with file-based discovery and built-in SSE auth, and you do not need the newest 2026-07-28 stateless features; the quoted feature list is the basis. PLAUSIBLE NOT VERIFIED: 2026-07-28 support.

Minimal tool (SOURCE FACT, from the [QuantGeekDev/mcp-framework README](https://github.com/QuantGeekDev/mcp-framework)):

```typescript
import { MCPTool, MCPInput } from "mcp-framework";
import { z } from "zod";

const AddToolSchema = z.object({
  a: z.number().describe("First number to add"),
  b: z.number().describe("Second number to add"),
});

class AddTool extends MCPTool {
  name = "add";
  description = "Add tool description";
  schema = AddToolSchema;
  async execute(input: MCPInput<this>) { return `Result: ${input.a + input.b}`; }
}
export default AddTool;
```

## Spring AI (Java / Spring Boot)

SOURCE FACT: "Spring AI embraces MCP with comprehensive support through dedicated Boot Starters and MCP Java Annotations" ([Spring AI — MCP overview](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-overview.html)).

**What it adds over the raw SDK.** SOURCE FACT: Spring AI provides `spring-ai-starter-mcp-client`, `spring-ai-starter-mcp-client-webflux`, `spring-ai-starter-mcp-server`, `spring-ai-starter-mcp-server-webmvc`, and `spring-ai-starter-mcp-server-webflux`, plus annotation-based handling with `@McpTool`, `@McpResource`, `@McpPrompt`, `@McpComplete` and client annotations `@McpLogging`, `@McpSampling`, `@McpElicitation`, `@McpProgress` ([Spring AI — MCP overview](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-overview.html)). It also provides "MCP Security" with "OAuth 2.0 and API key-based security support" ([java-sdk README](https://github.com/modelcontextprotocol/java-sdk)).

**Transports and protocol era.** SOURCE FACT: Server starters support STDIO, SSE, Streamable-HTTP, and "Stateless Streamable-HTTP" via `spring.ai.mcp.server.protocol=STATELESS` ([Spring AI — MCP overview](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-overview.html)).

**Breaking change in Spring AI 2.0.** SOURCE FACT: "Starting with **Spring AI 2.0**, the Spring-specific MCP transport implementations (`mcp-spring-webflux` and `mcp-spring-webmvc`) are no longer shipped by the MCP Java SDK. They have been moved into the Spring AI project itself" ([Spring AI — MCP overview](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-overview.html)). Spring AI 2.0 "requires **MCP Java SDK 1.0.0** (RC1 or later)" ([Spring AI — MCP overview](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-overview.html)).

**Language / license / maturity.** SOURCE FACT: Java / Spring Boot; the reference is versioned "Spring AI 2.0.1"; Apache-2.0 (Spring projects) ([Spring AI — MCP overview](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-overview.html)). PLAUSIBLE NOT VERIFIED: exact license file for the MCP integration module.

**When to choose it.** AI INFERENCE: choose Spring AI when you are already in the Spring Boot ecosystem and want auto-configuration, dependency injection, and annotation-driven MCP servers; the quoted starter and annotation lists are the basis.

Minimal server (SOURCE FACT, from the [MCP docs — Build an MCP server](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server)):

```java
@Service
public class WeatherService {
    @Tool(description = "Get weather alerts for a US state")
    public String getAlerts(
        @ToolParam(description = "Two-letter US state code (e.g. CA, NY)") String state) { ... }
}
```

## mcp-use (TypeScript, with a Python package)

SOURCE FACT: The project calls itself "The TypeScript framework for MCP" for building "MCP servers, ChatGPT plugins, Claude connectors" ([mcp-use/mcp-use README](https://github.com/mcp-use/mcp-use)).

**What it adds over the raw SDK.** SOURCE FACT: "mcp-use builds on the official TypeScript SDK v2 and adds first-class Views, typed tool-to-UI contracts, an optimized stateless runtime, the Inspector, screenshot verification, agent-first CLI workflows, and deployment" ([mcp-use/mcp-use README](https://github.com/mcp-use/mcp-use)). It provides React "Views" bound to tools, a built-in Inspector at `/mcp/inspector`, a headless CLI (`mcp-use client`, `mcp-use screenshot`), and tunneling ([mcp-use/mcp-use README](https://github.com/mcp-use/mcp-use)).

**Protocol era.** SOURCE FACT: The project's own comparison table marks "MCP 2026 protocol" as supported (✅) for mcp-use and the official SDK v2, and "Native Views on MCP 2026" as supported for mcp-use and FastMCP TS but not the official SDK ([mcp-use/mcp-use README](https://github.com/mcp-use/mcp-use)). SOURCE CLAIM (vendor self-comparison, rank: low — the table is published by mcp-use about itself and competitors): the same table claims performance and install-size advantages over FastMCP TS, the official SDK, xmcp, Skybridge, and mcp-handler ([mcp-use/mcp-use README](https://github.com/mcp-use/mcp-use)).

**Language / license / maturity.** SOURCE FACT: TypeScript (and a Python package on PyPI); MIT license; v2 line ([mcp-use/mcp-use README](https://github.com/mcp-use/mcp-use)). UNKNOWN: a specific stable version number.

**When to choose it.** AI INFERENCE: choose mcp-use when you want interactive React UIs ("Views") inside MCP tools and an integrated inspector/tunnel workflow; the quoted feature list is the basis. Treat the vendor benchmark table as a claim, not a fact.

Minimal tool (SOURCE FACT, from the [mcp-use/mcp-use README](https://github.com/mcp-use/mcp-use)):

```typescript
import { MCPServer } from "mcp-use";
import { z } from "zod";

const server = new MCPServer({ name: "weather-app", title: "Weather App", version: "1.0.0" });

export const getWeather = server.tool(
  { name: "get-weather", description: "Get the current weather for a city",
    inputSchema: z.object({ city: z.string().describe("City to look up") }),
    view: { name: "weather-card" } },
  async ({ city }) => ({ content: [{ type: "text", text: `Weather in ${city}` }] })
);
```

## MCP Toolbox for Databases (Go server + multi-language client SDKs)

SOURCE FACT: "MCP Toolbox for Databases is an open source Model Context Protocol (MCP) server that connects your AI agents, IDEs, and applications directly to your enterprise databases" ([googleapis/mcp-toolbox README](https://github.com/googleapis/genai-toolbox)).

**Naming note.** SOURCE FACT: "The `genai-toolbox` repository has been officially renamed to `mcp-toolbox`" ([googleapis/mcp-toolbox README](https://github.com/googleapis/genai-toolbox)). The requested URL `https://github.com/googleapis/genai-toolbox` redirects to the renamed repository.

**What it adds over the raw SDK.** SOURCE FACT: It is a configuration-driven server: "The primary way to configure Toolbox is through the `tools.yaml` file", with `sources`, `tools`, `toolsets`, `prompts`, `resources`, and `resourceTemplates` sections ([googleapis/mcp-toolbox README](https://github.com/googleapis/genai-toolbox)). It adds prebuilt database tools (e.g. `list_tables`, `execute_sql`), connection pooling, IAM auth, and "End-to-end Observability ... with built-in support for OpenTelemetry" ([googleapis/mcp-toolbox README](https://github.com/googleapis/genai-toolbox)). It also ships client SDKs for Python, JS/TS, Go, and Java to load tools into agent frameworks ([googleapis/mcp-toolbox README](https://github.com/googleapis/genai-toolbox)).

**Language / license / maturity.** SOURCE FACT: Server written in Go; Apache-2.0 license; the README references version `1.13.1` in install instructions and follows Semantic Versioning ([googleapis/mcp-toolbox README](https://github.com/googleapis/genai-toolbox)).

**When to choose it.** AI INFERENCE: choose MCP Toolbox when your MCP server is primarily a secure, governed database-access layer and you prefer declarative YAML over writing tool code; the quoted configuration model and prebuilt-tool list are the basis.

Minimal tool config (SOURCE FACT, from the [googleapis/mcp-toolbox README](https://github.com/googleapis/genai-toolbox)):

```yaml
kind: tool
name: search-hotels-by-name
type: postgres-sql
source: my-pg-source
description: Search for hotels based on name.
parameters:
  - name: name
    type: string
    description: The name of the hotel.
statement: SELECT * FROM hotels WHERE name ILIKE '%' || $1 || '%';
```

## mcp-agent (Python)

SOURCE FACT: "`mcp-agent` is a simple, composable framework to build effective agents using Model Context Protocol" ([lastmile-ai/mcp-agent README](https://github.com/lastmile-ai/mcp-agent)).

**What it adds over the raw SDK.** SOURCE FACT: It "fully implements MCP, and handles the pesky business of managing the lifecycle of MCP server connections", implements "every pattern described in Anthropic's Building Effective Agents in a composable way", and "works for simple agents and scales to sophisticated workflows built on Temporal so you can pause, resume, and recover without any API changes to your agent" ([lastmile-ai/mcp-agent README](https://github.com/lastmile-ai/mcp-agent)). It also supports creating servers: "Create MCP servers with a FastMCP-compatible API. You can even expose agents as MCP servers" ([lastmile-ai/mcp-agent README](https://github.com/lastmile-ai/mcp-agent)).

**MCP feature coverage.** SOURCE FACT: The README lists "Core: Tools ✅ Resources ✅ Prompts ✅ Notifications ✅" and "Advanced: OAuth ✅ Sampling ✅ Elicitation ✅ Roots ✅" ([lastmile-ai/mcp-agent README](https://github.com/lastmile-ai/mcp-agent)). UNKNOWN: explicit 2026-07-28 stateless support.

**Language / license / maturity.** SOURCE FACT: Python; Apache-2.0 license; installable via `uv add "mcp-agent"` ([lastmile-ai/mcp-agent README](https://github.com/lastmile-ai/mcp-agent)). UNKNOWN: a specific stable version number.

**When to choose it.** AI INFERENCE: choose mcp-agent when you are building agent applications (not just a server) that consume many MCP servers and need durable, resumable workflows; the quoted agent-pattern and Temporal statements are the basis.

Minimal example (SOURCE FACT, from the [lastmile-ai/mcp-agent README](https://github.com/lastmile-ai/mcp-agent)):

```python
from mcp_agent.app import MCPApp
from mcp_agent.agents.agent import Agent
from mcp_agent.workflows.llm.augmented_llm_openai import OpenAIAugmentedLLM

app = MCPApp(name="hello_world")
async def main():
    async with app.run():
        agent = Agent(name="finder", instruction="Use filesystem and fetch to answer questions.",
                      server_names=["filesystem", "fetch"])
        async with agent:
            llm = await agent.attach_llm(OpenAIAugmentedLLM)
            print(await llm.generate_str("Summarize README.md in two sentences."))
```

## MCP Inspector (developer tool, brief)

SOURCE FACT: The Inspector is "A developer tool for inspecting Model Context Protocol (MCP) servers" that "ships as a single package, `@modelcontextprotocol/inspector`, that provides three ways to inspect a server" — Web, CLI, and TUI ([modelcontextprotocol/inspector README](https://github.com/modelcontextprotocol/inspector)). It is run with `npx @modelcontextprotocol/inspector`, `--cli`, or `--tui` ([modelcontextprotocol/inspector README](https://github.com/modelcontextprotocol/inspector)).

SOURCE FACT: The Inspector "manages secrets — OAuth tokens, OAuth client secrets, and stdio `env:` values — and stores them in the OS keychain, if available, by default" ([modelcontextprotocol/inspector README](https://github.com/modelcontextprotocol/inspector)). It requires Node `>=22.19.0` and is on a v2 line ([modelcontextprotocol/inspector README](https://github.com/modelcontextprotocol/inspector)).

**When to use it.** AI INFERENCE: use the Inspector as the standard local debugging and CI smoke-test tool for any MCP server, regardless of the SDK or framework used to build it; the quoted three-mode description is the basis.

## Comparison summary

| Framework | Language | License | Adds over raw SDK | Protocol era | Best for |
| --- | --- | --- | --- | --- | --- |
| FastMCP | Python (+ TS) | MIT | schema/validation, auth providers, providers/transforms, CLI, Apps, middleware | 2026-07-28 + legacy (v4) | batteries-included Python servers |
| MCP Framework | TypeScript | MIT | file-based discovery, base classes, SSE auth, CLI validation | PLAUSIBLE NOT VERIFIED | convention-over-config TS servers |
| Spring AI | Java / Spring Boot | Apache-2.0 (Spring) | Boot starters, annotations, DI, security | stateless Streamable HTTP | Spring ecosystem servers |
| mcp-use | TypeScript (+ Python) | MIT | React Views, Inspector, CLI, tunneling, stateless runtime | 2026-07-28 (self-claimed) | interactive UI tools |
| MCP Toolbox | Go server + client SDKs | Apache-2.0 | YAML config, prebuilt DB tools, pooling, OTel | UNKNOWN | governed database access |
| mcp-agent | Python | Apache-2.0 | agent patterns, Temporal durability, server creation | UNKNOWN | agent applications |
| MCP Inspector | TypeScript (dev tool) | Apache-2.0 / MIT transition | web/CLI/TUI inspection, secret storage | n/a | debugging and CI |

AI INFERENCE: The frameworks split into two groups — server-authoring frameworks (FastMCP, MCP Framework, Spring AI, mcp-use, MCP Toolbox) and agent/consumer frameworks (mcp-agent), with the Inspector as a cross-cutting dev tool; the quoted descriptions of each are the basis. For a professional server that must track 2026-07-28, FastMCP v4 and Spring AI are the frameworks with the clearest explicit dual-era or stateless statements.

## Retrieval notes

All URLs above were retrieved successfully on 2026-10-03, except that `https://github.com/googleapis/genai-toolbox` redirected to the renamed `mcp-toolbox` repository (content retrieved). The FastMCP updates page was truncated after the FastMCP 2.7 entry; earlier 2.x entries were not analyzed. The `https://docs.spring.io/spring-ai/reference/` root was not fetched directly; the MCP overview page under it was fetched instead.
