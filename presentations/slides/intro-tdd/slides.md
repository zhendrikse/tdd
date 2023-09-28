---
title: Introduction into test-driven development
author: Zeger Hendrikse
date: 2023-09-29
---

<!-- .slide: data-background="./images/intricate-explorer-HZ7VEe7Ni1s-unsplash.jpg" -->

#### Coders should test &mdash; testers should code

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

#### We all should do TDD!

by [Zeger Hendrikse](https://www.it-essence.nl/)
</section>

---

##### eXtreme Programming

![XP](./images/xp_circles.jpg)

---
 
![Feedback loops](./images/Extreme_Programming.svg.png) <!-- .element width="75%" height="75%" -->

---

### [Dave Farley](https://www.youtube.com/watch?v=Bq_oz7nCNUA) &#8212; the culture of TDD

![TDD](./images/dave_farley_tdd.png)

---

##### Daniel North and Chris Matts

- Test Suite => specification
- Test => scenario
- Structure tests around "[Given, When, Then](https://martinfowler.com/bliki/GivenWhenThen.html)"

---

##### rSPec

```ruby
# spec/string_calculator_spec.rb
describe StringCalculator do

  describe ".add" do
    context "given an empty string" do
      it "returns zero" do
        expect(StringCalculator.add("")).to eq(0)
      end
    end
  end
end
```

---

##### We test _behaviour_ with TDD

<iframe width="100%" height="500" src="//jsfiddle.net/zhendrikse/bu7tv1kp/3/embedded/js,result/dark/" allowfullscreen="allowfullscreen" allowpaymentrequest frameborder="0"></frame>

---

##### Specifications drive design

![Design](./images/video-game.png)

---

##### TDD &amp; BDD

![TDD &amp; BDD](./images/tdd-scope.png)

---


### Contra-variance and co-variance

![Contra- and co-variance](./images/contra_co_variant5.png)

---

### <a href="https://blog.cleancoder.com/uncle-bob/2017/10/03/TestContravariance.html">Test Contra-variance</a>

[![unit tests](./images/covariant_unit_tests.png)](https://martinfowler.com/bliki/UnitTest.html)

---

### Bob Martin: [Test Contra-variance](https://www.infoq.com/news/2017/10/bob-martin-contra-variance/)

> The structure of the tests must not reflect the structure of the production code because that much coupling makes the system fragile and obstructs refactoring. Rather, the structure of the tests must be independently designed so as to minimize the coupling to the production code.

---

### Contra-variance can only be achieved using TDD

Why? ==> Because we specify! <!-- .element: class="fragment"-->


---

### Rulez of the TDD game

<table>
  <colgroup>
    <col span="1" style="width: 60%;"/>
    <col span="1" style="width: 40%;"/>
  </colgroup>
			         
  <tbody><tr>
    <td>
      <img alt="Red Green Refactor" src="./images/redgreenrefactor.png"/>
    </td>
    <td>
      <ol>
        <li>Write a failing test</li>
        <li>Make it pass</li>
        <li>Refactor relentlessly</li>
      </ol>
    </td>
  </tr></tbody>
</table>

---

### [Martin Fowler](https://refactoring.com/): refactoring

![Martin Fowler](./images/fowler.jpg)

... is a disciplined technique for restructuring an existing body of code, altering its internal structure without changing its external behavior 
---

### Rulez of the TDD game

**Small increments**, so we are [not allowed to write](http://blog.cleancoder.com/uncle-bob/2014/12/17/TheCyclesOfTDD.html):

1. <!-- .element: class="fragment"-->
   any production code before you have a failing test
2. <!-- .element: class="fragment"-->
   any more of a test than is sufficient to fail (also compilation!)
3. <!-- .element: class="fragment"-->
   any more code than is sufficient to pass the one failing unit test

---

### Kent Beck

![Kent Beck](./images/kent_beck.png)

---
### <a href="https://en.wikipedia.org/wiki/Kent_Beck">Kent Beck's</a> [design rules](https://martinfowler.com/bliki/BeckDesignRules.html)

1. <!-- .element: class="fragment"-->
   Passes the tests
2. <!-- .element: class="fragment"-->
   Reveals intention ([Clean code](https://gist.github.com/wojteklu/73c6914cc446146b8b533c0988cf8d29)) &rarr; [game of life](https://github.com/zhendrikse/tdd/blob/master/tdd-katas/game-of-life/README.md):
   ```clojure
   (defn next-generation-of [game]
     (map #(to-living-cell 
            (which-both 
             is-dead? 
             (has-exactly-three? (living-neighbours-in game))) %) 
     (map #(to-dead-cell 
            (which-both 
             is-alive? 
             (which-either 
              (has-less-than-two? (living-neighbours-in game)) 
              (has-more-than-three? (living-neighbours-in game)))) %) game)))
   ```
4. <!-- .element: class="fragment"-->
   No duplication ([DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself))
5. <!-- .element: class="fragment"-->
   Fewest elements ([STTCPW](http://wiki.c2.com/?DoTheSimplestThingThatCouldPossiblyWork))

---

### TDD is not building a bridge nor house!

![cartoon](./images/tdd_cartoon.png)

---

### User story

<div style="text-align: left">
<b>As</b> a worker in a restaurant 

<b>I want</b> to place my clean plates on a stack 

<b>so that</b> I always have plates available to serve dishes
<div>

---

#### Plans are worthless ...

### ... but planning is essential:

- Start with an empty stack
- Define pop on an empty stack
- Define push on an empty stack
- Define pop on a non-empty stack
- Define multiple pushes and pops

&nbsp;

Credits to <a href="http://barbra-coco.dyndns.org/yuri/Kent_Beck_TDD.pdf">Kent Beck</a> and <a href="https://quoteinvestigator.com/2017/11/18/planning/">Eisenhower</a>! <!-- .element: class="fragment"-->

---

<iframe width="100%" height="700" src="//replit.com/@zwh/Scrumblr?embed=true" allowfullscreen="allowfullscreen" allowpaymentrequest frameborder="0"></frame>

---

### Let's do this

- Let's do this [in Javascript](./javascript/slides.md)!
- Let's do this [in Python](./python/index.html)!
- Let's do this [in Typescript](./typescript/index.html)!
- Let's do this in Java
- Let's do this in C#
- Let's do this in C++

---

### Retrospective

- <!-- .element: class="fragment"-->
  [Tests become more _specific_, code more _generic_](http://blog.cleancoder.com/uncle-bob/2014/12/17/TheCyclesOfTDD.html)
- <!-- .element: class="fragment"-->
  [TBD](../ci-tbd/index.html) becomes a no-brainer
- <!-- .element: class="fragment"-->
  Difficulty is "postponing the gold"
- <!-- .element: class="fragment"-->
  [Contravariant test suites](https://blog.cleancoder.com/uncle-bob/2017/10/03/TestContravariance.html)
- <!-- .element: class="fragment"-->
  1, 2, N
- <!-- .element: class="fragment"-->
  Tests grouped according to shared set-up
- <!-- .element: class="fragment"-->
  What is still left to test?

---

### It's only the beginning...

<ul>
<div>
<li><a href="https://martinfowler.com/articles/mocksArentStubs.html">Mocks, stubs, fakes, spies, ...</a></li>
</div>
<div class="fragment">
<li><a href="https://khalilstemmler.com/articles/software-design-architecture/organizing-app-logic/">The Clean Architecture</a>: how to cope with dependencies on external systems</li>
</div>
<div class="fragment">
<li><a href="https://blog.devgenius.io/detroit-and-london-schools-of-test-driven-development-3d2f8dca71e5">London vs Detroit schools of TDD</a></li>
</div>
<div class="fragment">
<li>Developer tests his own code: <a href="../four-eyes/index.html">the nightmare of every auditor!</a></li>
</div>
</ul>

---
### Resources

- Kent Beck, [Test-Driven Development By Example](http://barbra-coco.dyndns.org/yuri/Kent_Beck_TDD.pdf) 
- [QWAN’s Little Book of Test Driven Development](tdd-booklet.pdf)
- ...


### With special thanks to ...

![Uncle Bob](./images/unclebob.gif)

---
![Goals](./images/goals.png)

- <!-- .element: class="fragment"-->
Coding + testing are the same activity

- <!-- .element: class="fragment"-->
The importance of [test contra-variance](https://blog.cleancoder.com/uncle-bob/2017/10/03/TestContravariance.html)

- <!-- .element: class="fragment"-->
See how TDD is done _in practice_

- <!-- .element: class="fragment"-->
Motivation to learn & practice more TDD

---
### Rulez during this session

<ul>
<div>
<li>Questions are allowed at all times</li>
</div>
<div class="fragment">
<li>
The goal is to illustrate <i>the TDD process</i>
  <ul>
  <li>The goal is <em>not</em> to write the best
    <ul>
    <li>Javascript ever</li>
    <li>Python ever</li>
    <li>...</li>
    </ul>
   </li>
   <li>User story is not the most realistic either</li>
</li>
</div>

---

---

### Summary

<ul>
  <div>
    <li>Unit test === Functional test</li>
  </div>
  <div class="fragment">
    <li>Unit tests test the smallest <em>functional</em> unit</li>
  </div>
  <div class="fragment">
    <li>Practicing TDD/BDD &nbsp;==&gt;&nbsp; test contra-variance</li>
  </div>
  <div class="fragment">
    <li>xUnit tests &#8800; TDD</li>
  </div>
  <div class="fragment">
    <li>BDD &#8800; tools (<a href="https://cucumber.io/docs/bdd/">Cucumber</a> / <a href="https://specflow.org/">Specflow</a>)</li>
  </div>
  <div class="fragment">
    <li>BDD = <a href="http://rspec.info/">RSpec</a>-style specifications</br>
     (<a href="http://jasmine.github.io/">Jasmine</a>/<a href="https://mochajs.org/">Mocha</a>/<a href="https://facebook.github.io/jest">Jest</a>/<a href="https://opensourcelibs.com/lib/specnaz">Specnaz</a>/<a href="https://github.com/nestorsalceda/mamba">Mamba</a>...)
    </div>
  <div>
    <li>Unit test === Functional test</li>
  </div>
</ul>
