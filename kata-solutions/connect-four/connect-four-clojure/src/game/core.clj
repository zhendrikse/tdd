(ns game.core
  (:require [game.printer :refer :all]
            [game.board :refer :all]))

(def TOTAL_MOVES (/ (* WIDTH HEIGHT) 2))

(defn read-input [player-num]
  (printf "Player %d's turn [human]: " (inc player-num)) (flush)
  (dec (Integer/parseInt (or (re-find #"^\d+" (read-line)) "0"))))

;; (defn prompt-input [player-num boards]
;;   (first (drop-while
;;           #(or (> % 6) (< % 0)
;;                (nil? (board/insert boards % player-num)))
;;           (repeatedly #(read-input player-num)))))

(defn- game-end? [game] (or (connect-four? game) (is-full? game)))

(defn- game-exit 
  [game]
  (let [previous-player (bit-xor 1 (current-player-in game))]
    (if (connect-four? game)  
      (println (str "Player " (inc previous-player) " has won!")) 
      (println (str "It's a draw!")))))


(defn- can-play? [move game] (not (is-full? game move)))

(defn- is-winning-move?
  [move game]
  (connect-four? (make-move move game)))

;; (defn- negamax 
;;   [game move]
;;   (if (and (can-play? move game) (is-winning-move? move game))
;;     (/ (- (* WIDTH HEIGHT) (game MOVES_COUNTER_INDEX)) 2)
;;     0))

(defn- rate-move 
  [game move]
  (let [moves-made (/ (dec (game MOVES_COUNTER_INDEX)) 2)
        moves-left (- TOTAL_MOVES moves-made)
        score moves-left]
  (if (is-winning-move? move game)
    score
    0)))

(defn rate-moves 
  [game] 
  (map (partial rate-move game) (range WIDTH)))

(defn- equal-ratings? [move-ratings] (apply = move-ratings))

(defn generate-ai-move [game]
  (let [move-ratings (rate-moves game)
        best-move (.indexOf move-ratings (apply max move-ratings))] 
    (if (equal-ratings? move-ratings)
      ((vec (range WIDTH)) (rand-int WIDTH))
      best-move)))

(defn- play-game
  [game] 
  (let [current-player (current-player-in game)]
    (print-game game)
    (if (game-end? game) 
      (game-exit game)
      (if (= current-player RED)
        (recur (make-move (read-input current-player) game))
        (recur (make-move (generate-ai-move game) game))))))


(defn -main
   [& args]
   (play-game GAME))
   