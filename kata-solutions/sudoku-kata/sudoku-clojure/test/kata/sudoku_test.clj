(ns kata.sudoku-test
  (:require [clojure.test :refer :all]
            [kata.sudoku :refer :all]))

(def board-1 ".5..83.17...1..4..3.4..56.8....3...9.9.8245....6....7...9....5...729..861.36.72.4")
(def solved-1 "652483917978162435314975628825736149791824563436519872269348751547291386183657294")
(def sudoku-board (board-from-vector
                   [[5 3 0 0 7 0 0 0 0]
                    [6 0 0 1 9 5 0 0 0]
                    [0 9 8 0 0 0 0 6 0]
                    [8 0 0 0 6 0 0 0 3]
                    [4 0 0 8 0 3 0 0 1]
                    [7 0 0 0 2 0 0 0 6]
                    [0 6 0 0 0 0 2 8 0]
                    [0 0 0 4 1 9 0 0 5]
                    [0 0 0 0 8 0 0 7 9]]))

(def sudoku-board-after-change-at-2-1 (board-from-vector 
        [[5 3 0 0 7 0 0 0 0]
         [6 0 0 1 9 5 0 0 0]
         [0 4 8 0 0 0 0 6 0]
         [8 0 0 0 6 0 0 0 3]
         [4 0 0 8 0 3 0 0 1]
         [7 0 0 0 2 0 0 0 6]
         [0 6 0 0 0 0 2 8 0]
         [0 0 0 4 1 9 0 0 5]
         [0 0 0 0 8 0 0 7 9]]))

(def solved-board (board-from-vector
                   [[5 3 4 6 7 8 9 1 2]
                    [6 7 2 1 9 5 3 4 8]
                    [1 9 8 3 4 2 5 6 7]
                    [8 5 9 7 6 1 4 2 3]
                    [4 2 6 8 5 3 7 9 1]
                    [7 1 3 9 2 4 8 5 6]
                    [9 6 1 5 3 7 2 8 4]
                    [2 8 7 4 1 9 6 3 5]
                    [3 4 5 2 8 6 1 7 9]]))

(deftest a-board-from-string 
         (is (= [
                 [0 5 0 0 8 3 0 1 7] 
                 [0 0 0 1 0 0 4 0 0] 
                 [3 0 4 0 0 5 6 0 8] 
                 [0 0 0 0 3 0 0 0 9] 
                 [0 9 0 8 2 4 5 0 0] 
                 [0 0 6 0 0 0 0 7 0] 
                 [0 0 9 0 0 0 0 5 0] 
                 [0 0 7 2 9 0 0 8 6] 
                 [1 0 3 6 0 7 2 0 4]] (board-from-string board-1))))

