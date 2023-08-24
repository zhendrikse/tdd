(ns game.board
  (:gen-class))

(def RED 0)
(def YELLOW 1)
(def EMPTY 2)
(def NEW_BITBOARD 0)

(def TOTAL_ROWS 6)
(def TOTAL_COLUMNS 7)

(def MOVES_COUNTER 0)
(def BITBOARDS [NEW_BITBOARD NEW_BITBOARD])
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

(defn- bit-position [row column]
  (+ row (* column TOTAL_COLUMNS)))

(defn check-board-at [row column game]
  (cond
    (bit-test (game RED) (bit-position row column)) RED
    (bit-test (game YELLOW) (bit-position row column)) YELLOW
    :else EMPTY))

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

(defn make-move [column game]
  (-> (update-column-heights-in column
      (increment-move-counter-in
      (update-board-in game column)))))

(defn play-connect-4
  [moves game]
  (let [updated-game (make-move (first moves) game)]
    (if (= 1 (count moves))
      updated-game
      (recur (rest moves) updated-game))))

(defn play-connect-4-with
  [moves]
  (play-connect-4 moves GAME))