# Kata overview

![Clojure build](https://img.shields.io/github/actions/workflow/status/zhendrikse/tdd/clojure.yml?label=Clojure%20katas)
![Python build](https://img.shields.io/github/actions/workflow/status/zhendrikse/tdd/python.yml?label=Python%20katas)
![Nodejs build](https://img.shields.io/github/actions/workflow/status/zhendrikse/tdd/node.js.yml?label=NodeJS%20katas)
![Java/Kotlin build](https://img.shields.io/github/actions/workflow/status/zhendrikse/tdd/gradle.yml?label=Java%2FKotlin%20katas)
![.Net build](https://img.shields.io/github/actions/workflow/status/zhendrikse/tdd/dotnet.yml?label=.NET%20katas)

This section summarizes details of all katas contained in this repository.
It includes both a difficulty level as well as a list of topics (per kata) 
that are being targeted.
Difficulties range from low (**L**) &rarr; medium (**M**) &rarr; high (**H**).
  
| Kata                                            | Ranking | Aspects                                               | Py | Java | JS | Clj | Kt | TS | C# |
| ----------------------------------------------- | ------- | ----------------------------------------------------- |:--:|:----:|:--:|:---:|:--:|:--:|:--:|
| [audio-player-kata](./audio-player-kata)        | M       | London vs. Detroit schools of TDD / Mocks, spies      | ✗  | ✗   | ✔  | ✗   | ✗  | ✗ | ✗ |
| [babysteps-timer](./babysteps-timer)            | H       | **Refactoring front-end legacy** / Baby steps TDD     | ✗  | ✗   | ✗  | ✗   | ✗  | ✔ | ✗ |
| [bugs-zero-kata](./bugs-zero-kata)              | M       | **Legacy code** / **Refactoring** / Approval tests    | ✔  | ✗   | ✗  | ✗   | ✗  | ✗ | ✗ |
| [cache-kata](./cache-kata)                      | L       | Verification of state versus behavior                 | ✔  | ✗   | ✗  | ✗   | ✗  | ✗ | ✗ |
| [christmas-tree](./christmas-tree)              | L       | Implement an algorithm in **small steps**             | ✔  | ✗   | ✗  | ✗   | ✗  | ✗ | ✗ |
| [connect-four](./connect-four)                  | H       | Implement a game in **small steps**                   | ✔  | ✗   | ✗  | ✔   | ✗  | ✗ | ✗ |
| [countries-kata](./countries-kata)              | L / M   | Ports &amp; adapters / **Refactoring** / REST / DI    | ✔  | ✗   | ✔  | ✗   | ✗  | ✔ | ✗ |
| [cqrs-booking](./cqrs-booking)                  | H       | CQRS / DDD / Event-based architecture                 | ✗  | ✔   | ✗  | ✗   | ✗  | ✗ | ✗ |
| [db-adapter-kata](./db-adapter-kata)            | M       | Ports &amp; adapters / Database / DI                  | ✔  | ✗   | ✗  | ✗   | ✗  | ✗ | ✗ |
| [elephant-carpaccio](./elephant-carpaccio)      | M       | Slicing user stories                                  | ✗  | ✔   | ✗  | ✗   | ✗  | ✗ | ✗ |
| [fibonacci-kata](./db-adapter-kata)             | M       | Pipelines / Automated deployments / IaC               | ✔  | ✗   | ✗  | ✗   | ✗  | ✗ | ✗ |
| [game-of-life](./game-of-life)                  | M       | **Generic TDD** / **Small steps**                     | ✔  | ✔   | ✗  | ✔   | ✗  | ✗ | ✗ |
| [gilded-rose-kata](./gilded-rose-kata)          | M / H   | **Legacy code** / **Refactoring** / Approval tests    | ✔  | ✗   | ✔  | ✗   | ✗  | ✗ | ✗ |
| [greed-kata](./greed-kata)                      | M       | Implement complex rules in **small steps**            | ✗  | ✗   | ✗  | ✔   | ✗  | ✗ | ✗ |
| [locker-room-kata](./locker-room-kata)          | M       | Stateless / Functional programming                    | ✗  | ✗   | ✗  | ✔   | ✔  | ✗ | ✗ |
| [manhattan-distance](./manhattan-distance)      | L       | 1, 2, N / Encapsulation                               | ✔  | ✗   | ✗  | ✗   | ✗  | ✗ | ✗ |
| [mars-rover](./mars-rover)                      | M       | **Generic TDD** / Design decisions                    | ✔  | ✗   | ✗  | ✗   | ✗  | ✗ | ✔ |
| [poker-hands-kata](./poker-hands-kata)          | H       | Outside-in / Mocks / Design decisions                 | ✔  | ✗   | ✗  | ✔   | ✗  | ✗ | ✗ |
| [questionnaire-kata](./questionnaire-kata)      | M       | Data science / Dashboarding / Ports &amp; adapters    | ✔  | ✗   | ✗  | ✗   | ✗  | ✗ | ✗ |
| [report-generator-kata](./report-generator-kata)| L / M   | **Refactoring** / SOLID / Code smells / Clean code    | ✔  | ✗   | ✗  | ✗   | ✗  | ✗ | ✗ |
| [registration-form](./registration-form)        | L / M   | **Generic TDD** / Front-end TDD / Custom matchers     | ✗  | ✗   | ✔  | ✗   | ✗  | ✗ | ✗ |
| [shunting-yard-algo](./shunting-yard-algo)      | M       | **Generic TDD**                                       | ✗  | ✗   | ✗  | ✗   | ✗  | ✗ | ✔ |
| [stack-kata](./stack-kata)                      | L       | Getting started with TDD (**small steps**)            | ✔  | ✔   | ✔  | ✗   | ✗  | ✔ | ✗ |
| [sudoku-kata](./sudoku-kata)                    | M       | Recursion, TDD and **small steps**                    | ✔  | ✔   | ✗  | ✔   | ✗  | ✗ | ✗ |
| [task-list-kata](./task-list-kata)              | M       | Command-Query / Strong typing / Realistic app         | ✔  | ✗   | ✗  | ✗   | ✗  | ✗ | ✗ |
| [tell-dont-ask](./tell-dont-ask)                | M       | **Refactoring** / Anemic domain model / DDD           | ✔  | ✔   | ✗  | ✗   | ✗  | ✗ | ✔ | 
| [tire-pressure-kata](./tire-pressure-kata)      | L       | Ports &amp; adapters / **Testable design** / DI       | ✔  | ✗   | ✗  | ✗   | ✗  | ✗ | ✗ | 
| [train-reservation](./train-reservation)        | M       | Example mapping / Double loop TDD / Test doubles      | ✔  | ✗   | ✗  | ✗   | ✗  | ✗ | ✔ | 
| [vending-machine](./vending-machine)            | L / M   | **Small steps** / Code smells and **refactoring**     | ✔  | ✔   | ✔  | ✗   | ✔  | ✔ | ✔ |
| [video-store-kata](./video-store-kata)          | L       | **Legacy code** / Code smells and **refactoring**     | ✔  | ✔   | ✔  | ✗   | ✗  | ✔ | ✗ |

## License
  
Shield: [![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

This work is licensed under a
[CC-BY-SA-4.0 license](https://creativecommons.org/licenses/by-sa/4.0/). Attribution: [github.com/zhendrikse/tdd](https://github.com/zhendrikse/tdd).

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg
  
