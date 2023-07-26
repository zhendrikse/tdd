(ns kata.poker-hands-test
  (:require [clojure.test :refer :all]
            [kata.poker-hands :refer :all]))

(use 'clojure.test)

(def no-score                     ["2D" "4C" "6H" "8D" "TD"])
(def high-seven                   ["2H" "3S" "4C" "5C" "7D"])
(def pair-hand                    ["2H" "2S" "4C" "5C" "7D"])
(def two-pairs-hand               ["2H" "2S" "4C" "4D" "7D"])
(def three-of-a-kind-hand         ["2H" "2S" "2C" "4D" "7D"])
(def four-of-a-kind-hand          ["2H" "2S" "2C" "2D" "7D"])
(def straight-hand                ["2H" "3S" "6C" "5D" "4D"])
(def low-ace-straight-hand        ["2H" "3S" "4C" "5D" "AD"])
(def high-ace-straight-hand       ["TH" "AS" "QC" "KD" "JD"])
(def flush-hand                   ["2H" "4H" "5H" "9H" "7H"])
(def full-house-hand              ["2H" "5D" "2D" "2C" "5S"])
(def straight-flush-hand          ["2H" "3H" "6H" "5H" "4H"])
(def low-ace-straight-flush-hand  ["2D" "3D" "4D" "5D" "AD"])
(def high-ace-straight-flush-hand ["TS" "AS" "QS" "KS" "JS"])

;; suit function on card
(deftest suit-of-heart-2 (is (= HEART (suit "2H"))))
(deftest suit-of-diamond-2 (is (= DIAMOND (suit "2D"))))
(deftest suit-of-club-2 (is (= CLUB (suit "2C"))))
(deftest suit-of-spade-3 (is (= SPADE (suit "3S"))))

;; rank function on card
(deftest rank-of-heart-2 (is (= 2 (rank "2H"))))
(deftest rank-of-spade-4 (is (= 4 (rank "4S"))))
(deftest rank-of-spade-ten (is (= 10 (rank "TS"))))
(deftest rank-of-spade-jack (is (= 11 (rank "JS"))))
(deftest rank-of-spade-quin (is (= 12 (rank "QS"))))
(deftest rank-of-spade-king (is (= 13 (rank "KS"))))
(deftest rank-of-spade-ace (is (= 14 (rank "AS"))))

;; value on hand
(deftest a-straight-flush-hand
  (is (= (list STRAIGHT_FLUSH 6) (poker-value-in straight-flush-hand))))
(deftest a-four-of-a-kind-hand
  (is (= (list FOUR_OF_A_KIND 7 2) (poker-value-in four-of-a-kind-hand))))
(deftest a-full-house-hand
  (is (= (list FULL_HOUSE 5) (poker-value-in full-house-hand))))
(deftest a-low-ace-straight-flush-hand
  (is (= (list STRAIGHT_FLUSH 5) (poker-value-in low-ace-straight-flush-hand))))
(deftest a-high-ace-straight-flush-hand
  (is (= (list STRAIGHT_FLUSH 14) (poker-value-in high-ace-straight-flush-hand))))
(deftest a-flush-hand
  (is (= (list FLUSH [9 7 5 4 2]) (poker-value-in flush-hand))))
(deftest a-three-of-a-kind-hand
  (is (= (list THREE_OF_A_KIND 2 [7 4 2 2 2]) (poker-value-in three-of-a-kind-hand))))
(deftest a-two-pair-hand
  (is (= (list TWO_PAIR 4 [7 4 4 2 2]) (poker-value-in two-pairs-hand))))
(deftest an-one-pair-hand
  (is (= (list TWO_OF_A_KIND [7 5 4 2 2]) (poker-value-in pair-hand))))
(deftest a-no-score-hand
  (is (= (list ONE_OF_A_KIND [10 8 6 4 2]) (poker-value-in no-score))))
(deftest another-no-score-hand
  (is (= (list ONE_OF_A_KIND [7 5 4 3 2]) (poker-value-in high-seven))))
(deftest a-low-ace-straight-hand
  (is (= (list STRAIGHT 5) (poker-value-in low-ace-straight-hand))))
(deftest a-high-ace-straight-hand
  (is (= (list STRAIGHT 14) (poker-value-in high-ace-straight-hand))))

(deftest a-straight-hand
  (is (= true (straight? straight-hand))))
(deftest not-a-straight-hand-where-max-value-minus-min-value-equals-4
  (is (= false (straight? ["2H" "3S" "6C" "5D" "5S"]))))

(run-tests)
