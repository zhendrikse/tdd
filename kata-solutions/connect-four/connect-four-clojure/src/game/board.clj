(ns game.board
  (:gen-class))

(def for-player-1 0)
(def for-player-2 1)
(def for-no-player 2)
(def game-symbol ["🔴", "🟡", ".."])
(def red-ply (game-symbol for-player-1))
(def yellow-ply (game-symbol for-player-2))
(def no-ply (game-symbol for-no-player))

(def board-for-player-1 0)
(def board-for-player-2 0)
(def initial-game
  [board-for-player-1 board-for-player-2 for-player-1])

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

(defn- current-player
       [in-game]
       (get in-game 2))

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

(defn- insert-ply-at
  [column in-game]
  (let [row (first-free-row-in column in-game)
        current-player (current-player in-game)
        other-player (bit-xor 1 current-player)]
    (-> (assoc in-game 2 other-player)
        (assoc current-player (bit-insert-at row column (in-game current-player))))))

(defn board-full? [game]
  (empty? (filter #(not (bit-test (combined-player-board game) %)) board-bitnumbers)))

(defn- generate-game-state-for 
  [game]
  (let [bit-is-set-in (fn[board row column] (bit-test board (bit-index-for row column)))]
  (for [row y-range-of-bit-numbers]
    (vec (for [column (range 0 total-columns)]
           (if  (bit-is-set-in (game for-player-1) row column) red-ply
             (if (bit-is-set-in (game for-player-2) row column) yellow-ply
               no-ply)))))))

(defn print-board
  [game]
  (println (vec (map #(str % " ") (range 0 total-columns))))
  (doseq [row (generate-game-state-for game)]
    (println row)))

(defn- play-connect-4
  [moves game]
  (if (= 1 (count moves))
    (insert-ply-at (first moves) game)
    (recur (rest moves) (insert-ply-at (first moves) game))
  ))

(defn play-connect-4-with
  [moves]
  (play-connect-4 moves initial-game))

(defn -main
  [& args]
  (print-board (play-connect-4-with [0 1 2 3 4 5 6 3 4 3 3])))
