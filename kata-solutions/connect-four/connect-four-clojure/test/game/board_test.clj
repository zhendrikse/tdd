(ns game.board-test
  (:require [clojure.test :refer :all]
            [game.board :refer :all]))

(def second-column 1)

(deftest first-player-first-move-in-second-column
  (is (= [128 0 1] 
         (insert-ply-at second-column in-initial-game))))

(deftest second-player-first-move-in-second-column
  (is (= [128 256 0] 
         (insert-ply-at second-column
           (insert-ply-at second-column in-initial-game)))))

(deftest first-player-second-move-in-second-column
  (is (= [640 256 1]
         (insert-ply-at second-column
           (insert-ply-at second-column
             (insert-ply-at second-column in-initial-game))))))

(deftest full-column-when-with-six-plies-in-second-column
  (is (= true
         (column-full-for? second-column
          (insert-ply-at second-column
           (insert-ply-at second-column
            (insert-ply-at second-column
             (insert-ply-at second-column
              (insert-ply-at second-column
               (insert-ply-at second-column in-initial-game))))))))))
