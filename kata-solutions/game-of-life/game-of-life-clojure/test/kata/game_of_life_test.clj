(ns kata.game-of-life-test
  (:require [clojure.test :refer :all]
            [kata.game-of-life :refer :all]))

(deftest a-living-cell-is-alive
  (testing "Living cell should be alive."
    (is (= true (alive? (living_cell 0 0))))))

(deftest a-dead-cell-is-not-alive
  (testing "Dead cell is not alive."
    (is (= false (alive? (dead_cell 0 0))))))

(deftest a-living-cell-is-not-dead
  (testing "Living cell is not dead."
    (is (= false (dead? (living_cell 0 0))))))

(deftest a-dead-cell-is-dead
  (testing "Dead cell is dead."
    (is (= true (dead? (dead_cell 0 0))))))
