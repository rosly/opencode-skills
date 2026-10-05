# Testing, Conformance, and CI for MCP Servers

Research note for the MCP server creator skill. Protocol revision under discussion: **2026-07-28**. Compiled 2026-10-03.

Notation used throughout:

- **SOURCE FACT** — official specification, official documentation, or official repository.
- **SOURCE CLAIM** — lower-tier source (vendor blog, community guide, search snippet); rank is stated.
- **AI INFERENCE** — a conclusion drawn by naming the quoted facts it rests on.
- **PLAUSIBLE NOT VERIFIED** — consistent with sources but not directly confirmed.
- **UNKNOWN** — no source found.

---

## 1. The test pyramid for MCP

The official documentation does not publish a single canonical "test pyramid", but the ecosystem converges on four layers. The strongest articulation is from Signadot, a vendor, so it is a SOURCE CLAIM (rank: vendor engineering blog, August 2026).

SOURCE CLAIM (vendor blog): "Testing an MCP server means verifying four different things: that each tool handler behaves correctly in isolation, that the server speaks the protocol correctly, that the tools work against the real systems they front, and that an AI agent can actually use them to complete tasks." ([Signadot, "How to Test MCP Servers"](https://www.signadot.com/testing-mcp-servers))

The same source names the four levels explicitly: "Level 1: Unit test the tool handlers", "Level 2: Exercise the protocol surface with the MCP Inspector", "Level 3: Integration test against real dependencies", and "Level 4: Agent evals" ([Signadot](https://www.signadot.com/testing-mcp-servers)).

A community guide by Hidekazu Konishi frames the same idea as three stacked layers — protocol, server logic, and client integration — and maps each to a primary verification tool. SOURCE CLAIM (rank: independent technical blog, first published 2026-06-14, updated 2026-08-20): "The single most useful idea for testing MCP servers is that a server is not one thing — it is three things stacked on top of each other, and each layer fails differently and is tested differently." ([Hidekazu Konishi, "MCP Server Testing and Debugging Guide"](https://hidekazu-konishi.com/entry/mcp_server_testing_and_debugging_guide.html))

AI INFERENCE: The official docs supply the tools for each layer (Inspector for protocol, in-memory transports for server logic, client logs for integration) but leave the pyramid framing to the ecosystem. The four-level model is therefore a synthesis, not a normative requirement.

### 1.1 Why MCP testing differs from API testing

SOURCE CLAIM (vendor blog): "The caller is a model, not a program." ([Signadot](https://www.signadot.com/testing-mcp-servers)) The same page adds that "correctness includes things no traditional test covers: whether the model picks the right tool for a task, whether an ambiguous description sends it down the wrong path, and whether a schema change silently changes agent behavior" ([Signadot](https://www.signadot.com/testing-mcp-servers)).

SOURCE CLAIM (independent blog): MCP servers "fail **silently**", because "a tool that is never selected, a schema that the client quietly rejects, a transport that drops a session after the first reconnect, an authorization handshake that returns the wrong status code — none of these raise a stack trace in your server process." ([Hidekazu Konishi](https://hidekazu-konishi.com/entry/mcp_server_testing_and_debugging_guide.html))

---

## 2. Unit and in-memory integration testing

The cleanest automated surface is an in-memory client/server pair. SOURCE CLAIM (independent blog): "Both official SDKs ship an in-memory transport for exactly this purpose." ([Hidekazu Konishi](https://hidekazu-konishi.com/entry/mcp_server_testing_and_debugging_guide.html))

### 2.1 TypeScript

SOURCE CLAIM (independent blog): "The TypeScript SDK exposes `InMemoryTransport`, whose static `createLinkedPair()` returns a connected pair of transports — one for the client, one for the server." ([Hidekazu Konishi](https://hidekazu-konishi.com/entry/mcp_server_testing_and_debugging_guide.html))

The same guide warns about version pinning: "The TypeScript SDK is being restructured into a multi-package layout, and the import path for `InMemoryTransport` ... differs between the established single-package line and the newer split packages" ([Hidekazu Konishi](https://hidekazu-konishi.com/entry/mcp_server_testing_and_debugging_guide.html)).

SOURCE FACT (official repo): The TypeScript SDK v2 is the stable line "implementing the [2026-07-28 MCP spec]", and it publishes split packages `@modelcontextprotocol/server` and `@modelcontextprotocol/client` ([modelcontextprotocol/typescript-sdk README](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/README.md)). The README's minimal server example imports `McpServer` from `@modelcontextprotocol/server` and `StdioServerTransport` from `@modelcontextprotocol/server/stdio` ([typescript-sdk README](https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/README.md)).

### 2.2 Python

SOURCE FACT (official repo): The Python SDK's high-level server is `MCPServer`, imported from `mcp.server`, and the in-memory client is `Client`, imported from `mcp` ([modelcontextprotocol/python-sdk README](https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md)). The README shows a client connecting to a URL: `async with Client("http://localhost:8000/mcp") as client:` ([python-sdk README](https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md)).

SOURCE CLAIM (independent blog): "The Python SDK provides an in-memory testing path: you construct a `Client` around your server object, and the SDK wires them together over an in-memory transport with no subprocess." ([Hidekazu Konishi](https://hidekazu-konishi.com/entry/mcp_server_testing_and_debugging_guide.html)) The same guide notes the `FastMCP` → `MCPServer` rename and warns that the older `create_connected_server_and_client_session(...)` helper "is not part of the current public SDK surface" ([Hidekazu Konishi](https://hidekazu-konishi.com/entry/mcp_server_testing_and_debugging_guide.html)).

### 2.3 What to assert

SOURCE CLAIM (independent blog): in-memory tests should assert "the tool/resource/prompt inventory", "the declared schema", "the happy path **and** the error path", and "capability honesty" ([Hidekazu Konishi](https://hidekazu-konishi.com/entry/mcp_server_testing_and_debugging_guide.html)). The guide's rationale for the inventory assertion: "This single assertion catches accidental additions and removals" ([Hidekazu Konishi](https://hidekazu-konishi.com/entry/mcp_server_testing_and_debugging_guide.html)).

SOURCE CLAIM (vendor blog): "Every tool handler has unit tests through an in-memory client, covering error paths and schema violations, running in CI." ([Signadot](https://www.signadot.com/testing-mcp-servers))

---

## 3. The MCP Inspector: manual and CLI

### 3.1 Three clients, one binary

SOURCE FACT (official docs): The Inspector "ships as a single package, `@modelcontextprotocol/inspector`, providing **three clients behind one binary**" — Web, CLI, and TUI ([MCP Inspector docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector)). The docs state the Inspector "requires **Node 22.19.0 or newer** and runs directly through `npx`" ([MCP Inspector docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector)).

SOURCE FACT (official repo): "All three run through one global `mcp-inspector` binary" ([modelcontextprotocol/inspector README](https://github.com/modelcontextprotocol/inspector)).

### 3.2 Inspector CLI for CI

SOURCE FACT (official docs): "Each CLI run connects to a server, invokes the single request you name with `--method`, prints the result, and exits." ([Inspector CLI docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/cli))

SOURCE FACT (official docs): "`--format json` emits a single JSON object on stdout with no banners, so the whole output pipes cleanly" ([Inspector CLI docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/cli)).

SOURCE FACT (official docs): "Every non-zero exit maps to a stable failure class, so a caller can branch on *why* without scraping prose" ([Inspector CLI docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/cli)). The documented exit codes are:

| Code | Meaning |
| - | - |
| `0` | Success. |
| `1` | Usage or unexpected error (the catch-all). |
| `2` | No MCP App found on the tool (`--app-info` probe). |
| `3` | Server requires authentication (401/403, `WWW-Authenticate`, OAuth). |
| `4` | Server unreachable (DNS, connection refused, timeout, `fetch failed`). |
| `5` | Tool error: `tools/call` returned `isError: true`, or the tool wasn't found. |

The table above is quoted from the [Inspector CLI docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/cli). The Inspector's own smoke-testing guide adds a sixth code: "`6` | `--strict` found an error-severity schema portability problem" ([Inspector smoke-testing guide](https://raw.githubusercontent.com/modelcontextprotocol/inspector/main/docs/cli-smoke-testing.md)).

SOURCE FACT (official docs): "On any non-zero exit the CLI also writes a **single JSON line to stderr**" ([Inspector CLI docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/cli)).

SOURCE FACT (official docs): For unattended runs, "`--stored-auth-only`: never start interactive OAuth or step-up, and never auto-open a browser." ([Inspector CLI docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/cli))

SOURCE FACT (official repo): "In CI, pin an exact version — `npx --yes @modelcontextprotocol/inspector@2.5.0 --cli …`. A range like `@2` is *not* a pin" ([Inspector smoke-testing guide](https://raw.githubusercontent.com/modelcontextprotocol/inspector/main/docs/cli-smoke-testing.md)).

SOURCE FACT (official repo): "`--method initialize` is a **connect-only probe**: it completes the handshake, prints `{serverInfo, protocolVersion, capabilities, instructions}`, and disconnects without invoking anything." ([Inspector smoke-testing guide](https://raw.githubusercontent.com/modelcontextprotocol/inspector/main/docs/cli-smoke-testing.md))

SOURCE FACT (official repo): The `--strict` flag "names those constructs — path, issue, and a concrete fix — and exits `6` when any is error-severity" ([Inspector smoke-testing guide](https://raw.githubusercontent.com/modelcontextprotocol/inspector/main/docs/cli-smoke-testing.md)).

### 3.3 A CI recipe

SOURCE FACT (official docs) gives this CI verification recipe:

```bash
set -euo pipefail
mcp-inspector --cli --config ./ci-servers.json --server my-server \
  --stored-auth-only --method tools/list --format json \
  | jq -e '.result.tools | map(.name) | index("get_weather")' > /dev/null
```

([Inspector CLI docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/cli))

SOURCE CLAIM (independent blog) proposes a four-check pipeline ordered cheapest-first: "1. **In-memory unit and integration tests.** ... 2. **A tool-list (and schema) snapshot.** ... 3. **A client-integration smoke test.** ... 4. **A protocol-version matrix.**" ([Hidekazu Konishi](https://hidekazu-konishi.com/entry/mcp_server_testing_and_debugging_guide.html)). The guide's snapshot rationale: "a renamed tool, a removed parameter, or a tightened schema is a breaking change for every agent that depends on the server" ([Hidekazu Konishi](https://hidekazu-konishi.com/entry/mcp_server_testing_and_debugging_guide.html)).

---

## 4. Conformance test suites and SDK scoring

### 4.1 The conformance repository

SOURCE FACT (official repo): "A framework for testing MCP (Model Context Protocol) client and server implementations against the specification." ([modelcontextprotocol/conformance README](https://github.com/modelcontextprotocol/conformance))

SOURCE FACT (official repo): The framework tests clients and servers separately. For servers, it "Connecting to the running server as an MCP client", "Sending test requests and capturing responses", and "Running conformance checks against server behavior" ([conformance README](https://github.com/modelcontextprotocol/conformance)).

SOURCE FACT (official repo): "Every scenario also validates each JSON-RPC message on the wire against the spec's JSON schema for the negotiated spec version" ([conformance README](https://github.com/modelcontextprotocol/conformance)).

SOURCE FACT (official repo): The `--requirements <revision>` flag "Run exactly what a spec revision requires, frozen at its release" ([conformance README](https://github.com/modelcontextprotocol/conformance)). The README explains why: "`--suite` and `--spec-version` describe the suite as it is today. Neither answers 'which scenarios did I need to pass to conform to the spec released on 2026-07-28', because the suite keeps growing" ([conformance README](https://github.com/modelcontextprotocol/conformance)).

SOURCE FACT (official repo): "Scenarios run at their revision's wire version. ... the dated revisions through `2025-11-25` use the stateful initialize handshake and `2026-07-28` is stateless with per-request `_meta`, and a scenario emits different checks under each." ([conformance README](https://github.com/modelcontextprotocol/conformance))

### 4.2 Expected-failures baselines

SOURCE FACT (official repo): "SDKs that don't yet pass all conformance tests can specify a baseline of known failures. This allows running conformance tests in CI without failing, while still catching regressions." ([conformance README](https://github.com/modelcontextprotocol/conformance)) The exit-code contract is:

| Scenario Result | In Baseline? | Outcome |
| - | - | - |
| Fails | Yes | Exit 0 — expected failure |
| Fails | No | Exit 1 — unexpected regression |
| Passes | Yes | Exit 1 — stale baseline, remove the entry |
| Passes | No | Exit 0 — normal pass |

(quoted from the [conformance README](https://github.com/modelcontextprotocol/conformance))

SOURCE FACT (official repo): "A scenario is many checks — `server-stateless` alone is over twenty — so baselining the whole scenario to excuse one of them stops enforcing the other nineteen." ([conformance README](https://github.com/modelcontextprotocol/conformance)) The workaround is a per-check entry `scenario:check-id` ([conformance README](https://github.com/modelcontextprotocol/conformance)).

### 4.3 How SDKs are scored

SOURCE FACT (official docs): The SDK Tiering System classifies SDKs into three tiers, and "All SDKs are evaluated using [automated conformance tests](https://github.com/modelcontextprotocol/conformance) that validate protocol support against the published specifications." ([SDK Tiering System](https://modelcontextprotocol.io/community/sdk-tiers))

SOURCE FACT (official docs): "**Tier 1**: 100% conformance required; **Tier 2**: 80% conformance required; **Tier 3**: No minimum requirement" ([SDK Tiering System](https://modelcontextprotocol.io/community/sdk-tiers)).

SOURCE FACT (official docs): Conformance scores exclude non-applicable tests: "Tests for the specification version the SDK targets", "Excluding tests marked as pending or skipped", "Excluding tests for experimental features", and "Excluding tests labeled `disputed` in the conformance repository, until the dispute is resolved" ([SDK Tiering System](https://modelcontextprotocol.io/community/sdk-tiers)).

SOURCE FACT (official docs): "An SDK may be moved to a lower tier if existing conformance tests on the latest stable release fail continuously for 4 weeks: **Tier 1 → Tier 2**: Any conformance test fails; **Tier 2 → Tier 3**: More than 20% of conformance tests fail" ([SDK Tiering System](https://modelcontextprotocol.io/community/sdk-tiers)).

SOURCE FACT (official repo): The `tier-check` subcommand "evaluates an MCP SDK repository against [SEP-1730] (the SDK Tiering System)" and "The exit code is a CI verdict on the machine-checkable half: nonzero when any scored conformance scenario fails or a leg could not be measured." ([conformance README](https://github.com/modelcontextprotocol/conformance))

SOURCE FACT (official repo): "`tier-check` takes several at once, and every one of them must pass for Tier 1" ([conformance README](https://github.com/modelcontextprotocol/conformance)).

### 4.4 SEP-2484: conformance tests required for Final SEPs

SOURCE FACT (official SEP): "Before a Standards Track SEP that changes observable protocol behavior can be marked `Final`, a conformance scenario covering its normative requirements must be merged into the conformance repository, accompanied by a structured traceability file mapping each MUST/MUST NOT and SHOULD/SHOULD NOT to a check or a documented exclusion." ([SEP-2484](https://modelcontextprotocol.io/seps/2484-conformance-tests-required-for-final-seps))

SOURCE FACT (official SEP): "Conformance tests are derived from and **subordinate to** the specification text. Where a test and the spec disagree, the spec is authoritative and the test is a bug." ([SEP-2484](https://modelcontextprotocol.io/seps/2484-conformance-tests-required-for-final-seps))

SOURCE FACT (official SEP): "SEP-1730 tier assessments are run against a **pinned conformance release version**, not the tip of the conformance repository." ([SEP-2484](https://modelcontextprotocol.io/seps/2484-conformance-tests-required-for-final-seps))

AI INFERENCE: SEP-2484 and the tiering system together mean a server author can treat the conformance suite as an executable, versioned definition of "correct" for a given revision, and can pin to a conformance release to avoid surprise regressions. This rests on the quoted "pinned conformance release version" and the "100% conformance required" facts.

---

## 5. Security testing vs. functional testing

SOURCE CLAIM (vendor blog, rank: security vendor marketing/technical blog, April 2026): "MCP Inspector does not automatically determine whether an implementation is secure. It does not independently validate controls such as per-client consent, token audience restrictions, token-passthrough prevention, scope minimization, SSRF defenses, command injection protections, or identity-based authorization." ([Aembit, "MCP Security Testing"](https://aembit.io/blog/mcp-security-testing))

SOURCE CLAIM (vendor blog): "If you test the Model Context Protocol (MCP) like a standard API, you'll miss the vulnerabilities attackers are most likely to exploit." ([Aembit](https://aembit.io/blog/mcp-security-testing))

SOURCE CLAIM (independent blog): "Treating 'passes the Inspector' as 'is safe.' ... functional testing answers 'does it work', not 'is it safe to trust' — a malicious or compromised server can be perfectly well-behaved on the wire." ([Hidekazu Konishi](https://hidekazu-konishi.com/entry/mcp_server_testing_and_debugging_guide.html))

SOURCE FACT (official docs): The security best-practices page enumerates attack classes including the confused deputy problem, token passthrough, SSRF, state handle hijacking, local MCP server compromise, OAuth authorization URL validation, mix-up attacks, localhost redirect URI impersonation, and scope minimization ([MCP Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices)).

SOURCE FACT (official docs): "MCP servers **MUST NOT** accept any tokens that were not explicitly issued for the MCP server." ([MCP Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices))

SOURCE FACT (official docs): "MCP servers that implement authorization **MUST** verify all inbound requests. MCP servers **MUST NOT** treat possession of a state handle as authentication." ([MCP Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices))

SOURCE CLAIM (vendor blog): "The MCP specification explicitly forbids token passthrough, where servers forward authentication tokens through intermediaries rather than validating them directly." ([Aembit](https://aembit.io/blog/mcp-security-testing))

SOURCE CLAIM (vendor blog): "The five mandatory authorization patterns each create testable requirements that generic scanners miss: Per-client consent ... Token audience validation ... Exact redirect URI matching ... OAuth state parameter validation." ([Aembit](https://aembit.io/blog/mcp-security-testing))

SOURCE CLAIM (independent blog) lists concrete authorization assertions: "An unauthenticated request **MUST** receive a `401 Unauthorized` whose `WWW-Authenticate` header points at the server's Protected Resource Metadata via a `resource_metadata` parameter", and "present a token whose audience is some **other** resource and assert the server rejects it with `401`" ([Hidekazu Konishi](https://hidekazu-konishi.com/entry/mcp_server_testing_and_debugging_guide.html)).

AI INFERENCE: Functional tests (in-memory, Inspector, conformance) and security tests are complementary and neither substitutes for the other. This follows from the quoted Aembit statement that the Inspector "does not automatically determine whether an implementation is secure" and the quoted Konishi statement that a correctness suite "does not replace a security review".

---

## 6. Common failure modes

### 6.1 Schema drift

SOURCE CLAIM (independent blog): "The most common server-logic failure is **drift between the declared input schema and the handler implementation**." ([Hidekazu Konishi](https://hidekazu-konishi.com/entry/mcp_server_testing_and_debugging_guide.html)) The guide explains: "If the schema says a field is optional but the handler dereferences it unconditionally, or the schema names a field `userId` but the handler reads `user_id`, the tool will fail at runtime in a way that no schema-level check catches." ([Hidekazu Konishi](https://hidekazu-konishi.com/entry/mcp_server_testing_and_debugging_guide.html))

SOURCE CLAIM (independent blog): "Schema drift is the single biggest argument for the integration tests in Section 4, which exercise the real handler against the real declared schema." ([Hidekazu Konishi](https://hidekazu-konishi.com/entry/mcp_server_testing_and_debugging_guide.html))

### 6.2 Capability mismatch

SOURCE CLAIM (independent blog): "The server advertises a capability in the `initialize` result — `tools`, `resources`, `prompts`, `logging` — but never actually implements the corresponding methods. Clients trust the advertised capabilities; an advertised-but-missing capability is a latent failure that only fires when the client first uses it." ([Hidekazu Konishi](https://hidekazu-konishi.com/entry/mcp_server_testing_and_debugging_guide.html))

SOURCE FACT (official docs): A server "**MUST NOT** rely on capabilities the client has not declared", and if a request needs an undeclared client capability the server "**MUST** return a `MissingRequiredClientCapabilityError` (`-32021`)" ([MCP base protocol overview](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md)).

### 6.3 Error-shape regressions

SOURCE CLAIM (independent blog): "A well-behaved server converts the failure into a structured tool result with an error indication rather than letting it collapse into a generic transport error. ... a structured error tells the model (and you) **what** went wrong; a generic `-32603 Internal error` tells nobody anything." ([Hidekazu Konishi](https://hidekazu-konishi.com/entry/mcp_server_testing_and_debugging_guide.html))

SOURCE FACT (official docs): The Inspector CLI treats a tool error as a distinct failure class: exit `5` means "`tools/call` returned `isError: true`, or the tool wasn't found" ([Inspector CLI docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/cli)).

### 6.4 stdout contamination on stdio

SOURCE FACT (official docs): "Local MCP servers should not log messages to stdout (standard out), as this will interfere with protocol operation." ([MCP Debugging docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging))

SOURCE FACT (official spec): "The server **MUST NOT** write anything to its `stdout` that is not a valid MCP message." ([stdio transport spec](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio.md))

SOURCE CLAIM (independent blog): "This is the single most common stdio failure: a stray `print()`, a library that logs to stdout, a debugging line left in — any of these corrupts the JSON-RPC stream and the client disconnects with a confusing parse error." ([Hidekazu Konishi](https://hidekazu-konishi.com/entry/mcp_server_testing_and_debugging_guide.html))

### 6.5 Protocol-version and header failures

SOURCE FACT (official docs): "An `UnsupportedProtocolVersionError` (`-32022`) lists the server's supported versions in its `data` field" ([MCP Debugging docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging)).

SOURCE FACT (official docs): "every request must carry `io.modelcontextprotocol/protocolVersion` and `io.modelcontextprotocol/clientCapabilities` ... A request missing either required field is rejected with error `-32602` (Invalid params)" ([MCP Debugging docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging)).

SOURCE FACT (official spec): On Streamable HTTP, "Every POST request to the MCP endpoint **MUST** include an `MCP-Protocol-Version` header", and "The header value **MUST** match the `io.modelcontextprotocol/protocolVersion` field carried in the request body's `_meta`." ([Streamable HTTP spec](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http.md))

### 6.6 Slow startup

SOURCE CLAIM (independent blog): "the server performs expensive work — downloading data, opening upstream connections — before it finishes `initialize`, and exceeds the client's startup timeout." ([Hidekazu Konishi](https://hidekazu-konishi.com/entry/mcp_server_testing_and_debugging_guide.html))

---

## 7. Observability during testing

SOURCE FACT (official docs): "Server logging: structured logs to stderr (stdio transport) or via [OpenTelemetry](https://opentelemetry.io/) (all transports)." ([MCP Debugging docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging))

SOURCE FACT (official docs): "The `notifications/message` mechanism below is deprecated as of protocol version `2026-07-28`. It remains available during the deprecation window." ([MCP Debugging docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging))

SOURCE FACT (official spec): The `_meta` keys `traceparent`, `tracestate`, and `baggage` are reserved for OpenTelemetry trace context propagation, and "When present, their values MUST follow [W3C Trace Context] and [W3C Baggage] formats respectively." ([MCP base protocol overview](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md))

SOURCE CLAIM (independent blog): "**Distributed tracing — OpenTelemetry spans, W3C trace-context propagation via `traceparent`/`tracestate`/`baggage` — is not part of the ratified MCP specification.**" ([Hidekazu Konishi](https://hidekazu-konishi.com/entry/mcp_server_testing_and_debugging_guide.html))

AI INFERENCE: The Konishi claim that trace context is "not part of the ratified MCP specification" is contradicted by the 2026-07-28 base protocol, which reserves the `traceparent`/`tracestate`/`baggage` keys. The likely explanation is that Konishi's guide was anchored to an earlier revision (it states "The current revision at the time of writing is `2025-11-25`"). Treat the official spec as authoritative here.

---

## 8. Practical checklist

AI INFERENCE, assembled from the quoted facts above:

1. Unit-test every tool handler through an in-memory client, asserting inventory, schema, happy path, error path, and capability honesty ([Hidekazu Konishi](https://hidekazu-konishi.com/entry/mcp_server_testing_and_debugging_guide.html)).
2. Snapshot `tools/list` (names and schemas) and diff it in CI ([Hidekazu Konishi](https://hidekazu-konishi.com/entry/mcp_server_testing_and_debugging_guide.html)).
3. Run an Inspector CLI smoke test against the built artifact with `--format json`, `--stored-auth-only`, and a pinned version ([Inspector smoke-testing guide](https://raw.githubusercontent.com/modelcontextprotocol/inspector/main/docs/cli-smoke-testing.md)).
4. Run the official conformance suite with `--requirements 2026-07-28` and a baseline file ([conformance README](https://github.com/modelcontextprotocol/conformance)).
5. Add negative assertions (refusals stay refusals) and a secret-shape scan ([Inspector smoke-testing guide](https://raw.githubusercontent.com/modelcontextprotocol/inspector/main/docs/cli-smoke-testing.md)).
6. Add security tests for token audience, per-client consent, SSRF, and scope minimization ([Aembit](https://aembit.io/blog/mcp-security-testing); [MCP Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices)).
7. Keep a small agent-eval suite to guard tool selection and chaining ([Signadot](https://www.signadot.com/testing-mcp-servers)).

---

## 9. Retrieval log

| URL | Result |
| - | - |
| https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector | Retrieved |
| https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging | Retrieved |
| https://github.com/modelcontextprotocol/inspector | Retrieved |
| https://modelcontextprotocol.io/community/sdk-tiers | Retrieved |
| https://modelcontextprotocol.io/seps/2484-conformance-tests-required-for-final-seps | Retrieved |
| https://github.com/modelcontextprotocol/conformance | Retrieved |
| https://hidekazu-konishi.com/entry/mcp_server_testing_and_debugging_guide.html | Retrieved (truncated; full text saved locally) |
| https://www.signadot.com/testing-mcp-servers | Retrieved |
| https://aembit.io/blog/mcp-security-testing | Retrieved |
| https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/cli | Retrieved |
| https://raw.githubusercontent.com/modelcontextprotocol/inspector/main/docs/cli-smoke-testing.md | Retrieved |
| https://raw.githubusercontent.com/modelcontextprotocol/conformance/main/SDK_INTEGRATION.md | Retrieved |
| https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices | Retrieved |
| https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md | Retrieved |
| https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md | Retrieved |
| https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/README.md | Retrieved |
