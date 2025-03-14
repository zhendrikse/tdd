# Introduction

Please read the general [introduction to the bugs zero kata](../README.md) first!

## Getting started

First, create an intial Python kata set-up as described [here](https://github.com/zhendrikse/tdd/tree/master/cookiecutter).
Make sure you enable code coverage by correctly setting the associated option, 
as we will be using code coverage to create a comprehensive snapshot.

Next, you may want to go go the newly created project directory and consult
the provided ``README.md`` in there.

## Installation of the source code

Copy the contents of the `Game` class below
into the Python file that resides in de source folder.

<details>
<summary>The source code for the Trivia game: the main class <code>Game</code></summary>    

```python
class Game:
    def __init__(self):
        self.players = []
        self.places = [0] * 6
        self.purses = [0] * 6
        self.in_penalty_box = [0] * 6

        self.pop_questions = []
        self.science_questions = []
        self.sports_questions = []
        self.rock_questions = []

        self.current_player = 0
        self.is_getting_out_of_penalty_box = False

        for i in range(50):
            self.pop_questions.append("Pop Question %s" % i)
            self.science_questions.append("Science Question %s" % i)
            self.sports_questions.append("Sports Question %s" % i)
            self.rock_questions.append(self.create_rock_question(i))

    def create_rock_question(self, index):
        return "Rock Question %s" % index

    def is_playable(self):
        return self.how_many_players >= 2

    def add(self, player_name):
        self.players.append(player_name)
        self.places[self.how_many_players] = 0
        self.purses[self.how_many_players] = 0
        self.in_penalty_box[self.how_many_players] = False

        print(player_name + " was added")
        print("They are player number %s" % len(self.players))

        return True

    @property
    def how_many_players(self):
        return len(self.players)

    def roll(self, roll):
        print("%s is the current player" % self.players[self.current_player])
        print("They have rolled a %s" % roll)

        if self.in_penalty_box[self.current_player]:
            if roll % 2 != 0:
                self.is_getting_out_of_penalty_box = True

                print("%s is getting out of the penalty box" % self.players[self.current_player])
                self.places[self.current_player] = self.places[self.current_player] + roll
                if self.places[self.current_player] > 11:
                    self.places[self.current_player] = self.places[self.current_player] - 12

                print(self.players[self.current_player] + \
                            '\'s new location is ' + \
                            str(self.places[self.current_player]))
                print("The category is %s" % self._current_category)
                self._ask_question()
            else:
                print("%s is not getting out of the penalty box" % self.players[self.current_player])
                self.is_getting_out_of_penalty_box = False
        else:
            self.places[self.current_player] = self.places[self.current_player] + roll
            if self.places[self.current_player] > 11:
                self.places[self.current_player] = self.places[self.current_player] - 12

            print(self.players[self.current_player] + \
                        '\'s new location is ' + \
                        str(self.places[self.current_player]))
            print("The category is %s" % self._current_category)
            self._ask_question()

    def _ask_question(self):
        if self._current_category == 'Pop': print(self.pop_questions.pop(0))
        if self._current_category == 'Science': print(self.science_questions.pop(0))
        if self._current_category == 'Sports': print(self.sports_questions.pop(0))
        if self._current_category == 'Rock': print(self.rock_questions.pop(0))

    @property
    def _current_category(self):
        if self.places[self.current_player] == 0: return 'Pop'
        if self.places[self.current_player] == 4: return 'Pop'
        if self.places[self.current_player] == 8: return 'Pop'
        if self.places[self.current_player] == 1: return 'Science'
        if self.places[self.current_player] == 5: return 'Science'
        if self.places[self.current_player] == 9: return 'Science'
        if self.places[self.current_player] == 2: return 'Sports'
        if self.places[self.current_player] == 6: return 'Sports'
        if self.places[self.current_player] == 10: return 'Sports'
        return 'Rock'

    def was_correctly_answered(self):
        if self.in_penalty_box[self.current_player]:
            if self.is_getting_out_of_penalty_box:
                print('Answer was correct!!!!')
                self.purses[self.current_player] += 1
                print(self.players[self.current_player] + \
                    ' now has ' + \
                    str(self.purses[self.current_player]) + \
                    ' Gold Coins.')

                winner = self._did_player_win()
                self.current_player += 1
                if self.current_player == len(self.players): self.current_player = 0

                return winner
            else:
                self.current_player += 1
                if self.current_player == len(self.players): self.current_player = 0
                return True



        else:

            print("Answer was corrent!!!!")
            self.purses[self.current_player] += 1
            print(self.players[self.current_player] + \
                ' now has ' + \
                str(self.purses[self.current_player]) + \
                ' Gold Coins.')

            winner = self._did_player_win()
            self.current_player += 1
            if self.current_player == len(self.players): self.current_player = 0

            return winner

    def wrong_answer(self):
        print('Question was incorrectly answered')
        print(self.players[self.current_player] + " was sent to the penalty box")
        self.in_penalty_box[self.current_player] = True

        self.current_player += 1
        if self.current_player == len(self.players): self.current_player = 0
        return True

    def _did_player_win(self):
        return not (self.purses[self.current_player] == 6)
```
</details>

You may want to rename that source folder to `game.py` while you are at it. 
In that case, both the name of the file in the test folder needs to be
changed accordingly to `game_test.py`, as well as its contents, of course.

## Installation of the approval tests library

Add the most recent version of the `approvaltests` poetry package by invoking

```bash
$ poetry add approvaltests
```

# A potential approach explained in detail

## Creating a snapshot / golden master

Quite some versions of this kata come with a `GameRunner` class included.

The suggested version of such a game runner 
below fixes the seed of the random generator that 
is used to simulate the roll of a die. This becomes necessary once
we will be using the output for our snapshots.

<details>
    <summary>Definition of the <code>GameRunner</code> class</summary>

```python
from random import seed, randrange
from game import Game


class GameRunner:
    def __init__(self):
        self.not_a_winner = False

    @staticmethod
    def main():
        game = GameRunner()
        seed(30)
        game.play_game(randrange(5) + 1)

    def play_game(self, rand:int) -> None:
        game = Game()

        game.add('Chet')
        game.add('Pat')
        game.add('Sue')

        while True:
            game.roll(rand)

            if randrange(9) == 7:
                self.not_a_winner = game.wrong_answer()
            else:
                self.not_a_winner = game.was_correctly_answered()

            if not self.not_a_winner:
                break


if __name__ == '__main__':
    GameRunner.main()
```
</details>

When we run the game runner, we should see the output on the console:

```bash
$ python3 src/game_runner.py
``` 

### Capturing the console output

We capture the console output of a function with a little trick:

<details>
    <summary>Capturing the output from the console</summary>
    
```python
import io
from contextlib import redirect_stdout
from approvaltests.approvals import verify
from game_runner import GameRunner


class TestGame:
  def catch_output(self, func):
    result = io.StringIO()
    with redirect_stdout(result):
        func()
    return result.getvalue()

  def test_trivia_game(self):
    output = self.catch_output(GameRunner.main)
    verify(output)
```
</details>

This should give our first snapshot! By modifying the invocation of `pytest`
a little bit, we also get a coverage report

```bash
PYTHONPATH=src poetry run pytest --cov-report html --cov=game test/game_test.py
```


## Always at least two players

Note that the method `is_playable()` is never used!

### Statically

<details>
<summary>Enforce two players by modifying the constructor</summary>

```python
  def __init__(self, player1: str, player2: str, others:[str] = []):
    ...
            
    self.add(player1)
    self.add(player2)
    for player in others:
      self.add(player)
```
</details>

## Each player his own purse

<details>
<summary>Introduction of a <code>Player</code> class</summary>

First step, introduce a `Player` class like so:
```python
class Player:
  def __init__(self, name: str):
    self.name = name

  def __repr__(self):
    return self.name
```

Make the changes in the code accordingly. It is necessary to wrap all print statements like so:
```python 
print(repr(player) + " was added")
```

Next, give each player his/her own purse:

```python
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

Finally, the `self.purses` can be removed.
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
