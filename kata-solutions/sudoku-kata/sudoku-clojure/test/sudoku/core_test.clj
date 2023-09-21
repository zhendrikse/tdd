(ns sudoku.core-test
  (:refer-clojure :exclude [sudoku.core])
  (:require [midje.sweet :refer [facts, fact, truthy, falsey, =>]]
            [sudoku.core :refer :all]))

; Test cases and exercises from 
; http://iloveponies.github.io/120-hour-epic-sax-marathon/sudoku.html

(def sudoku-board
  (board [[5 3 0 0 7 0 0 0 0]
          [6 0 0 1 9 5 0 0 0]
          [0 9 8 0 0 0 0 6 0]
          [8 0 0 0 6 0 0 0 3]
          [4 0 0 8 0 3 0 0 1]
          [7 0 0 0 2 0 0 0 6]
          [0 6 0 0 0 0 2 8 0]
          [0 0 0 4 1 9 0 0 5]
          [0 0 0 0 8 0 0 7 9]]))

(def solved-board
  (board [[5 3 4 6 7 8 9 1 2]
          [6 7 2 1 9 5 3 4 8]
          [1 9 8 3 4 2 5 6 7]
          [8 5 9 7 6 1 4 2 3]
          [4 2 6 8 5 3 7 9 1]
          [7 1 3 9 2 4 8 5 6]
          [9 6 1 5 3 7 2 8 4]
          [2 8 7 4 1 9 6 3 5]
          [3 4 5 2 8 6 1 7 9]]))

(def invalid-board
  (board [[1 3 4 6 7 8 9 1 2]
          [6 7 2 1 9 5 3 4 8]
          [1 9 8 3 4 2 5 6 7]
          [8 5 9 7 6 1 4 2 3]
          [4 2 6 8 5 3 7 9 1]
          [7 1 3 9 2 4 8 5 6]
          [9 6 1 5 3 7 2 8 4]
          [2 8 7 4 1 9 6 3 5]
          [3 4 5 2 8 6 1 7 9]]))

(facts "Exercise 1: values at sudoku board"
       (fact "it returns the value at a given coordinate"
             (value-at sudoku-board [0 1]) => 3
             (value-at sudoku-board [0 0]) => 5))

(facts "Exercise 2: predicate to determine if square has a value"
       (fact "it returns true if the square has a value"
             (square-has-value? sudoku-board [0 0]) => true
             (square-has-value? sudoku-board [0 2]) => false))

