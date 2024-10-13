# Introduction

Please read the general [introduction to the gilded rose kata](../README.md) first!

# Getting started

First, create an initial Javascript kata set-up as described [here](https://github.com/zhendrikse/tdd/tree/master/cookiecutter).

Next, go the newly created project directory and consult
the provided ``README.md`` in there.

## Copying the required files

Copy the contents of the ``gilded_rose.js`` file over to the generated 
source file in the ``src`` folder. Depending on how you named your kata,
this should be something similar as

```shell
$ cat gilded_rose.js > gilded_rose_kata/src/gilded_rose_kata.js
```

Do the same with the spec file

```shell
$ cat gilded_rose_spec.js > gilded_rose_kata/spec/gilded_rose_kata_spec.js
```

#### IMPORTANT

Inspect the third line of your spec file. The import/require statement 
on line three should match the file name that is in the ``src`` 
directory. Make  sure this file name and the import/require 
statement are properly aligned!

Next, enter your generated kata directory and install the approvals test 
library

```shell
$ npm install approvals --save-dev
```

Finally, you should be able to start working by invoking

```shell
npm run test
```

# Improving the coverage

## Inspecting the code coverage

Let's see what the current coverage is by running

```bash
$ npm run report
```

A web window should now open, displaying the code coverage. 
You can click on the `gilded_rose.js` file in the table.

## Getting acquainted with approval testing

Looking at the coverage report, we see that quite a lot of code is still left uncovered. Let's first improve this.


