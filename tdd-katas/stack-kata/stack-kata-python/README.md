# Introduction

Please read the general [introduction to the stack kata](../README.md) first!

# Getting started

First install [cookiecutter](https://www.cookiecutter.io/) by invoking

```bash
$ poetry install
```

Next, create an empty kata project to get yourself started

```bash
$ poetry run cookiecutter https://github.com/zhendrikse/cookiecutter-kata-python.git
```

Answer the questions mutatis mutandum like so

```
$ poetry run cookiecutter https://github.com/zhendrikse/cookiecutter-kata-python.git

kata [GameOfLife]: Stack
description [This kata practices TDD]: Stack kata to practice TDD
Select rspec_syntax:
1 - y
2 - n
Choose from 1, 2 [1]: 1
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
$ poetry install
```

The tests can be run as follows

```bash
$ poetry run mamba --format=documentation test/*_test.py
```

In case you opted for plain PyTest, you can just run

```bash
$ ptw
```

## Preparations

When practising TDD, you basically make a mind switch from writing tests to writing (executable) specifications. In other words, we [specify the behaviour](https://www.youtube.com/watch?v=Bq_oz7nCNUA) that we would like our system to exhibit. An [RSpec](https://rspec.info/)-like syntax helps us to do so, and [Mamba](https://mamba-bdd.readthedocs.io/en/latest/) offers us such an equivalent for Python:

```python
with description(Stack) as self:
  with context("Given a new stack"):
    with it("should be empty"):
      my_stack = Stack()
      expect(my_stack.is_empty()).to(equal(True))
```

When you run this example, you'll see that the test fails, as we did not implement the `Stack` class yet:

```python
class Stack:
  pass
```

## Implementation

### Exercise I: emtpy stack

- Write the most simple/stupid implementation of the required method `is_empty()`. 
- Check if the test passes now. 
- Check if the code coverage is (still) 100%.
- In our TDD cycle we went from red -> green. At this point there is nothing to refactor though.

### Exercise II: pop on empty stack

We are going to continue with bullet number 2 from our TODO list. According to this list, we are going to specify our stack throws an exception when we perform a `pop()` operation on an empty stack.

- Add the following specification to the existing context:
  ```python
      with it("should throw an exception on a pop operation"):
        my_stack = Stack()
        expect(lambda: my_stack.pop()).to(raise_error(KeyError, "Stack underflow"))  
  ```
- Check that the test fails.
- Write the most simple/stupid implementation of the required method `pop()`.
- Check that the code coverage is still 100%
- We went from red -> green. Can you identify the line(s) with any duplicate code?

### Intermezzo: using `before.each`

We can isolate duplicate code by using a `before.each` clause:
```python
with description(Stack) as self:
  with context("Given a new stack"):
    with before.each:
      self.my_stack = Stack()
```

### Exercise III: applying the DRY principle

- Move the duplicate stack initialization into a shared `before.each` clause.

### Exercise IV: push on empty stack

Continuing with item number three from our TODO list:

- Specify that the stack should no longer be empty after a `push()` operation:
  ```python
      with context("when one element is pushed"):
       with it("should not be empty anymore"):
         self.my_stack.push(8)
         expect(self.my_stack.is_empty()).to(equal(False))
  ```  
- Check that the test fails.
- Write the most simple/stupid implementation of the required method `push()`. 
  
  **Hint**: we cannot avoid the introduction of a (boolean) member variable in the `Stack` class to check for "emptyness". Set this variable accordingly in the `push()` and `pop()` methods.
- Check that the code coverage is still 100%
- Is there anything left to refactor?

### Exercise V: pop on an non-empty stack

Arriving at item number four from our TODO list:

- Write a specification that asserts that a stack with one element pushed should be empty after a `pop()` operation. Don't assert for the right value to be returned just yet!
- Make the test succeed just by modifying the `pop()` method, so that it sets the boolean member variable.
- Refactor the shared set-up, i.e. the initialization of a stack containing one element.
- Create a failing test that verifies the proper value is returned by the `pop()` operation.
- Modify the production code to return the proper value. Do this by hardcoding the return value for now!

### Exercise VI: multple pushes and pops

Finally we are going for the real stack implementation:

- Write a failing specification that asserts the stack is not empty after an additional element is pushed onto the stack followed by a single pop operation.
- Modify the production code to make the test green by introducing a member varialbe `size`.
- Can we refactor? Hint: the boolean member variable, is it still needed?
- Write a specification that verifies the most recent pushed value is actually returned. 
- Make the test green by introducing a member variable that stores the most recently pushed value. 
- Can we refactor a shared initialization once more? Make it so!
- Write a specification that verifies if the value that has been pushed first is returned after two pop operations.
- Finally, extend the production code by changing the type of the element member variable into an array, using the size member variable as an index, so that the test becomes green again!

## Retrospective

If you completed this exercise, you should end up with something like the following:

```
Stack
  Given a new stack
    ✓ it should be empty
    ✓ it should throw an exception on a pop operation
    with one item pushed
      ✓ it should not be empty anymore
      when element is popped
        ✓ it should be empty again
        ✓ it should return the popped element
      when an additional element is pushed
        ✓ it should not be empty after a pop
        ✓ it should return the most recent element after one pop
        ✓ it should return the first element after two pops

8 examples ran in 0.0399 seconds
Wrote HTML report to htmlcov/index.html
```
Note the following:
- We can show our (executable) specifications/tests to our product owner: in this form he should also be able to read them!
- That tests tend to group themselves according to a commonly shared set-up. This turns out to be a general rule.
- The difficulty in TDD is "postponing the gold", i.e. postponing the final solution until all tests have been put in place first.
- The tests gradually become more specific, while at the same time our code base becomes more generic.
