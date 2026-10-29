# TDD — Topic 2: Cycle Mechanics

Retrieved: 2026-10-05. Subject: Test-Driven Development (TDD) as a methodology.
Scope: how red-green-refactor works; the nano/micro/milli/primary cycles; the Three Laws of TDD; triangulation; the Transformation Priority Premise (TPP); "fake it till you make it"; obvious implementation; baby steps; the test list.
Out of scope: tooling, language specifics, empirical effectiveness evidence, and any single language's test framework. All wording below is deliberately paradigm-neutral; where a source uses a language-specific illustration it is described, not reproduced.

## Classification legend used in this file

- **SOURCE FACT (Rank 1)** — reserved for directly inspected source code at a revision, or scientific/peer-reviewed literature.
- **SOURCE CLAIM (Rank 2-6)** — a statement asserted by a source, with its rank noted. Rank 2 = primary authored documentation (the originators' own books, articles, and official project pages); Rank 4 = Wikipedia; Rank 5 = forums/community threads.
- **AI INFERENCE** — a logical consequence drawn by this analysis from nearby quoted evidence.
- **PLAUSIBLE, NOT VERIFIED** — technically possible but not established by the available evidence.
- **UNKNOWN** — what the evidence cannot decide.

Because TDD is a methodology rather than a running artifact, this topic contains **no SOURCE FACT (Rank 1) lines**: there is no relevant source code or peer-reviewed result being inspected. All externally sourced lines are **SOURCE CLAIM**. The originators' own works are treated as the strongest tier available (Rank 2) and are quoted most heavily. This is a deliberate, stated limitation, not an omission.

Primary works used and their editions:

- Kent Beck, *Test-Driven Development: By Example*, Addison-Wesley Professional, 1st edition, 2002/2003. ISBN-10 0-321-14653-0, ISBN-13 978-0-321-14653-3, 240 pages. Full text was obtained as an archive.org OCR transcript and cross-checked against a second OCR rendering. ([InformIT bibliographic record](https://www.informit.com/store/test-driven-development-by-example-9780321146533), [Pearson catalog record](https://www.pearson.com/en-us/subject-catalog/p/test-driven-development-by-example/P200000009421/9780321146533)).

## 1. The nested cycles (nano / micro / milli / primary)

Robert C. Martin ("Uncle Bob") names four nested cycles of TDD at four time scales, from seconds to hours. Each outer cycle contains many repetitions of the inner one.

**SOURCE CLAIM (Rank 2, Martin, 2014)** — The finest cycle is the "nano-cycle", defined by the Three Laws: "You follow them on almost a second-by-second basis. You will likely iterate them a dozen or so times before you finish a single unit test." ([The Cycles of TDD](https://blog.cleancoder.com/uncle-bob/2014/12/17/TheCyclesOfTDD.html)).

**SOURCE CLAIM (Rank 2, Martin, 2014)** — The next cycle is the micro-cycle, Red/Green/Refactor: "This cycle is typically executed once for every complete unit test, or once every dozen or so cycles of the three laws." ([The Cycles of TDD](https://blog.cleancoder.com/uncle-bob/2014/12/17/TheCyclesOfTDD.html)).

**SOURCE CLAIM (Rank 2, Martin, 2014)** — The ~10-minute cycle is the milli-cycle, the Specific/Generic cycle: "As the tests get more specific, the code gets more generic." ([The Cycles of TDD](https://blog.cleancoder.com/uncle-bob/2014/12/17/TheCyclesOfTDD.html)).

**SOURCE CLAIM (Rank 2, Martin, 2014)** — The hourly cycle is the primary cycle, concerned with architectural boundaries: "Ever hour or so we stop and check to see whether we have crossed, or are encroaching upon, a significant architectural boundary." ([The Cycles of TDD](https://blog.cleancoder.com/uncle-bob/2014/12/17/TheCyclesOfTDD.html)) [sic: source text reads "Ever hour"].

**SOURCE CLAIM (Rank 2, Martin, 2014)** — The Three Laws are what the nano-cycle *is*: "*The three laws* are the *nano-cycle* of TDD." ([The Cycles of TDD](https://blog.cleancoder.com/uncle-bob/2014/12/17/TheCyclesOfTDD.html)).

**SOURCE CLAIM (Rank 2, Martin, 2014)** — Red/Green/Refactor is the micro-cycle, and its rules are three: "1. Create a unit tests that fails / 2. Write production code that makes that test pass. / 3. Clean up the mess you just made." ([The Cycles of TDD](https://blog.cleancoder.com/uncle-bob/2014/12/17/TheCyclesOfTDD.html)).

**SOURCE CLAIM (Rank 2, Martin, 2014)** — The micro-cycle separates "works" from "well structured": "the RGR cycle tells us to first focus on making the software work correctly; and then, *and only then*, to focus on giving that working software a long-term survivable structure." ([The Cycles of TDD](https://blog.cleancoder.com/uncle-bob/2014/12/17/TheCyclesOfTDD.html)).

**SOURCE CLAIM (Rank 2, Martin, 2014)** — The milli-cycle applies the TPP: "This is the cycle in which we apply the [*Transformation Priority Premise*]." ([The Cycles of TDD](https://blog.cleancoder.com/uncle-bob/2014/12/17/TheCyclesOfTDD.html)).

**SOURCE CLAIM (Rank 2, Martin, 2014)** — Refactoring is continuous, not a scheduled task: "Refactoring is a continuous in-process activity, not something that is done late (and therefore optionally)." ([The Cycles of TDD](https://blog.cleancoder.com/uncle-bob/2014/12/17/TheCyclesOfTDD.html)).

**SOURCE CLAIM (Rank 2, Martin, 2014)** — A symptom of an outer-cycle failure is getting stuck, and the remedy is to backtrack tests: "Once you are stuck, the only solution is to backtrack up through the previous tests, deleting them, until you reach a test from which you can take a different fork in the road." ([The Cycles of TDD](https://blog.cleancoder.com/uncle-bob/2014/12/17/TheCyclesOfTDD.html)).

**AI INFERENCE**: The four cycles are not alternatives but the same activity observed at four granularities: the nano-cycle governs a single edit, the micro-cycle a single test-to-green transition, the milli-cycle the sequence/ordering of tests and generalization, and the primary cycle the architectural placement of those edits. The milli-cycle is where test *ordering* decisions (and thus TPP) live; the primary cycle is where design boundaries are chosen. A TDD practitioner who is "stuck" has failed to keep production code general enough at the milli-cycle, which then forces a large edit that violates the nano-cycle.

## 2. The Three Laws (nano-cycle)

The canonical formulation comes from the 2009 "97 Things Every Programmer Should Know" wiki article attributed to Uncle Bob; the live O'Reilly page no longer serves the article, so it was retrieved from the Internet Archive capture.

**SOURCE CLAIM (Rank 2, Martin, "The Three Laws of TDD", 2009)** — "1. You can't write any production code until you have first written a failing unit test. 2. You can't write more of a unit test than is sufficient to fail, and not compiling is failing. 3. You can't write more production code than is sufficient to pass the currently failing unit test." ([The Three Laws of Test-Driven Development](https://web.archive.org/web/20160309220415/http://programmer.97things.oreilly.com/wiki/index.php/The_Three_Laws_of_Test-Driven_Development)).

**SOURCE CLAIM (Rank 2, Martin, "The Three Laws of TDD", 2009)** — The consequence is a tight cycle: "If you follow these three laws you will be locked into a cycle that is, perhaps, 30 seconds long." ([The Three Laws of Test-Driven Development](https://web.archive.org/web/20160309220415/http://programmer.97things.oreilly.com/wiki/index.php/The_Three_Laws_of_Test-Driven_Development)).

**SOURCE CLAIM (Rank 2, Martin, 2014)** — Uncle Bob's own restatement, phrased as three "You must" rules, includes the compile clause in law 2: "You must not write more of a test than is sufficient to fail, or fail to compile." ([The Cycles of TDD](https://blog.cleancoder.com/uncle-bob/2014/12/17/TheCyclesOfTDD.html)).

**SOURCE CLAIM (Rank 2, Martin, 2014)** — The laws aim at line-level granularity learned by pairing with Beck: "He would write *one line* of a failing test, and then write the corresponding *line* of production code to make it pass." ([The Cycles of TDD](https://blog.cleancoder.com/uncle-bob/2014/12/17/TheCyclesOfTDD.html)).

**AI INFERENCE**: Law 3 is the nano-cycle counterpart of the micro-cycle's refactoring step; it is what prevents the micro-cycle from silently absorbing design work. The "or fail to compile" clause means the failing state includes non-compilation, which is what makes the very first line of a brand-new test a legitimate red state.

The API/manual for the *original* 97things article at its live O'Reilly URL was not retrievable; see Retrieval log. The Internet Archive capture is used as the best available primary text, and it self-identifies the author as "Uncle Bob" and is dated "last modified 18:19, 8 October 2009".

## 3. Red-Green-Refactor (micro-cycle)

Martin Fowler gives the modern three-step summary, adding that the test list is a separate initial step.

**SOURCE CLAIM (Rank 2, Fowler, 2023 revision)** — "In essence we follow three simple steps repeatedly: Write a test for the next bit of functionality you want to add. Write the functional code until the test passes. Refactor both new and old code to make it well structured." ([Test Driven Development](https://martinfowler.com/bliki/TestDrivenDevelopment.html)).

**SOURCE CLAIM (Rank 2, Fowler, 2023 revision)** — The steps are named and the initial list is called out: "Although these three steps, often summarized as *Red - Green - Refactor*, are the heart of the process, there's also a vital initial step where we write out a list of test cases first." ([Test Driven Development](https://martinfowler.com/bliki/TestDrivenDevelopment.html)).

**SOURCE CLAIM (Rank 2, Fowler, 2023 revision)** — Test-first forces interface thinking: "The second benefit is that thinking about the test first forces us to think about the interface to the code first." ([Test Driven Development](https://martinfowler.com/bliki/TestDrivenDevelopment.html)).

**SOURCE CLAIM (Rank 2, Fowler, 2023 revision)** — The common failure is skipping refactor: "The most common way that I hear to screw up TDD is neglecting the third step." ([Test Driven Development](https://martinfowler.com/bliki/TestDrivenDevelopment.html)).

**SOURCE CLAIM (Rank 2, Beck, TDD By Example, 2002)** — Beck's two rules and their implications preface the book: "Don't write a line of new code unless you first have a failing automated test. • Eliminate duplication." ([Test-Driven Development By Example, Preface/Introduction text](https://www2.cs.uh.edu/~rsingh/documents/software_design/TDD.pdf)).

**SOURCE CLAIM (Rank 2, Beck, TDD By Example, 2002)** — Beck names the karma-strength phrasing and the three phases: "Red— Write a little test that doesn't work, and perhaps doesn't even compile at first. / Green— Make the test work quickly, committing whatever sins necessary in the process. / Refactor— Eliminate all of the duplication created in merely getting the test to work. / Red/green/refactor—the TDD mantra." ([Test-Driven Development By Example](https://www2.cs.uh.edu/~rsingh/documents/software_design/TDD.pdf)).

**SOURCE CLAIM (Rank 2, Beck, TDD By Example, 2002)** — The same cycle is also framed as three imperatives "Make it run / Make it right": "1. Write a test. ... 2. Make it run. Quickly getting that bar to go to green dominates everything else. ... 3. Make it right. Now that the system is behaving, put the sinful ways of the recent past behind you. ... Remove the duplication that you have introduced, and get to green quickly." ([Test-Driven Development By Example](https://www2.cs.uh.edu/~rsingh/documents/software_design/TDD.pdf)).

**SOURCE CLAIM (Rank 2, Beck, TDD By Example, 2002)** — The goal is stated as "clean code that works", divided and conquered: "First we'll solve the 'that works' part of the problem. Then we'll solve the 'clean code' part." ([Test-Driven Development By Example](https://www2.cs.uh.edu/~rsingh/documents/software_design/TDD.pdf)).

**SOURCE CLAIM (Rank 2, Beck, TDD By Example, 2002)** — The mandated rhythm is five explicit steps, not three: "1. Quickly add a test / 2. Run all tests and see the new one fail / 3. Make a little change / 4. Run all tests and see them all succeed / 5. Refactor to remove duplication" ([Test-Driven Development By Example](https://www2.cs.uh.edu/~rsingh/documents/software_design/TDD.pdf)).

**AI INFERENCE**: The Five-Step Rhythm and RGR describe the same loop; Beck's step 2 ("see the new one fail") is the explicit *observation* of red that Martin's law 1 presupposes. The naming varies (make it run / make it right; red / green / refactor) but the ordering is invariant: failing test → minimal production change → duplication removal. Fowler's addition of an initial list step is a superset of Beck's rhythm, and Beck independently confirms it (Section 4).

## 4. The Test List

**SOURCE CLAIM (Rank 2, Beck, "Canon TDD", 2023)** — The five-step canon begins with the list: "1. Write a list of the test scenarios you want to cover ... 5. Until the list is empty, go back to #2" ([Canon TDD](https://tidyfirst.substack.com/p/canon-tdd) / [newsletter mirror](https://newsletter.kentbeck.com/p/canon-tdd)).

**SOURCE CLAIM (Rank 2, Beck, "Canon TDD", 2023)** — The list is behavioral analysis, kept separate from implementation decisions: "This is analysis, but behavioral analysis. You're thinking of all the different cases in which the behavior change should work." ([Canon TDD](https://tidyfirst.substack.com/p/canon-tdd)).

**SOURCE CLAIM (Rank 2, Beck, "Canon TDD", 2023)** — Only one item is made concrete at a time: "Turn exactly one item on the list into an actual, concrete, runnable test" ([Canon TDD](https://tidyfirst.substack.com/p/canon-tdd)).

**SOURCE CLAIM (Rank 2, Beck, "Canon TDD", 2023)** — New tests discovered mid-cycle are appended to the list, not written immediately: "If in the process of going red to green you discover the need for a new test, add it to the Test List." ([Canon TDD](https://tidyfirst.substack.com/p/canon-tdd)).

**SOURCE CLAIM (Rank 2, Beck, TDD By Example, 2002, "Test List" pattern, Ch. 25)** — "What should you test? Before you begin, write a list of all the tests you know you will have to write." ([Test-Driven Development By Example](https://www2.cs.uh.edu/~rsingh/documents/software_design/TDD.pdf)).

**SOURCE CLAIM (Rank 2, Beck, TDD By Example, 2002)** — The list holds operations, their null versions, and planned refactorings: "First, put on the list examples of every operation that you know you need to implement. Next, for those operations that don't already exist, put the null version of that operation on the list. Finally, list all of the refactorings that you think you will have to do." ([Test-Driven Development By Example](https://www2.cs.uh.edu/~rsingh/documents/software_design/TDD.pdf)).

**SOURCE CLAIM (Rank 2, Beck, TDD By Example, 2002)** — Writing all tests up front is rejected for green-bar proximity: "Second, if you have ten tests broken, you are a long way from the green bar." ([Test-Driven Development By Example](https://www2.cs.uh.edu/~rsingh/documents/software_design/TDD.pdf)).

**SOURCE CLAIM (Rank 2, Beck, TDD By Example, 2002, "One Step Test", Ch. 26)** — Test selection rule: "Which test should you pick next from the list? Pick a test that will teach you something and that you are confident you can implement." ([Test-Driven Development By Example](https://www2.cs.uh.edu/~rsingh/documents/software_design/TDD.pdf)).

**SOURCE CLAIM (Rank 2, Beck, TDD By Example, 2002, "Starter Test", Ch. 26)** — Starting rule: "Which test should you start with? Start by testing a variant of an operation that doesn't do anything." ([Test-Driven Development By Example](https://www2.cs.uh.edu/~rsingh/documents/software_design/TDD.pdf)).

**SOURCE CLAIM (Rank 2, Beck, TDD By Example, 2002)** — The list is a reminder, sketched as a running to-do: "We'll make a to-do list to remind us what all we need to do, keep us focused, and tell us when we are finished." ([Test-Driven Development By Example](https://www2.cs.uh.edu/~rsingh/documents/software_design/TDD.pdf)).

**SOURCE CLAIM (Rank 5, community forum, Beck 2004 thread)** — Beck confirms FITYMI vs Triangulation as two "schools" in a mailing-list reply: "There are two schools on writing tests to force you to replace '10' with 'amount * rate'. The first school I call Triangulation. ... The second alternative is FITYMI (Fake it til you make it)." ([testdrivendevelopment group, message #22, mirrored](https://groups.io/g/testdrivendevelopment/message/22)).

**AI INFERENCE**: The test list is the operational home of the milli-cycle and the primary cycle's entry point: it is where ordering is decided (One Step Test) and where architectural concerns (e.g., "make amount private", "hashCode()") are parked. The list also supplies the "simplest possible test" discipline that Beck describes in "Before You Begin", so it directly feeds the nano-cycle's first law.

## 5. Green-bar implementation strategies: Fake It, Obvious Implementation, Triangulate

Beck names three implementation strategies for reaching green. They are alternatives that a practitioner shifts between, not sequential stages of one cycle.

**SOURCE CLAIM (Rank 2, Beck, TDD By Example, 2002, "Fake It ('Til You Make It)", Ch. 28)** — "What is your first implementation once you have a broken test? Return a constant. Once you have the test running, gradually transform the constant into an expression using variables." ([Test-Driven Development By Example](https://www2.cs.uh.edu/~rsingh/documents/software_design/TDD.pdf)).

**SOURCE CLAIM (Rank 2, Beck, TDD By Example, 2002)** — The one-line definition of Fake It: "Fake It— Return a constant and gradually replace constants with variables until you have the real code." ([Test-Driven Development By Example](https://www2.cs.uh.edu/~rsingh/documents/software_design/TDD.pdf)).

**SOURCE CLAIM (Rank 2, Beck, TDD By Example, 2002)** — Fake It is justified by reading the constant as deliberate data duplication to be removed in refactor: "Does Fake It violate the rule that says you don't write any code that isn't needed? I don't think so, because in the refactoring step you are eliminating duplication of data between the test case and the code." ([Test-Driven Development By Example](https://www2.cs.uh.edu/~rsingh/documents/software_design/TDD.pdf)).

**SOURCE CLAIM (Rank 2, Beck, TDD By Example, 2002)** — The two effects of Fake It: "Psychological— Having a green bar feels completely different from having a red bar. ... Scope control— ... Starting with one concrete example and generalizing from there prevents you from prematurely confusing yourself with extraneous concerns." ([Test-Driven Development By Example](https://www2.cs.uh.edu/~rsingh/documents/software_design/TDD.pdf)).

**SOURCE CLAIM (Rank 2, Beck, TDD By Example, 2002, "Obvious Implementation", Ch. 28)** — "How do you implement simple operations? Just implement them." ([Test-Driven Development By Example](https://www2.cs.uh.edu/~rsingh/documents/software_design/TDD.pdf)).

**SOURCE CLAIM (Rank 2, Beck, TDD By Example, 2002)** — "Use Obvious Implementation— Type in the real implementation." ([Test-Driven Development By Example](https://www2.cs.uh.edu/~rsingh/documents/software_design/TDD.pdf)).

**SOURCE CLAIM (Rank 2, Beck, TDD By Example, 2002)** — Strategy selection is a flat decision rule: "Methodology. If you know what to type, type the Obvious Implementation. If you don't know what to type, then Fake It. If the right design still isn't clear, then Triangulate." ([Test-Driven Development By Example](https://www2.cs.uh.edu/~rsingh/documents/software_design/TDD.pdf)).

**SOURCE CLAIM (Rank 2, Beck, TDD By Example, 2002)** — Shifting between modes in practice: "When I use TDD in practice, I commonly shift between these two modes of implementation. ... As soon as I get an unexpected red bar, I back up, shift to faking implementations, and refactor to the right code." ([Test-Driven Development By Example](https://www2.cs.uh.edu/~rsingh/documents/software_design/TDD.pdf)).

**SOURCE CLAIM (Rank 2, Beck, TDD By Example, 2002)** — Obvious Implementation carries risk: "However, by using only Obvious Implementation, you are demanding perfection of yourself. ... Keep track of how often you are surprised by red bars using Obvious Implementation." ([Test-Driven Development By Example](https://www2.cs.uh.edu/~rsingh/documents/software_design/TDD.pdf)).

**SOURCE CLAIM (Rank 2, Beck, TDD By Example, 2002)** — Step-size control by speed: "You want to maintain that red/green/refactor rhythm. Obvious Implementation is second gear. Be prepared to downshift if your brain starts writing checks your fingers can't cash." ([Test-Driven Development By Example](https://www2.cs.uh.edu/~rsingh/documents/software_design/TDD.pdf)).

**SOURCE CLAIM (Rank 2, Beck, "Canon TDD", 2023)** — The canon also warns against abstracting too soon: "Mistake: abstracting too soon. Duplication is a hint, not a command." ([Canon TDD](https://tidyfirst.substack.com/p/canon-tdd)).

**AI INFERENCE**: "Fake it till you make it" and TPP are complementary, not identical. Fake It is a *green-phase tactic*: produce a constant, then let later tests and refactoring remove the duplication. TPP is an *ordering/selection heuristic*: prefer tests and changes whose behavior-change is higher on a complexity list. Fake It is the concrete mechanism that often realizes a high-priority TPP transformation (constant→scalar), while TPP guides which test to pose so that Fake It remains possible.

**AI INFERENCE**: The three strategies form a spectrum of step size: Fake It and Triangulate are the "teensy-weensy tiny steps", Obvious Implementation is "second gear". Beck's guidance ties step size to confidence and to surprises (unexpected red bars), which makes step-size a dynamic, per-test decision rather than a fixed process parameter.

## 6. Triangulation

**SOURCE CLAIM (Rank 2, Beck, TDD By Example, 2002, "Triangulate", Ch. 28)** — "How do you most conservatively drive abstraction with tests? Abstract only when you have two or more examples." ([Test-Driven Development By Example](https://www2.cs.uh.edu/~rsingh/documents/software_design/TDD.pdf)).

**SOURCE CLAIM (Rank 2, Beck, TDD By Example, 2002, Ch. 3)** — Definition and the deliberate deferral of generalization: "By analogy, when we triangulate, we only generalize code when we have two examples or more. We briefly ignore the duplication between test and model code. When the second example demands a more general solution, then and only then do we generalize." ([Test-Driven Development By Example](https://www2.cs.uh.edu/~rsingh/documents/software_design/TDD.pdf)).

**SOURCE CLAIM (Rank 2, Beck, TDD By Example, 2002, "Triangulate", Ch. 28)** — The plus() illustration: a single `assertEquals(4, plus(3, 1))` permits `return 4;`, and a second assertion forces the general `return augend + addend;`: "When we have the second example, we can abstract the implementation of plus ()." ([Test-Driven Development By Example](https://www2.cs.uh.edu/~rsingh/documents/software_design/TDD.pdf)).

**SOURCE CLAIM (Rank 2, Beck, TDD By Example, 2002, "Triangulate", Ch. 28)** — Triangulation's self-limiting rule: "Although they seem simple, the rules for Triangulation create an infinite loop. Once we have the two assertions and we have abstracted the correct implementation for plus, we can delete one of the assertions on the grounds that it is completely redundant with the other. If we do that, however, we can simplify the implementation of plus() to return just a constant, which requires us to add an assertion." ([Test-Driven Development By Example](https://www2.cs.uh.edu/~rsingh/documents/software_design/TDD.pdf)).

**SOURCE CLAIM (Rank 2, Beck, TDD By Example, 2002)** — Beck's preference is to use it sparingly: "Triangulation feels funny to me. I use it only when I am completely unsure of how to refactor." ([Test-Driven Development By Example](https://www2.cs.uh.edu/~rsingh/documents/software_design/TDD.pdf)) and "I only use Triangulation when I'm really, really unsure about the correct abstraction for the calculation. Otherwise I rely on either Obvious Implementation or Fake It." ([Test-Driven Development By Example](https://www2.cs.uh.edu/~rsingh/documents/software_design/TDD.pdf)).

**SOURCE CLAIM (Rank 2, Beck, TDD By Example, 2002)** — What triangulation is good for: "However, when the design thoughts just aren't coming, Triangulation provides a chance to think about the problem from a slightly different direction. What axes of variability are you trying to support in your design?" ([Test-Driven Development By Example](https://www2.cs.uh.edu/~rsingh/documents/software_design/TDD.pdf)).

**SOURCE CLAIM (Rank 5, Beck 2004 mailing-list, as redistributed)** — Beck's own later reflection on the same technique: "I've tried Triangulation, but the steps don't seem valuable to me, so I quickly lose motivation." ([testdrivendevelopment group #22](https://groups.io/g/testdrivendevelopment/message/22)).

**AI INFERENCE**: Triangulation is the manual, test-count-driven way to reach generality: two differing examples make a constant unsatisfiable, forcing a general solution. In TPP terms (Section 7), the second example is what *forces* the constant→scalar (or scalar→array) transformation. Beck's reluctance to use it is consistent with his preference for removing duplication directly (Fake It + refactor), which reaches the same generality without the extra test.

## 7. The Transformation Priority Premise (TPP)

TPP was proposed by Robert C. Martin (Uncle Bob) as a refinement of the green phase and of test ordering. The primary source is his 2010/2013 blog article. A Wikipedia article summarizes it but is used here only as orientation (Rank 4).

**SOURCE CLAIM (Rank 2, Martin, "The Transformation Priority Premise")** — Core premise: "Refactorings are simple operations that change the structure of code without changing it's behavior. Transformations are simple operations that change the behavior of code. ... Transformations have a priority, or a preferred ordering, which if maintained, by the ordering of the tests, will prevent impasses, or long outages in the red/green/refactor cycle." ([The Transformation Priority Premise](https://blog.cleancoder.com/uncle-bob/2013/05/27/TheTransformationPriorityPremise.html)) [sic: source reads "it's behavior"].

**SOURCE CLAIM (Rank 2, Martin)** — The direction of a transformation is specific→generic: "Rather, the code goes through a sequence of transformation from specific to generic." ([The Transformation Priority Premise](https://blog.cleancoder.com/uncle-bob/2013/05/27/TheTransformationPriorityPremise.html)).

**SOURCE CLAIM (Rank 2, Martin)** — The premise in one sentence: "It is better (or simpler) to change a constant into a variable than it is to add an if statement. So when making a test pass, you try to do so with transformations that are simpler (higher on the list) than those that are more complex." ([The Transformation Priority Premise](https://blog.cleancoder.com/uncle-bob/2013/05/27/TheTransformationPriorityPremise.html)).

**SOURCE CLAIM (Rank 2, Martin)** — Test selection is also constrained by TPP: "when you pose a test, you try to pose one that allows simpler transformations rather than complex transformations; since the more complexity required by the test the larger the risk you take to get that test to pass." ([The Transformation Priority Premise](https://blog.cleancoder.com/uncle-bob/2013/05/27/TheTransformationPriorityPremise.html)).

**SOURCE CLAIM (Rank 2, Martin)** — The impasse problem TPP addresses: "There is one sequence of tests and implementation choices that forces you into an impasse, where there is no way to get the next text to pass without rewriting the whole algorithm." ([The Transformation Priority Premise](https://blog.cleancoder.com/uncle-bob/2013/05/27/TheTransformationPriorityPremise.html)) [sic: source reads "next text"].

**SOURCE CLAIM (Rank 2, Martin)** — The amendment to red-green-refactor: "When passing a test, prefer higher priority transformations. / When posing a test choose one that can be passed with higher priority transformations. / When an implementation seems to require a low priority transformation, backtrack to see if there is a simpler test to pass." ([The Transformation Priority Premise](https://blog.cleancoder.com/uncle-bob/2013/05/27/TheTransformationPriorityPremise.html)).

**SOURCE CLAIM (Rank 2, Martin)** — The transformation list as proposed (order = decreasing priority): "({}–>nil) no code at all->code that employs nil / (nil->constant) / (constant->constant+) a simple constant to a more complex constant / (constant->scalar) replacing a constant with a variable or an argument / (statement->statements) adding more unconditional statements. / (unconditional->if) splitting the execution path / (scalar->array) / (array->container) / (statement->recursion) / (if->while) / (expression->function) replacing an expression with a function or algorithm / (variable->assignment) replacing the value of a variable." ([The Transformation Priority Premise](https://blog.cleancoder.com/uncle-bob/2013/05/27/TheTransformationPriorityPremise.html)).

**SOURCE CLAIM (Rank 2, Martin)** — The ordering is explicitly rough and self-questioned: "It should also be clear that I have *roughly* ordered the transformations by their complexity." ([The Transformation Priority Premise](https://blog.cleancoder.com/uncle-bob/2013/05/27/TheTransformationPriorityPremise.html)); and the author lists open problems: "Are there other transformations? (almost certainly) ... Is the priority order presented in this blog correct? (not likely)" ([The Transformation Priority Premise](https://blog.cleancoder.com/uncle-bob/2013/05/27/TheTransformationPriorityPremise.html)).

**SOURCE CLAIM (Rank 2, Martin)** — The list is claimed to be language-dependent: the Wikipedia summary quotes Martin — "I think that the priority list is language specific..." ([Transformation Priority Premise, Wikipedia](https://en.wikipedia.org/wiki/Transformation_Priority_Premise)) [Rank 4: this quotation is reached through Wikipedia; the same open-problems framing is directly in the primary blog, but this specific sentence was not located in the retrieved primary text, so it is recorded as a Rank 4 secondary claim].

**SOURCE CLAIM (Rank 4, Wikipedia)** — Orientation only: "Transformation Priority Premise (TPP) is a programming approach developed by Robert C. Martin (Uncle Bob) as a refinement to make the process of test-driven development (TDD) easier and more effective for a computer programmer." ([Transformation Priority Premise, Wikipedia](https://en.wikipedia.org/wiki/Transformation_Priority_Premise)).

**AI INFERENCE**: TPP and triangulation solve the same milli-cycle question — "which test next, and by what change do I pass it?" — from opposite directions. Triangulation forces generality by adding a second example that contradicts a constant. TPP chooses the next example precisely so that the required behavior change stays high on the priority list, and it also constrains the *implementation* move. They are compatible: a test pair used for triangulation is exactly the kind of test order TPP would endorse if the resulting transformation (constant→scalar) is high-priority, and TPP warns against test orders whose only exit is a low-priority transformation such as expression→function.

**AI INFERENCE**: TPP's own author labels the ordering informal and possibly incorrect, and lists multiple unresolved problems. Therefore TPP is best treated as a heuristic for reducing impasses, not as a proven algorithm; its evidential status is an author's proposal plus peer discussion, not an experimentally established result. No control study testing impasse reduction was located.

## 8. Baby steps and step size

**SOURCE CLAIM (Rank 2, Beck, TDD By Example, 2002, Ch. 32 "How large should your steps be?")** — "The tendency of Test-Driven Developers over time is clear, though—smaller steps." ([Test-Driven Development By Example](https://www2.cs.uh.edu/~rsingh/documents/software_design/TDD.pdf)).

**SOURCE CLAIM (Rank 2, Beck, TDD By Example, 2002)** — Step size is a choice the developer can make either way: "Part of the answer is that you should be able to do either." ([Test-Driven Development By Example](https://www2.cs.uh.edu/~rsingh/documents/software_design/TDD.pdf)).

**SOURCE CLAIM (Rank 2, Beck, TDD By Example, 2002, Ch. 27 "Baby Steps")** — "If a test method is getting long and complicated, then you need to play 'Baby Steps.' The goal of the game is to write the smallest test method that represents real progress toward your end goal." ([Test-Driven Development By Example](https://www2.cs.uh.edu/~rsingh/documents/software_design/TDD.pdf)).

**SOURCE CLAIM (Rank 2, Beck, TDD By Example, 2002)** — Small steps are also prescribed for refactoring: "At first when you refactor, you should be prepared to take lots of little tiny steps." ([Test-Driven Development By Example](https://www2.cs.uh.edu/~rsingh/documents/software_design/TDD.pdf)).

**SOURCE CLAIM (Rank 2, Beck, "Canon TDD", 2023)** — The stopping/compaction signal: "Keep testing & coding until your fear for the behavior of the code has been transmuted into boredom." ([Canon TDD](https://tidyfirst.substack.com/p/canon-tdd)).

**SOURCE CLAIM (Rank 2, Beck, TDD By Example, 2002, Ch. 32)** — "Write tests until fear is transformed into boredom." ([Test-Driven Development By Example](https://www2.cs.uh.edu/~rsingh/documents/software_design/TDD.pdf)).

**AI INFERENCE**: "Baby steps" is the scale-control principle that spans every cycle: it is the nano-cycle's line-at-a-time granularity, the micro-cycle's minimal green change, the milli-cycle's One Step Test, and the refactoring rule of tiny transformations. Step size is the single control knob that the practitioner adjusts; Beck ties its use to confidence and to surprises rather than to a fixed threshold.

## Synthesis (answer to the core question)

All statements in this section are **AI INFERENCE** built from the quoted evidence above; the quotations themselves are in the labelled sections.

**The cycle structure.** TDD is one loop observed at four nested scales (Martin). From inner to outer: the **nano-cycle** (seconds) is the Three Laws — write only enough failing test to fail, then only enough code to pass. The **micro-cycle** (minutes, once per unit test) is Red-Green-Refactor, or equivalently "Write a test / Make it run / Make it right": make it work, then make it clean, never both at once. The **milli-cycle** (~10 minutes) is Specific/Generic: as the test suite becomes a more specific specification, the production code must become more general; this is where TPP and triangulation operate, and where the test list guides ordering. The **primary cycle** (hourly) is architectural: stop, look for boundaries, decide which side of them the current work belongs to, and feed that back into the inner cycles. Surrounding the micro-cycle is the **initial test list** — behavioral cases and planned refactorings — from which exactly one item is turned into a runnable test at a time.

**The Three Laws.** (1) No production code until a failing test exists. (2) No more test than is sufficient to fail; non-compilation counts as failing. (3) No more production code than is sufficient to pass the currently failing test. Together they enforce a cycle of roughly 30 seconds and force line-level granularity. Law 2's compile clause is what legitimizes starting a brand-new test before any type exists; law 3 is what prevents design work from leaking into the green phase, pushing it into refactor.

**How triangulation and TPP fit.** Both answer the milli-cycle question, "which test next and by what change do I pass it?" **Triangulation** is the conservative, test-count-driven route to generality: with one example a constant suffices; only a second, differing example forces the general solution — so generalize only at two or more examples. Beck uses it only when he cannot see the duplication to remove and is unsure of the target abstraction. **TPP** is Martin's refinement: behavior changes are "transformations" from specific to generic, ordered by complexity (nil→constant, constant→scalar, …, unconditional→if, …, expression→function); prefer the highest-priority transformation when making a test pass, choose the next test so it can be passed by a high-priority transformation, and if only a low-priority move works, backtrack and pick a simpler test. It is explicitly a heuristic: its author lists unresolved problems and calls the order "rough" and "not likely" correct, so it should be treated as an impasse-avoidance heuristic rather than a proven algorithm.

**Fake It and Obvious Implementation** are green-phase tactics that sit alongside triangulation: Fake It returns a constant and removes the test/code duplication later by refactoring; Obvious Implementation types the real solution when confidence is high, downshifting to Fake It on unexpected red bars. **Baby steps** is the cross-cutting scale principle: keep each step small and let confidence, not a fixed threshold, decide when to enlarge it.

## Retrieval log

| URL | Result |
|-----|--------|
| https://blog.cleancoder.com/uncle-bob/2014/12/17/TheCyclesOfTDD.html | Retrieved (direct fetch); primary source for nested cycles |
| https://martinfowler.com/bliki/TestDrivenDevelopment.html | Retrieved (direct fetch); page dated 11 December 2023, original 2005-03-05 |
| http://programmer.97things.oreilly.com/wiki/index.php/The_Three_Laws_of_Test-Driven_Development | **Failed** — live URL redirects to the O'Reilly marketing home page; the original article is no longer served |
| https://web.archive.org/web/20160309220415/http://programmer.97things.oreilly.com/wiki/index.php/The_Three_Laws_of_Test-Driven_Development | Retrieved (direct fetch); Internet Archive capture dated 8 October 2009; used for the Three Laws |
| https://blog.cleancoder.com/uncle-bob/2013/05/27/TheTransformationPriorityPremise.html | Retrieved (direct fetch); primary source for TPP |
| https://tidyfirst.substack.com/p/canon-tdd | Retrieved (direct fetch); Beck's canonical 5-step workflow, 11 December 2023 |
| https://newsletter.kentbeck.com/p/canon-tdd | Retrieved only as a search-index excerpt (not directly fetched); mirror of the same post |
| https://www2.cs.uh.edu/~rsingh/documents/software_design/TDD.pdf | Direct `webfetch` **Failed** ("Unsupported fetched file content type: application/pdf"); **Retrieved** by `curl` download plus local OCR/text extraction of the Beck book |
| https://archive.org/download/est-driven-development-by-example/test-driven-development-by-example_djvu.txt | Retrieved (direct download); second OCR rendering of the same book used to cross-check quotations |
| https://en.wikipedia.org/wiki/Transformation_Priority_Premise | Retrieved only as search-index excerpt (not directly fetched); Rank 4 orientation and one secondary quotation |
| https://groups.io/g/testdrivendevelopment/message/22 | Retrieved only as search-index excerpt (not directly fetched); Rank 5 forum post attributed to Kent Beck |
| https://www.pearson.com/.../test-driven-development-by-example/... | Retrieved only as search-index excerpt; used for edition/ISBN metadata only |
| https://www.informit.com/store/test-driven-development-by-example-9780321146533 | Retrieved only as search-index excerpt; used for edition/ISBN metadata only |
| https://search.worldcat.org/title/50479239 | Retrieved only as search-index excerpt; used for edition/ISBN metadata only |
| https://www.oreilly.com/library/view/test-driven-development/0321146530/ch26.xhtml (One Step Test) | Retrieved only as search-index excerpt; corroborating page, primary text taken from book OCR |
| https://xunit.net/docs/tdd-example | Retrieved only as search-index excerpt; Rank 2 official-project corroboration of keeping a behavior list, not used as a quotation source |

Method note: the Beck book was inspected as an OCR transcript of a scanned copy, not from the printed page. OCR substitutions were corrected only in the quotations reproduced here, and clear artifacts are marked `[sic]` or avoided. The edition is the 1st edition (2002/2003, ISBN 0-321-14653-0).

## Open questions

- **Which edition/printing was OCR'd?** The scanned archive item gives publication date 2002-11-08 and ISBN 0-321-14653-0, and the copyright page in the second OCR rendering shows "Second printing, April 2003". Whether any wording differs from the 2022 reissue (ISBN 9780137585236) is **UNKNOWN**; only the 2002/2003 edition was inspected.
- **Is TPP the same list in every language?** Martin is quoted (via Wikipedia, Rank 4) as saying the priority list is language-specific, but this sentence was not located in the retrieved primary blog text. The primary blog does say the order is "rough". **UNKNOWN / needs primary confirmation.**
- **Does TPP actually reduce impasses in practice?** No controlled or empirical evidence was retrieved; the claim is the author's premise. **PLAUSIBLE, NOT VERIFIED.**
- **Is triangulation still recommended?** Beck's book uses it sparingly and his 2004 forum statement says the steps don't seem valuable to him. Whether he currently recommends it at all is **UNKNOWN** from the retrieved sources.
- **Are there authoritative later revisions to the Three Laws?** The canonical text inspected is the 2009 wiki article; Daniel Terhorst-North and others have reworded the laws (the "Three Laws" are widely re-stated), but no such revision was inspected here. **UNKNOWN.**
- **Where exactly does the test list live in the cycle?** Beck's canon makes it step 1; Martin's nested-cycle article does not mention the test list explicitly, and the book's "Test List" pattern treats it as part of the red-bar patterns rather than a named cycle. Reconciliation between these framings is **UNKNOWN** and is a candidate for cross-topic reconciliation.

