# Sudoku solution in Clojure

The project uses [Midje](https://github.com/marick/Midje/).

## How to use midje


### Prerequisite
Add this to your `~/.lein/profiles.clj` file:

```bash
$ echo '{:user {:plugins [[lein-midje "3.2.1"]]}}' >> ~/.lein/profiles.clj
```

### Running the tests

`lein midje` will run all tests.

`lein midje namespace.*` will run only tests beginning with "namespace.".

`lein midje :autotest` will run all the tests indefinitely. It sets up a
watcher on the code files. If they change, only the relevant tests will be
run again.

## References

- [TDD Practice #1: The Sudoku Example in Clojure – The Feature Tests](https://www.linkedin.com/pulse/tdd-practice-1-sudoku-example-clojure-feature-tests-jorge-viana/)
- [TDD Practice #2: The Sudoku Example in Clojure – Starting the Unit Testing ](https://www.linkedin.com/pulse/tdd-practice-2-sudoku-example-clojure-starting-unit-testing-viana-/)