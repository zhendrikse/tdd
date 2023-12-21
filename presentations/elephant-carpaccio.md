---
title: Elephant carpaccio kata
author: Zeger Hendrikse
date: 2023-12-19
css: css/custom.css
highlightTheme: github-dark
---

<!-- .slide: data-background="./images/elephant.png" width="50%" height="50%" -->

&nbsp;

&nbsp;

# Elephant Carpaccio kata

&nbsp;

&nbsp;

### by [Zeger Hendrikse](https://www.it-essence.nl/)

&nbsp;


#### Credits: Alistair Cockburn, Hendrik Kniberg, Michael Wallace

&nbsp;


---

![Goals](./images/goals.png)

- <!-- .element: class="fragment" --> 
  Splitting user stories vertically
- <!-- .element: class="fragment" --> 
  Value of splitting user stories
- <!-- .element: class="fragment" --> 
  Software delivery value curve
- <!-- .element: class="fragment" --> 
  Hands-on practice and retrospective

&nbsp;

&nbsp;

&nbsp;

---

## About ...

- Elephant Carpaccio kata
  - <!-- .element: class="fragment" --> 
    Alistair Cockburn, minor mods by Henrik Kniberg
  - <!-- .element: class="fragment" --> 
    Practice and learn thin slicing
    - size ~ 1-week to 1-day requests
    - from the perspective of the business
  - <!-- .element: class="fragment" --> 
    Experienced teams: all user stories &lt;= 1 day 
  - <!-- .element: class="fragment" --> 
    Metaphor: huge elephant ==&gt; tiny sliced stories

---

## Good user stories

- [INVEST](https://www.agilealliance.org/glossary/invest/)
  - <!-- .element: class="fragment" --> 
    “I” ndependent (of all others)
  - <!-- .element: class="fragment" --> 
    “N” egotiable (not a specific contract for features)
  - <!-- .element: class="fragment" --> 
    “V” aluable (or vertical)
  - <!-- .element: class="fragment" --> 
    “E” stimable (to a good approximation)
  - <!-- .element: class="fragment" --> 
    “S” mall (so as to fit within an iteration)
  - <!-- .element: class="fragment" --> 
    “T” estable (in principle, even if there isn’t a test for it yet)

---

## How big are your stories

![Size of user stories](./images/sliced_user_stories.png)


- Target
  - <!-- .element: class="fragment" --> 
    Story = a few days
  - <!-- .element: class="fragment" --> 
    Task = a few hours
  - <!-- .element: class="fragment" --> 
    Commit = several times per hour

---

## Why split stories

- Discuss in teams (5 minutes)

----

- Example outcomes:
  - <!-- .element: class="fragment" --> 
    Learn faster
  - <!-- .element: class="fragment" --> 
    Deliver more often
  - <!-- .element: class="fragment" --> 
    Happier stakeholders
  - <!-- .element: class="fragment" --> 
    Better synchronization with other people and teams (testing)
  - <!-- .element: class="fragment" --> 
    Better prioritization
  - <!-- .element: class="fragment" --> 
    Better product earlier
  - <!-- .element: class="fragment" --> 
    More business options
  - <!-- .element: class="fragment" --> 
    Less risk (less time “under water”)
  - <!-- .element: class="fragment" --> 
    Sense of velocity
  - <!-- .element: class="fragment" --> 
    Easier planning
  - <!-- .element: class="fragment" --> 
    Less risk of carryover

---

## Software delivery value curve

![Size of user stories](./images/value_delivered.png)

---

## User story splitting 

- <!-- .element: class="fragment" --> 
  Split by
  - capabilities offered
  - user roles / user personas
  - target device
  - CRUD boundaries
  - Happy path/other paths
- <!-- .element: class="fragment" --> 
  Zero/One/Many approach
- <!-- .element: class="fragment" --> 
  Scope: walking skeleton

---

## The kata

- Assignment
  - Create +/- 15 user stories for a simple application
  - Extremely thin slices, but each is elephant-shaped

![Elephant](./images/sliced_elephant.png) <!-- .element width="50%" height="50%" -->


----

## The Product

- Build a retail calculator app
  - <!-- .element: class="fragment" --> 
    Inputs:
    - How many of an item
    - Price per item
    - two-letter state code (for sales tax)
  - <!-- .element: class="fragment" --> 
    Output:
    - Total price of order
      - Discount based on order value 
      - Sales tax based on discounted value

----

- Create 10 - 20 slices to reach the target
  - <!-- .element: class="fragment" --> 
    A slice should 
    - have a UI (input and output)
    - be visibly different from the last slice
  - <!-- .element: class="fragment" --> 
    Sales tax _before_ discounts
    - Compliance: tax is a legal requirement
    - When compliant: we can deploy
  - <!-- .element: class="fragment" --> 
    Validation &amp; GUI &rarr; last!

----

## Priorities

<div class="r-stack">
  <img class="fragment fade-in-then-out" data-fragment-index="0" src="./images/five_states_five_discounts_1.png" />
  <img class="fragment fade-in-then-out" data-fragment-index="1" src="./images/five_states_five_discounts_2.png" />
  <img class="fragment fade-in-then-out" data-fragment-index="2" src="./images/five_states_five_discounts_3.png" />
  <img class="fragment fade-in-then-out" data-fragment-index="3" src="./images/five_states_five_discounts_4.png" />
</div>

----

- Create the backlog
  - <!-- .element: class="fragment" --> 
    Work in teams of 2 or 3 (or by table)
    - 10 minutes to create backlog on cards
    - 10-20 demo-able user stories (“slices”) to 5 states and 5 discounts.
  - <!-- .element: class="fragment" --> 
    A slice should be:
    - Implementable (including UI).
    - Noticeably different from last slice.
    - More valuable to customer than last slice
    - _Not_ be a mockup/UI/data structure/test case.

----

### Discounts
<!-- .element id="left" -->

### Taxes
<!-- .element id="right" -->

<!-- .element id="left" -->
| State | Tax rate |
|:----- |:-------- |
| UT    |  6.85%   |
| NV    |  8.00%   |
| TX    |  6.25%   |
| AL    |  4.00%   |
| CA    |  8.25%   |


<!-- .element id="right" -->
| Order value | Discount rate |
|:----------- |:------------- |
| $1,000      | 3%            |
| $5,000      | 5%            |
| $7,000      | 7%            |
| $10,000     | 10%           |
| $50,000     | 15%           |

---

- Debrief
  - What was it like?
  - How many slices did you have? Examples?
  - Testing
    - No tests/unit tests/TDD?
    - Manual/automated (acceptance) tests?
  - Code quality?
  - Round-robin:
    - Any other questions or reflections?
    - What did you learn?
    - Take-aways from today?


