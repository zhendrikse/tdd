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

(defn is-winning-move? [column]
  (fn [board] (connect-four? (make-move column board))))

(defn can-play? [column]
  (fn [board] (not (is-full? board column))))

(defn- possible-moves-on [board] 
  (filter #((can-play? %) board) (range WIDTH)))

(defn- winning-move-is-possible? [board] (any? (map (is-winning-move? (possible-moves-on board)))))

(defn- score [board] (- TOTAL_MOVES (quot (board MOVES_COUNTER_INDEX) 2)))

(defn negamax-algo
  [board previous-score depth]
  (cond 
    (is-full? board)
    0
    (winning-move-is-possible? board)
      (score board) 
    (= 0 depth) 
      previous-score 
    :else
      (for [move (possible-moves-on board) 
            score (- (negamax-algo (make-move move board) previous-score (dec depth)))] 
          (max score previous-score))))

(defn negamax 
  [board]
  (negamax-algo board (- (* WIDTH HEIGHT)) 3))

(defn generate-ai-move [board]
  (let [possible-boards (map #(make-move % board) (possible-moves-on board))
        move-ratings (map negamax possible-boards)
        best-score (apply max move-ratings)
        best-move (.indexOf move-ratings best-score)]
    (println "Best move is " (inc best-move) " in " move-ratings)
    (if (not= 1 (apply max (vals (frequencies move-ratings))))
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
  ;(println (filter #((can-play? %) GAME) (range WIDTH))))
  ;(println (map #(make-move % GAME) (possible-moves-on GAME))))
   