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

(defn- score [board] 
  (let [score (- TOTAL_MOVES (quot (board MOVES_COUNTER_INDEX) 2))]
    (if (= (current-player-in board) RED)
      score
      (- score))))

(defn- heuristic
  [board] 
  0)

(defn min-max
  [board depth]
  (cond
    (connect-four-on? board)
      (score board) 
    (is-full? board)
      0
    (= depth 0)
      (heuristic board)
    :else
      (let [limit (* WIDTH HEIGHT)
            current-player (current-player-in board)
            best-score (if (= current-player RED) limit (- limit))]
        (if (= current-player RED)
          (do
            ;(println (for [move (possible-moves-on board)] (min-max (make-move move board) (dec depth))))
            (min (apply min (for [move (possible-moves-on board)] (min-max (make-move move board) (dec depth)))) best-score)
            )
          (do
            ;(println (for [move (possible-moves-on board)] (min-max (make-move move board) (dec depth))))
            (max (apply max (for [move (possible-moves-on board)] (min-max (make-move move board) (dec depth)))) best-score)
            )
          ))))

(defn generate-ai-move [board]
  (let [possible-boards (map #(make-move % board) (possible-moves-on board))
        move-ratings (vec (map #(min-max % 4) possible-boards))
        best-score (apply max move-ratings)
        best-moves (vec (filter #(= (get move-ratings %) best-score) (range (count move-ratings))))]
    (println "Best moves are " (map inc best-moves) " in " move-ratings)
    (get best-moves (rand-int (count best-moves)))))

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
