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

(defn- x-coordinate-from
    [cell]
    (first cell))

(defn- y-coordinate-from
    [cell]
    (get cell 1))

(defn- distance-between
  [cell other-cell]
  (list 
   (Math/abs (- (x-coordinate-from cell) (x-coordinate-from other-cell))) 
   (Math/abs (- (y-coordinate-from cell) (y-coordinate-from other-cell)))))

(defn- distance-less-than-two-between?
  [cell other-cell]
  (< (reduce max (distance-between cell other-cell)) 2))

(defn neighbour-of?
  [given-cell]
  (fn 
    [cell] 
    (and (not(= cell given-cell)) (distance-less-than-two-between? cell given-cell))
  ))

(defn living-neighbours-in
  [game]
  (fn [cell] (filter alive? (filter (neighbour-of? cell) game) )))

(defn exactly-three?
  [find-neighbours-for]
  (fn [cell] (= 3 (count (find-neighbours-for cell)))))

(defn more-than-three?
  [find-neighbours-for]
  (fn [cell] (> (count (find-neighbours-for cell)) 3)))

(defn less-than-two?
  [find-neighbours-for]
  (fn [cell] (< (count (find-neighbours-for cell)) 2)))