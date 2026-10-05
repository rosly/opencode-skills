# MCP Server Development Workflow and Tooling (Protocol Revision 2026-07-28)

Research file. Retrieved: 2026-10-03. Protocol revision referenced throughout: **2026-07-28**.

## Notation and evidence ranking

- **SOURCE FACT** — a normative statement quoted verbatim from an official specification/SEP or official documentation page.
- **SOURCE CLAIM (Rank N)** — a non-normative statement quoted verbatim. Ranks: **Rank A** = Final/Standards-Track SEP or normative specification text; **Rank B** = official documentation page (editorial guidance); **Rank C** = roadmap/project-status page.
- **AI INFERENCE** — my reasoning that names the specific quoted facts it is derived from.
- **PLAUSIBLE NOT VERIFIED** — a conjecture consistent with sources but not directly stated.
- **UNKNOWN** — no source retrieved or source is silent.

Quotations are short and exact. Every externally sourced fact carries an inline link to the source URL. No end-only bibliography is used. All eight requested URLs for this file were retrieved successfully; there are no failed retrievals for FILE 2. Two additional pages (the Inspector CLI client and the FastMCP CLI) were retrieved to cover the requested CLI/scaffolding and Inspector-CLI topics.

## 1. Project scaffolding and layout

**SOURCE FACT.** The official Python quickstart scaffolds with `uv`: "uv init weather", "uv venv", "uv add "mcp[cli]"", then "touch weather.py". ([Build an MCP server](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server))

**SOURCE FACT.** The official TypeScript quickstart scaffolds with npm: "npm init -y", "npm install @modelcontextprotocol/server zod", "npm install -D @types/node typescript", then creates `src/index.ts`. ([Build an MCP server](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server))

**SOURCE FACT.** The TypeScript project sets `"type": "module"`, a `bin` entry, and a build script `"build": "tsc && chmod 755 build/index.js"`, with `tsconfig.json` targeting `ES2022` and `Node16` module resolution. ([Build an MCP server](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server))

**SOURCE FACT.** "Make sure to run `npm run build` to build your server! This is a very important step in getting your server to connect." ([Build an MCP server](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server))

