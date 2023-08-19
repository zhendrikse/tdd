(ns game.board-test
  (:require [clojure.test :refer :all]
            [game.board :refer :all]))

(def column-two 1)

(deftest first-player-first-move-in-column-two
  (is (= [[128 0] 1 [0 8 14 21 28 35 42]] 
         (play-connect-4-with [column-two]))))

(deftest second-player-first-move-in-column-two
  (is (= [[128 256] 2 [0 9 14 21 28 35 42]] 
         (play-connect-4-with [column-two, column-two]))))

(deftest first-player-second-move-in-column-two
  (is (= [[640 256] 3 [0 10 14 21 28 35 42]]
         (play-connect-4-with [column-two, column-two, column-two]))))

;; (deftest full-column-when-with-six-plies-in-column-two
;;   (is (= true
;;          (column-full-for? column-two
;;           (play-connect-4-with [column-two, column-two, column-two, column-two, column-two, column-two])))))
