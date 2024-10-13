# Introduction

Please read the general [introduction to the bugs zero kata](../README.md) first!

## Getting started

First, create an intial Typescript 
kata set-up as described [here](https://github.com/zhendrikse/tdd/tree/master/cookiecutter).

Next, you may want to go go the newly created project directory and consult
the provided ``README.md`` in there.

## Installation of the source code

Copy the contents of the `Game` class below
into the Typescript file that resides in de source folder.

<details>
<summary>The source code for the Trivia game: the main class <code>Game</code></summary>    

```typescript

'use strict';

export class Game {
  private players = new Array<string>();
  private places = new Array<number>(6);
  private purses = new Array<number>(6);
  private inPenaltyBox = new Array<boolean>(6);

  private popQuestions = new Array<string>();
  private scienceQuestions = new Array<string>();
  private sportsQuestions = new Array<string>();
  private rockQuestions = new Array<string>();

  private currentPlayer = 0;
  private isGettingOutOfPenaltyBox = false;

  private didPlayerWin(): boolean {
    return !(this.purses[this.currentPlayer] == 6)
  };

  private currentCategory(): string {
    if (this.places[this.currentPlayer] == 0)
      return 'Pop';
    if (this.places[this.currentPlayer] == 4)
      return 'Pop';
    if (this.places[this.currentPlayer] == 8)
      return 'Pop';
    if (this.places[this.currentPlayer] == 1)
      return 'Science';
    if (this.places[this.currentPlayer] == 5)
      return 'Science';
    if (this.places[this.currentPlayer] == 9)
      return 'Science';
    if (this.places[this.currentPlayer] == 2)
      return 'Sports';
    if (this.places[this.currentPlayer] == 6)
      return 'Sports';
    if (this.places[this.currentPlayer] == 10)
      return 'Sports';
    return 'Rock';
  };

  private createRockQuestion(index: number): string {
    return "Rock Question " + index;
  };

  public constructor() {
    for (var i = 0; i < 50; i++) {
      this.popQuestions.push("Pop Question " + i);
      this.scienceQuestions.push("Science Question " + i);
      this.sportsQuestions.push("Sports Question " + i);
      this.rockQuestions.push(this.createRockQuestion(i));
    };
  }

  private isPlayable(howManyPlayers: number): boolean {
    return howManyPlayers >= 2;
  };

  public add(playerName: string) {
    this.players.push(playerName);
    this.places[this.howManyPlayers() - 1] = 0;
    this.purses[this.howManyPlayers() - 1] = 0;
    this.inPenaltyBox[this.howManyPlayers() - 1] = false;

    console.log(playerName + " was added");
    console.log("They are player number " + this.players.length);

    return true;
  };

  private howManyPlayers(): number {
    return this.players.length;
  };


  private askQuestion() {
    if (this.currentCategory() == 'Pop')
      console.log(this.popQuestions.shift());
    if (this.currentCategory() == 'Science')
      console.log(this.scienceQuestions.shift());
    if (this.currentCategory() == 'Sports')
      console.log(this.sportsQuestions.shift());
    if (this.currentCategory() == 'Rock')
      console.log(this.rockQuestions.shift());
  };

  public roll(roll: number) {
    console.log(this.players[this.currentPlayer] + " is the current player");
    console.log("They have rolled a " + roll);

    if (this.inPenaltyBox[this.currentPlayer]) {
      if (roll % 2 != 0) {
        this.isGettingOutOfPenaltyBox = true;

        console.log(this.players[this.currentPlayer] + " is getting out of the penalty box");
        this.places[this.currentPlayer] = this.places[this.currentPlayer] + roll;
        if (this.places[this.currentPlayer] > 11) {
          this.places[this.currentPlayer] = this.places[this.currentPlayer] - 12;
        }

        console.log(this.players[this.currentPlayer] + "'s new location is " + this.places[this.currentPlayer]);
        console.log("The category is " + this.currentCategory());
        this.askQuestion();
      } else {
        console.log(this.players[this.currentPlayer] + " is not getting out of the penalty box");
        this.isGettingOutOfPenaltyBox = false;
      }
    } else {

      this.places[this.currentPlayer] = this.places[this.currentPlayer] + roll;
      if (this.places[this.currentPlayer] > 11) {
        this.places[this.currentPlayer] = this.places[this.currentPlayer] - 12;
      }

      console.log(this.players[this.currentPlayer] + "'s new location is " + this.places[this.currentPlayer]);
      console.log("The category is " + this.currentCategory());
      this.askQuestion();
    }
  };

  public wasCorrectlyAnswered(): boolean {
    if (this.inPenaltyBox[this.currentPlayer]) {
      if (this.isGettingOutOfPenaltyBox) {
        console.log('Answer was correct!!!!');
        this.purses[this.currentPlayer] += 1;
        console.log(this.players[this.currentPlayer] + " now has " +
          this.purses[this.currentPlayer] + " Gold Coins.");

        var winner = this.didPlayerWin();
        this.currentPlayer += 1;
        if (this.currentPlayer == this.players.length)
          this.currentPlayer = 0;

        return winner;
      } else {
        this.currentPlayer += 1;
        if (this.currentPlayer == this.players.length)
          this.currentPlayer = 0;
        return true;
      }



    } else {

      console.log("Answer was correct!!!!");

      this.purses[this.currentPlayer] += 1;
      console.log(this.players[this.currentPlayer] + " now has " +
        this.purses[this.currentPlayer] + " Gold Coins.");

      var winner = this.didPlayerWin();

      this.currentPlayer += 1;
      if (this.currentPlayer == this.players.length)
        this.currentPlayer = 0;

      return winner;
    }
  };

  public wrongAnswer(): boolean {
    console.log('Question was incorrectly answered');
    console.log(this.players[this.currentPlayer] + " was sent to the penalty box");
    this.inPenaltyBox[this.currentPlayer] = true;

    this.currentPlayer += 1;
    if (this.currentPlayer == this.players.length)
      this.currentPlayer = 0;
    return true;
  };
};

```

</details>

You may want to rename that source folder to `game.ts` while you are at it. 
In that case, both the name of the file in the test folder needs to be
changed accordingly to `game.test.ts`, as well as its contents, of course.

# A potential approach explained in detail

## Creating a snapshot / golden master

Quite some versions of this kata come with a `GameRunner` class included.

The suggested version of such a game runner 
below fixes the seed of the random generator that 
is used to simulate the roll of a die. This becomes necessary once
we will be using the output for our snapshots.

Let's first import a random number generator

```bash
$ npm i --save-dev @types/seedrandom seedrandom
```

Next we define the `GameRunner`:

<details>
    <summary>Definition of the <code>GameRunner</code> class</summary>

```typescript
'use strict';

import { Game } from "./Game"
import seedrandom from "seedrandom";

export class GameRunner {
    private notAWinner: boolean;
    private randomNumberGenerator = seedrandom('1234');

    public constructor() {
        this.notAWinner = false;
    }

    public doRoll(): number {
        return Math.floor(this.randomNumberGenerator() * 6) + 1;
    }

    public playGame(rand: number) {
        var game = new Game();

        game.add('Chet')
        game.add('Pat')
        game.add('Sue')

        while (true) {
            game.roll(rand);

            if (Math.floor(this.randomNumberGenerator() * 10) == 7)
                this.notAWinner = game.wrongAnswer();
            else
                this.notAWinner = game.wasCorrectlyAnswered();

            if (!this.notAWinner)
                break;
        }
    }
}
```
</details>

<!--
When we run the game runner, we should see the output on the console:

```bash
$ npx ts-node src/GameRunner
``` 
-->

### Capturing the console output

We are going to capture the console output of the Trivia game to establish
a golden master. We do this using the `capture-console` library:

```bash
$ npm i --save-dev capture-console @types/capture-console
```

With this library we can capture the console output in our test
and use the `verify()` function from the approval testing library
to assert that the output has not changed.

### Installation of the approval tests library

Add the most recent version of the `approvaltests` poetry package by invoking

```bash
$ npm i --save-dev approvals
```

Next we replace the content of the test file in the `spec` directory
by the following contents:

<details>
    <summary>Capturing the output from the console</summary>
    
```typescript
'use strict';

import { GameRunner } from "../src/GameRunner"
import { verify, verifyAsJson } from "approvals/lib/Providers/Jest/JestApprovals";

describe("A new Trivia", function () {
  it("is successfully created", function () {
    var gameRunner = new GameRunner()

    const capcon = require('capture-console');

    let stdout = "";
    stdout = capcon.captureStdout(() => {
      gameRunner.playGame(gameRunner.doRoll());
    });

    verify(stdout);
  })
})
```

</details>

Now we can run the test by invoking

```bash
$ npm run test
```

This should give our first snapshot! 

### !Caveat when working with Jest!

As of this writing, Jest 'decorates' the console output in such a way,
that it makes it unsuitable for creating our golden master.

In order to remove the 'decorations' that are added by Jest, modify
the tests so that they use the standard console instead of the Jest
console, like so:

```typescript
'use strict';

import { GameRunner } from "../src/GameRunner"
import { verify, verifyAsJson } from "approvals/lib/Providers/Jest/JestApprovals";

const jestConsole = console;


describe("A new Trivia", function () {
  beforeEach(() => {
    global.console = require('console');
  });

  afterEach(() => {
    global.console = jestConsole;
  });

  it("is successfully created", function () {
    var gameRunner = new GameRunner()

    const capcon = require('capture-console');

    let stdout = "";
    stdout = capcon.captureStdout(() => {
      gameRunner.playGame(gameRunner.doRoll());
    });

    verify(stdout);
  })
})
```

## Always at least two players

Note that the method `is_playable()` is never used!

### Statically enforcing at least two players

<details>
<summary>Enforce two players by modifying the constructor</summary>

```typescript
  public constructor(player1: string, player2: string, players: string[] = []) {
    for (var i = 0; i < 50; i++) {
      this.popQuestions.push("Pop Question " + i);
      this.scienceQuestions.push("Science Question " + i);
      this.sportsQuestions.push("Sports Question " + i);
      this.rockQuestions.push(this.createRockQuestion(i));
    };

    this.add(player1);
    this.add(player2);
    players.forEach(player => this.add(player));
  }
```
</details>

## Each player his own purse

<details>
<summary>Introduction of a <code>Player</code> class</summary>

First step, introduce a `Player` class like so:
```typescript
export class Player {
  private name: string;

  constructor(name: string) {
    this.name = name;
  }

  public toString(): string {
    return this.name;
  }
}
```

Make the changes in the code accordingly. It is necessary to wrap all print statements like so:
```typescript 
print(player.toString() + " was added")
```

Next, give each player his/her own purse:

```typescript
export class Player {
  private name: string;
  private purse: number;

  constructor(name: string) {
    this.name = name;
    this.purse = 0;
  }

  public addCoin() {
    this.purse += 1
    console.log(this.name + " now has " + this.purse + " Gold Coins.");
  }

  public hasWon(): boolean {
    return this.purse == 6
  }

  public toString(): string {
    return this.name;
  }
}
```

Finally, the `this.purses` can be removed.
</details>

## Each player his own rank

<details>
<summary>Giving each player his own rank</summary>

Move rank (`places`) out of the `Game` class into the `Player` class:

```typescript
export class Player {
  private name: string;
  private purse: number;
  private rank: number;

  constructor(name: string) {
    this.name = name;
    this.purse = 0;
    this.rank = 0;
  }

  public addCoin() {
    this.purse += 1
    console.log(this.name + " now has " + this.purse + " Gold Coins.");
  }

  public hasWon(): boolean {
    return this.purse == 6
  }

  public addToRank(amount: number) {
    this.rank += amount
    if (this.rank > 11)
        this.rank -= 12
    console.log(this.name + "'s new location is " + this.rank);
  }

  public currentCategory(): string {
    const rank_category_map = ["Pop", "Science", "Sports", "Rock", "Pop", "Science", "Sports", "Rock", "Pop", "Science", "Sports"]
    if (this.rank <= 10)
      return rank_category_map[this.rank]
    else
      return "Rock"
  }

  public toString(): string {
    return this.name;
  }
}
```

</details>

## Each player its own penalty box status

<details>
<summary>Each player his own penalty box status</summary>

Move `inPenaltyBox` out of the `Game` class into the `Player` class. Next, note that there is no `isGettingOutOfPenaltyBox` variable for each player individually, which probably leads to the bug that once in, you'll never get out!

```typescript
export class Player {
  private name: string;
  private purse: number;
  private rank: number;
  private inPenaltyBox: boolean;

  constructor(name: string) {
    this.name = name;
    this.purse = 0;
    this.rank = 0;
    this.inPenaltyBox = false;
  }

  // ...

  public goToInPenaltyBox() {
    this.inPenaltyBox = true;
  }

  public isInPenaltyBox(): boolean {
    return this.inPenaltyBox;
  }
```

</details>

## Make questions it's own class

<details>
<summary>Introduction of a <code>Questions</code> class</summary>

```typescript
export class Questions {
  private popQuestions = new Array<string>();
  private scienceQuestions = new Array<string>();
  private sportsQuestions = new Array<string>();
  private rockQuestions = new Array<string>();

  public constructor() {
    for (var i = 0; i < 50; i++) {
      this.popQuestions.push("Pop Question " + i);
      this.scienceQuestions.push("Science Question " + i);
      this.sportsQuestions.push("Sports Question " + i);
      this.rockQuestions.push("Rock Question " + i);
    }
  }

  public getPopQuestion(): string {
    return this.popQuestions.shift()!;
  }

  public getRockQuestion(): string {
    return this.rockQuestions.shift()!;
  }

  public getScienceQuestion(): string {
    return this.scienceQuestions.shift()!;
  }

  public getSportsQuestion(): string {
    return this.sportsQuestions.shift()!;
  }
}
```
</details>

Next, the `askQuestion()` method could and should be moved into the `Player` class:

<details>Moving the `askQuestion()` method into the Player class<details>

```typescript
  public askQuestion(questions: Questions) {
    if (this.currentCategory() == 'Pop')
      console.log(questions.getPopQuestion());
    if (this.currentCategory() == 'Science')
      console.log(questions.getScienceQuestion());
    if (this.currentCategory() == 'Sports')
      console.log(questions.getSportsQuestion());
    if (this.currentCategory() == 'Rock')
      console.log(questions.getRockQuestion());
  }
```

</details>
  
## Fix bug coins credited to wrong player

<details>
<summary>Fixing the coins being credited to the wrong player</summary>

Apply the DRY principle to the logic to determine the next player:

```python
def next_player(self) -> None:
  self.currentPlayer += 1
  if self.currentPlayer == len(self.players):
      self.currentPlayer = 0
```

Now you see that in `was_correctly_answered(self)` coins can be credited to a wrong player, as the next player is determined _first_ after which the coins are credited.
</details>

## Create a Players class

<details>
<summary>Introduction of a class with a list of players</summary>

```typescript
class Players {
  private players = new Array<Player>();

  private current = 0;

  public constructor(player1: Player, player2: Player, players: Player[] = []) {
    this.add(player1);
    this.add(player2);
    players.forEach(player => this.add(player));
  }

  public nextPlayersTurn() {
    this.current += 1;
    if (this.current == this.players.length)
      this.current = 0;
  }

  private add(player: Player) {
    this.players.push(player);
    console.log(player.toString() + " was added");
    console.log("They are player number " + this.players.length);
  };

  public currentPlayer(): Player {
    return this.players[this.current];
  }
}
```

</details>
