(def HEART "H")
(def SPADE "S")
(def CLUB "C")
(def DIAMOND "D")
(def REPLACEMENTS {\T 10, \J 11, \Q 12, \K 13, \A 14})
(def STRAIGHT_FLUSH 8)
(def FOUR_OF_A_KIND 7)
(def FULL_HOUSE 6)
(def FLUSH 5)
(def STRAIGHT 4)
(def THREE_OF_A_KIND 3)
(def TWO_PAIR 2)
(def TWO_OF_A_KIND 1)
(def ONE_OF_A_KIND 0)

; ------------------
; U n i t  t e s t s
; ------------------
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