(ns game.printer
  (:require [game.board :as board]))

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
   (print-game (board/play-connect-4-with [0 1 2 3 4 5 6 3 4 3 3])))
