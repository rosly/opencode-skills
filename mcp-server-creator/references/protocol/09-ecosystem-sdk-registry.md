# MCP Ecosystem: SDKs and the Official MCP Registry

Research file for the MCP server creator report. Topic: the distribution ecosystem — official SDKs and their tiering system, and the official MCP Registry (what it is, how to publish, and the surrounding policy).

Protocol revision under study: **2026-07-28**. Research date: **2026-10-02**.

## Notation used in this file

- **SOURCE FACT** — a statement taken directly from an official primary source, quoted exactly and linked inline.
- **SOURCE CLAIM (rank)** — a claim made by a source, with a rank for how authoritative it is for the fact asserted. Ranks used here: `[primary/official]` (the MCP project's own docs/spec), `[primary/SEP]` (an accepted SEP), `[secondary]` (a third party).
- **AI INFERENCE** — a conclusion drawn by this research, naming the quoted facts it rests on.
- **PLAUSIBLE NOT VERIFIED** — a reasonable reading that the fetched sources do not directly confirm.
- **UNKNOWN** — the sources fetched do not answer the point, or retrieval failed.

---

## 1. Official SDKs and the SDK Tiering System

### 1.1 The official SDK list

**SOURCE FACT:** The official SDK page lists ten SDKs, each with a repository and a tier: TypeScript, Python, C#, Go, Rust, and Ruby are **Tier 1**; Java is **Tier 2**; Swift, PHP, and Kotlin are **Tier 3** ([SDKs, modelcontextprotocol.io/docs/2026-07-28/sdk](https://modelcontextprotocol.io/docs/2026-07-28/sdk.md)). The page states that "SDKs are classified into tiers based on feature completeness, protocol support, and maintenance commitment" ([SDKs](https://modelcontextprotocol.io/docs/2026-07-28/sdk.md)).

**SOURCE FACT:** The SDK page says each SDK "provides the same functionality but follows the idioms and best practices of its language," and that all SDKs support "Creating MCP servers that expose tools, resources, and prompts," "Building MCP clients that can connect to any MCP server," "Local and remote transport protocols," and "Protocol compliance with type safety" ([SDKs](https://modelcontextprotocol.io/docs/2026-07-28/sdk.md)).

**SOURCE FACT:** The SDK page links each language to a dedicated subdomain, e.g. TypeScript at `ts.sdk.modelcontextprotocol.io`, Python at `py.sdk.modelcontextprotocol.io`, and C# at `csharp.sdk.modelcontextprotocol.io` ([SDKs](https://modelcontextprotocol.io/docs/2026-07-28/sdk.md)).

**AI INFERENCE (from the SDK list and tier table):** For a server author choosing a language, the practical default is a Tier 1 SDK (TypeScript, Python, C#, Go, Rust, Ruby), because Tier 1 is the only tier with a 100% conformance requirement and a defined new-feature timeline; Java (Tier 2) is the strongest non-Tier-1 option.

### 1.2 What the tiers mean

**SOURCE FACT:** The tiering page defines three tiers: "**Tier 1**: Fully supported SDKs with complete protocol implementation, including all non-experimental features and optional capabilities like sampling and elicitation," "**Tier 2**: Actively-maintained SDKs working toward full protocol specification support," and "**Tier 3**: Experimental, partially implemented, or specialized SDKs" ([SDK Tiering System, modelcontextprotocol.io/community/sdk-tiers](https://modelcontextprotocol.io/community/sdk-tiers.md)).

**SOURCE FACT:** The tiering page states that "Experimental features and protocol extensions (such as Tasks and MCP Apps) are not required for any tier" ([SDK Tiering System](https://modelcontextprotocol.io/community/sdk-tiers.md)).

**SOURCE FACT:** The tier requirements table sets conformance thresholds of "100% pass rate" for Tier 1, "80% pass rate" for Tier 2, and "No minimum" for Tier 3; new protocol features must land "Before new spec version release" for Tier 1 and "Within 6 months" for Tier 2; issue triage is "Within 2 business days" for Tier 1 and "Within a month" for Tier 2; and critical bug resolution is "Within 7 days" for Tier 1 and "Within two weeks" for Tier 2 ([SDK Tiering System](https://modelcontextprotocol.io/community/sdk-tiers.md)).

**SOURCE FACT:** The tiering page defines a "**Stable Release**" as "a published version explicitly marked as production-ready (e.g., version `1.0.0` or higher without pre-release identifiers like `-alpha`, `-beta`, or `-rc`)" ([SDK Tiering System](https://modelcontextprotocol.io/community/sdk-tiers.md)).

**SOURCE FACT:** Conformance is measured with "automated conformance tests" that "validate protocol support against the published specifications," and scores exclude "tests marked as pending or skipped," "tests for experimental features," "legacy backward-compatibility tests (unless the SDK claims legacy support)," and "tests labeled `disputed` in the conformance repository, until the dispute is resolved" ([SDK Tiering System](https://modelcontextprotocol.io/community/sdk-tiers.md)).

**SOURCE FACT:** Tier advancement requires a maintainer to self-assess, open an issue in the `modelcontextprotocol/modelcontextprotocol` repository, pass automated conformance testing, and receive "approval from SDK Working Group maintainers" ([SDK Tiering System](https://modelcontextprotocol.io/community/sdk-tiers.md)).

**SOURCE FACT:** An SDK may be relegated if conformance tests "fail continuously for 4 weeks": "**Tier 1 → Tier 2**: Any conformance test fails" and "**Tier 2 → Tier 3**: More than 20% of conformance tests fail"; an SDK "may also be relegated if issues remain unaddressed for two months" ([SDK Tiering System](https://modelcontextprotocol.io/community/sdk-tiers.md)).

**SOURCE FACT:** The tiering page defines a `P0` priority as "Critical: core functionality failures or high-severity security," and specifies P0 issues are "Security vulnerabilities with CVSS score ≥ 7.0 (High or Critical severity)" or "Core functionality failures that prevent basic MCP operations: connection establishment, message exchange, or use of core primitives (tools, resources, prompts)" ([SDK Tiering System](https://modelcontextprotocol.io/community/sdk-tiers.md)).

**SOURCE FACT:** The tiering page records key dates: "**January 23, 2026**: Conformance tests available" and "**February 23, 2026**: Official SDK tiering published" ([SDK Tiering System](https://modelcontextprotocol.io/community/sdk-tiers.md)).

### 1.3 The originating SEP: SEP-1730

**SOURCE FACT:** SEP-1730 is titled "SDKs Tiering System," has status **Final**, type **Standards Track**, was created **2025-10-29**, and is authored by "Inna Harper, Felix Weinberger" ([SEP-1730, modelcontextprotocol.io/seps/1730-sdks-tiering-system](https://modelcontextprotocol.io/seps/1730-sdks-tiering-system.md)).

**SOURCE FACT:** SEP-1730's motivation states users "currently face challenges" including "**Feature Support Uncertainty**: No standardized way to know which SDKs support specific MCP features (OAuth, client/server/system features, like sampling, transports)," "**Maintenance Expectations**: Unclear commitment levels for bug fixes, security patches, and feature updates," and "**Implementation Timelines**: No visibility into when SDKs will support new protocol versions and features" ([SEP-1730](https://modelcontextprotocol.io/seps/1730-sdks-tiering-system.md)).

**SOURCE FACT:** SEP-1730's Tier 1 definition requires "All conformance tests pass" and "New protocol features before the new spec version release. (There is two week window between Release Candidate and the new protocol version release)" ([SEP-1730](https://modelcontextprotocol.io/seps/1730-sdks-tiering-system.md)).

**SOURCE FACT:** SEP-1730's Tier 2 definition requires "80% of conformance tests pass" and "New protocol features implemented within six months," plus "**Commitment to move to Tier1**" via "Published roadmap showing intent to achieve Tier 1" ([SEP-1730](https://modelcontextprotocol.io/seps/1730-sdks-tiering-system.md)).

**SOURCE FACT:** SEP-1730's Tier 3 is described as "Early-stage or specialized SDKs exploring the protocol space" with "No feature completeness guarantees," "No stable release requirement," and "No timeline commitments for updates" ([SEP-1730](https://modelcontextprotocol.io/seps/1730-sdks-tiering-system.md)).

**SOURCE FACT:** SEP-1730's tier advancement process is "1. **Self-Assessment:** Maintainers evaluate their SDK against tier criteria 2. **Application:** Submit tier advancement request with evidence 3. **Review:** Community review period (2 weeks) 4. **Validation:** Automated conformance testing, github stats on issues 5. **Decision:** Tier assignment by MCP maintainers" ([SEP-1730](https://modelcontextprotocol.io/seps/1730-sdks-tiering-system.md)).

**SOURCE FACT:** SEP-1730's relegation process triggers on "compliance tests continuously not passing for four week for Tier 1" and "20% of compliance tests continuously not passing for four week for Tier 2," plus "Issues are not addressed within two months" ([SEP-1730](https://modelcontextprotocol.io/seps/1730-sdks-tiering-system.md)).

**SOURCE FACT:** SEP-1730's appendix explains the initial simplified conformance approach: "The most straightforward approach is to have an Example Server for each SDK, similar to to [Everything Server]... Then we will have Conformance Test Client with all the test cases we want to be able to test" ([SEP-1730](https://modelcontextprotocol.io/seps/1730-sdks-tiering-system.md)).

**SOURCE CLAIM (rank: primary/SEP):** SEP-1730 claims the tiering system will produce "Improved overall SDK quality," "Standardized feature support," and "Healthy competition between implementations" ([SEP-1730](https://modelcontextprotocol.io/seps/1730-sdks-tiering-system.md)).

**AI INFERENCE (from SEP-1730's motivation and the tiering page's requirements):** The tiering system exists to convert an ad-hoc "which SDK supports what" question into an objective, machine-checked score; the conformance repository is the enforcement mechanism, and the tier is a maintenance commitment as much as a feature list.

---

## 2. The Official MCP Registry

### 2.1 What it is and the problem it solves

**SOURCE FACT:** The Registry is described as "the official centralized metadata repository for publicly accessible MCP servers, backed by major trusted contributors to the MCP ecosystem such as Anthropic, GitHub, PulseMCP, and Microsoft" ([The MCP Registry, modelcontextprotocol.io/registry/about](https://modelcontextprotocol.io/registry/about.md)).

**SOURCE FACT:** The Registry "provides: A single place for server creators to publish metadata about their servers; Namespace management through DNS verification; A REST API for MCP clients and aggregators to discover available servers; Standardized installation and configuration information" ([The MCP Registry](https://modelcontextprotocol.io/registry/about.md)).

**SOURCE FACT:** Server metadata is stored in a standardized `server.json` format containing "The server's unique name (e.g., `io.github.user/server-name`)," "Where to locate the server (e.g., npm package name, remote server URL)," "Execution instructions (e.g., command-line args, env vars)," and "Other discovery data (e.g., description, server capabilities)" ([The MCP Registry](https://modelcontextprotocol.io/registry/about.md)).

**SOURCE FACT:** The Registry is in preview: "The MCP Registry is currently in preview. Breaking changes or data resets may occur before general availability" ([The MCP Registry](https://modelcontextprotocol.io/registry/about.md)).

**SOURCE FACT:** The Registry distinguishes itself from package registries: "Package registries — such as npm, PyPI, and Docker Hub — host packages with code and binaries. The MCP Registry hosts metadata that points to those packages" ([The MCP Registry](https://modelcontextprotocol.io/registry/about.md)).

**SOURCE FACT:** The Registry "supports both open-source and closed-source servers" but "**does not** support private servers," defined as "servers published on a private network (like `mcp.acme-corp.internal`) or on private package registries" ([The MCP Registry](https://modelcontextprotocol.io/registry/about.md)).

**SOURCE FACT:** The Registry "is intended to be consumed primarily by downstream aggregators, such as MCP server marketplaces," and its metadata "is deliberately unopinionated" so aggregators "can provide curation or additional metadata such as community ratings" ([The MCP Registry](https://modelcontextprotocol.io/registry/about.md)).

**SOURCE FACT:** The Registry "is not intended to be directly consumed by host applications"; instead "host applications should consume other MCP registries, such as downstream marketplaces, via a REST API conforming to the official MCP Registry's OpenAPI spec" ([The MCP Registry](https://modelcontextprotocol.io/registry/about.md)).

**SOURCE FACT:** The official codebase "is **not** designed for self-hosting, and the registry maintainers cannot provide support for this use case" ([The MCP Registry](https://modelcontextprotocol.io/registry/about.md)).

**SOURCE FACT:** On trust, the Registry "uses namespace authentication to ensure that servers come from their claimed sources," with names in "a reverse DNS format (like `io.github.username/server` or `com.example/server`) that ties them to verified GitHub accounts or domains" ([The MCP Registry](https://modelcontextprotocol.io/registry/about.md)).

**SOURCE FACT:** The Registry "delegates security scanning to" the "Underlying package registries" and "Downstream aggregators," and "focuses on namespace authentication and metadata hosting, while relying on the broader ecosystem for security scanning of actual server code" ([The MCP Registry](https://modelcontextprotocol.io/registry/about.md)).

**SOURCE FACT:** Spam prevention uses "Namespace authentication requirements," "Character limits and validation," and "Manual takedown"; future measures "under consideration include stricter rate limiting, AI-based spam detection, and community reporting capabilities" ([The MCP Registry](https://modelcontextprotocol.io/registry/about.md)).

**AI INFERENCE (from the "metadata not artifacts" and "consumed by aggregators" facts):** The Registry solves the discovery-and-installation-metadata problem, not the hosting or security-scanning problem; a server author still publishes the actual artifact to npm/PyPI/NuGet/crates.io/OCI and relies on those registries plus downstream marketplaces for code-level trust.

### 2.2 Publishing a server: the quickstart flow

**SOURCE FACT:** The quickstart publishes a TypeScript server "using the official `mcp-publisher` CLI tool," with prerequisites of Node.js, an npm account, and a GitHub account ([Quickstart, modelcontextprotocol.io/registry/quickstart](https://modelcontextprotocol.io/registry/quickstart.md)).

**SOURCE FACT:** The Registry "verifies that a server's underlying package matches its metadata," and for npm packages "this requires adding an `mcpName` property to `package.json`"; the value of `mcpName` "will be your server's name in the MCP Registry" ([Quickstart](https://modelcontextprotocol.io/registry/quickstart.md)).

**SOURCE FACT:** The quickstart states "The MCP Registry only hosts metadata, not artifacts, so we must publish the package to npm before publishing the server to the MCP Registry" ([Quickstart](https://modelcontextprotocol.io/registry/quickstart.md)).

**SOURCE FACT:** The `mcp-publisher` CLI supports commands "init Create a server.json file template," "login Authenticate with the registry," "logout Clear saved authentication," and "publish Publish server.json to the registry" ([Quickstart](https://modelcontextprotocol.io/registry/quickstart.md)).

**SOURCE FACT:** The generated `server.json` uses `"$schema": "https://static.modelcontextprotocol.io/schemas/2025-12-11/server.schema.json"` and the quickstart warns "The `name` property in `server.json` **must** match the `mcpName` property in `package.json`" ([Quickstart](https://modelcontextprotocol.io/registry/quickstart.md)).

**SOURCE FACT:** Publishing is done with `mcp-publisher publish`, and the result can be verified via the API: `curl "https://registry.modelcontextprotocol.io/v0.1/servers?search=io.github.my-username/weather"` ([Quickstart](https://modelcontextprotocol.io/registry/quickstart.md)).

**SOURCE FACT:** The quickstart troubleshooting table maps "Registry validation failed for package" to ensuring the package includes the required validation information, "Invalid or expired Registry JWT token" to re-authenticating, and "You do not have permission to publish this server" to an authentication/namespace mismatch ([Quickstart](https://modelcontextprotocol.io/registry/quickstart.md)).

### 2.3 Supported package types

**SOURCE FACT:** The Registry supports npm (`"registryType": "npm"`), PyPI (`"pypi"`), NuGet (`"nuget"`), Cargo (`"cargo"`), Docker/OCI (`"oci"`), and MCPB (`"mcpb"`) package types ([MCP Registry Supported Package Types, modelcontextprotocol.io/registry/package-types](https://modelcontextprotocol.io/registry/package-types.md)).

**SOURCE FACT:** For npm, the Registry "currently supports the npm public registry (`https://registry.npmjs.org`) only," and verifies ownership "by checking `mcpName` in `package.json`," where "The `mcpName` property **MUST** match the server name from `server.json`" ([Package Types](https://modelcontextprotocol.io/registry/package-types.md)).

**SOURCE FACT:** For PyPI, the Registry "currently supports the official PyPI registry (`https://pypi.org`) only," and verifies ownership "by checking for the existence of an `mcp-name: $SERVER_NAME` string in the package README," which "may be hidden in a comment" ([Package Types](https://modelcontextprotocol.io/registry/package-types.md)).

**SOURCE FACT:** For NuGet, the Registry "currently supports the official NuGet registry (`https://api.nuget.org/v3/index.json`) only," and verifies ownership via an `mcp-name: $SERVER_NAME` string in the package README ([Package Types](https://modelcontextprotocol.io/registry/package-types.md)).

**SOURCE FACT:** For Cargo, the Registry "currently supports the official crates.io registry (`https://crates.io`) only," and notes a "**Cargo-specific gotcha:** Unlike PyPI and NuGet (which preserve HTML comments in their README rendering), **crates.io strips HTML comments during markdown→HTML conversion**," so "Cargo authors must include the `mcp-name:` token as visible markdown text" ([Package Types](https://modelcontextprotocol.io/registry/package-types.md)).

**SOURCE FACT:** For Cargo, the page describes two first-class distribution paths: "**Cargo (`registryType: cargo`)** — source-distributed via crates.io" requiring the Rust toolchain, and "**MCPB (`registryType: mcpb`)** — prebuilt binary distributed via GitHub or GitLab Releases" requiring no toolchain ([Package Types](https://modelcontextprotocol.io/registry/package-types.md)).

**SOURCE FACT:** For Docker/OCI, the Registry supports "Docker Hub (`docker.io`)," "GitHub Container Registry (`ghcr.io`)," "Google Artifact Registry (any `*.pkg.dev` domain)," "Azure Container Registry (`*.azurecr.io`)," and "Microsoft Container Registry (`mcr.microsoft.com`)," and verifies ownership "by checking for an `io.modelcontextprotocol.server.name` annotation" ([Package Types](https://modelcontextprotocol.io/registry/package-types.md)).

**SOURCE FACT:** For MCPB, the Registry "currently supports MCPB artifacts hosted via GitHub or GitLab releases," the package URL "**MUST** contain the string 'mcp'," and the metadata "**MUST** include a `fileSha256` property with a SHA-256 hash of the MCPB artifact" ([Package Types](https://modelcontextprotocol.io/registry/package-types.md)).

**SOURCE FACT:** The Registry "does not validate this hash; however, MCP clients **do** validate the hash before installation to ensure file integrity" ([Package Types](https://modelcontextprotocol.io/registry/package-types.md)).

**AI INFERENCE (from the per-type verification rules):** Each package type has a distinct ownership-proof mechanism (npm `mcpName`, PyPI/NuGet/Cargo README token, OCI label, MCPB URL+hash); a server author must match the proof mechanism to the chosen distribution channel, and the Cargo HTML-comment stripping is a concrete trap that would silently fail validation.

### 2.4 Remote servers

**SOURCE FACT:** The Registry "supports remote MCP servers via the `remotes` property in `server.json`," and "A remote server **MUST** be publicly accessible at its specified URL" ([Publishing Remote Servers, modelcontextprotocol.io/registry/remote-servers](https://modelcontextprotocol.io/registry/remote-servers.md)).

**SOURCE FACT:** "Remote servers should use the Streamable HTTP transport. The SSE transport is [deprecated](https://modelcontextprotocol.io/specification/draft/deprecated), so publish an `"sse"` remote only to support existing clients" ([Remote Servers](https://modelcontextprotocol.io/registry/remote-servers.md)).

**SOURCE FACT:** Remote servers "can define URL template variables using `{curly_braces}` notation," enabling "multi-tenant deployments where a single server definition can support multiple endpoints with configurable values," and variables "support additional properties like `default`, `choices`, and `isSecret`" ([Remote Servers](https://modelcontextprotocol.io/registry/remote-servers.md)).

**SOURCE FACT:** "MCP clients can be instructed to send specific HTTP headers by adding the `headers` property to the `remotes` entry," with fields including `name`, `description`, `isRequired`, and `isSecret` ([Remote Servers](https://modelcontextprotocol.io/registry/remote-servers.md)).

**SOURCE FACT:** "The `remotes` property can coexist with the `packages` property in `server.json` in order to allow MCP host applications to choose the preferred method of installation" ([Remote Servers](https://modelcontextprotocol.io/registry/remote-servers.md)).

### 2.5 Versioning

**SOURCE FACT:** "MCP servers **MUST** define a version string in `server.json`," and "The version string **MUST** be unique for each publication of the server. Once published, the version string (and other metadata) cannot be changed" ([Versioning Published MCP Servers, modelcontextprotocol.io/registry/versioning](https://modelcontextprotocol.io/registry/versioning.md)).

**SOURCE FACT:** "The MCP Registry recommends [semantic versioning](https://semver.org/), but supports any version string format," and "will mark the version as 'latest' if appropriate. If parsing fails, the version will always be marked as 'latest'" ([Versioning](https://modelcontextprotocol.io/registry/versioning.md)).

**SOURCE FACT:** "As an error prevention mechanism, the MCP Registry prohibits version strings that appear to refer to ranges of versions," with prohibited examples including `^1.2.3`, `~1.2.3`, `>=1.2.3`, `<=1.2.3`, `>1.2.3`, `<1.2.3`, `1.x`, `1.2.*`, `1 - 2`, and `1.2 || 1.3` ([Versioning](https://modelcontextprotocol.io/registry/versioning.md)).

**SOURCE FACT:** Recommended version examples include `1.0.0`, `2.1.3-alpha`, `1.0.0-beta.1`, `3.0.0-rc.2`, `2025.11.25`, and `2025.6.18`; allowed examples include `2025.06.18`, `2025-06-18`, and `v1.0` ([Versioning](https://modelcontextprotocol.io/registry/versioning.md)).

**SOURCE FACT:** Best practices include "Align Server Version with Package Version" for local servers, "Align Server Version with Remote API Version" for remote servers, and "Use Prerelease Versions for Registry-only Updates" ([Versioning](https://modelcontextprotocol.io/registry/versioning.md)).

**SOURCE FACT:** Aggregators "**SHOULD**: 1. Attempt to interpret versions as semantic versions when possible 2. Use the following version comparison rules: If one version is marked as 'latest', treat it as later; If both versions are valid semantic versions, use semantic versioning comparison rules; If neither versions are valid semantic versions, compare published timestamp; If one version is a valid semantic version and the other is not, treat the semantic version as later" ([Versioning](https://modelcontextprotocol.io/registry/versioning.md)).

### 2.6 Authentication

**SOURCE FACT:** "You must authenticate before publishing to the official MCP Registry," and "Which authentication method you choose determines the namespace of your server's name" ([Authentication, modelcontextprotocol.io/registry/authentication](https://modelcontextprotocol.io/registry/authentication.md)).

**SOURCE FACT:** With GitHub-based authentication, the server name "**MUST** be of the form `io.github.username/*` (or `io.github.orgname/*`)"; with domain-based authentication, the name "**MUST** be of the form `com.example.*/*`, where `com.example` is the reverse-DNS form of your domain name" ([Authentication](https://modelcontextprotocol.io/registry/authentication.md)).

**SOURCE FACT:** The Registry supports GitHub authentication ("uses an OAuth flow initiated by the `mcp-publisher` CLI tool"), DNS authentication ("relies on a DNS TXT record"), and HTTP authentication ("relies on a `/.well-known/mcp-registry-auth` file hosted on your domain") ([Authentication](https://modelcontextprotocol.io/registry/authentication.md)).

**SOURCE FACT:** DNS authentication supports key types "Ed25519," "ECDSA P-384," "Google KMS," and "Azure Key Vault," with TXT records of the form `v=MCPv1; k=ed25519; p=${PUBLIC_KEY}` or `v=MCPv1; k=ecdsap384; p=${PUBLIC_KEY}` ([Authentication](https://modelcontextprotocol.io/registry/authentication.md)).

**SOURCE FACT:** HTTP authentication hosts the proof at `https://example.com/.well-known/mcp-registry-auth` with content such as `v=MCPv1; k=ed25519; p=${PUBLIC_KEY}` ([Authentication](https://modelcontextprotocol.io/registry/authentication.md)).

**AI INFERENCE (from the name-format rules):** The authentication method and the server namespace are coupled by design — GitHub auth forces an `io.github.*` namespace, while DNS/HTTP auth is what unlocks a custom reverse-DNS domain namespace such as `com.example.*`.

### 2.7 GitHub Actions automation

**SOURCE FACT:** The GitHub Actions guide shows a workflow triggered "on: push: tags: ['v*']" that publishes the underlying package and then the server, with three authentication variants: "OIDC authentication (recommended)," "PAT authentication," and "DNS authentication" ([GitHub Actions, modelcontextprotocol.io/registry/github-actions](https://modelcontextprotocol.io/registry/github-actions.md)).

**SOURCE FACT:** The OIDC variant requires `permissions: id-token: write # Required for OIDC authentication` and authenticates with `./mcp-publisher login github-oidc` ([GitHub Actions](https://modelcontextprotocol.io/registry/github-actions.md)).

**SOURCE FACT:** The PAT variant authenticates with `./mcp-publisher login github --token ${{ secrets.MCP_GITHUB_TOKEN }}`, and the guide says the PAT needs "`read:org` and `read:user` scopes" ([GitHub Actions](https://modelcontextprotocol.io/registry/github-actions.md)).

**SOURCE FACT:** The DNS variant authenticates with `./mcp-publisher login dns --domain example.com --private-key ${{ secrets.MCP_PRIVATE_KEY }}` ([GitHub Actions](https://modelcontextprotocol.io/registry/github-actions.md)).

**SOURCE FACT:** The guide states "**GitHub OIDC Authentication**: No dedicated secret necessary," while PAT needs `MCP_GITHUB_TOKEN` and DNS needs `MCP_PRIVATE_KEY` ([GitHub Actions](https://modelcontextprotocol.io/registry/github-actions.md)).

**SOURCE FACT:** The workflow is triggered by tagging: `git tag v1.0.0` then `git push origin v1.0.0`, after which "The workflow will run tests, build the package, publish the package to npm, and publish the server to the MCP Registry" ([GitHub Actions](https://modelcontextprotocol.io/registry/github-actions.md)).

### 2.8 Moderation policy

**SOURCE FACT:** The moderation policy's TL;DR is "The MCP Registry is quite permissive! We only remove illegal content, malware, spam, and completely broken servers" ([Moderation Policy, modelcontextprotocol.io/registry/moderation-policy](https://modelcontextprotocol.io/registry/moderation-policy.md)).

**SOURCE FACT:** "The MCP Registry **does not** make guarantees about moderation, and consumers should assume minimal-to-no moderation," and "We largely rely on upstream package registries (like NPM, PyPI, and Docker) or downstream subregistries (like the GitHub MCP Registry) to do more in-depth moderation" ([Moderation Policy](https://modelcontextprotocol.io/registry/moderation-policy.md)).

**SOURCE FACT:** The Registry "will remove servers that contain: Illegal content, which includes obscene content, copyright violations, and hacking tools; Malware, regardless of intentions; Spam...; Non-functioning servers" ([Moderation Policy](https://modelcontextprotocol.io/registry/moderation-policy.md)).

**SOURCE FACT:** The Registry "**won't** remove: Low-quality or buggy servers; Servers with security vulnerabilities; Servers that do the same thing as other servers; Servers that provide or contain adult content" ([Moderation Policy](https://modelcontextprotocol.io/registry/moderation-policy.md)).

**SOURCE FACT:** "When we remove a server, we set the server's `status` to `"deleted"`, but the server's metadata remains accessible via the MCP Registry API" ([Moderation Policy](https://modelcontextprotocol.io/registry/moderation-policy.md)).

**SOURCE FACT:** Appeals are made by opening an issue on the Registry GitHub repository with "The name of the server" and "Why you believe the server doesn't meet the above criteria for removal" ([Moderation Policy](https://modelcontextprotocol.io/registry/moderation-policy.md)).

**AI INFERENCE (from the "won't remove security vulnerabilities" and "minimal-to-no moderation" facts):** The Registry is a discovery index, not a safety gate; a server author should not treat listing as an endorsement, and a consumer should not treat absence-from-removal as a security signal.

---

## 3. Example and Reference Servers

**SOURCE FACT:** The examples page lists "Current reference servers" as "**Everything** - Reference / test server with prompts, resources, and tools," "**Fetch** - Web content fetching and conversion for efficient LLM usage," "**Filesystem** - Secure file operations with configurable access controls," "**Git** - Tools to read, search, and manipulate Git repositories," "**Memory** - Knowledge graph-based persistent memory system," "**Sequential Thinking** - Dynamic and reflective problem-solving through thought sequences," and "**Time** - Time and timezone conversion capabilities" ([Example Servers, modelcontextprotocol.io/examples](https://modelcontextprotocol.io/examples.md)).

**SOURCE FACT:** "Additional example servers (archived)" are in the "servers-archived repository," and "They are provided for historical reference only" ([Example Servers](https://modelcontextprotocol.io/examples.md)).

**SOURCE FACT:** The page points to "Official integrations" maintained "by companies for their platforms" and "Community implementations" maintained "by community members," both in the MCP Servers Repository ([Example Servers](https://modelcontextprotocol.io/examples.md)).

**SOURCE FACT:** TypeScript-based reference servers "can be used directly with `npx`" (e.g. `npx -y @modelcontextprotocol/server-memory`), and Python-based servers "can be used with `uvx` (recommended) or `pip`" (e.g. `uvx mcp-server-git`) ([Example Servers](https://modelcontextprotocol.io/examples.md)).

**SOURCE FACT:** The page shows a Claude configuration example using `"mcpServers"` with `command`/`args`/`env` entries for `memory`, `filesystem`, and `github` servers ([Example Servers](https://modelcontextprotocol.io/examples.md)).

**AI INFERENCE (from the reference-server list and SEP-1730's appendix):** The "Everything" server is doubly significant: it is the canonical reference/test server for the protocol and the template SEP-1730 uses to seed per-SDK conformance testing.

---

## 4. Retrieval log

All URLs requested for this file were retrieved successfully on 2026-10-02:

| URL | Result |
| - | - |
| https://modelcontextprotocol.io/docs/2026-07-28/sdk.md | Retrieved |
| https://modelcontextprotocol.io/community/sdk-tiers.md | Retrieved |
| https://modelcontextprotocol.io/seps/1730-sdks-tiering-system.md | Retrieved |
| https://modelcontextprotocol.io/registry/about.md | Retrieved |
| https://modelcontextprotocol.io/registry/quickstart.md | Retrieved |
| https://modelcontextprotocol.io/registry/package-types.md | Retrieved |
| https://modelcontextprotocol.io/registry/remote-servers.md | Retrieved |
| https://modelcontextprotocol.io/registry/versioning.md | Retrieved |
| https://modelcontextprotocol.io/registry/authentication.md | Retrieved |
| https://modelcontextprotocol.io/registry/github-actions.md | Retrieved |
| https://modelcontextprotocol.io/registry/moderation-policy.md | Retrieved |
| https://modelcontextprotocol.io/examples.md | Retrieved |

**UNKNOWN:** The fetched pages do not state the current count of servers in the Registry, the exact general-availability date, or the full list of downstream aggregators beyond the named examples (Anthropic, GitHub, PulseMCP, Microsoft). The Registry API version observed in the quickstart is `v0.1`, but the pages do not state whether that is stable.
