(ns game.core
  (:require [game.check-board :refer :all]
            [game.printer :refer :all]
            [game.board :refer :all]))

(defn read-input [player-num]
  (printf "Player %d's turn [human]: " (inc player-num)) (flush)
  (dec (Integer/parseInt (or (re-find #"^\d+" (read-line)) "0"))))

;; (defn prompt-input [player-num boards]
;;   (first (drop-while
;;           #(or (> % 6) (< % 0)
;;                (nil? (board/insert boards % player-num)))
;;           (repeatedly #(read-input player-num)))))

(defn- connect-four-for?
  [current-player game]
  (not= 0 (connect-four? (bitboard-for-player-in game current-player))))

(defn- play-game
  [game]
    (let [current-player (current-player-in game)
          move (read-input current-player)
          updated-game (play-connect-4 [move] game)]
    (print-game updated-game)
    (if (connect-four-for? current-player updated-game)
      (println (str "Player " (inc current-player) " has won!"))
      (recur updated-game))))
  
(defn -main
   [& args]
   (print-game new-game)
   (play-game new-game))
   