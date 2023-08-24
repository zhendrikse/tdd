# Implementation

Implementation inspired by [this solution on GitHub](https://github.com/eigenlicht/clj-connect-four/tree/master) combined with [bitboard design](https://github.com/denkspuren/BitboardC4/blob/master/BitboardDesign.md) and 
the principles of TDD.

## Moves on the board

We start by making a move in the first column of the board.
We assume the red player always starts.

But before he does so, we want to verify that that position is vacant 
(as a first test).

### An empty board is empty

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

### A first move in the first column

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

### A first move in the second column

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

### A first move in the third column by the first player

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

### A first move by the second player

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


### A first move by the second player

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

## Intermezzo: convenience functions for constructing boards

As we eventually want to test various board configurations, we
need a way to set up board configurations in a convenient way,
for example:

```clojure
;; player one plays first column, then player two plays first
;; column, then player one the second column, player two the
;; third, player one the second, etc.
(play-connect-4-with [0 0 1 2 3 2 4]))))
```

In Clojure, we are almost invited to implement this
recursively:

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