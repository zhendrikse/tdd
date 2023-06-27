# TTD materials

Test-driven development is a lot of fun, and a
great form of "deliberate practice". You have arrived at the right
place, you'll find here everything to get you up and running!

## Features

This repository contains materials to practice TDD

- **`cookiecutter/`** &rarr; [cookiecutter](https://github.com/cookiecutter/cookiecutter) templates for starting a kata in various languages
- **`docs/`** &rarr; additional free books
- **`kata-solutions/`** &rarr; solutions for almost all katas 
- **`presentations/`** &rarr; [reveal-md](https://github.com/webpro/reveal-md) presentations
- **`tdd-katas/`** &rarr; TDD katas
  - **`README.md`** outlining which aspects are addressed in which katas
  - **`a-kata-name/`** &rarr; katas in various languages such as Python, Java, Javascript, Kotlin, and Clojure with both introduction and detailed instructions
- **`tools/`** &rarr; playgrounds for getting aquainted with tools, libraries, and frameworks such as [approval testing](https://approvaltests.com/)

All materials are ready to be used in the Cloud, e.g. on [replit.com](https://replit.com) or [gitpod.io](https://gitpod.io)

# About coding katas

> Japanese culture influenced a lot software and project management fields. 
> Concepts like [Lean](https://apiumhub.com/?p=55302), [Kata](https://apiumhub.com/?p=4044), etc 
> has come from Japan. And we should admit, that they have improved the existing processes, 
> increasing efficiency and satisfaction overall &#8212; [apiumhub.com](https://apiumhub.com/tech-blog-barcelona/code-kata/)

With the materials in this repository you'll learn TDD by practicing 
so-called [coding katas](https://apiumhub.com/tech-blog-barcelona/code-kata/):

![Kata](./assets/kata.png)

> A kata is an exercise in karate where you repeat a form many, many times, making little improvements in each. 
> The intent behind code kata is similar &#8212; [codekata.com](http://codekata.com/) 

Generally speaking, each kata tries to target one or more skills, 
and this curriculum is no exception to that general rule. As the saying goes, 
practice makes perfect, and the same holds for (coding) katas: preferably 
you make them your own by repeating them _time and again_.

## Katas to practice TDD

Although the basic rules of TDD are relatively straightforward, 
TDD turns out to be a skill and as such, has to be acquired. 
Like playing piano. Like practicing martial arts in a dojo by executing 
katas time and again!

And although the saying goes that practice makes perfect, the reality is 
that code almost never reaches a perfect state: you can always find ways to 
further improve your code and your skill(s). Likewise with TDD, your TDD journey 
definitely won't stop after completing this course. There are always new ways to 
become more proficient and faster. Luckily, it turns out that mastery 
(from [Daniel Pink's Autonomy Mastery Purpose](https://www.youtube.com/watch?v=u6XAPnuFjJc)) 
is one of the three primary drivers that keeps us motivated. Moreover, the pay-off of
mastering TDD is much higher than the investments that you'll put in. 

After spending a certain time with TDD, people claim that there is no 
other way to develop a software. It is almost a learning to type with ten 
fingers: once you master the skill, you wonder how you ever managed without it.

The primary focus of all katas in this repository will be on TDD, but 
obviously many other programming ascpects will be practiced along the way! 
Among these are [encapsulation](https://en.wikipedia.org/wiki/Encapsulation_(computer_programming)), 
[single responsibility principle](https://en.wikipedia.org/wiki/Single-responsibility_principle), 
[clean architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html), 
[approval testing](https://approvaltests.com/), [mutation testing](https://en.wikipedia.org/wiki/Mutation_testing), 
[lift-up conditional refactoring](https://www.eficode.com/blog/advanced-testing-refactoring-techniques-2), to name but a few.  

 

# Learning Goals

![Skills](./assets/skillz.png)

By practising these katas, you will:

- be confident to apply both TDD and BDD (behaviour driven development) in day-to-day work by writing executable specifications as opposed to unit tests that are tightly coupled to implementation.
- know how to explain why TDD and BDD are such a pivotal skills to have as a software engineer
- be able to confidently refactor any piece of code (as you will always have 100% coverage), and you will be able to do so in extremely small increments.
- be able to not only refactor but also extend/modify legacy code that initially did not have any unit tests at all!
- know how to cope with external dependencies to the system under test by applying the [adapter pattern](https://refactoring.guru/design-patterns/adapter)
- be able to work according to the [Detroit and London schools of TDD](https://github.com/testdouble/contributing-tests/wiki/Test-Driven-Development) and know when and how to properly apply mocks, stubs, fakes, spies, etc.

# Expected  Background

![Student](./assets/black-belt.png)

---

### What general programming skills are required?

These katas are intended for people who want to learn TDD. Some basic programming experience is required, such as knowning what a `class` is, what an `object` is, what a `primitive` is, what `exception handling` entails, and how to write `conditionals` and `loops`. 

Although not scritly required, it will also definitely help if you are already familiar with concepts such as [encapsulation](https://en.wikipedia.org/wiki/Encapsulation_(computer_programming)) and the [single responsibility principle](https://en.wikipedia.org/wiki/Single-responsibility_principle).

---

### Is there a preferred programming language?

No, there isn't. There are cookie cutter templates for many languages available,
but even if there isn't any for your favourite programming language, you can still
do many of the katas. Moreover, the programming language is kind of irrelevant for
practising the various aspects that are being addressed. I have facilitated many [coding dojos](https://codingdojo.org/WhatIsCodingDojo/) where multiple participants were exposed to 
e.g. Python for the first time, and they managed pretty soon pretty well.

---


# About the author

![Zeger Hendrikse](assets/zeger_profile.png)

My name is [Zeger Hendrikse](https://www.linkedin.com/in/zegerhendrikse/). I am a self-employed IT consultant. I'm a fan of [extreme programming](https://en.wikipedia.org/wiki/Extreme_programming), [continuous delivery](https://www.continuousdelivery.com/), and [DevOps](https://cloud.google.com/devops) / [DORA](https://www.devops-research.com/research.html). 

This means my heroes are [Dave Farley](https://www.davefarley.net/), [Robert C. Martin](http://blog.cleancoder.com/) (aka Uncle Bob), [Martin Fowler](https://martinfowler.com/), [Kent Beck](https://www.kentbeck.com/)... just to name a few.

I decided to share one of my passions with all of you here: TDD (test driven development)!

### Contact

Feel free to contact me at: **zeger** _&lt;dot&gt;_ **hendrikse** _&lt;at&gt;_ **gmail** _&lt;dot&gt;_ **com** for e.g.:
- Feedback and suggestions
- Offering any of the katas in other languages than offered here
- Facilitating a course and/or [coding dojos](https://codingdojo.org/WhatIsCodingDojo/), where apprentices can practice [katas](http://codekata.com/) together (with me as sensei 😉).


  
# Credits

Pictures in this course are legally taken from [pixabay.com](https://pixabay.com). Many of the original unadapted code katas can be found at [kata-log.rocks](https://kata-log.rocks/) and/or at [codingdojo.org](http://codingdojo.org/) and [katas](http://codingdojo.org/) contained therein.
