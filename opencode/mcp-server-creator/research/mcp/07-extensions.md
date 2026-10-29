# MCP Extensions: Official Model and Named Extensions

Research file. Retrieved: 2026-10-02. Current protocol revision referenced throughout: **2026-07-28**.

## Notation and evidence ranking

- **SOURCE FACT** — a normative statement quoted verbatim from an official specification/SEP or official documentation page.
- **SOURCE CLAIM (Rank N)** — a non-normative statement quoted verbatim. Ranks: **Rank A** = Final/Standards-Track SEP or normative specification text; **Rank B** = official documentation page (editorial guidance); **Rank C** = community-maintained content on an official page.
- **AI INFERENCE** — my reasoning that names the specific quoted facts it is derived from.
- **PLAUSIBLE NOT VERIFIED** — a conjecture consistent with sources but not directly stated.
- **UNKNOWN** — no source retrieved or source is silent.

Quotations are short and exact. Every externally sourced fact carries an inline link to the source URL. No end-only bibliography is used. All twelve requested URLs for this file were retrieved successfully; there are no failed retrievals for FILE 1.

## 1. What an MCP extension is

**SOURCE FACT.** "MCP extensions are optional additions to the specification that define capabilities beyond the core protocol." ([Extensions Overview](https://modelcontextprotocol.io/extensions/overview))

**SOURCE FACT.** Extensions are categorized as "modular (e.g., distinct features like authentication), specialized (e.g., industry-specific logic), or experimental (e.g., features being incubated for potential core inclusion)." ([Extensions Overview](https://modelcontextprotocol.io/extensions/overview))

**SOURCE FACT.** The defining SEP states: "An MCP extension is an optional addition to the specification that defines capabilities beyond the core protocol." ([SEP-2133: Extensions](https://modelcontextprotocol.io/seps/2133-extensions))

**SOURCE CLAIM (Rank A).** SEP-2133 metadata: **SEP** 2133, **Title** "Extensions", **Status Final**, **Type Standards Track**, **Created** 2025-01-21, **Author(s)** "Peter Alexander ([@pja-ant](https://github.com/pja-ant))", **Sponsor** "None (seeking sponsor)", **PR** [#2133](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2133). ([SEP-2133: Extensions](https://modelcontextprotocol.io/seps/2133-extensions))

**SOURCE FACT.** SEP-2133's abstract: "This SEP establishes a lightweight framework for extending the Model Context Protocol through optional, composable extensions." ([SEP-2133: Extensions](https://modelcontextprotocol.io/seps/2133-extensions))

## 2. Extension identifiers and the reverse-DNS naming rule

**SOURCE FACT.** "Extensions are identified using a unique *extension identifier* with the format: `{vendor-prefix}/{extension-name}`, e.g. `io.modelcontextprotocol/oauth-client-credentials`." ([Extensions Overview](https://modelcontextprotocol.io/extensions/overview))

**SOURCE FACT.** "Identifiers follow the same rules as [`_meta` keys](https://modelcontextprotocol.io/specification/draft/basic/index#meta), with a mandatory prefix. Official extensions use the `io.modelcontextprotocol` vendor prefix." ([Extensions Overview](https://modelcontextprotocol.io/extensions/overview))

**SOURCE FACT.** "If you're building a third-party extension, use a reversed domain name you own as the vendor prefix to avoid collisions (similar to Java package naming). For example, a company owning `example.com` would use `com.example/` as their prefix (e.g., `com.example/my-extension`)." ([Extensions Overview](https://modelcontextprotocol.io/extensions/overview))

**SOURCE FACT.** SEP-2133 adds the normative form: "The names follow the same rules as the [_meta keys](https://modelcontextprotocol.io/specification/draft/basic/index#meta), except that the prefix is mandatory." ([SEP-2133: Extensions](https://modelcontextprotocol.io/seps/2133-extensions))

**SOURCE FACT.** "To prevent identifier collisions, the vendor prefix SHOULD be a reversed domain name that the extension author owns or controls (similar to Java package naming conventions)." ([SEP-2133: Extensions](https://modelcontextprotocol.io/seps/2133-extensions))

**SOURCE FACT.** "Breaking changes MUST use a new identifier, e.g. `io.modelcontextprotocol/oauth-client-credentials-v2`. A breaking change is any modification that would cause existing compliant implementations to fail or behave incorrectly, including: removing or renaming fields, changing field types, altering the semantics of existing behavior, or adding new required fields." ([SEP-2133: Extensions](https://modelcontextprotocol.io/seps/2133-extensions))

**AI INFERENCE (from the identifier-format and prefix facts above).** The reverse-DNS prefix mirrors Java package naming so that independently authored extensions cannot collide on `{extension-name}`; the mandatory prefix makes the namespace globally scoped rather than local. This is stated as intent in SEP-2133 ("To prevent identifier collisions…"), so the inference is direct.

## 3. Official extension repositories, experimental extensions, and lifecycle

**SOURCE FACT.** "Official extensions live inside the [Model Context Protocol GitHub organization](https://github.com/modelcontextprotocol/) in repositories with the `ext-` prefix." ([Extensions Overview](https://modelcontextprotocol.io/extensions/overview))

**SOURCE FACT.** "Experimental extensions provide an incubation pathway for [Working Groups and Interest Groups](https://modelcontextprotocol.io/community/working-interest-groups) to prototype ideas and collaborate on extension concepts before formal SEP submission." ([Extensions Overview](https://modelcontextprotocol.io/extensions/overview))

**SOURCE FACT.** "Experimental extension repositories live within the MCP GitHub organization with the `experimental-ext-` prefix (e.g., `experimental-ext-interceptors`)." ([Extensions Overview](https://modelcontextprotocol.io/extensions/overview))

**SOURCE FACT.** The official lifecycle is stated as: "**Propose**: Create a SEP in the main MCP repository using the [standard SEP guidelines](https://modelcontextprotocol.io/community/sep-guidelines) with type **Extensions Track**." followed by "**Implement**: Build at least one reference implementation in an official SDK — this is required before the SEP can be reviewed." ([Extensions Overview](https://modelcontextprotocol.io/extensions/overview))

**SOURCE FACT.** "Extension specifications need to use RFC 2119 language (MUST, SHOULD, MAY)" and "Extensions must have an associated working group or interest group". ([Extensions Overview](https://modelcontextprotocol.io/extensions/overview))

**SOURCE FACT.** SEP-2133 requires licensing: "Official extensions MUST be available under the Apache 2.0 license." ([SEP-2133: Extensions](https://modelcontextprotocol.io/seps/2133-extensions))

**SOURCE FACT.** SEP-2133: "Extension SEPs: … MUST have at least one reference implementation in an official SDK prior to review to ensure the extension is practical and implementable." ([SEP-2133: Extensions](https://modelcontextprotocol.io/seps/2133-extensions))

**SOURCE FACT.** SEP-2133 defers several design areas: "**Schema**: we do not specify a mechanism for extensions to advertise how they modify the schema." plus "**Dependencies** …" and "**Profiles** …". ([SEP-2133: Extensions](https://modelcontextprotocol.io/seps/2133-extensions))

**AI INFERENCE (from the identifiers and lifecycle facts).** Because SEP-2133 explicitly leaves schema, dependencies, and profiles unspecified, an extension cannot currently declare machine-readable version dependencies on the core protocol or on other extensions; interoperability beyond the settings object must be arranged out of band. This follows from the quoted "Not Specified" list.

## 4. Capability negotiation via the `extensions` field

**SOURCE FACT.** "Clients and servers advertise their support for extensions in the `extensions` field within their respective capability declarations." ([Extensions Overview](https://modelcontextprotocol.io/extensions/overview))

**SOURCE FACT.** "Clients advertise extension support in `_meta[\"io.modelcontextprotocol/clientCapabilities\"]` within each request". The example places the extension map under `clientCapabilities.extensions`, e.g. `"io.modelcontextprotocol/ui": { "mimeTypes": ["text/html;profile=mcp-app"] }`, alongside `"io.modelcontextprotocol/protocolVersion": "2026-07-28"`. ([Extensions Overview](https://modelcontextprotocol.io/extensions/overview))

**SOURCE FACT.** "Servers advertise extension support in the `server/discover` response". The example shows `"capabilities": { "tools": {}, "extensions": { "io.modelcontextprotocol/ui": {} } }` plus `"supportedVersions": ["2026-07-28"]`. ([Extensions Overview](https://modelcontextprotocol.io/extensions/overview))

**SOURCE FACT.** "Each extension specifies the schema of its settings object; an empty object indicates no settings." ([Extensions Overview](https://modelcontextprotocol.io/extensions/overview))

**SOURCE FACT.** Graceful degradation: "If one side supports an extension but the other doesn't, the supporting side needs to either fall back to core protocol behavior or reject the request with an appropriate error if the extension is mandatory." ([Extensions Overview](https://modelcontextprotocol.io/extensions/overview))

**SOURCE FACT.** The official docs add: "It's a good practice to document expected fallback behavior in your extension. For example, a server offering UI-enhanced tools should still return meaningful text content for clients that don't support the UI extension." ([Extensions Overview](https://modelcontextprotocol.io/extensions/overview))

**SOURCE FACT.** "Extensions are always disabled by default and require explicit opt-in from the developer." ([Extensions Overview](https://modelcontextprotocol.io/extensions/overview))

**SOURCE FACT.** "SDKs can choose to implement extensions, but it's not required for protocol conformance. SDK maintainers have full autonomy over which extensions they support." ([Extensions Overview](https://modelcontextprotocol.io/extensions/overview))

**SOURCE FACT.** SEP-2133 normative form: "SDKs MAY implement extensions. Where implemented, extensions MUST be disabled by default and require explicit opt-in. SDK documentation SHOULD list supported extensions." ([SEP-2133: Extensions](https://modelcontextprotocol.io/seps/2133-extensions))

**PUBLISHED NOTE (historical difference).** SEP-2133 was written against the `2025-06-18` protocol and negotiated through `initialize`, not the `2026-07-28` per-request `clientCapabilities`/`server/discover` flow. Its examples show `"method": "initialize"` with `"protocolVersion": "2025-06-18"`. ([SEP-2133: Extensions](https://modelcontextprotocol.io/seps/2133-extensions)) **AI INFERENCE (from that contrast and the Extensions Overview).** The current negotiated location for the `extensions` map moved from the `initialize` handshake to per-request `_meta` client capabilities and the `server/discover` response; the historical SEP text was not updated, consistent with its own banner that "Changes made to the protocol after finalization are not reflected here."

## 5. Extension evolution and breaking changes

**SOURCE FACT.** "Extensions evolve independently of the core protocol. Updates are managed by the extension repository maintainers and don't require core maintainer review." ([Extensions Overview](https://modelcontextprotocol.io/extensions/overview))

**SOURCE FACT.** "When you need to change an extension, prefer using capability flags or versioning within the extension settings object rather than creating a new extension identifier. If a breaking change is unavoidable, use a new identifier (e.g., `io.modelcontextprotocol/my-extension-v2`)." ([Extensions Overview](https://modelcontextprotocol.io/extensions/overview))

**SOURCE FACT.** "Extensions SHOULD be versioned, but exact versioning approach is not specified here." ([SEP-2133: Extensions](https://modelcontextprotocol.io/seps/2133-extensions))

**SOURCE FACT.** Security: "Extensions MUST implement all related security best practices in the area that they extend. Clients and servers SHOULD treat any new fields or data introduced as part of an extension as untrusted and SHOULD comprehensively validate them." ([SEP-2133: Extensions](https://modelcontextprotocol.io/seps/2133-extensions))

## 6. Official extension inventory

**SOURCE FACT.** The overview lists four official extension areas: "**MCP Authorization Extensions**" (`ext-auth`), "**MCP Apps**" (`ext-apps`), "**MCP Tasks**", and "**Skills over MCP**" (`ext-skills`). ([Extensions Overview](https://modelcontextprotocol.io/extensions/overview))

### 6.1 MCP Apps (`io.modelcontextprotocol/ui`)

**SOURCE FACT.** Identifier: "MCP Apps | `io.modelcontextprotocol/ui` | Interactive HTML interfaces rendered inline in the conversation". ([Extension Support Matrix](https://modelcontextprotocol.io/extensions/client-matrix))

**SOURCE FACT.** Purpose: "MCP Apps let servers return interactive HTML interfaces (data visualizations, forms, dashboards) that render directly in the chat." ([MCP Apps](https://modelcontextprotocol.io/extensions/apps/overview))

**SOURCE FACT.** "The core pattern combines two MCP primitives: a tool that declares a UI resource in its description, plus a UI resource that renders data as an interactive HTML interface." ([MCP Apps](https://modelcontextprotocol.io/extensions/apps/overview))

**SOURCE FACT.** "The tool description includes a `_meta.ui.resourceUri` field pointing to a `ui://` resource." ([MCP Apps](https://modelcontextprotocol.io/extensions/apps/overview))

**SOURCE FACT.** "MCP Apps run in a sandboxed [iframe](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe) … The sandbox prevents your app from accessing the parent window's DOM, reading the host's cookies or local storage, navigating the parent page, or executing scripts in the parent context." ([MCP Apps](https://modelcontextprotocol.io/extensions/apps/overview))

**SOURCE FACT.** "The initial specification focuses on HTML resources (`text/html;profile=mcp-app`) with a clear path for future extensions." ([SEP-1865: MCP Apps - Interactive User Interfaces for MCP](https://modelcontextprotocol.io/seps/1865-mcp-apps-interactive-user-interfaces-for-mcp))

**SOURCE FACT.** Build guide path: the fastest setup uses the `create-mcp-app` skill; the server registers a tool with `_meta: { ui: { resourceUri } }` and registers a resource with `RESOURCE_MIME_TYPE`, while the UI uses the `App` class from `@modelcontextprotocol/ext-apps`. ([Build an MCP App](https://modelcontextprotocol.io/extensions/apps/build))

**SOURCE CLAIM (Rank A).** SEP-1865 metadata: **SEP** 1865, **Title** "MCP Apps - Interactive User Interfaces for MCP", **Status Final**, **Type Extensions Track**, **Created** 2025-11-21, nine named authors including Ido Salomon and Liad Yosef, **PR** [#1865](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/1865). ([SEP-1865](https://modelcontextprotocol.io/seps/1865-mcp-apps-interactive-user-interfaces-for-mcp))

**SOURCE FACT.** Security rationale from the SEP: "**Iframe sandboxing**: All UI content runs in sandboxed iframes with restricted permissions"; "**Predeclared templates**: Hosts can review HTML content before rendering"; "**Auditable messages**: All UI-to-host communication goes through loggable JSON-RPC"; "**User consent**: Hosts can require explicit approval for UI-initiated tool calls". ([SEP-1865](https://modelcontextprotocol.io/seps/1865-mcp-apps-interactive-user-interfaces-for-mcp))

### 6.2 Authorization extensions

**SOURCE FACT.** "The [ext-auth repository](https://github.com/modelcontextprotocol/ext-auth) contains official MCP extensions that add authorization capabilities beyond the core MCP specification." ([Authorization Extensions](https://modelcontextprotocol.io/extensions/auth/overview))

**SOURCE FACT.** Motivation: "**Machine-to-machine integrations** don't have a human in the loop." and "**Enterprise environments** often have centralized identity providers (IdPs) that enforce policy across all applications." ([Authorization Extensions](https://modelcontextprotocol.io/extensions/auth/overview))

**SOURCE FACT.** Choosing guidance: "Standard interactive user authorization | Core MCP spec (no extension needed)". ([Authorization Extensions](https://modelcontextprotocol.io/extensions/auth/overview))

#### OAuth Client Credentials (`io.modelcontextprotocol/oauth-client-credentials`)

**SOURCE FACT.** "The OAuth Client Credentials extension (`io.modelcontextprotocol/oauth-client-credentials`) adds support for the [OAuth 2.0 client credentials flow](https://datatracker.ietf.org/doc/html/rfc6749#section-4.4) to MCP." ([OAuth Client Credentials](https://modelcontextprotocol.io/extensions/auth/oauth-client-credentials))

**SOURCE FACT.** "The authorization server validates the signature using the client's registered public key." JWT Bearer Assertions are described as "recommended" and "Defined in [RFC 7523](https://datatracker.ietf.org/doc/html/rfc7523)". ([OAuth Client Credentials](https://modelcontextprotocol.io/extensions/auth/oauth-client-credentials))

**SOURCE FACT.** Security warning: "Client secrets are **long-lived credentials** that grant access without user interaction. If a secret is leaked, an attacker can silently authenticate as your application until the secret is rotated." ([OAuth Client Credentials](https://modelcontextprotocol.io/extensions/auth/oauth-client-credentials))

#### Enterprise-Managed Authorization (`io.modelcontextprotocol/enterprise-managed-authorization`)

**SOURCE FACT.** "The Enterprise-Managed Authorization extension (`io.modelcontextprotocol/enterprise-managed-authorization`) enables organizations to control MCP server access centrally through their existing identity provider (IdP)." ([Enterprise-Managed Authorization](https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization))

**SOURCE FACT.** "The MCP Client requests a special type of token from the enterprise IdP called an Identity Assertion JWT Authorization Grant, or ID-JAG. The MCP Client then exchanges the ID-JAG for an access token from the MCP server's Authorization Server". ([Enterprise-Managed Authorization](https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization))

**SOURCE FACT.** "ID-JAG tokens will always contain a subject claim and may additionally contain an email claim that can be used to link the enterprise identity to an existing account in your system." ([Enterprise-Managed Authorization](https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization))

**SOURCE FACT.** Related SEP link: "Original proposal: Enable Enterprise IdP Policy Controls" → [SEP-990](https://modelcontextprotocol.io/seps/990-enable-enterprise-idp-policy-controls-during-mcp-o). ([Enterprise-Managed Authorization](https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization))

### 6.3 MCP Tasks (`io.modelcontextprotocol/tasks`)

**SOURCE FACT.** "MCP Tasks let servers return a durable handle instead of blocking, so clients can poll for progress, provide input when needed, and retrieve the final result after reconnecting." ([Tasks](https://modelcontextprotocol.io/extensions/tasks/overview))

**SOURCE FACT.** "The server decides per-request whether to create a task. Clients opt in once via the extension capability and handle whichever result shape arrives. No per-tool warmup or per-request flag." ([Tasks](https://modelcontextprotocol.io/extensions/tasks/overview))

**SOURCE FACT.** Lifecycle statuses: "`working`", "`input_required`", "`completed`", "`failed`", "`cancelled`". ([Tasks](https://modelcontextprotocol.io/extensions/tasks/overview))

**SOURCE FACT.** "When a server decides a request will be long-running, it returns a task handle instead of the final result." ([Tasks](https://modelcontextprotocol.io/extensions/tasks/overview))

**SOURCE FACT.** Protocol methods introduced: "The extension introduces three methods: `tasks/get`, `tasks/update`, and `tasks/cancel`; a polymorphic-result discriminator (`resultType: \"task\"`); and a `Task` shape". ([SEP-2663: Tasks Extension](https://modelcontextprotocol.io/seps/2663-tasks-extension))

**SOURCE FACT.** "This extension is identified as: `io.modelcontextprotocol/tasks`." ([SEP-2663](https://modelcontextprotocol.io/seps/2663-tasks-extension))

**SOURCE FACT.** Forward intent: "Tasks will become a foundational building block of MCP and are expected to be supported in future protocol versions." ([SEP-2663](https://modelcontextprotocol.io/seps/2663-tasks-extension))

**SOURCE FACT.** Compatibility: "The experimental `tasks` feature in the `2025-11-25` specification served as a stopgap until the protocol's extension mechanism was available." ([SEP-2663](https://modelcontextprotocol.io/seps/2663-tasks-extension))

**SOURCE CLAIM (Rank A).** SEP-2663 metadata: **SEP** 2663, **Title** "Tasks Extension", **Status Final**, **Type Extensions Track**, **Created** 2026-04-27, **Author(s)** "Luca Chang ([@LucaButBoring](https://github.com/LucaButBoring)), Caitie McCaffrey ([@CaitieM20](https://github.com/CaitieM20)); on behalf of the Agents Working Group", **Sponsor** Caitie McCaffrey, **PR** [#2663](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2663). ([SEP-2663](https://modelcontextprotocol.io/seps/2663-tasks-extension))

**SOURCE FACT.** Cancellation semantics: "A server is not obligated to actually stop the work; it is only obligated to acknowledge the request." ([SEP-2663](https://modelcontextprotocol.io/seps/2663-tasks-extension))

**SOURCE FACT.** Missing-capability error: the server returns error with code `-32021` (Missing Required Client Capability) naming the required extension. ([SEP-2663](https://modelcontextprotocol.io/seps/2663-tasks-extension))

**SOURCE FACT.** Sacred prefixes: "The `tasks/` method prefix and `notifications/tasks/` notification prefix are reserved for this extension." ([SEP-2663](https://modelcontextprotocol.io/seps/2663-tasks-extension))

### 6.4 Skills over MCP (`io.modelcontextprotocol/skills`)

**SOURCE FACT.** "The [ext-skills repository](https://github.com/modelcontextprotocol/ext-skills) contains the published specification for the official Skills extension (`io.modelcontextprotocol/skills`). [SEP-2640](https://modelcontextprotocol.io/seps/2640-skills-extension) is Final." ([Skills](https://modelcontextprotocol.io/extensions/skills/overview))

**SOURCE FACT.** "The Skills extension allows MCP servers to expose workflow instructions and supporting files to clients." ([Skills](https://modelcontextprotocol.io/extensions/skills/overview))

**SOURCE FACT.** "A skill is a directory containing a `SKILL.md` file and optional supporting files, following the [Agent Skills specification](https://agentskills.io/specification)." ([Skills](https://modelcontextprotocol.io/extensions/skills/overview))

**SOURCE FACT.** "Servers that declare this extension **MUST** implement `skills/list` and `skills/get`. Skill files are served through `resources/read`." ([Skills](https://modelcontextprotocol.io/extensions/skills/overview))

**SOURCE FACT.** Optional setting: "The optional `directoryRead` setting indicates support for `resources/directory/read` and defaults to `false`." ([Skills](https://modelcontextprotocol.io/extensions/skills/overview))

**SOURCE FACT.** "Servers that support Skills **MUST** declare both the `resources` capability and the `io.modelcontextprotocol/skills` extension in [`server/discover`](https://modelcontextprotocol.io/specification/draft/server/discover)". ([Skills](https://modelcontextprotocol.io/extensions/skills/overview))

**SOURCE FACT.** The SEP calls itself "a convention for serving [Agent Skills](https://agentskills.io/) over MCP using the existing Resources primitive." ([SEP-2640: Skills Extension](https://modelcontextprotocol.io/seps/2640-skills-extension))

**SOURCE CLAIM (Rank A).** SEP-2640 metadata: **SEP** 2640, **Title** "Skills Extension", **Status Final**, **Type Extensions Track**, **Created** 2026-04-23, **Author(s)** Peter Alexander, Ola Hungerford, Sambhav Kothari, Aditya Kumar "on behalf of the Skills Over MCP Working Group", **Sponsor** @pja-ant, **PR** [#2640](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2640). ([SEP-2640](https://modelcontextprotocol.io/seps/2640-skills-extension))

**SOURCE FACT.** Limits: "This extension fixes two per-skill limits": "Resources per skill | 512 entries" and "Total file size per skill | 16 MiB (16,777,216 bytes)". ([SEP-2640](https://modelcontextprotocol.io/seps/2640-skills-extension))

**SOURCE FACT.** Integrity model: "Digests are SHA-256 hashes of an artifact's raw bytes, formatted as `sha256:{hex}`." ([SEP-2640](https://modelcontextprotocol.io/seps/2640-skills-extension))

**SOURCE FACT.** But integrity is not trust: "Digests are unsigned and supplied by the same server that supplies the content. A match proves the two are consistent, not that either is trustworthy." ([SEP-2640](https://modelcontextprotocol.io/seps/2640-skills-extension))

**SOURCE FACT.** The ext-skills docs add security requirements: "Hosts **MUST NOT** retrieve files ahead of need, including on connection, listing, or approval." ([Skills](https://modelcontextprotocol.io/extensions/skills/overview))

## 7. How extension support is tracked: the client matrix

**SOURCE CLAIM (Rank C — community-maintained).** "This matrix shows which MCP clients support each [official extension](https://modelcontextprotocol.io/extensions/overview)." and "This list is maintained by the community." ([Extension Support Matrix](https://modelcontextprotocol.io/extensions/client-matrix))

**SOURCE FACT.** The matrix's extension overview table lists identifiers `io.modelcontextprotocol/ui`, `io.modelcontextprotocol/oauth-client-credentials`, `io.modelcontextprotocol/enterprise-managed-authorization`, and `io.modelcontextprotocol/skills`. ([Extension Support Matrix](https://modelcontextprotocol.io/extensions/client-matrix))

**SOURCE CLAIM (Rank C).** As of retrieval, MCP Apps shows support from Claude (web), Claude Desktop, VS Code GitHub Copilot, Microsoft 365 Copilot, Goose, Postman, MCPJam, ChatGPT, Cursor, Archestra.AI, and PostHog Code; OAuth Client Credentials and Enterprise Auth show `mcpc MCP CLI` (and Archestra.AI for enterprise); Skills shows Partial support for ChatGPT, fast-agent, and MCP Inspector, plus `mcpc MCP CLI`. ([Extension Support Matrix](https://modelcontextprotocol.io/extensions/client-matrix))

**SOURCE FACT.** "Extensions are always opt-in: a client only uses an extension if both client and server declare support in the `extensions` field of their [capabilities](https://modelcontextprotocol.io/extensions/overview#negotiation)." ([Extension Support Matrix](https://modelcontextprotocol.io/extensions/client-matrix))

**SOURCE CLAIM (Rank C).** "Auth extension support (OAuth Client Credentials and Enterprise-Managed Authorization) is tracked separately from the core MCP authorization features (DCR, CIMD)." ([Extension Support Matrix](https://modelcontextprotocol.io/extensions/client-matrix))

**SOURCE FACT.** "If you're building an MCP client and want to implement extension support: … Declare support in the `extensions` field of the `io.modelcontextprotocol/clientCapabilities` your client sends in each request's `_meta`, and read the server's `extensions` from its [`server/discover`](https://modelcontextprotocol.io/specification/draft/server/discover) response". ([Extension Support Matrix](https://modelcontextprotocol.io/extensions/client-matrix))

**UNKNOWN.** The matrix carries no retrieval or "last updated" timestamp, so the exact freshness of its support rows is not established by the page. ([Extension Support Matrix](https://modelcontextprotocol.io/extensions/client-matrix))

## 8. Consolidated identifier reference

| Extension | Identifier | SEP | SEP status |
| - | - | - | - |
| MCP Apps | `io.modelcontextprotocol/ui` | [1865](https://modelcontextprotocol.io/seps/1865-mcp-apps-interactive-user-interfaces-for-mcp) | Final, Extensions Track |
| OAuth Client Credentials | `io.modelcontextprotocol/oauth-client-credentials` | (no SEP number retrieved) | UNKNOWN |
| Enterprise-Managed Authorization | `io.modelcontextprotocol/enterprise-managed-authorization` | related [990](https://modelcontextprotocol.io/seps/990-enable-enterprise-idp-policy-controls-during-mcp-o) | UNKNOWN |
| Tasks | `io.modelcontextprotocol/tasks` | [2663](https://modelcontextprotocol.io/seps/2663-tasks-extension) | Final, Extensions Track |
| Skills | `io.modelcontextprotocol/skills` | [2640](https://modelcontextprotocol.io/seps/2640-skills-extension) | Final, Extensions Track |
| Extensions framework | (framework, not an extension) | [2133](https://modelcontextprotocol.io/seps/2133-extensions) | Final, Standards Track |

**UNKNOWN.** No SEP number for the OAuth Client Credentials extension or the Enterprise-Managed Authorization extension was present in the retrieved pages; the enterprise page links SEP-990 as the "Original proposal" only. ([OAuth Client Credentials](https://modelcontextprotocol.io/extensions/auth/oauth-client-credentials), [Enterprise-Managed Authorization](https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization))

## 9. Key takeaways

- **SOURCE FACT.** Extensions are optional and frameworked by identity + capability negotiation, not by a compiled-in core. ([Extensions Overview](https://modelcontextprotocol.io/extensions/overview))
- **SOURCE FACT.** The `{vendor-prefix}/{extension-name}` form with a mandatory reverse-DNS prefix is the collision-avoidance mechanism, and the official vendor prefix is `io.modelcontextprotocol`. ([SEP-2133](https://modelcontextprotocol.io/seps/2133-extensions))
- **AI INFERENCE (naming the above facts).** Because extension declarations live in `clientCapabilities` per request and in `server/discover`, and because extensions are opt-in and disabled by default, a server that makes an extension mandatory must be prepared to reject a non-declaring client with an explicit missing-capability error (as Tasks does with `-32021`). This chains the quoted negotiation, opt-in, and Tasks error facts.
- **SOURCE FACT.** Four named official extensions exist in the retrieved material: MCP Apps, two auth extensions, Tasks, and Skills; each has its own `ext-` repository. ([Extensions Overview](https://modelcontextprotocol.io/extensions/overview))
