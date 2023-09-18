# Babysteps timer

This kata contains a working babysteps timer. It can actually be used 
[as a constraint](https://kata-log.rocks/baby-steps) when practicing TDD! 

The idea is that writing a failing test and making
it green, should be possible within 2 minutes. If not, all changes should
be reverted (.e.g. `git reset --hard`). The same holds for the refactoring phase.

Note that the babysteps timer can (should?) even be used during its own refactoring 😄

## Starting the babysteps timer

The timer can be started like so:

```bash
$ npm install
$ npm run test
$ npm run compile
$ npm run serve
``` 

## Goal of the babysteps timer kata

The constraint is to write tests for the babysteps timer before refactoring
the Typescript code. A first example test has already been provided to get
you started, but feel free to throw that (somewhat) useless test away!

Tip: you may want to run tests continuously by using:

```bash
$npm run watch
```

## References

I first read about this kata in [5 coding exercises to practice refactoring Legacy Code](https://understandlegacycode.com/blog/5-coding-exercises-to-practice-refactoring-legacy-code/).

The original code was taken from the 
[Babysteps timer](https://github.com/dtanzer/babystepstimer) 
repository with some modifcations and updates such as

- Updates of all the npm packages.
- Removed deprecated `mocha.opts` file
- Updates (using modules) of the `package.json` and `tsconfig.json` to make tests possible
- Minor update of `babysteps.ts` to latest node (timer) types.
- Changed the way the Javascript is included as a module from within the HTML file using
  [these tips](https://stackoverflow.com/questions/69888029/how-to-call-a-function-declared-in-a-javascript-module-type-module-from-an-htm).

 ### Related materials

  - [Baby Steps Push Challenge](http://blog.code-cop.org/2021/09/baby-steps-push-challenge.html)
  - [Tic tac toe in babysteps](https://github.com/ttsui/scsyd-taking-baby-steps-kata#readme)
  - [Babysteps in TDD](https://medium.com/@heaton.cai/baby-steps-in-tdd-7761ad362e34)
  - [Workshop taking babysteps](https://blog.adrianbolboaca.ro/2013/03/taking-baby-steps/)