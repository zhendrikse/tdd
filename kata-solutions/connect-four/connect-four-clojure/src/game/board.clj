(ns game.board
  (:gen-class))

(def player ["_", "X", "O"])

(def board-player-1 0)
(def board-player-2 0)
(def turn-player-1 0)
(def turn-player-2 1)

(def in-initial-game
  [board-player-1 board-player-2 turn-player-1])

(def total-rows 6)
(def total-columns 7)






(def top-left-bit-number 5)
(def bottom-right-bit-number 42)

(def y-range-of-bit-numbers (range top-left-bit-number -1 -1))
(def x-range-of-bit-numbers (range 0 (+ bottom-right-bit-number 1) total-columns))
(def board-bitnumbers
  "All bit numbers which are inside the bitboard."
  ;; (
  ;;   (5 12 19 26 33 40 47) 
  ;;   (4 11 18 25 32 39 46) 
  ;;   (3 10 17 24 31 38 45) 
  ;;   (2 9 16 23 30 37 44) 
  ;;   (1 8 15 22 29 36 43) 
  ;;   (0 7 14 21 28 35 42)
  ;; )
  (vec (flatten (for [y y-range-of-bit-numbers]
                  (for [x x-range-of-bit-numbers]
                    (+ x y))))))






(defn- bit-index-for 
  [row column]
  (+ row (* column total-columns)))

(defn- bit-insert-at
  [row column in-board]
  (bit-set in-board (bit-index-for row column)))

(defn- combined-player-board
       [game]
       (+ (game 0) (game 1)))

(defn- first-free-row-in
  [column in-game]
    (let [board (combined-player-board in-game)
          bit-off? (fn[row] (not (bit-test board (bit-index-for row column))))]
      (first (filter bit-off? (range 0 (+ 1 total-rows))))))
      
(defn column-full-for?
  [column in-game]
  (= total-rows (first-free-row-in column in-game)))

(defn insert-ply-at
  [column in-game]
  (let [row (first-free-row-in column in-game)
        player-num (in-game 2)]
    (-> (assoc in-game 2 (bit-xor 1 player-num))
        (assoc player-num (bit-insert-at row column (in-game player-num))))))






(defn bit-insert
  [board row column]
  (bit-set board (+ row (* column 7))))

(defn get-y
  "Determines y-coordinate for given x-coordinate."
  [board column]
  (first (filter #(not (bit-test board (+ % (* column total-columns))))
                 (range 0 total-rows))))

(defn insert
  "Inserts symbol for given player (either 1 or 2) at specified x
  and sets according bit on his bitboard."
  [boards x player-num]
  (let [y (get-y (boards 0) x)]
    (if (nil? y) nil
      (-> (assoc boards 0 (bit-insert (boards 0) y x))
          (assoc player-num (bit-insert (boards player-num) y x))))))

(defn board-full? [boards]
  (empty? (filter #(not (bit-test (boards 0) %)) board-bitnumbers)))

(defn gen-game-state [boards]
  (for [y (range 5 -1 -1)]
    (vec (for [x (range 0 7)]
           (if (bit-test (boards 1) (+ y (* 7 x))) (player 1)
             (if (bit-test (boards 2) (+ y (* 7 x))) (player 2)
               (player 0)))))))

(defn print-board
  [boards]
  (println [1 2 3 4 5 6 7])
  (doseq [row (gen-game-state boards)]
    (println row)))


(defn -main
  [& args]
  ;(print-board (insert (insert (insert( insert (insert (insert (insert in-initial-game 1 1) 1 2) 1 1) 1 2) 1 1) 1 2) 1 1)))
  (print-board (insert (insert( insert (insert (insert (insert in-initial-game 1 1) 1 2) 1 1) 1 2) 1 1) 1 2)))
  ;(print-board (insert (insert in-initial-game 0 1) 0 2)))
  ;(print-board (insert in-initial-game 0 1)))
  ;(print-board in-initial-game))
  ;(println (get-y (get in-initial-game 0) 0)))
