# Introduction

Please read the general [introduction to the sudoku kata](../README.md) first!

# Getting started

To get started, simply invoke the following command:

```bash
$ lein new app kata/sudoku
```

# Implementation

This implementation is based on the instructions found in the
[Functional Programming in Clojure](http://iloveponies.github.io/120-hour-epic-sax-marathon/sudoku.html) course.

## Initialization of a board

Let's first initialize a Sudoku puzzle from a string.

<details>
  <summary>Test to read a Sudoku puzzle from string</summary>
  
```clojure
(def board-1 ".5..83.17...1..4..3.4..56.8....3...9.9.8245....6....7...9....5...729..861.36.72.4")

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
```
</details>

### Exercise 0

The first exercise is to finish up the implementation for the above specification. 
Note that a value of zero is used to indicate that a value still needs to be found, 
i.e. represents an empty cell in the initial puzzle.

## The basic building blocks

In the following exercises, the examples are based on the following two boards:

```clojure
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
```

### Exercise 1

<details>
  <summary>
Write the function <code>(value-at board coordinates)</code> that returns the value at coordinate in board
  </summary>

```clojure
(value-at sudoku-board [0 1]) ;=> 3
(value-at sudoku-board [0 0]) ;=> 5
```

Tip: use

```clojure
(get-in [["a" "b"] ["c" "d"]] [0 1])
```
    
</details>

### Exercise 2

<details>
  <summary>
Write the function <code>(has-value? board coordinates)</code> that returns false if the square at coordinates is empty (has 0), and otherwise true.
  </summary>

```clojure
(has-value? sudoku-board [0 0]) ;=> true
(has-value? sudoku-board [0 2]) ;=> false
```
</details>

Now we can check if square is empty. To figure out which numbers are valid for a square we need to know which are already taken. Let’s write a couple of functions to figure this out.

### Exercise 3

<details>
  <summary>
Write the function <code>(row-values board coordinates)</code> that returns a set with all numbers on the row of the coordinates    
  </summary>

Remember that you can use destructing inside the parameter vector to get the row.

```clojure
(row-values sudoku-board [0 2]) ;=> #{0 5 3 7}
(row-values sudoku-board [3 2]) ;=> #{0 8 6 3}
```
</details>

### Exercise 4

<details>
  <summary>
Write the function <code>(col-values board coordinates)</code> that returns a set with all numbers on the col of the coordinates
  </summary>

```clojure
(col-values sudoku-board [0 2]) ;=> #{0 8}
(col-values sudoku-board [4 8]) ;=> #{3 1 6 0 5 9}
```
</details>

### Exercise 5

<details>
  <summary>
Write the function <code>(coord-pairs coord-sequence)</code> that returns all coordinate-pairs of the form <code>[row col]</code> where <code>row</code> is from <code>coord-sequence</code> and <code>col</code> is from <code>coord-sequence</code>.
</summary>
  
```clojure
(coord-pairs [0 1])   ;=> [[0 0] [0 1]
                      ;    [1 0] [1 1]]

(coord-pairs [0 1 2]) ;=> [[0 0] [0 1] [0 2]
                      ;    [1 0] [1 1] [1 2]
                      ;    [2 0] [2 1] [2 2]]
```

Tip: use list comprehensions in Clojure

```clojure
(for [number [1 2 3]]
  (+ number 2))
;=> (3 4 5)
```

Here the name number gets bound to each value of the sequence `[1 2 3]` one by one. For each value, evaluate the body `(+ number 2)` with it and collect the results into a sequence.

But you can give for multiple bindings, and it will go through all combinations:

```clojure
(for [name ["John" "Jane"]
      number [1 2 3]]
  (str name " " number))
;=> ("John 1" "John 2" "John 3" "Jane 1" "Jane 2" "Jane 3")
```
  
</details>

### Exercise 6

<details>
  <summary>
Write the function <code>(block-values board coordinates)</code> that returns a set with all numbers in the block of coordinates.
  </summary>

You might want to write a helper function that returns the coordinates for the top left corner of the block.

```clojure
(block-values sudoku-board [0 2]) ;=> #{0 5 3 6 8 9}
(block-values sudoku-board [4 5]) ;=> #{0 6 8 3 2}    
```
</details>

### Exercise 7

Write the function (valid-values-for board coordinates) that returns a set with all valid numbers for the square at coordinates.

If the square at coordinates already has a value, valid-values should return the empty set #{}.

Remember that we already defined the set all-values.

(valid-values-for sudoku-board [0 0]) ;=> #{}
(valid-values-for sudoku-board [0 2]) ;=> #{1 2 4})
Next, let’s write a function to figure out if a sudoku board is completely filled.

### Exercise 8

Write the function (filled? board) which returns true if there are no empty squares in board, and otherwise false.

It might help to write a helper function that returns all numbers of the board in a sequence.

Remember that (contains? set element) can be used to check if element is in set.

(filled? sudoku-board) ;=> false
(filled? solved-board) ;=> true