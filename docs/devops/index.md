{% include breadcrumbs.html %}

# Relation of the katas with the 24 Key Capabilities
<div class="header_line"><br/></div>

This page elaborates on the relationship between 
[the topics that are practiced in the katas](https://github.com/zhendrikse/tdd/tree/master/tdd-katas#readme)
and the 
[24 Key Capabilities to Drive Improvement in Software Delivery](https://itrevolution.com/articles/24-key-capabilities-to-drive-improvement-in-software-delivery/).

The 24 key capabilities are divided into a couple of subcategories. 
Each category has its own table. The columns with the checkmarks and 
crosses indicate which of the capabilities are covered by the coding 
katas. A plus-minus sign indicates partial coverage.

The picture below illustrates how improvements in either of these 24 capabilities 
enhance organizational performance, which in turn can be measured using the 
[DORA metrics](https://cloud.google.com/blog/products/devops-sre/using-the-four-keys-to-measure-your-devops-performance).
The original picture was created by 
[Rob Westgeest](https://www.qwan.eu/#team) and has been recreated in 
[Excalidraw](https://excalidraw.com/). 

![Organizational health](https://github.com/zhendrikse/tdd/blob/master/assets/organizational-health.png?raw=true)

Note that this is a capability model, [_not_ a maturity model](https://octopus.com/blog/devops-uses-capability-not-maturity)! 
It is crucial that the team (together with the coach) 
continually reassess its proficiency in order to determine which improvements on which 
capabilities will result in the greatest return on investment.

# Intermezzo: The attraction of maturity models as the lure of the Sirens

Personally, I have never really understood the appeal of the various and seemingly ubiquitous maturity models, if only because of their inherent pejorative connotation: as if a team is still in some kind of infantile phase. They need to come out of it, under the watchful eye of a trainer/coach, in order to eventually reach a certain imposed level of maturity. What a nice way to start as a coach.

How great was the celebration of recognition when I started reading the now-famous book Accelerate, where I came across a little rant about these maturity models on pages six and seven. Instead, the book recommends what it calls capability models, in which improvements in a set of capabilities are continuously sought in an iterative way.

The book states that maturity models are characterized by:

- Providing a context-independent answer
- Emphasizing a fixed partial result/maturity level
- Encouraging standards rather than experimentation and innovation
- Assuming a linear progression

The superiority of capability models therefore lies in the fact that they:

- Commit to continuous improvement
- Are based on the measurement of outcomes (e.g. DORA metrics)
- Are dynamic, adaptive and multi-dimensional
- Address an ever-changing and evolving environment/market

Ideally, the coach's craft is to iteratively determine with the team which capability (or set of capabilities) they can best develop in order to continuously achieve the most profitable improvement at that time  (for fun, compare this to the Toyota improvement kata).

In short: because of their KPI-like nature, maturity models seem to exert a powerful attraction on many organizations: the seductive but at the same time fatal call of the Sirens. Hopefully, it is clear that only capability models are truly compatible with agile thinking, and that maturity models are at odds with it.

# Coverage of the 24 key capabilities by practicing the katas

## Continuous Delivery Capabilities

The table below lists the coverage of the [Continuous Delivery capabilities](https://itrevolution.com/articles/24-key-capabilities-to-drive-improvement-in-software-delivery/#nav-1).
  
| Capability                                       | Covered | Explanation |
| ------------------------------------------------ | ------- | ----------- |
| Use Version Control for all Production Artifacts | ✔      | You may always opt to use a version control system when practicing your katas. When katas are done in a group in a [randori style](https://codingdojo.org/practices/RandoriKata/), a commit by the person(s) ending his/her/their turn and a subsequent pull by the next may be used to pass the code on. |
| Automate Your Deployment Process                 | ✔      | This capability is covered by the Fibonacci kata. |
| Implement Continuous Integration                 | ±       | Continuous integration is elaborated on directly below this table |
| Use Trunk-Based Development Methods              | ✔      | Trunk-based development can easily be simulated when katas are done in a group in a [randori style](https://codingdojo.org/practices/RandoriKata/), a commit by the person(s) ending his/her/their turn and a subsequent pull by the next may be used to pass the code on. |
| Implement Test Automation                        | ✔      | Obviously, this is what lies at the heart of TDD. Note that integration testing is also touched upon when the katas involve working with [ports and adapters](https://alistair.cockburn.us/hexagonal-architecture/). Even more so, many katas address the subject of creating a testable design, and/or address techniques for making legacy code testable. |
| Support Test Data Management                     | ✗      | This capability is not covered by any of the katas yet |
| Shift Left on Security                           | ✗      | This capability is not covered by any of the katas yet |
| Implement Continuous Delivery                    | ✔       | When the skills and heuristics of TDD are correctly and properly applied all of the time, it should be no problem for a team to go to production at any given time. This is one of the hallmarks of continuous delivery! So TDD is a necessary but not sufficient condition for continuous delivery. |

All [aspects belonging to the "Implement Continuous Integration" capability](https://martinfowler.com/articles/continuousIntegration.html) are outlined
separately in the table below.

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

The table below lists the coverage of the [architecture capabilities](https://itrevolution.com/articles/24-key-capabilities-to-drive-improvement-in-software-delivery/#nav-2).
  
| Capability                                       | Covered | Explanation |
| ------------------------------------------------ | ------- | ----------- |
| Use a Loosely Coupled Architecture               | ✔      | This capability is touched upon when the katas involve working with [ports and adapters](https://alistair.cockburn.us/hexagonal-architecture/), [CQRS](https://martinfowler.com/bliki/CQRS.html), and [dependency inversion](https://www.sammancoaching.org/learning_hours/testable_design/dependency_inversion_principle.html). |
| Architect for Empowered Teams                    | ✗      | This capability is not covered by any of the katas yet. |

## Product and Process Capabilities

The table below lists the coverage of the [product and process capabilities](https://itrevolution.com/articles/24-key-capabilities-to-drive-improvement-in-software-delivery/#nav-3).

| Capability                                             | Covered | Explanation |
| ------------------------------------------------------ | ------- | ----------- |
| Gather and Implement Customer Feedback                 | ±       | This may partially be covered e.g. in the video store kata, by asking the participants to produce a PDF statement printer after they have finished with the HTML variant. After finishing the PDF statement printer, ask them to write a CSV variant, etc. Continue to the point where they will start to complain "What do you actually need this statement format for", and grab that opportunity to teach the participants to ask that question for each and every single feature now and in the future! |
| Make the Flow of Work Visible through the Value Stream | ±       | This may partially be addressed by showing the participants the TODO list that they are encouraged to maintain while practicing the katas. In addition, you may consider using [Scrumblr](https://github.com/aliasaria/scrumblr), an instance of which you can easily start yourself [here](https://replit.com/@zwh/Scrumblr). |
| Work in Small Batches                                  | ✔      | This aspect is addressed in _all_ katas as it lies at the heart of TDD! |
| Foster and Enable Team Experimentation                 | ±       | Although this aspect isn't addressed _specifically_ by any of the katas, it is addressed _implicitly_, as the way of working practiced here contributes to the capability of a team to carry out experiments. |

## Lean Management and Monitoring Capabilities

The table below lists the coverage of the [lean management and monitoring capabilities](https://itrevolution.com/articles/24-key-capabilities-to-drive-improvement-in-software-delivery/#nav-4).

| Capability                                                                  | Covered | Explanation |
| --------------------------------------------------------------------------- | ------- | ----------- |
| Have Lightweight Change Approval Processes                                  | ✔       | [Pair programming](https://martinfowler.com/articles/on-pair-programming.html) and/or intrateam code reviews are continuously being addressed when practicing katas in coding dojos.   |
| Monitor across Applications and Infrastructure to Inform Business Decisions | ✗       | This capability is not covered by any of the katas yet.   |
| Check System Health Proactively                                             | ✗       | This capability is not covered by any of the katas yet.   |
| Improve Processes and Manage Work with Work-In-Process (WIP) Limits         | ±        | In each and every kata, it is always emphasized to focus on one change at a time, and one change at a time only!   |
|  Visualize Work to Monitor Quality and Communicate throughout the Team       | ✗       | This capability is not covered by any of the katas yet.   |

## Cultural Capabilities

The table below lists the coverage of the [cultural capabilities](https://itrevolution.com/articles/24-key-capabilities-to-drive-improvement-in-software-delivery/#nav-5).

| Capability                                            | Covered | Explanation |
| ----------------------------------------------------- | ------- | ----------- |
| Support a Generative Culture                          | ✔       | Almost all hallmarks of this measure such as good information flow, high cooperation, and trust, bridging between teams, and conscious inquiry are continually practiced during coding dojos, albeit only within the team (so obviously _not_ including leadership itself)   |
| Encourage and Support Learning                        | ✔       | The whole purpose of a coding dojo and its katas is to support learning!  |
| Support and Facilitate Collaboration among Teams      | ✗       | This capability is not covered by any of the katas yet.   |
| Provide Resources and Tools that Make Work Meaningful | ✔       | As this measure is about being given the tools and resources needed to do your job well, it is obviously continually being addressed by these katas.   |
| 24. Support or Embody Transformational Leadership         | ±        | As participants need regular time to practice these katas, management needs to be informed about these activities. Viewed this way, at least one of the aspects of transformational leadership (intellectual stimulation) is a prerequisite for making coding dojos a reality.   |

  

