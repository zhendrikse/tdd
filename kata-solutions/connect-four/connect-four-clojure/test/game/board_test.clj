(ns game.board-test
  (:require [clojure.test :refer :all]
            [game.board :refer :all]))

(def second-column 1)

(deftest first-player-first-move-in-second-column
  (is (= [128 128 0] 
         (insert-for-player-one-at second-column in-initial-game))))

(deftest second-player-first-move-in-second-column
  (is (= [384 128 256] 
         (insert-for-player-two-at second-column
           (insert-for-player-one-at second-column in-initial-game)))))

(deftest first-player-second-move-in-second-column
  (is (= [896 640 256]
         (insert-for-player-one-at second-column
           (insert-for-player-two-at second-column
             (insert-for-player-one-at second-column in-initial-game))))))

