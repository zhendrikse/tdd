# Kata overview

The difficulty is ranked as **L** (low), **M** (medium), and **H** (high).

|     | Kata                                       | Difficulty | Aspects                                            |
| --- | ------------------------------------------ | ---------- | -------------------------------------------------- |
|  1. | [audio-player-kata](./audio-player-kata)   | M          | London vs. Detroit schools of TDD / Mocks, spies   |
|  2. | [bugs-zero-kata](./bugs-zero-kata)         | M          | **Legacy code** / **Refactoring** / Approval tests |
|  3. | [christmas-tree](./christmas-tree)         | L          | Implement an algorithm in **small steps**          |
|  4. | [countries-kata](./countries-kata)         | L &harr; M | Ports &amp; adapters / **Refactoring** / REST / DI |
|  5. | [cqrs-booking](./cqrs-booking)             | H          | CQRS / DDD / Event-based architecture              |
|  6. | [db-adapter-kata](./db-adapter-kata)       | M          | Ports &amp; adapters / Database / DI               |
|  7. | [fibonacci-kata](./db-adapter-kata)        | M          | Pipelines / Automated deployments / IaC            |
|  8. | [game-of-life](./game-of-life)             | M          | Generic TDD skills (**small steps**)               |
|  9. | [gilded-rose-kata](./gilded-rose-kata)     | M &harr; H | **Legacy code** / **Refactoring** / Approval tests |
| 10. | [greed-kata](./greed-kata)                 | M          | Implement complex rules in **small steps**         |
| 11. | [locker-room-kata](./locker-room-kata)     | M          | Stateless / Functional programming                 |
| 12. | [manhattan-distance](./manhattan-distance) | L          | 1, 2, N / Encapsulation                            |
| 13. | [mars-rover](./mars-rover)                 | M          | Generic TDD / Design decisions                     |
| 14. | [poker-hands-kata](./poker-hands-kata)     | H          | Outside-in / Mocks / Design decisions              |
| 15. | [stack-kata](./stack-kata)                 | L          | Getting started with TDD (**small steps**)         |
| 16. | [sudoku-kata](./sudoku-kata)               | M          | Recursion, TDD, and **small steps**                |
| 17. | [task-list-kata](./task-list-kata)         | M          | Command-Query / Strong typing / Realistic app      |
| 18. | [tell-dont-ask](./tell-dont-ask)           | M          | **Refactoring** / Anemic domain model / DDD        |
| 19. | [tire-pressure-kata](./tire-pressure-kata) | L          | Ports &amp; adapters / **Testable design** / DI    |
| 20. | [vending-machine](./vending-machine)       | L &harr; M | **Small steps** / Code smells and **refactoring**  |
| 21. | [video-store-kata](./video-store-kata)     | L          | **Legacy code** / Code smells and **refactoring**  |

# Relation with 24 Key Capabilities

