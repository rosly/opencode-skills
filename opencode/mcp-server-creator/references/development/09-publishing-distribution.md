# Publishing and Distributing MCP Servers

Research date: 2026-10-03. MCP protocol revision in scope: 2026-07-28.

Notation used in this document:

- **SOURCE FACT** — official documentation, specification, or repository.
- **SOURCE CLAIM** — lower-tier source; a rank is given in parentheses.
- **AI INFERENCE** — reasoning that names the quoted facts it is built from.
- **PLAUSIBLE NOT VERIFIED** — consistent with sources but not directly confirmed.
- **UNKNOWN** — no source found.

## 1. The official MCP Registry: what it is and does not do

The official registry is a metadata catalog, not an artifact host. **SOURCE FACT:** "The MCP Registry is the official centralized metadata repository for publicly accessible MCP servers, backed by major trusted contributors to the MCP ecosystem such as Anthropic, GitHub, PulseMCP, and Microsoft" ([The MCP Registry](https://modelcontextprotocol.io/registry/about)). It is explicitly a pointer layer: "The MCP Registry hosts metadata that points to those packages" ([The MCP Registry](https://modelcontextprotocol.io/registry/about)). The quickstart repeats the boundary: "The MCP Registry only hosts metadata, not artifacts" ([Quickstart](https://modelcontextprotocol.io/registry/quickstart)).

The registry is in preview and makes no durability promises. **SOURCE FACT:** "The MCP Registry is currently in preview. Breaking changes or data resets may occur before general availability" ([The MCP Registry](https://modelcontextprotocol.io/registry/about)). Aggregators are told the same: "The MCP Registry does not provide uptime or data durability guarantees" ([MCP Registry Aggregators](https://modelcontextprotocol.io/registry/registry-aggregators)).

What it does not do:

- **Private servers.** **SOURCE FACT:** "The MCP Registry does not support private servers" ([The MCP Registry](https://modelcontextprotocol.io/registry/about)). The recommended alternative is to "host your own private MCP registry and add them there" ([The MCP Registry](https://modelcontextprotocol.io/registry/about)).
- **Direct host consumption.** **SOURCE FACT:** "The MCP Registry is not intended to be directly consumed by host applications" ([The MCP Registry](https://modelcontextprotocol.io/registry/about)). Hosts should consume downstream marketplaces via the registry's OpenAPI spec.
- **Self-hosting support.** **SOURCE FACT:** "the official MCP Registry codebase is not designed for self-hosting, and the registry maintainers cannot provide support for this use case" ([The MCP Registry](https://modelcontextprotocol.io/registry/about)).
- **Security scanning.** **SOURCE FACT:** the registry "delegates security scanning to" underlying package registries and downstream aggregators, and "focuses on namespace authentication and metadata hosting" ([The MCP Registry](https://modelcontextprotocol.io/registry/about)).

**AI INFERENCE:** Because the registry stores only metadata and delegates scanning, a publisher's real trust surface is the underlying package registry (npm/PyPI/OCI) plus whatever downstream marketplace adds curation. The registry's own contribution is namespace authentication.

## 2. `server.json` and `mcp-publisher`

Server metadata is stored in a standardized `server.json`. **SOURCE FACT:** it "contains: The server's unique name (e.g., `io.github.user/server-name`); Where to locate the server (e.g., npm package name, remote server URL); Execution instructions (e.g., command-line args, env vars); Other discovery data" ([The MCP Registry](https://modelcontextprotocol.io/registry/about)). The schema is date-versioned, e.g. `https://static.modelcontextprotocol.io/schemas/2025-12-11/server.schema.json` ([Quickstart](https://modelcontextprotocol.io/registry/quickstart)).

The official CLI is `mcp-publisher`. **SOURCE FACT:** its commands are "init Create a server.json file template; login Authenticate with the registry; logout Clear saved authentication; publish Publish server.json to the registry" ([Quickstart](https://modelcontextprotocol.io/registry/quickstart)). The canonical flow is `mcp-publisher init`, edit `server.json`, `mcp-publisher login github`, then `mcp-publisher publish` ([Quickstart](https://modelcontextprotocol.io/registry/quickstart)).

A critical consistency rule ties the two files together. **SOURCE FACT:** "The `name` property in `server.json` **must** match the `mcpName` property in `package.json`" ([Quickstart](https://modelcontextprotocol.io/registry/quickstart)). The registry verifies the underlying package matches the metadata: "The MCP Registry verifies that a server's underlying package matches its metadata" ([Quickstart](https://modelcontextprotocol.io/registry/quickstart)).

**AI INFERENCE:** `server.json` is the registry-side identity record and the package manifest is the package-side proof; the `name`/`mcpName` equality is the cryptographic-style binding that prevents one publisher from claiming another's package.

## 3. Per-package-type ownership proofs

Each package type has its own proof mechanism. **SOURCE FACT:** "The MCP Registry supports several different package types, and each package type has its own verification method" ([MCP Registry Supported Package Types](https://modelcontextprotocol.io/registry/package-types)).

| `registryType` | Supported registry | Ownership proof | Exact requirement |
| --- | --- | --- | --- |
| `npm` | npm public registry only | `mcpName` in `package.json` | "The `mcpName` property **MUST** match the server name from `server.json`" ([package-types](https://modelcontextprotocol.io/registry/package-types)) |
| `pypi` | official PyPI only | `mcp-name:` token in README | "checking for the existence of an `mcp-name: $SERVER_NAME` string in the package README" ([package-types](https://modelcontextprotocol.io/registry/package-types)) |
| `nuget` | official NuGet only | `mcp-name:` token in README | "checking for the existence of an `mcp-name: $SERVER_NAME` string in the package README" ([package-types](https://modelcontextprotocol.io/registry/package-types)) |
| `cargo` | crates.io only | `mcp-name:` token in README | "checking for the existence of an `mcp-name: $SERVER_NAME` string in the package README" ([package-types](https://modelcontextprotocol.io/registry/package-types)) |
| `oci` | Docker Hub, ghcr.io, GAR, ACR, MCR | image label annotation | "checking for an `io.modelcontextprotocol.server.name` annotation" ([package-types](https://modelcontextprotocol.io/registry/package-types)) |
| `mcpb` | GitHub or GitLab releases | URL contains "mcp" + `fileSha256` | "The MCPB package URL (`identifier` in `server.json`) **MUST** contain the string "mcp"" ([package-types](https://modelcontextprotocol.io/registry/package-types)) |

Notable per-type details:

- **npm.** **SOURCE FACT:** "For npm packages, the MCP Registry currently supports the npm public registry (`https://registry.npmjs.org`) only" ([package-types](https://modelcontextprotocol.io/registry/package-types)).
- **PyPI/NuGet.** **SOURCE FACT:** the token "may be hidden in a comment, but the `$SERVER_NAME` portion **MUST** match the server name from `server.json`" ([package-types](https://modelcontextprotocol.io/registry/package-types)).
- **Cargo gotcha.** **SOURCE FACT:** "crates.io strips HTML comments during markdown→HTML conversion" so "Cargo authors must include the `mcp-name:` token as visible markdown text" ([package-types](https://modelcontextprotocol.io/registry/package-types)). This differs from PyPI/NuGet, which "preserve HTML comments in their README rendering" ([package-types](https://modelcontextprotocol.io/registry/package-types)).
- **Cargo runtime model.** **SOURCE FACT:** "`cargo install <crate>` places the compiled binary on PATH at `~/.cargo/bin`, after which MCP clients invoke it directly by name. There is no per-invocation runner equivalent to `npx` (npm), `uvx` (PyPI), or `dnx` (NuGet, .NET 10 SDK Preview 6+)" ([package-types](https://modelcontextprotocol.io/registry/package-types)).
- **OCI identifier format.** **SOURCE FACT:** "The format of `identifier` is `registry/namespace/repository:tag`" ([package-types](https://modelcontextprotocol.io/registry/package-types)).
- **MCPB hash.** **SOURCE FACT:** "The MCP Registry does not validate this hash; however, MCP clients **do** validate the hash before installation to ensure file integrity" ([package-types](https://modelcontextprotocol.io/registry/package-types)). The hash is computed with `openssl dgst -sha256 image-processor.mcpb` ([package-types](https://modelcontextprotocol.io/registry/package-types)).

**AI INFERENCE:** The proof mechanisms are deliberately asymmetric because each upstream registry exposes different verifiable surfaces: npm exposes structured `package.json` fields, PyPI/NuGet/crates expose rendered README text, OCI exposes image config labels, and MCPB exposes a URL plus a client-verified content hash. The Cargo HTML-comment stripping is the one case where a proof that works elsewhere silently fails.

## 4. Remote server publishing

Remote servers use the `remotes` array instead of (or alongside) `packages`. **SOURCE FACT:** "A remote server **MUST** be publicly accessible at its specified URL" ([Publishing Remote Servers](https://modelcontextprotocol.io/registry/remote-servers)). Transport guidance is explicit: "Remote servers should use the Streamable HTTP transport. The SSE transport is deprecated, so publish an `"sse"` remote only to support existing clients" ([Publishing Remote Servers](https://modelcontextprotocol.io/registry/remote-servers)).

Remote entries support URL template variables, headers, and hybrid packaging. **SOURCE FACT:** "Remote servers can define URL template variables using `{curly_braces}` notation" for multi-tenant deployments ([Publishing Remote Servers](https://modelcontextprotocol.io/registry/remote-servers)); "MCP clients can be instructed to send specific HTTP headers by adding the `headers` property" ([Publishing Remote Servers](https://modelcontextprotocol.io/registry/remote-servers)); and "The `remotes` property can coexist with the `packages` property in `server.json` in order to allow MCP host applications to choose the preferred method of installation" ([Publishing Remote Servers](https://modelcontextprotocol.io/registry/remote-servers)).

**AI INFERENCE:** The hybrid `remotes` + `packages` pattern lets one registry record serve both users who want a locally spawned stdio process and users who want a hosted endpoint, without duplicating the server identity.

## 5. Versioning rules

Versions are mandatory, unique, and immutable. **SOURCE FACT:** "MCP servers **MUST** define a version string in `server.json`" and "The version string **MUST** be unique for each publication of the server. Once published, the version string (and other metadata) cannot be changed" ([Versioning Published MCP Servers](https://modelcontextprotocol.io/registry/versioning)).

Ranges are prohibited. **SOURCE FACT:** "As an error prevention mechanism, the MCP Registry prohibits version strings that appear to refer to ranges of versions" ([Versioning Published MCP Servers](https://modelcontextprotocol.io/registry/versioning)). The prohibited examples include `^1.2.3`, `~1.2.3`, `>=1.2.3`, `1.x`, `1.2.*`, `1 - 2`, and `1.2 || 1.3` ([Versioning Published MCP Servers](https://modelcontextprotocol.io/registry/versioning)).

Semver is recommended but not required, with a "latest" footgun. **SOURCE FACT:** "The MCP Registry recommends semantic versioning, but supports any version string format" and "If parsing fails, the version will always be marked as 'latest'" ([Versioning Published MCP Servers](https://modelcontextprotocol.io/registry/versioning)). A warning states: "If a server uses semantic version strings but publishes a new version that does *not* conform to semantic versioning, the new version will be marked as 'latest' even if it would otherwise be sorted before the semantic version strings" ([Versioning Published MCP Servers](https://modelcontextprotocol.io/registry/versioning)).

Best practices: align server version with package version, align remote server version with API version, and use prerelease versions for metadata-only republishes ([Versioning Published MCP Servers](https://modelcontextprotocol.io/registry/versioning)). A warning notes prerelease versions "are sorted before regular semantic versions" so a late prerelease "will **not** be marked as 'latest'" ([Versioning Published MCP Servers](https://modelcontextprotocol.io/registry/versioning)).

**AI INFERENCE:** The immutability rule means a metadata typo cannot be fixed in place; the only remedy is a new version, which is why the docs recommend prerelease suffixes for registry-only updates.

## 6. Authentication and namespaces

Authentication choice determines the namespace. **SOURCE FACT:** "Which authentication method you choose determines the namespace of your server's name" ([How to Authenticate](https://modelcontextprotocol.io/registry/authentication)). GitHub auth requires `io.github.username/*` or `io.github.orgname/*`; domain auth requires `com.example.*/*` ([How to Authenticate](https://modelcontextprotocol.io/registry/authentication)).

Supported methods:

- **GitHub OAuth.** **SOURCE FACT:** "GitHub authentication uses an OAuth flow initiated by the `mcp-publisher` CLI tool" via `mcp-publisher login github` ([How to Authenticate](https://modelcontextprotocol.io/registry/authentication)).
- **DNS.** **SOURCE FACT:** "DNS authentication is a domain-based authentication method that relies on a DNS TXT record" with the form `v=MCPv1; k=ed25519; p=${PUBLIC_KEY}` ([How to Authenticate](https://modelcontextprotocol.io/registry/authentication)). Supported key backends include Ed25519, ECDSA P-384, Google KMS, and Azure Key Vault ([How to Authenticate](https://modelcontextprotocol.io/registry/authentication)).
- **HTTP.** **SOURCE FACT:** "HTTP authentication is a domain-based authentication method that relies on a `/.well-known/mcp-registry-auth` file hosted on your domain" ([How to Authenticate](https://modelcontextprotocol.io/registry/authentication)).

**AI INFERENCE:** Namespace authentication is the registry's core trust primitive: a server name is a claim of ownership, and the auth method is the proof. This is why the registry can be permissive about content (Section 8) while still resisting impersonation.

## 7. GitHub Actions automation

Publishing can be automated on version tags. **SOURCE FACT:** the example workflow triggers on `push: tags: ["v*"]` and runs tests, builds, publishes the underlying package, then publishes to the registry ([How to Automate Publishing with GitHub Actions](https://modelcontextprotocol.io/registry/github-actions)).

OIDC is the recommended auth path. **SOURCE FACT:** the workflow labels "OIDC authentication (recommended)" and requires `permissions: id-token: write` ([How to Automate Publishing with GitHub Actions](https://modelcontextprotocol.io/registry/github-actions)). It authenticates with `./mcp-publisher login github-oidc` ([How to Automate Publishing with GitHub Actions](https://modelcontextprotocol.io/registry/github-actions)).

Secrets differ by method. **SOURCE FACT:** "GitHub OIDC Authentication: No dedicated secret necessary"; PAT auth needs a `MCP_GITHUB_TOKEN` with `read:org` and `read:user` scopes; DNS auth needs `MCP_PRIVATE_KEY` ([How to Automate Publishing with GitHub Actions](https://modelcontextprotocol.io/registry/github-actions)). The workflow also needs package-registry secrets such as `NPM_TOKEN` ([How to Automate Publishing with GitHub Actions](https://modelcontextprotocol.io/registry/github-actions)).

**AI INFERENCE:** OIDC removes long-lived registry credentials from CI, which is the strongest available automation posture; PAT and DNS methods remain for cases where OIDC cannot be used.

## 8. Moderation

The registry is intentionally permissive. **SOURCE FACT:** "**TL;DR**: The MCP Registry is quite permissive! We only remove illegal content, malware, spam, and completely broken servers" ([The MCP Registry Moderation Policy](https://modelcontextprotocol.io/registry/moderation-policy)). Consumers are warned: "The MCP Registry **does not** make guarantees about moderation, and consumers should assume minimal-to-no moderation" ([The MCP Registry Moderation Policy](https://modelcontextprotocol.io/registry/moderation-policy)).

Removed: illegal content, malware, spam, and non-functioning servers ([The MCP Registry Moderation Policy](https://modelcontextprotocol.io/registry/moderation-policy)). Not removed: "Low-quality or buggy servers", "Servers with security vulnerabilities", "Servers that do the same thing as other servers", and "Servers that provide or contain adult content" ([The MCP Registry Moderation Policy](https://modelcontextprotocol.io/registry/moderation-policy)).

Removal is a status change, not a deletion. **SOURCE FACT:** "When we remove a server, we set the server's `status` to `"deleted"`, but the server's metadata remains accessible via the MCP Registry API" ([The MCP Registry Moderation Policy](https://modelcontextprotocol.io/registry/moderation-policy)). Aggregators are advised to keep `status` current and may "prefer to remove these servers from their index" ([MCP Registry Aggregators](https://modelcontextprotocol.io/registry/registry-aggregators)).

**AI INFERENCE:** Because the registry does not remove vulnerable or low-quality servers, a publisher cannot rely on registry moderation as a quality signal; downstream marketplaces and the underlying package registries carry that burden.

## 9. Downstream aggregators and marketplaces

The registry is designed to feed aggregators. **SOURCE FACT:** "The MCP Registry is intended to be consumed primarily by downstream aggregators, such as MCP server marketplaces" and "The metadata hosted by the MCP Registry is deliberately unopinionated" ([The MCP Registry](https://modelcontextprotocol.io/registry/about)). Aggregators "are expected to scrape data on a regular but infrequent basis (e.g., once per hour), and persist the data in their own data store" ([MCP Registry Aggregators](https://modelcontextprotocol.io/registry/registry-aggregators)).

The read API is unauthenticated and read-only. **SOURCE FACT:** "The MCP Registry provides an unauthenticated read-only REST API that aggregators can use to populate their data stores" ([MCP Registry Aggregators](https://modelcontextprotocol.io/registry/registry-aggregators)). Endpoints include `GET /v0.1/servers`, `GET /v0.1/servers/{serverName}/versions`, and `GET /v0.1/servers/{serverName}/versions/{version}` ([MCP Registry Aggregators](https://modelcontextprotocol.io/registry/registry-aggregators)). Path parameters "**must** be URL-encoded", e.g. `io.modelcontextprotocol%2Feverything` ([MCP Registry Aggregators](https://modelcontextprotocol.io/registry/registry-aggregators)). Pagination is cursor-based and `updated_since` supports RFC 3339 filtering ([MCP Registry Aggregators](https://modelcontextprotocol.io/registry/registry-aggregators)).

A "subregistry" is an aggregator that also implements the registry's OpenAPI spec and may inject custom metadata via `_meta` ([MCP Registry Aggregators](https://modelcontextprotocol.io/registry/registry-aggregators)). **SOURCE FACT:** "The subregistry OpenAPI spec allows subregistries to inject custom metadata via the `_meta` field" such as "user ratings, download counts, and security scan results" ([MCP Registry Aggregators](https://modelcontextprotocol.io/registry/registry-aggregators)).

Named downstream consumers and marketplaces:

- **GitHub MCP Registry.** **SOURCE FACT:** GitHub operates an MCP registry at `github.com/mcp` listing "Servers and tools from the community that connect models to files, APIs, databases, and more" with a count of "355" servers at retrieval time ([GitHub MCP Registry](https://github.com/mcp)).
- **Glama.** **SOURCE CLAIM (vendor, rank: medium):** Glama describes itself as "A superset of the official MCP Registry – every server scanned, scored, and testable in your browser" and reports "94,156 MCP servers · 25,437 MCP connectors · 900,823 MCP tools" ([Glama](https://glama.ai/)). It distinguishes itself: "The official MCP Registry is a vendor-neutral index of MCP server metadata maintained by the MCP steering group – the canonical source of truth for publicly published servers" ([Glama](https://glama.ai/)).
- **PulseMCP, mcp.so, Smithery, Docker MCP Catalog, awesome-mcp-servers.** **SOURCE CLAIM (editorial roundup, rank: low-medium):** a 2026 roundup describes the field as "a canonical registry (the official one) and a layer of marketplaces on top of it (Glama, mcp.so, Smithery, PulseMCP, Docker, and more)" and recommends submitting "to the official MCP Registry first (the marketplaces increasingly sync from it)" ([Best MCP Marketplaces & Registries (2026)](https://designrevision.com/blog/best-mcp-marketplaces-and-registries)).
- **Directory counts and sync behavior.** **SOURCE CLAIM (practitioner recipe, rank: low):** a recipe lists approximate counts and auto-pull behavior — Glama "~21k indexed" auto-indexing from GitHub topics, mcp.so "~19k indexed" via form, PulseMCP "~12k indexed" auto-syncing from the Registry, and Smithery "~7k curated" via form — and advises "publish to the Registry FIRST ... Most other directories sync from it" ([MCP marketplaces, where to submit](https://studiomeyer.academy/recipes/9.3-mcp-marketplaces)).

**AI INFERENCE:** The registry-plus-aggregators architecture means a publisher's highest-leverage single action is a correct registry submission; the marketplace layer then re-serves and enriches that metadata. The exact counts above are volatile and should be treated as directional only.

## 10. Reference and example servers

The official examples page lists current reference servers: Everything, Fetch, Filesystem, Git, Memory, Sequential Thinking, and Time ([Example Servers](https://modelcontextprotocol.io/examples)). **SOURCE FACT:** "These official reference servers demonstrate core MCP features and SDK usage" ([Example Servers](https://modelcontextprotocol.io/examples)). Archived examples live in the `servers-archived` repository and "are provided for historical reference only" ([Example Servers](https://modelcontextprotocol.io/examples)).

**AI INFERENCE:** The reference servers are the canonical worked examples a professional publisher should read before writing a new server, because they demonstrate the SDK patterns the registry and clients expect.

## 11. Packaging local servers for `npx`/`uvx` and MCPB

### 11.1 `npx` and `uvx`

The official examples page shows the intended invocation patterns. **SOURCE FACT:** "TypeScript-based servers can be used directly with `npx`" and "Python-based servers can be used with `uvx` (recommended) or `pip`" ([Example Servers](https://modelcontextprotocol.io/examples)). The page gives `npx -y @modelcontextprotocol/server-memory` and `uvx mcp-server-git` as examples ([Example Servers](https://modelcontextprotocol.io/examples)).

The package-side requirements are documented by lower-tier guides. **SOURCE CLAIM (practitioner guide, rank: low-medium):** "An npm package is executable via `npx` when it has a `bin` entry in `package.json`" and "A Python MCP server published to PyPI is runnable via `uvx` when it has a `[project.scripts]` entry in `pyproject.toml`" ([Packaging an MCP server for npm and PyPI](https://connector.zone/guides/packaging-an-mcp-server-for-npm-and-pypi/)). The same guide states the entry point "must have a shebang line as its first line" and that TypeScript compilers "do not add the shebang automatically" ([Packaging an MCP server for npm and PyPI](https://connector.zone/guides/packaging-an-mcp-server-for-npm-and-pypi/)).

**SOURCE CLAIM (practitioner guide, rank: low):** a distribution guide recommends "Always use stdio transport for published servers" and "Write all logs to stderr, never stdout" because "stdout is reserved for JSON-RPC protocol messages" ([MCP Server Marketplace: Publishing and Distribution](https://www.grizzlypeaksoftware.com/library/mcp-server-marketplace-publishing-and-distribution-4rlxx8j5)). It also recommends pinning the SDK dependency with tilde rather than caret ([MCP Server Marketplace: Publishing and Distribution](https://www.grizzlypeaksoftware.com/library/mcp-server-marketplace-publishing-and-distribution-4rlxx8j5)).

**AI INFERENCE:** The `npx`/`uvx` path is the lowest-friction distribution for stdio servers because the client downloads and runs the package on demand; the `bin`/`[project.scripts]` entry point plus a correct shebang are the mechanical prerequisites.

### 11.2 MCPB (MCP Bundles)

MCPB is the one-click local-install format. **SOURCE FACT:** "MCP Bundles (`.mcpb`) are zip archives containing a local MCP server and a `manifest.json` that describes the server and its capabilities" and the format is "spiritually similar to Chrome extensions (`.crx`) or VS Code extensions (`.vsix`), enabling end users to install local MCP servers with a single click" ([modelcontextprotocol/mcpb README](https://github.com/modelcontextprotocol/mcpb)). The toolchain is `npm install -g @anthropic-ai/mcpb`, then `mcpb init` and `mcpb pack` ([modelcontextprotocol/mcpb README](https://github.com/modelcontextprotocol/mcpb)).

The manifest spec is versioned. **SOURCE FACT:** "Current version: `0.3`" with required fields `manifest_version`, `name`, `version`, `description`, `author`, and `server` ([MCPB Manifest.json Spec](https://github.com/modelcontextprotocol/mcpb/blob/main/MANIFEST.md)). Server types are `node`, `python`, `binary`, and (v0.4+) `uv` ([MCPB Manifest.json Spec](https://github.com/modelcontextprotocol/mcpb/blob/main/MANIFEST.md)). The `uv` type "enables cross-platform Python extensions without bundling dependencies" and "Handles compiled dependencies (pydantic, numpy, etc.)" ([MCPB Manifest.json Spec](https://github.com/modelcontextprotocol/mcpb/blob/main/MANIFEST.md)).

Language guidance is explicit. **SOURCE FACT:** "We recommend implementing MCP servers in Node.js rather than Python to reduce installation friction. Node.js ships with Claude for macOS and Windows" ([modelcontextprotocol/mcpb README](https://github.com/modelcontextprotocol/mcpb)). For traditional Python bundles, "Cannot portably bundle compiled dependencies (e.g., pydantic, which the MCP Python SDK requires)" ([modelcontextprotocol/mcpb README](https://github.com/modelcontextprotocol/mcpb)).

The format was renamed from DXT. **SOURCE FACT:** "This project is being renamed from DXT (Desktop Extensions) to MCPB (MCP Bundles)"; "`dxt` CLI is now `mcpb`"; "`.dxt` files are now `.mcpb` files" ([modelcontextprotocol/mcpb README](https://github.com/modelcontextprotocol/mcpb)).

**AI INFERENCE:** MCPB is the right choice when the target user should not need a toolchain; `npx`/`uvx` is the right choice when the user already has Node or Python and the server is a normal package. The registry's `mcpb` package type (Section 3) connects the bundle to the metadata catalog.

## 12. Practical publishing checklist

**AI INFERENCE** (assembled from the SOURCE FACTS above):

1. Choose the namespace first, because it determines the auth method and the server name (Section 6).
2. Publish the underlying artifact to npm/PyPI/NuGet/crates/OCI/MCPB release before the registry, since "The MCP Registry only hosts metadata, not artifacts" (Section 1).
3. Add the matching ownership proof (`mcpName`, README `mcp-name:`, OCI label, or MCPB URL+hash) (Section 3).
4. Write `server.json` with a unique, immutable, non-range version aligned to the package version (Sections 2, 5).
5. Authenticate with `mcp-publisher login` and publish; prefer OIDC in CI (Sections 2, 7).
6. For remote servers, use `streamable-http` and ensure the URL is publicly accessible (Section 4).
7. Expect minimal moderation and rely on the package registry and downstream marketplaces for quality signals (Sections 8, 9).

## Sources and retrieval log

Retrieved successfully:

- [The MCP Registry](https://modelcontextprotocol.io/registry/about)
- [Quickstart](https://modelcontextprotocol.io/registry/quickstart)
- [MCP Registry Supported Package Types](https://modelcontextprotocol.io/registry/package-types)
- [Publishing Remote Servers](https://modelcontextprotocol.io/registry/remote-servers)
- [Versioning Published MCP Servers](https://modelcontextprotocol.io/registry/versioning)
- [How to Authenticate](https://modelcontextprotocol.io/registry/authentication)
- [How to Automate Publishing with GitHub Actions](https://modelcontextprotocol.io/registry/github-actions)
- [The MCP Registry Moderation Policy](https://modelcontextprotocol.io/registry/moderation-policy)
- [MCP Registry Aggregators](https://modelcontextprotocol.io/registry/registry-aggregators)
- [Example Servers](https://modelcontextprotocol.io/examples)
- [modelcontextprotocol/mcpb README](https://github.com/modelcontextprotocol/mcpb)
- [MCPB Manifest.json Spec](https://github.com/modelcontextprotocol/mcpb/blob/main/MANIFEST.md)
- [GitHub MCP Registry](https://github.com/mcp)
- [Glama](https://glama.ai/)
- [Best MCP Marketplaces & Registries (2026)](https://designrevision.com/blog/best-mcp-marketplaces-and-registries)
- [MCP marketplaces, where to submit](https://studiomeyer.academy/recipes/9.3-mcp-marketplaces)
- [Packaging an MCP server for npm and PyPI](https://connector.zone/guides/packaging-an-mcp-server-for-npm-and-pypi/)
- [MCP Server Marketplace: Publishing and Distribution](https://www.grizzlypeaksoftware.com/library/mcp-server-marketplace-publishing-and-distribution-4rlxx8j5)

Failed retrievals (recorded as results):

- `https://raw.githubusercontent.com/modelcontextprotocol/registry/main/docs/guides/publishing/publish-server.md` — HTTP 404. The official publishing guide is not at this raw path; the equivalent content was obtained from the official `package-types` and `quickstart` pages instead.
- Web search for "MCP registry server.json mcp-publisher tutorial" — search tool returned an execution error; no results.

**UNKNOWN:** the exact current server count of the official registry (the GitHub registry page showed 355, but that is GitHub's own registry, not `registry.modelcontextprotocol.io`); the precise list of downstream aggregators that have implemented the subregistry OpenAPI spec; and whether the MCPB manifest spec has advanced beyond v0.4 as of 2026-10-03.
