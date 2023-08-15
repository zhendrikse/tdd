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


### Exercise 0

<details>
  <summary>Read a Sudoku puzzle from string</summary>
  
The first exercise is to finish up the implementation for the above specification. 
Note that a value of zero is used to indicate that a value still needs to be found, 
i.e. represents an empty cell in the initial puzzle.

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

<details>
  <summary>
Write the function <code>(valid-values-for board coordinates)</code> that returns a set with all valid numbers for the square at coordinates.    
  </summary>

If the square at coordinates already has a value, valid-values should return the empty set `#{}`.

Remember that we already defined the set all-values.

```clojure
(valid-values-for sudoku-board [0 0]) ;=> #{}
(valid-values-for sudoku-board [0 2]) ;=> #{1 2 4})
```

Tip

The `clojure.set` namespace has some useful functions for working with sets. `(clojure.set/union set1 set2 ...)` returns a set containing all the elements of its arguments:

```clojure
(clojure.set/union #{1 2} #{2 3} #{7}) ;=> #{1 2 3 7}
```

In the project file, `clojure.set` is required with the shorthand set, so you can also just write: 

```clojure
(set/union #{1 2} #{2 3} #{7}) ;=> #{1 2 3 7}
```

Another helpful set operation is `(set/difference set1 set2)`, which returns a set with all elements of set1 except those that are also in set2. Or put another way, removes all elements of set2 from set1:

```clojure
(set/difference #{1 2 3} #{1 3})   ;=> #{2}
(set/difference #{1 2 3} #{2 4 5}) ;=> #{1 3}
```
</details>

Next, let’s write a function to figure out if a sudoku board is completely filled.

### Exercise 8

<details>
<summary>
Write the function <code>(filled? board)</code> which returns true if there are no empty squares in board, and otherwise false.  
</summary>  

It might help to write a helper function that returns all numbers of the board in a sequence.

Remember that `(contains? set element)` can be used to check if element is in set.

```clojure
(filled? sudoku-board) ;=> false
(filled? solved-board) ;=> true
```
</details>

Now that we can check if a board is full, it would be nice to know if the solution is valid.

A sudoku is valid if each row, each column and each block contains the numbers from 1 to 9 exactly once. Let’s write functions for checking each of these conditions.

To start, let’s write some functions to get the values for each row, column and block.

### Exercise 9

<details>
<summary>
Write the function <code>(rows board)</code> that returns a sequence of value sets for each row of board. That is, the first set in <code>(rows board)</code> is a set that has every element of the first row of board as element and so on.</summary>  

```clojure
(rows sudoku-board) ;=> [#{5 3 0 7}
                    ;    #{6 0 1 9 5}
                    ;    #{0 9 8 6}
                    ;    #{8 0 6 3}
                    ;    #{4 0 8 3 1}
                    ;    #{7 0 2 6}
                    ;    #{0 6 2 8}
                    ;    #{0 4 1 9 5}
                    ;    #{0 8 7 9}]

(rows solved-board) ;=> [#{1 2 3 4 5 6 7 8 9}
                    ;    #{1 2 3 4 5 6 7 8 9}
                    ;    #{1 2 3 4 5 6 7 8 9}
                    ;    #{1 2 3 4 5 6 7 8 9}
                    ;    #{1 2 3 4 5 6 7 8 9}
                    ;    #{1 2 3 4 5 6 7 8 9}
                    ;    #{1 2 3 4 5 6 7 8 9}
                    ;    #{1 2 3 4 5 6 7 8 9}
                    ;    #{1 2 3 4 5 6 7 8 9}]
```

Write the function `(cols board)` that returns the values of each column in board as a sequence of sets.

```clojure
(cols sudoku-board) ;=> [#{5 6 0 8 4 7}
                    ;    #{3 0 9 6}
                    ;    #{0 8}
                    ;    #{0 1 8 4}
                    ;    #{7 9 0 6 2 1 8}
                    ;    #{0 5 3 9}
                    ;    #{0 2}
                    ;    #{0 6 8 7}
                    ;    #{0 3 1 6 5 9}]

(cols solved-board) ;=> [#{1 2 3 4 5 6 7 8 9}
                    ;    #{1 2 3 4 5 6 7 8 9}
                    ;    #{1 2 3 4 5 6 7 8 9}
                    ;    #{1 2 3 4 5 6 7 8 9}
                    ;    #{1 2 3 4 5 6 7 8 9}
                    ;    #{1 2 3 4 5 6 7 8 9}
                    ;    #{1 2 3 4 5 6 7 8 9}
                    ;    #{1 2 3 4 5 6 7 8 9}
                    ;    #{1 2 3 4 5 6 7 8 9}]
```
</details>

### Exercise 10

<details>
  <summary>
Write the function <code>(blocks board)</code> that returns the values of each block in board as a sequence of sets.
  </summary>

