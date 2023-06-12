# Introduction

Please read the general [introduction to the stack kata](../README.md) first!

# Getting started

First install [cookiecutter](https://www.cookiecutter.io/) by invoking

```bash
$ poetry install
```

Next, create an empty kata project to get yourself started

```bash
$ poetry run cookiecutter https://github.com/zhendrikse/cookiecutter-kata-javascript.git
```

Answer the questions mutatis mutandum like so

```
$ poetry run cookiecutter https://github.com/zhendrikse/cookiecutter-kata-python.git

kata [GameOfLife]: Stack
description [This kata practices TDD]: Stack kata to practice TDD
author [Your name]: Zeger Hendrikse
email [your@email.com]: zegerh@yahoo.co.uk
Select license:
1 - GNU General Public License v3
2 - MIT license
3 - Apache Software License 2.0
Choose from 1, 2, 3 [1]: 
```

Finally, go the the newly created project directory and make sure
the required dependencies are installed by invoking

```bash
$ npm install
```

The tests can be run as follows

```bash
$ npm run test
```

