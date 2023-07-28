(ns kata.game-of-life
  (:gen-class))

(defn living_cell 
  [x y]
  [x y true])

(defn dead_cell 
  [x y]
  [x y false])

(defn dead?
  [cell]
  (= (last cell) false))

(defn alive?
  [cell]
  (= (last cell) true))
