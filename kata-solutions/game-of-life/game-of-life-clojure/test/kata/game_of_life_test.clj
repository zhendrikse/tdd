(ns kata.game-of-life-test
  (:require [clojure.test :refer :all]
            [kata.game-of-life :refer :all]))

(def LIVING-CELL (living-cell 0 0))
(def DEAD-CELL (dead-cell 0 0))

(deftest a-living-cell-is-alive
  (testing "Living cell should be alive."
    (is (alive? LIVING-CELL))))

(deftest a-dead-cell-is-not-alive
  (testing "Dead cell is not alive."
    (is (not (alive? DEAD-CELL)))))

(deftest a-living-cell-is-not-dead
  (testing "Living cell is not dead."
    (is (not (dead? LIVING-CELL)))))

(deftest a-dead-cell-is-dead
  (testing "Dead cell is dead."
    (is (dead? DEAD-CELL))))

(deftest map-living-cell-to-dead-cell
  (testing "Map living cell to dead cell.")
    (is (dead? (to-dead-cell alive? LIVING-CELL))))

(deftest map-dead-cell-to-dead-cell
  (testing "Map dead cell to dead cell.")
    (is (dead? (to-dead-cell alive? DEAD-CELL))))

(deftest map-dead-cell-to-living-cell
  (testing "Map dead cell to living cell.")
    (is (alive? (to-living-cell dead? DEAD-CELL))))

(deftest map-living-cell-to-living-cell
  (testing "Map living cell to living cell.")
    (is (alive? (to-living-cell dead? LIVING-CELL))))
