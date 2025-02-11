{% include breadcrumbs.html %}

# Communication with the outside world
<div class="header_line"><br/></div>

This page is about the hexagonal architecture.

![Ports and adapters](https://github.com/zhendrikse/tdd/raw/master/assets/ports-and-adapters-architecture.svg?sanitize=true)

The above picture has been taken from 
[Growing Object-Oriented Software Guided by Tests](http://www.growing-object-oriented-software.com/figures.html)
by Steve Freeman and Nat Pryce ([Creative Commons License](http://creativecommons.org/licenses/by-sa/4.0/)).

The central idea here is to move the dependencies to external systems
to the boundaries of your domain model. By defining ports (realized as interfaces)
and adapters (implementations of these interfaces that connect to the
external system), we

- Prevent externalities leaking into our system, such as relational data models, 
  JSON and/or XML message structures, and so forth.
- Make it easy to plug in fakes and stubs into our ports, which in turn keeps
  our tests independent of the external systems and guarantees that they remain fast!

Since some of the coding katas in this repository specifically address 
this topic, this page discusses the required concepts that are common
to all these katas. These concepts all fall under the umbrella of what's
generally known as the 
[Hexagonal Architecture](http://alistair.cockburn.us/Hexagonal+architecture) 
(a.k.a. Ports and Adapters). Uncle Bob elaborated on this concept and coined it the 
[clean architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html).

## TDD and communication with external systems

A question that is often raised is: How do I practice TDD when I
have to deal with the dependencies of my system to the outside world?
Examples of such dependencies are databases, file systems, networks, etc.
So isn't it inevitable then that I eventually have to include 
tests involving these external systems in my tests and as 
a consequence my tests (gradually) become slow?

Many people are inclined to introduce mocks into their tests at
this point, but apparently these people haven't heard of the
[don't mock what you don't own](http://jmock.org/oopsla2004.pdf)
principle. A good but somewhat long read about this topic is also
Martin Fowler's well-known 
[mocks aren't stubs](https://martinfowler.com/articles/mocksArentStubs.html).

So what do we do then when mocks are not meant to be used for this purpose?
The answer is to apply dependency
inversion and to use so-called ports and adapters. 
  
![Hexagonal architecture](https://github.com/zhendrikse/tdd/raw/master/assets/hex-arch.png)

- [Dependency Inversion](https://stackify.com/dependency-inversion-principle/) 
  is the last of the five well-known
  [SOLID](http://blog.cleancoder.com/uncle-bob/2020/10/18/Solid-Relevance.html)
  principles. In a nutshell, it boils down to dictating to the outside world
  what the data should look like, as opposed to letting the outside world 
  determine your (object) model. The idea is to think in terms of the 
  domain model first and to make the 
  [primary and secondary actors](https://codesoapbox.dev/ports-adapters-aka-hexagonal-architecture-explained/)
  comply with the ubiquitous language established by our domain model. 
  This implies e.g. that no field names or data models from external systems
  should be able to "leak" into our domain model!
  
- [Ports and adapters](https://alistair.cockburn.us/hexagonal-architecture/):
  as is explained in
  [this article](https://codesoapbox.dev/ports-adapters-aka-hexagonal-architecture-explained/),
  "The main principle of the Ports &amp; Adapters architecture is to have 
  inputs and outputs on the edges of technology-agnostic code". 


![Hexagonal architecture](https://github.com/zhendrikse/tdd/raw/master/assets/hex-arch-unit.png)

## References

- A good read is the 
[Ports and adapters as they should be](https://medium.com/wearewaes/ports-and-adapters-as-they-should-be-6aa5da8893b)
post by Felipe Flores.
By realizing the ports &amp; adapters by using
[the adapter pattern](https://refactoring.guru/design-patterns/adapter) 
(which is polymorphic by definition), we keep our system under 
development testable all the time.
- Another good website with project structure and code examples is [Hexagonal Me](https://jmgarridopaz.github.io/).
- Nicolas Carlo on separating infrastructure (tests) from domain (tests): [If you mock, are you even testing?](https://understandlegacycode.com/blog/if-you-mock-are-you-even-testing/)

{% include share_buttons.html %}