(facts "Exercise 3: set of row values"
       (fact "it returns a set of all values in a row"
             (row-values-in sudoku-board [0 2]) => #{0 5 3 7}
             (row-values-in sudoku-board [3 2]) => #{0 8 6 3}))

(facts "Exercise 4: set of column values"
       (fact "it returns a set of all values in a column"
             (column-values-in sudoku-board [0 2]) => #{0 8}
             (column-values-in sudoku-board [4 8]) => #{3 1 6 0 5 9}))

(facts "Exercise 5: generate coordinate pairs"
       (fact "it returns all coordinate pairs generated from the input"
             (block-coordinate-pairs [0 1]) => [[0 0] [0 1] [0 2]
                                                [1 0] [1 1] [1 2]
                                                [2 0] [2 1] [2 2]]

             (block-coordinate-pairs [3 3]) => [[3 3] [3 4] [3 5]
                                                [4 3] [4 4] [4 5]
                                                [5 3] [5 4] [5 5]]))

(facts "Exercise 6: set of values in a 3x3 block at given coordinates"
       (fact "it returns a set of all values in a column"
             (block-values-in sudoku-board [0 2]) => #{0 5 3 6 8 9}
             (block-values-in sudoku-board [4 5]) => #{0 6 8 3 2}))

(facts "Exercise 7: valid values for a 3x3 block"
       (fact "it returns a set of valid values in a block at given coordinates"
             (valid-values-for-square sudoku-board [0 0]) => #{}
             (valid-values-for-square sudoku-board [0 2]) => #{1 2 4}))

(facts "Exercise 8: predicate for full board"
       (fact "it returns true if there are no empty squares left"
             (filled? sudoku-board) => false
             (filled? solved-board) => true))

(facts "Exercise 9: a set of all values in a row or column"
       (fact "it returns a set of all values in a row"
             (row-values-in sudoku-board [0 0]) => #{5 3 0 7}
             (row-values-in sudoku-board [1 0]) => #{6 0 1 9 5}
             (row-values-in sudoku-board [2 0]) => #{0 9 8 6}
             (row-values-in sudoku-board [3 0]) => #{8 0 6 3}
             (row-values-in sudoku-board [4 0]) => #{4 0 8 3 1}
             (row-values-in sudoku-board [5 0]) => #{7 0 2 6}
             (row-values-in sudoku-board [6 0]) => #{0 6 2 8}
             (row-values-in sudoku-board [7 0]) => #{0 4 1 9 5}
             (row-values-in sudoku-board [8 0]) => #{0 8 7 9}

             (row-values-in solved-board [0 0]) => #{1 2 3 4 5 6 7 8 9}
             (row-values-in solved-board [1 0]) => #{1 2 3 4 5 6 7 8 9}
             (row-values-in solved-board [2 0]) => #{1 2 3 4 5 6 7 8 9}
             (row-values-in solved-board [3 0]) => #{1 2 3 4 5 6 7 8 9}
             (row-values-in solved-board [4 0]) => #{1 2 3 4 5 6 7 8 9}
             (row-values-in solved-board [5 0]) => #{1 2 3 4 5 6 7 8 9}
             (row-values-in solved-board [6 0]) => #{1 2 3 4 5 6 7 8 9}
             (row-values-in solved-board [7 0]) => #{1 2 3 4 5 6 7 8 9}
             (row-values-in solved-board [8 0]) => #{1 2 3 4 5 6 7 8 9})

       (fact "it returns a set of all values in a column"
             (column-values-in sudoku-board [0 0]) => #{5 6 0 8 4 7}
             (column-values-in sudoku-board [0 1]) => #{3 0 9 6}
             (column-values-in sudoku-board [0 2]) => #{0 8}
             (column-values-in sudoku-board [0 3]) => #{0 1 8 4}
             (column-values-in sudoku-board [0 4]) => #{7 9 0 6 2 1 8}
             (column-values-in sudoku-board [0 5]) => #{0 5 3 9}
             (column-values-in sudoku-board [0 6]) => #{0 2}
             (column-values-in sudoku-board [0 7]) => #{0 6 8 7}
             (column-values-in sudoku-board [0 8]) => #{0 3 1 6 5 9}

             (column-values-in solved-board [0 0]) => #{1 2 3 4 5 6 7 8 9}
             (column-values-in solved-board [1 0]) => #{1 2 3 4 5 6 7 8 9}
             (column-values-in solved-board [2 0]) => #{1 2 3 4 5 6 7 8 9}
             (column-values-in solved-board [3 0]) => #{1 2 3 4 5 6 7 8 9}
             (column-values-in solved-board [4 0]) => #{1 2 3 4 5 6 7 8 9}
             (column-values-in solved-board [5 0]) => #{1 2 3 4 5 6 7 8 9}
             (column-values-in solved-board [6 0]) => #{1 2 3 4 5 6 7 8 9}
             (column-values-in solved-board [7 0]) => #{1 2 3 4 5 6 7 8 9}
             (column-values-in solved-board [8 0]) => #{1 2 3 4 5 6 7 8 9}))

(facts "Exercise 10: a set of all values in the 3x3 blocks"
       (fact "it returns a sequence of sets of all 3x3 blocks"
             (block-values-in sudoku-board [0, 0]) => #{5 3 0 6 9 8}
             (block-values-in sudoku-board [0, 3]) => #{0 7 1 9 5}
             (block-values-in sudoku-board [0, 6]) => #{0 6}
             (block-values-in sudoku-board [3, 0]) => #{8 0 4 7}
             (block-values-in sudoku-board [3, 3]) => #{0 6 8 3 2}
             (block-values-in sudoku-board [3, 6]) => #{0 3 1 6}
             (block-values-in sudoku-board [6, 0]) => #{0 6}
             (block-values-in sudoku-board [6, 3]) => #{0 4 1 9 8}
             (block-values-in sudoku-board [6, 6]) => #{2 8 0 5 7 9}

             (block-values-in solved-board [0, 0]) => #{1 2 3 4 5 6 7 8 9}
             (block-values-in solved-board [3, 0]) => #{1 2 3 4 5 6 7 8 9}
             (block-values-in solved-board [6, 0]) => #{1 2 3 4 5 6 7 8 9}
             (block-values-in solved-board [0, 3]) => #{1 2 3 4 5 6 7 8 9}
             (block-values-in solved-board [3, 3]) => #{1 2 3 4 5 6 7 8 9}
             (block-values-in solved-board [6, 3]) => #{1 2 3 4 5 6 7 8 9}
             (block-values-in solved-board [0, 6]) => #{1 2 3 4 5 6 7 8 9}
             (block-values-in solved-board [3, 6]) => #{1 2 3 4 5 6 7 8 9}
             (block-values-in solved-board [6, 6]) => #{1 2 3 4 5 6 7 8 9}))

(facts "Exercise 11: predicates for valid row, column, and block values"
       (fact "it returns true if every row in board is a valid filled row"
             (all-rows-valid? solved-board)  => truthy
             (all-rows-valid? invalid-board) => falsey)
       (fact "it returns true if every column in board is a valid filled column"
             (all-columns-valid? solved-board)  => truthy
             (all-columns-valid? invalid-board) => falsey)
       (fact "it returns true if every block in board is a valid filled block"
             (all-blocks-valid? solved-board)  => truthy
             (all-blocks-valid? invalid-board) => falsey))

(facts "Exercise 12: predicate for valid solution of whole board"
       (fact "it returns true if board is a valid solution to sudoku"
             (valid-solution? solved-board)  => truthy
             (valid-solution? invalid-board) => falsey))

(def before-change
  (board [[5 3 0 0 7 0 0 0 0]
          [6 0 0 1 9 5 0 0 0]
          [0 9 8 0 0 0 0 6 0]
          [8 0 0 0 6 0 0 0 3]
          [4 0 0 8 0 3 0 0 1]
          [7 0 0 0 2 0 0 0 6]
          [0 6 0 0 0 0 2 8 0]
          [0 0 0 4 1 9 0 0 5]
          [0 0 0 0 8 0 0 7 9]]))

(def after-change
  (board [[5 3 0 0 7 0 0 0 0]
          [6 0 0 1 9 5 0 0 0]
          [0 4 8 0 0 0 0 6 0]
          [8 0 0 0 6 0 0 0 3]
          [4 0 0 8 0 3 0 0 1]
          [7 0 0 0 2 0 0 0 6]
          [0 6 0 0 0 0 2 8 0]
          [0 0 0 4 1 9 0 0 5]
          [0 0 0 0 8 0 0 7 9]]))

(facts "Exercise 13: change value at a square"
       (fact "it changes the value at a square with given coordinates"
             (set-value-at before-change [2 1] 4) => after-change))

(facts "Exercise 14: find empty square"
       (fact "it returns coordinates of next empty square"
             (find-empty-square sudoku-board) => [0 2]))

(facts "Exercise 15: solving the puzzle"
       (fact "it returns the solved puzzle"
             (solve sudoku-board) => solved-board))

(def board-string "53..7....6..195....98....6.8...6...34..8.3..17...2...6.6....28....419..5....8..79")

(facts "Boards can be constructed from strings"
       (fact "board constructed from string"
             (board-from-string board-string) => sudoku-board))
