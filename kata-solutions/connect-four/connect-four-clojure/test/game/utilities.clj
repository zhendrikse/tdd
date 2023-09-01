(ns game.utilities
  (:require [game.board :refer :all]))

(def EMPTY 2)

(defn- bit-position [row column]
  (+ row (* column WIDTH)))

(defn check-board-at [row column game]
  (cond
    (bit-test (game RED) (bit-position row column)) RED
    (bit-test (game YELLOW) (bit-position row column)) YELLOW
    :else EMPTY))

(defn board-with-moves
  [moves]
  (loop [moves-to-make moves 
         board GAME]
    (let [updated-board (make-move (first moves-to-make) board)]
    (if (empty? (rest moves-to-make))
      updated-board
      (recur (rest moves-to-make) updated-board)))))