The relation to the 
[24 Key Capabilities to Drive Improvement in Software Delivery](https://itrevolution.com/articles/24-key-capabilities-to-drive-improvement-in-software-delivery/)
is outlined next.

## Continuous Delivery Capabilities

The column with the checkmarks and crosses indicates which practices are covered with the coding katas. A plus-minus sign indicates partial coverage.

|     | [Continuous Delivery Capabilities](https://itrevolution.com/articles/24-key-capabilities-to-drive-improvement-in-software-delivery/#nav-1) | Covered | Explanation |
| --- | ------------------------------------------------ | ------- | ----------- |
|  1. | Use Version Control for all Production Artifacts | ✔      | You may always opt to use a version control system when practicing your katas. When katas are done in a group in a [randori style](https://codingdojo.org/practices/RandoriKata/), a commit by the person(s) ending his/her/their turn and a subsequent pull by the next may be used to pass the code on. |
|  2. | Automate Your Deployment Process                 | ✔      | This capability is covered by the Fibonacci kata. |
|  3. | Implement Continuous Integration                 | ±       | Continuous integration is elaborated on directly below this table |
|  4. | Use Trunk-Based Development Methods              | ✔      | Trunk-based development can easily be simulated when katas are done in a group in a [randori style](https://codingdojo.org/practices/RandoriKata/), a commit by the person(s) ending his/her/their turn and a subsequent pull by the next may be used to pass the code on. |
|  5. | Implement Test Automation                        | ✔      | Obviously, this is what lies at the heart of TDD. Note that integration testing is also touched upon when the katas involve working with [ports and adapters](https://alistair.cockburn.us/hexagonal-architecture/). Even more so, many katas address the subject of creating a testable design, and/or address techniques for making legacy code testable. |
|  6. | Support Test Data Management                     | ✗      | This capability is not covered by any of the katas yet ||
|  7. | Shift Left on Security                           | ✗      | This capability is not covered by any of the katas yet ||
|  8. | Implement Continuous Delivery                    | ✔       | When the skills and heuristics of TDD are correctly and properly applied all of the time, it should be no problem for a team to go to production at any given time. This is one of the hallmarks of continuous delivery! So TDD is a necessary but not sufficient condition for continuous delivery. |

According to Martin Fowler, **continuous integration** is 
[characterized by the following practices](https://martinfowler.com/articles/continuousIntegration.html):

| CI practice                                                       | Covered | 
| ----------------------------------------------------------------- | ------- | 
| Maintain a Single Source Repository                               | ✔      |
| Automate the Build                                                | ✔      |
| Make Your Build Self-Testing                                      | ✔      |
| Everyone Commits To the Mainline Every Day                        | ✔      |
| Every Commit Should Build the Mainline on an Integration Machine  | ✔      |
| Fix Broken Builds Immediately                                     | ±      |
| Keep the Build Fast                                               | ✔      |
| Test in a Clone of the Production Environment                     | ✗      |
| Make it Easy for Anyone to Get the Latest Executable              | ✗      |
| Everyone can see what's happening                                 | ±       |
| Automate Deployment                                               | ✔      | 

Note that when practicing katas in a dojo format, you are effectively continuously integrating 
all changes of all participants. The main difference compared to working on regular user stories 
is the lack of a build server, that performs all the checks and balances that all developers 
should actually execute already before committing any code. This way the build server acts as a 
kind of second line of defense, as it should.

## Architecture Capabilities

|     | [Architecture Capabilities](https://itrevolution.com/articles/24-key-capabilities-to-drive-improvement-in-software-delivery/#nav-2) | Covered | Explanation |
| --- | ------------------------------------------------ | ------- | ----------- |
|  9. | Use a Loosely Coupled Architecture               | ✔      | This capability is touched upon when the katas involve working with [ports and adapters](https://alistair.cockburn.us/hexagonal-architecture/), [CQRS](https://martinfowler.com/bliki/CQRS.html), and [dependency inversion](https://www.sammancoaching.org/learning_hours/testable_design/dependency_inversion_principle.html). |
| 10. | Architect for Empowered Teams                    | ✗      | This capability is not covered by any of the katas yet. |

## Product and Process Capabilities

|     | [Product and Process Capabilities](https://itrevolution.com/articles/24-key-capabilities-to-drive-improvement-in-software-delivery/#nav-3) | Covered | Explanation |
| --- | ------------------------------------------------------ | ------- | ----------- |
| 11. | Gather and Implement Customer Feedback                 | ±       | This may partially be covered e.g. in the video store kata, by asking the participants to produce a PDF statement printer after they have finished with the HTML variant. After finishing the PDF statement printer, ask them to write a CSV variant, etc. Continue to the point where they will start to complain "What do you actually need this statement format for", and grab that opportunity to teach the participants to ask that question for each and every single feature now and in the future! |
| 12. | Make the Flow of Work Visible through the Value Stream | ±       | This may partially be addressed by showing the participants the TODO list that they are encouraged to maintain while practicing the katas. In addition, you may consider using [Scrumblr](https://github.com/aliasaria/scrumblr), an instance of which you can easily start yourself [here](https://replit.com/@zwh/Scrumblr). |
| 13. | Work in Small Batches                                  | ✔      | This aspect is addressed in _all_ katas as it lies at the heart of TDD! |
| 14. | Foster and Enable Team Experimentation                 | ±       | Although this aspect isn't addressed _specifically_ by any of the katas, it is addressed _implicitly_, as the way of working practiced here contributes to the capability of a team to carry out experiments. |

## Lean Management and Monitoring Capabilities

|     | [Lean Management and Monitoring Capabilities](https://itrevolution.com/articles/24-key-capabilities-to-drive-improvement-in-software-delivery/#nav-4) | Covered | Explanation |
| --- | --------------------------------------------------------------------------- | ------- | ----------- |
| 15. | Have Lightweight Change Approval Processes                                  | ✔       | [Pair programming](https://martinfowler.com/articles/on-pair-programming.html) and/or intrateam code reviews are continuously being addressed when practicing katas in coding dojos.   |
| 16. | Monitor across Applications and Infrastructure to Inform Business Decisions | ✗       | This capability is not covered by any of the katas yet.   |
| 17. | Check System Health Proactively                                             | ✗       | This capability is not covered by any of the katas yet.   |
| 18. | Improve Processes and Manage Work with Work-In-Process (WIP) Limits         | ±        | In each and every kata, it is always emphasized to focus on one change at a time, and one change at a time only!   |
| 19. | Visualize Work to Monitor Quality and Communicate throughout the Team       | ✗       | This capability is not covered by any of the katas yet.   |

## Cultural Capabilities

|     | [Cultural Capabilities](https://itrevolution.com/articles/24-key-capabilities-to-drive-improvement-in-software-delivery/#nav-5) | Covered | Explanation |
| --- | --------------------------------------------------------------- | ------- | ----------- |
| 20. | Support a Generative Culture                          | ✔       | Almost all hallmarks of this measure such as good information flow, high cooperation, and trust, bridging between teams, and conscious inquiry are continually practiced during coding dojos, albeit only within the team (so obviously _not_ including leadership itself)   |
| 21. | Encourage and Support Learning                        | ✔       | The whole purpose of a coding dojo and its katas is to support learning!  |
| 22. | Support and Facilitate Collaboration among Teams      | ✗       | This capability is not covered by any of the katas yet.   |
| 23. | Provide Resources and Tools that Make Work Meaningful | ✔       | As this measure is about being given the tools and resources needed to do your job well, it is obviously continually being addressed by these katas.   |
| 24. | Support or Embody Transformational Leadership         | ±        | As participants need regular time to practice these katas, management needs to be informed about these activities. Viewed this way, at least one of the aspects of transformational leadership (intellectual stimulation) is a prerequisite for making coding dojos a reality.   |

## License

License: [CC-BY-SA-4.0](https://creativecommons.org/licenses/by-sa/4.0/). Attribution: [github.com/zhendrikse/tdd](https://github.com/zhendrikse/tdd).
  