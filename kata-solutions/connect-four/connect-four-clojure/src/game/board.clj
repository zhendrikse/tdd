(ns game.board
  (:gen-class))

(def RED 0)
(def YELLOW 1)
(def EMPTY 2)
(def NEW_BITBOARD 0)

(def TOTAL_ROWS 6)
(def TOTAL_COLUMNS 7)

(def MOVES_COUNTER 0)
(def BITBOARD_COLUMN_INDICES [0 7 14 21 28 35 42])
(def GAME [NEW_BITBOARD NEW_BITBOARD MOVES_COUNTER BITBOARD_COLUMN_INDICES])
(def MOVES_COUNTER_INDEX 2)
(def COLUMNS_INDEX 3)

(defn current-player-in
  [game]
  (bit-and 1 (game MOVES_COUNTER_INDEX)))

(defn- increment-move-counter-in
  [game]
  (let [updated-game-counter (inc (get game MOVES_COUNTER_INDEX))]
    (assoc game MOVES_COUNTER_INDEX updated-game-counter))) 

(defn- update-bitboard [bitboard bit-index]
  (let [move (bit-shift-left 1 bit-index)]
  (bit-xor move bitboard)))

(defn- update-board-in [game column]
  (let [player (current-player-in game) 
        bitboard (game player)
        bit-index ((game COLUMNS_INDEX) column)
        updated-bitboard (update-bitboard bitboard bit-index)]
   (assoc game player updated-bitboard)))

(defn- column-height-for
  [column, game]
  ((get game COLUMNS_INDEX) column))

(defn- increment-column-height
  [column game]
  (let [current-height (column-height-for column game)
        updated-height (inc current-height)]
    (assoc (get game COLUMNS_INDEX) column updated-height))) 

(defn- update-column-heights-in
  [column game]
  (let [updated-columns (increment-column-height column game)]
    (assoc game COLUMNS_INDEX updated-columns)))

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
(defn make-move 
  "def make_move(column):          // Pseudo code
     move = 1 << height[col]++     // (1)
     bitboard[counter & 1] ^= move // (2)
     moves[counter++] = column     // (3) <= Moves aren't stored yet"
  [column game]
  (-> (update-column-heights-in column  ; // (1)
      (increment-move-counter-in        ; // (3)
      (update-board-in game column))))) ; // (2)

(defn play-connect-4
  [moves game]
  (let [updated-game (make-move (first moves) game)]
    (if (= 1 (count moves))
      updated-game
      (recur (rest moves) updated-game))))

(defn play-connect-4-with
  [moves]
  (play-connect-4 moves GAME))