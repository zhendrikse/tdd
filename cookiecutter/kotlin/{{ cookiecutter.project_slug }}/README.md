# {{ cookiecutter.kata }} Code Kata

Welcome to your new Code Kata.  Test-driven development is a lot of fun, and a
great form of "deliberate practice."  You're almost there - there's
one more step needed to get up and running.

## Running the tests

You can continuously run the test by using

```bash
$ gradle test --continuous
```

# Introduction TDD

TDD gives you a fast feedback cycle, and helps you evolve a
solution incrementally, in _tiny_ increments.  
TDD gives you feedback
on your design and lets you make many small improvements to your
code. You can do this with confidence because the tests will catch any
accidental regression as you apply these refactorings.

Doing TDD means you iteratively repeat the following three steps 

1. First, we write a _failing_ test. It is important to make the test fail first, as this assures us the test actually works! We are allowed to write just so much test code, that makes test fail. This includes compilation errors!
2. Next, we implement _just enough_ production code to make the test pass.
3. We ask ourselves if there is anything that we can refactor, by applying, e.g. the [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) principle.

```                                 
  +--------------------------------+
  | RED: write the smallest amount |
  | of code to make the test fail, +------------+
  | and treat compilation failures |            |
  | as a test failure.             |            |
  +--------------------------------+            |
         ^                                      |
         |                                      v
         |                +-------------------------------------+
         |                | GREEN: write the smallest amount of |
         |                | production code to pass the one     |
         |                | failing test.                       |
         |                +---------------------+---------------+
         |                                      |
         |                                      |
     +---+-----------------------------+        |
     | REFACTOR: clean up the code,    |        |
     | remove duplication, improve     |<-------+
     | names to better express intent. |
     +---------------------------------+
```

## Kent Beck's design rules

![Kent Beck](./assets/kent_beck.png)
**Figure 1**: _One of the founding fathers of test-driven development: [Kent Beck](https://en.wikipedia.org/wiki/Kent_Beck)._

Kent Beck introduced the [four design rules](https://martinfowler.com/bliki/BeckDesignRules.html). After making the test pass, he (strictly) applies the [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) and the [reveal intent, hide implementation](https://dev.to/codingunicorn/reveal-intent-hide-implementation-42lc) principles. Last but not least, he also (again strictly) applies the simplest thing that could possibly work. This may actually be one of the trickiest practices to apply properly, as you will see.

Summarizing, Kent Beck applies the following rules in descending order of priority:

- Passes the tests
- Reveals intention
- No duplication
- Fewest elements

These are described very well by Joe Rainsberger
[here](http://blog.jbrains.ca/permalink/the-four-elements-of-simple-design)
and
[here](http://blog.thecodewhisperer.com/permalink/putting-an-age-old-battle-to-rest/). Corey
Haines wrote an [excellent, small
book](https://leanpub.com/4rulesofsimpledesign) on the subject based
on his observations running the Game Of Life Kata over many code
retreats.

### Conclusion 

Summarizing, we continuously ping back and forth between our production code and our specifications (test code). We do this in the _smallest increments_ that we can possibly think of. We keep ourselves in check by requiring 100% code coverage at all times. If we get below 100%, apparently we "managed" to write code before we had a test for it. Remember that this spoils the whole idea of TDD!

## Resources

There's a great list of Code Kata exercises at
[codekata.com](http://codekata.com/). Emily Bache wrote and published
[a guide book](https://leanpub.com/codingdojohandbook) on code katas,
with guidance and ideas for running coding dojos.

Read the documentation on [Google
Mock](https://github.com/google/googletest/tree/master/googlemock/docs/v1_7)
and [Google
Test](https://github.com/google/googletest/tree/master/googletest/docs)
online.

## License(s)

The license for this kata can be found in the LICENSE.md file, - but
be advised that the Google Test library found in the lib folder has
its own license terms. Please read that license from Google relating
specifically to Google Test and Google Mock.
