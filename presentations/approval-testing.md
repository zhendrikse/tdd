---
title: Approval testing legacy code
author: Zeger Hendrikse
date: 2023-09-29
css: css/custom.css
highlightTheme: github-dark
---

<!-- .slide: data-background="./images/clay-banks-a9kHtTbjpwY-unsplash.jpg" data-transition="fade" -->

## Refactoring Legacy Code

# Using approval tests

by [Zeger Hendrikse](https://www.it-essence.nl/)

&nbsp;

&nbsp;

&nbsp;

&nbsp;

---

![Goals](./images/goals.png)

- <!-- .element: class="fragment" --> 
  Learn about legacy code
- <!-- .element: class="fragment" --> 
  Learn about approval testing
- <!-- .element: class="fragment" --> 
  When to use it and when not

&nbsp;

&nbsp;

&nbsp;


---

![Michael Feathers](./images/legacy_code.png) <!-- .element width="33%" height="33%" -->

> To me, legacy code is simply code without tests &#8212; [Michael Feathers](https://www.goodreads.com/book/show/44919.Working_Effectively_with_Legacy_Code)

---

## Or even better...

> Legacy Code is valuable code you’re afraid to change &#8212; [Nicolas Carlo](https://understandlegacycode.com/blog/what-is-legacy-code-is-it-code-without-tests/)

---

## 😱 But we need to modify it 😱 


![Question](./images/hiclipart.com.png)

---

## [The naive](https://github.com/nicoespeon/talk-how-to-change-untested-code): Edit and Pray 🙏

1. <!-- .element: class="fragment" --> 
   Edit the code
2. <!-- .element: class="fragment" --> 
   Test manually
3. <!-- .element: class="fragment" --> 
   Pray you didn't brake anything

&nbsp;
Drawbacks: very risky &amp; stressful
<!-- .element: class="fragment" --> 

---

## [The ideal](https://github.com/nicoespeon/talk-how-to-change-untested-code): Write the damn tests ✅

1. <!-- .element: class="fragment" --> 
   Reverse engineer the specs from the code
2. <!-- .element: class="fragment" --> 
   Write automated tests
3. <!-- .element: class="fragment" --> 
   Refactor the code
4. <!-- .element: class="fragment" --> 
   Add your feature

&nbsp;
Drawbacks: very costly and sl-o-o-o-w...
<!-- .element: class="fragment" --> 

---
## [The pragmatic](https://github.com/nicoespeon/talk-how-to-change-untested-code): Approval tests 💁

1. <!-- .element: class="fragment" --> 
   Generate an output you can snapshot 📸 
2. <!-- .element: class="fragment" --> 
   Use test coverage to find all input combinations ✅ 
3. <!-- .element: class="fragment" --> 
   Use mutations to verify your snapshots 👽 


---

## [Approval tests](https://approvaltests.com/)

Also known as

- Characterization Tests
- Golden Master
- Snapshot Tests
- Locking Tests
- Regression Tests
---

## What we are going to test

```python
class Calculator():
  @staticmethod
  def addNumbers(x: int, y: int) -> int:
    return x + y
```

---

## How we verify

```python
import unittest
from approvaltests.approvals import verify
from calculator import Calculator

class CalculatorTest(unittest.TestCase):

  def test_main(self):
    # ARRANGE
    x: int = 1
    y: int = 2;
    # ACT
    result = Calculator.addNumbers(x, y)
    # APPROVE
    verify(result)
```

---

## Even with combinatorial tests 🤩

```python
...
from approvaltests.combination_approvals import verify_all_combinations

class CalculatorTest(unittest.TestCase):

  def test_add_combinatorial(self):
    verify_all_combinations( Calculator.addNumbers, [[1,2], [4,3]])
```

---

<iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@zwh/ApprovalTestDemoPython?lite=false"></iframe>

---

## Approval testing [use cases](file://solon.prd/files/P/Global/Users/C65923/UserData/Downloads/raid_informaatika_2021.pdf)

- <!-- .element: class="fragment" --> 
  Code without tests that needs to be changed
- <!-- .element: class="fragment" --> 
  APIs that return JSON or XML
- <!-- .element: class="fragment" --> 
  Complex return objects
- <!-- .element: class="fragment" --> 
  Strings longer than one line

---

## [You should NOT keep these tests](https://github.com/nicoespeon/talk-how-to-change-untested-code)

Problems:

- <!-- .element: class="fragment" --> 
  Existing behavior is captured, bugs included
- <!-- .element: class="fragment" --> 
  Tests will fail whenever behavior changes. Noisy!
- <!-- .element: class="fragment" --> 
  People will get used to just update them
- <!-- .element: class="fragment" -->
  You can't read them to understand what the code does
- <!-- .element: class="fragment" --> 
  Delete them or have a plan to replace them with unit tests.

