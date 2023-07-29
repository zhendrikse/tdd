(ns kata.game-of-life
  (:gen-class))

(defn living-cell 
  [x y]
  [x y true])

(defn dead-cell 
  [x y]
  [x y false])

(defn dead?
  [cell]
  (= (last cell) false))

(defn alive?
  [cell]
  (= (last cell) true))

(defn to-dead-cell
  [cell-killable? cell]
  (if (cell-killable? cell)
    (dead-cell (get cell 0) (get cell 1))
    cell))

(defn to-living-cell
  [cell-viable? cell]
  (if (cell-viable? cell)
    (living-cell (get cell 0) (get cell 1))
    cell))
