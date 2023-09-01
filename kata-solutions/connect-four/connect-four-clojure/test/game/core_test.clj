(ns game.core-test
  (:require [clojure.test :refer :all]
            [game.utilities :refer :all]
            [game.board :refer :all]
            [game.core :refer :all]))

(deftest given-three-in-a-row-test-for-winning-move
  (is (= false ((is-winning-move? 2) (on-board-with-moves [0 6 0 5 1 4 1]))))
  (is ((is-winning-move? 3) (on-board-with-moves [0 6 0 5 1 4 1]))))

(deftest given-full-column-cannot-play-full-column
  (is (= false ((can-play? 3) (on-board-with-moves [2 3 3 2 2 3 3 2 2 3 3]))))
  (is ((can-play? 2) (on-board-with-moves [2 3 3 2 2 3 3 2 2 3 3]))))

(deftest score-zero-for-a-draw
  (is (negamax (on-board-with-moves [0 0 0 0 0 0 1 1 1 1 1 1 2 2 2 2 2 2 4 3 3 3 3 3 3 4 4 4 4 4 5 5 5 5 5 5 6 6 6 6 6 6]))))

(deftest score-board-where-winning-move-is-possible
  (testing "Winning move rating."
    (is (= 18 (negamax (on-board-with-moves [0 6 0 5 1 4 1]))))))

(deftest score-board-where-winning-opponent-move-is-possible
  (testing "Opponent winning move rating."
    (is (= 19 (negamax (on-board-with-moves [0 1 0 1 0]))))))

