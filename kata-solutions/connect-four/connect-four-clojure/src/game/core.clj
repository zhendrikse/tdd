(ns game.core
  (:require [game.printer :refer :all]
            [game.board :refer :all]))

(def TOTAL_MOVES (/ (* WIDTH HEIGHT) 2))

(def DEFAULT_SCORE Integer/MIN_VALUE)
(def COLUMNS_SCORE_MAP (into {} (map (fn[column] [column DEFAULT_SCORE]) (range WIDTH))))

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

(defn rate-moves
  [game]
  (let [moves-made (/ (dec (game MOVES_COUNTER_INDEX)) 2)
        moves-left (- TOTAL_MOVES moves-made)
        score moves-left
        score-mapper (fn [[key value]] [key (if (is-winning-move? key game) score value)])] 
    (into {} (map score-mapper COLUMNS_SCORE_MAP))))

(defn- pick-max-score-column
  [columns-score-map]
  (key (first (sort-by val > columns-score-map))))

(defn generate-ai-move [game]
  (let [move-ratings (rate-moves game)
        best-move (pick-max-score-column move-ratings)] 
    (if (= (get move-ratings best-move) DEFAULT_SCORE)
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
   