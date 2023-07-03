# Kata overview

The difficulty is ranked as **L** (low), **M** (medium), and **H** (high).

| Kata                                           | Difficulty | Aspects                                             |
| ---------------------------------------------- | ---------- | --------------------------------------------------- |
|  1. [bugs-zero-kata](./bugs-zero-kata)         | M &harr; H | Legacy code / refactoring / bugs                    |
|  2. [christmas-tree](./christmas-tree)         | M          | Implement an algorithm in small steps               |
|  3. [countries-kata](./countries-kata)         | L &harr; M | Ports &amp; adapters / REST / Ports &amp; adapters  |
|  4. [db-adapter-kata](./db-adapter-kata)       | M          | Ports &amp; adapters / DB / Ports &amp; adapters    |
|  5. [game-of-life](./game-of-life)             | H          | Generic TDD skills                                  |
|  6. [gilded-rose-kata](./gilded-rose-kata)     | H          | Legacy code / refactoring / approval tests          |
|  7. [greed-kata](./greed-kata)                 | M          | Implement complex rules                             |
|  8. [locker-room-kata](./locker-room-kata)     | M &harr; H | Stateless / functional programming                  |
|  9. [manhattan-distance](./manhattan-distance) | L &harr; M | 1, 2, N / encapsulation                             |
| 10. [mars-rover](./mars-rover)                 | M &harr; H | Generic TDD / Design decisions                      |
| 11. [poker-hands-kata](./poker-hands-kata)     | H          | Outside-in / Mocks / Design decisions               |
| 12. [stack-kata](./stack-kata)                 | L          | Getting started with TDD                            |
| 13. [sudoku-kata](./sudoku-kata)               | M &harr; H | Recursion &amp; TDD / Backtracking algorithms       |
| 14. [task-list-kata](./task-list-kata)         | M &harr; H | Command-Query / Strong typing / Realistic app       |
| 15. [tell-dont-ask](./tell-dont-ask)           | M &harr; H | Refactoring / Anemic domain model / DDD             |
| 16. [tire-pressure-kata](./tire-pressure-kata) | L          | Ports &amp; adapters / Testability                  |
| 17. [vending-machine](./vending-machine)       | M          | Generic TDD skills / Code smells and refactoring    |
| 18. [video-store-kata](./video-store-kata)     | M          | Legacy code / Refactoring / Code smells             |

# Relation with 24 Key Capabilities

The relation to the 
[24 Key Capabilities to Drive Improvement in Software Delivery](https://itrevolution.com/articles/24-key-capabilities-to-drive-improvement-in-software-delivery/)
is outlined next.

## [Continuous Delivery Capabilities](https://itrevolution.com/articles/24-key-capabilities-to-drive-improvement-in-software-delivery/#nav-1)

### 1. Use Version Control for all Production Artifacts

You may always opt to use a version control system when practicing your katas. 

When katas are done in a group in a [randori style](https://codingdojo.org/practices/RandoriKata/), 
a commit by the person(s) ending his/her/their turn and a subsequent pull by the next may be used to
pass the code on.

### 2. Automate Your Deployment Process

For this capability, a dedicated kata still needs to be added.

### 3. Implement Continuous Integration

For this capability, a dedicated kata still needs to be added.

### 4. Use Trunk-Based Development Methods

Trunk-based development can easily be simulated when katas are done 
in a group in a [randori style](https://codingdojo.org/practices/RandoriKata/), 
a commit by the person(s) ending his/her/their turn and a subsequent pull 
by the next may be used to pass the code on.

### 5. Implement Test Automation

Obviously, this is what lies at the heart of TDD. 
Note that integration testing is also touched upon when the katas
involve working with 
[ports and adapters](https://alistair.cockburn.us/hexagonal-architecture/).

Even more so, many katas address the subject of creating a testable design,
and/or address techniques for making legacy code testable.

### 6. Support Test Data Management

This is not covered (yet).

### 7. Shift Left on Security

This is not covered (yet).

### 8. Implement Continuous Delivery (CD)

## [Architecture Capabilities](https://itrevolution.com/articles/24-key-capabilities-to-drive-improvement-in-software-delivery/#nav-2)

### 9. Use a Loosely Coupled Architecture

This capability is touched upon when the katas
involve working with 
[ports and adapters](https://alistair.cockburn.us/hexagonal-architecture/).

### 10. Architect for Empowered Teams

This is not covered (yet).

## [Product and Process Capabilities](https://itrevolution.com/articles/24-key-capabilities-to-drive-improvement-in-software-delivery/#nav-3)

### 11. Gather and Implement Customer Feedback

This can be covered e.g. with the video store kata, by asking the participants
to produce a PDF statement printer after they have finished with the HTML variant.
After finishing the PDF statement printer, ask them to write a CSV variant, etc.
Continue to the point where they will start to complain "What do you actually need
this statement format for", and grab that opportunity to teach the participants to
ask that question for each and every single feature now and in the future!

### 12. Make the Flow of Work Visible through the Value Stream

This is addressed by showing the participants the TODO list that they are encouraged
to maintain while practicing the katas. In addition, you may consider using 
[Scrumblr](https://github.com/aliasaria/scrumblr), an instance of which you can 
easily start yourself [here](https://replit.com/@zwh/Scrumblr).

### 13. Work in Small Batches

This aspect is addressed in _all_ katas.

### 14. Foster and Enable Team Experimentation 

Although this aspect isn't addressed _specifically_ by any of the katas, it is
addressed _implicitly_, as the way of working practiced here contributes to
the capability of a team to carry out experiments.

## [Lean Management and Monitoring Capabilities](https://itrevolution.com/articles/24-key-capabilities-to-drive-improvement-in-software-delivery/#nav-4)

## 15. Have Lightweight Change Approval Processes

[Pair programming](https://martinfowler.com/articles/on-pair-programming.html) and/or 
intrateam code reviews are continuously being addressed when practicing katas in coding dojos. 

### 16. Monitor across Applications and Infrastructure to Inform Business Decisions

This is not covered (yet).

### 17. Check System Health Proactively

This is not covered (yet).

### 18. Improve Processes and Manage Work with Work-In-Process (WIP) Limits

In each and every kata, it is always emphasized to focus on one change at a time,
and one change at a time only!

### 19. Visualize Work to Monitor Quality and Communicate throughout the Team

This is not covered (yet).

## [Cultural Capabilities](https://itrevolution.com/articles/24-key-capabilities-to-drive-improvement-in-software-delivery/#nav-5)

### 20. Support a Generative Culture

Almost all hallmarks of this measure such as good information flow, high cooperation, and trust, 
bridging between teams, and conscious inquiry are continually practiced during coding dojos.

### 21. Encourage and Support Learning

The whole purpose of a coding dojo and its katas is to support learning!

### 22. Support and Facilitate Collaboration among Teams

This is not covered (yet).

### 23. Provide Resources and Tools that Make Work Meaningful.

As this measure is about being given the tools and resources needed to do your job well,
it is obviously continually being addressed by these katas.

### 24. Support or Embody Transformational Leadership

As participants need regular time to practice these katas, management needs to be
informed about these activities. In this way, at least one of the aspects of transformational
leadership (intellectual stimulation) is a prerequisite for making coding dojos a reality. 
