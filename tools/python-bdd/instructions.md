# Goal 

The goal of this module is to get acquainted with the (behaviour driven development, BDD) testing framework that we will be using in this curriculum. This framework promotes you to write (executable) specifications as opposed to tests that test implementation. 

### Before we move on

If you haven't done so already in the previous lesson, please watch the [Test Driven Development vs Behavior Driven Development](https://www.youtube.com/watch?v=Bq_oz7nCNUA) video by Dave Farley before continuing the remainder of this course.

![Dave Farley](./assets/dave_farley_tdd.png)

### Summary

As explained in the video, BDD helps you to 
- specify behaviour, and hence "forces" you to test for the correct behaviour of your systemtest as opposed to a correct implementation. This, in turn, makes your test suites/sets of specifications much less brittle. 
- to make your code _express intent_.
- to write your specifications (tests) in the same way, indepedent of the programming language used. This is because the [RSpec](https://rspec.info/)-syntax is so widely used.

## Practical work

Please follow and study the items below before continuing the remainder of this course:

1. First read the explanation on [RSpec](https://rspec.info/) below.
2. Run this repl and inspect the output. Do you understand what you see?
3. Inspect/study the `example_spec.py` file.
4. Optional: try to modify/extend the `example_spec.py` file.
5. Be sure to also check out the references section!
6. Assure yourself to remember this module, as it also serves as a reference when making the katas and exercises.
  
So let's start with the first item from our practical work list by briefly going over the [RSpec](https://rspec.info/) syntax. Thereafter you'll be able to quickly grasp the motivation as well as the syntax of Python's Mamba framework as well.

# Introducing the RSpec syntax

## Introduction

[RSpec](https://rspec.info/) is a domain-specific language written in Ruby and specifically designed for writing test as specifications, or, specifications as tests if you will. It is used for testing ruby applications. It syntax caught on widely though, and for almost all
programming languages equivalent frameworks/libraries have become
avaible. 

[Mamba](https://mamba-bdd.readthedocs.io/en/latest/) offers us such an RSpec equivalent for Python. We will use Mamba in the remainder of this course.

Files with tests are preferrably referred to as _specifications_. These so-called spec files in turn contain one or more scenarios. Actually, they almost always contain more than one scenario.

## Important keywords

### The keyword `describe`
  
The describe keyword is used to bundle a group of tests together, e.g. for grouping all scenarios pertaining to one of the CRUD (create/read/update/delete) operations.

In [RSpec](https://rspec.info/) these tests are rather referred to as examples.

Descriptions can be nested. A description can either contain a string argument or a class:

```python
with description(TaskList):
  ...

with description("A new task list"):
  ...
```

### The keyword  `context`
Each `context` establishes the state of the world before executing the method. It basically represents the "given" from the "[given/when/then](https://martinfowler.com/bliki/GivenWhenThen.html)" or the "arrange" from the "[arrange/act/assert](http://wiki.c2.com/?ArrangeActAssert)":

```python
with description("Create task"):
  with context("with valid credentials"):
    ...

  with context("with invalid credentials"):
    ...
```

### The keyword `it`
With the `it` clause we specify the behaviour:

```python
with description("Create task"):
  with context("with valid credentials"):
    with it("creates the task"):
      ...

  with context("with invalid credentials"):
    with it("throws a authentication failed exception"):
    ...
```

### The keyword `expect`

Once the context is set up for examination, we can verify our expectations using so-called matchers.

There are dozens of matchers that help you to express _the intent_ of your code/expectations. A few of the ones that we are going to need the most are discussed in the next section!


# Introducing Mamba!
When practising TDD, you basically make a mind switch from writing tests to writing (executable) specifications. In other words, we [specify the behaviour](https://www.youtube.com/watch?v=Bq_oz7nCNUA) that we would like our system to exhibit. An [RSpec](https://rspec.info/)-like syntax helps (forces?) us to do so. 

## Writing our tests... uhm, I mean specifications!
[Mamba](https://mamba-bdd.readthedocs.io/en/latest/) offers us an RSpec equivalent for Python:

```python
with description("A specification") as self:
  with context("within a certain context"):
    with it("asserts that True is True"):
      expect(True).to(be_true)
```

Mamba is often used together with the [expects framework]((https://expects.readthedocs.io/en/stable/matchers.html#)), but certainly is _not_ limited to it. For example, it is equally valid to use frameworks such as [doublex](https://pypi.org/project/doublex/), [Hamcrest](https://github.com/hamcrest/PyHamcrest), and many others.

In this course, we will mainly use the matchers from the expects framework:
- `equal` for asserting values:
  ```python 
  expect(0).to(equal(False))
  ``` 
- `be` 
  ```python 
  expect(True).to(be_true)
  expect(False).to(be_false)
  ``` 
- `be_empty`, `have_length`, `contain`, for asserting lists (with Dutch words 😉):
  ```python
  expect(["aap", "noot", "mies"]).to(have_length(3))
  expect([]).to(be_empty)
  expect(["aap", "noot", "mies"]).to(contain("noot"))
  expect(["noot"]).to(contain_only("noot"))
  ```
- `be_a` for checking class instances:
  ```python
  expect(ASampleClass()).to(be_a(ASampleClass))
  ```
- `equal` can be used as well, but `be` is generally preferred as it is better at expressing _intent_:
  ```python
  expect(3 + 4).to(equal(7))
  expect(1).to(be(1)) 
  ```
- `raise_error` to check for exceptions:
  ```python
  expect(lambda: sample_class.method_throws_error()).to(raise_error(ValueError, "Illegal value"))
  ```
  Note that we have to apply the keyword `lambda` when writing specifications for exceptions, as the code/function following
  the lambda expression needs to generate the exception that is
  then verified to be of the right type.

## Mamba tips & tricks

When developing, you sometimes just want to run one test, temporarily excluding all the others. To this extent, Mamba offers so-called [focussed examples](https://mamba-bdd.readthedocs.io/en/latest/filtering.html). You can try this out by replacing e.g. one or more of the `it()` or `description()` statements by `fit()` and `fdescription()`, running the examples once more and observe what happens.

You can also do the opposite, just excluding a single assertion or description by prepending an underscore: `_it()` or `_description()`. Try it out as well and see what happens!

Although it is strictly speaking not needed for the remainder of this course, it is strongly recommended to get yourself inspired by browsing through some [Mamba examples](https://github.com/jaimegildesagredo/mamba) and [Python describe Examples
](https://python.hotexamples.com/examples/mamba/-/describe/python-describe-function-examples.html).

## References

- [RSpec best practices](https://www.methodsandtools.com/tools/rspecbestpractices.php), recommended!
- [Mamba examples](https://github.com/jaimegildesagredo/mamba) and [Python describe Examples
](https://python.hotexamples.com/examples/mamba/-/describe/python-describe-function-examples.html) for some other examples on how Mamba can be used.
- [Expects matchers](https://expects.readthedocs.io/en/stable/matchers.html#) on how to use the matchers.
- [Mamba PDF doc](https://readthedocs.org/projects/mamba-bdd/downloads/pdf/latest/) for more comprehensive documentation on Mamba.
- The [Test Driven Development vs Behavior Driven Development](https://www.youtube.com/watch?v=Bq_oz7nCNUA) video by Dave Farley

