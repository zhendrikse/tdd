; ------------------------------- 
; U n i t  t e s t  l i b r a r y
; -------------------------------

(defn execute-test [text, expected, actual]
  (if (= actual expected) 
      (str "Running " text "... ok")
          (str "Running " text "... failed, expected >>" expected "<< but was >>" actual "<<")
            )
            )

; ------------------
; G r e e d  c o d e
; ------------------

; Rules of the game
(def triple-scores {1 1000, 2 200, 3 300, 4 400, 5 500, 6 600})
(def single-scores {1 100, 2 0, 3 0, 4 0, 5 50, 6 0})
(def score-map {1 single-scores, 3 triple-scores})

(defn count-occurrences [value dice-list]
  (count (filter #(= value %) dice-list))
  )

(defn determine-score [x times dice-list]
      (+ (if (>= (count-occurrences x dice-list) times) (get (get score-map times) x) 0))
      )

(defn score-frequency [times dice-list]
  (reduce +  (map #(determine-score % times dice-list) (range 1 7)) )
  )

(defn score [dice-list]
  (+ (score-frequency 1 dice-list) (score-frequency 3 dice-list))
  )

; ------------------
; U n i t  t e s t s
; ------------------
(execute-test "single one in list scores 100" 100  (score '(1 4 2 4 6 6)))
(execute-test "not a single one in list scores 0" 0 (score '(3 4 2 4 6 6))) 
(execute-test "double one in list scores 100" 100 (score '(1 4 1 4 6 6)))
(execute-test "single five in list scores 50" 50 (score '(3 4 2 4 5 6)))
(execute-test "double five in list scores 50" 50 (score '(5 4 2 4 5 6)))
(execute-test "single five and single in list scores 150" 150 (score '(1 4 2 4 5 6)))
(execute-test "triple one in list scores 1100" 1100 (score '(1 2 4 6 1 1)))
(execute-test "triple two in list scores 200" 200 (score '(2 6 4 6 2 2)))
(execute-test "triple three in list scores 300" 300 (score '(3 2 4 6 3 3)))
(execute-test "triple four in list scores 400" 400 (score '(3 2 4 6 4 4)))
(execute-test "triple five in list scores 550" 550 (score '(5 2 4 6 5 5)))
(execute-test "triple six in list scores 600" 600 (score '(3 2 4 6 6 6)))

(execute-test "test case 1 from kata scores 1150" 1150 (score '(1 1 1 5 1)))
(execute-test "test case 2 from kata scores 0" 0 (score '(2 3 4 6 2)))
