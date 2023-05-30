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

(defn suit [card-as-string]
  (str (let [[_ suit] card-as-string] suit)))

(defn- value-as-char [card-as-string]
  (let [[value _] card-as-string] value))

(defn rank [card-as-string]
  (let [card-value (value-as-char card-as-string)]
    (if (Character/isDigit card-value)
      (Integer/valueOf (str card-value))
      (REPLACEMENTS card-value))))

(defn flush? [hand]
  (let [[number-of different-suits-in-hand] [count (set (map suit hand))]]
    (= (number-of different-suits-in-hand) 1)))

(defn- sorted-ranks-in
  "Sort the ranks in the hand in descending order where an ace has a value of one"
  [hand]
  (let [sorted-ranks-in-hand (reverse (sort (map rank hand)))
        hand-with-ace `(14 5 4 3 2)]
    (if
     (= sorted-ranks-in-hand hand-with-ace) `(5 4 3 2 1)
     sorted-ranks-in-hand)))

(defn- max-rank-in [hand]  (apply max (sorted-ranks-in hand)))
(defn- min-rank-in [hand]  (apply min (sorted-ranks-in hand)))

(defn card-with-frequency
  [n ranks]
  (let [count-occurrences-of
        (fn [card-value] (fn [ranks] (count (filter (fn [value] (= value card-value)) ranks))))
        cards-contained-n-times
        (fn [value] (= ((count-occurrences-of value) ranks) n))]
    (first (filter cards-contained-n-times ranks))))

(defn- n-of-a-kind? [n] (fn [hand] (not= (card-with-frequency n (sorted-ranks-in hand)) nil)))

(defn four-of-a-kind? [hand] ((n-of-a-kind? 4) hand))

(defn- three-of-a-kind? [hand] ((n-of-a-kind? 3) hand))

(defn- pair? [hand] ((n-of-a-kind? 2) hand))

(defn- high-pair-card [hand] (card-with-frequency 2 (sorted-ranks-in hand)))
(defn- low-pair-card [hand] (card-with-frequency 2 (reverse (sorted-ranks-in hand))))

(defn- two-pairs? [hand]
  (not (= (high-pair-card hand) (low-pair-card hand))))

(defn full-house? [hand] (and (pair? hand) (three-of-a-kind? hand)))

(defn straight? [hand]
  (let [different-values-in-hand (count (set (sorted-ranks-in hand)))]
    (and
     (= (- (max-rank-in hand) (min-rank-in hand)) 4)
     (= different-values-in-hand 5))))

(defn straight-flush? [hand]  (and (straight? hand) (flush? hand)))

(defn poker-value-in [hand]
  (let [sorted-ranks-in-hand (into [] (sorted-ranks-in hand))]
    (cond
      (straight-flush? hand) (list STRAIGHT_FLUSH (max-rank-in hand))
      (four-of-a-kind? hand) (list FOUR_OF_A_KIND (max-rank-in hand) (min-rank-in hand))
      (full-house? hand) (list FULL_HOUSE  (max-rank-in hand))
      (flush? hand) (list FLUSH sorted-ranks-in-hand)
      (straight? hand) (list STRAIGHT (max-rank-in hand))
      (three-of-a-kind? hand) (list THREE_OF_A_KIND (card-with-frequency 3 sorted-ranks-in-hand) sorted-ranks-in-hand)
      (two-pairs? hand) (list TWO_PAIR (high-pair-card hand) sorted-ranks-in-hand)
      (pair? hand) (list TWO_OF_A_KIND sorted-ranks-in-hand)
      (= true true) (list ONE_OF_A_KIND sorted-ranks-in-hand))))

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
