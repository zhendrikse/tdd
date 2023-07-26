(ns kata.poker-hands
  (:gen-class))

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
