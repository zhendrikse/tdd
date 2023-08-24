(ns game.printer
  (:require [game.board :refer :all]))

;; Define plies for printing purposes
(def red "🔴")
(def yellow "🟡")
(def none "..")

;; Bitboard indices
(def top-left-bit-number 5)
(def bottom-right-bit-number 42)
(def y-range-of-bit-numbers (range top-left-bit-number -1 -1))
(def x-range-of-bit-numbers (range 0 (+ bottom-right-bit-number 1) TOTAL_COLUMNS))
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

;; Logic for printing a game
(defn- map-to-symbol
  [game bitboard-index]
  (cond 
    (bit-test (get game RED) bitboard-index) red
    (bit-test (get game YELLOW) bitboard-index) yellow
    :else none))

(defn- map-to-string
  [game]
  (vec (map (partial map-to-symbol game) board-bitnumbers)))

(defn- index-in
    [game-string row column]
       (game-string (+ column (* row TOTAL_COLUMNS))))
    
(defn- print-rows
  [game-string]
  (doseq [row (range 0 TOTAL_ROWS)] 
    (println 
     (for [column (range 0 TOTAL_COLUMNS)] 
       (index-in game-string row column)))))

(defn print-game
  [game]
  (let [game-string (map-to-string game)
        header (vec (map (partial str " ") (range 1 (inc TOTAL_COLUMNS))))]
  (println header)
  (print-rows game-string)))