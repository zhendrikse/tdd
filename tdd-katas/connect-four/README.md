# Connect 4

## Game rules

- Two players: RED and YELLOW
- A board has 7 columns and 6 rows
- First column is column number 1
- The first player that manages to get 4-in-a-row horizontally,
  vertically, or diagonally, wins.

# Implementation

## Bitboards

Biboards are a great approach for a fast implementation. In this approach
a game is represented by a tuple of three 64-bit integers where:

- Every player gets his own bitboard, represented as an at least 64-bit integer
- An additional integer is used to indicate which players turn it is

Each bit in the 64-bit integer corresponds to a location on the board:

|Row| 0 |  1 | 2  |  3 |  4 |  5 |  6 |
|:-:|:-:|:--:|:--:|:--:|:--:|:--:|:--:|
|Bit| 5 | 12 | 19 | 26 | 33 | 40 | 47 | 
|Bit| 4 | 11 | 18 | 25 | 32 | 39 | 46 |
|Bit| 3 | 10 | 17 | 24 | 31 | 38 | 45 | 
|Bit| 2 | 9  | 16 | 23 | 30 | 37 | 44 | 
|Bit| 1 | 8  | 15 | 22 | 29 | 36 | 43 | 
|Bit| 0 | 7  | 14 | 21 | 28 | 35 | 42 |

The initial state of the game is thus characterized by the 
tuple `[bitboard_player_1, bitboard_player_2, turn_player_one] = [0 0 0]`)
and may visually be represented as:

```
[1 2 3 4 5 6 7]
[_ _ _ _ _ _ _]
[_ _ _ _ _ _ _]
[_ _ _ _ _ _ _]
[_ _ _ _ _ _ _]
[_ _ _ _ _ _ _]
[_ _ _ _ _ _ _]
```

This means that after two moves

```
[1 2 3 4 5 6 7]
[_ _ _ _ _ _ _]
[_ _ _ _ _ _ _]
[_ _ _ _ _ _ _]
[_ _ _ _ _ _ _]
[O _ _ _ _ _ _]
[X _ _ _ _ _ _]
```

the tuple has changed to `[2^0 + 2^1, 2^0, 2^1] = [3 1 2]`. 
Equivalently, in case the first two moves would have been 
at the second column of the board, the tuple would have been 
`[2^7 + 2^8, 2^7, 2^8] = [384, 128, 256]`.

### Finding the winning combinations

I'll try to explain this algorithm by the aid of an example where a row is a winning combination. The bitboard looks like this:

```
[1 2 3 4 5 6 7]
[_ _ _ _ _ _ _]
[X X X _ _ O _]
[O X O _ _ X _]
[X O X X _ O _]
[O O X O O O O]
[X O O X O X X]
```

The bitboard belonging to the winning player looks like this:

```
[0 0 0 0 0 0 0]
[0 0 0 0 0 1 0]
[1 0 1 0 0 0 0]
[0 1 0 0 0 1 0]
[1 1 0 1 1 1 1]
[0 1 1 0 1 0 0]
```

The number representing this board is 9552816915338. 
Let's see what those bit-operations actually do.

First step:
```clojure
(bit-and bitboard (bit-shift-right bitboard 7)
``` 

```
[0 0 0 0 0 0 0]   [0 0 0 0 0 0 0]   [0 0 0 0 0 0 0]
[0 0 0 0 0 1 0]   [0 0 0 0 1 0 0]   [0 0 0 0 0 0 0]
[1 0 1 0 0 0 0] & [0 1 0 0 0 0 0] = [0 0 0 0 0 0 0]
[0 1 0 0 0 1 0]   [1 0 0 0 1 0 0]   [0 0 0 0 0 0 0]
[1 1 0 1 1 1 1]   [1 0 1 1 1 1 0]   [1 0 0 1 1 1 0]
[0 1 1 0 1 0 0]   [1 1 0 1 0 0 0]   [0 1 0 0 0 0 0]
```

Second step:

```clojure
(bit-and bitboard (bit-shift-right bitboard (* 2 7)))
```

```
[0 0 0 0 0 0 0]   [0 0 0 0 0 0 0]   [0 0 0 0 0 0 0]
[0 0 0 0 0 0 0]   [0 0 0 0 0 0 0]   [0 0 0 0 0 0 0]
[0 0 0 0 0 0 0] & [0 0 0 0 0 0 0] = [0 0 0 0 0 0 0]
[0 0 0 0 0 0 0]   [0 0 0 0 0 0 0]   [0 0 0 0 0 0 0]
[1 0 0 1 1 1 0]   [0 1 1 1 0 0 0]   [0 0 0 1 0 0 0]
[0 1 0 0 0 0 0]   [0 0 0 0 0 0 0]   [0 0 0 0 0 0 0]
```

As you can see the second row, which contains four connected pieces, results into [0 0 0 1 0 0 0] and is therefore the winning combination. All the other rows results into 0.


# Links


## Board representations

- [Bitboards and Connect Four](https://github.com/denkspuren/BitboardC4/blob/master/BitboardDesign.md)

## Languages

- [Connect 4 in Clojure](https://github.com/eigenlicht/clj-connect-four), good code but without tests

## Algorithms

- [Constructing Agents for Connect-4: Initial Notes](https://markusthill.github.io/programming/connect-4-introduction-and-tree-search-algorithms/)
- [Solving connect four: how to build a perfect AI](http://blog.gamesolver.org/solving-connect-four/01-introduction/)
- [Artificial Intelligence at Play — Connect Four (Mini-max algorithm explained)](https://medium.com/analytics-vidhya/artificial-intelligence-at-play-connect-four-minimax-algorithm-explained-3b5fc32e4a4f)
- [Creating the (nearly) perfect connect-four bot with limited move time and file size](https://towardsdatascience.com/creating-the-perfect-connect-four-ai-bot-c165115557b0)
- [How to teach your robot to play connect four](https://roboticsproject.readthedocs.io/en/latest/index.html)
- [Connect 4 AI: How it works](https://roadtolarissa.com/connect-4-ai-how-it-works/)
- https://markusthill.github.io/programming/connect-4-transposition-tables/
