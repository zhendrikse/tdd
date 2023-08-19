(ns game.printer
  (:require [game.board :refer :all]))

;; Board properties
(def total-columns 7)
(def total-rows 6)

;; Define plies for printing purposes
(def red-ply "🔴")
(def yellow-ply "🟡")
(def no-ply "..")

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

;; Logic for printing a game
(defn- map-to-symbol
  [bitboards bitboard-index]
  (if (bit-test (get bitboards player-1) bitboard-index)
    red-ply
    (if (bit-test (get bitboards player-2) bitboard-index)
      yellow-ply
      no-ply)))

(defn- map-to-string
  [game]
  (let [bitboards (get game bitboards)]
    (vec (map (partial map-to-symbol bitboards) board-bitnumbers))))

(defn- index-in
    [game-string row column]
       (game-string (+ column (* row total-columns))))
    
(defn- print-rows
  [game-string]
  (doseq [row (range 0 total-rows)] 
    (println 
     (for [column (range 0 total-columns)] 
       (index-in game-string row column)))))

(defn print-game
  [game]
  (let [game-string (map-to-string game)
        header (vec (map (partial str " ") (range 1 (inc total-columns))))]
  (println header)
  (print-rows game-string)))



