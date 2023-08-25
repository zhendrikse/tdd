# Introduction

The implementation below is inspired by 
[this solution on GitHub](https://github.com/eigenlicht/clj-connect-four/tree/master) 
combined with [bitboard design](https://github.com/denkspuren/BitboardC4/blob/master/BitboardDesign.md) and 
the principles of TDD.

Let's start by implementing the board.

# Moves on the board

We start by making a move in the first column of the board.
We assume the red player always starts.

But before he does so, we want to verify that that position is vacant 
(as a first test).

## An empty board is empty

<details>
  <summary>Bottom-left position should be empty for a new board</summary>

```clojure
(deftest player-one-move-at-column-one-results-in-red-at-bottom-left
  (testing "A first move of player 1 in column 1."
    (is (= RED (check-board-at 0 0 (make-move 0 GAME))))))
```  

We can easily make this test pass by defining the function

```clojure
(def RED 0)
(def YELLOW 1)
(def EMPTY 2)
(def NEW_BITBOARD 0)

(def TOTAL_ROWS 6)
(def TOTAL_COLUMNS 7)

(def GAME [NEW_BITBOARD NEW_BITBOARD])

(defn check-board-at [row column game] EMPTY)
```
</details>

## A first move in the first column

<details>
  <summary>A first move in the first column</summary>

```clojure
(deftest player-one-move-at-column-one-results-in-red-at-bottom-left
  (testing "A first move of player 1 in column 1."
    (is (= RED (check-board-at 0 0 (make-move 0 GAME))))))
```  

Next, we define the function `make-move`:
```clojure
(def MOVES_COUNTER 0)
(def GAME [NEW_BITBOARD NEW_BITBOARD MOVES_COUNTER])
(def MOVES_COUNTER_INDEX 2)

(defn check-board-at [row column game] (if (= game GAME) EMPTY RED))

(defn make-move [column game]
  (let [current-player (game MOVES_COUNTER_INDEX)]
    assoc game current-player [1 0]))
```

We fake and cheat once more by hardcoding the updated board.
</details>

Since we have hardcoded the updated board, let's force a first
generalization, by writing a test for column two.

## A first move in the second column

<details>
  <summary>A first move in the second column</summary>

```clojure
(deftest player-one-move-at-column-two-results-in-red-at-bottom-column-two
  (testing "A first move of player 1 in column 2." 
    (is (= EMPTY (check-board-at 0 0 (make-move 1 GAME))))
    (is (= RED   (check-board-at 0 1 (make-move 1 GAME))))))
```  

We are now forced to generalize the bit that is being flipped.

```clojure
(defn bit-position [row column]
  (if (= column 0) 0 7))

(defn check-board-at [row column game]
  (cond
    (bit-test (game RED) (bit-position row column)) RED
    (bit-test (game YELLOW) (bit-position row column)) YELLOW
    :else EMPTY))

(defn- update-bitboard [bitboard column]
  (if (= column 0) 1 (bit-shift-left 1 7)))

(defn- update-board-in [game column]
  (let [player (game MOVES_COUNTER_INDEX) 
        bitboard-player (game player)
        updated-bitboard (update-bitboard bitboard-player column)]
   (assoc game player updated-bitboard)))

(defn make-move [column game]
    (update-board-in game column))
```
</details>

## A first move in the third column by the first player

Let's see what happens if we play the third column.

<details>
  <summary>A first move in the third column</summary>

```clojure
(deftest player-one-move-at-column-three-results-in-red-at-bottom-column-three
  (testing "A first move of player 1 in column 3."
    (is (= EMPTY (check-board-at 0 0 (make-move 2 GAME))))
    (is (= EMPTY (check-board-at 0 1 (make-move 2 GAME))))
    (is (= RED   (check-board-at 0 2 (make-move 2 GAME))))))
```

We now have to do something with the x-coordinates, because the bit we
have to set is now determined by the index of the column that is chosen:

```clojure
(def BITBOARD_COLUMN_INDICES [0 7 14 21 28 35 42])
(def NEW_BOARD [NEW_BITBOARD NEW_BITBOARD BITBOARD_COLUMN_INDICES])
```

Now we modify the `make-move` and `check-board-at` 
functions accordingly: 

```clojure
(defn bit-position [row column]
  (+ row (* column TOTAL_COLUMNS)))

(defn check-board-at [row column game]
  (cond
    (bit-test (game RED) (bit-position row column)) RED
    (bit-test (game YELLOW) (bit-position row column)) YELLOW
    :else EMPTY))

(defn- update-bitboard [bitboard bit-index]
  (let [move (bit-shift-left 1 bit-index)]
  (bit-xor move bitboard)))

(defn- update-board-in [game column]
  (let [player (game MOVES_COUNTER_INDEX) 
        bitboard (game player)
        bit-index ((game COLUMNS_INDEX) column)
        updated-bitboard (update-bitboard bitboard bit-index)]
   (assoc game player updated-bitboard)))

(defn make-move [column game]
    (update-board-in game column))
```
</details>

## A first move by the second player

Let's see what happens if we play the second player too.

<details>
  <summary>A first move in the third column</summary>

```clojure

(deftest player-one-move-at-column-one-player-two-column-two
  (testing "Players 1 and 2 in columns 1 and 2 respectively."
    (is (= RED    (check-board-at 0 0 (make-move 1 (make-move 0 GAME)))))
    (is (= YELLOW (check-board-at 0 1 (make-move 1 (make-move 0 GAME)))))))
```

We now have to update the moves counter, so that the player is 
automatically switched (the current player is red when the
moves counter is even, and yellow when it is odd):

```clojure
(defn- current-player-in
  [game]
  (bit-and 1 (game MOVES_COUNTER_INDEX)))

(defn- increment-move-counter
  [game]
  (let [updated-game-counter (inc (get game MOVES_COUNTER_INDEX))]
    (assoc game MOVES_COUNTER_INDEX updated-game-counter))) 

;; ...

(defn- update-board-in [game column]
  (let [player (current-player-in game) 
        bitboard (game player)
        bit-index ((game COLUMNS_INDEX) column)
        updated-bitboard (update-bitboard bitboard bit-index)]
   (assoc game player updated-bitboard)))

(defn make-move [column game]
  (-> (increment-move-counter
      (update-board-in game column))))
```
</details>


## A first move by the second player

Let's see what happens if we play the second player in the same column, so
that the height in the column increases.

<details>
  <summary>Players 1 and 2 play the same column</summary>


```clojure
(deftest player-one-move-at-column-one-player-two-column-one
  (testing "Players 1 and 2 in column 1."
    (is (= RED    (check-board-at 0 0 (make-move 0 (make-move 0 GAME)))))
    (is (= YELLOW (check-board-at 1 0 (make-move 0 (make-move 0 GAME)))))))
```

We have to update the value of the corresponding column in the
list containing the bitboard column indices:

```clojure
(defn- column-height-for
  [column, game]
  ((get game COLUMNS_INDEX) column))

(defn- increment-column-height
  [column game]
  (let [current-height (column-height-for column game)
        updated-height (inc current-height)]
    (assoc (get game COLUMNS_INDEX) column updated-height))) 

(defn- update-column-heights-in
  [column game]
  (let [updated-columns (increment-column-height column game)]
    (assoc game COLUMNS_INDEX updated-columns)))

(defn make-move [column game]
  (-> (update-column-heights-in column
      (increment-move-counter-in
      (update-board-in game column)))))
```
</details>

# Intermezzo: convenience functions for constructing boards

As we eventually want to test various board configurations, we
need a way to set up board configurations in a convenient way,
for example:

```clojure
;; player one plays first column, then player two plays first
;; column, then player one the second column, player two the
;; third, player one the second, etc.
(play-connect-4-with [0 0 1 2 3 2 4])
```

In Clojure, we are almost invited to implement this recursively:

```clojure
(defn play-connect-4
  [moves game]
  (let [updated-game (make-move (first moves) game)]
    (if (= 1 (count moves))
      updated-game
      (recur (rest moves) updated-game))))

(defn play-connect-4-with
  [moves]
  (play-connect-4 moves GAME))
```

It would also be convenient if we can inspect these configurations
visually:

```
[ 1  2  3  4  5  6  7]
(.. .. .. .. .. .. ..)
(.. ..🟡 .. ..  .. ..)
(.. ..🔴 🟡 ..  .. ..)
(..🟡 🔴 🟡 🔴 .. ..)
(..🔴 🔴 🔴 🟡 .. ..)
(..🔴 🟡 🟡 🟡 🔴..)
```

<details>
<summary>The printing logic</summary>

```clojure
(def board-bitnumbers
  "All bit numbers which are inside the bitboard.
  (
    (5 12 19 26 33 40 47) 
    (4 11 18 25 32 39 46) 
    (3 10 17 24 31 38 45) 
    (2 9 16 23 30 37 44) 
    (1 8 15 22 29 36 43) 
    (0 7 14 21 28 35 42)
  )"
  (vec (flatten (for [y y-range-of-bit-numbers]
                  (for [x x-range-of-bit-numbers]
                    (+ x y))))))

(defn- map-to-symbol
  [game bitboard-index]
  (cond 
    (bit-test (get game RED) bitboard-index) red
    (bit-test (get game YELLOW) bitboard-index) yellow
    :else none))

(defn- map-to-string
  [game]
  (vec (map (partial map-to-symbol game) board-bitnumbers)))

(defn- index-in
    [game-string row column]
       (game-string (+ column (* row TOTAL_COLUMNS))))
    
(defn- print-rows
  [game-string]
  (doseq [row (range 0 TOTAL_ROWS)] 
    (println 
     (for [column (range 0 TOTAL_COLUMNS)] 
       (index-in game-string row column)))))

(defn print-game
  [game]
  (let [game-string (map-to-string game)
        header (vec (map (partial str " ") (range 1 (inc TOTAL_COLUMNS))))]
  (println header)
  (print-rows game-string)))
```
</details>

## Full board

We need a predicate for a full board so that we can determine 
whether or not the game ended in a draw.

<details>
  <summary>Predicate for a full board</summary>

```clojure
(deftest is-draw
  ;(print-game (play-connect-4-with [0 0 0 0 0 0 1 1 1 1 1 1 2 2 2 2 2 2 4 3 3 3 3 3 3 4 4 4 4 4 5 5 5 5 5 5 6 6 6 6 6 6]))
  (is (= true (is-full? (play-connect-4-with [0 0 0 0 0 0 1 1 1 1 1 1 2 2 2 2 2 2 4 3 3 3 3 3 3 4 4 4 4 4 5 5 5 5 5 5 6 6 6 6 6 6])))))
```

You can visually inspect the board configuration by commenting in 
the print statement and verify that the board is full and has no
winner.

```clojure
(defn is-full? 
  ([game] 
   (= (* HEIGHT WIDTH) (game MOVES_COUNTER_INDEX))))
``` 
</details>


## Full column

Likewise, we need a predicate for a full column so that we can determine 
which columns are still eligible to make a move.

<details>
  <summary>Predicate for a full column</summary>

```clojure
(deftest full-column-when-inserted-results-in-no-operation
  (testing "Insert in full column will be neglected."
    (is (= (play-connect-4-with [0 0 0 0 0 0]) (play-connect-4-with [0 0 0 0 0 0 0])))))
```

We test this indirectly by verifying that a move in a column
that is already full leaves the game board unchanged.

We extend the arity of the `is-full?` predicate to make the test green:

```clojure
(defn is-full? 
  ([game] 
   (= (* HEIGHT WIDTH) (game MOVES_COUNTER_INDEX)))
  ([game column] 
   (let [column-bitindex ((game COLUMNS_INDEX) column)
         full-column-bitindex (+ HEIGHT (BITBOARD_COLUMN_INDICES column))]
     (= column-bitindex full-column-bitindex))))
``` 
</details>

# Checking for connect four

The code in the solution has been taken from 
[this solution on GitHub](https://github.com/eigenlicht/clj-connect-four/tree/master) 
and needs to be developed from scratch using TDD.

There are some tests though.

<details>
  <summary>Tests for verification of connect four</summary>

```clojure
(deftest check-no-connect-four
  ;(print-game (play-connect-4-with [3 3]))
  (is (= false (connect-four? (play-connect-4-with [3 3])))))

(deftest check-horizontal-four-player-one
  ;(print-game (play-connect-4-with [0 0 1 1 2 2 3]))
  (is (connect-four? (play-connect-4-with [0 0 1 1 2 2 3]))))

(deftest check-horizontal-four-player-two
  ;(print-game (play-connect-4-with [0 1 1 2 2 3 3 4]))
  (is (connect-four? (play-connect-4-with [0 1 1 2 2 3 3 4]))))

(deftest check-vertical-four-player-one
  ;(print-game (play-connect-4-with [0 1 0 1 0 1 0]))
  (is (connect-four? (play-connect-4-with [0 1 0 1 0 1 0]))))

(deftest check-vertical-four-player-two
  ;(print-game (play-connect-4-with [0 1 0 1 0 1 2 1]))
  (is (connect-four? (play-connect-4-with [0 1 0 1 0 1 2 1]))))

(deftest check-diagonal-four-player-one
  ;(print-game (play-connect-4-with [0 1 1 2 2 3 2 3 3 5 3]))
  (is (connect-four? (play-connect-4-with [0 1 1 2 2 3 2 3 3 5 3]))))

(deftest is-draw
  ;(print-game (play-connect-4-with [0 0 0 0 0 0 1 1 1 1 1 1 2 2 2 2 2 2 4 3 3 3 3 3 3 4 4 4 4 4 5 5 5 5 5 5 6 6 6 6 6 6]))
  (is (= true (is-full? (play-connect-4-with [0 0 0 0 0 0 1 1 1 1 1 1 2 2 2 2 2 2 4 3 3 3 3 3 3 4 4 4 4 4 5 5 5 5 5 5 6 6 6 6 6 6])))))
```

The last test is a bit special, in the sense that it test for a draw.
</details>

# Playing connect four

## Two human players

Let's first build the logic to have two human players
compete against one another.

<details>
<summary>Accommodating two human players</summary>

```clojure
(defn read-input [player-num]
  (printf "Player %d's turn [human]: " (inc player-num)) (flush)
  (dec (Integer/parseInt (or (re-find #"^\d+" (read-line)) "0"))))

(defn- game-end? [game] (or (connect-four? game) (is-full? game)))

(defn- game-exit 
  [game]
  (let [previous-player (bit-xor 1 (current-player-in game))]
    (if (connect-four? game)  
      (println (str "Player " (inc previous-player) " has won!")) 
      (println (str "It's a draw!")))))

(defn- play-game
  [game]
  (let [current-player (current-player-in game)]
    (print-game game)
    (if (game-end? game)
      (game-exit game)
      (recur (make-move (read-input current-player) game)))))
```
</details>

## A human player against an AI player

### AI player that plays random moves

We extend the above code with the simplest thing that could 
possibly work, namely an AI player that just randomly picks
its moves.

<details>
  <summary>Human player against an AI player with random moves</summary>

```clojure
(deftest generate-random-ai-move
  (testing "AI player generates a random move on empty board")
    (is (and (> (generate-ai-move GAME) 0) (< (generate-ai-move GAME) WIDTH))))
```

We can make this test pass easily by defining

```clojure
(defn generate-ai-move [game] (get (vec (range WIDTH)) (rand-int WIDTH)))
```

The function that plays the game can now use this `genrate-ai-move` function
for the AI player:

```clojure
(defn- play-game
  [game] 
  (let [current-player (current-player-in game)]
    (print-game game)
    (if (game-end? game) 
      (game-exit game)
      (if (= current-player RED)
        (recur (make-move (read-input current-player) game))
        (recur (make-move (generate-ai-move game) game))))))
```
</details>

### AI player that plays the winning move

Next step up is to let the AI player make an exception from
its default random selection strategy when he can make a 
winning move. 

To this extent, we are going to rate all the possible moves.
By default, all moves are rated with a zero score. As has been explained
[here](http://blog.gamesolver.org/solving-connect-four/02-test-protocol/)

- A score is positive if the current player can win. 
  The score is 1 if he wins with his last stone, 
  2 if he wins with your second last stone and so on.
- A score is zero if the game ends by a draw game
- A score is negative if the current player loses whatever he plays. 
  The score is -1 if his opponent wins with his last stone, 
  -2 if his opponent wins with his second last stone and so on.

<details>
  <summary>Creating a score for the winning move</summary>

```clojure
(deftest winning-move-ratings-for-connect-four
  (testing "Winning move ratings for a connect four."
    (is (= [0 0 0 18 0 0 0] (rate-moves (play-connect-4-with [0 6 0 5 1 4 1]))))))
```

We can make this test pass with

```clojure
(def TOTAL_MOVES (/ (* WIDTH HEIGHT) 2))

(defn- is-winning-move?
  [move game]
  (connect-four? (make-move move game)))

(defn- rate-move 
  [game move]
  (let [moves-made (/ (dec (game MOVES_COUNTER_INDEX)) 2)
        moves-left (- TOTAL_MOVES moves-made)
        score moves-left]
  (if (is-winning-move? move game)
    score
    0)))

(defn rate-moves 
  [game] 
  (map (partial rate-move game) (range WIDTH)))
```

The `genrate-ai-move` function now has to pick this move with
the highest score:

```clojure
(deftest ai-selects-highest-move
  (testing "AI player generates a random move on empty board")
  (is (= 3 (generate-ai-move (play-connect-4-with [0 6 0 5 1 4 1])))))
```

So we modify `generate-ai-move`

```clojure
(defn- equal-ratings? [move-ratings] (apply = move-ratings))

(defn generate-ai-move [game]
  (let [move-ratings (rate-moves game)
        best-move (.indexOf move-ratings (apply max move-ratings))] 
    (if (equal-ratings? move-ratings)
      ((vec (range WIDTH)) (rand-int WIDTH))
      best-move)))
```
</details>