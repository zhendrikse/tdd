# Introduction

Please read the general [introduction to the countries kata](../README.md) first!

# Getting started

Carry out the following steps in order:

1. Create an intial Python kata set-up as described
   [here](https://github.com/zhendrikse/tdd/tree/master/cookiecutter).
   Choose 'n' when prompted for the rSpec syntax. The code coverage is optional.
2. Remove the `.py` files in the `src` and `test` directories, but leave the
   `__init__.py` files untouched!
4. Copy the `country.py` file into the `src` directory 
5. Copy the `countries_test.py` file into the `test` directory
6. Run the test and veriffy all assertions are still valid: 
   it is testing the real API after all, which may have changed!
   ```
   $ poetry install
   $ ./run_tests.sh
   ``` 

## Running the tests

```bash
$ ./run_tests.sh
```