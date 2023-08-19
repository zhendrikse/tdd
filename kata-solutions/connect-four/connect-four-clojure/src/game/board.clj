(ns game.board
  (:gen-class))

;; Board properties
(def total-columns 7)
(def total-rows 6)

;; Define plies for printing purposes
(def for-player-1 0)
(def for-player-2 1)
(def for-no-player 2)
(def game-symbol ["🔴", "🟡", ".."])
(def red-ply (game-symbol for-player-1))
(def yellow-ply (game-symbol for-player-2))
(def no-ply (game-symbol for-no-player))

;; Bitboard indices
(def top-left-bit-number 5)
(def bottom-right-bit-number 42)
(def y-range-of-bit-numbers (range top-left-bit-number -1 -1))
(def x-range-of-bit-numbers (range 0 (+ bottom-right-bit-number 1) total-columns))
(def board-bitnumbers
  "All bit numbers which are inside the bitboard.
  (
    (5 12 19 26 33 40 47) 
    (4 11 18 25 32 39 46) 
    (3 10 17 24 31 38 45) 
    (2 9 16 23 30 37 44) 
    (1 8 15 22 29 36 43) 
    (0 7 14 21 28 35 42)
  )"
  (vec (flatten (for [y y-range-of-bit-numbers]
                  (for [x x-range-of-bit-numbers]
                    (+ x y))))))

;; Data structure for connect four game
(def column-heights [0 7 14 21 28 35 42])
(def player-bit-boards [0 0])
(def moves-counter 0)
(def game [player-bit-boards moves-counter column-heights])

;; Board logic
(defn- increment-column-height
  [column game]
  (let [current-height ((game 2) column)]
  (assoc (game 2) column (inc current-height)))) ; // (1)

(defn- update-column-heights
  [column game]
  (assoc game 2 (increment-column-height column game)))

(defn- increment-move-counter
  [game]
  (assoc game 1 (inc (game 1)))) ; // (3)

(defn- update-board
  [column game]
  (let [move (bit-shift-left 1 ((game 2) column)) ; // (1)
        player-num (bit-and 1 (game 1))
        bitboards (game 0)
        board (bitboards player-num)]
  (assoc bitboards player-num (bit-xor move board)))) ; // (2)

(defn- update-bitboards
  [column game]
  (assoc game 0 (update-board column game)))

;; (1) Given the column col, get the index(!) of the position 
;;     stored in height for that column, shift a single bit 
;;     (1L) to that position in the binary representation of 
;;     the bitboard and store the result in move afterwards 
;;     (because the increment operator is in postfix position), 
;;     height[col] is incremented by one.
;; (2) bitboard[counter & 1] gets us the bitboard of the party 
;;     (either X or O) on turn. The bit move is simply set via the 
;;     XOR-operator on the corresponding bitboard. 
;;     bitboard[counter & 1] ^= move is a shortcut for 
;;     bitboard[counter & 1] = bitboard[counter & 1] ^ move.
;; (3) Store the column col in the history of moves, afterwards 
;;     (because ++ is again in postfix position) increment the 
;;      counter.
(defn- make-move 
  "def make_move(column):
     move = 1 << height[col]++     // (1)
     bitboard[counter & 1] ^= move // (2)
     moves[counter++] = column     // (3) <= Moves aren't stored yet"
  [column game]
  (-> (update-column-heights column 
      (increment-move-counter 
      (update-bitboards column game)))))

(defn- play-connect-4
  [moves game]
  (if (= 1 (count moves))
    (make-move (first moves) game)
    (recur (rest moves) (make-move (first moves) game))
  ))

(defn play-connect-4-with
  [moves]
  (play-connect-4 moves game))

;; Logic for printing a game
(defn- to-symbol
  [index bitboards]
  (if (bit-test (bitboards 0) index)
    red-ply
    (if (bit-test (bitboards 1) index)
      yellow-ply
      no-ply)))

(defn- map-to-string
  [game]
  (let [bitboards (game 0)
        game-as-string (vec (map #(to-symbol % bitboards) board-bitnumbers))]
    game-as-string))

(defn- print-rows
  [game-string]
  (doseq [row (range 0 total-rows)] 
    (println (for [column (range 0 total-columns)] (game-string (+ column (* row total-columns)))))))

(defn print-game
  [game]
  (let [game-string (map-to-string game)
        header (vec (map #(str % " ") (range 0 total-columns)))]
  (println header)
  (print-rows game-string)))


(defn -main
   [& args]
   (print-game (play-connect-4-with [0 1 2 3 4 5 6 3 4 3 3])))
