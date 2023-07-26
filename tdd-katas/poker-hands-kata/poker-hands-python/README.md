# Introduction

Please read the general [introduction to the poker hands kata](../README.md) first!

# Getting started

First, create an intial Python kata set-up as described [here](https://github.com/zhendrikse/tdd/tree/master/cookiecutter).

Next, go the the newly created project directory and consult
the provided ``README.md`` in there.

# Implementation

Before we start with the implementation, let's first consider a couple of design decisions that we would otherwise would have to make along the way.

## Design considerations

First off, we need to be able to rank the above poker sets/rules. This can be achieved by assigning integer values to these sets. This can best been done using an enumeration
in a  `poker_ranks.py` file

```python
from enum import Enum

class PokerRanks(Enum):
    STRAIGHT_FLUSH = 8
    FOUR_OF_A_KIND = 7
    FULL_HOUSE = 6
    FLUSH = 5
    STRAIGHT = 4
    THREE_OF_A_KIND = 3
    TWO_PAIR = 2
    TWO_OF_A_KIND = 1
    ONE_OF_A_KIND = 0
``` 

### Dealing with the cards

In addition, we'll need to rank the individual cards a well. Individual cards will be denoted by a rank and a suit, so for example "TC" (club 10), "JD" (diamond jack), etc. A hand can then be represented by 

```python
Hand("TC TH TD TS 3S".split())
``` 

where we strongly recommend to move the `split()` into the constructor.

Individual cards may then easily be ranked by simply ignoring the suit and mapping all cards to integer values like so: 
- 2 &rarr; 2, 
- 3 &rarr; 3, 
- ..., 
- Ten &rarr; 10,
- Jack &rarr; 11, 
- Queen &rarr; 12, 
- King &rarr; 13, 
- Ace &rarr; 14.

Thus, we are going to need a function that maps cards (strings) such as ``"TC"``, ``"JD"``, and ``"3S"`` to one of these integer values.

### Ranking the hands

Suppose e.g. one hand to contain "9 9 9 9 5" and the other "3 3 3 3 2". As is argued in the course [Design of Computer Programs](https://www.udacity.com/course/design-of-computer-programs--cs212), the best way to represent the ranking is to use tuples:

- **Four of a kind**: "9 9 9 9 5" &rarr; _(7, 9, 5)_ 
- **Four of a kind**: "3 3 3 3 2" &rarr; _(7, 3, 2)_

The first integer in the tuple represents the ranking from the enumeration in `poker_ranks.py`. The second integer represents the highest card, so that we can break ties. The last integer represents the remaining card. 

For the other poker combinations, it may happen that the highest card cannot be used to disambiguate a tie, in which case we'll use the complete deck.

So let's summarize how we are going to uniquely associate a tuple to each hand (where suits have been omitted) that allows us to rank a hand:
- **Straight flush**: "11 10 9 8 7" & same suit &rarr; _(8, 11)_
- **Four of a kind**: "14 14 14 14 12" &rarr; _(7, 14, 12)_
- **Full house**: "8 8 8 13 13" &rarr; _(6, 8, 13)_
- **Flush**: "10 8 7 5 3" & same suit &rarr; _(5, [10, 8, 7, 5, 3])_
- **Straight**: "11 10 9 8 7" &rarr; _(4, 11)_
- **Three of a kind**: "7 7 7 5 2" &rarr; _(3, 7, [7, 7, 7, 5, 2])_
- **Two pairs**: "11, 11, 3, 3, 13" &rarr; _(2, 11, 3, [13, 11, 11, 3, 3])_
- **Two of a kind**: "2 2 11 6 3" &rarr; _(1, 2, [11, 6, 3, 2, 2])_
- **One of a kind**: "7 5 4 3 2" &rarr; _(0, [7, 5, 4, 3, 2])_

Note that the Python language offers us the added benefit of being able to compare such tuples by default, e.g. `(7, 9, 5) > (7, 3, 2)` is valid in Python. By default it compares the first entries, if that's still true, the second entries, and so forth till all entries have been compared.


## Behaviour on empty set of hands

We start by defining the behaviour for an empty set of hands.
```python
with description('Given an empty set of hands'):
  with it('raises an exception'):
    expect(lambda: determine_best_hand([])) \
      .to(raise_error(IllegalArgumentsException))
```

This is implemented by
```python
def determine_best_hand(hands):
  if len(hands) == 0:
    raise IllegalArgumentsException()
```

and defining the `IllegalArgumentsException`
```python
class IllegalArgumentsException(Exception):
    pass
```

## Behaviour on a set consisting of a single hand

Let's define the behaviour for a single hand:
```python
with context("Given a straight flush hand"):
  with it('returns the one and only hand as winner'):
    straight_flush = Hand("6C 7C 8C 9C TC")
    hands = [straight_flush]
    expect(determine_best_hand(hands)).to(equal(straight_flush))
```

This is implemented by
```python
def determine_best_hand(hands):
  if len(hands) == 0:
    raise IllegalArgumentsException()
  elif len(hands) == 1:
    return hands[0]
```

and a `Hand` class
```python
class Hand:
  def __init__(self, cards):
    self.cards = cards
```

---
#### Exercise

Refactor the `Hand` class so that the `split()` function is moved into the constructor. Next, assure that a poker hand always has five cards:

```python
with description(Hand):
  with it("throws an exception when less than five cards are created"):
    expect(lambda: Hand("6C")).to(raise_error(ValueError, "Invalid number of cards"))
  with it("has 5 cards"):
    expect(Hand("6C 7C 8C 9C TC").cards).to(have_len(5))
```

---

## Two hands

Let's assume two hands, one containing a straight flush and the other containing a full house (how to deal with breaking ties is still too complicated at this point):

```python
with context("straight flush and a full house hand"):
  with it('returns the straight flush hand'):
    full_house = Hand("TD TC TH 7C 7D")
    straight_flush = Hand("6C 7C 8C 9C TC")
    hands = [full_house, straight_flush]
    expect(determine_best_hand(hands)).to(equal(straight_flush))
```

This can be implemented by always returning the second hand: 

```python
def determine_best_hand(hands):
  ...  
  return hands[1]
```

Obviously, we want to enforce some ranking mechanism, so we introduce yet another test, which is the same as the previous test, but now the order reversed:

```python
with context("full house and a straight flush hand"):
  with it('returns the straight flush hand'):
    full_house = Hand("TD TC TH 7C 7D")
    straight_flush = Hand("6C 7C 8C 9C TC")
    hands = [straight_flush, full_house]
    expect(determine_best_hand(hands)).to(equal(straight_flush))
```

We have to generalize the `determine_best_hand()` method
```python
def rank_hand(hand):
  return hand.rank_hand()
  
def determine_best_hand(hands):
  if len(hands) == 0:
    raise IllegalArgumentsException()
  elif len(hands) == 1:
    return hands[0]
  
  return max(hands, key = rank_hand)
```

where we assume a `rank_hand()` function to rank the hands and mocking the `rank_hand()` call for now

```python
when(poker_hands).rank_hand(full_house).thenReturn(PokerRanks.FULL_HOUSE.value)
when(poker_hands).rank_hand(straight_flush).thenReturn(PokerRanks.STRAIGHT_FLUSH.value)
```

Remember that the DRY principle has not been applied yet in these examples, so that is left intentionally to you!

## Implementing the hand ranking

Let's create a separate specification for the `Hand` class (`hand_spec.py`). The most logical scenario to start with would be the scenario where there is no score. In that case, we just return the ordered deck as described in the section on design considerations.

```python
with description("Given a hand") as self:
  with context("with no score"): 
    no_score = Hand("2D 4C 6H 8D TD")
    expect(no_score.rank_hand()).to(equal(
      (PokerRanks.ONE_OF_A_KIND, [10, 8, 6, 4, 2])
    ))
```

Strictly speaking, we don't need to properly configure the hand, as there is no logic checking it yet. However, since it will be needed later, it can't harm to initialize it properly already at this point. Moreover, it helps to express the intent of the scenario.

We make the test green, by hard-coding the tuple that must be returned. However, the ranking of the hand, _[10, 8, 6, 4, 2]_ will be carried out by a dedicated function, so let's move that logic to a separate function:

```python
...
def rank_cards(self):
  pass

def rank(self):
  return (PokerRanks.ONE_OF_A_KIND, self.rank_cards())
```

and mock that function accordingly in our scenario

```python
when(no_score).rank_cards().thenReturn([10, 8, 6, 4, 2])
```

Now that we have implemented the "default", we can start from the highest ranking and working our way back, see the list of rankings and associated tuples as was discussed in the section on design decisions. 

### Straight flush

The highest ranking, straight flush, obviously is a combination of straight and flush:

```python
with context('with straight flush'):
  with it('ranks the hand as straight flush 9'):
    straight_flush = Hand("6C 7C 8C 9C TC")
    # TODO: mocking calls go here
    expect(straight_flush.rank_hand()).to(equal(
      (PokerRanks.STRAIGHT_FLUSH, 10)
    ))
```

---
#### Exercise
Complete the production code to make the test green. Is there anything we can refactor (DRY)? Make it so!

---

### Four of a kind

As is implied by the names of `PokerRanks` enum values, there are various "of-a-kind" types: one of a kind, two of a kind, three of a kind, and four of a kind. This strongly suggests a `of_a_kind(self, kind_type:int)` function, that we can use to implement the next scenario, namely four of a kind (where the `kind_type` parameter equals four):

```python
...
with context('with four of a kind'):
  with it('ranks the hand as four of a kind, high 9'):
    four_of_a_kind = Hand("9D 9H 9S 9C 7D")
    # TODO: mocking calls go here
    expect(four_of_a_kind.rank_hand()).to(equal(
      (PokerRanks.FOUR_OF_A_KIND, 9, 11)
    ))
```

---
#### Exercise
Complete the test and production code.

---

After this exercise, your ranking function should start to look something like this:

```python
def rank(self):
  if self.straight() and self.flush():
    return (PokerRanks.STRAIGHT_FLUSH, max(self.rank_cards()))
  elif self.of_a_kind(4):
    return (PokerRanks.FOUR_OF_A_KIND, self.of_a_kind(4), self.of_a_kind(1))
  else:
    return (PokerRanks.ONE_OF_A_KIND, self.rank_cards())
```

where all the functions such as `rank_cards()` and `of_a_kind(4)` are mocked.

---
#### Exercise
Complete the _scenarios and production code_ by implementing all rankings (implemented as tuples) as described in the section on design decisions. Compared to the previous exercises, this exercise is rather time consuming.
Don't forget to look at the possiblities to refactor (apply DRY) after each green test.

---

## Implementing the ranking of the cards

Let's now implement all the functions that we have mocked thus far:

```python
def straight(self):
  pass

def flush(self):
  pass

def of_a_kind(self, kind_type: int):
  pass

def rank_cards(self):
  pass

def two_pair(self):
  pass
```

Let's start with the `rank_cards()`.

### Ranking the five cards

In order to rank the separate cards, let's introduce a card class first:

```python
class Card:
  def __init__(self, card: str):
      self.card = card

  def get_rank(self) -> int:
    pass
        
  def get_suit(self) -> str:
    pass
```
Let's create the set of five cards in the constructor of the hand class using a list comprehension:

```python
self.cards = [Card(c) for c in cards_string.split()]
```

Next, we can specify what we would like our `rank_cards()` function to do:

```python
with context("when ranking the cards"):
  with it("returns a list in descending order"):
    # TODO: mocking the calls to get_rank() in the card class here
    expect(Hand("6C 7C 8C 9C TC").rank_cards()).to(equal([10, 9, 8, 7, 6]))
```

---
#### Exercise

Given that subsequent calls to the `get_rank()` function in the card class can be mocked like this:

```python
when(Card).get_rank().thenReturn(6, 7, 8, 9, 10)
```

write an implementation for `rank_cards()` that makes the test green. Do we need to test more scenarios? If so, add these scenarios.

---

### Implementing straight and flush

Let's start with a scenario for straight first:

```python
straight = Hand("6C 7D 8S 9C TC")
with it('identifies the straight'):
  # mocks go here
  expect(self.straight.straight()).to(be_true)
```
---
#### Exercise
Implement the `straight()` function. Analogously, implement the `flush()`.

#### Caveat
Note that for a straight, it is not enough to just look at the difference of the higest card and the lowest card (being four), because in a hand such as `Hand("TD 8C 8H 7S 6D")` this difference is four, but it is _not_ a straight, so make sure to include (a) negative edge case(s) as well!

---

### Implementing _N_ of a kind

Let's implement our `of_a_kind(n)` function using the 1,2,N-principle. This means we are going to write a scenario first for one of a kind, then two of a kind, and then generalize to _N_.

---
#### Exercise
Implement the `of_a_kind(n)` function.

Hint: (eventually) checking the highest of-a-kind first (so for _N=4_) and returning the value when found, we prevent the `of_a_kind(3)` to also score when there are four of a kind.

Hint: add additional scenarios to confirm that `of_a_kind(3)` does not match in case of a straight!

---

### Implementing two pairs

Last but not least, let's implement the function that checks for two pairs.

---
#### Exercise
Implement this function.

Hint: add additional scenarios to confirm that the two pairs function does not accidentally match in case of only two of a kind, i.e., when both pairs are in fact the same pair. In this case the score should merely be a two of a kind!

---

## Implementing the cards

We have almost completely worked our way from the outside in. There is just one little class to complete that we have mocked so far, the card class.

---
#### Exercise

Write a specification and scenarios contained therein to implement the `get_rank()` and  `get_suit()` methods of the card class.

---

## Special cases

Most likely, there are still cases that you may not have covered yet. How about for example

```python
with description(Hand):
  with fcontext('with ace low straight'):
    with it('ranks the hand accordingly'):
      ace_low_straight = Hand("AC 2D 4H 3D 5S")
      expect(ace_low_straight.rank_hand()).to(equal(
       (PokerRanks.STRAIGHT, [5, 4, 3, 2, 1])
      ))
```

Since we mock the card class in most of the `hand_spec.py` specification, copy the above scenario into the _very beginning_ of the `hand_spec.py` file, and see what happens!

---
#### Exercise
Fix this special case by modifying the `rank_cards()` function to make an exception for _[14, 5, 4, 3, 2]_. In this case, return _[5, 4, 3, 2, 1]_.

---


# Retrospective

We have seen a nice example of how to program an application from the outside inwards, mocking the calls of the delegates/dependencies that haven't been implemented yet. We have also applied our TDD skills to a somewhat more complicated, or at least less trivial example.

We have seen the one and only use of mocks ([don't mock what you don't own](https://maksimivanov.com/posts/dont-mock-what-you-dont-own/)). Although we haven't touched upon using spies, their proper usage can now properly be imagined as well: suppose we want to send a command to a delegate. As commands don't return anything by definition, how do we verify the command actually arrived? This is exactly what spies are for!

We can conclude that the mockist/London school approach worked amazingly well. At the same time, you may have noticed that the test become more dependent on the code, as the calls to the delegates turn up explicitly in the specifications.

Does this mean that [the mockist approach is inferior](https://www.thoughtworks.com/insights/blog/mockists-are-dead-long-live-classicists)? You have to decide for yourself, but as with most things in life, it is not a matter of either-or, but of and-and.

As is explained in the course [Design of Computer Programs](https://www.udacity.com/course/design-of-computer-programs--cs212), we didn't properly deal with breaking ties yet. What if for example I managed to get a straight flush, ace high, and the other player managed to get the same result but in a different suite? This is left unanswered intentionally, as the kata is pretty long already. It may be done as an additional/bonus extension to this kata nonetheless. 

Last but not least, remember that a kata is supposed to be practiced, i.e. repeated multiple times, perfecting the skill along the way. Every inspiring repetition is suggested in [part 29: refactoring](https://classroom.udacity.com/courses/cs212/lessons/48688918/concepts/486836870923) of the course [Design of Computer Programs](https://www.udacity.com/course/design-of-computer-programs--cs212).