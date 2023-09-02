(ns game.core
  (:require [game.printer :refer [print-game]]
            [game.board :refer [TOTAL_MOVES
                                MOVES_COUNTER_INDEX
                                RED
                                GAME
                                connect-four-on?
                                current-player-in
                                is-full?
                                possible-moves-in
                                make-move]]))

(defn- read-input [player-num]
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

(defn- move-winning? [column game]
  [column (connect-four-on? (make-move column game))])

(defn winning-move-in [game]
  (let [rated-moves (into {} (map #(move-winning? % game) (possible-moves-in game)))]
    (first (filter val rated-moves))))

(defn- score [game]
  (let [score (quot (- TOTAL_MOVES (dec (game MOVES_COUNTER_INDEX))) 2)]
    (if (= (current-player-in game) RED)
      score
      (- score))))

(defn- heuristic
  [game]
  0)

(defn min-max
  [game depth]
  (cond
    (connect-four-on? game)
    (score game)
    (is-full? game)
    0
    (= depth 0)
    (heuristic game)
    :else
    (let [limit TOTAL_MOVES
          current-player (current-player-in game)
          best-score (if (= current-player RED) limit (- limit))
          possible-moves (possible-moves-in game)
          children-scores (for [move possible-moves] (min-max (make-move move game) (dec depth)))]
      (if (= current-player RED)
        (min (apply min children-scores) best-score)
        (max (apply max children-scores) best-score)))))

(defn generate-ai-move-for [game]
  (let [possible-boards (map #(make-move % game) (possible-moves-in game))
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
        (recur (make-move (generate-ai-move-for game) game))))))

(defn -main
  [& args]
  (play-game GAME))
