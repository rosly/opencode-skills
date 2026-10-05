# KISS and the Subtractive Completion Criterion

This file supports the uber rule in `SKILL.md`: apply KISS whenever writing new code, and treat removal as the measure of completion. It records the sourced origin of both ideas and the caveats.

## KISS — origin and meaning

- SOURCE CLAIM (Rank 4, Wikipedia): "KISS ('Keep it simple, stupid') is a design principle first noted by the U.S. Navy in 1960." ([KISS principle](https://en.wikipedia.org/wiki/KISS_principle)).
- SOURCE CLAIM (Rank 4): "The acronym 'Keep it simple, stupid' was reportedly coined by Kelly Johnson, lead engineer at the Lockheed Skunk Works" — note the hedge "reportedly" ([KISS principle](https://en.wikipedia.org/wiki/KISS_principle)). The underlying citation is Ben Rich's 1995 National Academies biographical memoir of Johnson, not fetched directly.
- SOURCE CLAIM (Rank 4): The phrase predates the acronym in a variant form — "the variant 'Keep it Short and Simple' is attested from a 1938 issue of the *Minneapolis Star*" ([KISS principle](https://en.wikipedia.org/wiki/KISS_principle)). Johnson wrote it without the comma: "Keep it simple stupid".
- SOURCE CLAIM (Rank 4): The canonical illustration is Johnson handing engineers a handful of tools and requiring the aircraft be "repairable by an average mechanic in the field under combat conditions with only these tools. Hence, the 'stupid' refers to the relationship between the way things break and the sophistication available to repair them" ([KISS principle](https://en.wikipedia.org/wiki/KISS_principle)).

AI INFERENCE: KISS is a design directive — prefer the simplest solution that works — and its original justification is operational (repairability under constraint), not aesthetic. The "stupid" is not an insult to the designer; it is a constraint on the repair environment.

## The Saint-Exupéry quote — original, translation, context

- SOURCE CLAIM (Rank 4 reproduction of a primary text; *Terre des hommes*, 1939, ch. III "L'Avion", p. 59): The French original is "Il semble que la perfection soit atteinte non quand il n'y a plus rien à ajouter, mais quand il n'y a plus rien à retrancher." ([fr.wikiquote, Terre des hommes](https://fr.wikiquote.org/wiki/Terre_des_hommes)).
- SOURCE CLAIM (Rank 5, StackExchange): The common English rendering is "...perfection is finally attained not when there is no longer anything to add, but when there is no longer anything to take away..." and the fuller passage continues "...when a body has been stripped down to its nakedness" ([English StackExchange](https://english.stackexchange.com/questions/38837/where-does-this-translation-of-saint-exuperys-quote-on-design-come-from)).

AI INFERENCE: Two things are usually lost in the popular paraphrase. First, the original context is the airplane, not design in general — Saint-Exupéry describes how an aircraft reaches its final form by removing everything non-essential. Second, the verb is *retrancher* ("to cut away / prune"), more aggressive than "take away"; the image is subtractive. The popular version "Perfection is achieved, not when there is nothing more to add, but when there is nothing left to take away" is a paraphrase, not a literal translation.

## How the two connect

- SOURCE CLAIM (Rank 4): Wikipedia lists the Saint-Exupéry line among the minimalist concepts that KISS "most probably finds its origins in", alongside Occam's razor, Mies van der Rohe's "Less is more", "Simplicity is the ultimate sophistication", and Colin Chapman's "Simplify, then add lightness" ([KISS principle](https://en.wikipedia.org/wiki/KISS_principle)).

AI INFERENCE: The two ideas are complementary but not identical:

- KISS answers "what should the design be?" — prefer simplicity.
- Saint-Exupéry answers "when is it finished?" — when nothing more can be removed.

Together they give a subtractive completion criterion: simplicity is not achieved by adding the right abstractions, but by removing everything that is not load-bearing. This is stronger than "keep it simple" — it makes removal the measure of done.

## Software-engineering lineage

- SOURCE CLAIM (Rank 4): Wikipedia places KISS in software alongside DRY, YAGNI, the Unix philosophy, minimalism, and "worse is better" ([KISS principle](https://en.wikipedia.org/wiki/KISS_principle)).
- SOURCE CLAIM (Rank 3, Laws of Software Engineering): C.A.R. Hoare's framing is quoted: "There are two ways of constructing a software design: One way is to make it so simple that there are obviously no deficiencies, and the other way is to make it so complicated that there are no obvious deficiencies. The first method is far more difficult." ([Laws of Software Engineering](https://lawsofsoftwareengineering.com/laws/kiss-principle/)).

AI INFERENCE: The subtractive criterion maps directly onto TDD's refactor step. Beck's second rule is "Eliminate duplication" and the goal is "clean code that works" (`02-cycle-mechanics.md` §3); Fowler's simple-design criteria are "Runs all the Tests", "No duplication", "Reveals all the intention", "Fewest number of classes or methods" (`06-design-outcomes.md` §2). "Nothing left to remove" is the same instinct as "no duplication" and "fewest classes or methods" — a completion test based on subtraction.

## Caveats and conflicts

- Attribution is hedged. Wikipedia says "reportedly coined" for Johnson; the 1960 U.S. Navy "Project KISS" and the 1938 "Keep it Short and Simple" variant are separate data points. Treat "Kelly Johnson invented KISS" as a widely repeated attribution, not a settled fact.
- The quote is a paraphrase. The French original and the popular English version differ in wording and context; the "designer knows he has achieved perfection" form is a later adaptation.
- "As simple as possible, but not simpler" is attributed to Einstein but Wikipedia flags it as "possibly an editor's paraphrase of a lecture he gave" ([KISS principle](https://en.wikipedia.org/wiki/KISS_principle)) — do not present it as a verified Einstein quote.
- Simplicity is conditional, not absolute. YAGNI and simple design are safe only when refactoring and tests keep the cost of change low (`06-design-outcomes.md` §2). "Nothing to remove" is a good stopping rule only if the design is already correct; removing a needed abstraction is not simplicity.

## Operational rule for the agent

After reaching green, ask "what can I delete?" before "what can I add?". Prefer the simplest thing that works, resist speculative generality, and consider the design finished when there is nothing left to remove. This is the refactor discipline in `02-cycle-mechanics.md` §3 and the simple-design criteria in `06-design-outcomes.md` §2.