(deftest all-rows-of-a-board (is (=
               [#{5 3 0 7}
                #{6 0 1 9 5}
                #{0 9 8 6}
                #{8 0 6 3}
                #{4 0 8 3 1}
                #{7 0 2 6}
                #{0 6 2 8}
                #{0 4 1 9 5}
                #{0 8 7 9}] (all-rows sudoku-board))))

(deftest all-rows-of-a-solved-board (is (=
               [#{1 2 3 4 5 6 7 8 9}
                #{1 2 3 4 5 6 7 8 9}
                #{1 2 3 4 5 6 7 8 9}
                #{1 2 3 4 5 6 7 8 9}
                #{1 2 3 4 5 6 7 8 9}
                #{1 2 3 4 5 6 7 8 9}
                #{1 2 3 4 5 6 7 8 9}
                #{1 2 3 4 5 6 7 8 9}
                #{1 2 3 4 5 6 7 8 9}] (all-rows solved-board))))

(deftest all-columns-of-a-board (is (=
               [#{5 6 0 8 4 7}
                #{3 0 9 6}
                #{0 8}
                #{0 1 8 4}
                #{7 9 0 6 2 1 8}
                #{0 5 3 9}
                #{0 2}
                #{0 6 8 7}
                #{0 3 1 6 5 9}] (all-columns sudoku-board))))

(deftest all-columns-of-a-solved-board (is (=
               [#{1 2 3 4 5 6 7 8 9}
                #{1 2 3 4 5 6 7 8 9}
                #{1 2 3 4 5 6 7 8 9}
                #{1 2 3 4 5 6 7 8 9}
                #{1 2 3 4 5 6 7 8 9}
                #{1 2 3 4 5 6 7 8 9}
                #{1 2 3 4 5 6 7 8 9}
                #{1 2 3 4 5 6 7 8 9}
                #{1 2 3 4 5 6 7 8 9}] (all-columns solved-board))))

(deftest all-blocks-of-a-sudoku-board (is (=
               [#{5 3 0 6 9 8}
                #{0 7 1 9 5}
                #{0 6}
                #{8 0 4 7}
                #{0 6 8 3 2}
                #{0 3 1 6}
                #{0 6}
                #{0 4 1 9 8}
                #{2 8 0 5 7 9}] (all-blocks sudoku-board))))

(deftest all-blocks-of-a-solved-board (is (= 
               [#{1 2 3 4 5 6 7 8 9}
                #{1 2 3 4 5 6 7 8 9}
                #{1 2 3 4 5 6 7 8 9}
                #{1 2 3 4 5 6 7 8 9}
                #{1 2 3 4 5 6 7 8 9}
                #{1 2 3 4 5 6 7 8 9}
                #{1 2 3 4 5 6 7 8 9}
                #{1 2 3 4 5 6 7 8 9}
                #{1 2 3 4 5 6 7 8 9}] (all-blocks solved-board))))

(deftest valid-solution-solved-board
  (is (= true (valid-solution? solved-board))))
(deftest valid-solution-unsolved-board
  (is (= false (valid-solution? sudoku-board))))
(deftest solved-board-1-valid 
         (is (= true (valid-solution? (board-from-string solved-1)))))

(deftest value-at-0-0
  (is (= 5 (value-at sudoku-board [0 0]))))
(deftest value-at-0-1
  (is (= 3 (value-at sudoku-board [0 1]))))

(deftest square-has-value-at-0-0
  (is (= true (square-has-value? sudoku-board [0 0]))))
(deftest square-has-value-at-0-2
  (is (= false (square-has-value? sudoku-board [0 2]))))

(deftest is-sudoku-board-filled
  (is (= false (filled? sudoku-board))))
(deftest is-solved-board-filled
  (is (= true (filled? solved-board))))

(deftest blok-values-at-1-1
  (is (= #{0 5 3 6 8 9} (block-values-in sudoku-board [1 1]))))
(deftest blok-values-at-4-5
  (is (= #{0 6 8 3 2} (block-values-in sudoku-board [4 5]))))

(deftest all-rows-valid-in-solved-board
  (is (= true (all-rows-valid? solved-board))))
(deftest all-rows-valid-in-board-to-be-solved
  (is (= false (all-rows-valid? sudoku-board))))

(deftest all-columns-valid-in-solved-board
  (is (= true (all-columns-valid? solved-board))))
(deftest all-columns-valid-in-board-to-be-solved
  (is (= false (all-columns-valid? sudoku-board))))

(deftest all-blocks-valid-in-solved-board
  (is (= true (all-blocks-valid? solved-board))))
(deftest all-blocks-valid-in-board-to-be-solved
  (is (= false (all-blocks-valid? sudoku-board))))

(deftest row-values-at-0-2
  (is (= #{0 5 3 7} (row-values-in sudoku-board [0 2]))))
(deftest row-values-at-3-2
  (is (= #{0 8 6 3} (row-values-in sudoku-board [3 2]))))
(deftest column-values-at-0-2
  (is (= #{0 8} (column-values-in sudoku-board [0 2]))))
(deftest column-values-at-4-8
  (is (= #{3 1 6 0 5 9} (column-values-in sudoku-board [4 8]))))

(deftest coordinate-sequence-0-0
  (is (= (list [0 0] [0 1] [0 2] [1 0] [1 1] [1 2] [2 0] [2 1] [2 2]) (block-coordinate-pairs [2 2])))
  (is (= (list [0 0] [0 1] [0 2] [1 0] [1 1] [1 2] [2 0] [2 1] [2 2]) (block-coordinate-pairs [0 0]))))
(deftest coordinate-sequence-4-8
  (is (= (list [3 6] [3 7] [3 8] [4 6] [4 7] [4 8] [5 6] [5 7] [5 8]) (block-coordinate-pairs [4 8]))))
(deftest coordinate-sequence-8-8
  (is (= (list [6 6] [6 7] [6 8] [7 6] [7 7] [7 8] [8 6] [8 7] [8 8]) (block-coordinate-pairs [8 8]))))

(deftest valid-values-at-square-0-0
  (is (= #{} (valid-values-for-square sudoku-board [0 0]))))
(deftest valid-values-at-square-0-2
  (is (= #{1 2 4} (valid-values-for-square sudoku-board [0 2]))))

(deftest set-value-at-2-1-to-4
  (is (= sudoku-board-after-change-at-2-1 (set-value-at sudoku-board [2 1] 4))))

(deftest find-empty-square-on-sudoku-board
  (is (= [0 2] (find-empty-square sudoku-board))))

(deftest solve-sudoku-board
  ;(println (solve sudoku-board)))
  (is (= solved-board (solve sudoku-board))))
