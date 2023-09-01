(ns game.core-test
  (:require [clojure.test :refer :all]
            [game.utilities :refer :all]
            [game.board :refer :all]
            [game.core :refer :all]))

(deftest given-three-in-a-row-test-for-winning-move
  (is (= [3, true] (winning-move-on (board-with-moves [0 6 0 5 1 4 1])))))

(deftest winning-move-is-not-possible
  (is (empty? (winning-move-on GAME))))

(deftest given-full-column-cannot-play-full-column
  (is (= false ((can-play? 3) (board-with-moves [2 3 3 2 2 3 3 2 2 3 3]))))
  (is ((can-play? 2) (board-with-moves [2 3 3 2 2 3 3 2 2 3 3]))))

(deftest score-zero-for-a-draw
  (is (negamax (board-with-moves [0 0 0 0 0 0 1 1 1 1 1 1 2 2 2 2 2 2 4 3 3 3 3 3 3 4 4 4 4 4 5 5 5 5 5 5 6 6 6 6 6 6]))))

(deftest score-board-where-winning-move-is-not-possible
  (testing "Rating for arbitrary configuration.")
    (is (= 42 (negamax (board-with-moves [0 1 1 0 6 4 3])))))

(deftest score-board-where-winning-move-is-possible
  (testing "Winning move rating.")
    (is (= 18 (negamax (board-with-moves [0 6 0 5 1 4 1])))))

(deftest suggested-move-on-board-where-winning-move-is-possible)
  (testing "Generated AI move should be the winning move")
    (is (= 3 (generate-ai-move (board-with-moves [0 6 0 5 1 4 1]))))

(deftest score-board-where-winning-opponent-move-is-possible
  (testing "Opponent winning move rating.")
    (is (= 42 (negamax (board-with-moves [5 1 5 2 5])))))

(deftest suggested-move-on-board-where-winning-opponent-move-is-possible)
  (testing "Generated AI move should prevent the winning move of the opponent")
    (is (= 5 (generate-ai-move (board-with-moves [5 1 5 2 5]))))

