(ns game.board
  (:gen-class))

;; Data structure for connect four game
(def column-heights [0 7 14 21 28 35 42])
(def player-bit-boards [0 0])
(def moves-counter 0)
(def game [player-bit-boards moves-counter column-heights])
(def bitboards 0)
(def counter 1)
(def columns 2)

;; Board logic
(defn- column-height-for
  [column, game]
  ((get game columns) column))

(defn- increment-column-height
  [column game]
  (let [current-height (column-height-for column game)
        updated-height (inc current-height)]
  (assoc (get game columns) column updated-height))) ; // (1)

(defn- update-bitboard-in
  [game column]
  (let [move (bit-shift-left 1 (column-height-for column game)) ; // (1)
        player-num (bit-and 1 (get game counter))
        bitboards (get game bitboards)
        board (bitboards player-num)
        updated-board (bit-xor move board)]
  (assoc bitboards player-num updated-board))) ; // (2)

(defn- increment-move-counter
  [game]
  (let [updated-game-counter (inc (get game counter))]
  (assoc game counter updated-game-counter))) ; // (3)

(defn- update-column-heights
  [column game]
  (let [updated-columns (increment-column-height column game)]
  (assoc game columns updated-columns)))

(defn- update-bitboards-in
  [game with-column]
  (let [updated-bitboards (update-bitboard-in game with-column)]
    (assoc game bitboards updated-bitboards)))

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
  [game column]
  (-> (update-column-heights column       ; // (1)
      (increment-move-counter             ; // (3)
      (update-bitboards-in game column)))))  ; // (2)

(defn- play-connect-4
  [moves game]
  (let [updated-game (make-move game (first moves))]
  (if (= 1 (count moves))
    updated-game
    (recur (rest moves) updated-game)
  )))

(defn play-connect-4-with
  [moves]
  (play-connect-4 moves game))

