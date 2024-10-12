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
class Player:
  def __init__(self, name: str):
    self.name = name
    self.purse = 0

  def add_coin(self) -> None:
    self.purse += 1
    print(repr(self) + " now has " + str(self.purse) + " Gold Coins.")

  def has_won(self) -> bool:
    return self.purse == 6

  def __repr__(self):
    return self.name
```

Finally, the `this.purses` can be removed.
</details>

## Each player his own rank

<details>
<summary>Giving each player his own rank</summary>

Move rank (`places`) out of the `Game` class into the `Player` class:

```python
class Player:
  def __init__(self, name: str):
    self.name = name
    self.purse = 0
    self.rank = 0

  def add_coin(self) -> None:
    self.purse += 1
    print(repr(self) + " now has " + str(self.purse) + " Gold Coins.")

  def has_won(self) -> bool:
    return self.purse == 6

  def add_to_rank(self, amount:int) -> None:
    self.rank += amount
    if self.rank > 11:
        self.rank -= 12
    print(repr(self) + "'s new location is " + str(self.rank))

  def __repr__(self):
    return self.name
  ```
</details>

## Each player its own penalty box status

<details>
<summary>Each player his own penalty box status</summary>

Move `inPenaltyBox` out of the `Game` class into the `Player` class. Next, note that there is no `isGettingOutOfPenaltyBox` variable for each player individually, which probably leads to the bug that once in, you'll never get out!

## Simplify `currentCategory()`

```python
def currentCategory(self) -> str:
    rank_category_map = ["Pop", "Science", "Sports", "Rock", "Pop", "Science", "Sports", "Rock", "Pop", "Science", "Sports"]
    current_player = self.players[self.currentPlayer]
    if current_player.rank <= 10:
      return rank_category_map[current_player.rank]
    else:
      return "Rock"
```
</details>

## Make questions it's own class

<details>Introduction of a <code>Questions</code> class</details>

```python
class Questions:
  def __init__(self):        
    # https://realpython.com/linked-lists-python/
    self.popQuestions = deque()
    self.scienceQuestions = deque()
    self.sportsQuestions = deque()
    self.rockQuestions = deque()
    for i in range(50):
      self.popQuestions.append("Pop Question " + str(i))
      self.scienceQuestions.append("Science Question " + str(i))
      self.sportsQuestions.append("Sports Question " + str(i))
      self.rockQuestions.append("Rock Question " + str(i))

  def currentCategory(self, index:int) -> str:
    rank_category_map = ["Pop", "Science", "Sports", "Rock", "Pop", "Science", "Sports", "Rock", "Pop", "Science", "Sports"]
    if index <= 10:
      return rank_category_map[index]
    else:
      return "Rock"
  
  def ask_question(self, index:int) -> str:
    if self.currentCategory(index) == "Pop":
        print(self.popQuestions.popleft())
    if self.currentCategory(index) == "Science":
        print(self.scienceQuestions.popleft())
    if self.currentCategory(index) == "Sports":
        print(self.sportsQuestions.popleft())
    if self.currentCategory(index) == "Rock":
        print(self.rockQuestions.popleft())
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

```python

class Players:
  def __init__(self, player1: Player, player2: Player, others:[Player] = []):
    self.players: List[Player] = []
    self.add(player1)
    self.add(player2)
    for player in others:
      self.add(player)
      
    self.currentPlayer = 0
    self.current_player = self.players[self.currentPlayer]

  def add(self, player: Player) -> bool:
    self.players.append(player)
    print(repr(player) + " was added")
    print("They are player number " + str(len(self.players)))
    return True

  def next_player(self) -> None:
    self.currentPlayer += 1
    if self.currentPlayer == len(self.players):
        self.currentPlayer = 0
    self.current_player = self.players[self.currentPlayer]
```

which simplifies the `Game` class constructor like this:

```python
class Game:
  def __init__(self, player1: Player, player2: Player, others:[Player] = []):
      self.participants: List[Players] = Players(player1, player2, others)
      self.questions = Questions()
      self.isGettingOutOfPenaltyBox: bool = False
```
</details>
