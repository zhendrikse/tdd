(ns kata.game-of-life
  (:gen-class))

(defn living-cell 
  [x y]
  [x y true])

(defn dead-cell 
  [x y]
  [x y false])

(defn is-dead?
  [cell]
  (= (last cell) false))

(defn is-alive?
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

(defn is-neighbour-of?
  [given-cell]
  (fn 
    [cell] 
    (and (not(= cell given-cell)) (distance-less-than-two-between? cell given-cell))
  ))

(defn which 
  [& preds]
  (fn [& args] (every? #(apply % args) preds)))

(defn living-neighbours-in
  [game]
  (fn [cell] (filter is-alive? (filter (is-neighbour-of? cell) game) )))

(defn has-exactly-three?
  [find-neighbours-for]
  (fn [cell] (= 3 (count (find-neighbours-for cell)))))

(defn has-more-than-three?
  [find-neighbours-for]
  (fn [cell] (> (count (find-neighbours-for cell)) 3)))

(defn has-less-than-two?
  [find-neighbours-for]
  (fn [cell] (< (count (find-neighbours-for cell)) 2)))

(defn next-generation-of
  [game]
  (map #(to-living-cell (and is-dead? (has-exactly-three? (living-neighbours-in game))) %) 
  (map #(to-dead-cell (and is-alive? (or (has-less-than-two? (living-neighbours-in game)) (has-more-than-three? (living-neighbours-in game))) ) %) game)   )
)