**SOURCE CLAIM (Rank B).** FastMCP presents itself as the standard framework: "FastMCP is the standard framework for building Model Context Protocol (MCP) servers, clients, and interactive applications." ([FastMCP: The Framework for MCP](https://gofastmcp.com/getting-started/welcome))

**SOURCE CLAIM (Rank B).** FastMCP's minimal server is a decorated function: `mcp = FastMCP("Demo 🚀")` then `@mcp.tool` above `def add(a: int, b: int) -> int:`. ([FastMCP: The Framework for MCP](https://gofastmcp.com/getting-started/welcome))

**SOURCE CLAIM (Rank B).** MCP-Framework offers directory-based scaffolding: "MCP-Framework gives you architecture out of the box, with automatic directory-based discovery for tools, resources, and prompts." ([MCP Framework README](https://github.com/QuantGeekDev/mcp-framework))

**SOURCE CLAIM (Rank B).** MCP-Framework's CLI creates and extends projects: "mcp create my-mcp-server", "mcp add tool price-fetcher", "mcp add prompt price-analysis", "mcp add resource market-data". ([MCP Framework README](https://github.com/QuantGeekDev/mcp-framework))

**SOURCE CLAIM (Rank B).** MCP-Framework validates tool schemas: "mcp validate" and "This command checks that all tools using Zod schemas have descriptions for every field." ([MCP Framework README](https://github.com/QuantGeekDev/mcp-framework))

**AI INFERENCE (naming the scaffolding facts).** The official quickstarts are minimal (one file, one server object, one transport), while the frameworks add structure: FastMCP adds a CLI and decorator registration, MCP-Framework adds directory discovery and a build-time schema validator. A team choosing a framework is trading the quickstart's transparency for enforced conventions. This is derived from the quoted quickstart steps and the framework feature statements.

## 2. Local development loop

**SOURCE FACT.** The Python server runs with `mcp.run(transport="stdio")` and "Run `uv run weather.py` to start the MCP server, which will listen for messages from MCP hosts." ([Build an MCP server](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server))

**SOURCE FACT.** The TypeScript server connects a `StdioServerTransport` and logs "Weather MCP Server running on stdio" to stderr. ([Build an MCP server](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server))

**SOURCE CLAIM (Rank B).** FastMCP's CLI is the primary local loop: "The `fastmcp` CLI is installed automatically with FastMCP. It's the primary way to run, test, install, and interact with MCP servers from your terminal." ([FastMCP CLI](https://gofastmcp.com/patterns/cli.md))

**SOURCE CLAIM (Rank B).** FastMCP CLI commands include `run`, `dev inspector`, `install`, `inspect`, `list`, `call`, `discover`, and `generate-cli`. ([FastMCP CLI](https://gofastmcp.com/patterns/cli.md))

**SOURCE CLAIM (Rank B).** "fastmcp dev inspector ... Launch a server inside the MCP Inspector for interactive testing". ([FastMCP CLI](https://gofastmcp.com/patterns/cli.md))

**SOURCE CLAIM (Rank B).** "fastmcp install ... Install a server into Claude Code, Claude Desktop, Cursor, Gemini CLI, or Goose". ([FastMCP CLI](https://gofastmcp.com/patterns/cli.md))

**SOURCE CLAIM (Rank B).** FastMCP resolves server targets automatically: "**Python files** are loaded directly — no `mcp.run()` boilerplate needed." and "**Stdio commands** connect to any MCP server that speaks over standard I/O. Use `--command` instead of a positional argument". ([FastMCP CLI](https://gofastmcp.com/patterns/cli.md))

**SOURCE CLAIM (Rank B).** FastMCP can discover servers already configured in editors: "FastMCP scans configs from Claude Desktop, Claude Code, Cursor, Gemini CLI, and Goose". ([FastMCP CLI](https://gofastmcp.com/patterns/cli.md))

## 3. Connecting to hosts

### Claude Desktop

**SOURCE FACT.** Claude Desktop is configured through `claude_desktop_config.json`, located at "`~/Library/Application Support/Claude/claude_desktop_config.json`" on macOS and "`%APPDATA%\Claude\claude_desktop_config.json`" on Windows. ([Connect to local MCP servers](https://modelcontextprotocol.io/docs/2026-07-28/develop/connect-local-servers))

**SOURCE FACT.** Servers are declared under the `mcpServers` key with `command` and `args`, e.g. `"command": "npx"` and `"args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/username/Desktop"]`. ([Connect to local MCP servers](https://modelcontextprotocol.io/docs/2026-07-28/develop/connect-local-servers))

**SOURCE FACT.** "Make sure you pass in the absolute path to your server." ([Build an MCP server](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server))

**SOURCE FACT.** "After saving the configuration file, completely quit Claude Desktop and restart it. The application needs to restart to load the new configuration and start the MCP server." ([Connect to local MCP servers](https://modelcontextprotocol.io/docs/2026-07-28/develop/connect-local-servers))

**SOURCE FACT.** Remote servers are added as Custom Connectors by URL, e.g. `https://example-server.modelcontextprotocol.io/mcp`, and "Most remote MCP servers require authentication". ([Connect to remote MCP servers](https://modelcontextprotocol.io/docs/2026-07-28/develop/connect-remote-servers))

### VS Code

**SOURCE CLAIM (Rank B).** "The VS Code format is stored in .vscode/mcp.json in your workspace or in your user profile. It defines servers in a top-level servers object." and "The portable format is stored in .mcp.json at the root of your workspace ... It defines servers in a top-level mcpServers object." ([MCP configuration reference — Visual Studio Code](https://code.visualstudio.com/docs/agents/reference/mcp-configuration))

**SOURCE CLAIM (Rank B).** "VS Code first tries the HTTP Stream transport and falls back to SSE if HTTP is not supported." ([MCP configuration reference — Visual Studio Code](https://code.visualstudio.com/docs/agents/reference/mcp-configuration))

**SOURCE CLAIM (Rank B).** "When using Docker with stdio servers, don't use the detach option (-d). The server must run in the foreground to communicate with VS Code." ([MCP configuration reference — Visual Studio Code](https://code.visualstudio.com/docs/agents/reference/mcp-configuration))

**SOURCE CLAIM (Rank B).** "Avoid hardcoding sensitive information like API keys. Use input variables or environment files instead." ([Add and manage MCP servers in VS Code](https://code.visualstudio.com/docs/agent-customization/mcp-servers))

### Cursor

**SOURCE CLAIM (Rank B).** "Create .cursor/mcp.json in your project for project-specific tools." and "Create ~/.cursor/mcp.json in your home directory for tools available everywhere." ([Cursor MCP docs](https://cursor.com/docs/mcp))

**SOURCE CLAIM (Rank B).** "Both files are merged. If the same server name appears in both, the project-level config takes priority." ([MCP integrations — Cursor Docs](https://cursor.com/help/customization/mcp))

**SOURCE CLAIM (Rank B).** "Save the file and restart Cursor." ([MCP integrations — Cursor Docs](https://cursor.com/help/customization/mcp))

**SOURCE CLAIM (Rank B).** Cursor supports config interpolation: "`${env:NAME}` environment variables", "`${userHome}` path to your home folder", "`${workspaceFolder}` project root". ([Cursor MCP docs](https://cursor.com/docs/mcp))

**AI INFERENCE (naming the host-config facts).** The three hosts share the same shape — a JSON file mapping a server name to a `command`/`args` (stdio) or `url`/`headers` (remote) — but differ in file location and top-level key: Claude Desktop uses `mcpServers`, VS Code's workspace format uses `servers`, and Cursor uses `mcpServers`. A server README should therefore document the exact file and key per host rather than assume one config format. This is derived from the quoted config locations and key names.

## 4. MCP Inspector: Web, CLI, and TUI

**SOURCE FACT.** "It ships as a single package, `@modelcontextprotocol/inspector`, providing **three clients behind one binary**": Web (`npx @modelcontextprotocol/inspector`), CLI (`--cli`), and TUI (`--tui`). ([MCP Inspector](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector))

**SOURCE FACT.** "The Inspector requires **Node 22.19.0 or newer** and runs directly through `npx`. No installation is required". ([MCP Inspector](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector))

**SOURCE FACT.** "All three are built on the same shared core, so a connection behaves identically across them: the same transports, the same configuration files, the same OAuth state on disk". ([MCP Inspector](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector))

**SOURCE FACT.** The CLI is scriptable: "Each CLI run connects to a server, invokes the single request you name with `--method`, prints the result, and exits." ([CLI client](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/cli))

**SOURCE FACT.** CLI methods include `initialize`, `tools/list`, `tools/call`, `resources/list`, `resources/read`, `resources/templates/list`, `prompts/list`, and `prompts/get`. ([CLI client](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/cli))

**SOURCE FACT.** "`--format json` emits a single JSON object on stdout with no banners, so the whole output pipes cleanly". ([CLI client](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/cli))

**SOURCE FACT.** Exit codes are stable: "`0` Success."; "`1` Usage or unexpected error (the catch-all)."; "`3` Server requires authentication (401/403, `WWW-Authenticate`, OAuth)."; "`4` Server unreachable (DNS, connection refused, timeout, `fetch failed`)."; "`5` Tool error: `tools/call` returned `isError: true`, or the tool wasn't found." ([CLI client](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/cli))

**SOURCE FACT.** "A `tools/call` that returns `isError: true` still prints its payload, but exits `5`, so an `&&` chain doesn't proceed on a failed call." ([CLI client](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/cli))

**SOURCE FACT (secrets).** "The Inspector manages secrets — OAuth tokens, OAuth client secrets, and stdio `env:` values — and stores them in the OS keychain, if available, by default." ([MCP Inspector repository](https://github.com/modelcontextprotocol/inspector))

**SOURCE CLAIM (Rank B).** The Inspector repo's own quality gate: "npm run local:gate # MANDATORY before pushing". ([MCP Inspector repository](https://github.com/modelcontextprotocol/inspector))

**AI INFERENCE (naming the Inspector facts).** The Inspector is the reference tool because it is transport-agnostic and shared-core: the same connection works in browser, terminal, and CI. The CLI's stable exit codes and single-line JSON error envelope make it the natural automated gate, while the Web/TUI clients serve interactive exploration. This is derived from the quoted "three clients behind one binary", "shared core", and exit-code statements.

## 5. Debugging: stderr, OTel, and common errors

**SOURCE FACT.** "MCP Inspector ... This should be your first stop." ([Debugging](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging))

**SOURCE FACT.** "When building a server that uses the local stdio transport, all messages logged to stderr (standard error) will be captured by the host application automatically." ([Debugging](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging))

**SOURCE FACT.** "Local MCP servers should not log messages to stdout (standard out), as this will interfere with protocol operation." ([Debugging](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging))

**SOURCE FACT.** "For servers using the Streamable HTTP transport, stderr is not captured by the client. Use your own server-side log aggregation or OpenTelemetry for logs". ([Debugging](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging))

**SOURCE FACT.** "Logging over the protocol (`notifications/message`) is deprecated as of protocol version `2026-07-28`." ([Debugging](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging))

**SOURCE FACT.** "MCP defines eight RFC 5424 severity levels (`debug` through `emergency`)." ([Debugging](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging))

**SOURCE FACT (error -32022).** "An `UnsupportedProtocolVersionError` (`-32022`) lists the server's supported versions in its `data` field". ([Debugging](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging))

**SOURCE FACT (error -32602).** "A request missing either required field is rejected with error `-32602` (Invalid params), the same code returned for many other malformed inputs." ([Debugging](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging))

**SOURCE FACT (error -32021).** "If the server needs a capability the request's `clientCapabilities` did not declare, such as elicitation, it returns a `MissingRequiredClientCapabilityError` (`-32021`) naming the missing capabilities." ([Debugging](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging))

**SOURCE FACT.** "every request must carry `io.modelcontextprotocol/protocolVersion` and `io.modelcontextprotocol/clientCapabilities`, and clients should also include `io.modelcontextprotocol/clientInfo`." ([Debugging](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging))

**SOURCE FACT (Claude Desktop logs).** "Log files are written to: macOS: `~/Library/Logs/Claude`; Windows: `%APPDATA%\Claude\logs`". ([Debugging](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging))

**SOURCE FACT (Chrome DevTools).** "Create a `developer_settings.json` file with `allowDevTools` set to true" to inspect client-side errors. ([Debugging](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging))

**AI INFERENCE (naming the logging and error facts).** The three error codes form a diagnostic ladder: `-32022` means the two sides disagree on protocol version, `-32602` means the request is malformed (often a missing `_meta` field), and `-32021` means the server asked for a client capability the request did not declare. Because all three are protocol errors, they surface at the client/application layer rather than in the model's context. This is derived from the quoted error descriptions and the SEP-1303 forwarding distinction.

## 6. Environment and working-directory pitfalls

**SOURCE FACT.** "The working directory for servers launched via the client's config may be undefined (like `/` on macOS) since the client could be started from anywhere". ([Debugging](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging))

**SOURCE FACT.** "Always use absolute paths in your configuration and `.env` files to ensure reliable operation". ([Debugging](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging))

**SOURCE FACT.** "MCP servers launched over stdio inherit only a limited subset of environment variables automatically (the exact set is platform-dependent)." ([Debugging](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging))

**SOURCE FACT.** To provide variables, "you can specify an `env` key in `claude_desktop_config.json`". ([Debugging](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging))

**SOURCE FACT (Windows).** "If your configured server fails to load, and you see within its logs an error referring to `${APPDATA}` within a path, you may need to add the expanded value of `%APPDATA%` to your `env` key". ([Connect to local MCP servers](https://modelcontextprotocol.io/docs/2026-07-28/develop/connect-local-servers))

**SOURCE FACT (stdio logging).** "**For STDIO-based servers:** Never write to stdout. Writing to stdout will corrupt the JSON-RPC messages and break your server." ([Build an MCP server](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server))

**SOURCE FACT.** "Use the standard library `logging` module, which writes to stderr." and "Create one logger per module with `logging.getLogger(__name__)`". ([Build an MCP server](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server))

**SOURCE FACT (C#).** "When creating the `ApplicationHostBuilder`, ensure you use `CreateEmptyApplicationBuilder` instead of `CreateDefaultBuilder`. This ensures that the server does not write any additional messages to the console." ([Build an MCP server](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server))

**AI INFERENCE (naming the working-directory and env facts).** Two independent failure modes share one root cause — the host, not the developer's shell, launches the server. The working directory is undefined, so relative paths break; the environment is a limited subset, so secrets and `%APPDATA%` are missing. Absolute paths plus an explicit `env` block address both. This is derived from the quoted working-directory and environment statements.

## 7. Hot reload and restart

**SOURCE FACT.** "**Configuration changes**: Restart the MCP client"; "**Server code changes**: Restart the client (for Claude Desktop, fully quit and reopen; closing the window is not enough)"; "**Quick iteration**: Use Inspector during development". ([Debugging](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging))

**SOURCE FACT.** "After saving the configuration file, completely quit Claude Desktop and restart it." ([Connect to local MCP servers](https://modelcontextprotocol.io/docs/2026-07-28/develop/connect-local-servers))

**SOURCE CLAIM (Rank B).** "Save the file and restart Cursor." ([MCP integrations — Cursor Docs](https://cursor.com/help/customization/mcp))

**SOURCE CLAIM (Rank B).** The Inspector web client supports fast iteration: "For day-to-day **web** iteration, run Vite directly — fast HMR, no launcher build needed". ([MCP Inspector repository](https://github.com/modelcontextprotocol/inspector))

**AI INFERENCE (naming the restart facts).** There is no protocol-level hot reload: the host owns the server process, so code changes require a full client restart (and for Claude Desktop, a full quit). The Inspector is the exception because it connects to a freshly launched process per run, which is why the docs recommend it for quick iteration. This is derived from the quoted restart and Inspector-iteration statements.

## 8. Versioning your server

**SOURCE FACT.** "The Model Context Protocol uses string-based version identifiers following the format `YYYY-MM-DD`, to indicate the last date backwards incompatible changes were made." ([Versioning](https://modelcontextprotocol.io/docs/2026-07-28/learn/versioning))

**SOURCE FACT.** "The protocol version will *not* be incremented when the protocol is updated, as long as the changes maintain backwards compatibility." ([Versioning](https://modelcontextprotocol.io/docs/2026-07-28/learn/versioning))

**SOURCE FACT.** "Every request declares the protocol version it is using via the `io.modelcontextprotocol/protocolVersion` key in its `_meta` field, and the server accepts or rejects each request independently." ([Versioning](https://modelcontextprotocol.io/docs/2026-07-28/learn/versioning))

**SOURCE FACT.** "Clients and servers **MAY** support multiple protocol versions simultaneously." ([Versioning](https://modelcontextprotocol.io/docs/2026-07-28/learn/versioning))

**SOURCE FACT.** "Clients that want to select a version up front can call `server/discover`, a mandatory RPC that returns the server's supported protocol versions, capabilities, and identity in a single request." ([Versioning](https://modelcontextprotocol.io/docs/2026-07-28/learn/versioning))

**SOURCE FACT (server identity).** The `Implementation` schema "requires `name` and `version`"; servers "SHOULD include this field on every response unless specifically configured not to do so." ([Schema Reference — ResultMetaObject](https://modelcontextprotocol.io/specification/2026-07-28/schema.md))

**SOURCE CLAIM (Rank B).** FastMCP's versioning policy: "For production use, always pin to exact versions" with the example "fastmcp==4.0.5 # Good - an exact version" and "fastmcp>=4.0.0 # Bad - may install breaking changes". ([FastMCP Installation](https://gofastmcp.com/getting-started/installation.md))

**SOURCE CLAIM (Rank B).** "FastMCP follows semantic versioning with pragmatic adaptations for the rapidly evolving MCP ecosystem. Breaking changes may occur in minor versions". ([FastMCP Installation](https://gofastmcp.com/getting-started/installation.md))

**AI INFERENCE (naming the versioning facts).** Two version axes must be tracked separately: the protocol revision (`YYYY-MM-DD`, negotiated per request via `_meta` and `server/discover`) and the server's own software version (`serverInfo.version`). Because the protocol revision is per-request and multiple versions may be supported simultaneously, a server can add support for a new revision without dropping the old one. This is derived from the quoted date-format, per-request `_meta`, and `server/discover` statements.

## Retrieval log

| URL | Result |
|-----|--------|
| https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server | Retrieved |
| https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector | Retrieved |
| https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging | Retrieved |
| https://github.com/modelcontextprotocol/inspector | Retrieved |
| https://gofastmcp.com/getting-started/welcome | Retrieved |
| https://github.com/QuantGeekDev/mcp-framework | Retrieved |
| https://modelcontextprotocol.io/docs/2026-07-28/develop/connect-local-servers | Retrieved |
| https://modelcontextprotocol.io/docs/2026-07-28/develop/connect-remote-servers | Retrieved |
| https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/cli | Retrieved (additional, for Inspector CLI) |
| https://gofastmcp.com/patterns/cli.md | Retrieved (additional, for FastMCP CLI/scaffolding) |
| https://modelcontextprotocol.io/docs/2026-07-28/learn/versioning | Retrieved (additional, for versioning) |
| https://code.visualstudio.com/docs/agents/reference/mcp-configuration | Retrieved (additional, for VS Code host) |
| https://cursor.com/docs/mcp | Retrieved (additional, for Cursor host) |