```clojure
(blocks sudoku-board) ;=> [#{5 3 0 6 9 8}
                      ;    #{0 7 1 9 5}
                      ;    #{0 6}
                      ;    #{8 0 4 7}
                      ;    #{0 6 8 3 2}
                      ;    #{0 3 1 6}
                      ;    #{0 6}
                      ;    #{0 4 1 9 8}
                      ;    #{2 8 0 5 7 9}]

(blocks solved-board) ;=> [#{1 2 3 4 5 6 7 8 9}
                      ;    #{1 2 3 4 5 6 7 8 9}
                      ;    #{1 2 3 4 5 6 7 8 9}
                      ;    #{1 2 3 4 5 6 7 8 9}
                      ;    #{1 2 3 4 5 6 7 8 9}
                      ;    #{1 2 3 4 5 6 7 8 9}
                      ;    #{1 2 3 4 5 6 7 8 9}
                      ;    #{1 2 3 4 5 6 7 8 9}
                      ;    #{1 2 3 4 5 6 7 8 9}])
```
</details>

Now we can get the values used in every row, column and block. Let’s write functions that check if every row, column and block is valid as per the rules of sudoku.

### Exercise 11

<details>
  <summary>
Write the function <code>(valid-rows? board)</code> that returns true if every row in board is a valid filled row.
  </summary>

```clojure
(valid-rows? solved-board)  ;=> truthy
(valid-rows? invalid-board) ;=> falsey
```

Write the function `(valid-cols? board)` that returns true if every row in board is a valid filled column.

```clojure
(valid-cols? solved-board)  ;=> truthy
(valid-cols? invalid-board) ;=> falsey
```

Write the function `(valid-blocks? board)` that returns true if every block in board is a valid filled block.

```clojure
(valid-blocks? solved-board)  ;=> truthy
(valid-blocks? invalid-board) ;=> falsey
```
</details>

Finally, we can write a function that checks if the whole board is a valid solution.

### Exercise 12

<details>
  <summary>
Write the function <code>(valid-solution? board)</code> that returns true if board is a valid solution to sudoku.
  </summary>

```clojure
(valid-solution? solved-board)  ;=> truthy
(valid-solution? invalid-board) ;=> falsey)
```
</details>

Now we can verify whether or not a solution is valid. However, if we want to actually solve a sudoku, we need to be able to modify a partial solution.

Earlier we saw how useful get-in can be when indexing nested structures. Theres a similar function for changing nested structures, called assoc-in. (assoc-in nested-structure path new-value) changes the value pointed by path, which is a sequence of keys. Here’s an example:

```clojure
 (assoc-in [[:a :b] [:c :d]] [1                                  0] :E)
;=> (assoc [[:a :b] [:c :d]]  1 (assoc (get [[:a :b] [:c :d]] 1) 0  :E))
;=> (assoc [[:a :b] [:c :d]]  1 (assoc               [:c :d]     0  :E))
;=> (assoc [[:a :b] [:c :d]]  1 [:E :d])
;=>        [[:a :b] [:E :d]]
```

Now we can write a function to change a single value in our representation of a sudoku.

### Exercise 13

<details>
  <summary>
Write the function <code>(set-value-at board coord new-value)</code> that changes the value at coord in board to new-value.
  </summary>

```clojure
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

(set-value-at before-change [2 1] 4)
```
</details>

Now that we can change the board, the next obstacle is figuring out what to change. Now we need to find an empty point in the sudoku board.

### Exercise 14

<details>
  <summary>
Write the function <code>(find-empty-point board)</code> that returns coordinates to an empty point (that is, in our representation has value <code>0</code>).
  </summary>
</details>

## Interludium

Okay, so now we can find an empty location and we also know what 
the valid values for that location are. What’s left is to try each one of 
those values in that location and trying to solve the rest. 

This is called backtracking search. You try one choice and recurse, 
if the recursive call didn’t find any solutions, try the next choice. 
If none of the choices return a valid solution, return nil.

Please consult 
[the Wiki page on backtracking algorithms](https://github.com/zhendrikse/tdd/wiki/Coding-Katas#katas-using-backtracking-algorithms)
before continuing to the next and final exercise. You'll find there 
[a dedicated section on backtracking with clojure](https://github.com/zhendrikse/tdd/wiki/Coding-Katas#a-simple-backtracking-example-in-clojure).

## Solving Sudokus

It’s finally time to write the search for a solution to sudokus.

### Exercise 15

<details>
  <summary>
Write the function <code>(solve board)</code> which takes a sudoku board as a parameter and returns a valid solution to the given sudoku.
  </summary>

```clojure
  (solve sudoku-board) => solved-board
```

#### Recap of backtracking:

- check if you are at the end
- if so, is the solution valid?
  - if not, return an empty sequence
  - otherwise return [solution]
- if not
  - select an empty location
  - try solving with each valid value for that location
</details>
