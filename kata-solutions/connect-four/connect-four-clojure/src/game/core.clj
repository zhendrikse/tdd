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

(defn- game-end? [game] (or (connect-four-on? game) (is-full? game)))

(defn- game-exit
  [game]
  (let [previous-player (bit-xor 1 (current-player-in game))]
    (if (connect-four-on? game)
      (println (str "Player " (inc previous-player) " has won!"))
      (println (str "It's a draw!")))))

(defn move-winning? [board column]
  [column (connect-four-on? (make-move column board))])

(defn can-play? [column]
  (fn [board] (not (is-full? board column))))

(defn possible-moves-on [board] 
  (filter #((can-play? %) board) (range WIDTH)))

(defn winning-move-on [board]
  (let [rated-moves (into {} (map (partial move-winning? board) (possible-moves-on board)))]
   (first (filter val rated-moves))))

(defn- score [board] (- TOTAL_MOVES (quot (board MOVES_COUNTER_INDEX) 2)))

(defn negamax-algo
  [board depth]
  (cond 
    (is-full? board)
    0
    (not (nil? (winning-move-on board)))
      (score board) 
    (= 0 depth) 
      (if (connect-four-on? board)
        (score board)
        (- (* WIDTH HEIGHT))) 
    :else
      (let [best-score (- (* WIDTH HEIGHT))
            score-children (fn[move] (- (negamax-algo (make-move move board) (dec depth))))]
        ;; (println (for [move (possible-moves-on board)] (score-children move)))
        (max (apply max (for [move (possible-moves-on board)] 
          (score-children move))) best-score))))

(defn negamax 
  [board]
  (negamax-algo board 1))

(defn generate-ai-move [board]
  (let [possible-boards (map #(make-move % board) (possible-moves-on board))
        move-ratings (map negamax possible-boards)
        best-score (apply max move-ratings)
        best-move (.indexOf move-ratings best-score)]
    (println "Best move is " (inc best-move) " in " move-ratings)
    (if (nil? (winning-move-on board)) 
      (if (apply = move-ratings)
        ((vec (range WIDTH)) (rand-int WIDTH))
        best-move)
      (first (winning-move-on board)))))

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
