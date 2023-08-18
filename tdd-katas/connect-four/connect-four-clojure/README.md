# Implementation

## Moves on the board

<details>
  <summary>Moving the first player</summary>

```clojure
(deftest first-player-first-move-in-first-column
  (is (= [1 1 0] 
         (insert-at-column-for-player initial-game 0 1))))
```  
</details>

<details>
  <summary>Moving the first player</summary>

```clojure
(deftest second-player-first-move-in-first-column
  (is (= [3 1 2] 
         (insert-at-column-for-player 
          (insert-at-column-for-player initial-game 0 1) 0 2))))
```  
</details>

<details>
  <summary>Moving the first player</summary>

```clojure
(deftest first-player-second-move-in-first-column
  (is (= [7 5 2]
         (insert-at-column-for-player
          (insert-at-column-for-player 
           (insert-at-column-for-player initial-game 0 1) 0 2) 0 1))))
```  
</details>
