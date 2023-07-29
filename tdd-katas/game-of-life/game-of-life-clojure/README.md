# Introduction

Please read the general [introduction to the game of life kata](../README.md) first!


# Teaser

We are going to build the following code, which is a showcase of _code should
express intent_, Kent Beck's design rule number 2!

```clojure
(defn next-generation-of
  [game]
  (map #(to-living-cell 
         (which-both 
          is-dead? 
          (has-exactly-three? (living-neighbours-in game))) %) 
  (map #(to-dead-cell 
         (which-both 
          is-alive? 
          (which-either 
           (has-less-than-two? (living-neighbours-in game)) 
           (has-more-than-three? (living-neighbours-in game))) ) %) game)   )
)
```

The approach here is an almost literal TDD version of
the marvelous functional solution proposed in 
[this excellent post](https://medium.com/@davidibl/functional-java-9e95a647af3c)
and the associated 
[code repository](https://github.com/davidibl/GameOfLifeFunctional/tree/master) 
mentioned therein, transcribed to Clojure.

# Getting started

You can simply start coding by invoking

```bash
$ lein new app kata/game-of-life
```

# Functional implementation

## Living and dead cells

Let's write our first specification(s) for predicates of living and
dead cells.

<details>
  <summary>Predicates for living and dead cells</summary>

  ```clojure
  (def LIVING-CELL (living-cell 0 0))
  (def DEAD-CELL (dead-cell 0 0))
  
  (deftest a-living-cell-is-is-alive
    (testing "Living cell should be is-alive."
      (is (is-alive? LIVING-CELL))))
  
  (deftest a-dead-cell-is-not-is-alive
    (testing "Dead cell is not is-alive."
      (is (not (is-alive? DEAD-CELL)))))
  
  (deftest a-living-cell-is-not-dead
    (testing "Living cell is not dead."
      (is (not (is-dead? LIVING-CELL)))))
  
  (deftest a-dead-cell-is-dead
    (testing "Dead cell is dead."
      (is (is-dead? DEAD-CELL))))
  ``` 
  where the `is-alive?` and `is-dead?` predicates are (to be) defined in the 
  production code.

  <details>
  <summary>Definition of the predicates that make the test pass</summary>
  
  ```clojure
  (defn living-cell 
    [x y]
    [x y true])
  
  (defn dead-cell 
    [x y]
    [x y false])
  
  (defn is-dead?
    [cell]
    (= (last cell) false))
  
  (defn is-alive?
    [cell]
    (= (last cell) true))
  ```
  </details>
  </details>

  ## Killing and resurrecting cells

  We should be able to change cells from living to dead and vice versa.
  In functional programming, this means creating new cells, as we cannot
  change state (because of immutability!).

  Note that we would like to conditionally transition from a living to 
  a dead cell, e.g. depending on the status of the cell itself (we 
  cannot kill an already dead cell). More importantly, eventually we 
  would like to conditionally kill a cell, depending on the conditions 
  and rules imposed by its neighbours.

  Summarizing, we want to map a list of cells to dead cells, given 
  a certain condition (= predicate!).

<details>
  <summary>The specification for the <code>to-dead-cell</code> mapping</summary>

  ```clojure
    (deftest map-living-cell-to-dead-cell
      (testing "Map living cell to dead cell.")
        (is (is-dead? (to-dead-cell is-alive? LIVING-CELL))))

    (deftest map-dead-cell-to-dead-cell
      (testing "Map dead cell to dead cell.")
        (is (is-dead? (to-dead-cell is-alive? DEAD-CELL))))
  ```

And the code that makes this test pass

<details>
  <summary>The implementation for the <code>to-dead-cell</code> mapping</summary>

  ```clojure
  (defn to-dead-cell
    [cell-killable? cell]
    (if (cell-killable? cell)
      (dead-cell (get cell 0) (get cell 1))
      cell))
  ```
</details>
</details>


Analogously we implement the `to-living-cell` mapping.

## Determining the living neighbours

The rules of the game depend on the number of living neighbours.
Consequently, we need to define a predicate that for a given field
determines the number of living neighbours in a game.

### Determining the neigbours of a cell

Let's tackle the most generic case first, namely
a non-edge cell should have eight neighbours.

<details>
  <summary>A non-edge cell should have eight neighbours</summary>

  ```clojure
  (def GAME (list 
           (dead-cell 0 0)   (living-cell 0 1) (living-cell 0 2)
           (living-cell 1 0) (living-cell 1 1) (dead-cell 1 2)
           (dead-cell 2 0)   (living-cell 2 1) (dead-cell 2 2)))

  (deftest neighbours-of-center-cell 
    (testing "Neighbours of center cell.") 
      (is 8 (count (filter (is-neighbour-of? (living-cell 1 1)) GAME))))
  ```

and the simplest thing/solution that could possibly work to make this test pass

<details>
  <summary>Making the test pass</summary>

  ```clojure
   (defn is-neighbour-of?
      [given-cell]
      (fn 
        [cell] 
        (not(= cell given-cell))
      ))
  ```
  
</details>
</details>

Next, we test for a left-edge cell.

<details>
  <summary>A left-edge cell should have five neighbours</summary>

  ```clojure
  (deftest neighbours-of-left-edge-center-cell 
    (testing "Neighbours of left edge center cell.") 
      (is 5 (count (filter (is-neighbour-of? (living-cell 1 2)) GAME))))

  ```

and the simplest thing/solution that could possibly work to make this test pass

<details>
  <summary>Making the test pass</summary>

  ```clojure
  
  (defn- distance-between
    [cell other-cell]
    (list 
     (- (x-coordinate-from cell) (x-coordinate-from other-cell)) 
     (- (y-coordinate-from cell) (y-coordinate-from other-cell))))

  (defn- distance-less-than-two-between?
    [cell other-cell]
    (< (reduce max (distance-between cell other-cell)) 2))

  (defn is-neighbour-of?
    [given-cell]
    (fn 
      [cell] 
      (and (not(= cell given-cell)) (distance-less-than-two-between? cell given-cell))
    ))
  ```
  
</details>
</details>

Now see what happens if we test a right-edge cell.

<details>
  <summary>A right-edge cell should have five neighbours</summary>

  ```clojure
  (deftest neighbours-of-right-edge-center-cell 
    (testing "Neighbours of right edge center cell.") 
      (is 5 (count (filter (is-neighbour-of? (living-cell 1 2)) GAME))))
  ```

We note that this test fails, as the subtraction of the indices 
may become negative. Note that we only have to apply a fix to
the subtraction of the y-coordinates to make the test pass!

<details>
  <summary>Making the test pass</summary>

  ```java
    (defn- distance-between
      [cell other-cell]
      (list 
       (- (x-coordinate-from cell) (x-coordinate-from other-cell)) 
       (Math/abs (- (y-coordinate-from cell) (y-coordinate-from other-cell)))))
  ```
  
</details>
</details>

We can force a similar generalization for the x-coordinate by writing
a test for the top-edge cell. As the test and solution are almost identical
to the code snippets listed above, this is left as an exercise for the reader.

### Living neighbours

Ultimately, we are interested in the living neighbours of a cell, given a board.
So let's write a specification that defines precisely this feature, namely a function
that returns a list of living neighbours of a given cell in a game.

<details>
  <summary>Defining the <code>living-neighbours-in</code> function</summary>

  ```clojure
  (deftest living-neighbours-of-center-cell
    (testing "Living neighbours of center cell.")
      (is (= 4 (count ((living-neighbours-in GAME) (living-cell 1 1))))))
  ```

We can easily make this test pass.

<details>
  <summary>Making the test pass</summary>

  ```clojure
  (defn living-neighbours-in
    [game]
    (fn [cell] (filter is-alive? (filter (is-neighbour-of? cell) game) )))
  ```
  
</details>
  
</details>


## Implementation of the rules of the game of life

### The predicates

Remember that the rules of the game of life are based on the number of living neighbours:

- A dead cell resurrects if it _has exactly three_ living neighbours
- A living cell dies if it _has less than two_ living neighbours
- A living cell dies if it _has more than three_ living neighbours

The predicates are easily distilled from these game rules: they are
written in italics!


<details>
  <summary>Defining the tests for the predicates</summary>

  ```clojure
  (deftest has-has-exactly-three-living-neighbours
    (testing "Filter out all cells that have exactly 3 living neighbours")
      (is (= 4 (count (filter (has-exactly-three? (living-neighbours-in GAME)) GAME)))))
  ```

The implementation of this predicate is relatively straightforward.

<details>
  <summary>Implementation of the predicate</summary>

  ```clojure
  (defn has-exactly-three?
    [find-neighbours-for]
    (fn [cell] (= 3 (count (find-neighbours-for cell)))))
  ```
</details>
  
</details>

Finally, the other predicates are implemented analogously, so we don't
include them here for the sake of brevity.

### Applying the rules in a game by combining predicates

Eventually, we want to apply these rules to each cell in a game when
going to the next iteration:

- if a cell is dead _and_ has exactly three living neighbours, it should be
  mapped to a living cell
- if a cell is alive _and_ has less than two living neightbours _or_
  more than three living neighbours, it should be mapped to a dead cell
- All other cells should be left unchanged

So we need a means to combine predicates with _and_ and _or_.

<details>
  <summary>Definitions of the <code>which-either</code> and <code>which-both</code> predicates</summary>

  ```clojure
  ; --------------------------------------------------------+
  ; Filtering with multiple predicates:                     |
  ; https://groups.google.com/g/clojure/c/O977jrXU-Cg?pli=1 |
  (defmacro which-either [& predicates]                    ;| 
    (let [x# (gensym)]                                     ;|
    `(fn [~x#] (or ~@(map #(list % x#) predicates)))))     ;|
                                                         ;|
  (defmacro which-both [& predicates]                      ;|   
    (let [x# (gensym)]                                     ;|
    `(fn [~x#] (and ~@(map #(list % x#) predicates)))))    ;|
  ; --------------------------------------------------------+
  ```
</details>

We have now constructed a domain-specific language with which we
can realize the snippet from the teaser listed at the beginning of 
these instructions!

<details>
  <summary>Defining the <code>next-generation-of</code> function</summary>

  ```clojure
  (def BLINKER_START (list 
           (dead-cell 0 0) (living-cell 0 1) (dead-cell 0 2)
           (dead-cell 1 0) (living-cell 1 1) (dead-cell 1 2)
           (dead-cell 2 0) (living-cell 2 1) (dead-cell 2 2) ))

  (def BLINKER_END (list 
           (dead-cell 0 0)   (dead-cell 0 1)   (dead-cell 0 2)
           (living-cell 1 0) (living-cell 1 1) (living-cell 1 2)
           (dead-cell 2 0)   (dead-cell 2 1)   (dead-cell 2 2) ))


(deftest next-iteration-of-blinker
  (testing "Next iteration of blinker.")
  (is (= BLINKER_END (next-generation-of BLINKER_START))))
  ```

We can finally make this test pass.

<details>
  <summary>Making the test pass</summary>

  ```clojure
  (defn next-generation-of
    [game]
    (map #(to-living-cell 
           (which-both 
            is-dead? 
            (has-exactly-three? (living-neighbours-in game))) %) 
    (map #(to-dead-cell 
           (which-both 
            is-alive? 
            (which-either 
             (has-less-than-two? (living-neighbours-in game)) 
             (has-more-than-three? (living-neighbours-in game))) ) %) game)   )
    )
  ```
  
</details>
  
</details>

## Putting it all together

### Setting up and displaying a game

First, we need to be able to create a game-of-life world. And equally important,
we need to be able to check (and watch/inspect) it. For example, a blinker 
oscillator should be something like

``` 
-----
--#--
--#--
--#--
-----
```

Roughly speaking, we may distinguish the following steps:

1. So first of all, a cell should be mapped to
   either `-` or `#`, depending on whether it is alive or not.

2. Secondly, this strongly suggests to generate a list of strings (`List<String>`)
   as output to represent a game board, so we need a mapping from the list of cells
   to a list of strings.

3. As a consequence, it would also be convenient to have a function
   that initializes a game board by using the same list of strings.

### 1. Mapping a cell to a string

Look at the Java solution on how to approach this.

### 2. Mapping the list of cells to a list of strings

Look at the Java solution on how to approach this.

### 3. Initializing a board

Look at the Java solution on how to approach this.

### 4. The iteration logic

Look at the Java solution on how to approach this.
