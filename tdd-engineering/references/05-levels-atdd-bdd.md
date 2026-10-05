# Topic 5 — Test levels, ATDD, and BDD

**Core question:** How do unit, integration, and acceptance tests relate? Cover the test pyramid, the ice-cream-cone anti-pattern, outside-in vs inside-out TDD, the double-loop (acceptance + unit) model, Acceptance Test-Driven Development (ATDD), and Behavior-Driven Development (BDD) from Dan North.

**Scope and method:** Language-agnostic only; no compiler/test-runner-specific mechanics, no Python/pytest. xUnit-family concepts are used as the generic frame (test case, fixture, assertion, test double). Evidence lines carry a rank label. Exact quotations are kept short and linked inline on the same line. Where a quotation comes from a reproduction rather than the publisher, that provenance is stated.

**Label key:** SOURCE FACT (Rank 1) = primary author/creator/canonical publisher material. SOURCE CLAIM (Rank 2–6) = reputable secondary, tertiary, practitioner, or reproduced material whose authority is lower. AI INFERENCE = the author's reasoning, not sourced. PLAUSIBLE NOT VERIFIED = asserted but not confirmed against a primary source here. UNKNOWN = not established.

---

## 1. Unit, integration, and acceptance tests as distinct scopes

- SOURCE FACT (Rank 1): A unit test targets a deliberately chosen small subject — "Your unit tests make sure that a certain unit (your subject under test) of your codebase works as intended." ([Fowler/Vocke, The Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)).
- SOURCE FACT (Rank 1): Unit scope is the narrowest — "Unit tests have the narrowest scope of all the tests in your test suite." ([Fowler/Vocke](https://martinfowler.com/articles/practical-test-pyramid.html)).
- SOURCE FACT (Rank 1): "What's a unit?" has no canonical answer — "If you ask three different people what 'unit' means in the context of unit tests, you'll probably receive four different, slightly nuanced answers." ([Fowler/Vocke](https://martinfowler.com/articles/practical-test-pyramid.html)).
- SOURCE FACT (Rank 1): Unit tests should test observable behaviour, not implementation — "Don't reflect your internal code structure within your unit tests. Test for observable behaviour instead." ([Fowler/Vocke](https://martinfowler.com/articles/practical-test-pyramid.html)).
- SOURCE FACT (Rank 1): Trivial code is not unit-tested — "you don't test trivial code" ([Fowler/Vocke](https://martinfowler.com/articles/practical-test-pyramid.html)).
- SOURCE FACT (Rank 1): Integration tests cover the boundary to outside parts — "Integration Tests are there to help. They test the integration of your application with all the parts that live outside of your application." ([Fowler/Vocke](https://martinfowler.com/articles/practical-test-pyramid.html)).
- SOURCE FACT (Rank 1): The article's author prefers narrow integration — "I like to treat integration testing more narrowly and test one integration point at a time by replacing separate services and databases with test doubles." ([Fowler/Vocke](https://martinfowler.com/articles/practical-test-pyramid.html)).
- SOURCE FACT (Rank 1): "integration tests" is vaguer than "unit test" — "I mentioned before that 'unit tests' is a vague term, this is even more true for 'integration tests'." ([Fowler/Vocke](https://martinfowler.com/articles/practical-test-pyramid.html)).
- SOURCE FACT (Rank 1): End-to-end tests exercise the fully integrated system and give the strongest signal — "End-to-end tests (also called Broad Stack Tests) give you the biggest confidence when you need to decide if your software is working or not." ([Fowler/Vocke](https://martinfowler.com/articles/practical-test-pyramid.html)).
- SOURCE FACT (Rank 1): End-to-end tests are costly in several dimensions — "End-to-End tests come with their own kind of problems. They are notoriously flaky and often fail for unexpected and unforeseeable reasons." ([Fowler/Vocke](https://martinfowler.com/articles/practical-test-pyramid.html)).
- SOURCE FACT (Rank 1): Acceptance is defined by user perspective, not by pyramid level — "The concept of acceptance tests - proving that your features work correctly for the user - is completely orthogonal to your test pyramid." ([Fowler/Vocke, Acceptance Tests section](https://martinfowler.com/articles/practical-test-pyramid.html)).
- SOURCE FACT (Rank 1): A lower-level acceptance test is preferred over a higher-level one when possible — "Having a low-level test is better than having a high-level test." ([Fowler/Vocke](https://martinfowler.com/articles/practical-test-pyramid.html)).
- SOURCE FACT (Rank 1): The author expects acceptance tests at any granularity — "there's technically no need to write acceptance tests at the highest level of your test pyramid. If your application design and your scenario at hand permits that you write an acceptance test at a lower level, go for it." ([Fowler/Vocke](https://martinfowler.com/articles/practical-test-pyramid.html)).
- SOURCE FACT (Rank 1): High-level failure implies a missing lower-level test — "If you get a failure in a high level test, not just do you have a bug in your functional code, you also have a missing or incorrect unit test." ([Fowler, Test Pyramid bliki](https://martinfowler.com/bliki/TestPyramid.html)).
- AI INFERENCE: The three labels are therefore not a strict hierarchy of kinds but partly a spectrum of scope and integration; the acceptance property is a purpose (whose perspective) and can coincide with any level.

### Terminology is not standardized

- SOURCE FACT (Rank 1): Names are contested and unstable — "There's no right or wrong. The software development community simply hasn't managed to settle on well-defined terms around testing." ([Fowler/Vocke, The Confusion About Testing Terminology](https://martinfowler.com/articles/practical-test-pyramid.html)).
- SOURCE FACT (Rank 1): The reality is continuous, not categorical — "it's really more of a spectrum than a bunch of discrete buckets anyways" ([Fowler/Vocke](https://martinfowler.com/articles/practical-test-pyramid.html)).
- SOURCE FACT (Rank 1): Teams should choose their own terms and be consistent — "The important takeaway is that you should find terms that work for you and your team." ([Fowler/Vocke](https://martinfowler.com/articles/practical-test-pyramid.html)).
- SOURCE FACT (Rank 1): Even within one article the boundaries are judgment calls — coarse tests are not automatically wrong technique, only wrong granularity here — "it's also true that using overly coarse grained tests isn't necessarily a failure of classical testing as a technique, rather a failure to do classic testing properly." ([Fowler, Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html)).

---

## 2. The test pyramid

- SOURCE FACT (Rank 1): Definition — "The test pyramid is a way of thinking about how different kinds of automated tests should be used to create a balanced portfolio." ([Fowler, Test Pyramid bliki](https://martinfowler.com/bliki/TestPyramid.html)).
- SOURCE FACT (Rank 1): Shape rule — "you should have many more low-level UnitTests than high level BroadStackTests running through a GUI" ([Fowler, Test Pyramid bliki](https://martinfowler.com/bliki/TestPyramid.html)).
- SOURCE FACT (Rank 1): Origin attribution — "Mike Cohn came up with this concept in his book Succeeding with Agile." ([Fowler/Vocke, The Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)).
- SOURCE FACT (Rank 1): Further origin detail — "He originally drew it in conversation with Lisa Crispin in 2003-4 and described it at a scrum gathering in 2004." ([Fowler, Test Pyramid bliki](https://martinfowler.com/bliki/TestPyramid.html)).
- SOURCE FACT (Rank 1): Cohn's book phrasing is "Test Automation Pyramid" — "In the book he refers to it as the 'Test Automation Pyramid', but in use it's generally referred to as just the 'test pyramid'." ([Fowler, Test Pyramid bliki](https://martinfowler.com/bliki/TestPyramid.html)).
- SOURCE FACT (Rank 1): The two durable takeaways from the original — "1. Write tests with different granularity / 2. The more high-level you get the fewer tests you should have" ([Fowler/Vocke](https://martinfowler.com/articles/practical-test-pyramid.html)).
- SOURCE FACT (Rank 1): Practical shape guidance — "Write lots of small and fast unit tests. Write some more coarse-grained tests and very few high-level tests that test your application from end to end." ([Fowler/Vocke](https://martinfowler.com/articles/practical-test-pyramid.html)).
- SOURCE CLAIM (Rank 2): The original pyramid has three named layers — "An effective test automation strategy calls for automating tests at three different levels" ([Cohn, The Forgotten Layer of the Test Automation Pyramid](https://www.mountaingoatsoftware.com/blog/the-forgotten-layer-of-the-test-automation-pyramid)).
- SOURCE FACT (Rank 1): Bottom layer is unit — "At the base of the test automation pyramid is unit testing." ([Cohn](https://www.mountaingoatsoftware.com/blog/the-forgotten-layer-of-the-test-automation-pyramid)).
- SOURCE FACT (Rank 1): Middle layer is service-level, often forgotten — "Without service-level testing to fill the gap between unit and user interface testing, all other testing ends up being performed through the user interface" ([Cohn](https://www.mountaingoatsoftware.com/blog/the-forgotten-layer-of-the-test-automation-pyramid)).
- SOURCE FACT (Rank 1): Original Cohn layers are — "1. Unit Tests / 2. Service Tests / 3. User Interface Tests" ([Fowler/Vocke](https://martinfowler.com/articles/practical-test-pyramid.html)).
- SOURCE FACT (Rank 1): The author extends the pyramid with contract tests and integration tests between unit and E2E — "For each interface there are two parties involved: the provider and the consumer." ([Fowler/Vocke, Contract Tests](https://martinfowler.com/articles/practical-test-pyramid.html)).
- SOURCE FACT (Rank 1): The pyramid is explicitly critiqued as simplistic — "the concept of the test pyramid falls a little short if you take a closer look." ([Fowler/Vocke](https://martinfowler.com/articles/practical-test-pyramid.html)).
- SOURCE FACT (Rank 1): Because of that, layer names may be re-chosen — "it's totally okay to come up with other names for your test layers, as long as you keep it consistent within your codebase and your team's discussions." ([Fowler/Vocke](https://martinfowler.com/articles/practical-test-pyramid.html)).
- SOURCE FACT (Rank 1): Counter-argument recorded by Fowler — "Some writers argue that the pyramid isn't a good test distribution, preferring more integration tests and few unit tests." ([Fowler, Test Pyramid bliki](https://martinfowler.com/bliki/TestPyramid.html)).
- SOURCE FACT (Rank 1): Fowler's intermediate layer is subcutaneous tests — "The pyramid also argues for an intermediate layer of tests that act through a service layer of an application, what I refer to as SubcutaneousTests." ([Fowler, Test Pyramid bliki](https://martinfowler.com/bliki/TestPyramid.html)).

---

## 3. The ice-cream-cone anti-pattern

- SOURCE FACT (Rank 1): The anti-pattern is an inverted pyramid, typically with too many UI-driven tests — "Watch out that you don't end up with a test ice-cream cone that will be a nightmare to maintain and takes way too long to run." ([Fowler/Vocke](https://martinfowler.com/articles/practical-test-pyramid.html)).
- SOURCE FACT (Rank 1): Fowler describes the drift into it — "But this kind of approach quickly runs into trouble, becoming an ice-cream cone." ([Fowler, Test Pyramid bliki](https://martinfowler.com/bliki/TestPyramid.html)).
- SOURCE FACT (Rank 1): Why UI-heavy suites degrade — "In short, tests that run end-to-end through the UI are: brittle, expensive to write, and time consuming to run." ([Fowler, Test Pyramid bliki](https://martinfowler.com/bliki/TestPyramid.html)).
- SOURCE CLAIM (Rank 3): The metaphor is attributed to Alister Scott's testing-pyramids material — "the best pyramid to invert is the cloud one since it becomes the the software testing ice-cream cone (anti-pattern)" ([Alister Scott, Testing Pyramids & Ice-Cream Cones](https://alisterscott.github.io/TestingPyramids.html)) [note the source's own duplicated "the the"].
- SOURCE CLAIM (Rank 3): The same page frames the cone as an inversion failure — "I often see organizations fall into the trap of creating 'inverted' pyramids of software testing" ([Alister Scott](https://alisterscott.github.io/TestingPyramids.html)).
- SOURCE FACT (Rank 1): The pyramid's own caveat — the assumption that broad tests are costly is not universal — "If my high level tests are fast, reliable, and cheap to modify - then lower-level tests aren't needed." ([Fowler, Test Pyramid bliki](https://martinfowler.com/bliki/TestPyramid.html)).
- AI INFERENCE: The ice-cream cone is best read as a consequence of optimizing for test realism without weighting feedback speed, brittleness, and maintenance cost, rather than as a claim that end-to-end testing is inherently wrong.

---

## 4. Outside-in vs inside-out TDD

- SOURCE CLAIM (Rank 3): Traditional TDD is framed as unit-first and middle-out — "Traditional test-driven development is a process that is specifically about unit tests... It's sometimes referred to as 'middle-out TDD', because you start in the middle of your application building domain logic." ([Outside-In Frontend Development, Overview of Outside-In TDD](https://outsidein.dev/concepts/outside-in-tdd)).
- SOURCE CLAIM (Rank 3): Outside-in starts at the user-facing surface — "This style of TDD is called 'outside-in' because you start from the outside of your application: the user interface, as tested by the E2E test." ([Outside-In Frontend Development](https://outsidein.dev/concepts/outside-in-tdd)).
- SOURCE FACT (Rank 1): Mockist/need-driven development is the same idea in the OO/mock community — "In particular they advocate a style called need-driven development." ([Fowler, Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html)).
- SOURCE FACT (Rank 1): The synonym — "This style is also referred to as outside-in, which is a very descriptive name for it." ([Fowler, Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html)).
- SOURCE FACT (Rank 1): The classic-domain-first alternative — "A common style is middle-out." ([Fowler, Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html)).
- SOURCE FACT (Rank 1): Geographic naming of the two camps — "You sometimes see 'Detroit' style used for 'classical' and 'London' for 'mockist'." ([Fowler, Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html)).
- SOURCE CLAIM (Rank 4): London style is commonly characterized as outside-in, Chicago as inside-out — "London style, a.k.a. 'mockist' / Mostly outside-in: from acceptance tests to unit tests"; "Chicago style, a.k.a. 'classic' / Mostly inside-out: from unit tests to acceptance tests" ([O'Reilly OSCON slide, citing Freeman & Pryce](https://conferences.oreilly.com/oscon/oscon-or-2018/cdn.oreillystatic.com/en/assets/1/event/274/A%20gentle%20introduction%20to%20TDD%20in%20Go%20Presentation.pdf)).
- SOURCE FACT (Rank 1): Outside-in uses mocks to discover collaborators — "By thinking through the expectations upon the collaborators, you explore the interaction between the SUT and its neighbors - effectively designing the outbound interface of the SUT." ([Fowler, Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html)).
- SOURCE CLAIM (Rank 3): Outside-in's stated design rationale — "in outside-in TDD, each end-to-end test focuses on one user-facing feature" and "you write the code that calls into the module before you write the module itself" ([Outside-In Frontend Development](https://outsidein.dev/concepts/outside-in-tdd)).
- SOURCE CLAIM (Rank 3): Complementary test roles — "Whereas end-to-end tests confirm the external quality of your app, unit tests expose its 'internal quality' by showing how your units are used." ([Outside-In Frontend Development](https://outsidein.dev/concepts/outside-in-tdd)).
- SOURCE FACT (Rank 1): Mockist tests couple more tightly to implementation than classical state-based tests — "Mockist tests are thus more coupled to the implementation of a method. Changing the nature of calls to collaborators usually cause a mockist test to break." ([Fowler, Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html)).
- SOURCE FACT (Rank 1): Fowler's own preference — "Personally I've always been a old fashioned classic TDDer and thus far I don't see any reason to change." ([Fowler, Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html)).
- SOURCE FACT (Rank 1): Whichever style is chosen, acceptance tests are still required — "you must combine it with coarser grained acceptance tests that operate across the system as a whole." ([Fowler, Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html)).

---

## 5. The double-loop (acceptance + unit) model

- SOURCE CLAIM (Rank 3): The two-level loop stated plainly — "The first thing outside-in TDD adds is a second TDD loop outside the first one:" ([Outside-In Frontend Development, Overview of Outside-In TDD](https://outsidein.dev/concepts/outside-in-tdd)).
- SOURCE CLAIM (Rank 3): The loop's three steps — "1. Write an E2E test and watch it fail. 2. Step down to a unit test and use the Red-Green-Refactor loop to implement just enough functionality to get past the current E2E test failure. 3. Step back up and rerun the E2E test to see if it passes." ([Outside-In Frontend Development](https://outsidein.dev/concepts/outside-in-tdd)).
- SOURCE CLAIM (Rank 4): A video transcript states the same sequencing — "this is the double loop of TDD: so first we start with an acceptance test, once the acceptance test is failing for the right reason then you go into the inner loop of TDD, that is the unit test." ([Sandro Mancuso, Outside-In TDD transcript gist](https://gist.github.com/xpepper/66ced102032ad479b8170d9205754519)).
- SOURCE CLAIM (Rank 3): Timescale sometimes given for the two loops — "you go around the inner loop on the timescale of minutes, and the outer loop on the timescale of hours to days." ([Coding Is Like Cooking, Outside-In development with Double Loop TDD](https://coding-is-like-cooking.info/2013/04/outside-in-development-with-double-loop-tdd)).
- SOURCE CLAIM (Rank 4): The book commonly credited with the nested-cycle framing — "In our work, we apply feedback cycles at every level of development, organizing projects as a system of nested loops ranging from seconds to months" (Freeman & Pryce, *Growing Object-Oriented Software, Guided by Tests*, as reproduced at [dokumen.pub, 6th printing](https://dokumen.pub/growing-object-oriented-software-guided-by-tests-6th-printingnbsped-9780321503626-0321503627.html)) [unofficial reproduction; see Retrieval log].
- SOURCE CLAIM (Rank 4): The book's unit-under-acceptance ordering — "Underneath the acceptance test, we follow the unit level test/implement/refactor cycle to develop the feature" (Freeman & Pryce, as reproduced at [dokumen.pub](https://dokumen.pub/growing-object-oriented-software-guided-by-tests-6th-printingnbsped-9780321503626-0321503627.html)) [unofficial reproduction].
- SOURCE CLAIM (Rank 4): The orientation of the outer loop — "The outer test loop is a measure of demonstrable progress, and the growing suite of tests protects us against regression failures when we change the system." (Freeman & Pryce, as reproduced at [dokumen.pub](https://dokumen.pub/growing-object-oriented-software-guided-by-tests-6th-printingnbsped-9780321503626-0321503627.html)) [unofficial reproduction].
- SOURCE FACT (Rank 1): The canonical structure of the book's process chapter — Chapter 5 is titled "Maintaining the Test-Driven Cycle" with sections "Start Each Feature with an Acceptance Test" and "Separate Tests That Measure Progress from Those That Catch Regressions" ([official GOOS Table of Contents](https://growing-object-oriented-software.com/toc.html)).
- SOURCE FACT (Rank 1): Chapter 1 explicitly includes end-to-end and levels-of-testing concerns — "Testing End-to-End" and "Levels of Testing" ([official GOOS Table of Contents](https://growing-object-oriented-software.com/toc.html)).
- SOURCE CLAIM (Rank 3): Review characterizes the book as "end-to-end TDD" using mocks — "It's a style characterized by heavy use of mock objects and end-to-end TDD." ([Adam Tornhill, review of GOOS](https://www.adamtornhill.com/reviews/goos.htm)).
- PLAUSIBLE NOT VERIFIED: The specific phrase "double loop" may not appear verbatim in GOOS; the book's own wording appears to be "nested loops" and "inner and outer feedback loops", with "double loop" popularized by later secondary sources. This file did not obtain a licensed full text of GOOS to confirm whether "double loop" is used verbatim (see Open questions).
- AI INFERENCE: The double loop makes each inner unit cycle justified by a currently failing outer test, so it prevents building unused units — the exact failure mode GOOS's snippet describes as high-quality code "that turned out not to be called from anywhere".

**Bibliographic record (book):** Steve Freeman and Nat Pryce, *Growing Object-Oriented Software, Guided by Tests*, Addison-Wesley Professional, 2009/2010, ISBN 978-0-321-50362-6 ([ACM listing](https://dl.acm.org/doi/10.5555/1655852); [Pearson listing](https://www.pearson.com/en-ca/subject-catalog/p/growing-object-oriented-software-guided-by-tests/P200000009298/9780321503626); [official site](https://growing-object-oriented-software.com/)).

---

## 6. Acceptance Test-Driven Development (ATDD)

- SOURCE CLAIM (Rank 3): Definition — "ATDD is a development methodology based on communication between the business customers, the developers, and the testers." ([Wikipedia, Acceptance test-driven development](https://en.wikipedia.org/wiki/Acceptance_test-driven_development)).
- SOURCE CLAIM (Rank 3): It is closely related to TDD but differs in collaboration emphasis — "It differs by the emphasis on developer-tester-business customer collaboration." ([Wikipedia, ATDD](https://en.wikipedia.org/wiki/Acceptance_test-driven_development)).
- SOURCE CLAIM (Rank 3): The defining temporal move — "highlights writing acceptance tests before starting any coding." ([Wikipedia, ATDD](https://en.wikipedia.org/wiki/Acceptance_test-driven_development)).
- SOURCE CLAIM (Rank 2): Purpose relative to TDD — "Acceptance test-driven development (acceptance TDD) is what helps developers build high-quality software that fulfills the business's needs as reliably as TDD helps ensure the software's technical quality." ([Koskela, Test Driven: Practical TDD and Acceptance TDD for Java Developers, Ch. 9](https://livebook.manning.com/book/test-driven/chapter-9/ch09)).
- SOURCE CLAIM (Rank 3): Acceptance tests are external-view — "Acceptance tests are from the user's point of view – the external view of the system." ([Wikipedia, ATDD](https://en.wikipedia.org/wiki/Acceptance_test-driven_development)).
- SOURCE CLAIM (Rank 3): They are implementation-independent in intent — "In general, they are implementation independent, although automation of them may not be." ([Wikipedia, ATDD](https://en.wikipedia.org/wiki/Acceptance_test-driven_development)).
- SOURCE CLAIM (Rank 3): They are authored during analysis, before coding, collaboratively — "Acceptance tests are created when the requirements are analyzed and prior to coding." ([Wikipedia, ATDD](https://en.wikipedia.org/wiki/Acceptance_test-driven_development)).
- SOURCE CLAIM (Rank 3): Business-domain wording yields a shared vocabulary — "The tests are specified in business domain terms. The terms then form a ubiquitous language that is shared between the customers, developers, and testers." ([Wikipedia, ATDD](https://en.wikipedia.org/wiki/Acceptance_test-driven_development)).
- SOURCE CLAIM (Rank 3): ATDD shares practices with adjacent movements — "ATDD encompasses many of the same practices as specification by example (SBE), behavior-driven development (BDD), example-driven development (EDD)" ([Wikipedia, ATDD](https://en.wikipedia.org/wiki/Acceptance_test-driven_development)).
- SOURCE CLAIM (Rank 3): ATDD does not strictly require automation — "TDD requires test automation. ATDD does not, although automation helps with regression testing." ([Wikipedia, Test-driven development, TDD and ATDD](https://en.wikipedia.org/wiki/Test-driven_development)).
- SOURCE CLAIM (Rank 3): TDD and ATDD have different audiences and purposes — "ATDD is a communication tool between the customer, developer, and tester to ensure that the requirements are well-defined." ([Wikipedia, TDD and ATDD](https://en.wikipedia.org/wiki/Test-driven_development)).
- SOURCE CLAIM (Rank 3): TDD tests need not be customer-readable, ATDD tests should be — "ATDD tests should be readable by the customer. TDD tests do not need to be." ([Wikipedia, TDD and ATDD](https://en.wikipedia.org/wiki/Test-driven_development)).
- SOURCE CLAIM (Rank 3): The coupling direction from acceptance to unit — "Tests used in TDD can often be derived from ATDD tests, since the code units implement some part of a requirement." ([Wikipedia, TDD and ATDD](https://en.wikipedia.org/wiki/Test-driven_development)).
- SOURCE CLAIM (Rank 3): The standard ATDD scenario form is Given/When/Then — "Given (setup) / When (trigger) / Then (verification)" ([Wikipedia, ATDD](https://en.wikipedia.org/wiki/Acceptance_test-driven_development)).
- SOURCE CLAIM (Rank 2): Primary book for ATDD — Ken Pugh, *Lean-Agile Acceptance Test-Driven Development: Better Software Through Collaboration*, Addison-Wesley, 2011, ISBN 978-0321714084 ([Wikipedia, ATDD references](https://en.wikipedia.org/wiki/Acceptance_test-driven_development)).
- AI INFERENCE: ATDD can be understood as specifying acceptance criteria as tests before coding, with the collaboration of business, development, and test roles; its automated outputs can then seed the unit-level TDD cycle.

---

## 7. Behavior-Driven Development (BDD) from Dan North

- SOURCE FACT (Rank 1): BDD's origin as a response to TDD confusion — "My response is behaviour-driven development (BDD). It has evolved out of established agile practices and is designed to make them more accessible and effective for teams new to agile software delivery." ([Dan North, Introducing BDD, 20 Sep 2006](https://dannorth.net/blog/introducing-bdd/)).
- SOURCE FACT (Rank 1): The word "test" was the diagnosed problem — "people's misunderstandings about TDD almost always came back to the word 'test'." ([Dan North, Introducing BDD](https://dannorth.net/blog/introducing-bdd/)).
- SOURCE FACT (Rank 1): Renaming as behaviour was the pivotal move — "I found the shift from thinking in tests to thinking in behaviour so profound" ([Dan North, Introducing BDD](https://dannorth.net/blog/introducing-bdd/)).
- SOURCE FACT (Rank 1): Why names matter — "if the methods do not comprehensively describe the behaviour of your system, then they are lulling you into a false sense of security." ([Dan North, Introducing BDD](https://dannorth.net/blog/introducing-bdd/)).
- SOURCE FACT (Rank 1): Tests named as sentences — "What to call your test is easy: it's a sentence describing the next behaviour in which you are interested." ([Dan North, Introducing BDD](https://dannorth.net/blog/introducing-bdd/)).
- SOURCE FACT (Rank 1): The "should" template — "This sentence template—The class should do something—means you can only define a test for the current class." ([Dan North, Introducing BDD](https://dannorth.net/blog/introducing-bdd/)).
- SOURCE FACT (Rank 1): Stories as the unit of functionality — "Behaviour-driven development uses a story as the basic unit of functionality, and therefore of delivery." ([Dan North, What's in a Story?](https://dannorth.net/blog/whats-in-a-story)).
- SOURCE FACT (Rank 1): Acceptance criteria are intrinsic to the story — "The acceptance criteria are an intrinsic part of the story; in effect they define the scope of its behaviour, and give us a shared definition of 'done'." ([Dan North, What's in a Story?](https://dannorth.net/blog/whats-in-a-story)).
- SOURCE FACT (Rank 1): BDD is explicitly outside-in — "Behaviour-driven development is an 'outside-in' methodology." ([Dan North, What's in a Story?](https://dannorth.net/blog/whats-in-a-story)).
- SOURCE FACT (Rank 1): What outside-in means here — "It starts at the outside by identifying business outcomes, and then drills down into the feature set that will achieve those outcomes." ([Dan North, What's in a Story?](https://dannorth.net/blog/whats-in-a-story)).
- SOURCE FACT (Rank 1): The Given/When/Then template — "Given some initial context (the givens), When an event occurs, Then ensure some outcomes." ([Dan North, Introducing BDD](https://dannorth.net/blog/introducing-bdd/)).
- SOURCE FACT (Rank 1): Acceptance criteria as scenarios using that template, with the ATM withdrawal example — "Given the account is in credit / And the card is valid / And the dispenser contains cash / When the customer requests cash / Then ensure the account is debited" ([Dan North, Introducing BDD](https://dannorth.net/blog/introducing-bdd/)).
- SOURCE FACT (Rank 1): Scenario fragments can map to executable code — "The fragments of the scenario—the givens, event, and outcomes—are fine-grained enough to be represented directly in code." ([Dan North, Introducing BDD](https://dannorth.net/blog/introducing-bdd/)).
- SOURCE FACT (Rank 1): Scenarios evolve toward end-to-end tests — "by the time the scenario is completed, they have become proper end-to-end functional tests." ([Dan North, Introducing BDD](https://dannorth.net/blog/introducing-bdd/)).
- SOURCE FACT (Rank 1): Story narrative template — "As a [role] / I want [feature] / So that [benefit]" ([Dan North, What's in a Story?](https://dannorth.net/blog/whats-in-a-story)).
- SOURCE FACT (Rank 1): Full story-plus-scenarios template — "Title (one line describing the story) / Narrative: ... / Acceptance Criteria: (presented as Scenarios)" ([Dan North, What's in a Story?](https://dannorth.net/blog/whats-in-a-story)).
- SOURCE FACT (Rank 1): BDD vs TDD scope — "BDD is the same thing but for a broader audience: testers, analysts, project and program managers, multiple SMEs covering multiple interrelated domains." ([Dan North, BDD is like TDD if, 31 May 2012](https://dannorth.net/blog/bdd-is-like-tdd-if)).
- SOURCE FACT (Rank 1): When the audience is all programmers, North agrees they collapse — "Is BDD the same as TDD? Yes. If you're a programmer, and your entire team is programmers, and all your stakeholders are programmers" ([Dan North, BDD is like TDD if](https://dannorth.net/blog/bdd-is-like-tdd-if)).
- SOURCE CLAIM (Rank 2): North's compact 2009 definition — "BDD is a 2nd generation, outside-in, pull-based, multiple-stakeholder, multiple-scale, high-automation, Agile methodology." ([Dan North, quoted in the Behavior-Driven Development group](https://groups.google.com/g/behaviordrivendevelopment/c/OQnb3APpUJk/m/RklRiyEKde4J)) [posted by North; forum medium].
- SOURCE FACT (Rank 1): Fowler on BDD's lineage — "An important offshoot of the mockist style is that of Behavior Driven Development (BDD)." ([Fowler, Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html)).
- SOURCE FACT (Rank 1): Fowler on BDD's purpose — "BDD was originally developed by my colleague Daniel Terhorst-North as a technique to better help people learn Test Driven Development by focusing on how TDD operates as a design technique." ([Fowler, Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html)).
- SOURCE FACT (Rank 1): BDD tends to the mockist/outside-in camp — "BDD takes a mockist approach, but it expands on this, both with its naming styles, and with its desire to integrate analysis within its technique." ([Fowler, Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html)).
- SOURCE CLAIM (Rank 3): BDD is a synthesis of TDD and ATDD — "BDD (behavior-driven development) combines practices from TDD and from ATDD." ([Wikipedia, TDD and BDD](https://en.wikipedia.org/wiki/Test-driven_development)).
- SOURCE CLAIM (Rank 3): The behavioural emphasis over unit implementation — "it includes the practice of writing tests first, but focuses on tests which describe behavior, rather than tests which test a unit of implementation." ([Wikipedia, TDD and BDD](https://en.wikipedia.org/wiki/Test-driven_development)).
- SOURCE CLAIM (Rank 3): BDD tooling is deliberately shared across roles — "Tools such as JBehave, Cucumber, Mspec and Specflow provide syntaxes which allow product owners, developers and test engineers to define together the behaviors which can then be translated into automated tests." ([Wikipedia, TDD and BDD](https://en.wikipedia.org/wiki/Test-driven_development)).

---

## 8. How the topics interlock

- SOURCE FACT (Rank 1): TDD-defined scope — "TDD is primarily a developer's tool to help create well-written unit of code (function, class, or module) that correctly performs a set of operations." ([Wikipedia, TDD and ATDD](https://en.wikipedia.org/wiki/Test-driven_development)).
- SOURCE CLAIM (Rank 3): ATDD = communication + acceptance-before-code; TDD = developer unit tool — "ATDD is a communication tool between the customer, developer, and tester to ensure that the requirements are well-defined." ([Wikipedia, TDD and ATDD](https://en.wikipedia.org/wiki/Test-driven_development)).
- SOURCE CLAIM (Rank 3): BDD sits at their intersection — "combines practices from TDD and from ATDD" ([Wikipedia, TDD and BDD](https://en.wikipedia.org/wiki/Test-driven_development)).
- SOURCE FACT (Rank 1): BDD's given-when-then is the same expression ATDD uses for acceptance tests — "Given some initial context (the givens), When an event occurs, Then ensure some outcomes." ([Dan North, Introducing BDD](https://dannorth.net/blog/introducing-bdd/)) and "Given (setup) / When (trigger) / Then (verification)" ([Wikipedia, ATDD](https://en.wikipedia.org/wiki/Acceptance_test-driven_development)).
- SOURCE FACT (Rank 1): Acceptance tests and unit tests are complementary, not substitutes — "you must combine it with coarser grained acceptance tests that operate across the system as a whole." ([Fowler, Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html)).
- SOURCE CLAIM (Rank 3): Each layer covers the other's blind spot — "each type of test covers the limitations of the other." ([Outside-In Frontend Development](https://outsidein.dev/concepts/outside-in-tdd)).
- SOURCE FACT (Rank 1): BDD and ATDD do not replace the pyramid; acceptance can live at any level — "The concept of acceptance tests ... is completely orthogonal to your test pyramid." ([Fowler/Vocke](https://martinfowler.com/articles/practical-test-pyramid.html)).
- AI INFERENCE: A defensible synthesis is that the pyramid organizes tests by scope/cost from the bottom up, while the double loop organizes the same tests temporally from the top down; ATDD and BDD are primarily ways of producing the outer-loop acceptance criteria, and BDD adds a ubiquitous, behaviour-oriented language shared across roles.

---

## Retrieval log

| URL | Result |
| --- | --- |
| https://martinfowler.com/articles/practical-test-pyramid.html | Fetched; full article (truncated in tool view, full text saved locally and read for acceptance/terminology sections) |
| https://martinfowler.com/bliki/TestPyramid.html | Fetched; full bliki entry incl. etymology, ice-cream cone, caveats |
| https://martinfowler.com/articles/mocksArentStubs.html | Fetched; full article incl. classical vs mockist, outside-in, BDD lineage |
| https://www.mountaingoatsoftware.com/blog/the-forgotten-layer-of-the-test-automation-pyramid | Fetched; Cohn's three-level pyramid and service layer |
| https://alisterscott.github.io/TestingPyramids.html | Fetched; ice-cream-cone anti-pattern source |
| https://dannorth.net/introducing-bdd/ | First direct fetch returned empty; alternate path below succeeded |
| https://dannorth.net/blog/introducing-bdd/ | Fetched; full article (origin of BDD, Given/When/Then, JBehave) |
| https://dannorth.net/blog/whats-in-a-story | Fetched; full article (story template, outside-in, scenario structure) |
| https://dannorth.net/blog/bdd-is-like-tdd-if | Fetched; full article (BDD vs TDD audience) |
| https://outsidein.dev/concepts/outside-in-tdd | Fetched; full chapter on the two-level loop |
| https://en.wikipedia.org/wiki/Test-driven_development | Fetched; TDD/ATDD/BDD comparison and xUnit framing |
| https://en.wikipedia.org/wiki/Acceptance_test-driven_development | Fetched; ATDD definition, Given/When/Then, references |
| https://growing-object-oriented-software.com/toc.html | Fetched; official GOOS table of contents (chapter/section titles) |
| https://growing-object-oriented-software.com/ | Fetched via search result; official book description and coverage list |
| https://dl.acm.org/doi/10.5555/1655852 | Retrieved via search snippet; publisher/ISBN bibliographic record |
| https://www.pearson.com/en-ca/subject-catalog/p/growing-object-oriented-software-guided-by-tests/P200000009298/9780321503626 | Retrieved via search snippet; publisher ISBN/date |
| https://dokumen.pub/growing-object-oriented-software-guided-by-tests-6th-printingnbsped-9780321503626-0321503627.html | Retrieved via search snippet only; UNOFFICIAL reproduction of GOOS used for two short excerpts, flagged Rank 4 |
| https://gist.github.com/xpepper/66ced102032ad479b8170d9205754519 | Retrieved via search snippet; video transcript for the double loop, Rank 4 |
| https://coding-is-like-cooking.info/2013/04/outside-in-development-with-double-loop-tdd | Retrieved via search snippet only; timescale claim, Rank 3 |
| https://livebook.manning.com/book/test-driven/chapter-9/ch09 | Retrieved via search snippet; Koskela ATDD chapter text (page itself reported "Unable to load book!") |
| https://groups.google.com/g/behaviordrivendevelopment/c/OQnb3APpUJk/m/RklRiyEKde4J | Retrieved via search snippet; North's 2009 BDD definition, Rank 2 forum |
| https://conferences.oreilly.com/oscon/oscon-or-2018/cdn.oreillystatic.com/en/assets/1/event/274/A%20gentle%20introduction%20to%20TDD%20in%20Go%20Presentation.pdf | Retrieved via search snippet; London/Chicago mapping, Rank 4 slide deck |
| https://www.adamtornhill.com/reviews/goos.htm | Retrieved via search snippet; review characterization of GOOS, Rank 3 |

## Limitations

- The canonical `https://dannorth.net/introducing-bdd/` returned an empty body on the first attempt; the dated archive path `https://dannorth.net/blog/introducing-bdd/` was used and yielded the full article. This is a retrieval-path difference, not a content difference.
- The full text of *Growing Object-Oriented Software, Guided by Tests* is copyrighted and was not obtained from the publisher online. Only the official table of contents/description were fetched directly; three short excerpts of the book's prose were captured from an unofficial reproduction and are labeled Rank 4. Two of the book's own phrases ("nested loops", "inner and outer feedback loops") are also visible in search snippets of the same reproduction.
- Several items (Cohn's book ISBN, Koskela chapter, transcripts, London/Chicago mapping, Mancuso transcript) are captured from search-engine snippets because the destination pages were not fully parsed; quotations were matched to visible snippet text.
- No verbatim occurrence of the term "double loop" in GOOS was confirmed.

## Open questions

- Does *Growing Object-Oriented Software, Guided by Tests* use the exact phrase "double loop", or only "nested loops"/"inner and outer feedback loops"? A licensed copy is needed to settle attribution of the term.
- Is the double-loop model best attributed to GOOS, to earlier mockist literature, or to later synthesis (e.g., outside-in teaching material)? The primary-vs-secondary boundary is unresolved here.
- What is the earliest authoritative source for the ice-cream-cone anti-pattern term — Alister Scott's post, or an earlier venue? The retrieved page is undated.
- How exactly should the "service test" middle layer (Cohn) be reconciled with "narrow integration test" (Vocke) and "subcutaneous test" (Fowler)? The three overlap without an agreed boundary.
- Is ATDD's Given/When/Then form historically prior to BDD's, or did North's BDD template shape the ATDD convention? The retrieved ATDD page does not establish priority.
- Does any canonical source give an accepted threshold or ratio for pyramid layers, or is the shape only qualitative? None of the retrieved primary sources give numeric guidance.