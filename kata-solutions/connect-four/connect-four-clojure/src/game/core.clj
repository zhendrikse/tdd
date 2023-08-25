(ns game.core
  (:require [game.printer :refer :all]
            [game.board :refer :all]))

(defn read-input [player-num]
  (printf "Player %d's turn [human]: " (inc player-num)) (flush)
  (dec (Integer/parseInt (or (re-find #"^\d+" (read-line)) "0"))))

;; (defn prompt-input [player-num boards]
;;   (first (drop-while
;;           #(or (> % 6) (< % 0)
;;                (nil? (board/insert boards % player-num)))
;;           (repeatedly #(read-input player-num)))))

(defn- game-end? [game] (or (connect-four? game) (is-full? game)))

(defn- game-exit [game]
  (let [previous-player (bit-xor 1 (current-player-in game))]
    (if 
      (connect-four? game) 
        (println (str "Player " (inc previous-player) " has won!"))
        (println (str "It's a draw!")))))

(defn ai-move [game] (rand-int WIDTH))

(defn- play-game
  [game]
    (let [current-player (current-player-in game)]
    (print-game game)
    (if (game-end? game) 
      (game-exit game)
      (if (= current-player RED)
        (recur (make-move (read-input current-player) game))
        (recur (make-move (ai-move game) game))))))

(defn -main
   [& args]
   (play-game GAME))
   