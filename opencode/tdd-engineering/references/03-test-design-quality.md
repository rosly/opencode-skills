# Topic 3 — Test design and quality (evidence file)

Retrieved: 2026-10-05. Research round: 01. Scope: what makes a test good or bad in the xUnit-family / paradigm-neutral sense. In scope: FIRST principles and their variants, test structure (Four-Phase Test, Arrange-Act-Assert, Given-When-Then), test naming, the one-assertion-per-test debate, test smells, test data builders and object mothers. Out of scope: any language- or framework-specific mechanics (no Python/pytest, no tooling APIs), TDD process/rhythm (covered in other topics).

Notation: **SOURCE FACT** = Rank 1 (peer-reviewed paper, or a directly quoted primary artifact); **SOURCE CLAIM** = Rank 2–6; **AI INFERENCE** = reasoning derived from quoted facts; **PLAUSIBLE, NOT VERIFIED**; **UNKNOWN**. Quotations are the shortest exact passage supporting the line, with a descriptive inline link on the same line.

---

## 1. What makes a test good: the FIRST principles

- **SOURCE CLAIM** (Rank 2, book content reported by a study-notes page; the primary book text could not be retrieved — see Retrieval log): Clean Code states the acronym as "Fast: Tests should be fast", "Independent: Test shouldn't depend on each other", "Repeatable: Tests should be repeatable in any environment", "Self-Validating: Test should have a boolean output, pass or fail", "Timely: Tests need to be written in a timely fashion." ([Dsons' notes on Clean Code, Ch. 9](https://notes.d-sons.com/textbooks/clean-code/ch09)).
- **SOURCE CLAIM** (Rank 2, same page): "Clean tests follow five other rules as well: Fast, Independent, Repeatable, Self-Validating, Timely." ([Dsons' notes on Clean Code, Ch. 9](https://notes.d-sons.com/textbooks/clean-code/ch09)).
- **SOURCE CLAIM** (Rank 2, same page, on the one-assertion rule): "Every unit test should ideally have one assert statement." ([Dsons' notes on Clean Code, Ch. 9](https://notes.d-sons.com/textbooks/clean-code/ch09)).
- **SOURCE CLAIM** (Rank 3, practitioner training material): the acronym is rendered with an alternative middle letter and an added sixth letter — "To write good unit tests apply the 'FIRST-U' rules: Fast, Isolated/Independent, Repeatable, Self-validating, Timely and Understandable." ([TMAP, Unit Testing Principles](https://www.tmap.net/building-blocks/unit-testing-principles/)).
- **SOURCE CLAIM** (Rank 3, same page): "A repeatable test is one that produces the same result each time you run it." ([TMAP, Unit Testing Principles](https://www.tmap.net/building-blocks/unit-testing-principles/)).
- **SOURCE CLAIM** (Rank 3, same page): "Tests must be self-validating. This means each test must be able to determine if the actual output is according to the expected output." ([TMAP, Unit Testing Principles](https://www.tmap.net/building-blocks/unit-testing-principles/)).
- **SOURCE CLAIM** (Rank 3, same page, on naming as a quality criterion): "A unit test should have a title in the form of a user story or a description of what it does and what to expect." ([TMAP, Unit Testing Principles](https://www.tmap.net/building-blocks/unit-testing-principles/)).

**Conflict / naming variant (surface, do not silently resolve).** The topic brief lists the "I" as *Isolated*; Clean Code as reported uses *Independent*; TMAP uses *Isolated/Independent*. The "T" is *Timely* in Clean Code as reported, while some derivative material lists *Thorough* instead. This is a naming variant across secondary sources, not evidence that the underlying criteria differ.
- **AI INFERENCE**: The five criteria are stable in substance (fast, non-interdependent, environment-independent, machine-checked, written at the right time); only the mnemonic wording varies. The canonical-claim attribution to Clean Code is corroborated only by secondary pages in this capture, so it is SOURCE CLAIM rather than SOURCE FACT until the book text is inspected.

---

## 2. Structuring a test: Four-Phase Test, Arrange-Act-Assert, Given-When-Then

- **SOURCE CLAIM** (Rank 2, book companion site): "We design each test to have four distinct phases that are executed in sequence. The four parts are fixture setup, exercise SUT, result verification and fixture teardown." ([Meszaros, Four-Phase Test, xUnit Patterns](http://xunitpatterns.com/Four%20Phase%20Test.html)).
- **SOURCE CLAIM** (Rank 2, same page, on why it matters): "Clearly identifying the four phases makes the intent of the test much easier to see." ([Meszaros, Four-Phase Test, xUnit Patterns](http://xunitpatterns.com/Four%20Phase%20Test.html)).
- **SOURCE CLAIM** (Rank 2, same page, on single-condition tests): "In fact, it is preferable to have many small Single Condition Tests." ([Meszaros, Four-Phase Test, xUnit Patterns](http://xunitpatterns.com/Four%20Phase%20Test.html)).
- **SOURCE CLAIM** (Rank 3, originator's own page): Bill Wake named and observed Arrange-Act-Assert in 2001 — "I (Bill Wake) observed and named the pattern in 2001. 'Arrange-Act-Assert' has been the full name the whole time." ([Bill Wake, 3A – Arrange, Act, Assert, XP123](https://xp123.com/articles/3a-arrange-act-assert/)).
- **SOURCE CLAIM** (Rank 3, same page, definition): "**Arrange**: Set up the object to be tested. ... **Act**: Act on the object (through some mutator). ... **Assert**: Make claims about the object, its collaborators, its parameters, and possibly (rarely!!) global state." ([Bill Wake, XP123](https://xp123.com/articles/3a-arrange-act-assert/)).
- **SOURCE CLAIM** (Rank 3, same page, on multi-step tests): "Such multi-step unit tests are usually better off being split into several tests." ([Bill Wake, XP123](https://xp123.com/articles/3a-arrange-act-assert/)).
- **SOURCE CLAIM** (Rank 3, Fowler's bliki): "The essential idea is to break down writing a scenario (or test) into three sections" — "The **given** part describes the state of the world before you begin the behavior", "The **when** section is that behavior that you're specifying", "the **then** section describes the changes you expect due to the specified behavior." ([Fowler, GivenWhenThen](https://martinfowler.com/bliki/GivenWhenThen.html)).
- **SOURCE CLAIM** (Rank 3, same page, attribution and equivalence): Given-When-Then "is an approach developed by Daniel Terhorst-North and Chris Matts as part of Behavior-Driven Development (BDD)" and "You can also look at it as a reformulation of the Four-Phase Test pattern." ([Fowler, GivenWhenThen](https://martinfowler.com/bliki/GivenWhenThen.html)).
- **SOURCE CLAIM** (Rank 3, same page, mapping to AAA): "Meszaros describes the pattern as Four-Phase Test. His four phases are Setup (Given), Exercise (When), Verify (Then) and Teardown. Bill Wake came up with the formulation as Arrange, Act, Assert." ([Fowler, GivenWhenThen](https://martinfowler.com/bliki/GivenWhenThen.html)).
- **AI INFERENCE**: Four-Phase Test (setup/exercise/verify/teardown), Arrange-Act-Assert, and Given-When-Then denote the same structural decomposition; GWT and AAA merge the teardown phase into setup/automation. GWT is the BDD-facing phrasing, AAA the developer-facing phrasing, Four-Phase Test the pattern-catalogue phrasing.

---

## 3. Test naming

- **SOURCE CLAIM** (Rank 3, originator of the widely repeated convention): "The basic naming of a test comprises of three main parts: [UnitOfWork_StateUnderTest_ExpectedBehavior]." ([Roy Osherove, Naming standards for unit tests](https://osherove.com/blog/2005/4/3/naming-standards-for-unit-tests.html)).
- **SOURCE CLAIM** (Rank 3, same page, on requirement): "Your unit test name should express a specific requirement." ([Osherove](https://osherove.com/blog/2005/4/3/naming-standards-for-unit-tests.html)).
- **SOURCE CLAIM** (Rank 3, same page, on readability): "Test names which are written as short declarative statements are much more expressive that names which are machine readable." ([Osherove](https://osherove.com/blog/2005/4/3/naming-standards-for-unit-tests.html)).
- **SOURCE CLAIM** (Rank 3, Fowler): "Test frameworks tend to follow either naming style of xunit or BDD, the latter tend to name methods in the Given-When-Then style." ([Fowler, GivenWhenThen](https://martinfowler.com/bliki/GivenWhenThen.html)).
- **SOURCE FACT** (Rank 1, peer-reviewed survey): naming defects are recognized as a smell class — the survey groups "unsuitable naming" among test smells and notes different source terminologies collapse to the same concept: "'test-class name' ... 'unsuitable test method names' ... and 'using meaningless names for test methods' all refer to the same test-smell concept (unsuitable naming)." ([Garousi & Küçük 2018, *Smells in software test code*, JSS 138](https://pureadmin.qub.ac.uk/ws/portalfiles/portal/178889150/MLR_Smells_in_test_code_Dec_9.pdf)).
- **AI INFERENCE**: Two dominant naming families exist — a structural `UnitOfWork_StateUnderTest_ExpectedBehavior` style (Osherove) and a GWT/declarative sentence style (Fowler/BDD). Both trace back to making intent and expected behavior visible without reading the body; poor naming is itself catalogued as a smell.

---

## 4. The one-assertion-per-test debate

- **SOURCE CLAIM** (Rank 2, Clean Code as reported): "Every unit test should ideally have one assert statement. This basically comes down to each unit test testing one thing, one piece of functionality." ([Dsons' notes on Clean Code, Ch. 9](https://notes.d-sons.com/textbooks/clean-code/ch09)).
- **SOURCE CLAIM** (Rank 3, Bill Wake, against over-applying it): "I don't follow that guideline too closely." ([Bill Wake, XP123](https://xp123.com/articles/3a-arrange-act-assert/)).
- **SOURCE CLAIM** (Rank 3, same page, two valid reasons to keep several assertions): (1) "A series of assertions may indicate the object is missing functionality", (2) "A series of similar assertions might benefit from a helper (assertion) method." ([Bill Wake, XP123](https://xp123.com/articles/3a-arrange-act-assert/)).
- **SOURCE CLAIM** (Rank 2, Meszaros, distinguishing condition from assertion): "Some test drivers insist on one assertion per test." — but "the current principle is Verify One Condition per Test" and "when it doesn't [make the test more readable], I wouldn't be too dogmatic about insisting on a single assertion." ([Meszaros, Principles of Test Automation](http://xunitpatterns.com/Principles%20of%20Test%20Automation.html)).
- **SOURCE CLAIM** (Rank 2, same page, the rationale for one condition): "when one assertion fails, the rest of the test is not executed. This makes it hard to achieve Defect Localization." ([Meszaros, Principles of Test Automation](http://xunitpatterns.com/Principles%20of%20Test%20Automation.html)).
- **SOURCE CLAIM** (Rank 3, Roy Osherove, for the rule): "I personally am in favor of the 'single assert per unit test' idea" and "a test with multiple asserts is actually testing multiple things, so it may as well be considered as multiple tests." ([Osherove, Avoid multiple asserts revisited](https://osherove.com/blog/2006/10/3/avoid-multiple-asserts-in-a-single-unit-test-revisited.html)).
- **SOURCE CLAIM** (Rank 3, same page, framework-driven rationale): "all unit test frameworks I know ... will fail the test on the first failing assert call" so later assertions in the same test "won't run and you won't know if they would have succeeded." ([Osherove](https://osherove.com/blog/2006/10/3/avoid-multiple-asserts-in-a-single-unit-test-revisited.html)).
- **SOURCE FACT** (Rank 1, peer-reviewed survey, reporting the guideline landscape): "There are guidelines which recommend that it is a good idea to include only a single assert or a few of them per test." ([Garousi & Küçük 2018, JSS 138](https://pureadmin.qub.ac.uk/ws/portalfiles/portal/178889150/MLR_Smells_in_test_code_Dec_9.pdf)).
- **AI INFERENCE**: The live distinction is *one condition per test* (the defensible principle, because first-failure aborts the run and destroys defect localization) versus *one assertion statement per test* (a stricter heuristic that Wake, Meszaros, and Osherove all treat as optional). Extra assertions that probe different dimensions of a single condition are acceptable; extra assertions that probe different conditions should be split or hidden behind a custom assertion/verification helper.

---

## 5. Test smells

### 5.1 Origin and catalogues

- **SOURCE FACT** (Rank 1, peer-reviewed XP2001 paper, CWI report SEN-R0119; the first to apply "code smells" to test code): "We found that refactoring test code is different from refactoring production code in two ways: (1) there is a distinct set of bad smells involved, and (2) improving test code involves additional test-specific refactorings." ([van Deursen, Moonen, van den Bergh & Kok 2001, *Refactoring Test Code*, XP2001](https://ir.cwi.nl/pub/4324/04324D.pdf)).
- **SOURCE FACT** (Rank 1, same paper): "we describe a set of bad smells that indicate trouble in test code, and a collection of test refactorings to remove these smells." ([van Deursen et al. 2001](https://ir.cwi.nl/pub/4324/04324D.pdf)).
- **SOURCE FACT** (Rank 1, same paper, 11 named smells): the paper enumerates Mystery Guest, Resource Optimism, Test Run War, General Fixture, Eager Test, Lazy Test, Assertion Roulette, Indirect Testing, For Testers Only, Sensitive Equality, and Test Code Duplication. ([van Deursen et al. 2001](https://ir.cwi.nl/pub/4324/04324D.pdf)).
- **SOURCE FACT** (Rank 1, peer-reviewed survey): "As a type of anti-pattern, test smells are defined as poorly designed tests and their presence may negatively affect the quality of test suites and production code." ([Garousi & Küçük 2018, *Smells in software test code*, JSS 138](https://pureadmin.qub.ac.uk/ws/portalfiles/portal/178889150/MLR_Smells_in_test_code_Dec_9.pdf)).
- **SOURCE FACT** (Rank 1, same survey): "A test smell refers to any symptom in test code that indicates a deeper problem." ([Garousi & Küçük 2018](https://pureadmin.qub.ac.uk/ws/portalfiles/portal/178889150/MLR_Smells_in_test_code_Dec_9.pdf)).
- **SOURCE FACT** (Rank 1, same survey, smell vs. bug): "Bugs (faults) in test code are issues that ... change the intended (expected) behaviour of the test ..., whereas test smells are issues that lower quality of tests, e.g., low execution speed (the slow test smell), low readability (the obscure test smell), low maintainability, and low fault detection power." ([Garousi & Küçük 2018](https://pureadmin.qub.ac.uk/ws/portalfiles/portal/178889150/MLR_Smells_in_test_code_Dec_9.pdf)).
- **SOURCE CLAIM** (Rank 2, Meszaros catalogue; three categories): code smells — Obscure Test, Conditional Test Logic, Hard-to-Test Code, Test Code Duplication, Test Logic in Production; behavior smells — Assertion Roulette, Erratic Test, Fragile Test, Frequent Debugging, Manual Intervention, Slow Tests; project smells — Buggy Tests, Developers Not Writing Tests, High Test Maintenance Cost, Production Bugs. ([Meszaros, Test Smells, xUnit Patterns](http://xunitpatterns.com/Test%20Smells.html)).
- **SOURCE CLAIM** (Rank 2, Meszaros, attribution of specific smells to the 2001 paper): "*Assertion Roulette* and *Eager Test* were first described in a paper at XP2001 called 'Refactoring Test Code'." ([Meszaros, Assertion Roulette](http://xunitpatterns.com/Assertion%20Roulette.html)); and "*Sensitive Equality* and *Fragile Fixture* were first described in [RTC] which was the first paper published on test smells and refactoring test code." ([Meszaros, Fragile Test](http://xunitpatterns.com/Fragile%20Test.html)).
- **SOURCE CLAIM** (Rank 2, Meszaros, on smell taxonomy size in later work): the site lists 11 test smells in its index, including sub-smells and project smells. ([Meszaros, Test Smells index](http://xunitpatterns.com/Test%20Smells.html)).
- **AI INFERENCE**: The canonical smell vocabulary originates in van Deursen et al. (2001) and was substantially expanded by Meszaros; the 2018 survey later consolidated a much larger catalogue (see §7). Treat "the" list of smells as open-ended and partly overlapping.

### 5.2 Individual smells (short definitions with exact quotes)

- **SOURCE FACT** (Rank 1, van Deursen): **Mystery Guest** — "When a test uses external resources, such as a file containing test data, the test is no longer self contained." ([van Deursen et al. 2001](https://ir.cwi.nl/pub/4324/04324D.pdf)).
- **SOURCE FACT** (Rank 1, van Deursen): **Resource Optimism** — "Test code that makes optimistic assumptions about the existence (or absence) and state of external resources ... can cause non-deterministic behavior in test outcomes." ([van Deursen et al. 2001](https://ir.cwi.nl/pub/4324/04324D.pdf)).
- **SOURCE FACT** (Rank 1, van Deursen): **Test Run War** — "Such wars arise when the tests run fine as long as you are the only one testing but fail when more programmers run them." ([van Deursen et al. 2001](https://ir.cwi.nl/pub/4324/04324D.pdf)).
- **SOURCE FACT** (Rank 1, van Deursen): **General Fixture** — "Things start to smell when the setUp fixture is too general and different tests only access part of the fixture." ([van Deursen et al. 2001](https://ir.cwi.nl/pub/4324/04324D.pdf)).
- **SOURCE FACT** (Rank 1, van Deursen): **Eager Test** — "When a test method checks several methods of the object to be tested, it is hard to read and understand, and therefore more difficult to use as documentation." ([van Deursen et al. 2001](https://ir.cwi.nl/pub/4324/04324D.pdf)).
- **SOURCE FACT** (Rank 1, van Deursen): **Lazy Test** — "This occurs when several test methods check the same method using the same fixture (but for example check the values of different instance variables)." ([van Deursen et al. 2001](https://ir.cwi.nl/pub/4324/04324D.pdf)).
- **SOURCE FACT** (Rank 1, van Deursen): **Assertion Roulette** — "'Guess what's wrong?' This smell comes from having a number of assertions in a test method that have no explanation." ([van Deursen et al. 2001](https://ir.cwi.nl/pub/4324/04324D.pdf)).
- **SOURCE FACT** (Rank 1, van Deursen): **Indirect Testing** — "It starts to smell when a test class contains methods that actually perform tests on other objects." ([van Deursen et al. 2001](https://ir.cwi.nl/pub/4324/04324D.pdf)).
- **SOURCE FACT** (Rank 1, van Deursen): **For Testers Only** — "When a production class contains methods that are only used by test methods" they should be removed or moved to a test subclass. ([van Deursen et al. 2001](https://ir.cwi.nl/pub/4324/04324D.pdf)).
- **SOURCE FACT** (Rank 1, van Deursen): **Sensitive Equality** — "It is fast and easy to write equality checks using the toString method." (and such tests break when the string representation changes). ([van Deursen et al. 2001](https://ir.cwi.nl/pub/4324/04324D.pdf)).
- **SOURCE FACT** (Rank 1, van Deursen): **Test Code Duplication** — "Test code may contain undesirable duplication. In particular the parts that set up test fixtures are susceptible to this problem." ([van Deursen et al. 2001](https://ir.cwi.nl/pub/4324/04324D.pdf)).
- **SOURCE CLAIM** (Rank 2, Meszaros): **Obscure Test** — "It is difficult to understand the test at a glance." ([Meszaros, Obscure Test](http://xunitpatterns.com/Obscure%20Test.html)).
- **SOURCE CLAIM** (Rank 2, same page): **Eager Test / Mystery Guest / General Fixture / Irrelevant Information / Hard-Coded Test Data / Indirect Testing** are the named causes of Obscure Test. ([Meszaros, Obscure Test](http://xunitpatterns.com/Obscure%20Test.html)).
- **SOURCE CLAIM** (Rank 2, Meszaros): **Erratic Test** — "One or more tests are behaving erratically; sometimes they pass and sometimes they fail." Named causes include Interacting Tests, Interacting Test Suites, Lonely Test, Resource Leakage, Resource Optimism, Unrepeatable Test, Test Run War, and Nondeterministic Test. ([Meszaros, Erratic Test](http://xunitpatterns.com/Erratic%20Test.html)).
- **SOURCE CLAIM** (Rank 2, Meszaros): **Fragile Test** — "A test fails to compile or run when the system under test (SUT) is changed in ways that do not affect the part the test is exercising." Four sensitivities: Interface, Behavior, Data, Context; also Overspecified Software and Sensitive Equality. ([Meszaros, Fragile Test](http://xunitpatterns.com/Fragile%20Test.html)).
- **SOURCE CLAIM** (Rank 2, Meszaros): **Conditional Test Logic** — "A test contains code that may or may not be executed"; "Any control structures within a Test Method should be viewed with extreme suspicion!" ([Meszaros, Conditional Test Logic](http://xunitpatterns.com/Conditional%20Test%20Logic.html)).
- **SOURCE CLAIM** (Rank 2, Meszaros): **Slow Tests** — "The tests take too long to run." ([Meszaros, Slow Tests](http://xunitpatterns.com/Slow%20Tests.html)).
- **SOURCE CLAIM** (Rank 2, Meszaros): **Test Code Duplication** — "The same test code is repeated many times." ([Meszaros, Test Code Duplication](http://xunitpatterns.com/Test%20Code%20Duplication.html)).
- **AI INFERENCE**: Across both catalogues the recurring mechanical causes are the same: shared or over-general fixture state (General Fixture, Erratic Test), hidden data (Mystery Guest, Hard-Coded Test Data), absent or ambiguous verification messages (Assertion Roulette), branching/loops in test code (Conditional Test Logic), and over-coupling to implementation (Fragile Test / Overspecified Software).

---

## 6. Test data builders and object mothers

- **SOURCE CLAIM** (Rank 1-attributed bibliographic fact, verified in a doctoral dissertation): the Object Mother pattern originates with Schuh and Punke — the dissertation states: "Schuh et al. [Schuh and Punke, 2001] describe a so called mock framework called 'Object Mother' to create scenarios which are difficult to set up otherwise." ([Gälli 2006, *Modeling Examples to Test and Understand Software*, Univ. Bern, §2.6](https://scg.unibe.ch/archive/phd/gaelli-phd.pdf)).
- **SOURCE CLAIM** (Rank 1-attributed, same dissertation bibliography): "Peter Schuh and Stephanie Punke. ObjectMother, easing test object creation in XP, 2001, http://www.xpuniverse.com/2001/pdfs/Testing03.pdf." ([Gälli 2006, bibliography](https://scg.unibe.ch/archive/phd/gaelli-phd.pdf)). The original XP Universe 2001 PDF itself could not be retrieved (see Retrieval log).
- **SOURCE CLAIM** (Rank 3, originator's own article): "An Object Mother is a class that contains a number of (usually static) Factory Methods that create objects for use in tests." ([Nat Pryce, Test Data Builders: an alternative to the Object Mother pattern, 2007-08-27](https://web.archive.org/web/20231224102029/http://www.natpryce.com/articles/000714.html)).
- **SOURCE CLAIM** (Rank 3, same article, the failure mode): "However, the Object Mother pattern does not cope at all well with variation in the test data. Every time programmers need some slightly different test data they add another factory method to the Object Mother." ([Nat Pryce 2007](https://web.archive.org/web/20231224102029/http://www.natpryce.com/articles/000714.html)).
- **SOURCE CLAIM** (Rank 3, same article, the remedy): "A solution is to use the Builder Pattern. For each class you want to use in a test, create a Builder for that class that: 1. Has an instance variable for each constructor parameter 2. Initialises its instance variables to commonly used or safe values 3. Has a `build` method that creates a new object using the values in its instance variables 4. Has 'chainable' public methods for overriding the values in its instance variables." ([Nat Pryce 2007](https://web.archive.org/web/20231224102029/http://www.natpryce.com/articles/000714.html)).
- **SOURCE CLAIM** (Rank 3, same article, isolation benefit): "Tests are isolated from those aspects of the objects' structure that have no bearing on the test. ... You can add constructor arguments without breaking tests at all." ([Nat Pryce 2007](https://web.archive.org/web/20231224102029/http://www.natpryce.com/articles/000714.html)).
- **SOURCE CLAIM** (Rank 3, same article, readability benefit of named overrides): "the test code is easier to write and read because the parameters are clearly identified." ([Nat Pryce 2007](https://web.archive.org/web/20231224102029/http://www.natpryce.com/articles/000714.html)).
- **AI INFERENCE**: Object Mother centralizes fixture construction behind named factory methods (improves readability, but bloats and duplicates under variation); Test Data Builder keeps per-object builder types with safe defaults plus chainable overrides, so each test states only the fields that matter and becomes insulated from unrelated structural change. Builder is the later refinement intended to fix Object Mother's data-variation problem.
- **PLAUSIBLE, NOT VERIFIED**: the term "test data builder" is attributed by third parties to Freeman & Pryce's book *Growing Object-Oriented Software, Guided by Tests* (2009), chapter 22. The book itself was not inspected in this capture; the pattern's public origin article is the Nat Pryce 2007 post above. (Lead from search results only.)

---

## 7. Empirical evidence on test smells and quality

- **SOURCE FACT** (Rank 1, peer-reviewed multivocal literature mapping, *Journal of Systems and Software*): "Our review has identified the largest catalogue of test smells, along with the summary of guidelines/techniques and the tools to deal with those smells." ([Garousi & Küçük 2018, JSS 138](https://pureadmin.qub.ac.uk/ws/portalfiles/portal/178889150/MLR_Smells_in_test_code_Dec_9.pdf)).
- **SOURCE FACT** (Rank 1, same survey, provenance of smell discovery): "In total, 81 sources (81/166=48%) presented new smell names and types. Out of those, only 9 were formally-published sources, while 72 were grey sources." ([Garousi & Küçük 2018](https://pureadmin.qub.ac.uk/ws/portalfiles/portal/178889150/MLR_Smells_in_test_code_Dec_9.pdf)).
- **SOURCE FACT** (Rank 1, same survey quoting the Google Testing Blog): "Almost 16% of our tests have some level of flakiness associated with them!" ([Garousi & Küçük 2018, §2.1, quoting the Google Testing Blog](https://pureadmin.qub.ac.uk/ws/portalfiles/portal/178889150/MLR_Smells_in_test_code_Dec_9.pdf)).
- **SOURCE FACT** (Rank 1, peer-reviewed empirical study, *Empirical Software Engineering*): "Although the number of test smell instances increases, test smell density decreases as systems evolve." ([Kim, Chen & Yang 2021, *The Secret Life of Test Smells*, EMSE](https://jinqiuyang.github.io/papers/emse21-test-smell.pdf)).
- **SOURCE FACT** (Rank 1, same study): "most test smell removal (83%) is a by-product of feature maintenance activities" and "developers deliberately address the only 17% of test smells." ([Kim et al. 2021, EMSE](https://jinqiuyang.github.io/papers/emse21-test-smell.pdf)).
- **SOURCE FACT** (Rank 1, same study, on defect-proneness): "most types of test smells have a minimal effect on post-release defects. ... Some test smells (e.g., Conditional Test Logic, Exception Catch/Throw, and Mystery Guest) have an increasing relationship with a source code file's defect-proneness when controlling for confounding factors." ([Kim et al. 2021, EMSE](https://jinqiuyang.github.io/papers/emse21-test-smell.pdf)).
- **SOURCE FACT** (Rank 1, same study, commonly surfaced smells from the 2001 set): the 18 studied smells include Assertion Roulette, Eager Test, General Fixture, Lazy Test, Mystery Guest, Resource Optimism, Sensitive Equality, Conditional Test Logic, Duplicate Assert, Unknown Test, Sleepy Test, and Magic Number Test. ([Kim et al. 2021, EMSE, Table 1](https://jinqiuyang.github.io/papers/emse21-test-smell.pdf)).
- **SOURCE CLAIM** (Rank 2, Meszaros, distinguishing smell from bug): "Buggy Tests" and "Production Bugs" are *project* smells (downstream consequences), not the same thing as test smells. ([Meszaros, Test Smells index](http://xunitpatterns.com/Test%20Smells.html)).
- **AI INFERENCE**: The empirical record supports test smells as real but heterogeneous: they are widespread and mostly handled incidentally, and only a subset (Conditional Test Logic, Exception Catch/Throw, Mystery Guest) shows measurable association with defects. This undercuts any claim that "all smells are equally harmful" and argues for prioritizing smell types with demonstrated impact rather than chasing an exhaustive catalogue.

---

## Retrieval log

| URL | Result |
|-----|--------|
| http://xunitpatterns.com/Test%20Smells.html | Retrieved |
| http://xunitpatterns.com/Four%20Phase%20Test.html | Retrieved |
| http://xunitpatterns.com/Obscure%20Test.html | Retrieved |
| http://xunitpatterns.com/Assertion%20Roulette.html | Retrieved |
| http://xunitpatterns.com/Erratic%20Test.html | Retrieved |
| http://xunitpatterns.com/Fragile%20Test.html | Retrieved |
| http://xunitpatterns.com/Conditional%20Test%20Logic.html | Retrieved |
| http://xunitpatterns.com/Slow%20Tests.html | Retrieved |
| http://xunitpatterns.com/Test%20Code%20Duplication.html | Retrieved |
| http://xunitpatterns.com/Principles%20of%20Test%20Automation.html | Retrieved |
| http://xunitpatterns.com/vanDeursen.html | Retrieved |
| http://xunitpatterns.com/Test%20Data%20Builder.html | Failed (HTTP 404 — pattern not hosted here) |
| http://xunitpatterns.com/Object%20Mother.html | Failed (HTTP 404 — pattern not hosted here) |
| https://martinfowler.com/bliki/GivenWhenThen.html | Retrieved |
| https://xp123.com/articles/3a-arrange-act-assert/ | Retrieved |
| https://www.oreilly.com/library/view/clean-code-a/9780136083238/ | Failed (HTTP 403 — primary Clean Code text not accessible) |
| https://notes.d-sons.com/textbooks/clean-code/ch09 | Retrieved (secondary report of Clean Code Ch. 9) |
| https://www.tmap.net/building-blocks/unit-testing-principles/ | Retrieved |
| https://www.natpryce.com/articles/000714.html | Failed (transport error) |
| https://web.archive.org/web/20231224102029/http://www.natpryce.com/articles/000714.html | Retrieved (archived Nat Pryce article) |
| https://ir.cwi.nl/pub/4324/04324D.pdf | Failed natively (application/pdf unsupported); Retrieved via https://r.jina.ai/ |
| https://wiki.c2.com/?TestDataBuilder | Failed (page requires JavaScript; returned shell) |
| https://wiki.c2.com/?ObjectMother | Failed (page requires JavaScript; returned shell) |
| https://osherove.com/blog/2005/4/3/naming-standards-for-unit-tests.html | Retrieved |
| https://osherove.com/blog/2006/10/3/avoid-multiple-asserts-in-a-single-unit-test-revisited.html | Retrieved |
| https://www.semanticscholar.org/paper/Easing-Test-Object-Creation-in-XP-Schuh-Punke/a55fa574c23f04c86b3472c95cd68d5a3080d8da | Failed (no output returned) |
| https://www.yumpu.com/en/document/view/36565144/objectmother-easing-test-object-creation-in-xp-agile-alliance | Failed (no output returned) |
| https://pureadmin.qub.ac.uk/ws/portalfiles/portal/178889150/MLR_Smells_in_test_code_Dec_9.pdf | Retrieved via https://r.jina.ai/ (Garousi & Küçük 2018) |
| https://jinqiuyang.github.io/papers/emse21-test-smell.pdf | Retrieved via https://r.jina.ai/ (Kim et al. 2021) |
| https://scg.unibe.ch/archive/phd/gaelli-phd.pdf | Retrieved via https://r.jina.ai/ (Object Mother origin + bibliography verified) |
| https://testing.googleblog.com/2018/02/testing-on-toilet-cleanly-create-test.html | Partial (post body did not render; comments only) |
| https://www.google.com/search & https://scholar.google.com (via websearch tool) | Used for discovery only; not treated as evidence |

---

## Open questions

- **FIRST origin.** The acronym is widely attributed to Clean Code (Robert C. Martin). The primary book text was not retrievable (O'Reilly 403), so attribution rests on secondary pages. Separately, one low-rank comment claims "FIRST was originated by Tim Ottinger and Brett Schuhart." The true first publication and whether the original "I"/"T" were *Independent*/*Timely* or *Isolated*/*Thorough* remain UNKNOWN.
- **Object Mother primary source.** The original Schuh & Punke XP Universe 2001 PDF (xpuniverse.com) was not retrievable; the origin is confirmed only via a doctoral dissertation's citation and bibliography. The paper's own wording of the pattern is UNKNOWN.
- **Test Data Builder in the GOOS book.** Third parties attribute the pattern name to Freeman & Pryce (2009) ch. 22; the book was not inspected. The relation between the 2007 article and the 2009 book treatment is not established here.
- **Smell → defect causality.** Kim et al. show most smell types have minimal effect on post-release defects; a stronger causal design (e.g., controlled or replicated study) is needed to decide which smells are worth enforcing against. UNKNOWN.
- **One-assertion rule.** No decisive evidence was found that a literal one-assertion limit improves outcomes; the defensible rule appears to be one condition per test with first-failure localization as the mechanism. A controlled study discriminating the two rules was not found.
- **Failed retrievals as limitations.** The C2 wiki pages, O'Reilly, semantic scholar, yumpu, and the Google Testing Blog post body could not be retrieved by the available methods; nothing is concluded from their absence.