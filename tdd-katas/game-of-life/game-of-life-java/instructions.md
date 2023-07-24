# Introduction

Please read the general [introduction to the game of life kata](../README.md) first!

# Getting started

First, create an intial Java kata set-up as described [here](https://github.com/zhendrikse/tdd/tree/master/cookiecutter).

Next, go the the newly created project directory and consult
the provided ``README.md`` in there.

# Functional implementation

## Source

This kata is a TDD version of the excellent functional solution proposed in 
[this excellent post](https://medium.com/@davidibl/functional-java-9e95a647af3c)
and the associated 
[code repository](https://github.com/davidibl/GameOfLifeFunctional/tree/master) 
mentioned therein.

## Living and dead cells

Let's write our first specification(s) for predicates of living and
dead cells.

<details>
  <summary>Predicates for living and dead cells</summary>

  ```java
  import static gameoflife.Cell.*;

  class GameOfLifeTest {
    @Test 
    void isLivingPredicate() {
      assertNotNull(Optional.of(newLivingCell()).filter(isLiving).get());
      assertTrue(Optional.of(newDeadCell()).filter(isLiving).isEmpty());
    }
  
    @Test
    void isDeadPredicate() {
      assertNotNull(Optional.of(newDeadCell()).filter(isDead).get());
      assertTrue(Optional.of(newLivingCell()).filter(isDead).isEmpty());
    }
  }
  ``` 
  where the `newDeadCell()`, `newLivingCell()`, `isAlive`, and `isDead`
  methods and predicates are (to be) defined in the `Cell` class.

  <details>
  <summary>Definition of the <code>Cell</code> class that makes the test pass</summary>
  
  ```java
  public class Cell {
    private final boolean alive;
  
    private Cell(final boolean alive) {
      this.alive = alive;
    }
  
    private boolean isAlive() {
      return alive;
    }
    
    public static final Cell newLivingCell() {
      return new Cell(true);
    }
    
    public static final Cell newDeadCell() {
      return new Cell(false);
    }
  
    public static Predicate<Cell> isAlive = Cell::isLiving;
    
    public static Predicate<Cell> isDead = isLiving.negate();
  }
  ```
  </details>

  We may want to refactor the tests a bit to express intent more clearly



  <details>
  <summary>Refactoring the tests to express intent more clearly</summary>
  
  ```java
    class GameOfLifeTest {

      private boolean isDead(final Cell cell) {
        return !Optional.of(cell).filter(isDead).isEmpty();
      }
    
      private boolean isLiving(final Cell cell) {
        return !Optional.of(cell).filter(isLiving).isEmpty();
      }
    
      @Test 
      void isLivingPredicate() {
        assertTrue(isLiving(newLivingCell()));
        assertFalse(isLiving(newDeadCell()));
      }
    
      @Test
      void isDeadPredicate() {
        assertFalse(isDead(newLivingCell()));
        assertTrue(isDead(newDeadCell()));
      }
    }
  ```
  </details>
  </details>

  ## Killing and resurrecting cells

  We should be able to change cells from living to dead and vice versa.
  In functional programming this means creating new cells, as we cannot
  change state (because of immutability!).

  Note that we would like to conditionally transition from a living to 
  a dead cell, e.g. depending on the status of the cell itself (we 
  cannot kill an already dead cell). More importantly, eventually we 
  woudld like to conditionally kill a cell, depending on the conditions 
  and rules imposed by its neighbours.

  Summarizing, we want to map a list of cells to dead cells, given 
  a certain condition (= predicate!).

<details>
  <summary>The specification for the <code>toDeadCell(Predicate&lt;Cell&gt; isCellKillable)</code> mapping</summary>

  ```java
    @Test
    void toDeadCellMapping() {
      Predicate<Cell> ifCellKillable = isLiving;
      Optional<Cell> mappedList = 
        Optional
        .of(livingCell(0, 0))
        .map(toDeadCell(ifCellKillable));
      
      assertFalse(mappedList.isEmpty());
      assertTrue(isDead(mappedList.get()));
    }
  ```
</details>

And the code that makes this test pass

<details>
  <summary>The implementation for the <code>toDeadCell(Predicate&lt;Cell&gt; isCellKillable)</code> mapping</summary>

  ```java
  public static Function<Cell, Cell> toDeadCell(Predicate<Cell> isCellKillable) {
    return cell -> Optional
      .of(cell)
      .filter(isCellKillable.negate())
      .orElse(newDeadCell());  
  }
  ```
</details>

Analogously we implement the `toLivingCell(Predicate<Cell> isCellViable)`.

## Introduction of coordinates

As we need to be able to determine the neighbours of a cell, we need  
to introduce coordinates in the cell.

<details>
  <summary>Introduction of coordinates in a cell</summary>

  ```java
  public class Cell {
    private final boolean alive;
    private final int x;
    private final int y;
    
    private Cell(final int x, final int y, final boolean alive) {
      this.alive = alive;
      this.x = x;
      this.y = y;
    }
  
    private boolean isAlive() {
      return alive;
    }
    
    public static final Cell newLivingCell(final int x, final int y) {
      return new Cell(x, y, true);
    }
    
    public static final Cell newDeadCell(final int x, final int y) {
      return new Cell(x, y, false);
    }
  
    public static Predicate<Cell> isLiving = Cell::isAlive;
    
    public static Predicate<Cell> isDead = isLiving.negate();
  
    public static Function<Cell, Cell> toDeadCell(Predicate<Cell> isCellKillable) {
      return cell -> Optional
        .of(cell)
        .filter(isCellKillable.negate())
  			.orElse(newDeadCell(cell.x, cell.y));  
    }
  
    public static Function<Cell, Cell> toLivingCell(Predicate<Cell> isCellViable) {
      return cell -> Optional
        .of(cell)
        .filter(isCellViable.negate())
  			.orElse(newLivingCell(cell.x, cell.y));  
    }
  }
  ```
</details>

The tests need to be modified accordingly as well, of course!

## Determining the living neighbours

The rules of the game depend on the number of living neighbours.
Consequently, we need to define a predicate that for a given field
determines the number of living neighbours in a game.
