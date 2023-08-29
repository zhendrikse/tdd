(ns kata.sudoku
  "Sudoku solver"
  (:require
   [clojure.string :as string]
   [clojure.set :as set]))

(def board-from-vector identity)
(def all-values #{1 2 3 4 5 6 7 8 9})
(def dim (count all-values))

(defn board-from-string
  "creates a sudoku board from a string"
  [board-as-string]
  (let [string-with-zeros (string/replace board-as-string #"(\.)" "0")
        vector-with-integers (map #(Integer/parseInt (str %)) string-with-zeros)
        substring (fn [x] (drop (* dim x) (drop-last (* dim (- (- dim 1) x)) vector-with-integers)))]
    (into [] (for [x (range dim)] (into [] (substring x))))))

(defn value-at [board coordinates] (get-in board coordinates))

(defn square-has-value?
  [board coordinates]
  (let [empty-value 0]
    (not= (value-at board coordinates) empty-value)))

(defn row-values-in
  [board coordinates]
  (let [row-value (first coordinates)]
    (set (get board row-value))))

(defn column-values-in
  [board coordinates]
  (let [column-value (second coordinates)
        dimension (count (first board))
        board-columns (into [] (partition dimension (apply interleave board)))]
    (set (get board-columns column-value))))

(defn block-coordinate-pairs
  [block-coordinates] ; may be anywhere in block
  (let [block-x (* (quot (first block-coordinates) 3) 3)
        block-y (* (quot (second block-coordinates) 3) 3)
        range-x (range block-x (+ block-x 3))
        range-y (range block-y (+ block-y 3))]
    (for [x range-x y range-y] (into [] (list x y)))))

(defn block-values-in
  [board block-coordinates] ; block coordinates may be anywhere in block
  (let [coordinates-list (block-coordinate-pairs block-coordinates)
        value-at-board (fn [index] (value-at board index))]
    (set (map value-at-board coordinates-list))))

(defn valid-values-for-square
  [board coordinates]
  (let [row-values-taken (row-values-in board coordinates)
        column-values-taken (column-values-in board coordinates)
        block-values-taken (block-values-in board coordinates)
        occupied-values (set/union row-values-taken column-values-taken block-values-taken)]
    (if (square-has-value? board coordinates)
      #{}
      (set/difference all-values occupied-values))))

(defn filled?
  [board]
  (let [value-at-board (fn [index] (value-at board index))
        coordinates (for [x (range dim) y (range dim)] (into [] (list x y)))
        all-board-values (set (map value-at-board coordinates))]
    (not (contains? all-board-values 0))))

(defn all-rows
  [board]
  (for [row (range dim)] (row-values-in board [row, 0])))

(defn all-columns
  [board]
  (for [column (range dim)] (column-values-in board [0, column])))

(defn all-blocks
  [board]
  (for [row `(0 3 6) column `(0 3 6)] (block-values-in board [row, column])))

(defn all-rows-valid?
  [board]
  (let [evaluated-rows (map #(= all-values %) (all-rows board))]
    (every? #(= % true) evaluated-rows)))

(defn all-columns-valid?
  [board]
  (let [evaluated-columns (map #(= all-values %) (all-columns board))]
    (every? #(= % true) evaluated-columns)))

(defn all-blocks-valid?
  [board]
  (let [evaluated-blocks (map #(= all-values %) (all-blocks board))]
    (every? #(= % true) evaluated-blocks)))

(defn valid-solution?
  [board]
  (let [rows-valid (all-rows-valid? board)
        columns-valid (all-columns-valid? board)
        blocks-valid (all-blocks-valid? board)]
    (every? #(= % true) (list rows-valid columns-valid blocks-valid))))

(defn set-value-at
  [board path new-value]
  (assoc-in board path new-value))

(defn- square-empty? [board coordinates] (not (square-has-value? board coordinates)))
(defn find-empty-square
  [board]
  (let [board-coordinates (for [x (range  dim) y (range  dim)] [x y])]
    (first (filter (partial square-empty? board) board-coordinates))))

(defn- valid-values-for-next-empty-square
  [board]
  (let [next-square (find-empty-square board)]
    (valid-values-for-square board next-square)))

(defn solve
  [board]
  (if (filled? board)
    (if (valid-solution? board)
      board
      [])
    (let [valid-values (valid-values-for-next-empty-square board)]
      (if (empty? valid-values)
        [] ; board not solved and no valid values can be found => backtrack
        (for [value valid-values
              updated-board (solve (set-value-at board (find-empty-square board) value))] updated-board)))))

(def demo-board (board-from-vector
                 [[5 3 0 0 7 0 0 0 0]
                  [6 0 0 1 9 5 0 0 0]
                  [0 9 8 0 0 0 0 6 0]
                  [8 0 0 0 6 0 0 0 3]
                  [4 0 0 8 0 3 0 0 1]
                  [7 0 0 0 2 0 0 0 6]
                  [0 6 0 0 0 0 2 8 0]
                  [0 0 0 4 1 9 0 0 5]
                  [0 0 0 0 8 0 0 7 9]]))
(defn -main [& args]
  (println (solve demo-board)))