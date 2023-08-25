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

(defn play-connect-4
  [moves game]
  (let [updated-game (make-move (first moves) game)]
    (if (= 1 (count moves))
      updated-game
      (recur (rest moves) updated-game))))

(defn play-connect-4-with
  [moves]
  (play-connect-4 moves GAME))