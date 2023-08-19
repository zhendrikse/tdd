(ns game.check-board
  (:require [game.board :as board]))

(defn and-board-with-right-shifted
  [board by-x-bits]
  (bit-and board (bit-shift-right board by-x-bits)))

(defn check-board-4
  "Checks whether given bitboard has 4 connected coins."
  [bitboard]
  (map and-board-with-right-shifted
       (map (partial and-board-with-right-shifted bitboard) [6 7 8 1])
       [12 14 16 2]))

(defn check-board-3
  "Checks whether given bitboard has 3 connected coins."
  [bitboard]
  (map #(and-board-with-right-shifted (and-board-with-right-shifted bitboard %) %) [6 7 8 1]))

(defn check-board-2
  "Checks whether given bitboard has 2 connected coins."
  [bitboard]
  (map (partial and-board-with-right-shifted bitboard) [6 7 8 1]))

(defn connect-four?
  "Checks whether given bitboard has won."
  [bitboard]
  (apply bit-or (check-board-4 bitboard)))
