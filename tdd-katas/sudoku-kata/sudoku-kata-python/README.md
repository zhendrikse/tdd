# Introduction

Please read the general [introduction to the sudoku kata](../README.md) first!

# Getting started

First, create an intial Python kata set-up as described [here](https://github.com/zhendrikse/tdd/tree/master/cookiecutter).

Next, go the the newly created project directory and consult
the provided ``README.md`` in there.

# Instructions

## 1. Initialization

Let's first initialize a Sudoku puzzle from a string:

```python
with context("Given a string"):
  with it("initializes the puzzle"):
    puzzle = ".5..83.17...1..4..3.4..56.8....3...9.9.8245....6....7...9....5...729..861.36.72.4"
    expect(Sudoku(puzzle).puzzle[0][0]).to(equal(0))
    expect(Sudoku(puzzle).puzzle[8][8]).to(equal(4))
```
---

#### Exercise I
The first exercise is to finish up the implementation for this specification. Note that a value of zero is used to indicate that a value still needs to be found, i.e. represents an empty cell in the initial puzzle.

---

## 2. Validation

Next we need to be able to check whether trying a value in at a certain location is allowed or not:

```python
with it("identifies a given cell value is present in a row"):
  self.sudoku.puzzle[0][0] = 5
  expect(self.sudoku.duplicate_cell_value_in_row(0, 0)).to(be_true)

with it("identifies a given cell value is absent in a row"):
  self.sudoku.puzzle[0][0] = 2
  expect(self.sudoku.duplicate_cell_value_in_row(0, 0)).to(be_false)
```
---

#### Exercise II
Write the implementation and repeat the above for the column check.

---

Finally, we have to check for the uniqueness in the 3x3 box.

---

#### Exercise III
Write the scenario(s) and associated implementation for the 3x3 box check.

---

Finally, let's combine all these checks into one method call.

---

#### Exercise IV
Write the scenario(s) and associated implementation for a method that does all the above checks in one method call.

---

## 3. Solving the puzzle

At this point, you may want to try to solve the puzzle by recursively invoking a function `solve(self, row, column)`. First, of course, we have to write a test. The test should verify the outcome, so e.g. given an initial puzzle of 

```python
puzzle_string = ".5..83.17...1..4..3.4..56.8....3...9.9.8245....6....7...9....5...729..861.36.72.4"
```

The solution should be

```python
with it("solves the puzzle"):
  solution_string = "652483917978162435314975628825736149791824563436519872269348751547291386183657294"
  solved_puzzle = Sudoku(solution_string)

  expect(self.sudoku.solve(0, 0)).to(be_true)

  for i in range(81):
    expect(self.sudoku.puzzle[i // 9][i % 9]).to(equal(solved_puzzle.puzzle[i // 9][i % 9]))
```

In case this challenge is still too daunting at this point, please continue follow the instructions a bit further. You'll be given a couple of additional hints.


## 4. Additional preparations

We need to be able to determine if a cell has already been assigned a value or whether it needs to be filled by us (in which case it still has a default value of zero).

---

#### Exercise V
Specify/test the behavior of a function returning a boolean that checks whether a cell is empty or not and implement it accordingly!

---

Last but not least, we need functions to determine the next values for our row and column paraters if we want to advance one cell in the Sudoku puzzle.

---

#### Exercise VI

Implement _scenarios and [(Python class) methods](https://www.geeksforgeeks.org/class-method-vs-static-method-python/)_ that determine the next values for the row and column parameters if we advance one cell. Obviously, if we reached the end of a row, we have to reset the column to zero and increment the row by one.

```python
@classmethod
def next_row(cls, row:int, column:int) -> int:
  # Implementation goes here

@classmethod
def next_column(cls, row:int, column:int) -> int:
  # Implementation goes here
```

---

All preparations have been done for now. Perhaps you may want to do some additional refactoring at this point before we continue. 

If not, we can now implement the actual solver using back tracking. 

## 5. Solving the puzzle

At this point we have to write a recursive function to solve the puzzle. This function consists of the following steps:

1. Check if we have already reached the last cell, in which case we end the recursion and return a value of `True` to indicate that a solution has been found.
2. If the current cell is given/filled already, invoke `solve` for the next cell.
3. Now in all other cases (so we haven't reached the last cell, nor is the cell already given in the puzzle), we have to start building a tree of possibilities and back track whenever we stumble upon an invalid configuration:
   - try all values 1...9 by creating a loop for these values
   - check for each value if this value is allowed. If not, continue with the next value. If it is, invoke `solve` for the next cell.
   - after the loop, we are apparently in a situation that all values 1...9 failed. In this case we reset the cell value back to its original value of zero and return false, as a signal that we need to back track.

---

#### Exercise VII 
Solve the puzzle by recursively invoking a function `solve(self, row, column)`. Section 3 contains a scenario that you can use to write the test first. Use the instructions listed above as a source of inspiration.

---

![Spoiler](./assets/spoiler.png)
<p align="center" ><b>Figure 1</b>: <i>In case you are stuck, you can find some code snippets below.</i></p>

At this point, you can use the following code snippets. They correspond to the steps in the algorithm listed above:

1. Check if we have already reached the last cell:
  ```python
    # arrived at last cell? --> done, so return
    if (index.is_last_cell()):
      return True
  ```

2. If the current cell is given, invoke solve for the next cell:
  ```python
  # go to next cell if cell value is given
  if not self.is_cell_empty(index):
    return self.solve(index.next()) 
  ```

3. Cell is still empty, so start trying:
  ```python
  # build tree for each allowed value 1...9
  for i in range(1, 10):
    self.puzzle[index.row][index.column] = i
    if not self.cell_value_allowed(index): 
      continue
    if self.solve(index.next()): 
      return True
   ```

4. Back track if all values in for-loop have failed

   ```python
    # backtrack because at this point all values failed
    self.puzzle[index.row][index.column] = 0 
    return False 
   ```

## 6. Refactoring the data clump

By inspecting the code the [data clumping](https://refactoring.guru/smells/data-clumps) of the row and column parameters immediately pops to the eye. 

This strongly suggests that both paramters form a unit. Let's call this unit a `SudokuIndex` and let's assign this value object its own class. This class then automatically becomes a behavior attractor:

> Think about behaviour attraction. Quite often, you can reduce the amount of behaviour that relies upon primitives from the outside world (as opposed to internal primitives stored as private fields or locals) simply by moving the behaviour to a value object which holds the primitives. If you don’t have a value object, create one. These value objects are known as behaviour attractors because once they’re created, they make it far more obvious where behaviour should live &#8212; [kata-log.rocks](https://kata-log.rocks/task-list-kata)

In our case, the logic to determine the next value for the row and column parameters when advancing to the next cell are now kind of naturally "attracted" towards this `SudokuIndex` value object:

```python
from dataclasses import dataclass

@dataclass(frozen = True)
class SudokuIndex(object):
  row: int
  column: int
  
  def next_row(self) -> int:
    # Implementation goes here

  def next_column(self) -> int:
    # Implementation goes here

  def next(self):
    # Implementation goes here

  def is_last_cell(self) -> bool:
    # Implementation goes here
```

---

#### Exercise VIII 
Refactor the code using the above value object.

---