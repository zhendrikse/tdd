(ns game.board-test
  (:require [clojure.test :refer :all]
            [game.board :refer :all]))

(deftest a-new-board-has-no-plies-at-bottom-left
  (testing "No plies on a new board."
    (is (= EMPTY (check-board-at 0 0 GAME)))))

(deftest player-one-move-at-column-one-results-in-red-at-bottom-left
  (testing "A first move of player 1 in column 1."
    (is (= RED (check-board-at 0 0 (make-move 0 GAME))))))

(deftest player-one-move-at-column-two-results-in-red-at-bottom-column-two
  (testing "A first move of player 1 in column 2."
    (is (= EMPTY (check-board-at 0 0 (make-move 1 GAME))))
    (is (= RED   (check-board-at 0 1 (make-move 1 GAME))))))

(deftest player-one-move-at-column-three-results-in-red-at-bottom-column-three
  (testing "A first move of player 1 in column 3."
    (is (= EMPTY (check-board-at 0 0 (make-move 2 GAME))))
    (is (= EMPTY (check-board-at 0 1 (make-move 2 GAME))))
    (is (= RED   (check-board-at 0 2 (make-move 2 GAME))))))

(deftest player-one-move-at-column-one-player-two-column-two
  (testing "Players 1 and 2 in columns 1 and 2 respectively."
    (is (= RED    (check-board-at 0 0 (make-move 1 (make-move 0 GAME)))))
    (is (= YELLOW (check-board-at 0 1 (make-move 1 (make-move 0 GAME)))))))

(deftest player-one-move-at-column-one-player-two-column-one
  (testing "Players 1 and 2 in column 1."
    (is (= RED    (check-board-at 0 0 (make-move 0 (make-move 0 GAME)))))
    (is (= YELLOW (check-board-at 1 0 (make-move 0 (make-move 0 GAME)))))))
