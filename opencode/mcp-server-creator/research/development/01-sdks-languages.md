# Official MCP SDKs by Language

Research date: 2026-10-03. Current MCP protocol revision: **2026-07-28**.

This file surveys the official Model Context Protocol SDKs, one section per language, covering server API shape, transports, auth, maturity/tier, a minimal server example, and which SDKs support the 2026-07-28 stateless model versus the legacy `initialize` handshake.

## How to read the evidence labels

- **SOURCE FACT** — stated by an official spec, official docs, or the project's own repository.
- **SOURCE CLAIM** — lower-tier source (vendor blog, third-party comparison); rank is stated.
- **AI INFERENCE** — a conclusion drawn by naming the quoted facts it rests on.
- **PLAUSIBLE NOT VERIFIED** — consistent with evidence but not directly confirmed.
- **UNKNOWN** — no source found.

## The tiering system

SOURCE FACT: The official SDK index states that "SDKs are classified into tiers based on feature completeness, protocol support, and maintenance commitment" ([MCP docs — SDKs](https://modelcontextprotocol.io/docs/2026-07-28/sdk)). The same page lists TypeScript, Python, C#, Go, Rust, and Ruby as **Tier 1**; Java as **Tier 2**; and Swift, PHP, and Kotlin as **Tier 3** ([MCP docs — SDKs](https://modelcontextprotocol.io/docs/2026-07-28/sdk)).

SOURCE FACT: The tiering page defines the levels: "**Tier 1**: Fully supported SDKs with complete protocol implementation, including all non-experimental features and optional capabilities like sampling and elicitation", "**Tier 2**: Actively-maintained SDKs working toward full protocol specification support", and "**Tier 3**: Experimental, partially implemented, or specialized SDKs" ([MCP docs — SDK Tiering System](https://modelcontextprotocol.io/community/sdk-tiers)).

SOURCE FACT: Tier 1 requires a "100% pass rate" on conformance tests, new protocol features "Before new spec version release", issue triage "Within 2 business days", and critical bug resolution "Within 7 days" ([MCP docs — SDK Tiering System](https://modelcontextprotocol.io/community/sdk-tiers)). Tier 2 requires an "80% pass rate" and new features "Within 6 months"; Tier 3 has "No minimum" ([MCP docs — SDK Tiering System](https://modelcontextprotocol.io/community/sdk-tiers)).

SOURCE FACT: The tiering page records the key dates "**January 23, 2026**: Conformance tests available" and "**February 23, 2026**: Official SDK tiering published" ([MCP docs — SDK Tiering System](https://modelcontextprotocol.io/community/sdk-tiers)).

SOURCE FACT: The SDK index says all SDKs support "Creating MCP servers that expose tools, resources, and prompts", "Building MCP clients that can connect to any MCP server", "Local and remote transport protocols", and "Protocol compliance with type safety" ([MCP docs — SDKs](https://modelcontextprotocol.io/docs/2026-07-28/sdk)).

AI INFERENCE: Because Tier 1 requires a 100% conformance pass rate and pre-release feature support, the six Tier 1 SDKs (TypeScript, Python, C#, Go, Rust, Ruby) are the safest default choices for a production server that must track the 2026-07-28 revision; the quoted tier requirements are the basis.

## The 2026-07-28 stateless model in one paragraph

SOURCE FACT: The Python SDK's v2 notes describe the protocol change: "v2 speaks the 2026-07-28 revision of MCP, which removes the connection handshake, the session, and every server-initiated request" ([Python SDK — What's new in v2](https://py.sdk.modelcontextprotocol.io/whats-new/)). The same page explains the mechanics: "A 2026-07-28 client does not open a connection, negotiate, and then talk. Every request carries its protocol version, client info, and client capabilities in `_meta`" and "Over Streamable HTTP there is no `Mcp-Session-Id` on the 2026 path" ([Python SDK — What's new in v2](https://py.sdk.modelcontextprotocol.io/whats-new/)).

SOURCE FACT: The Python SDK "serves **both** revisions at once: the same `streamable_http_app()` (and the same stdio server) answers a 2025-era client's `initialize` and a 2026-era client's requests with nothing to configure" ([Python SDK — What's new in v2](https://py.sdk.modelcontextprotocol.io/whats-new/)).

AI INFERENCE: The practical consequence for server authors is that a modern server should be written to be stateless per request (no reliance on `Mcp-Session-Id`), while still answering the legacy `initialize` handshake for older clients; this follows from the quoted "no `Mcp-Session-Id` on the 2026 path" and "serves both revisions at once" facts.

## TypeScript (Tier 1)

SOURCE FACT: The repository README states "This is the `main` branch — v2 of the SDK (`@modelcontextprotocol/server`, `@modelcontextprotocol/client`), implementing the 2026-07-28 MCP spec" ([typescript-sdk README](https://github.com/modelcontextprotocol/typescript-sdk)). It adds "v2 is the stable release line, released alongside the 2026-07-28 spec. v1.x continues to receive bug fixes and security updates for at least 6 months after v2's release" ([typescript-sdk README](https://github.com/modelcontextprotocol/typescript-sdk)).

- **Server API shape.** SOURCE FACT: Servers are built with `McpServer` and `server.registerTool(name, config, handler)`; "Tool and prompt schemas use Standard Schema — bring Zod v4, Valibot, ArkType, or any compatible library" ([typescript-sdk README](https://github.com/modelcontextprotocol/typescript-sdk)). The v2 docs state "the SDK validates every call against that `z.object(...)` schema before your handler runs" ([TypeScript SDK v2 docs](https://ts.sdk.modelcontextprotocol.io/v2/)).
- **Transports.** SOURCE FACT: The SDK ships "MCP **server** libraries (tools/resources/prompts, Streamable HTTP, stdio, auth helpers)" plus optional middleware packages for "Express, Fastify, Hono, Node.js HTTP" ([typescript-sdk README](https://github.com/modelcontextprotocol/typescript-sdk)).
- **Auth.** SOURCE FACT: The server package exposes `bearerAuth`, `oauthMetadata`, `hostHeaderValidation`, and `originValidation` middleware, and the client package ships OAuth helpers ([TypeScript SDK v2 API reference](https://ts.sdk.modelcontextprotocol.io/v2/)).
- **Maturity.** SOURCE FACT: Tier 1; v2 is the stable line for 2026-07-28 ([MCP docs — SDKs](https://modelcontextprotocol.io/docs/2026-07-28/sdk), [typescript-sdk README](https://github.com/modelcontextprotocol/typescript-sdk)).
- **2026-07-28 stateless.** SOURCE FACT: v2 implements the 2026-07-28 spec; the docs list a "Sessions, state, scaling" page and a "Legacy clients" page, indicating both eras are handled ([TypeScript SDK v2 docs](https://ts.sdk.modelcontextprotocol.io/v2/)).

Minimal server (SOURCE FACT, from the [TypeScript SDK v2 docs](https://ts.sdk.modelcontextprotocol.io/v2/)):

```ts
import { McpServer } from '@modelcontextprotocol/server';
import { serveStdio } from '@modelcontextprotocol/server/stdio';
import * as z from 'zod/v4';

serveStdio(() => {
    const server = new McpServer({ name: 'weather', version: '1.0.0' });
    server.registerTool(
        'get-forecast',
        { description: 'Get the weather forecast for a city',
          inputSchema: z.object({ city: z.string() }) },
        async ({ city }) => ({ content: [{ type: 'text', text: `Sunny in ${city} all week.` }] })
    );
    return server;
});
```

## Python (Tier 1)

SOURCE FACT: The README says the SDK can "Speak every standard transport: stdio, Streamable HTTP, and SSE" and requires "Python 3.10+" ([python-sdk README](https://github.com/modelcontextprotocol/python-sdk)).

- **Server API shape.** SOURCE FACT: The high-level class is `MCPServer` with `@mcp.tool()`, `@mcp.resource()`, and `@mcp.prompt()` decorators; "no JSON Schema (`a: int, b: int` *is* the schema), no request parsing, no validation code, no protocol handling" ([python-sdk README](https://github.com/modelcontextprotocol/python-sdk)). The v2 notes confirm the rename: "`FastMCP` is now `MCPServer`" ([Python SDK — What's new in v2](https://py.sdk.modelcontextprotocol.io/whats-new/)).
- **Transports.** SOURCE FACT: stdio, Streamable HTTP, and SSE; transport configuration moved to `run()` ([python-sdk README](https://github.com/modelcontextprotocol/python-sdk), [Python SDK — What's new in v2](https://py.sdk.modelcontextprotocol.io/whats-new/)).
- **Auth.** SOURCE FACT: The docs include an "Authorization" page and a client "OAuth" page; the v2 notes describe OAuth hardening including RFC 9207 `iss` validation and the SEP-990 identity-assertion flow ([Python SDK — What's new in v2](https://py.sdk.modelcontextprotocol.io/whats-new/)).
- **Maturity.** SOURCE FACT: Tier 1; `pip install mcp` installs 2.x, the stable line ([MCP docs — SDKs](https://modelcontextprotocol.io/docs/2026-07-28/sdk), [Python SDK — What's new in v2](https://py.sdk.modelcontextprotocol.io/whats-new/)).
- **2026-07-28 stateless.** SOURCE FACT: v2 implements 2026-07-28 and serves both eras; the official quickstart requires "the Python MCP SDK 2.0.0 or higher" ([Python SDK — What's new in v2](https://py.sdk.modelcontextprotocol.io/whats-new/), [MCP docs — Build an MCP server](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server)).

Minimal server (SOURCE FACT, from the [python-sdk README](https://github.com/modelcontextprotocol/python-sdk)):

```python
from mcp.server import MCPServer

mcp = MCPServer("Demo")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

@mcp.resource("greeting://{name}")
def greeting(name: str) -> str:
    """Greet someone by name."""
    return f"Hello, {name}!"
```

SOURCE FACT: The official quickstart warns "Never write to stdout. Writing to stdout will corrupt the JSON-RPC messages and break your server" ([MCP docs — Build an MCP server](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server)). This warning applies to every stdio server in every language.

## C# / .NET (Tier 1)

SOURCE FACT: The README calls it "The official C# SDK for the Model Context Protocol" and ships `ModelContextProtocol.Core`, `ModelContextProtocol`, and `ModelContextProtocol.AspNetCore` packages ([csharp-sdk README](https://github.com/modelcontextprotocol/csharp-sdk)).

- **Server API shape.** SOURCE FACT: Attribute-based discovery: "The call to `WithToolsFromAssembly` discovers every class marked with `[McpServerToolType]` in the assembly and registers every `[McpServerTool]` method as a tool" ([C# SDK — Getting Started](https://csharp.sdk.modelcontextprotocol.io/v1/concepts/getting-started.html)). Prompts and resources use `[McpServerPromptType]`/`[McpServerPrompt]` and `[McpServerResourceType]`/`[McpServerResource]` ([C# SDK — Getting Started](https://csharp.sdk.modelcontextprotocol.io/v1/concepts/getting-started.html)).
- **Transports.** SOURCE FACT: stdio via `WithStdioServerTransport()` and HTTP via `ModelContextProtocol.AspNetCore` with `WithHttpTransport()` and `app.MapMcp()` ([C# SDK — Getting Started](https://csharp.sdk.modelcontextprotocol.io/v1/concepts/getting-started.html)).
- **Auth.** SOURCE FACT: The README documents the "Identity Assertion Authorization Grant flow" via `IdentityAssertionGrantProvider` ([csharp-sdk README](https://github.com/modelcontextprotocol/csharp-sdk)).
- **Maturity.** SOURCE FACT: Tier 1 ([MCP docs — SDKs](https://modelcontextprotocol.io/docs/2026-07-28/sdk)).
- **2026-07-28 stateless.** SOURCE FACT: "Stateless mode is recommended for servers that don't need server-to-client requests like sampling or elicitation" and is enabled with `options.Stateless = true` ([C# SDK — Getting Started](https://csharp.sdk.modelcontextprotocol.io/v1/concepts/getting-started.html)).

Minimal server (SOURCE FACT, from the [C# SDK — Getting Started](https://csharp.sdk.modelcontextprotocol.io/v1/concepts/getting-started.html)):

```csharp
builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithToolsFromAssembly();
await builder.Build().RunAsync();

[McpServerToolType]
public static class EchoTool
{
    [McpServerTool, Description("Echoes the message back to the client.")]
    public static string Echo(string message) => $"hello {message}";
}
```

## Go (Tier 1)

SOURCE FACT: The README states "The SDK endeavors to implement the full MCP spec" and documents a version-compatibility table where "v1.7.0+" targets "2026-07-28" and supports "2026-07-28, 2025-11-25\*, 2025-06-18, 2025-03-26, 2024-11-05" ([go-sdk README](https://github.com/modelcontextprotocol/go-sdk)).

- **Server API shape.** SOURCE FACT: Create an `mcp.Server` and register tools with `mcp.AddTool(server, &mcp.Tool{...}, handler)`; the handler signature is `func(ctx, *mcp.CallToolRequest, Input) (*mcp.CallToolResult, Output, error)` ([go-sdk README](https://github.com/modelcontextprotocol/go-sdk)). JSON Schema is derived from struct tags such as `jsonschema:"the name of the person to greet"` ([go-sdk README](https://github.com/modelcontextprotocol/go-sdk)).
- **Transports.** SOURCE FACT: `mcp.StdioTransport{}` for stdio; the `jsonrpc` package is "for users implementing their own transports" ([go-sdk README](https://github.com/modelcontextprotocol/go-sdk)).
- **Auth.** SOURCE FACT: The `auth` package "provides some primitives for supporting OAuth" and `oauthex` provides "extensions to the OAuth protocol, such as ProtectedResourceMetadata" ([go-sdk README](https://github.com/modelcontextprotocol/go-sdk)).
- **Maturity.** SOURCE FACT: Tier 1 ([MCP docs — SDKs](https://modelcontextprotocol.io/docs/2026-07-28/sdk)).
- **2026-07-28 stateless.** SOURCE FACT: v1.7.0+ targets 2026-07-28; the README notes "The roots, sampling, and logging features are deprecated as of protocol version 2026-07-28 by SEP-2577" ([go-sdk README](https://github.com/modelcontextprotocol/go-sdk)).

Minimal server (SOURCE FACT, from the [go-sdk README](https://github.com/modelcontextprotocol/go-sdk)):

```go
server := mcp.NewServer(&mcp.Implementation{Name: "greeter", Version: "v1.0.0"}, nil)
mcp.AddTool(server, &mcp.Tool{Name: "greet", Description: "say hi"}, SayHi)
if err := server.Run(context.Background(), &mcp.StdioTransport{}); err != nil {
    log.Fatal(err)
}
```

## Rust (Tier 1)

SOURCE FACT: The README states "This SDK implements the stable MCP **`2026-07-28`** specification while remaining fully compatible with the **`2025-11-25`** release and earlier versions" ([rust-sdk README](https://github.com/modelcontextprotocol/rust-sdk)). The crate is `rmcp` ([rust-sdk README](https://github.com/modelcontextprotocol/rust-sdk)).

- **Server API shape.** SOURCE FACT: Procedural macros `#[tool]`, `#[tool_router]`, and `#[tool_handler]` "handle all the wiring"; input/output schemas are derived from a struct via `schemars::JsonSchema` ([rust-sdk README](https://github.com/modelcontextprotocol/rust-sdk)).
- **Transports.** SOURCE FACT: stdio via `transport::stdio()`; the README documents "Stateless Streamable HTTP" and a "Transports" section ([rust-sdk README](https://github.com/modelcontextprotocol/rust-sdk)).
- **Auth.** SOURCE FACT: The README has an "OAuth Support" section ([rust-sdk README](https://github.com/modelcontextprotocol/rust-sdk)).
- **Maturity.** SOURCE FACT: Tier 1; the README references a "Migrating to 3.x?" guide ([MCP docs — SDKs](https://modelcontextprotocol.io/docs/2026-07-28/sdk), [rust-sdk README](https://github.com/modelcontextprotocol/rust-sdk)).
- **2026-07-28 stateless.** SOURCE FACT: The README documents both lifecycles: "`serve()` uses the legacy MCP lifecycle: the client sends `initialize`, receives the negotiated server information, and then sends `notifications/initialized`", while `ClientLifecycleMode::Discover` starts "directly with server/discover" ([rust-sdk README](https://github.com/modelcontextprotocol/rust-sdk)). It also states "Protocol `2026-07-28` replaces `resources/subscribe`, `resources/unsubscribe`, and the standalone HTTP GET stream with the transport-neutral, long-lived `subscriptions/listen` request" ([rust-sdk README](https://github.com/modelcontextprotocol/rust-sdk)).

Minimal server (SOURCE FACT, from the [rust-sdk README](https://github.com/modelcontextprotocol/rust-sdk)):

```rust
#[tool_router(server_handler)]
impl Calculator {
    #[tool(description = "Add two numbers")]
    fn add(&self, Parameters(AddParams { a, b }): Parameters<AddParams>) -> String {
        (a + b).to_string()
    }
}
```

## Ruby (Tier 1)

SOURCE FACT: The README says the SDK can "Speak every standard transport: stdio and Streamable HTTP (including SSE), with a Rails integration" and offers clients "with automatic lifecycle negotiation and OAuth 2.1 authorization" ([ruby-sdk README](https://github.com/modelcontextprotocol/ruby-sdk)).

- **Server API shape.** SOURCE FACT: Define a class inheriting `MCP::Tool` with `description`, `input_schema(...)`, and a `self.call(...)` method, then register it with `MCP::Server.new(name:, tools: [...])` ([ruby-sdk README](https://github.com/modelcontextprotocol/ruby-sdk)).
- **Transports.** SOURCE FACT: `MCP::Server::Transports::StdioTransport` and Streamable HTTP, "including mounted inside a Rails application" ([ruby-sdk README](https://github.com/modelcontextprotocol/ruby-sdk)).
- **Auth.** SOURCE FACT: Client-side "OAuth 2.1 authorization" ([ruby-sdk README](https://github.com/modelcontextprotocol/ruby-sdk)).
- **Maturity.** SOURCE FACT: Tier 1 ([MCP docs — SDKs](https://modelcontextprotocol.io/docs/2026-07-28/sdk)).
- **2026-07-28 stateless.** SOURCE FACT: The README claims coverage of "multi round-trip requests" and "automatic lifecycle negotiation", consistent with both eras, but does not name the 2026-07-28 revision explicitly ([ruby-sdk README](https://github.com/modelcontextprotocol/ruby-sdk)). PLAUSIBLE NOT VERIFIED: exact 2026-07-28 stateless support in Ruby.

Minimal server (SOURCE FACT, from the [ruby-sdk README](https://github.com/modelcontextprotocol/ruby-sdk)):

```ruby
class ExampleTool < MCP::Tool
  description "A simple example tool that echoes back its arguments"
  input_schema(properties: { message: { type: "string" } }, required: ["message"])
  class << self
    def call(message:, server_context:)
      MCP::Tool::Response.new([{ type: "text", text: "Hello! Message: #{message}" }])
    end
  end
end
server = MCP::Server.new(name: "example_server", tools: [ExampleTool])
```

## Java (Tier 2)

SOURCE FACT: The README says the SDK "enables Java applications to interact with AI models and tools through a standardized interface, supporting both synchronous and asynchronous communication patterns" and requires Java 17+ ([java-sdk README](https://github.com/modelcontextprotocol/java-sdk)).

- **Server API shape.** SOURCE FACT: The SDK uses "Reactive Streams for public APIs, with Project Reactor as the internal implementation and a synchronous facade for blocking use cases" ([java-sdk README](https://github.com/modelcontextprotocol/java-sdk)). Spring AI adds annotation-based handling with `@McpTool`, `@McpResource`, `@McpPrompt`, `@McpComplete` ([Spring AI — MCP overview](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-overview.html)).
- **Transports.** SOURCE FACT: "Stdio, Streamable-HTTP, Stateless Streamable-HTTP, SSE" ([Spring AI — MCP overview](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-overview.html)).
- **Auth.** SOURCE FACT: "Pluggable authorization hooks for MCP servers; no built-in implementation" ([java-sdk README](https://github.com/modelcontextprotocol/java-sdk)).
- **Maturity.** SOURCE FACT: Tier 2; the README reports conformance "at 0.1.15 version" with "Server | ✅ 40/40 passed (100%)" ([MCP docs — SDKs](https://modelcontextprotocol.io/docs/2026-07-28/sdk), [java-sdk README](https://github.com/modelcontextprotocol/java-sdk)).
- **2026-07-28 stateless.** SOURCE FACT: Spring AI exposes a `STATELESS` protocol property for "Stateless Streamable-HTTP" servers ([Spring AI — MCP overview](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-overview.html)).

Minimal server (SOURCE FACT, from the [MCP docs — Build an MCP server](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server), Spring AI path):

```java
@Service
public class WeatherService {
    @Tool(description = "Get weather alerts for a US state")
    public String getAlerts(
        @ToolParam(description = "Two-letter US state code (e.g. CA, NY)") String state) { ... }
}
```

## Kotlin (Tier 3)

SOURCE FACT: The README calls it a "Kotlin Multiplatform SDK for the Model Context Protocol" that can "Target **JVM, Native, JS, and Wasm** from a single codebase" ([kotlin-sdk README](https://github.com/modelcontextprotocol/kotlin-sdk)).

- **Server API shape.** SOURCE FACT: `Server(serverInfo, options)` with `server.addTool(name, description, inputSchema) { request -> ... }`, `addPrompt`, and `addResource` ([kotlin-sdk README](https://github.com/modelcontextprotocol/kotlin-sdk)).
- **Transports.** SOURCE FACT: "Use standard transports like **stdio**, **SSE**, **Streamable HTTP**, and **WebSocket**"; helpers include `mcpStreamableHttp()` and `mcpStatelessStreamableHttp()` ([kotlin-sdk README](https://github.com/modelcontextprotocol/kotlin-sdk)).
- **Auth.** SOURCE FACT: The README does not document server-side auth; it documents client capabilities (roots, sampling, elicitation) ([kotlin-sdk README](https://github.com/modelcontextprotocol/kotlin-sdk)). UNKNOWN: server-side auth support.
- **Maturity.** SOURCE FACT: Tier 3 ([MCP docs — SDKs](https://modelcontextprotocol.io/docs/2026-07-28/sdk)).
- **2026-07-28 stateless.** SOURCE FACT: The `mcpStatelessStreamableHttp()` helper exists, indicating stateless Streamable HTTP support ([kotlin-sdk README](https://github.com/modelcontextprotocol/kotlin-sdk)).

Minimal server (SOURCE FACT, from the [kotlin-sdk README](https://github.com/modelcontextprotocol/kotlin-sdk)):

```kotlin
mcpServer.addTool(
    name = "example-tool",
    description = "An example tool",
    inputSchema = ToolSchema(properties = buildJsonObject { put("input", buildJsonObject { put("type", "string") }) })
) { request -> CallToolResult(content = listOf(TextContent("Hello, world!"))) }
```

## Swift (Tier 3)

SOURCE FACT: The README states "This Swift SDK implements both client and server components according to the [2025-11-25] (latest) version of the MCP specification" ([swift-sdk README](https://github.com/modelcontextprotocol/swift-sdk)). This is a notable version lag: the README still calls 2025-11-25 "latest" while the current revision is 2026-07-28.

- **Server API shape.** SOURCE FACT: `Server(name, version, capabilities:)` with `server.withMethodHandler(ListTools.self) { ... }` and `withMethodHandler(CallTool.self) { ... }` ([swift-sdk README](https://github.com/modelcontextprotocol/swift-sdk)).
- **Transports.** SOURCE FACT: `StdioTransport`, `HTTPClientTransport`, `StatelessHTTPServerTransport`, `StatefulHTTPServerTransport`, `InMemoryTransport`, and `NetworkTransport` ([swift-sdk README](https://github.com/modelcontextprotocol/swift-sdk)).
- **Auth.** SOURCE FACT: `HTTPClientTransport` supports "OAuth 2.1 Bearer token authorization per the MCP authorization specification", with `BearerTokenValidator` and `ProtectedResourceMetadataValidator` on the server ([swift-sdk README](https://github.com/modelcontextprotocol/swift-sdk)).
- **Maturity.** SOURCE FACT: Tier 3; requires Swift 6.0+ ([MCP docs — SDKs](https://modelcontextprotocol.io/docs/2026-07-28/sdk), [swift-sdk README](https://github.com/modelcontextprotocol/swift-sdk)).
- **2026-07-28 stateless.** SOURCE FACT: The README documents `StatelessHTTPServerTransport` as "HTTP server transport with simple request-response semantics; no session management or SSE streaming", but the stated spec target is 2025-11-25 ([swift-sdk README](https://github.com/modelcontextprotocol/swift-sdk)). AI INFERENCE: the stateless transport is a 2025-11-25-era feature, not necessarily the 2026-07-28 stateless model; the quoted spec target is the basis.

Minimal server (SOURCE FACT, from the [swift-sdk README](https://github.com/modelcontextprotocol/swift-sdk)):

```swift
let server = Server(name: "MyModelServer", version: "1.0.0",
    capabilities: .init(tools: .init(listChanged: true)))
await server.withMethodHandler(CallTool.self) { params in
    return .init(content: [.text("Tool result")], isError: false)
}
```

## PHP (Tier 3)

SOURCE FACT: The README says the SDK "provides a framework-agnostic API for implementing MCP servers and clients in PHP — tools, resources, prompts, STDIO and HTTP transports, sessions, authorization, and both protocol eras (the `initialize` handshake and the stateless `2026-07-28` revision)" ([php-sdk README](https://github.com/modelcontextprotocol/php-sdk)). This is the clearest explicit statement of dual-era support among the Tier 3 SDKs.

- **Server API shape.** SOURCE FACT: Attribute-based: `#[McpTool]` and `#[McpResource(uri: ...)]` on plain PHP methods, wired with `Server::builder()->setDiscovery(...)->build()->run(new StdioTransport())` ([php-sdk README](https://github.com/modelcontextprotocol/php-sdk)).
- **Transports.** SOURCE FACT: STDIO and HTTP transports, with sessions and framework integration ([php-sdk README](https://github.com/modelcontextprotocol/php-sdk)).
- **Auth.** SOURCE FACT: The README lists "authorization" as a feature and links a "Running your server" page covering "sessions, authorization" ([php-sdk README](https://github.com/modelcontextprotocol/php-sdk)).
- **Maturity.** SOURCE FACT: Tier 3; "Until the first major release, this SDK is considered experimental" ([MCP docs — SDKs](https://modelcontextprotocol.io/docs/2026-07-28/sdk), [php-sdk README](https://github.com/modelcontextprotocol/php-sdk)).
- **2026-07-28 stateless.** SOURCE FACT: Explicitly supports "both protocol eras (the `initialize` handshake and the stateless `2026-07-28` revision)" ([php-sdk README](https://github.com/modelcontextprotocol/php-sdk)).

Minimal server (SOURCE FACT, from the [php-sdk README](https://github.com/modelcontextprotocol/php-sdk)):

```php
class Calculator
{
    #[McpTool]
    public function add(int $a, int $b): int { return $a + $b; }
}
exit(Server::builder()
    ->setServerInfo('Calculator', '1.0.0')
    ->setDiscovery(__DIR__, ['.'], excludeDirs: ['vendor'])
    ->build()
    ->run(new StdioTransport()));
```

## Cross-language summary

| SDK | Tier | Server registration | Transports | Server auth | 2026-07-28 stateless |
| --- | --- | --- | --- | --- | --- |
| TypeScript | 1 | `registerTool` + Standard Schema | stdio, Streamable HTTP | bearer/OAuth middleware | Yes (v2) |
| Python | 1 | `@mcp.tool()` decorators | stdio, Streamable HTTP, SSE | OAuth pages | Yes (v2, dual-era) |
| C# | 1 | `[McpServerTool]` attributes | stdio, ASP.NET HTTP | Identity assertion | Yes (`Stateless = true`) |
| Go | 1 | `mcp.AddTool` | stdio, custom | OAuth primitives | Yes (v1.7.0+) |
| Rust | 1 | `#[tool]` macros | stdio, Streamable HTTP | OAuth section | Yes (dual lifecycle) |
| Ruby | 1 | `MCP::Tool` subclass | stdio, Streamable HTTP | client OAuth 2.1 | PLAUSIBLE NOT VERIFIED |
| Java | 2 | programmatic / Spring annotations | stdio, Streamable HTTP, stateless, SSE | pluggable hooks | Yes (Spring `STATELESS`) |
| Kotlin | 3 | `addTool` | stdio, SSE, Streamable HTTP, WebSocket | UNKNOWN | `mcpStatelessStreamableHttp()` |
| Swift | 3 | `withMethodHandler` | stdio, HTTP, stateless/stateful | OAuth 2.1 | Stated spec target 2025-11-25 |
| PHP | 3 | `#[McpTool]` attributes | STDIO, HTTP | authorization | Yes (explicit dual-era) |

AI INFERENCE: For a new professional server in 2026, the Tier 1 SDKs are the lowest-risk choices because Tier 1 mandates a 100% conformance pass rate and pre-release feature support; the quoted tier requirements are the basis. The Swift README's stale "2025-11-25 (latest)" claim is the main version-drift risk observed.

## Retrieval notes

All URLs above were retrieved successfully on 2026-10-03. The C# documentation URL `https://csharp.sdk.modelcontextprotocol.io/concepts/getting-started.html` redirected to `https://csharp.sdk.modelcontextprotocol.io/v1/concepts/getting-started.html`, which was retrieved. The `https://csharp.sdk.modelcontextprotocol.io/` landing page was not separately fetched. The Rust README was truncated by the fetch tool after the "Standard HTTP Headers" section; the truncated remainder was not analyzed.
