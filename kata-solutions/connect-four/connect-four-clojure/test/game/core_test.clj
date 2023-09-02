(ns game.core-test
  (:require [clojure.test :refer :all]
            [game.utilities :refer :all]
            [game.board :refer :all]
            [game.core :refer :all]
            [game.printer :refer :all]))

(deftest given-three-in-a-row-test-for-winning-move
  (is (= [3, true] (winning-move-on (board-with-moves [0 6 0 5 1 4 1])))))

(deftest winning-move-is-not-possible
  (is (empty? (winning-move-on GAME))))

(deftest given-full-column-cannot-play-full-column
  (is (= false ((can-play? 3) (board-with-moves [2 3 3 2 2 3 3 2 2 3 3]))))
  (is ((can-play? 2) (board-with-moves [2 3 3 2 2 3 3 2 2 3 3]))))

(deftest score-zero-for-a-draw
  (is (= 0 (min-max (board-with-moves [0 0 0 0 0 0 1 1 1 1 1 1 2 2 2 2 2 2 4 3 3 3 3 3 3 4 4 4 4 4 5 5 5 5 5 5 6 6 6 6 6 6]) 1))))

(deftest score-board-with-red-connect-four
  (is (= -18 (min-max (board-with-moves [0 1 0 1 0 1 0]) 1))))

(deftest score-board-with-yellow-connect-four
  (is (= 17 (min-max (board-with-moves [0 1 0 1 0 1 3 1]) 1))))

(deftest score-undecided-board
  (is (= 0 (min-max (board-with-moves [0 6 1 5 0 6]) 1))))

(deftest score-board-where-red-next-move-is-winning
  (is (= -18 (min-max (board-with-moves [0 1 0 1 0 1]) 1))))

(deftest score-board-where-yellow-next-move-is-winning
  ;(testing (print-game (board-with-moves [0 6 0 5 1 4 1])))
  (is (= 17 (min-max (board-with-moves [0 6 0 5 1 4 1]) 1))))

(deftest score-board-where-red-move-after-yellow-move-can-be-winning
  (is (= -18 (min-max (board-with-moves [3 3 2 2 1]) 2))))



(deftest suggested-move-on-board-where-yellow-next-move-is-winning)
  (is (= 3 (generate-ai-move (board-with-moves [0 6 0 5 1 4 1]))))

(deftest suggested-move-on-board-where-winning-opponent-move-is-possible)
  ;(testing (print-game (board-with-moves [5 1 5 2 5])))
  (is (= 5 (generate-ai-move (board-with-moves [5 1 5 2 5]))))

(deftest score-board-where-either-move-for-yellow-results-in-red-winning
  ;(testing (print-game (board-with-moves [3 6 4 4 2])))
  (is (= -18 (min-max (board-with-moves [3 6 4 4 2]) 2))))

