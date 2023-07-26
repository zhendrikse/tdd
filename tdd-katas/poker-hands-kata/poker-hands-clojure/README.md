# Introduction

Please read the general [introduction to the poker hands kata](../README.md) first!

# Getting started

You can simply start coding by invoking

```bash
$ lein new app kata/poker-hands
```

# Implementation

Before we start with the implementation, let's first consider a couple of design decisions that we would otherwise would have to make along the way.

## Design

### Ranking the hands

Suppose e.g. one hand to contain ``(9 9 9 9 5)`` and the other ``(3 3 3 3 2)``. As is argued in the course [Design of Computer Programs](https://www.udacity.com/course/design-of-computer-programs--cs212), the best way to represent the ranking is to use tuples:

- **Four of a kind**: ``(9 9 9 9 5)`` &rarr; ``(FOUR_OF_A_KIND 9 5)`` 
- **Four of a kind**: ``(3 3 3 3 2)`` &rarr; ``(FOUR_OF_A_KIND 3 2)``

The first integer in the tuple represents the ranking 

```clojure
(def STRAIGHT_FLUSH 8)
(def FOUR_OF_A_KIND 7)
(def FULL_HOUSE 6)
(def FLUSH 5)
(def STRAIGHT 4)
(def THREE_OF_A_KIND 3)
(def TWO_PAIR 2)
(def TWO_OF_A_KIND 1)
(def ONE_OF_A_KIND 0)
```

The second integer represents the highest card, so that we can break ties. The last integer represents the remaining card. 

For the other poker combinations, it may happen that the highest card cannot be used to disambiguate a tie, in which case we'll use the complete deck.

So let's summarize how we are going to uniquely associate a tuple to each hand (where suits have been omitted) that allows us to rank a hand:
- **Straight flush**: ``(11 10 9 8 7)`` & same suit &rarr; ``(STRAIGHT_FLUSH 11)``
- **Four of a kind**: ``(14 14 14 14 12)`` &rarr; ``(FOUR_OF_A_KIND 14 12)``
- **Full house**: ``(8 8 8 13 13)`` &rarr; ``(FULL_HOUSE 8 13)``
- **Flush**: ``(10 8 7 5 3)`` & same suit &rarr; ``(FLUSH [10 8 7 5 3])``
- **Straight**: ``(11 10 9 8 7)`` &rarr; ``(STRAIGHT 11)``
- **Three of a kind**: ``(7 7 7 5 2)`` &rarr; ``(THREE_OF_A_KIND 7 [7 7 7 5 2])``
- **Two pairs**: ``(11, 11, 3, 3, 13)`` &rarr; ``(TWO_PAIR 11 3 [13 11 11 3 3])``
- **Two of a kind**: ``(2 2 11 6 3)`` &rarr; ``(TWO_OF_A_KIND 2 [11 6 3 2 2])``
- **One of a kind**: ``(7 5 4 3 2)`` &rarr; ``(ONE_OF_A_KIND [7 5 4 3 2])``

Note that the Clojure language offers us the added benefit of being able to compare such tuples by default, e.g. ``(compare `(7, 9, 5) `(7, 3, 2))`` is valid in Clojure. By default it compares the first entries, if that's still true, the second entries, and so forth till all entries have been compared.

A hand can best be represented by 

```clojure
(def high-seven ["2H" "3S" "4C" "5C" "7D"])
``` 

Individual cards may then easily be ranked by simply ignoring the suit and mapping all cards to integer values like so: 
- 2 &rarr; 2, 
- 3 &rarr; 3, 
- ..., 
- Ten &rarr; 10,
- Jack &rarr; 11, 
- Queen &rarr; 12, 
- King &rarr; 13, 
- Ace &rarr; 14.

Thus, we are going to need a function that maps cards (strings) such as ``"TC"``, ``"JD"``, and ``"3S"`` to one of these integer values, e.g. ``(rank "JS") ;=> 11``

## Dealing with the cards

Individual cards will be denoted by a rank and a suit, so for example "TC" (club 10), "JD" (diamond jack), etc. We’ll want a couple of helper functions to read the rank and suit of a card.

A useful thing to note is that Strings are sequencable, so we can use sequence destructuring on them:

```clojure
(let [[value suit] "5H"]
  [value suit]) ;=> [\5 \H]
```

In case we are merely interested in some destructured values, it is idiomatic to use the name ``_`` for ignored values:

```clojure
(let [[_ suit] "AH"]
  suit) ;=> \H
```

And finally, remember that ``(str value)`` can be used to turn anything into its string representation, including characters.

```clojure
(str \C) ;=> "C"
```

So let's try to write the ``(suit card)`` function that returns the suit of a card.

### Exercise 1

Write the function ``(suit card)`` which takes a single card and returns the suit 
of the card as a one character string. You can you the following test cases:

```clojure
;; suit function on card
(deftest suit-of-heart-2 (is (= HEART (suit "2H"))))
(deftest suit-of-diamond-2 (is (= DIAMOND (suit "2D"))))
(deftest suit-of-club-2 (is (= CLUB (suit "2C"))))
(deftest suit-of-spade-3 (is (= SPADE (suit "3S"))))
```

To get the rank, we’ll need to convert a character into an integer. To see if a character is a digit, like ``\5`` or ``\2``, we can use ``(Character/isDigit char)``:

```clojure
(Character/isDigit \5) ;=> true
(Character/isDigit \A) ;=> false
```

If a character is a digit, we can use ``(Integer/valueOf string)`` to convert it to an integer. We will first have to convert the character into a string.

```clojure
(Integer/valueOf "12")     ;=> 12
(Integer/valueOf (str \5)) ;=> 5
```

Finally, to turn the characters ``T``, ``J``, ``Q``, ``K`` and ``A`` into integers, using a map to store the values is very useful:

```clojure
(get {\A 100, \B 20} \B) ;=> 20
({\A 100, \B 20} \B) ;=> 20

(def replacements {\A 100, \B 20})

(replacements \B) ;=> 20
```

We can now write the ``(rank card)`` function.

### Exercise 2
Write the function ``(rank card)`` which takes a single card and returns the rank as a number between 2 and 14. You can you the following test cases:

```clojure
;; rank function on card
(deftest rank-of-heart-2 (is (= 2 (rank "2H"))))
(deftest rank-of-spade-4 (is (= 4 (rank "4S"))))
(deftest rank-of-spade-ten (is (= 10 (rank "TS"))))
(deftest rank-of-spade-jack (is (= 11 (rank "JS"))))
(deftest rank-of-spade-quin (is (= 12 (rank "QS"))))
(deftest rank-of-spade-king (is (= 13 (rank "KS"))))
(deftest rank-of-spade-ace (is (= 14 (rank "AS"))))
```

### Exercise 3



Write the function ``(pair? hand)`` that returns true if there is a pair in hand and false if there is no pair in hand.


```clojure
(pair? pair-hand)  ;=> true
(pair? high-seven) ;=> false
```


