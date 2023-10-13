# Introduction

Please read the general [introduction to the babysteps timer kata](../README.md) first!

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

These updates have now been merged into the original GitHub repository!