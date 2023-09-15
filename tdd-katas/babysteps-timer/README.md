# Babysteps timer kata

This kata contains a working babysteps timer. It can actually be used 
when practicing TDD! 

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

Tip: you want to run tests continuously by using:

```bash
$npm run watch
```

## References

The original code was taken from the 
[Babysteps timer](https://github.com/dtanzer/babystepstimer) 
repository with some modifcations and updates such as

- Updates of all the npm packages
- Updates of the `package.json` and `tsconfig.json` to make tests possible
- Minor update of `babysteps.ts` to latest node (timer) types 