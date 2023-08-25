(ns game.board-test
  (:require [clojure.test :refer :all]
            [game.board :refer :all]
            [game.printer :refer :all]))

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

(deftest a-new-board-has-no-plies-at-bottom-left
  (testing "No moves are present a new board."
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

(deftest full-column-when-inserted-results-in-no-operation
  (testing "Insert in full column will be neglected."
    (is (= (play-connect-4-with [0 0 0 0 0 0]) (play-connect-4-with [0 0 0 0 0 0 0])))))

(deftest check-no-connect-four
  ;(print-game (play-connect-4-with [3 3]))
  (is (= false (connect-four? (play-connect-4-with [3 3])))))

(deftest check-horizontal-four-player-one
  ;(print-game (play-connect-4-with [0 0 1 1 2 2 3]))
  (is (connect-four? (play-connect-4-with [0 0 1 1 2 2 3]))))

(deftest check-horizontal-four-player-two
  ;(print-game (play-connect-4-with [0 1 1 2 2 3 3 4]))
  (is (connect-four? (play-connect-4-with [0 1 1 2 2 3 3 4]))))

(deftest check-vertical-four-player-one
  ;(print-game (play-connect-4-with [0 1 0 1 0 1 0]))
  (is (connect-four? (play-connect-4-with [0 1 0 1 0 1 0]))))

(deftest check-vertical-four-player-two
  ;(print-game (play-connect-4-with [0 1 0 1 0 1 2 1]))
  (is (connect-four? (play-connect-4-with [0 1 0 1 0 1 2 1]))))

(deftest check-diagonal-four-player-one
  ;(print-game (play-connect-4-with [0 1 1 2 2 3 2 3 3 5 3]))
  (is (connect-four? (play-connect-4-with [0 1 1 2 2 3 2 3 3 5 3]))))

(deftest is-draw
  ;(print-game (play-connect-4-with [0 0 0 0 0 0 1 1 1 1 1 1 2 2 2 2 2 2 4 3 3 3 3 3 3 4 4 4 4 4 5 5 5 5 5 5 6 6 6 6 6 6]))
  (is (= true (is-full? (play-connect-4-with [0 0 0 0 0 0 1 1 1 1 1 1 2 2 2 2 2 2 4 3 3 3 3 3 3 4 4 4 4 4 5 5 5 5 5 5 6 6 6 6 6 6])))))
