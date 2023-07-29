(ns kata.game-of-life-test
  (:require [clojure.test :refer :all]
            [kata.game-of-life :refer :all]))

(def LIVING-CELL (living-cell 0 0))
(def DEAD-CELL (dead-cell 0 0))

(deftest a-living-cell-is-is-alive
  (testing "Living cell should be is-alive."
    (is (is-alive? LIVING-CELL))))

(deftest a-dead-cell-is-not-is-alive
  (testing "Dead cell is not is-alive."
    (is (not (is-alive? DEAD-CELL)))))

(deftest a-living-cell-is-not-dead
  (testing "Living cell is not dead."
    (is (not (is-dead? LIVING-CELL)))))

(deftest a-dead-cell-is-dead
  (testing "Dead cell is dead."
    (is (is-dead? DEAD-CELL))))

(deftest map-living-cell-to-dead-cell
  (testing "Map living cell to dead cell.")
    (is (is-dead? (to-dead-cell is-alive? LIVING-CELL))))

(deftest map-dead-cell-to-dead-cell
  (testing "Map dead cell to dead cell.")
    (is (is-dead? (to-dead-cell is-alive? DEAD-CELL))))

(deftest map-dead-cell-to-living-cell
  (testing "Map dead cell to living cell.")
    (is (is-alive? (to-living-cell is-dead? DEAD-CELL))))

(deftest map-living-cell-to-living-cell
  (testing "Map living cell to living cell.")
    (is (is-alive? (to-living-cell is-dead? LIVING-CELL))))

(def GAME (list 
           (dead-cell 0 0)   (living-cell 0 1) (living-cell 0 2)
           (living-cell 1 0) (living-cell 1 1) (dead-cell 1 2)
           (dead-cell 2 0)   (living-cell 2 1) (dead-cell 2 2)))

(deftest neighbours-of-center-cell 
  (testing "Neighbours of center cell.") 
    (is 8 (count (filter (is-neighbour-of? (living-cell 1 1)) GAME))))

(deftest neighbours-of-top-center-cell 
  (testing "Neighbours of top center cell.") 
    (is 5 (count (filter (is-neighbour-of? (living-cell 0 1)) GAME))))

(deftest neighbours-of-bottom-center-cell 
  (testing "Neighbours of bottom center cell.") 
    (is 5 (count (filter (is-neighbour-of? (living-cell 2 1)) GAME))))

(deftest neighbours-of-right-edge-center-cell 
  (testing "Neighbours of right edge center cell.") 
    (is 5 (count (filter (is-neighbour-of? (living-cell 1 2)) GAME))))

(deftest living-neighbours-of-center-cell
  (testing "Living neighbours of center cell.")
    (is (= 4 (count ((living-neighbours-in GAME) (living-cell 1 1))))))

(deftest has-has-exactly-three-living-neighbours
  (testing "Filter out all cells that have exactly 3 living neighbours")
    (is (= 4 (count (filter (has-exactly-three? (living-neighbours-in GAME)) GAME)))))

(deftest has-has-more-than-three-living-neighbours
  (testing "Filter out all cells that have more than 3 living neighbours")
    (is (= 2 (count (filter (has-more-than-three? (living-neighbours-in GAME)) GAME)))))

(deftest has-has-less-than-two-living-neighbours
  (testing "Filter out all cells that have less than 2 living neighbours")
    (is (= 0 (count (filter (has-less-than-two? (living-neighbours-in GAME)) GAME)))))

(def BLINKER_START (list 
           (dead-cell 0 0) (living-cell 0 1) (dead-cell 0 2)
           (dead-cell 1 0) (living-cell 1 1) (dead-cell 1 2)
           (dead-cell 2 0) (living-cell 2 1) (dead-cell 2 2) ))

(def BLINKER_END (list 
           (dead-cell 0 0)   (dead-cell 0 1)   (dead-cell 0 2)
           (living-cell 1 0) (living-cell 1 1) (living-cell 1 2)
           (dead-cell 2 0)   (dead-cell 2 1)   (dead-cell 2 2) ))


(deftest next-iteration-of-blinker
  (testing "Next iteration of blinker.")
  (is (= BLINKER_END (next-generation-of BLINKER_START))))
