---
name: news-aggregator
description: This skill should be used when the user asks what happened today or on a given date, asks for news from a country, region, or topic, or asks which current events matter for their own life. It collects headlines, delegates multi-source verification of each event to subagents with a structured fact template, and ranks the events in the main thread by personal impact across life aspects and time horizons, based on the user's profile file.
metadata:
  version: "0.1"
---

# News Aggregator

## Overview

Produce a news digest that separates confirmed facts from speculation, cites several independent sources for each event, and ranks events by their impact on the user's life. Subagents verify the facts. The main thread owns the impact assessment and the ranking.

## Resources

- [assets/worker-prompt-template.md](assets/worker-prompt-template.md) — prompt template for each research subagent.
- [assets/report-template.md](assets/report-template.md) — format of the final report in the main thread.
- [assets/profile-template.md](assets/profile-template.md) — fields of the user profile file.

Resolve these paths relative to this skill directory.

## Workflow

### Step 1: Load the user profile

Read `~/.config/opencode/news-profile.md`.

If the file does not exist:

1. Tell the user that the impact ranking needs a profile.
2. Ask for the profile fields from `assets/profile-template.md` through the question tool. Ask only the fields that change the ranking.
3. Propose to save the answers to `~/.config/opencode/news-profile.md`. Create the file only after the user approves.

Do not write personal data to any other location. Do not commit the profile to Git.

### Step 2: Collect candidate events

Search the web for the requested date, country, region, or topic. Use aggregate sources first: newsroom timelines, daily press reviews, and "top news of the day" pages. Use sources in the language of the country concerned.

Select candidate events. Show the user a short list grouped by area. Continue to Step 3 when the user asks for a deeper analysis, or when the request already asks for it.

### Step 3: Delegate verification to subagents

Group the events by area, for example security, economy and finance, daily life and society. Put 3–6 events in each group.

For each group, start one `general` subagent with a prompt built from `assets/worker-prompt-template.md`. Fill all placeholders. Run the subagents in parallel.

Do not pass the user profile to the subagents. Subagents report facts and generic implications only. The personal assessment stays in the main thread.

### Step 4: Check the subagent results

For each event, check that the result contains:

- facts with a separate list of confirmed and speculative items,
- at least two independent sources with name, date, and URL,
- an explicit statement for each unknown item.

If an event fails a check, resume that subagent with its session ID and name the missing items. Do not fill the gaps from your own knowledge.

### Step 5: Assess personal impact

For each event, assess the impact on the user against the profile. Use the aspects and the horizons below.

**Aspects:**

| Aspect | Scope |
|---|---|
| Finance | prices, taxes, loan installments, benefits, cost of living |
| Law and obligations | new rights, obligations, formal deadlines, bans |
| Security | physical safety, civil protection, threats |
| Daily life | transport, weather, services, shopping, daily logistics |
| Work and career | labor market, industry, jobs in the user's region |
| Health | health, medical services, public health insurance |
| Family | children, education, care |

**Time horizons** (the time when the impact starts for the user):

| Horizon | Meaning |
|---|---|
| H1 | today or tomorrow |
| H2 | up to one month |
| H3 | up to one year |
| H4 | 1–5 years |
| H5 | more than 5 years, or context only |

For each event, record:

- the affected aspects, each with a concrete effect on the user (for example "+6.50 PLN per 50 l tank"),
- the horizon,
- whether the effect is direct or indirect,
- the profile fields that support the assessment.

If the effect depends on a speculative item or on a missing profile field, state this. Do not present the consequence of an assumption as a fact.

### Step 6: Rank and report

Sort the events by horizon first (H1 before H5). Within one horizon, put direct effects before indirect effects, then put events with more affected aspects first.

Write the report with `assets/report-template.md`. Write in the user's language. End with a short summary of the 1–3 events that matter most for the user.

## Rules

- Use only facts from the sources. Put interpretation only in the assessment sections.
- Mark the status of each event precisely: "detention, not a verdict", "bill, not a law", "model scenario, not an official forecast".
- Quote official statements word for word, with name and function.
- Do not drop an event because its impact is low. Put it in the last horizon.
