## Always at least two players

Note that the method `is_playable()` is never used!

### Statically

Enforce it by modifying the constructor like so:

```python
  def __init__(self, player1: str, player2: str, others:[str] = []):
    ...
            
    self.add(player1)
    self.add(player2)
    for player in others:
      self.add(player)
```

## Each player his own purse

First step, introduce a Player class like so:
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

## Each player his own rank

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

## Each player its own penalty box status

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

## Make questions it's own class

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
  
## Fix bug coins credited to wrong player

Apply the DRY principle to the logic to determine the next player:

```python
def next_player(self) -> None:
  self.currentPlayer += 1
  if self.currentPlayer == len(self.players):
      self.currentPlayer = 0
```

Now you see that in `was_correctly_answered(self)` coins can be credited to a wrong player, as the next player is determined _first_ after which the coins are credited.

## Create a Players class

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