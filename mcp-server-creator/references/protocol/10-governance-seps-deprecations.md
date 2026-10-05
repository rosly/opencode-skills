# MCP Governance, SEPs, and Deprecations

Research file for the MCP server creator report. Topic: who governs MCP, the Specification Enhancement Proposal (SEP) process, the feature lifecycle/deprecation policy, the currently deprecated features in revision **2026-07-28**, and the working/interest groups relevant to server implementation.

Protocol revision under study: **2026-07-28**. Research date: **2026-10-02**.

## Notation used in this file

- **SOURCE FACT** — a statement taken directly from an official primary source, quoted exactly and linked inline.
- **SOURCE CLAIM (rank)** — a claim made by a source, with a rank for how authoritative it is for the fact asserted. Ranks used here: `[primary/official]` (the MCP project's own docs/spec), `[primary/SEP]` (an accepted SEP), `[secondary]` (a third party).
- **AI INFERENCE** — a conclusion drawn by this research, naming the quoted facts it rests on.
- **PLAUSIBLE NOT VERIFIED** — a reasonable reading that the fetched sources do not directly confirm.
- **UNKNOWN** — the sources fetched do not answer the point, or retrieval failed.

---

## 1. Governance and Stewardship

### 1.1 Legal home and licensing

**SOURCE FACT:** MCP "has been established as **Model Context Protocol a Series of LF Projects, LLC**," and "Governance changes approved as per the provisions of this governance document must also be approved by LF Projects, LLC" ([Governance and Stewardship, modelcontextprotocol.io/community/governance](https://modelcontextprotocol.io/community/governance.md)).

**SOURCE FACT:** "Except as described below, all code and specification contributions to the project must be made using the Apache License, Version 2.0," and "All documentation (excluding specifications) will be made available under Creative Commons Attribution 4.0 International license" ([Governance](https://modelcontextprotocol.io/community/governance.md)).

**SOURCE FACT:** "Model Context Protocol participants acknowledge that the copyright in all new contributions will be retained by the copyright holder as independent works of authorship and that no contributor or copyright holder will be required to assign copyrights to the project" ([Governance](https://modelcontextprotocol.io/community/governance.md)).

### 1.2 The stewardship hierarchy

**SOURCE FACT:** "The MCP project adopts a hierarchical structure, similar to Python, PyTorch, and other open source projects," with roles "**Lead Maintainers (BDFL)** — Final decision authority," "**Core Maintainers** — Overall project direction," "**Maintainers** — Working Groups, SDKs, components," and "**Contributors** — Issues, PRs, discussions" ([Governance](https://modelcontextprotocol.io/community/governance.md)).

**SOURCE FACT:** "Together, Maintainers, Core Maintainers, and Lead Maintainers form the **MCP Steering Group**" ([Governance](https://modelcontextprotocol.io/community/governance.md)).

**SOURCE FACT:** "Membership in the technical governance process is for individuals, not companies. That is, there are no seats reserved for specific companies, and membership is associated with the person rather than the company employing that person" ([Governance](https://modelcontextprotocol.io/community/governance.md)).

**SOURCE FACT:** "**Core Maintainers** steer the MCP specification and overall project direction. They can veto Maintainer decisions by majority vote, resolve disputes, and appoint or remove Maintainers" ([Governance](https://modelcontextprotocol.io/community/governance.md)).

**SOURCE FACT:** "**Lead Maintainers** hold final authority and can veto any decision by Core Maintainers or Maintainers — the role commonly known as Benevolent Dictator for Life (BDFL)" ([Governance](https://modelcontextprotocol.io/community/governance.md)).

**SOURCE FACT:** "The Core Maintainer group meets every two weeks to discuss and vote on proposals," and "The Lead Maintainer, Core Maintainer, and Maintainer group should attempt to meet in person every three to six months" ([Governance](https://modelcontextprotocol.io/community/governance.md)).

**SOURCE FACT:** The current Lead Maintainers are "David Soria Parra" and "Den Delimarsky"; the current Core Maintainers are "Peter Alexander," "Caitie McCaffrey," "Kurtis Van Gent," "Clare Liguori," "Paul Carleton," and "Nick Cooper" ([Governance](https://modelcontextprotocol.io/community/governance.md)).

**SOURCE FACT:** Emeritus members include "Justin Spahr-Summers (Co-Inventor, Lead Maintainer Emeritus)," "Basil Hosmer (Core Maintainer Emeritus)," "Che Liu (Core Maintainer Emeritus)," and "Nick Aldridge (Core Maintainer Emeritus)" ([Governance](https://modelcontextprotocol.io/community/governance.md)).

**SOURCE FACT:** "Technical governance is facilitated through a shared [Discord server] for all maintainers," and "all decisions and their supporting discussions must be recorded and made transparently available on the Discord server" ([Governance](https://modelcontextprotocol.io/community/governance.md)).

**SOURCE FACT:** "Maintainers, Core Maintainers, and Lead Maintainers should use the same contribution process as external contributors, rather than making direct changes to repos" ([Governance](https://modelcontextprotocol.io/community/governance.md)).

**AI INFERENCE (from the LF Projects, individual-membership, and BDFL facts):** MCP is vendor-neutral at the legal layer (a Linux Foundation series) and at the membership layer (individuals, not company seats), but retains a founder-controlled final authority (Lead Maintainers/BDFL) — a hybrid of open-foundation governance and founder stewardship.

### 1.3 The Contributor Ladder

**SOURCE FACT:** The Contributor Ladder "implements [SEP-2148](https://modelcontextprotocol.io/seps/2148-contributor-ladder)" and defines roles from Contributor to Lead Maintainer ([Contributor Ladder, modelcontextprotocol.io/community/contributor-ladder](https://modelcontextprotocol.io/community/contributor-ladder.md)).

**SOURCE FACT:** The roles-at-a-glance table gives minimum timelines: Contributor "Immediate," Member "2-3 months of meaningful contributions," Maintainer "6+ months as Member," Core Maintainer "By invitation after sustained Maintainer contribution," Lead Maintainer "Reserved for project founders; succession only," and Community Moderator "Parallel track: Member status + appointment" ([Contributor Ladder](https://modelcontextprotocol.io/community/contributor-ladder.md)).

**SOURCE FACT:** "Timelines are minimums, not guarantees. They protect the project from rapid privilege escalation and ensure a high bar of demonstrated commitment" ([Contributor Ladder](https://modelcontextprotocol.io/community/contributor-ladder.md)).

**SOURCE FACT:** A Member requires "Two-factor authentication enabled on GitHub" and "No objections from existing Members within 7 days," and is sponsored "by two existing Members or Maintainers from different organizations, **or** by one Core Maintainer or Lead Maintainer" ([Contributor Ladder](https://modelcontextprotocol.io/community/contributor-ladder.md)).

**SOURCE FACT:** "Lead Maintainers hold ultimate authority over MCP's direction and governance. This is a lifetime appointment reserved for project founders. There is no advancement path to this role" ([Contributor Ladder](https://modelcontextprotocol.io/community/contributor-ladder.md)).

**SOURCE FACT:** On succession, "If no Lead Maintainers remain, the Core Maintainers appoint a successor by majority vote within 30 days. Until a new Lead Maintainer is appointed, the project operates by two-thirds vote of Core Maintainers" ([Contributor Ladder](https://modelcontextprotocol.io/community/contributor-ladder.md)).

**SOURCE FACT:** The escalation matrix lists "Technical disagreement in PR" escalating from "Maintainer in scope" to "Core Maintainer" within "5 business days," and "Security issue" escalating from "Core Maintainer" to "Lead Maintainer" with timeline "Immediate" ([Contributor Ladder](https://modelcontextprotocol.io/community/contributor-ladder.md)).

**SOURCE FACT:** "MCP operates on a principle of delegation. Decisions should be made at the lowest appropriate level" ([Contributor Ladder](https://modelcontextprotocol.io/community/contributor-ladder.md)).

### 1.4 Design principles

**SOURCE FACT:** The design principles are "Convergence over choice," "Composability over specificity," "Interoperability over optimization," "Stability over velocity," "Capability over compensation," "Demonstration over deliberation," "Pragmatism over purity," and "Standardization over innovation" ([Design Principles, modelcontextprotocol.io/community/design-principles](https://modelcontextprotocol.io/community/design-principles.md)).

**SOURCE FACT:** "There should be one way to solve a problem in MCP. Rather than supporting multiple approaches that fragment the ecosystem, we choose a single well-designed path" ([Design Principles](https://modelcontextprotocol.io/community/design-principles.md)).

**SOURCE FACT:** "MCP provides foundational primitives: resources, tools, and prompts. We don't add protocol features for use cases that can be constructed from these existing building blocks" ([Design Principles](https://modelcontextprotocol.io/community/design-principles.md)).

**SOURCE FACT:** "Adding to a protocol as widely adopted as MCP is easy. Removing from it is nearly impossible. Every addition is a permanent commitment and a cost for client implementers to support" ([Design Principles](https://modelcontextprotocol.io/community/design-principles.md)).

**SOURCE FACT:** "MCP values working implementations over theoretical debates. When evaluating proposals, we prioritize evidence from real usage over hypothetical arguments" ([Design Principles](https://modelcontextprotocol.io/community/design-principles.md)).

**AI INFERENCE (from "Composability over specificity" and "Stability over velocity"):** A server author should expect that MCP will not add protocol features for narrow use cases; the intended path is to compose tools/resources/prompts, and any protocol addition is treated as a near-permanent commitment.

---

## 2. The SEP Process

### 2.1 What a SEP is and when one is required

**SOURCE FACT:** "SEP stands for Specification Enhancement Proposal. A SEP is a design document providing information to the MCP community, or describing a new feature for the Model Context Protocol or its processes" ([SEP Guidelines, modelcontextprotocol.io/community/sep-guidelines](https://modelcontextprotocol.io/community/sep-guidelines.md)).

**SOURCE FACT:** "SEPs are the primary mechanism for proposing major new features, collecting community input on an issue, and documenting the design decisions that have gone into MCP" ([SEP Guidelines](https://modelcontextprotocol.io/community/sep-guidelines.md)).

**SOURCE FACT:** "Write a SEP if your change involves: **A new feature or protocol change**...; **A breaking change** - Any change that is not backwards-compatible; **A governance or process change**...; **A complex or controversial topic**" ([SEP Guidelines](https://modelcontextprotocol.io/community/sep-guidelines.md)).

**SOURCE FACT:** "Skip the SEP process for: Bug fixes and typo corrections; Documentation clarifications; Adding examples to existing features; Minor schema fixes that don't change behavior" ([SEP Guidelines](https://modelcontextprotocol.io/community/sep-guidelines.md)).

**SOURCE FACT:** There are four SEP types: "**Standards Track**," "**Informational**," "**Process**," and "**Extensions Track**" ([SEP Guidelines](https://modelcontextprotocol.io/community/sep-guidelines.md)).

### 2.2 The workflow and statuses

**SOURCE FACT:** "**Prior discussion is required.** SEP authors must discuss the idea with the relevant working or interest group in Discord before opening the SEP pull request, and the PR description must link to that discussion... A SEP without a linked prior discussion is not accepted" ([SEP Guidelines](https://modelcontextprotocol.io/community/sep-guidelines.md)).

**SOURCE FACT:** The step-by-step process is: discuss with the relevant group; draft the SEP as `0000-your-feature-title.md`; create a pull request; update the SEP number to the PR number; find a Sponsor; the sponsor assigns themselves and sets status to `draft`; informal review; formal review (`in-review`); resolution; finalization ([SEP Guidelines](https://modelcontextprotocol.io/community/sep-guidelines.md)).

**SOURCE FACT:** "Once accepted, the reference implementation must be completed. For Standards Track SEPs with observable protocol behavior, a conformance test must also be merged... SDK implementations are not required for a SEP to become `final`" ([SEP Guidelines](https://modelcontextprotocol.io/community/sep-guidelines.md)).

**SOURCE FACT:** The SEP statuses are `draft`, `in-review`, `accepted`, `rejected`, `withdrawn`, `final`, `superseded`, and `dormant` ([SEP Guidelines](https://modelcontextprotocol.io/community/sep-guidelines.md)).

**SOURCE FACT:** "**Important distinction**: `dormant` is not the same as `rejected`. A dormant SEP simply didn't find a sponsor - the idea may still be valid" ([SEP Guidelines](https://modelcontextprotocol.io/community/sep-guidelines.md)).

**SOURCE FACT:** "SEPs are reviewed by the MCP Core Maintainers team every two weeks," and "For a SEP to be accepted it must meet these criteria: A prototype implementation demonstrating the proposal; Clear benefit to the MCP ecosystem; Community support and consensus" ([SEP Guidelines](https://modelcontextprotocol.io/community/sep-guidelines.md)).

**SOURCE FACT:** "**The Sponsor is responsible for updating the SEP status.** This ensures status transitions are made by someone with the authority and context to do so appropriately" ([SEP Guidelines](https://modelcontextprotocol.io/community/sep-guidelines.md)).

**SOURCE FACT:** "For **Standards Track SEPs** that introduce or modify observable protocol behavior, a conformance scenario must be merged into the conformance repository before the SEP can reach `Final` status" ([SEP Guidelines](https://modelcontextprotocol.io/community/sep-guidelines.md)).

**SOURCE FACT:** The required SEP format sections are Preamble, Abstract, Motivation, Specification, Rationale, Backward Compatibility, Reference Implementation, and Security Implications ([SEP Guidelines](https://modelcontextprotocol.io/community/sep-guidelines.md)).

### 2.3 SEP-1850: the PR-based workflow

**SOURCE FACT:** SEP-1850 is titled "PR-Based SEP Workflow," status **Final**, type **Process**, created **2025-11-20**, and "Accepted 2025-11-28, 8 Yes, 0 No, 0 Absent per vote in Discord" ([SEP-1850, modelcontextprotocol.io/seps/1850-pr-based-sep-workflow](https://modelcontextprotocol.io/seps/1850-pr-based-sep-workflow.md)).

**SOURCE FACT:** SEP-1850 "formalizes the pull request-based SEP workflow that stores proposals as markdown files in the `seps/` directory," and "The SEP number is always the pull request number that introduces the SEP file" ([SEP-1850](https://modelcontextprotocol.io/seps/1850-pr-based-sep-workflow.md)).

**SOURCE FACT:** SEP-1850 states "Status progression follows: `Draft → In-Review → Accepted → Final`," with "Additional terminal states: `Rejected`, `Withdrawn`, `Superseded`, `Dormant`" ([SEP-1850](https://modelcontextprotocol.io/seps/1850-pr-based-sep-workflow.md)).

**SOURCE FACT:** "**Dormant status**: If a SEP does not find a sponsor within six months, Core Maintainers may close the PR and mark the SEP as `dormant`" ([SEP-1850](https://modelcontextprotocol.io/seps/1850-pr-based-sep-workflow.md)).

**SOURCE FACT:** SEP-1850's rationale for PR numbers is that it "Eliminates race conditions around manual numbering," "Creates natural traceability between proposal and discussion," and "Prevents number conflicts" ([SEP-1850](https://modelcontextprotocol.io/seps/1850-pr-based-sep-workflow.md)).

**SOURCE FACT:** SEP-1850's vote section states "This SEP was accepted unanimously by the MCP Core Maintainers with a vote of 8 yes's, 0 no's and 0 absent votes on Friday December 28th, 2025 in a Discord poll" ([SEP-1850](https://modelcontextprotocol.io/seps/1850-pr-based-sep-workflow.md)).

**AI INFERENCE (from SEP-1850 and the SEP Guidelines):** The SEP process is deliberately file-and-PR based (mirroring PEPs), with the sponsor as the single status authority; this makes the SEP corpus version-controlled and searchable, and makes "no sponsor within six months" the only automatic terminal outcome.

### 2.4 The SEP index

**SOURCE FACT:** The SEP index summary states "**Final**: 42" ([SEP Index, modelcontextprotocol.io/seps/index](https://modelcontextprotocol.io/seps/index.md)).

**SOURCE FACT:** The index lists SEPs including "SEP-2663 Tasks Extension" (Final, Extensions Track, 2026-04-27), "SEP-2640 Skills Extension" (Final, Extensions Track, 2026-04-23), "SEP-2596 Specification Feature Lifecycle and Deprecation Policy" (Final, Process, 2026-04-17), and "SEP-2577 Deprecate Roots, Sampling, and Logging" (Final, Standards Track, 2026-04-14) ([SEP Index](https://modelcontextprotocol.io/seps/index.md)).

**SOURCE FACT:** The index also lists "SEP-2575 Make MCP Stateless" (Final, Standards Track, 2025-06-18), "SEP-2567 Sessionless MCP via Explicit State Handles" (Final, Standards Track, 2026-03-11), "SEP-2549 TTL for List Results" (Final, Standards Track, 2026-04-09), and "SEP-2484 Require Conformance Tests for Standards Track SEPs to Reach Final Status" (Final, Process, 2026-03-27) ([SEP Index](https://modelcontextprotocol.io/seps/index.md)).

**SOURCE FACT:** The index defines statuses including "Draft," "In-Review," "Accepted," "Final," "Rejected," "Withdrawn," "Superseded," and "Dormant" ([SEP Index](https://modelcontextprotocol.io/seps/index.md)).

**SOURCE FACT:** "Each SEP is reachable by number at `/seps/<number>` (for example, [/seps/1850](https://modelcontextprotocol.io/seps/1850))" ([SEP Index](https://modelcontextprotocol.io/seps/index.md)).

**AI INFERENCE (from the index's "Final: 42" and the listed SEPs):** As of the fetched index, all listed SEPs are Final and none are shown as Draft/In-Review/Rejected/Withdrawn/Dormant, which suggests the index page may only render finalized SEPs or that the corpus is currently all-final; the fetched page does not clarify which.

---

## 3. Feature Lifecycle and Deprecation Policy

### 3.1 The three feature states

**SOURCE FACT:** The policy "defines a lifecycle for individual features within the Model Context Protocol specification. It defines three feature states (Active, Deprecated, Removed), the criteria and procedure for moving between them, a minimum window between deprecation and removal, and the documentation required at each transition" ([Feature Lifecycle and Deprecation Policy, modelcontextprotocol.io/community/feature-lifecycle](https://modelcontextprotocol.io/community/feature-lifecycle.md)).

**SOURCE FACT:** "This policy was adopted via [SEP-2596]" ([Feature Lifecycle](https://modelcontextprotocol.io/community/feature-lifecycle.md)).

**SOURCE FACT:** The three states are defined as: "**Active** — The feature is part of the Current specification revision"; "**Deprecated** — The feature remains in the specification but is scheduled for removal. A migration path is documented"; and "**Removed** — The feature has been deleted from `draft` and will be absent from the next Current revision" ([Feature Lifecycle](https://modelcontextprotocol.io/community/feature-lifecycle.md)).

**SOURCE FACT:** "A Deprecated feature MAY be restored to Active by a SEP that supersedes the deprecation SEP and documents the changed circumstances" ([Feature Lifecycle](https://modelcontextprotocol.io/community/feature-lifecycle.md)).

**SOURCE FACT:** "Removal from the specification does not oblige an SDK to drop the feature from releases. That timeline is governed by the SDK's own revision-support policy" ([Feature Lifecycle](https://modelcontextprotocol.io/community/feature-lifecycle.md)).

### 3.2 Deprecation criteria and the minimum window

**SOURCE FACT:** A feature may be proposed for deprecation when "it has been superseded by another feature that covers the same use cases," "it presents a security, privacy, or interoperability risk that cannot be mitigated in place," "ecosystem telemetry or SDK maintainer consensus indicates negligible adoption relative to its maintenance cost," "or any other reasons the Core Maintainers deem appropriate" ([Feature Lifecycle](https://modelcontextprotocol.io/community/feature-lifecycle.md)).

**SOURCE FACT:** "Deprecation is a specification change and therefore requires a SEP per the SEP guidelines" ([Feature Lifecycle](https://modelcontextprotocol.io/community/feature-lifecycle.md)).

**SOURCE FACT:** The deprecation SEP must "Specify the **minimum deprecation window**: the number of months, at least twelve, that the feature must remain Deprecated before it is eligible for removal" ([Feature Lifecycle](https://modelcontextprotocol.io/community/feature-lifecycle.md)).

**SOURCE FACT:** "The window is measured from the release of the specification revision in which the feature is first marked Deprecated, not from the date the SEP reaches Final" ([Feature Lifecycle](https://modelcontextprotocol.io/community/feature-lifecycle.md)).

**SOURCE FACT:** "The feature becomes eligible for removal in the first specification revision released as Current on or after the window elapses; that point is the feature's **earliest removal**" ([Feature Lifecycle](https://modelcontextprotocol.io/community/feature-lifecycle.md)).

**SOURCE FACT:** "The twelve-month floor may be shortened when the feature presents an active security risk... The shortened window must still provide at least ninety days between the feature becoming Deprecated and its earliest removal" ([Feature Lifecycle](https://modelcontextprotocol.io/community/feature-lifecycle.md)).

**SOURCE FACT:** "Features may remain Deprecated, without removal, for much longer than the minimum deprecation window" ([Feature Lifecycle](https://modelcontextprotocol.io/community/feature-lifecycle.md)).

### 3.3 The deprecated registry and Tier 1 SDK obligations

**SOURCE FACT:** "`docs/specification/draft/deprecated.mdx` is a single page listing every feature in a Deprecated or Removed state. It is the canonical answer to 'what is on its way out, and by when'" ([Feature Lifecycle](https://modelcontextprotocol.io/community/feature-lifecycle.md)).

**SOURCE FACT:** "Once the revision in which a feature becomes Deprecated is released as Current, Tier 1 SDKs: Must mark the corresponding API surface deprecated using the language's native mechanism (for example `@Deprecated` in Java, `[Obsolete]` in .NET, `@deprecated` JSDoc in TypeScript, the `Deprecated:` doc convention in Go)... Should emit a runtime warning when a deprecated feature is exercised" ([Feature Lifecycle](https://modelcontextprotocol.io/community/feature-lifecycle.md)).

**SOURCE FACT:** "A Tier 1 SDK that consistently fails to surface a Deprecated feature is subject to the Tier Relegation Process" ([Feature Lifecycle](https://modelcontextprotocol.io/community/feature-lifecycle.md)).

**SOURCE FACT:** "Once a feature is set for removal, the removal is executed at the discretion of the Core Maintainers after the minimum deprecation window has elapsed," and "A SEP is required for any change to the original deprecation or removal SEP" ([Feature Lifecycle](https://modelcontextprotocol.io/community/feature-lifecycle.md)).

**SOURCE FACT:** "Lead Maintainers retain veto authority over each of the approvals above, per the governance roles definition" ([Feature Lifecycle](https://modelcontextprotocol.io/community/feature-lifecycle.md)).

### 3.4 SEP-2596: the originating policy SEP

**SOURCE FACT:** SEP-2596 is titled "Specification Feature Lifecycle and Deprecation Policy," status **Final**, type **Process**, created **2026-04-17**, authored by "Den Delimarsky ([@localden])" ([SEP-2596, modelcontextprotocol.io/seps/2596-spec-feature-lifecycle-and-deprecation](https://modelcontextprotocol.io/seps/2596-spec-feature-lifecycle-and-deprecation.md)).

**SOURCE FACT:** SEP-2596's motivation cites prior ad-hoc retirements: "The HTTP+SSE transport is described as 'deprecated'... with no stated removal date"; "The `includeContext` values `"thisServer"` and `"allServers"` are labeled 'soft-deprecated'"; and "JSON-RPC batching was added in revision `2025-03-26` and removed in `2025-06-18`, a single release later, with no deprecation period" ([SEP-2596](https://modelcontextprotocol.io/seps/2596-spec-feature-lifecycle-and-deprecation.md)).

**SOURCE FACT:** SEP-2596 states "The term 'soft-deprecated' is retired. Existing uses in the specification are reclassified as Deprecated under this policy" ([SEP-2596](https://modelcontextprotocol.io/seps/2596-spec-feature-lifecycle-and-deprecation.md)).

**SOURCE FACT:** SEP-2596's transition section gives grandfathered features a "three-month grace period from the date this SEP reaches Final before it is eligible for removal, matching the floor the Expedited removal clause sets for the shortest permissible window" ([SEP-2596](https://modelcontextprotocol.io/seps/2596-spec-feature-lifecycle-and-deprecation.md)).

**SOURCE FACT:** SEP-2596's rationale for twelve months references the "NYC maintainer meeting" which "floated a 'one year supported plus one year deprecation' model and recorded reluctance to commit to longer windows given how quickly the agentic space is moving" ([SEP-2596](https://modelcontextprotocol.io/seps/2596-spec-feature-lifecycle-and-deprecation.md)).

**SOURCE FACT:** SEP-2596's open questions include "**Specification revision support window**," "**Telemetry source for the 'negligible adoption' criterion**," "**Feature maturity tiers**," and "**Wire-level deprecation signal**" ([SEP-2596](https://modelcontextprotocol.io/seps/2596-spec-feature-lifecycle-and-deprecation.md)).

**SOURCE FACT:** SEP-2596 cites external precedents: "the [Kubernetes deprecation policy], the [Node.js deprecation cycle], and IETF practice such as [RFC 8996] (which deprecates TLS 1.0 and 1.1 within the TLS protocol family)" ([SEP-2596](https://modelcontextprotocol.io/seps/2596-spec-feature-lifecycle-and-deprecation.md)).

**AI INFERENCE (from SEP-2596's motivation and the policy's minimum window):** The policy exists specifically because earlier retirements were inconsistent (some immediate, some indefinite); the twelve-month floor plus revision-anchored clock is the mechanism that makes removal dates predictable and shared across features deprecated in the same revision.

### 3.5 SEP-2577: deprecating Roots, Sampling, and Logging

**SOURCE FACT:** SEP-2577 is titled "Deprecate Roots, Sampling, and Logging," status **Final**, type **Standards Track**, created **2026-04-14**, authored by "Kurtis Van Gent ([@kurtisvg])" ([SEP-2577, modelcontextprotocol.io/seps/2577-deprecate-roots-sampling-and-logging](https://modelcontextprotocol.io/seps/2577-deprecate-roots-sampling-and-logging.md)).

**SOURCE FACT:** SEP-2577 deprecates "**Roots** (`roots/list`, `notifications/roots/list_changed`)," "**Sampling** (`sampling/createMessage`, `ClientCapabilities.tasks.requests.sampling`)," and "**Logging** (`logging/setLevel`, `notifications/message`)" ([SEP-2577](https://modelcontextprotocol.io/seps/2577-deprecate-roots-sampling-and-logging.md)).

**SOURCE FACT:** "During the deprecation period, wire-level behavior is unchanged. No types are removed, no capability negotiation changes, and no existing implementations break" ([SEP-2577](https://modelcontextprotocol.io/seps/2577-deprecate-roots-sampling-and-logging.md)).

**SOURCE FACT:** On Roots, SEP-2577 cites "**Low adoption**: Few clients implement roots support, and few servers rely on it," "**Vague semantics**: The specification describes roots as informational — servers are not required to respect them," and "**Overlapping alternatives**: Working directory context can be provided through tool parameters, resource URIs, server configuration, or environment variables" ([SEP-2577](https://modelcontextprotocol.io/seps/2577-deprecate-roots-sampling-and-logging.md)).

**SOURCE FACT:** On Sampling, SEP-2577 cites "**Complex to implement**," "**Low adoption**," and "**Direct alternatives**: Servers that need LLM capabilities can integrate directly with LLM provider APIs" ([SEP-2577](https://modelcontextprotocol.io/seps/2577-deprecate-roots-sampling-and-logging.md)).

**SOURCE FACT:** On Logging, SEP-2577 cites "**Overlapping infrastructure**: Standard logging mechanisms (stderr for stdio transports, OpenTelemetry for structured observability) are mature, widely adopted, and better suited to logging than an application-protocol channel" ([SEP-2577](https://modelcontextprotocol.io/seps/2577-deprecate-roots-sampling-and-logging.md)).

**SOURCE FACT:** SEP-2577's security rationale says "**Sampling** is the most security-sensitive of the three. It allows servers to request LLM completions through the client, which creates attack surface for prompt injection and data exfiltration," and "**Roots** exposes information about the client's filesystem to servers" ([SEP-2577](https://modelcontextprotocol.io/seps/2577-deprecate-roots-sampling-and-logging.md)).

**SOURCE FACT:** SEP-2577's timeline says "**Deprecated**: In the next specification release (currently planned for June 2026)" and "**Removal**: Specification versions released more than one year after this version's release MAY remove these features entirely" ([SEP-2577](https://modelcontextprotocol.io/seps/2577-deprecate-roots-sampling-and-logging.md)).

**SOURCE FACT:** SEP-2577 states "No reference implementation is required. This SEP only marks existing functionality as deprecated — no new protocol behavior is introduced" ([SEP-2577](https://modelcontextprotocol.io/seps/2577-deprecate-roots-sampling-and-logging.md)).

**AI INFERENCE (from SEP-2577's deprecation list and the 2026-07-28 registry):** The three features deprecated by SEP-2577 are exactly the three core features (Roots, Sampling, Logging) that a server implementer might otherwise build on; the SEP's own rationale directs server authors to tool parameters/resource URIs/server config (for Roots), direct LLM provider APIs (for Sampling), and stderr/OpenTelemetry (for Logging).

---

## 4. Currently Deprecated Features in Revision 2026-07-28

**SOURCE FACT:** The deprecated-features page "is the registry of specification features that are currently in the **Deprecated** state under the feature lifecycle and deprecation policy ([SEP-2596])" ([Deprecated Features, modelcontextprotocol.io/specification/2026-07-28/deprecated](https://modelcontextprotocol.io/specification/2026-07-28/deprecated.md)).

**SOURCE FACT:** "A Deprecated feature remains part of the specification but is scheduled for removal: new implementations **SHOULD NOT** adopt it, and existing implementations **SHOULD** migrate before the feature's earliest removal" ([Deprecated Features](https://modelcontextprotocol.io/specification/2026-07-28/deprecated.md)).

**SOURCE FACT:** The registry lists six deprecated rows ([Deprecated Features](https://modelcontextprotocol.io/specification/2026-07-28/deprecated.md)):

| Feature | Deprecation SEP | Deprecated in | Migration path | Earliest removal |
| - | - | - | - | - |
| Roots | SEP-2577 | `2026-07-28` | Pass directories or files via tool parameters, resource URIs, or server configuration | First revision released on or after 2027-07-28 |
| Sampling | SEP-2577 | `2026-07-28` | Integrate directly with LLM provider APIs | First revision released on or after 2027-07-28 |
| Logging | SEP-2577 | `2026-07-28` | Log to `stderr` for stdio transports; use OpenTelemetry for observability | First revision released on or after 2027-07-28 |
| Dynamic Client Registration | PR #2858 | `2026-07-28` | Client ID Metadata Documents | First revision released on or after 2027-07-28 |
| `includeContext: "thisServer"` / `"allServers"` (Sampling) | SEP-2596 | `2025-11-25` | Omit the field or use `"none"` | Follows Sampling (SEP-2577) |
| HTTP+SSE transport | SEP-2596 | `2025-03-26` | Streamable HTTP | Three months after SEP-2596 reaches Final |

**SOURCE FACT:** "The HTTP+SSE transport and the `includeContext` values were already described as deprecated before the lifecycle policy existed; SEP-2596 reclassifies them as Deprecated under its transition provisions" ([Deprecated Features](https://modelcontextprotocol.io/specification/2026-07-28/deprecated.md)).

**SOURCE FACT:** Under "Removed," the page states "No features have been removed under this policy yet. When a Deprecated feature is removed, its row moves to this section with a link to the changelog entry recording the removal" ([Deprecated Features](https://modelcontextprotocol.io/specification/2026-07-28/deprecated.md)).

**SOURCE FACT:** "This registry is a derived view kept consistent with the per-feature deprecation notices and changelog entries, which are the normative records" ([Deprecated Features](https://modelcontextprotocol.io/specification/2026-07-28/deprecated.md)).

**AI INFERENCE (from the six registry rows):** For a server author targeting 2026-07-28, the actionable deprecations are: do not build on Roots, Sampling, or Logging; do not use the HTTP+SSE transport (use Streamable HTTP); do not use the `includeContext` values `"thisServer"`/`"allServers"`; and prefer Client ID Metadata Documents over Dynamic Client Registration. The earliest removal for the four 2026-07-28 deprecations is the first revision on or after 2027-07-28.

**PLAUSIBLE NOT VERIFIED:** The registry row for Dynamic Client Registration cites "PR #2858" rather than a SEP number, and the fetched page does not explain why; it may be a deprecation landed via a pull request under the transition provisions, but the page does not state this.

---

## 5. Working and Interest Groups

### 5.1 The two structures

**SOURCE FACT:** "Within the MCP contributor community we maintain two types of collaboration formats: **Interest Groups (IGs)** and **Working Groups (WGs)**" ([Working and Interest Groups, modelcontextprotocol.io/community/working-interest-groups](https://modelcontextprotocol.io/community/working-interest-groups.md)).

**SOURCE FACT:** An Interest Group's purpose is to "Identify and discuss problems," with output "Problem statements, use cases, recommendations" and "Rough consensus, non-binding" decisions; a Working Group's purpose is to "Build concrete solutions," with output "SEPs, implementations, code" and "Binding (lazy consensus → vote → escalation)" decisions ([Working and Interest Groups](https://modelcontextprotocol.io/community/working-interest-groups.md)).

**SOURCE FACT:** "**Typical flow**: Discuss a problem in an IG → Validate that it's worth solving → Form or join a WG to build the solution → Submit a SEP → Implement" ([Working and Interest Groups](https://modelcontextprotocol.io/community/working-interest-groups.md)).

**SOURCE FACT:** IG examples include "Security in MCP," "Auth in MCP," "Using MCP in enterprise settings," and "Tooling and practices for hosting MCP clients"; WG examples include "Registry," "Inspector," "Tool Filtering," and "Server Identity" ([Working and Interest Groups](https://modelcontextprotocol.io/community/working-interest-groups.md)).

**SOURCE FACT:** "**Goal:** Collaborate on a SEP, a series of related SEPs, or an officially endorsed project. WGs produce concrete deliverables," and WGs "Maintain ongoing projects (Inspector, Registry, SDKs)" ([Working and Interest Groups](https://modelcontextprotocol.io/community/working-interest-groups.md)).

### 5.2 Governance of groups

**SOURCE FACT:** "Each group has one or more **Leads** (referred to as **Facilitators** for Interest Groups)," and "Group and its leadership sponsored by at least two Core Maintainers or one Lead Maintainer" ([Working and Interest Groups](https://modelcontextprotocol.io/community/working-interest-groups.md)).

**SOURCE FACT:** "**Additional requirements for WG Leads:** Commitment to 2-3 hours/week for WG activities" ([Working and Interest Groups](https://modelcontextprotocol.io/community/working-interest-groups.md)).

**SOURCE FACT:** WG decision-making progresses through "Lazy Consensus (default)," "Formal Vote (when lazy consensus is blocked)," and "Escalation (when voting does not resolve)"; lazy consensus requires "Proposals announced with clear deadline (5 days minimum for minor items, 10 days for significant items)" and "Silence is consent" ([Working and Interest Groups](https://modelcontextprotocol.io/community/working-interest-groups.md)).

**SOURCE FACT:** A formal vote has "Quorum: 50% of active WG Members" and "Passage: simple majority for routine matters; 2/3 majority for scope changes" ([Working and Interest Groups](https://modelcontextprotocol.io/community/working-interest-groups.md)).

**SOURCE FACT:** "All group meetings must: Be open to all community participants (no closed or organization-internal meetings); Be published on meet.modelcontextprotocol.io at least 7 days in advance; Have agendas published and publicly available...; Have notes published within 48 hours" ([Working and Interest Groups](https://modelcontextprotocol.io/community/working-interest-groups.md)).

**SOURCE FACT:** "**Working Groups** provide quarterly updates (end of January, April, July, October)" ([Working and Interest Groups](https://modelcontextprotocol.io/community/working-interest-groups.md)).

**SOURCE FACT:** "**Do I need to be in a WG to submit a SEP?** No. Anyone can submit a SEP, and group membership is not required. The proposal must still be brought to the relevant group's Discord channel before the SEP pull request is opened" ([Working and Interest Groups](https://modelcontextprotocol.io/community/working-interest-groups.md)).

**SOURCE FACT:** The page references "SEP-2149: MCP Group Governance and Charter Template" for the full governance rules ([Working and Interest Groups](https://modelcontextprotocol.io/community/working-interest-groups.md)).

**AI INFERENCE (from the WG examples and the Registry/SDKs maintenance facts):** For a server implementer, the most directly relevant groups are the Registry WG (publishing/distribution), the SDKs WG (SDK behavior and tiering), the Inspector WG (debugging), and the Server Identity WG (identity verification); the Transports, Server Card, and Agents groups named in the task are not explicitly listed on this fetched page, so their existence is not confirmed here.

**UNKNOWN:** The fetched working-interest-groups page does not enumerate a "Transports" WG, a "Server Card" WG, or an "Agents" WG by those names. It lists "Registry," "Inspector," "Tool Filtering," and "Server Identity" as WG examples and "Security in MCP," "Auth in MCP," "Using MCP in enterprise settings," and "Tooling and practices for hosting MCP clients" as IG examples. The task's named groups (Transports, Server Card, Agents) could not be confirmed from this source.

---

## 6. Retrieval log

All URLs requested for this file were retrieved successfully on 2026-10-02:

| URL | Result |
| - | - |
| https://modelcontextprotocol.io/community/governance.md | Retrieved |
| https://modelcontextprotocol.io/community/sep-guidelines.md | Retrieved |
| https://modelcontextprotocol.io/community/feature-lifecycle.md | Retrieved |
| https://modelcontextprotocol.io/community/design-principles.md | Retrieved |
| https://modelcontextprotocol.io/community/working-interest-groups.md | Retrieved |
| https://modelcontextprotocol.io/community/contributor-ladder.md | Retrieved |
| https://modelcontextprotocol.io/specification/2026-07-28/deprecated.md | Retrieved |
| https://modelcontextprotocol.io/seps/index.md | Retrieved |
| https://modelcontextprotocol.io/seps/2596-spec-feature-lifecycle-and-deprecation.md | Retrieved |
| https://modelcontextprotocol.io/seps/2577-deprecate-roots-sampling-and-logging.md | Retrieved |
| https://modelcontextprotocol.io/seps/1850-pr-based-sep-workflow.md | Retrieved |

**UNKNOWN:** The fetched sources do not provide a complete, authoritative list of all current Working Groups and Interest Groups; the working-interest-groups page points to Discord channels and `docs/community/` in the repository for the full list. The specific groups named in the task brief (Transports, Registry, Server Card, Agents) are only partially confirmed: Registry is confirmed as a WG example, while Transports, Server Card, and Agents are not named on the fetched page.
