# Introduction

Please read the general [introduction to the stack kata](../README.md) first!

# Getting started

First, create an intial Python kata set-up as described [here](https://github.com/zhendrikse/tdd/tree/master/cookiecutter).

Next, go the the newly created project directory and consult
the provided ``README.md`` in there.

# Game of life

## The specifications for a living cell and its neighbours

- The first specifications we are going to write are for a living cell. The most simple case is a living cell with one living neighbour. On a next generation, it then dies:
  ```python
  with description("Game of life") as self:
    with context("Living cell survival"):
      with it("dies on one living neighbour"):
        expect(Cell(alive = True).next_generation([Cell(alive = True)]).is_alive()).to(be_false)
  ```
  Write the implementation to suffice the spec. Also apply a refactoring by implementing and using the two functions
  ```python
  def dead_cell():
  return Cell(alive = False)

  def living_cell():
    return Cell(alive = True)
  ```

- Next we specify that a living cell survives when it has two living neigbours:
  ```python
    with it("survives on two living neighbours"):
      expect(living_cell().next_generation([living_cell(), living_cell()]).is_alive()).to(be_true)
  ```
  Let's make this test succeed by testing just the number of neighbours: if it is two, we return a living cell.

- We need to force the production code not only to look at the number of neighbours, but also their state. To this extent, we create an additional test with two neighbours, but in this case one of the neighbours is dead:
  ```python
    with it("dies on one living and one dead neighbour"):
      expect(living_cell().next_generation([living_cell(), dead_cell()]).is_alive()).to(be_false)
   ```
  We fix this by filtering out the living neighbours from the incoming list of neighbours.

- The cell should also survive with three living neighbours, so
 ```python
    with it("survives on three living neighbours"):
      expect(living_cell().next_generation([living_cell(), living_cell(), living_cell()]).is_alive()).to(be_true)
  ```
  We fix this by specifying at least 2 living neighbours (">=")

- However, a living cell should die on overpopulation when it has 4 living neighbours (or more):
  ```python
    with it("dies on four living neighbours"):
      expect(living_cell().next_generation([living_cell(), living_cell(), living_cell(), living_cell()]).is_alive()).to(be_false)
  ```
  We fix this by specifying either two or three living neighbours in the
  if-statement.

## The specifications for a dead cell and its neighbours

As we have specified all scenarios for a living cell and its neighbours, we now switch to the scenarios for a dead cell and its neighbours.

- First we specify that a dead cell remains dead with two living neighbours:
  ```python
      with it("remains dead on two living neighbours"):
      expect(dead_cell().next_generation([living_cell(), living_cell()]).is_alive()).to(be_false)
   ```
- Next, a dead cell resurrects when it has three living neighbours:
  ```python
      with it("resurrects on three living neighbours"):
      expect(dead_cell().next_generation([living_cell(), living_cell(), living_cell()]).is_alive()).to(be_true)
   ```
  We fix this by merely checking if the number of neighbours in the if-branch
  for the case the cell is dead.

- Again, we need to force the if-statement for the dead cells to also take into account the number of _living_ neighbours, so we write a test to make that happen:
  ```python
  with it("remains dead on one dead on two living neighbours"):
    expect(dead_cell().next_generation([dead_cell(), living_cell(), living_cell()]).is_alive()).to(be_false)
  ```

## Determining the neighbours of a cell in a game

- Let's implement the game as a matrix of cells. As Python is a dynamically typed language, we can temporarily use integers as contents of the game matrix. Later we can effortlessly substitute the cells for the integers.
  ```python
  with context("Neighbours in game"):
    with it("has eight neighbours for non-edge cells"):
      game = Game([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
      expect(game.neighbours_for(1, 1)).to(equal([1, 2, 3, 4, 6, 7, 8, 9]))
  ```
  Fix this by returning the expected array of values first. Next, notice that
  we have duplication in the test and production code. So we can and should already
  generalize the entries of the returned array of cells by replacing the hard-coded
  integer values by the references to the neighbour cells like so:
  ```self.cell_at(row-1, column-1)```, e.g. for the top left neighbour.

- Now that we have determined the neighbours for a non-edge cell, let's formulate
  the specifications for the edge cells:
  ```python
    with it("has five neighbours for left edge cell"):
      game = Game([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
      expect(game.neighbours_for(1, 0)).to(equal([1, 2, 5, 7, 8]))
  ```
  Make the test green by returning a ```None``` value in the ```cell_at()```
  method whenever the index of the column becomes less than zero. Finally,
  remove the ```None``` elements from the list of all neighbours.

- Proceed analogously for the other edge cases.

## Next generation for a game

- Let's specify a ```next_generation()``` method on the game:
  ```python3
      with it("creates a new game with a next generation for all fields in a row"):
      game = Game([[living_cell(), living_cell(), living_cell()]])
      game = game.next_generation()
      expect(game.cell_at(0, 0)).to(equal(dead_cell()))
      expect(game.cell_at(0, 1)).to(equal(living_cell()))
      expect(game.cell_at(0, 2)).to(equal(dead_cell()))
  ```
  First, we make the ```next_generation()``` method return a game with the
  cells in a state as required by the specification. Again, we notice a duplication
  between the test and production code, and hence we can and should generalize as
  follows:
  ```python
    def next_generation(self):
    return Game([[
      self.cell_at(0, 0).next_generation(self.neighbours_for(0, 0)), 
      self.cell_at(0, 1).next_generation(self.neighbours_for(0, 1)), 
      self.cell_at(0, 2).next_generation(self.neighbours_for(0, 2)) 
      ]])
  ```
  Obviously, this should furhter be optimized like so:
  ```python
    def next_generation(self):
    row = 0
    return Game([[
      self.cell_at(row, i).next_generation(self.neighbours_for(row, i)) for i in range(self.width) 
      ]])
   ```
  
- Finally, we specify what the game must do for all fields in a column:
  ```python  
  with it("creates a new game with a next generation for all fields in a column"):
    game = Game([[living_cell()], [living_cell()], [living_cell()]])
    game = game.next_generation()
    expect(game.cell_at(0, 0)).to(equal(dead_cell()))
    expect(game.cell_at(1, 0)).to(equal(living_cell()))
    expect(game.cell_at(2, 0)).to(equal(dead_cell()))
   ```
  We make the test green by iterating through all the rows.

## Demonstrating the code

We can now demonstrate a working version of game of life by adding the following lines to the production code:
```python
from random import choice
import os, time

if __name__ == '__main__':
    game = Game([[choice([dead_cell, living_cell])()
        for c in range(80)]
            for r in range(40)])
    while True:
        os.system('clear')
        print(game)
        game = game.next_generation()
        time.sleep(0.4)
```

When running this, we notice that the game class doesn't have a string representation yet, so let's add that
```python
    def __str__(self):
      result = ""
      for row in range(0, self.height):
        line="".join([self.cell_at(row, column).char_repr() for column in range(0, self.width)])
        result += "\n"+ line

      return result
```
Finally we add the ```char_repr()``` method to the cell class
```python
  def char_repr(self):
    return "#" if self.is_alive() else " "
```
to arrive at a fully working version of the game of life!