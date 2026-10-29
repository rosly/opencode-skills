# Topic 4 — Test doubles and isolation

Scope: language-agnostic, xUnit-family concepts only. No language- or framework-specific APIs. Every externally sourced fact carries the shortest exact quotation and a descriptive inline link to the source URL on the same line. Labels: SOURCE FACT (Rank 1), SOURCE CLAIM (Rank 2–6), AI INFERENCE, PLAUSIBLE NOT VERIFIED, UNKNOWN.

## 1. The generic concept: Test Double

SOURCE FACT (Rank 1): "Test Double is a generic term for any case where you replace a production object for testing purposes." — [Fowler, "Test Double"](https://martinfowler.com/bliki/TestDouble.html)

SOURCE FACT (Rank 1): "We replace a component on which the SUT depends with a "test-specific equivalent."" — [Meszaros, "Test Double"](http://xunitpatterns.com/Test%20Double.html)

SOURCE FACT (Rank 1): "The Test Double doesn't have to behave exactly like the real DOC; it merely has to provide the same API as the real one so that the SUT thinks it is the real one!" — [Meszaros, "Test Double"](http://xunitpatterns.com/Test%20Double.html)

SOURCE FACT (Rank 1): "The generic term he uses is a Test Double (think stunt double)." — [Fowler, "Test Double"](https://martinfowler.com/bliki/TestDouble.html)

SOURCE FACT (Rank 1): "The name comes from the notion of a Stunt Double in movies." — [Fowler, "Mocks Aren't Stubs"](https://martinfowler.com/articles/mocksArentStubs.html)

SOURCE FACT (Rank 1): "The terminology around the various kinds of Test Doubles ... is confusing and inconsistent. Different authors use different terms to mean the same thing. And sometimes they mean different things by the same term!" — [Meszaros, "Mocks, Fakes, Stubs and Dummies"](http://xunitpatterns.com/Mocks,%20Fakes,%20Stubs%20and%20Dummies.html)

AI INFERENCE: The taxonomy is a vocabulary for a role a test object plays in a given test, not a fixed class hierarchy; the same object can play different roles in different tests.

## 2. Meszaros' five double types

SOURCE FACT (Rank 1): "Dummy objects are passed around but never actually used. Usually they are just used to fill parameter lists." — [Fowler, "Test Double"](https://martinfowler.com/bliki/TestDouble.html)

SOURCE FACT (Rank 1): "Fake objects actually have working implementations, but usually take some shortcut which makes them not suitable for production (an InMemoryTestDatabase is a good example)." — [Fowler, "Test Double"](https://martinfowler.com/bliki/TestDouble.html)

SOURCE FACT (Rank 1): "Stubs provide canned answers to calls made during the test, usually not responding at all to anything outside what's programmed in for the test." — [Fowler, "Test Double"](https://martinfowler.com/bliki/TestDouble.html)

SOURCE FACT (Rank 1): "Spies are stubs that also record some information based on how they were called. One form of this might be an email service that records how many messages it was sent." — [Fowler, "Test Double"](https://martinfowler.com/bliki/TestDouble.html)

SOURCE FACT (Rank 1): "Mocks are pre-programmed with expectations which form a specification of the calls they are expected to receive. They can throw an exception if they receive a call they don't expect and are checked during verification to ensure they got all the calls they were expecting." — [Fowler, "Test Double"](https://martinfowler.com/bliki/TestDouble.html)

SOURCE FACT (Rank 1): Meszaros' role table assigns each type a purpose: Dummy Object = "Attribute or Method Parameter"; Test Stub = "Verify indirect inputs of SUT"; Test Spy = "Verify indirect outputs of SUT"; Mock Object = "Verify indirect outputs of SUT"; Fake Object = "Run (unrunnable) tests (faster)". — [Meszaros, "Mocks, Fakes, Stubs and Dummies"](http://xunitpatterns.com/Mocks,%20Fakes,%20Stubs%20and%20Dummies.html)

SOURCE FACT (Rank 1): "We replace a real object with a test-specific object that feeds the desired indirect inputs into the system under test." — [Meszaros, "Test Stub"](http://xunitpatterns.com/Test%20Stub.html)

SOURCE FACT (Rank 1): "Use a Test Double to capture the indirect output calls made to another component by the system under test (SUT) for later verification by the test." — [Meszaros, "Test Spy"](http://xunitpatterns.com/Test%20Spy.html)

SOURCE FACT (Rank 1): "Replace an object the system under test (SUT) depends on with a test-specific object that verifies it is being used correctly by the SUT." — [Meszaros, "Mock Object"](http://xunitpatterns.com/Mock%20Object.html)

SOURCE FACT (Rank 1): "The test need not do any assertions at all!" (for a Mock Object, because verification is delegated to the double). — [Meszaros, "Mock Object"](http://xunitpatterns.com/Mock%20Object.html)

SOURCE FACT (Rank 1): "a Dummy Object isn't really a Test Double per se but rather an alternative to the value patterns Literal Value, Derived Value and Generated Value." — [Meszaros, "Test Double"](http://xunitpatterns.com/Test%20Double.html)

SOURCE FACT (Rank 1): "Mock Objects can be either "strict" or "lenient" (sometimes called "nice".) A "strict" Mock Object fails the test if the calls are received in a different order than was specified when the Mock Object was programmed. A "lenient" Mock Object tolerates out-of-order calls." — [Meszaros, "Mock Object"](http://xunitpatterns.com/Mock%20Object.html)

AI INFERENCE: The five types differ along two axes: (a) whether they carry a working implementation (Fake) or canned/empty behavior (Dummy, Stub, Spy, Mock), and (b) whether they are used to feed inputs (Stub), capture outputs (Spy), or assert outputs (Mock).

## 3. State verification vs behavior verification

SOURCE FACT (Rank 1): "This difference is actually two separate differences. On the one hand there is a difference in how test results are verified: a distinction between state verification and behavior verification." — [Fowler, "Mocks Aren't Stubs"](https://martinfowler.com/articles/mocksArentStubs.html)

SOURCE FACT (Rank 1): State verification "means that we determine whether the exercised method worked correctly by examining the state of the SUT and its collaborators after the method was exercised." — [Fowler, "Mocks Aren't Stubs"](https://martinfowler.com/articles/mocksArentStubs.html)

SOURCE FACT (Rank 1): Behavior verification is where "we instead check to see if the order made the correct calls on the warehouse." — [Fowler, "Mocks Aren't Stubs"](https://martinfowler.com/articles/mocksArentStubs.html)

SOURCE FACT (Rank 1): "Of these kinds of doubles, only mocks insist upon behavior verification. The other doubles can, and usually do, use state verification." — [Fowler, "Mocks Aren't Stubs"](https://martinfowler.com/articles/mocksArentStubs.html)

SOURCE FACT (Rank 1): "Mock objects always use behavior verification, a stub can go either way. Meszaros refers to stubs that use behavior verification as a Test Spy." — [Fowler, "Mocks Aren't Stubs"](https://martinfowler.com/articles/mocksArentStubs.html)

SOURCE FACT (Rank 1): "Because a Test Spy does not fail the test at the first deviation from the expected behavior like a Mock Object, our tests will be able to include more detailed diagnostic information in the Assertion Message based on information gathered after a Mock Object would have failed the test." — [Meszaros, "Test Spy"](http://xunitpatterns.com/Test%20Spy.html)

SOURCE FACT (Rank 1): "We should not use a Mock Object if a failed assertion cannot be reported effectively back to the Test Runner." — [Meszaros, "Mock Object"](http://xunitpatterns.com/Mock%20Object.html)

AI INFERENCE: State verification observes results after exercise; behavior verification observes the interactions during exercise. A Spy is the behavior-verification option that keeps assertions in the test body, whereas a Mock moves assertions into the double.

## 4. Classical (Chicago/Detroit) vs mockist (London) schools

SOURCE FACT (Rank 1): "The classical TDD style is to use real objects if possible and a double if it's awkward to use the real thing." — [Fowler, "Mocks Aren't Stubs"](https://martinfowler.com/articles/mocksArentStubs.html)

SOURCE FACT (Rank 1): "A mockist TDD practitioner, however, will always use a mock for any object with interesting behavior." — [Fowler, "Mocks Aren't Stubs"](https://martinfowler.com/articles/mocksArentStubs.html)

SOURCE FACT (Rank 1): "You sometimes see "Detroit" style used for "classical" and "London" for "mockist". This alludes to the fact that XP was originally developed with the C3 project in Detroit and the mockist style was developed by early XP adopters in London." — [Fowler, "Mocks Aren't Stubs"](https://martinfowler.com/articles/mocksArentStubs.html)

SOURCE FACT (Rank 1): "many mockist TDDers dislike that term, and indeed any terminology that implies a different style between classical and mockist testing. They don't consider that there is a useful distinction to be made between the two styles." — [Fowler, "Mocks Aren't Stubs"](https://martinfowler.com/articles/mocksArentStubs.html)

SOURCE FACT (Rank 1): "If you introduce a bug to a system with mockist testing, it will usually cause only tests whose SUT contains the bug to fail. With the classic approach, however, any tests of client objects can also fail." — [Fowler, "Mocks Aren't Stubs"](https://martinfowler.com/articles/mocksArentStubs.html)

SOURCE FACT (Rank 1): "Mockist tests are thus more coupled to the implementation of a method. Changing the nature of calls to collaborators usually cause a mockist test to break." — [Fowler, "Mocks Aren't Stubs"](https://martinfowler.com/articles/mocksArentStubs.html)

SOURCE FACT (Rank 1): "In essence classic xunit tests are not just unit tests, but also mini-integration tests." — [Fowler, "Mocks Aren't Stubs"](https://martinfowler.com/articles/mocksArentStubs.html)

SOURCE FACT (Rank 1): "I've always been a old fashioned classic TDDer and thus far I don't see any reason to change. I don't see any compelling benefits for mockist TDD, and am concerned about the consequences of coupling tests to implementation." — [Fowler, "Mocks Aren't Stubs"](https://martinfowler.com/articles/mocksArentStubs.html)

SOURCE CLAIM (Rank 4): "The London style emerged from Steve Freeman and Nat Pryce's work as pioneers of test doubles. Their seminal paper on mock objects and subsequent book Growing Object-Oriented Software, Guided by Tests established this approach." — [Valverde Ramos, "TDD styles Classicist vs Outside-in"](https://emmanuelvalverderamos.substack.com/p/test-driven-development-styles-classicist)

SOURCE CLAIM (Rank 4): "The "Classicist" or "Chicago" style stems from Beck's early work, emphasizing TDD as a way to design systems incrementally." — [Valverde Ramos, "TDD styles Classicist vs Outside-in"](https://emmanuelvalverderamos.substack.com/p/test-driven-development-styles-classicist)

SOURCE CLAIM (Rank 4): London style defining characteristics include "Interaction-Based Testing: Tests validate communication between objects using mocks and stubs" and "Top-Down Design". — [Valverde Ramos, "TDD styles Classicist vs Outside-in"](https://emmanuelvalverderamos.substack.com/p/test-driven-development-styles-classicist)

SOURCE CLAIM (Rank 4): "In Growing Object-Oriented Software, Guided by Tests (GOOS), Freeman and Pryce never claim that you must write solitary unit tests. In fact, they are clear about the boundaries: "Don't mock values" and "Only mock peers, not internals."" — [Valverde Ramos, "TDD styles Classicist vs Outside-in"](https://emmanuelvalverderamos.substack.com/p/test-driven-development-styles-classicist)

SOURCE CLAIM (Rank 4): "when you do TDD outside-in, you're not verifying behavior, you're verifying your design is correct." (attributed to Sandro Mancuso) — [Valverde Ramos, "TDD styles Classicist vs Outside-in"](https://emmanuelvalverderamos.substack.com/p/test-driven-development-styles-classicist)

SOURCE CLAIM (Rank 5): "London School says all dependencies are collaborators, & should be stubbed/mocked." — [Warden, "Chicago and London TDD Styles for Functional Programming"](https://dev.to/jesterxl/chicago-and-london-tdd-styles-for-functional-programming-455h)

SOURCE CLAIM (Rank 5): "Chicago Style is the best way to learn unit testing in FP if you're a n00b. This is because the rules are the same everywhere: Step 1: call a function with inputs Step 2: assert return value is what you expect with those inputs." — [Warden, "Chicago and London TDD Styles for Functional Programming"](https://dev.to/jesterxl/chicago-and-london-tdd-styles-for-functional-programming-455h)

AI INFERENCE: The two schools are not a binary of "mock vs no mock"; they differ primarily in default isolation boundary and in whether tests are treated as a design tool (London/outside-in) or as state/output checks with doubles only where awkward (Chicago/classic).

PLAUSIBLE NOT VERIFIED: The claim that the "inside-out" label for classicist TDD is a London-school characterization rather than a prescription of Beck's original method is asserted by the Rank 4 source but was not confirmed against Beck's primary text in this pass.

## 5. When to mock / when to use each double

SOURCE FACT (Rank 1): "If it's an easy collaboration then the choice is simple. If I'm a classic TDDer I don't use a mock, stub or any kind of double. I use a real object and state verification." — [Fowler, "Mocks Aren't Stubs"](https://martinfowler.com/articles/mocksArentStubs.html)

SOURCE FACT (Rank 1): "If it's an awkward collaboration, then there's no decision if I'm a mockist - I just use mocks and behavior verification. If I'm a classicist then I do have a choice, but it's not a big deal which one to use." — [Fowler, "Mocks Aren't Stubs"](https://martinfowler.com/articles/mocksArentStubs.html)

SOURCE FACT (Rank 1): "A great example of this is a cache. The whole point of a cache is that you can't tell from its state whether the cache hit or missed - this is a case where behavior verification would be the wise choice for even a hard core classical TDDer." — [Fowler, "Mocks Aren't Stubs"](https://martinfowler.com/articles/mocksArentStubs.html)

SOURCE FACT (Rank 1): "A key indication for using a Test Stub is having Untested Code caused by the inability to control the indirect inputs of the SUT." — [Meszaros, "Test Stub"](http://xunitpatterns.com/Test%20Stub.html)

SOURCE FACT (Rank 1): "If we do need an observation point that allows us to verify the indirect outputs of the SUT, we should consider using a Mock Object or a Test Spy." — [Meszaros, "Test Stub"](http://xunitpatterns.com/Test%20Stub.html)

SOURCE FACT (Rank 1): "We should use a Test Spy if any of the following are true: We are verifying the indirect outputs of the SUT and we can cannot predict the value of all attributes of the interactions with the SUT ahead of time." — [Meszaros, "Test Spy"](http://xunitpatterns.com/Test%20Spy.html)

SOURCE FACT (Rank 1): "To use a Mock Object, we need to be able to predict the value of most or all arguments of the method calls before we exercise the SUT." — [Meszaros, "Mock Object"](http://xunitpatterns.com/Mock%20Object.html)

SOURCE FACT (Rank 1): Test doubles are indicated when there is an "Untested Requirement" (no observation point for indirect output), "Untested Code" (no control point for indirect input), or "Slow Tests". — [Meszaros, "Test Double"](http://xunitpatterns.com/Test%20Double.html)

SOURCE FACT (Rank 1): "we really should have at least one test that verifies it works without a Test Double." — [Meszaros, "Test Double"](http://xunitpatterns.com/Test%20Double.html)

SOURCE FACT (Rank 1): "excessive use of Test Doubles can result in Fragile Tests as a result of Overspecified Software." — [Meszaros, "Test Double"](http://xunitpatterns.com/Test%20Double.html)

SOURCE FACT (Rank 1): "It's at this point that I should stress that whichever style of test you use, you must combine it with coarser grained acceptance tests that operate across the system as a whole." — [Fowler, "Mocks Aren't Stubs"](https://martinfowler.com/articles/mocksArentStubs.html)

SOURCE FACT (Rank 1): "A common mistake made by test automaters new to stubs is to replace a part of the SUT that they are trying to test." — [Meszaros, "Test Stub"](http://xunitpatterns.com/Test%20Stub.html)

AI INFERENCE: Practical selection rule from the sources: use a Dummy only to satisfy a signature; use a Stub to control indirect inputs; use a Spy when outputs must be captured but cannot be fully predicted up front; use a Mock when the interaction itself is the specification and arguments are predictable; use a Fake when a lightweight working implementation is needed for speed or availability.

## 6. Trade-offs and cautions

SOURCE FACT (Rank 1): "Mockist testers consider this to be a major issue; it results in a lot of debugging in order to find the root of the error and fix it. However classicists don't express this as a source of problems." — [Fowler, "Mocks Aren't Stubs"](https://martinfowler.com/articles/mocksArentStubs.html)

SOURCE FACT (Rank 1): "Coupling to the implementation also interferes with refactoring, since implementation changes are much more likely to break tests than with classic testing." — [Fowler, "Mocks Aren't Stubs"](https://martinfowler.com/articles/mocksArentStubs.html)

SOURCE FACT (Rank 1): "An acknowledged issue with state-based verification is that it can lead to creating query methods only to support verification." — [Fowler, "Mocks Aren't Stubs"](https://martinfowler.com/articles/mocksArentStubs.html)

SOURCE FACT (Rank 1): "Mockist tests lose that quality. In addition you also run the risk that expectations on mockist tests can be incorrect, resulting in unit tests that run green but mask inherent errors." — [Fowler, "Mocks Aren't Stubs"](https://martinfowler.com/articles/mocksArentStubs.html)

SOURCE FACT (Rank 1): "Tests written using Mock Objects look different from more traditional tests because all the expected behavior must be specified before the SUT is exercised. This makes them harder to write and to understand for test automation neophytes." — [Meszaros, "Mock Object"](http://xunitpatterns.com/Mock%20Object.html)

SOURCE FACT (Rank 1): "Mock Objects (especially those created using dynamic mocking tools) often use the equals method of the various objects being compared. If our test-specific equality is different from how the SUT would interpret equals, we may not be able to use Mock Object." — [Meszaros, "Mock Object"](http://xunitpatterns.com/Mock%20Object.html)

AI INFERENCE: The recurring failure mode across sources is over-specification: doubles that encode incidental implementation detail make tests brittle and can pass while the system is wrong. The recurring remedy is to keep at least one real-collaborator test and to add coarser acceptance tests.

## Retrieval log

| URL | Result |
| --- | --- |
| https://martinfowler.com/bliki/TestDouble.html | OK — full page retrieved; five-type definitions and generic term. |
| https://martinfowler.com/articles/mocksArentStubs.html | OK — full article retrieved; state/behavior verification, classical/mockist, trade-offs. |
| http://xunitpatterns.com/Mocks,%20Fakes,%20Stubs%20and%20Dummies.html | OK — role table and terminology cross-reference retrieved. |
| http://xunitpatterns.com/Test%20Double.html | OK — generic pattern, when-to-use, cautions. |
| http://xunitpatterns.com/Test%20Stub.html | OK — stub definition, responder/saboteur, when-to-use. |
| http://xunitpatterns.com/Test%20Spy.html | OK — spy definition, when-to-use, retrieval interface. |
| http://xunitpatterns.com/Mock%20Object.html | OK — mock definition, strict/lenient, when-to-use. |
| https://softwareengineering.stackexchange.com/questions/123627/what-are-the-london-and-chicago-schools-of-tdd | FAILED — HTTP 403 (non-2xx); content not retrieved. |
| https://emmanuelvalverderamos.substack.com/p/test-driven-development-styles-classicist | OK — Rank 4 secondary account of London/Chicago history and GOOS guidance. |
| https://dev.to/jesterxl/chicago-and-london-tdd-styles-for-functional-programming-455h | OK — Rank 5 secondary account; functional-programming angle. |

## Open questions

- UNKNOWN: The exact wording of Freeman & Pryce's "Mock Roles, Not Objects" paper and GOOS book on when to mock was not retrieved directly; the "Don't mock values" / "Only mock peers, not internals" guidance is quoted only via a Rank 4 secondary source.
- UNKNOWN: Whether the "inside-out" characterization of classicist TDD is a London-school framing or Beck's own prescription — not resolved against Beck's primary text.
- UNKNOWN: The StackExchange canonical answer on London vs Chicago could not be retrieved (403); its content is not represented here.
- UNKNOWN: No primary source was retrieved that gives a numeric or threshold rule for "how many doubles is too many"; only qualitative cautions were found.
- PLAUSIBLE NOT VERIFIED: The claim that mockist tests are "less likely to suffer" from coarse-grained debugging problems is Fowler's hedged conjecture ("It's quite likely that..."), not an established result.
