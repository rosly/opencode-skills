# Topic 6 — Design outcomes: emergent design, testability, seams, and legacy code

Retrieved: 2026-10-05. Version under study: TDD as described by Kent Beck (2002/2003) and the XP/evolutionary-design literature; legacy-code techniques as published by Michael Feathers (2004). Language scope: paradigm-neutral / xUnit-family concepts only; no language- or framework-specific APIs.

Core question: How does TDD drive emergent design, testability, seams, and legacy-code work?

Evidence labels used: SOURCE FACT (Rank 1), SOURCE CLAIM (Rank 2–6), AI INFERENCE, PLAUSIBLE NOT VERIFIED, UNKNOWN. Rank 1 is reserved for directly inspected source code or scientific papers; the sources here are author pages, publisher excerpts, and interviews, so they are labelled SOURCE CLAIM with their rank.

## 1. Emergent / evolutionary design

- SOURCE CLAIM (Rank 2): Fowler defines evolutionary design as growth during implementation — "evolutionary design means that the design of the system grows as the system is implemented" and "Design is part of the programming processes and as the program evolves the design changes" ([Is Design Dead?](https://martinfowler.com/articles/designDead.html)).
- SOURCE CLAIM (Rank 2): Fowler states the enabling practices that make evolutionary design viable — "These enabling practices of continuous integration, testing, and refactoring, provide a new environment that makes evolutionary design plausible" ([Is Design Dead?](https://martinfowler.com/articles/designDead.html)).
- SOURCE CLAIM (Rank 2): Fowler frames TDD's design effect as interface-first thinking — "thinking about the test first forces us to think about the interface to the code first" and "This focus on interface and how you use a class helps us separate interface from implementation, a key element of good design" ([Test Driven Development](https://martinfowler.com/bliki/TestDrivenDevelopment.html)).
- SOURCE CLAIM (Rank 2): Fowler states test sequencing is a design skill — "we want to pick tests that drive us quickly to the salient points in the design" ([Test Driven Development](https://martinfowler.com/bliki/TestDrivenDevelopment.html)).
- SOURCE CLAIM (Rank 2): Fowler warns that omitting refactoring defeats the design benefit — "Refactoring the code to keep it clean is a key part of the process, otherwise we just end up with a messy aggregation of code fragments" ([Test Driven Development](https://martinfowler.com/bliki/TestDrivenDevelopment.html)).
- SOURCE CLAIM (Rank 2): Kent Beck describes design as a deliberate checkpoint inside the TDD cycle — "After I get a test running, I think about, and sometimes execute on, the question, 'What is the design which, if I had had it, would have made that implementation easier?'" and "When I go to write a new test, I necessarily make API design decisions" ([Design in TDD](https://newsletter.kentbeck.com/p/design-in-tdd)).
- SOURCE CLAIM (Rank 2): Beck argues for later, better-informed design — "The earlier you make design decisions, the less informed you are when you make those decisions" ([Design in TDD](https://newsletter.kentbeck.com/p/design-in-tdd)).
- SOURCE CLAIM (Rank 5): A community quote aggregator attributes to Beck's book — "TDD helps you to pay attention to the right issues at the right time so you can make your designs cleaner, you can refine your designs as you learn" and "As you refine the design, more and more changes become possible" ([Goodreads: Test-Driven Development quotes](https://www.goodreads.com/work/quotes/376827-test-driven-development-by-example)). Rank 5: user-submitted quotes, not independently verified against the printed book.
- AI INFERENCE: The sources converge on a mechanism, not a guarantee: writing a failing test first fixes the caller's view of the interface, and the refactor step is where structure is improved. Emergent design is therefore conditional on the refactor step and on low change cost, not an automatic product of test-first ordering.

## 2. YAGNI and simplicity

- SOURCE CLAIM (Rank 2): Fowler states YAGNI — "you shouldn't add any code today which will only be used by feature that is needed tomorrow" ([Is Design Dead?](https://martinfowler.com/articles/designDead.html)).
- SOURCE CLAIM (Rank 2): Fowler conditions YAGNI on low change cost — "you can only sensibly behave this way when you are using XP, or a similar technique that lowers the cost of change" ([Is Design Dead?](https://martinfowler.com/articles/designDead.html)).
- SOURCE CLAIM (Rank 2): Fowler lists Beck's four simple-design criteria in priority order — "Runs all the Tests", "No duplication", "Reveals all the intention", "Fewest number of classes or methods" ([Is Design Dead?](https://martinfowler.com/articles/designDead.html)).
- SOURCE CLAIM (Rank 2): Fowler reports a practitioner heuristic on over-design — "it's easier to refactor over-design than it is to refactor no design" ([Is Design Dead?](https://martinfowler.com/articles/designDead.html)).
- SOURCE CLAIM (Rank 2): Fowler reports Robert Martin's advice — "the willingness to refactor is much more important than knowing what the simplest thing is right away" ([Is Design Dead?](https://martinfowler.com/articles/designDead.html)).
- SOURCE CLAIM (Rank 2): Fowler reconciles refactoring with YAGNI — "Refactoring is needed to keep the design as simple as you can, so you should refactor whenever you realize you can make things simpler" ([Is Design Dead?](https://martinfowler.com/articles/designDead.html)).
- SOURCE CLAIM (Rank 2): Fowler states the cost of unneeded complexity — "Any unneeded complexity makes a system harder to change in all directions except the one you anticipate with the complex flexibility you put in" ([Is Design Dead?](https://martinfowler.com/articles/designDead.html)).
- SOURCE CLAIM (Rank 2): Fowler's architecture advice — "begin by assessing what the likely architecture is" but "when in doubt err on the side of simplicity" ([Is Design Dead?](https://martinfowler.com/articles/designDead.html)).
- AI INFERENCE: YAGNI and simple design are presented as safe only when refactoring plus tests keep the cost of change low; without that enabling set, the same advice is described as harmful. This makes "simplicity" a strategy coupled to a change-cost assumption, not an unconditional rule.

## 3. Testability as design pressure

- SOURCE CLAIM (Rank 2): Feathers states the diagnostic link between test difficulty and design — "when you have trouble testing something, look for the design problem because it's there to see where things could be different" ([InfoQ podcast transcript](https://www.infoq.com/podcasts/working-effectively-legacy-code/)).
- SOURCE CLAIM (Rank 2): Feathers states that testing reveals modularity — "testing tells you a lot about modularity in your systems" ([InfoQ podcast transcript](https://www.infoq.com/podcasts/working-effectively-legacy-code/)).
- SOURCE CLAIM (Rank 2): Feathers states the causal direction for legacy code — "the reason why code is so difficult to get tests around quite often is because it wasn't designed with testing in mind" ([InfoQ podcast transcript](https://www.infoq.com/podcasts/working-effectively-legacy-code/)).
- SOURCE CLAIM (Rank 2): Fowler states that designing with testing in mind yields seams — "If we write our software with testing in mind, we tend to get a good set of seams, which is a reason why Test Driven Development is such a useful technique" ([Legacy Seam](https://martinfowler.com/bliki/LegacySeam.html)).
- SOURCE CLAIM (Rank 3): A practitioner book excerpt states the design-pressure thesis — "Designing for testability really means designing for extensibility" and "We view TDD as a design practice first, and a testing practice second" ([On Coupling and Abstractions](https://www.obeythetestinggoat.com/new-book-excerpt-abstractions.html)). Rank 3: original practitioner work, but the excerpt's code examples are language-specific and are not relied on here.
- AI INFERENCE: Testability functions as a feedback signal on structure: a dependency that cannot be substituted in a test is treated as evidence of a design problem (tight coupling, hidden construction, or I/O mixed with logic). This is the "design pressure" mechanism — the test harness makes coupling visible and costly, which pushes toward substitutable collaborators.

## 4. Coupling and cohesion effects

- SOURCE CLAIM (Rank 3): The excerpt defines coupling by change risk — "When we're unable to change component A for fear of breaking component B, we say that the components have become coupled" ([On Coupling and Abstractions](https://www.obeythetestinggoat.com/new-book-excerpt-abstractions.html)).
- SOURCE CLAIM (Rank 3): The excerpt distinguishes local from global coupling — "Locally, coupling is a good thing... high cohesion between the coupled elements" but "Globally, coupling is a nuisance: it increases the risk and the cost of changing our code" ([On Coupling and Abstractions](https://www.obeythetestinggoat.com/new-book-excerpt-abstractions.html)).
- SOURCE CLAIM (Rank 3): The excerpt states that abstractions reduce coupling — "we have reduced the degree of coupling by inserting a new, simpler, abstraction. This abstraction serves to protect us from change by hiding away the complex details" ([On Coupling and Abstractions](https://www.obeythetestinggoat.com/new-book-excerpt-abstractions.html)).
- SOURCE CLAIM (Rank 3): The excerpt describes separating logic from I/O to enable testing — "we can make our systems easier to test and maintain by simplifying the interface between our business logic and messy IO" ([On Coupling and Abstractions](https://www.obeythetestinggoat.com/new-book-excerpt-abstractions.html)).
- AI INFERENCE: The coupling/cohesion account explains why testability pressure improves design: tests require substituting collaborators, and substitution requires an abstraction boundary. Inserting that boundary lowers global coupling while keeping cohesive behavior together, which is the same structural change that improves maintainability.

## 5. Dependency injection and explicit dependencies

- SOURCE CLAIM (Rank 2): Fowler shows parameter passing as a seam — "One way to do this is to pass the function for `calculateShipping` as a parameter" and "Passing the function as parameter opens up an enabling point in the caller" ([Legacy Seam](https://martinfowler.com/bliki/LegacySeam.html)).
- SOURCE CLAIM (Rank 2): Fowler notes the trade-off of threading dependencies through a legacy call stack — "changing the signature of `calculateShipping` may be fraught, and we may not want to thread the shipping function parameter through the legacy call stack" ([Legacy Seam](https://martinfowler.com/bliki/LegacySeam.html)).
- SOURCE CLAIM (Rank 2): Fowler presents lookup-based alternatives — "a lookup may be a better approach, such as using a service locator" ([Legacy Seam](https://martinfowler.com/bliki/LegacySeam.html)).
- SOURCE CLAIM (Rank 3): The excerpt shows constructor/parameter injection without requiring an interface — "although we're using dependency injection, there was no need to define an abstract base class or any kind of explicit interface" ([On Coupling and Abstractions](https://www.obeythetestinggoat.com/new-book-excerpt-abstractions.html)).
- SOURCE CLAIM (Rank 2): Feathers names the highest-value dependency-breaking techniques — "the main one really is parameterized constructor... the parameterized method is another one... Introducing interfaces and places where they don't exist, extract interface" ([InfoQ podcast transcript](https://www.infoq.com/podcasts/working-effectively-legacy-code/)).
- AI INFERENCE: Dependency injection is treated here as a means to create a seam, not as an end in itself. The sources offer at least three substitutability mechanisms (parameter passing, constructor injection, lookup/service locator), and the choice is described as dependent on language and legacy constraints.

## 6. Seams (Michael Feathers)

- SOURCE CLAIM (Rank 2): Feathers' canonical definition, quoted by Fowler — "a seam is a place where you can alter behavior in your program without editing in that place" ([Legacy Seam](https://martinfowler.com/bliki/LegacySeam.html)).
- SOURCE CLAIM (Rank 2): Feathers' own publisher excerpt gives the same definition — "A seam is a place where you can alter behavior in your program without editing in that place" ([Testing Effectively With Legacy Code, InformIT](https://www.informit.com/articles/article.aspx?p=359417&seqNum=3)).
- SOURCE CLAIM (Rank 2): Feathers defines the enabling point — "Every seam has an enabling point, a place where you can make the decision to use one behavior or another" ([Testing Effectively With Legacy Code, InformIT](https://www.informit.com/articles/article.aspx?p=359417&seqNum=3)).
- SOURCE CLAIM (Rank 2): Feathers classifies seam types by build stage — "Preprocessing Seams", "Link Seams", and "Object Seams" ([Testing Effectively With Legacy Code, InformIT](https://www.informit.com/articles/article.aspx?p=359417&seqNum=3)).
- SOURCE CLAIM (Rank 2): Feathers ranks object seams highest in OO languages — "In general, object seams are the best choice in object-oriented languages" ([Testing Effectively With Legacy Code, InformIT](https://www.informit.com/articles/article.aspx?p=359417&seqNum=3)).
- SOURCE CLAIM (Rank 2): Feathers states the structural payoff — "When you get used to seeing code in terms of seams, it is easier to see how to test things and to see how to structure new code to make testing easier" ([Testing Effectively With Legacy Code, InformIT](https://www.informit.com/articles/article.aspx?p=359417&seqNum=3)).
- SOURCE CLAIM (Rank 2): Feathers states the minimal-change principle for legacy work — "If you know the seams that your language offers and how to use them, you can often get tests in place more safely than you could otherwise" ([Testing Effectively With Legacy Code, InformIT](https://www.informit.com/articles/article.aspx?p=359417&seqNum=3)).
- SOURCE CLAIM (Rank 2): Feathers' interview definition — "It's a place in your code where you can go and separate things for testing without doing any extra work" ([InfoQ podcast transcript](https://www.infoq.com/podcasts/working-effectively-legacy-code/)).
- SOURCE CLAIM (Rank 2): Fowler lists seam uses beyond testing — "Once we've found a seam, we can use it to break dependencies to simplify testing, insert probes to gain observability, and redirect program flow to new modules as part of legacy displacement" ([Legacy Seam](https://martinfowler.com/bliki/LegacySeam.html)).
- AI INFERENCE: A seam is defined by substitutability at a point without editing that point; the enabling point is where the substitution decision is made. This separates "where behavior can vary" from "where the choice is made", which is why a seam can be exploited from test code while production source stays unchanged.

## 7. Characterization tests

- SOURCE CLAIM (Rank 2): Feathers' interview definition — "within the book, I define a characterization test as essentially a test that you write to understand the behavior of the system" ([InfoQ podcast transcript](https://www.infoq.com/podcasts/working-effectively-legacy-code/)).
- SOURCE CLAIM (Rank 2): Feathers states the actual-vs-correct distinction — "the tests aren't really defining correct behavior, they're really defining actual behavior for the codebase" ([InfoQ podcast transcript](https://www.infoq.com/podcasts/working-effectively-legacy-code/)).
- SOURCE CLAIM (Rank 3): A practitioner summary quotes the book — "A characterization test is a test that characterizes the actual behavior of a piece of code" ([The key points of Working Effectively with Legacy Code](https://understandlegacycode.com/blog/key-points-of-working-effectively-with-legacy-code/)).
- SOURCE CLAIM (Rank 4): Wikipedia's definition — "a means to describe (characterize) the actual behavior of an existing piece of software, and therefore protect existing behavior of legacy code against unintended changes via automated testing" ([Characterization test](https://en.wikipedia.org/wiki/Characterization_test)). Rank 4: orientation only; the same page also lists the alias "Golden Master Testing".
- SOURCE CLAIM (Rank 2): Feathers describes the mechanical procedure — "you can just go and write a test and say... the return results should be zero... But then you get the actual return result and then you take that and you make that the expected value" ([InfoQ podcast transcript](https://www.infoq.com/podcasts/working-effectively-legacy-code/)).
- SOURCE CLAIM (Rank 2): Feathers notes the naming variant — "more recently, I've heard some people would call them pinning tests" ([InfoQ podcast transcript](https://www.infoq.com/podcasts/working-effectively-legacy-code/)).
- AI INFERENCE: A characterization test is a behavior-pinning test written after the fact against existing code. Its purpose is a regression safety net for refactoring, not a specification of desired behavior; the expected values are captured from observed output rather than asserted from intent.

## 8. Applying TDD to legacy code — the workflow

- SOURCE CLAIM (Rank 3): The practitioner summary quotes the book's definition of legacy code — "Legacy Code is code without tests" ([The key points of Working Effectively with Legacy Code](https://understandlegacycode.com/blog/key-points-of-working-effectively-with-legacy-code/)).
- SOURCE CLAIM (Rank 3): The summary states the ordering principle — "First, add tests, then do your changes" and "Before you change code, you should have tests in place" ([The key points of Working Effectively with Legacy Code](https://understandlegacycode.com/blog/key-points-of-working-effectively-with-legacy-code/)).
- SOURCE CLAIM (Rank 3): The summary states the legacy-code dilemma — "Before you change code, you should have tests in place. But to put tests in place, you have to change code" ([The key points of Working Effectively with Legacy Code](https://understandlegacycode.com/blog/key-points-of-working-effectively-with-legacy-code/)).
- SOURCE CLAIM (Rank 3): The summary gives the recipe — "1. Identify change points (Seams) 2. Break dependencies 3. Write the tests 4. Make your changes 5. Refactor" ([The key points of Working Effectively with Legacy Code](https://understandlegacycode.com/blog/key-points-of-working-effectively-with-legacy-code/)).
- SOURCE CLAIM (Rank 3): The summary states the minimal-change rule — "Change as little code as possible to get tests in place" ([The key points of Working Effectively with Legacy Code](https://understandlegacycode.com/blog/key-points-of-working-effectively-with-legacy-code/)).
- SOURCE CLAIM (Rank 2): Feathers describes the sprout technique — "rather than modifying this existing piece of code, can I just write the new functionality in a new class or method and then delegate to it from the existing monolith" ([InfoQ podcast transcript](https://www.infoq.com/podcasts/working-effectively-legacy-code/)).
- SOURCE CLAIM (Rank 3): The summary describes the wrap technique — "Rename the old method you want to wrap. Create a new method with the same name and signature as the old method. Call the old method from the new method" ([The key points of Working Effectively with Legacy Code](https://understandlegacycode.com/blog/key-points-of-working-effectively-with-legacy-code/)).
- SOURCE CLAIM (Rank 3): The summary describes scratch refactoring — "The goal is to get familiar with the code, not to actually clean it. The only rule is: revert your changes when you're done" ([The key points of Working Effectively with Legacy Code](https://understandlegacycode.com/blog/key-points-of-working-effectively-with-legacy-code/)).
- SOURCE CLAIM (Rank 3): The summary quotes the book's library-coupling warning — "Avoid littering direct calls to library classes in your code. You might think that you'll never change them, but that can become a self-fulfilling prophecy" ([The key points of Working Effectively with Legacy Code](https://understandlegacycode.com/blog/key-points-of-working-effectively-with-legacy-code/)).
- SOURCE CLAIM (Rank 2): Feathers states the hotspot strategy — "there tend to be hotspots and codebases, areas where you get lots and lots of change. So if you start just writing tests to support your work... over time you're going to start to cover the areas, which tend to have the highest amount of interaction" ([InfoQ podcast transcript](https://www.infoq.com/podcasts/working-effectively-legacy-code/)).
- AI INFERENCE: The legacy workflow is a bootstrapping loop: because tests are needed before safe change but code must change to enable tests, the practitioner makes minimal, seam-introducing edits first, pins current behavior with characterization tests, then refactors and adds features under that safety net. Sprout and wrap are low-risk ways to add tested code without first untangling the whole legacy unit.

## 9. Source editions and identifiers

- SOURCE CLAIM (Rank 2): Feathers' book is *Working Effectively with Legacy Code*, Prentice Hall, 2004; ISBN-10 0-13-117705-2 (Fowler's link) and ISBN-13 978-0-13-117705-5 (publisher page) ([Legacy Seam](https://martinfowler.com/bliki/LegacySeam.html); [InformIT](https://www.informit.com/articles/article.aspx?p=359417&seqNum=3)).
- SOURCE CLAIM (Rank 2): Beck's book is *Test-Driven Development: By Example*, Addison-Wesley, ISBN 0-321-14653-0 ([Test Driven Development](https://martinfowler.com/bliki/TestDrivenDevelopment.html)).
- SOURCE CLAIM (Rank 4): Wikipedia dates the book to 2003 — "Beck published Test Driven Development: By Example in 2003" ([Kent Beck](https://en.wikipedia.org/wiki/Kent_Beck)). Rank 4: orientation; the exact printing/edition was not independently verified.
- UNKNOWN: The precise printing and edition statements of both books were not inspected directly; only publisher/author metadata and excerpts were retrieved. Quotations from the books are therefore second-hand (publisher excerpt, interview, or quote aggregator), not read from a physical or licensed copy.

## Retrieval log

| URL | Result |
|-----|--------|
| https://martinfowler.com/articles/designDead.html | Retrieved (full article) |
| https://martinfowler.com/bliki/LegacySeam.html | Retrieved (full bliki page) |
| https://martinfowler.com/bliki/TestDrivenDevelopment.html | Retrieved (full bliki page) |
| https://www.informit.com/articles/article.aspx?p=359417&seqNum=3 | Retrieved (publisher book excerpt, "Seam Types") |
| https://understandlegacycode.com/blog/key-points-of-working-effectively-with-legacy-code/ | Retrieved (practitioner summary) |
| https://www.infoq.com/podcasts/working-effectively-legacy-code/ | Retrieved (podcast transcript) |
| https://newsletter.kentbeck.com/p/design-in-tdd | Retrieved (Kent Beck essay) |
| https://www.goodreads.com/work/quotes/376827-test-driven-development-by-example | Retrieved (quote aggregator; Rank 5) |
| https://www.obeythetestinggoat.com/new-book-excerpt-abstractions.html | Retrieved (practitioner book excerpt; Rank 3) |
| https://en.wikipedia.org/wiki/Characterization_test | Retrieved (Rank 4) |
| https://en.wikipedia.org/wiki/Kent_Beck | Retrieved via search snippet only; not fetched in full (Rank 4) |
| https://www.informit.com/articles/article.aspx?p=359417 (page 1) | Not fetched; only page 3 (seqNum=3) retrieved |
| Feathers, *Working Effectively with Legacy Code* (print) | Not inspected directly; no licensed copy |
| Beck, *Test-Driven Development: By Example* (print) | Not inspected directly; no licensed copy |

## Open questions

- The exact wording and page numbers of the seam and characterization-test definitions in the printed books were not verified against a licensed copy; only publisher excerpt, interview, and aggregator quotations were available.
- The claim that TDD *causes* good design is contested. Mark Seemann's "The TDD Apostate" asserts "TDD does not drive us towards good design" ([ploeh blog](https://blog.ploeh.dk/2010/12/22/TheTDDApostate/)); this counter-position was located but not captured in depth here and should be reconciled in synthesis.
- The boundary conditions of YAGNI (e.g., internationalization, database design) are explicitly left open by Fowler — "we still have very little data" ([Is Design Dead?](https://martinfowler.com/articles/designDead.html)).
- Whether emergent design is a property of test-first ordering or of the refactor step specifically is not settled by the sources; Beck's own essay places design reflection after green and at test-writing time.
- No controlled or empirical study measuring TDD's effect on coupling/cohesion was retrieved; the design-outcome claims here are practitioner assertions, not measured results.



