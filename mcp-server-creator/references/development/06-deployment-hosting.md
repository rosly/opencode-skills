# Deploying and Hosting MCP Servers

Research note for the MCP server creator skill. Protocol revision under discussion: **2026-07-28**. Compiled 2026-10-03.

Notation used throughout:

- **SOURCE FACT** — official specification, official documentation, or official repository.
- **SOURCE CLAIM** — lower-tier source (vendor blog, community guide, search snippet); rank is stated.
- **AI INFERENCE** — a conclusion drawn by naming the quoted facts it rests on.
- **PLAUSIBLE NOT VERIFIED** — consistent with sources but not directly confirmed.
- **UNKNOWN** — no source found.

---

## 1. Choosing stdio vs. Streamable HTTP

MCP defines two standard transports. SOURCE FACT (official spec): "In the **stdio** transport, the client launches the MCP server as a subprocess." ([stdio transport spec](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio.md))

SOURCE FACT (official spec): "In the **Streamable HTTP** transport, the server operates as an independent process that can handle multiple client connections." ([Streamable HTTP spec](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md))

SOURCE FACT (official spec): Streamable HTTP "was introduced in protocol version 2025-03-26 as a replacement for the [HTTP+SSE transport][http-sse] from protocol version 2024-11-05." ([Streamable HTTP spec](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md))

