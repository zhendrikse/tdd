(ns game.check-board-test
  (:require [clojure.test :refer :all]
            [game.check-board :refer :all]
            [game.printer :refer :all]
            [game.board :refer :all]))

(defn player-has-connect-four?
  [player moves]
  (not= 0 (connect-four? (bitboard-for-player-in (play-connect-4-with moves) player))))

(deftest check-bug-configuration
  ;(print-game (play-connect-4-with [3 3]))
  (is (not (player-has-connect-four? player-1 [3 3])))
  (is (not (player-has-connect-four? player-2 [3 3]))))

(deftest check-horizontal-four-player-one
  ;(print-game (play-connect-4-with [0 0 1 1 2 2 3]))
  (is (player-has-connect-four? player-1 [0 0 1 1 2 2 3]))
  (is (not (player-has-connect-four? player-2 [0 0 1 1 2 2 3]))))

(deftest check-horizontal-four-player-two
  ;(print-game (play-connect-4-with [0 1 1 2 2 3 3 4]))
  (is (not (player-has-connect-four? player-1 [0 1 1 2 2 3 3 4])))
  (is (player-has-connect-four? player-2 [0 1 1 2 2 3 3 4])))

(deftest check-vertical-four-player-one
  ;(print-game (play-connect-4-with [0 1 0 1 0 1 0]))
  (is (player-has-connect-four? player-1 [0 1 0 1 0 1 0]))
  (is (not (player-has-connect-four? player-2 [0 1 0 1 0 1 0]))))

(deftest check-vertical-four-player-two
  ;(print-game (play-connect-4-with [0 1 0 1 0 1 2 1]))
  (is (not (player-has-connect-four? player-1 [0 1 0 1 0 1 2 1])))
  (is (player-has-connect-four? player-2 [0 1 0 1 0 1 2 1])))

(deftest check-diagonal-four-player-one
  ;(print-game (play-connect-4-with [0 1 1 2 2 3 2 3 3 5 3]))
  (is (player-has-connect-four? player-1 [0 1 1 2 2 3 2 3 3 5 3]))
  (is (not (player-has-connect-four? player-2 [0 1 1 2 2 3 2 3 3 5 3]))))


