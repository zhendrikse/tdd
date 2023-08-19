(ns game.board
  (:gen-class))

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

