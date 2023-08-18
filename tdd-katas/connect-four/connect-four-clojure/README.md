# Implementation

Implementation inspired by [this solution on GitHub](https://github.com/eigenlicht/clj-connect-four/tree/master) combined with [bitboard design](https://github.com/denkspuren/BitboardC4/blob/master/BitboardDesign.md) and 
the principles of TDD.

That means that we start with a board consisting of a tuple of
three integers:
1. The bitboard belonging to player 1
2. The bitboard belonging to player 2
3. An integer with value zero denoting it is the turn of
   player 1 and with value one it is the turn of player 2

## Moves on the board

<details>
  <summary>The first move of the first player</summary>

```clojure
(def second-column 1)

(deftest first-player-first-move-in-second-column
  (is (= [128 0 1] 
         (insert-ply-at second-column in-initial-game))))

```  
We can make this test pass by
```clojure
(defn- first-free-row-in
  [column in-game]
  0)
  
(defn- index-for 
  [row column]
  (+ row (* column 7)))

(defn- bit-insert-at
  [row column in-board]
  (bit-set in-board (index-for row column)))
  
(defn insert-ply-at
  [column in-game]
  (let [row (first-free-row-in column in-game)
        player-num (in-game 2)]
    (-> (assoc in-game 2 (bit-xor 1 player-num))
        (assoc player-num (bit-insert-at row column (in-game player-num))))))
```
</details>

<details>
  <summary>The first move of the second player</summary>

```clojure
(deftest second-player-first-move-in-second-column
  (is (= [128 256 0] 
         (insert-ply-at second-column
           (insert-ply-at second-column in-initial-game)))))
```  

We can fake and cheat by extending the `first-free-row-in` function just a little bit:
```clojure
(defn- first-free-row-in
  [column in-game]
    (if (= in-game in-initial-game) 0 1))
```
</details>

<details>
  <summary>The second move of the first player</summary>

```clojure
(deftest first-player-second-move-in-second-column
  (is (= [640 256 1]
         (insert-ply-at second-column
           (insert-ply-at second-column
             (insert-ply-at second-column in-initial-game))))))
```  

Finally we need to generalize the `first-free-row-in` function:
```clojure
(defn- first-free-row-in
  [column in-game]
    (let [board (in-game 0)
          selected-column (bit-shift-right board (* column total-columns))
          selected-column-only (bit-and selected-column 127)
          column-as-string (Integer/toBinaryString selected-column-only)
          plie-count (count (re-seq #"1" column-as-string))]
      plie-count))
```
</details>

Finally, we implement a function to check whether a column is full or not

<details>
  <summary>Checking whether a column is full or not</summary>

```clojure

(deftest full-column-when-with-six-plies-in-second-column
  (is (= true
         (column-full-for? second-column
          (insert-ply-at second-column
           (insert-ply-at second-column
            (insert-ply-at second-column
             (insert-ply-at second-column
              (insert-ply-at second-column
               (insert-ply-at second-column in-initial-game))))))))))
```

which is easily made green by adding

```clojure
(defn column-full-for?
  [column in-game]
  (= total-rows (first-free-row-in column in-game)))
```
</details>