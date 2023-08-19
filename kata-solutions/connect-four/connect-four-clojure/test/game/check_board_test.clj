(ns game.check-board-test
  (:require [clojure.test :refer :all]
            [game.check-board :refer :all]
            [game.printer :refer :all]
            [game.board :refer :all]))

(deftest check-horizontal-four-when-there-is-none
  ;(print-game (play-connect-4-with [0 0 1 1 2 2]))
  (is (= false 
        (connect-four? (play-connect-4-with [0 0 1 1 2 2])))))

(deftest check-horizontal-four-player-one
  ;(print-game (play-connect-4-with [0 0 1 1 2 2 3]))
  (is (= true
        (connect-four? (play-connect-4-with [0 0 1 1 2 2 3])))))

(deftest check-horizontal-four-player-two
  ;(print-game (play-connect-4-with [0 1 1 2 2 3 3 4]))
  (is (= true
        (connect-four? (play-connect-4-with [0 1 1 2 2 3 3 4])))))

(deftest check-vertital-four-when-there-is-none
  ;(print-game (play-connect-4-with [0 1 0 1 0 1]))
  (is (= false
        (connect-four? (play-connect-4-with [0 1 0 1 0 1])))))

(deftest check-vertital-four-player-one
  ;(print-game (play-connect-4-with [0 1 0 1 0 1 0]))
  (is (= true
        (connect-four? (play-connect-4-with [0 1 0 1 0 1 0])))))

(deftest check-vertital-four-player-two
  ;(print-game (play-connect-4-with [0 1 0 1 0 1 2 1]))
  (is (= true
        (connect-four? (play-connect-4-with [0 1 0 1 0 1 0 2 1])))))

(deftest no-diagonal-four
  (print-game (play-connect-4-with [0 1 1 2 2 3 2 3 3 5]))
  (is (= false
        (connect-four? (play-connect-4-with [0 1 1 2 2 3 2 3 3 5])))))

(deftest diagonal-four-player-one
  ;(print-game (play-connect-4-with [0 1 1 2 2 3 2 3 3 5 3]))
  (is (= true
        (connect-four? (play-connect-4-with [0 1 1 2 2 3 2 3 3 5 3])))))


