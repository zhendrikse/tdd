# There is more to TDD than “red, green, refactor”

Although most people have heard of the slogan "red, green, refactor", 
this is only a small part of what defines TDD. From its inception, 
TDD and eXtreme Programing have always been 
[closely linked](https://www.thoughtworks.com/en-sg/insights/blog/testing/xp-tdd). 

TDD is best understood as a set of 
[skills and heuristics](https://www.qwan.eu/blog-by-tag#tag-test-driven-development) 
that enable you to ensure that every line of the code base contributes to the expected 
behavior while clearly expressing its intent.

But how do these skills and heuristics then relate to the familiar red-green-refactor 
slogan that is almost always the first response when people are asked to explain TDD? 
The short answer is that the aforementioned skills and heuristics are constantly 
being applied as the red-green-refactor loop is traversed.

For example, consider the following skills, heuristics, and principles (to name just a few):

- Start a test by [writing the assertion first](https://www.qwan.eu/2021/07/05/tdd-start-with-expectation.html) → heuristic for the “red” step.
- The DRY principle (don’t repeat yourself) → principle while refactoring.
- Refactoring in (extremely) small steps → profound skill in the “refactor” step.
- [Faking and cheating](https://www.qwan.eu/2021/07/20/tdd-faking-cheating.html) → heuristic to make a test pass, i.e. the “green” step.
- [0, 1, N](https://www.qwan.eu/2021/07/09/tdd-0-1-n.html) → heuristic to generalize production code.

But how on earth are all these skills, principles, and heuristics then connected and 
practically applied when practicing TDD, you may wonder. 

To illustrate this connection, consider the diagram below. 
As you go through the regular red, green, and refactor phases of TDD, 
you'll notice that there are many heuristics, skills, and principles 
that are constantly applied. This is done very consciously at first but 
gradually becomes more ingrained in your way of working as you become more 
fluent in practicing TDD.

![Heuristics](https://github.com/zhendrikse/tdd/raw/master/assets/heuristics.png)

It is exactly this combination of countless skills and heuristics that increases the 
quality of your code so significantly (as we are effectively building quality in) 
and hence boosts your confidence to such an extent that you are able to 
promote your changes to production whenever needed.
Perhaps the best and most fun way to practice all of these skills is by 
participating in so-called [coding katas](https://github.com/zhendrikse/tdd/wiki/Coding-Katas).

Last but not least, TDD is a lot of fun. This repository contains more than enough
materials to learn everything about TDD and get up and running
in the wink of an eye!

## Kent Beck's four rules of simple design

![Kent Beck](https://www.hendrikse.name/tdd/assets/kent_beck.png)
_One of the founding fathers of test-driven development: [Kent Beck](https://en.wikipedia.org/wiki/Kent_Beck)._

Kent Beck introduced the [four design rules](https://martinfowler.com/bliki/BeckDesignRules.html).
After making a test pass, he (strictly) applies the [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) 
and the [reveal intent, hide implementation](https://dev.to/codingunicorn/reveal-intent-hide-implementation-42lc) 
principles.

Last but not least, he also (again strictly) applies the simplest thing that could possibly work,
which is also often referred to as the "fewest elements". 
This may actually be one of the trickiest practices to apply properly, as you will see.

![Design rules](https://github.com/zhendrikse/tdd/blob/master/assets/design_rules.png)

_Kent Beck's four design rules are in ascending order of priority: make the test pass, make the code so readable that it immediately reveals its intention, do not allow any code duplication, and always code the simplest thing that could possibly work &mdash; [Kent Beck](https://en.wikipedia.org/wiki/Kent_Beck)_

One of the best examples to show the principle that code should express intent is probably 
a code snippet from one of the possible solutions to the
[game of life kata](https://github.com/zhendrikse/tdd/blob/master/tdd-katas/game-of-life/game-of-life-java/README.md) (in Java). 

```java
public static List<Cell> iterateGameboard(final List<Cell> gameboard) {
  return gameboard
      .stream()
        .map(toDeadCell(which(isLiving, and(), 
            which(hasLessThanTwo(livingNeighboursIn(gameboard)), or(), hasMoreThanThree(livingNeighboursIn(gameboard))))))
        .map(toLivingCell(which(isDead, and(), hasExactlyThree(livingNeighboursIn(gameboard)))))
        .collect(Collectors.toList());
}
```

It immediately becomes clear why this principle is so important and 
at the same time, it explains why comments in code are 
generally speaking redundant.

## Uncle Bob's cycles of TDD

![Uncle Bob](https://github.com/zhendrikse/tdd/blob/master/assets/uncle-bob.png)

Doing TDD means you iteratively repeat the following three steps in _extremely small_ increments.
This has been captured in what has become best known as
[Uncle Bob's cycles of TDD](https://blog.cleancoder.com/uncle-bob/2014/12/17/TheCyclesOfTDD.html):

1. First we write a _failing_ test. It is important to make the test fail first, 
   as this assures us the test actually works! We are allowed to write just so much 
   test code, that makes the test fail. This includes compilation errors!
2. Next we implement _just enough_ production code to make the test pass.
3. We ask ourselves if there is anything that we can refactor, 
   by applying e.g. the [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) principle.

These rules make you switch constantly between the test and production 
code bases, gradually making the test set more _specific_ and the 
production code more _generic_. This is also known as 
[test contra-variance](https://blog.cleancoder.com/uncle-bob/2017/10/03/TestContravariance.html).

By constantly going back and forth between the production and test code, 
you constantly try to write tests that force the code that is based
on the-simplest-thing-that-could-possibly-work more generic. 
Conversely, in the production code, you try to "trick" the test(s)
by implementing just the bare minimum to make them pass.

To summarize, we continuously ping back and forth between our production code 
and our specifications (test code). We do this in the _smallest increments_ 
that we can possibly think of. We may want to keep ourselves in check by requiring 100% 
code coverage at all times. If we get below 100%, apparently we "managed" to write code 
before we had a test for it. Remember that this spoils the whole idea of TDD!

# References

## TDD Heuristics
- [What is a heuristic](https://www.qwan.eu/2021/10/13/what-is-a-heuristic.html) 
- [Think about design in the test](https://www.qwan.eu/2021/06/28/tdd-think-about-design-in-test.html)
- [Wishful thinking](https://www.qwan.eu/2021/07/01/tdd-wishful-thinking.html)
- [Start with expectation](https://www.qwan.eu/2021/07/05/tdd-start-with-expectation.html)
- [0, 1, N](https://www.qwan.eu/2021/07/09/tdd-0-1-n.html)
- [Act dumb in implementation](https://www.qwan.eu/2021/07/12/tdd-act-dumb-in-implementation.html)
- [Faking & Cheating](https://www.qwan.eu/2021/07/20/tdd-faking-cheating.html)
- [Test name describes the action and the expected result](https://www.qwan.eu/2021/07/27/tdd-naming-tests.html)
- [Given-When-Then or Arrange-Act-Assert](https://www.qwan.eu/2021/09/02/tdd-given-when-then.html)
- [One (conceptual) assert per test](https://www.qwan.eu/2021/08/27/tdd-one-assert-per-test.html)
- [Glanceable tests](https://www.qwan.eu/2021/09/27/tdd-glanceable-tests.html)

## Code smells and refactoring
- [Catalog of refactorings](https://refactoring.com/catalog/) by Martin Fowler
- [Refactoring Guru](https://refactoring.guru/) makes it easy for you to discover everything you need to know about refactoring, design patterns, SOLID principles, and other smart programming topics
- [Branching by abstraction](https://www.martinfowler.com/bliki/BranchByAbstraction.html)
