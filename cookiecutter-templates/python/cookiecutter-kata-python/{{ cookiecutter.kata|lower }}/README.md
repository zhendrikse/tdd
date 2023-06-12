# {{ cookiecutter.kata }} Code Kata

Welcome to your new Code Kata.  Test-driven C++ is a lot of fun, and a
great form of "deliberate practice".  You're almost there - there's
one more step needed to get up and running.

## Generating the build

You've used a cookiecutter to generate this project, but there's
another step to get started - this project is based on CMake, so you
need to use this CMake build to generate a build that will work on
your system.

This build structure can be done "out of tree" (ie not in this folder
structure), or use the .build/ folder that's automatically created -
this is also in the .gitignore by default, if you want

A typical CMake invocation (for Clang and C++14) would be:

```
$ cd .build
$ cmake -DCMAKE_CXX_COMPILER=clang++ -DCMAKE_BUILD_TYPE=Debug
  -DCMAKE_CXX_FLAGS="-std=c++14"
  -DCMAKE_CXX_FLAGS_DEBUG="-fstandalone-debug -ggdb -O0" ..
```

Then run the makefile as (for example):

```
$ make -j8 unit
```

## The TDD cycle

TDD gives you a very fast feedback cycle, and helps you evolve a
solution incrementally, in very small steps.  TDD gives you feedback
on your design and lets you make many, small improvements to your
code. You can do this with confidence because the tests will catch any
accidental regression as you apply these refactorings.

TDD uses a cycle of three phases, always starting with RED : a
failing test, or failing compilation.

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

## The Four Rules of Simple Design

When you're doing a kata, try to stick to the "four rules" as
described first by Kent Beck:

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