SOURCE FACT (official docs): "Remote servers should use the Streamable HTTP transport. The SSE transport is [deprecated](https://modelcontextprotocol.io/specification/draft/deprecated), so publish an `"sse"` remote only to support existing clients." ([MCP Registry: Publishing Remote Servers](https://modelcontextprotocol.io/registry/remote-servers))

SOURCE FACT (official docs): "A remote server **MUST** be publicly accessible at its specified URL." ([MCP Registry: Publishing Remote Servers](https://modelcontextprotocol.io/registry/remote-servers))

SOURCE CLAIM (vendor docs, rank: Docker official documentation): "Streamable HTTP is the current recommended transport for most hosted MCP servers." ([Docker Agent: Remote MCP Servers](https://docs.docker.com/ai/docker-agent/features/remote-mcp))

### 1.1 Decision guidance

AI INFERENCE, from the quoted facts: choose **stdio** when the server runs on the same machine as the client and needs local filesystem or process access; choose **Streamable HTTP** when the server must be reachable by multiple clients, hosted remotely, or published to the registry. This rests on the stdio "subprocess" fact and the Streamable HTTP "independent process that can handle multiple client connections" fact.

SOURCE CLAIM (vendor docs): Docker Agent supports "**Streamable HTTP**, **SSE** (Server-Sent Events), and **Unix domain sockets**", and "Use a `unix://` URL to connect to an MCP server listening on a local Unix socket" ([Docker Agent: Remote MCP Servers](https://docs.docker.com/ai/docker-agent/features/remote-mcp)).

---

## 2. Packaging local servers

### 2.1 npx and uvx

SOURCE FACT (official docs): The canonical local install pattern is a package runner. The filesystem server is configured as `"command": "npx"` with `"args": ["-y", "@modelcontextprotocol/server-filesystem", ...]` ([Connect to local MCP servers](https://modelcontextprotocol.io/docs/2026-07-28/develop/connect-local-servers)).

SOURCE FACT (official docs): The Inspector can launch published servers via either runner: `npx -y @modelcontextprotocol/inspector npx @modelcontextprotocol/server-filesystem ~/Desktop` and `npx @modelcontextprotocol/inspector uvx mcp-server-git --repository ~/code/mcp/servers.git` ([MCP Inspector docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector)).

SOURCE FACT (official repo): The Python SDK installs a CLI extra: "The `cli` extra adds the `mcp` command-line tool (`mcp dev`, `mcp run`, `mcp install`)" ([python-sdk README](https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md)).

### 2.2 MCPB (MCP Bundles)

SOURCE FACT (official repo): "MCP Bundles (.mcpb) are zip archives containing a local MCP server and a manifest.json that describes the server and its capabilities." ([modelcontextprotocol/mcpb README](https://github.com/modelcontextprotocol/mcpb/blob/main/README.md))

SOURCE FACT (official repo): "The format is spiritually similar to Chrome extensions (.crx) or VS Code extensions (.vsix), enabling end users to install local MCP servers with a single click." ([modelcontextprotocol/mcpb README](https://github.com/modelcontextprotocol/mcpb/blob/main/README.md))

SOURCE FACT (official repo): "We recommend implementing MCP servers in Node.js rather than Python to reduce installation friction. Node.js ships with Claude for macOS and Windows, which means your bundle will work out-of-the-box for users without requiring them to install additional Python runtimes" ([modelcontextprotocol/mcpb README](https://github.com/modelcontextprotocol/mcpb/blob/main/README.md)).

SOURCE FACT (official repo): The packaging workflow is `mcpb init` then `mcpb pack`, installed via `npm install -g @anthropic-ai/mcpb` ([modelcontextprotocol/mcpb README](https://github.com/modelcontextprotocol/mcpb/blob/main/README.md)).

SOURCE FACT (official blog): "The MCP Bundle format (MCPB) is now part of the Model Context Protocol project." ([MCP Blog: Adopting the MCP Bundle format](https://blog.modelcontextprotocol.io/posts/2025-11-20-adopting-mcpb))

SOURCE CLAIM (vendor docs, rank: third-party docs site): "An MCPB file (`.mcpb`) is a ZIP archive containing a local MCP server and a `manifest.json`" and the format "supports four server types: Node.js ... Python ... Binary ... UV Runtime (experimental)" ([MCPBundles Docs](https://www.mcpbundles.com/docs/concepts/mcpb-files)).

SOURCE CLAIM (vendor docs, rank: Microsoft Learn): "If you want your MCP server to run in default mode, the values returned by your server implementation must match the values declared in your MCPB file." ([Microsoft Learn: Register an MCP server with an MCP bundle](https://learn.microsoft.com/en-us/windows/ai/mcp/servers/mcp-mcpb))

---

## 3. Containerizing

SOURCE FACT (official docs): The Inspector publishes a container image: "A container image is published to GitHub Container Registry for `linux/amd64` and `linux/arm64`" ([Inspector Recipes](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/recipes)).

SOURCE FACT (official docs): "The image defaults to `--web`, bound to `0.0.0.0:6274` with browser auto-open off, and runs as a non-root user." ([Inspector Recipes](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/recipes))

SOURCE FACT (official docs): "Its `HEALTHCHECK` probes the web UI, so add `--no-healthcheck` when running `--cli` or `--tui`" ([Inspector Recipes](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/recipes)).

SOURCE CLAIM (vendor docs, rank: Docker official documentation): Docker Agent can connect to a server "running Docker Agent inside a container and exposing an MCP server from the host via a bind-mounted socket" ([Docker Agent: Remote MCP Servers](https://docs.docker.com/ai/docker-agent/features/remote-mcp)).

SOURCE CLAIM (vendor docs, rank: Docker Hub / Google): The Cloud Run MCP server is distributed as `mcp/cloud-run-mcp` and can be run with `docker run -i --rm ... mcp/cloud-run-mcp` ([Docker Hub: Cloud Run MCP Server](https://hub.docker.com/r/mcp/cloud-run-mcp)).

SOURCE CLAIM (vendor blog, rank: AWS Builder Center): "To validate this pattern end-to-end, I built a reference Docker image that packages MCP servers inside a Lambda-compatible container" ([AWS Builder Center: Ship Your MCP Server to AWS Lambda in 5 Minutes](https://builder.aws.com/content/3AIQ6E9f2DnyQaNmHKuCZ5NpUUS/ship-your-mcp-server-to-aws-lambda-in-5-minutes)).

---

## 4. Serverless hosting and why statelessness enables it

### 4.1 The stateless core

SOURCE FACT (official spec): "The Model Context Protocol (MCP) is a **stateless protocol**: all the information needed to process a request is contained in the request itself." ([MCP base protocol overview](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md))

SOURCE FACT (official spec): "Servers **MUST NOT** rely on prior requests over the same connection to establish context (e.g., capabilities, protocol version, client identity). Every request supplies this metadata in its [`_meta`](#_meta) field." ([MCP base protocol overview](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md))

SOURCE FACT (official spec): "State that needs to span multiple requests (e.g., long-running tasks, application-level handles) **MUST** be referenced by an explicit identifier the client passes on each request." ([MCP base protocol overview](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md))

SOURCE FACT (official spec): Revision 2026-07-28 changed Streamable HTTP: "Removal of the GET stream endpoint. Removal of protocol-level sessions." ([Streamable HTTP spec](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md))

SOURCE FACT (official docs): "With MCP version 2026-07-28, MCP changes from a bidirectional, stateful protocol to a stateless protocol. Each MCP request is self-describing and can be routed using headers." ([Cloud Run: Use the Cloud Run remote MCP server](https://docs.cloud.google.com/run/docs/use-cloud-run-mcp))

AI INFERENCE: Statelessness is what makes serverless hosting viable. A request carries its own protocol version, capabilities, and identity, so any instance can serve it without session affinity. This rests on the quoted "all the information needed to process a request is contained in the request itself" and "Removal of protocol-level sessions" facts.

### 4.2 AWS Lambda

SOURCE CLAIM (vendor blog, rank: AWS Builder Center, Part 1): "Since we're implementing a stateless HTTP-only server, we handle these methods as follows: POST: Processes all MCP tool calls and returns standard HTTP responses; GET: Returns 405 Method Not Allowed (we've chosen not to implement SSE streaming for this stateless implementation); DELETE: Returns 405 Method Not Allowed (not needed, no sessions to terminate in stateless mode)." ([AWS Builder Center: Building a Serverless remote MCP Server on AWS — Part 1](https://builder.aws.com/content/2s44xHTSbQgo2Ws2bJr6hZsECGr/building-a-serverless-remote-mcp-server-on-aws-part-1))

SOURCE CLAIM (vendor blog, rank: AWS Builder Center): "We'll focus on using the 'Streamable HTTP (sessionless)' communication method to implement an MCP server as a Lambda function, and efficiently deploy it using AWS Lambda Web Adapter." ([AWS Builder Center: Building Scalable MCP Servers on AWS Lambda](https://builder.aws.com/content/2vzj07Wyk6Lw281Tvs1Lw7kJJNW/building-scalable-mcp-servers-on-aws-lambda-a-practical-guide))

SOURCE CLAIM (vendor blog): "Stateless Design : Perfectly matches Lambda's execution model" and "Minimized Cold Starts : No session state restoration required" ([AWS Builder Center: Building Scalable MCP Servers on AWS Lambda](https://builder.aws.com/content/2vzj07Wyk6Lw281Tvs1Lw7kJJNW/building-scalable-mcp-servers-on-aws-lambda-a-practical-guide)).

SOURCE CLAIM (vendor blog): "Stateless is also a hard constraint at the architecture level, since Lambda has no concept of long-lived sessions tied to a specific compute instance." ([AWS Builder Center: Hosting an MCP Server on AWS in 2026](https://builder.aws.com/content/3Dujid4QBzCvCrJKOfhf6O6kl5Y/hosting-an-mcp-server-on-aws-in-2026))

SOURCE CLAIM (vendor blog): "If yes, Lambda Function URL with AuthType=AWS_IAM is the right answer for almost every workload." and "If yes, Lambda plus API Gateway is the right answer" for external OAuth clients ([AWS Builder Center: Hosting an MCP Server on AWS in 2026](https://builder.aws.com/content/3Dujid4QBzCvCrJKOfhf6O6kl5Y/hosting-an-mcp-server-on-aws-in-2026)).

SOURCE CLAIM (vendor blog, rank: Serverless Framework blog, via search index): "Serverless Framework v4.41.0 introduces native MCP server deployment to AWS Lambda via four lines of YAML." ([daily.dev summary of Serverless Framework blog](https://daily.dev/posts/deploy-mcp-servers-on-aws-lambda-with-serverless-framework-v4-vjpvaowku))

SOURCE CLAIM (vendor docs, rank: Serverless Framework): "Introducing Serverless MCP : Built for Cursor, Windsurf, and other AI-powered IDEs, it auto-detects cloud resources from your code" ([Serverless Framework README](https://github.com/serverless/serverless/blob/main/README.md)).

SOURCE CLAIM (vendor repo, rank: AWS Labs): The `MCPLambdaHandler` library "provides a minimal, extensible framework for building MCP HTTP endpoints with pluggable session management support" and "You can use the default stateless (NoOp) session store, or configure a DynamoDB-backed store for persistent sessions." ([awslabs/mcp mcp-lambda-handler README](https://github.com/awslabs/mcp/blob/main/src/mcp-lambda-handler/README.md))

SOURCE CLAIM (vendor repo, rank: community blueprint): "The 2026-07-28 protocol is stateless: no initialize handshake, no Mcp-Session-Id, and the server runs with stateless_http=True." ([ran-isenberg/aws-lambda-mcp-cookbook](https://github.com/ran-isenberg/aws-lambda-mcp-cookbook))

### 4.3 Cloudflare Workers

SOURCE FACT (official docs): Cloudflare's Agents SDK offers `createMcpHandler()` which is "No" for stateful, "stateless with legacy compatibility", and "Best for: New stateless tools" ([Cloudflare: Build a Remote MCP server](https://developers.cloudflare.com/agents/model-context-protocol/guides/remote-mcp-server/)).

SOURCE FACT (official docs): "Use `createMcpHandler` for a new stateless server. An existing `McpAgent` without legacy stateful dependencies can migrate directly." ([Cloudflare: Build a Remote MCP server](https://developers.cloudflare.com/agents/model-context-protocol/guides/remote-mcp-server/))

SOURCE FACT (official docs): "Deploy once and Cloudflare runs your agents across its global network, scaling to tens of millions of instances. No infrastructure to manage, no sessions to reconstruct, no state to externalize." ([Cloudflare Agents](https://developers.cloudflare.com/agents/))

SOURCE FACT (official docs): "You can now deploy your MCP server to Cloudflare. From your project directory, run: `npx wrangler@latest deploy`" ([Cloudflare: Build a Remote MCP server](https://developers.cloudflare.com/agents/model-context-protocol/guides/remote-mcp-server/)).

SOURCE FACT (official docs): Cloudflare's `McpAgent` "gives you a Durable Object per session with built-in state management, elicitation support, and both SSE and Streamable HTTP transports" ([Cloudflare: Build a Remote MCP server](https://developers.cloudflare.com/agents/guides/remote-mcp-server)).

### 4.4 Azure Container Apps

SOURCE FACT (official docs): "Azure Container Apps supports two hosting models for MCP servers: Standalone container app ... Dynamic sessions" ([Microsoft Learn: MCP servers on Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/mcp-overview)).

SOURCE FACT (official docs): For the standalone model, "Container Apps has no MCP-specific awareness. The platform provides: HTTPS ingress with automatic TLS termination; Autoscaling, including scale-to-zero (a minimum of one replica is recommended for interactive MCP use); CORS policy ...; Built-in authentication with Microsoft Entra ID (optional)" ([Microsoft Learn: MCP servers on Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/mcp-overview)).

SOURCE FACT (official docs): "Azure provides five ways to host an MCP server. Each option targets a different mix of flexibility, simplicity, and isolation." The five are Container Apps (standalone), Container Apps dynamic sessions, App Service, Azure Functions, and AKS ([Microsoft Learn: Choose an Azure service for your MCP server](https://learn.microsoft.com/en-us/azure/container-apps/mcp-choosing-azure-service)).

SOURCE FACT (official docs): "Azure Functions is optimized for stateless, event-driven tool execution with per-invocation pricing." ([Microsoft Learn: Choose an Azure service for your MCP server](https://learn.microsoft.com/en-us/azure/container-apps/mcp-choosing-azure-service))

SOURCE CLAIM (vendor blog, rank: Microsoft Tech Community, April 2025): "In this article, we'll explore how to run remote MCP servers as serverless containers in Azure Container Apps and use them in GitHub Copilot" ([Microsoft Tech Community: Host remote MCP servers in Azure Container Apps](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)).

### 4.5 Google Cloud Run

SOURCE FACT (official docs): "Cloud Run supports hosting MCP servers with streamable HTTP transport, but not MCP servers with stdio transport." ([Cloud Run: Host MCP servers on Cloud Run](https://docs.cloud.google.com/run/docs/host-mcp-servers))

SOURCE FACT (official docs): "After you deploy your HTTP MCP server to Cloud Run, the MCP server gets a HTTPS URL and communication can use Cloud Run's built in support for HTTP response streaming." ([Cloud Run: Host MCP servers on Cloud Run](https://docs.cloud.google.com/run/docs/host-mcp-servers))

SOURCE FACT (official docs): The tutorial deploys with `mcp.run_async(transport="streamable-http", host="0.0.0.0", port=os.getenv("PORT", 8080))` and notes "host='0.0.0.0' required for Cloud Run" ([Cloud Run: Build and deploy a remote MCP server on Cloud Run](https://docs.cloud.google.com/run/docs/tutorials/deploy-remote-mcp-server)).

SOURCE FACT (official docs): "Cloud Run is a fully managed application platform that lets you run containers as services, jobs, worker pools, or instances. Cloud Run is serverless: it abstracts away all infrastructure management" ([Cloud Run documentation](https://cloud.google.com/run/docs)).

SOURCE CLAIM (vendor repo, rank: GoogleCloudPlatform): The Cloud Run MCP server can itself be deployed to Cloud Run: `gcloud run deploy cloud-run-mcp --image us-docker.pkg.dev/cloudrun/container/mcp --no-allow-unauthenticated` ([GoogleCloudPlatform/cloud-run-mcp README](https://github.com/GoogleCloudPlatform/cloud-run-mcp/blob/main/README.md)).

---

## 5. Kubernetes, gateways, and proxies

SOURCE FACT (official repo): ToolHive "runs every MCP server in an isolated container, enforces identity and access policy per request when configured with an authentication source, and gives platform teams the observability they need to put MCP in production." ([stacklok/toolhive README](https://github.com/stacklok/toolhive))

SOURCE FACT (official repo): "ToolHive includes a Kubernetes operator, so you can declare policies, integrate with your IdP and observability stack, emit OTel traces, and more" ([stacklok/toolhive README](https://github.com/stacklok/toolhive)).

SOURCE FACT (official repo): ToolHive's Gateway "Orchestrate multiple tools into a virtual MCP with a deterministic workflow engine", "Define access policies and network endpoints", and "Centralize control of security policy, authentication, authorization, auditing" ([stacklok/toolhive README](https://github.com/stacklok/toolhive)).

SOURCE FACT (official repo): ToolHive's Runtime "Deploy MCP servers in the cloud via Kubernetes for enterprise scalability", "Run MCP servers locally via Docker or Podman", and "Proxy remote MCP servers securely for unified management" ([stacklok/toolhive README](https://github.com/stacklok/toolhive)).

SOURCE FACT (official docs): Azure's AKS option: "Deploy MCP servers as standard Kubernetes Deployments with HTTP ingress. AKS gives you full access to the Kubernetes API, so you can use Helm charts, custom networking (CNI, network policies), service mesh, GPU node pools, and KEDA-based autoscaling." ([Microsoft Learn: Choose an Azure service for your MCP server](https://learn.microsoft.com/en-us/azure/container-apps/mcp-choosing-azure-service))

SOURCE FACT (official spec): Streamable HTTP mirrors body fields into headers "so that intermediaries (load balancers, gateways, observability tooling) can route and inspect requests without parsing the body." ([Streamable HTTP spec](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md))

SOURCE FACT (official spec): "Intermediate servers that do not recognize an `Mcp-Param-{Name}` header **MUST** forward it and otherwise ignore it" ([Streamable HTTP spec](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md)).

SOURCE FACT (official spec): "Intermediaries that enforce policy based on mirrored headers (e.g., routing or rate-limiting by tenant) **SHOULD** verify that the `MCP-Protocol-Version` header indicates a version that requires header–body validation." ([Streamable HTTP spec](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md))

SOURCE CLAIM (vendor docs, rank: Docker official documentation): Docker Agent "automatically reconnect after the server closes an idle connection — no configuration needed. Services like Notion and Linear close idle connections periodically; Docker Agent detects the clean close and reconnects with exponential backoff." ([Docker Agent: Remote MCP Servers](https://docs.docker.com/ai/docker-agent/features/remote-mcp))

---

## 6. Scaling, cold starts, timeouts, and streaming

SOURCE FACT (official spec): "When initiating an SSE stream, servers **SHOULD** include the `X-Accel-Buffering: no` header in the HTTP response. This instructs reverse proxies (such as nginx) to disable response buffering" ([Streamable HTTP spec](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md)).

SOURCE FACT (official spec): "For long-lived streams ... servers are encouraged to periodically emit an SSE comment line (a line beginning with a colon, e.g. `:\r\n`) as a keep-alive." ([Streamable HTTP spec](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md))

SOURCE FACT (official spec): "Resumable SSE streams via `Last-Event-ID` are not supported." ([Streamable HTTP spec](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md))

SOURCE FACT (official spec): "Closing the SSE response stream **MUST** be treated by the server as cancellation of that request." ([Streamable HTTP spec](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md))

SOURCE FACT (official spec): For stdio, "If the server process exits unexpectedly, the client **SHOULD** restart it. Because the protocol is stateless, any in-flight requests are simply lost and the client can retry them against the fresh process." ([stdio transport spec](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio.md))

SOURCE CLAIM (vendor blog): "Minimized Cold Starts : No session state restoration required" ([AWS Builder Center: Building Scalable MCP Servers on AWS Lambda](https://builder.aws.com/content/2vzj07Wyk6Lw281Tvs1Lw7kJJNW/building-scalable-mcp-servers-on-aws-lambda-a-practical-guide)).

SOURCE CLAIM (vendor blog): "Serverless scale – Zero to thousands of calls automatically" and "Cost-efficient – Most setups cost less than $1/month" ([AWS Builder Center: Ship Your MCP Server to AWS Lambda in 5 Minutes](https://builder.aws.com/content/3AIQ6E9f2DnyQaNmHKuCZ5NpUUS/ship-your-mcp-server-to-aws-lambda-in-5-minutes)).

SOURCE CLAIM (vendor docs): "Autoscaling, including scale-to-zero (a minimum of one replica is recommended for interactive MCP use)" ([Microsoft Learn: MCP servers on Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/mcp-overview)).

SOURCE CLAIM (vendor docs): Docker Agent "handles the failure automatically: Silent refresh: when a refresh token is available, Docker Agent silently exchanges it for a new access token and replays the request" ([Docker Agent: Remote MCP Servers](https://docs.docker.com/ai/docker-agent/features/remote-mcp)).

AI INFERENCE: The removal of `Last-Event-ID` resumability in 2026-07-28 shifts the burden of recovery to the client and to application-level identifiers. This rests on the quoted "Resumable SSE streams via `Last-Event-ID` are not supported" and "State that needs to span multiple requests ... MUST be referenced by an explicit identifier" facts.

---

## 7. Health checks and observability hooks

SOURCE FACT (official docs): The Inspector image's "`HEALTHCHECK` probes the web UI" ([Inspector Recipes](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/recipes)).

SOURCE FACT (official spec): The `_meta` keys `traceparent`, `tracestate`, and `baggage` are reserved for OpenTelemetry trace context propagation, and "When present, their values MUST follow [W3C Trace Context] and [W3C Baggage] formats respectively." ([MCP base protocol overview](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md))

SOURCE FACT (official spec): "Servers **SHOULD** include the following `io.modelcontextprotocol/*` field in every result's `_meta` ... `io.modelcontextprotocol/serverInfo`" ([MCP base protocol overview](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md)).

SOURCE FACT (official docs): "For servers using the [Streamable HTTP transport], stderr is not captured by the client. Use your own server-side log aggregation or [OpenTelemetry](https://opentelemetry.io/) for logs" ([MCP Debugging docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging)).

SOURCE FACT (official repo): ToolHive "Leverage OpenTelemetry and Prometheus for monitoring and audit logging" ([stacklok/toolhive README](https://github.com/stacklok/toolhive)).

SOURCE CLAIM (vendor docs): Azure Container Apps templates include "Application Insights: Provides telemetry and monitoring." ([MicrosoftDocs/azure-dev-docs: Deploy the Azure MCP Server as a Remote MCP Server](https://github.com/MicrosoftDocs/azure-dev-docs/blob/main/articles/azure-mcp-server/how-to/deploy-remote-mcp-server-copilot-studio.md))

SOURCE CLAIM (vendor docs): Cloudflare Agents provide "Observability Logs · metrics · traces" ([Cloudflare Agents](https://developers.cloudflare.com/agents/)).

---

## 8. Security and endpoint hardening for hosted servers

SOURCE FACT (official spec): "Servers **MUST** validate the `Origin` header on all incoming connections to prevent DNS rebinding attacks." ([Streamable HTTP spec](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md))

SOURCE FACT (official spec): "When running locally, servers **SHOULD** bind only to localhost (127.0.0.1) rather than all network interfaces (0.0.0.0)." ([Streamable HTTP spec](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md))

SOURCE FACT (official spec): "Servers **SHOULD** implement proper authentication for all connections." ([Streamable HTTP spec](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md))

SOURCE FACT (official spec): "Servers that process the request body **MUST** reject requests where the values specified in the headers do not match the corresponding values in the request body." ([Streamable HTTP spec](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md))

SOURCE FACT (official docs): "MCP servers intending for their servers to be run locally **SHOULD** implement measures to prevent unauthorized usage from malicious processes: Use the `stdio` transport to limit access to just the MCP client; Restrict access if using an HTTP transport, such as: Require an authorization token; Use unix domain sockets or other Interprocess Communication (IPC) mechanisms with restricted access" ([MCP Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices)).

SOURCE CLAIM (vendor docs): Docker Agent's `allow_private_ips` defaults to blocking private/loopback/link-local addresses "to reduce SSRF risk", and "Set `allow_private_ips: true` on a remote MCP toolset only when the MCP server or its OAuth registration/token endpoints intentionally resolve to private, loopback, or link-local addresses." ([Docker Agent: Remote MCP Servers](https://docs.docker.com/ai/docker-agent/features/remote-mcp))

SOURCE CLAIM (vendor docs): Azure Container Apps standalone MCP servers use "Container Apps built-in authentication with Microsoft Entra ID" with "OAuth 2.0 Bearer token" ([Microsoft Learn: Secure MCP servers on Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/mcp-authentication)).

---

## 9. Publishing to the MCP Registry

SOURCE FACT (official docs): Remote servers are declared via the `remotes` property in `server.json`, with `"type": "streamable-http"` and a `url` ([MCP Registry: Publishing Remote Servers](https://modelcontextprotocol.io/registry/remote-servers)).

SOURCE FACT (official docs): "Remote servers can define URL template variables using `{curly_braces}` notation. This enables multi-tenant deployments where a single server definition can support multiple endpoints with configurable values" ([MCP Registry: Publishing Remote Servers](https://modelcontextprotocol.io/registry/remote-servers)).

SOURCE FACT (official docs): "MCP clients can be instructed to send specific HTTP headers by adding the `headers` property to the `remotes` entry" ([MCP Registry: Publishing Remote Servers](https://modelcontextprotocol.io/registry/remote-servers)).

SOURCE FACT (official docs): "The `remotes` property can coexist with the `packages` property in `server.json` in order to allow MCP host applications to choose the preferred method of installation." ([MCP Registry: Publishing Remote Servers](https://modelcontextprotocol.io/registry/remote-servers))

SOURCE FACT (official docs): "The MCP Registry is currently in preview. Breaking changes or data resets may occur before general availability." ([MCP Registry: Publishing Remote Servers](https://modelcontextprotocol.io/registry/remote-servers))

---

## 10. Practical decision matrix

AI INFERENCE, assembled from the quoted facts above:

| Requirement | Recommended transport / host | Basis |
| - | - | - |
| Local filesystem or process access | stdio | "the client launches the MCP server as a subprocess" ([stdio spec](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio.md)) |
| Multiple remote clients | Streamable HTTP | "independent process that can handle multiple client connections" ([Streamable HTTP spec](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md)) |
| One-click desktop install | MCPB bundle | "install local MCP servers with a single click" ([mcpb README](https://github.com/modelcontextprotocol/mcpb/blob/main/README.md)) |
| Serverless, stateless tools | Lambda / Workers / Container Apps / Cloud Run | "all the information needed to process a request is contained in the request itself" ([base protocol](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md)) |
| Fleet governance, SSO, audit | Kubernetes + gateway (e.g. ToolHive) | "Centralize control of security policy, authentication, authorization, auditing" ([toolhive README](https://github.com/stacklok/toolhive)) |
| Public discovery | MCP Registry `remotes` | "A remote server **MUST** be publicly accessible at its specified URL" ([registry docs](https://modelcontextprotocol.io/registry/remote-servers)) |

---

## 11. Retrieval log

| URL | Result |
| - | - |
| https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md | Retrieved |
| https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio.md | Retrieved |
| https://modelcontextprotocol.io/registry/remote-servers | Retrieved |
| https://docs.docker.com/ai/docker-agent/features/remote-mcp | Retrieved |
| https://builder.aws.com/content/2s44xHTSbQgo2Ws2bJr6hZsECGr/building-a-serverless-remote-mcp-server-on-aws-part-1 | **Direct fetch failed (empty response, twice).** Content obtained via web search index; cited as SOURCE CLAIM. |
| https://www.serverless.com/blog/deploy-mcp-servers-on-aws-lambda-with-serverless-framework-v4 | **Direct fetch failed (footer only).** Content obtained via web search index; cited as SOURCE CLAIM. |
| https://developers.cloudflare.com/agents/ | Retrieved |
| https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550 | **Direct fetch failed (title only).** Content obtained via web search index; cited as SOURCE CLAIM. |
| https://github.com/stacklok/toolhive | Retrieved |
| https://cloud.google.com/run/docs | Retrieved (generic Cloud Run docs; MCP-specific pages found via search) |
| https://docs.cloud.google.com/run/docs/host-mcp-servers | Retrieved via search |
| https://docs.cloud.google.com/run/docs/tutorials/deploy-remote-mcp-server | Retrieved via search |
| https://docs.cloud.google.com/run/docs/use-cloud-run-mcp | Retrieved via search |
| https://learn.microsoft.com/en-us/azure/container-apps/mcp-overview | Retrieved via search |
| https://learn.microsoft.com/en-us/azure/container-apps/mcp-choosing-azure-service | Retrieved via search |
| https://developers.cloudflare.com/agents/model-context-protocol/guides/remote-mcp-server/ | Retrieved via search |
| https://github.com/modelcontextprotocol/mcpb/blob/main/README.md | Retrieved via search |
| https://blog.modelcontextprotocol.io/posts/2025-11-20-adopting-mcpb | Retrieved via search |
| https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md | Retrieved |
| https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/recipes | Retrieved |
| https://modelcontextprotocol.io/docs/2026-07-28/develop/connect-local-servers | Retrieved |
| https://modelcontextprotocol.io/docs/2026-07-28/develop/connect-remote-servers | Retrieved |
| https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging | Retrieved |
| https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices | Retrieved |
