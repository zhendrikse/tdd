(ns game.check-board
  (:require [game.board :as board]))

(defn bit-check
  [board x]
  (bit-and board (bit-shift-right board x)))

(defn check-board-4
  "Checks whether given bitboard has 4 connected coins."
  [bitboard]
  (map bit-check
       (map (partial bit-check bitboard) [6 7 8 1])
       [12 14 16 2]))

(defn check-board-3
  "Checks whether given bitboard has 3 connected coins."
  [bitboard]
  (map #(bit-check (bit-check bitboard %) %) [6 7 8 1]))

(defn check-board-2
  "Checks whether given bitboard has 2 connected coins."
  [bitboard]
  (map (partial bit-check bitboard) [6 7 8 1]))

(defn check-board-in
  "Checks whether given bitboard has won."
  [game]
  (let [combined-bitboards (+ ((game 0) 0) ((game 0) 1))]
  (apply bit-or (check-board-4 combined-bitboards))))

(defn connect-four?
  [game]
  (not (= 0 (check-board-in game))))