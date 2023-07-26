# Introduction

Please read the general [introduction to the game of life kata](../README.md) first!

# Teaser

We are going to build the following code, which is a showcase of _code should
express intent_, Kent Beck's design rule number 2!

```java
public static List<Cell> iterateGameboard(final List<Cell> gameboard) {
  return gameboard
      .stream()
        .map(toDeadCell(which(isLiving, and(), 
            which(hasLessThanTwo(livingNeighboursIn(gameboard)), or(), hasMoreThanThree(livingNeighboursIn(gameboard))))))
        .map(toLivingCell(which(isDead, and(), hasExactlyThree(livingNeighboursIn(gameboard)))))
        .collect(Collectors.toList());
}
```

The approach here is an almost literral TDD version of the 
excellent functional solution proposed in 
[this excellent post](https://medium.com/@davidibl/functional-java-9e95a647af3c)
and the associated 
[code repository](https://github.com/davidibl/GameOfLifeFunctional/tree/master) 
mentioned therein.

# Getting started

First, create an intial Java kata set-up as described [here](https://github.com/zhendrikse/tdd/tree/master/cookiecutter).

Next, go the the newly created project directory and consult
the provided ``README.md`` in there.

# Functional implementation

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

### Determining the neigbours of a cell

Let's create a separate test class containing the specifications
for the neighbours and tackle the most generic case first, namely
a non-edge cell should have eight neighbours.

<details>
  <summary>A non-edge cell should have eight neighbours</summary>

  ```java
  class NeighboursTest {
    @Test
    void filterNeighboursForGivenCenterCell() {
      List<Cell> game = List.of(
        livingCell(0, 0), livingCell(0, 1), livingCell(0, 2),
        livingCell(1, 0), livingCell(1, 1), livingCell(1, 2),
        livingCell(2, 0), livingCell(2, 1), livingCell(2, 2)
      );    
      
      assertEquals(8, 
        game.stream()
          .filter(isNeighbourOf(game.get(4)))
          .collect(Collectors.toList())
          .size());
    }
  }
  ```

and the simplest thing/solution that could possibly work to make this test pass

<details>
  <summary>Making the test pass</summary>

  ```java
   public static Predicate<Cell> isNeighbourOf(final Cell givenCell) {
    return cell -> !cell.equals(givenCell);
   }
  ```
  
</details>
</details>

Next we test for a left-edge cell.

<details>
  <summary>A left-edge cell should have five neighbours</summary>

  ```java
  class NeighboursTest {
    @Test
    void filterNeighboursForGivenLeftEdgeCell() {
      List<Cell> game = List.of(
        livingCell(0, 0), livingCell(0, 1), livingCell(0, 2),
        livingCell(1, 0), livingCell(1, 1), livingCell(1, 2),
        livingCell(2, 0), livingCell(2, 1), livingCell(2, 2)
      );    
      
      assertEquals(5, 
        game.stream()
          .filter(isNeighbourOf(game.get(3)))
          .collect(Collectors.toList())
          .size());
    }
  }
  ```

and the simplest thing/solution that could possibly work to make this test pass

<details>
  <summary>Making the test pass</summary>

  ```java
  public static Predicate<Cell> isNeighbourOf(final Cell givenCell) {
    return cell -> 
      !cell.equals(givenCell) &&
      (cell.x - givenCell.x < 2) && 
      (cell.y - givenCell.y < 2); 
  }
  ```
  
</details>

Obviously, we have to apply the DRY principle in the tests:

<details>
  <summary>Applying the DRY principle to the tests</summary>

  ```java
  class NeighboursTest {
    private List<Cell> game;
  
    @BeforeEach
    private void setUpGame() {
      game = List.of(
        livingCell(0, 0), livingCell(0, 1), livingCell(0, 2),
        livingCell(1, 0), livingCell(1, 1), livingCell(1, 2),
        livingCell(2, 0), livingCell(2, 1), livingCell(2, 2)
      );    
    }
    
    @Test
    void filterNeighboursForGivenCenterCell() {
      assertEquals(
        game.stream()
        .filter(isNeighbourOf(game.get(4)))
        .collect(Collectors.toList())
        .size(), 8);
    }  
    // ...
  ```
  
</details>
</details>

Now see what happens if we test a right-edge cell.

<details>
  <summary>A right-edge cell should have five neighbours</summary>

  ```java
  class NeighboursTest {
    @Test
    void filterNeighboursForGivenRightEdgeCell() {
      List<Cell> game = List.of(
        livingCell(0, 0), livingCell(0, 1), livingCell(0, 2),
        livingCell(1, 0), livingCell(1, 1), livingCell(1, 2),
        livingCell(2, 0), livingCell(2, 1), livingCell(2, 2)
      );    
      
      assertEquals(5, 
        game.stream()
          .filter(isNeighbourOf(game.get(5)))
          .collect(Collectors.toList())
          .size());
    }
  }
  ```

We note that this test fails, as the subtraction of the indices 
may become negative. Note that we only have to apply a fix to
the subtraction of the y-coordinates to make the test pass!

<details>
  <summary>Making the test pass</summary>

  ```java
  public static Predicate<Cell> isNeighbourOf(final Cell givenCell) {
    return cell -> 
      !cell.equals(givenCell) &&
      (cell.x - givenCell.x < 2) && 
      (Math.abs(cell.y - givenCell.y) < 2); 
  }
  ```
  
</details>
</details>

We can force a similar generalization for the x-coordinate by writing
a test for the top-edge cell. As the test and solution are almost identical
to the code snippets listed above, this is left as an exercise to the reader.

### Living neighbours

Ultimately, we are interested in the living neighbours of a cell, given a board.
So let's write a specification that defines precisely this feature, namely a function
that returns a list of living neighbours of a given cell in a game.

<details>
  <summary>Defining the <code>Function&lt;Cell, List&lt;Cell&gt;&gt; livingNeighboursIn(game)</code> function</summary>

  ```java
  class GameTest {
    @Test
    void assertNumberOfLivingNeighboursInAGameForAGivenCell() {
      List<Cell> game = List.of(
        deadCell(0, 0), livingCell(0, 1), livingCell(0, 2),
        livingCell(1, 0), livingCell(1, 1), deadCell(1, 2),
        deadCell(2, 0), livingCell(2, 1), deadCell(2, 2)
      );
  
      assertEquals(livingNeighboursIn(game).apply(game.get(0)).size(), 3);
      assertEquals(livingNeighboursIn(game).apply(game.get(1)).size(), 3);
      assertEquals(livingNeighboursIn(game).apply(game.get(2)).size(), 2);
      assertEquals(livingNeighboursIn(game).apply(game.get(3)).size(), 3);
      assertEquals(livingNeighboursIn(game).apply(game.get(4)).size(), 4);
      assertEquals(livingNeighboursIn(game).apply(game.get(5)).size(), 4);
      assertEquals(livingNeighboursIn(game).apply(game.get(6)).size(), 3);
      assertEquals(livingNeighboursIn(game).apply(game.get(7)).size(), 2);
      assertEquals(livingNeighboursIn(game).apply(game.get(8)).size(), 2);
    } 
  }
  ```

We can easily make this test pass.

<details>
  <summary>Making the test pass</summary>

  ```java
  public class Game {
    public static Function<Cell, List<Cell>> livingNeighboursIn(final List<Cell> game) {
      return cell -> game
        .stream()
  			.filter(isNeighbourOf(cell))
        .filter(isLiving)
  			.collect(Collectors.toList());      
    }  
  }
  ```
  
</details>
  
</details>

Note that we define this function in a dedicated `Game` class with an 
associated class containing the tests.

## Implementation of the rules of the game of life

### The predicates

Remember that the rules of the game of life are based on the number of living neighbours:

- A dead cell resurrects if it _has exactly three_ living neighbours
- A living cell dies if it _has less than two_ living neighbours
- A living cell dies if it _has more than three_ living neighbours

The predicates are easily destilled from these game rules: they are
written in italics!


<details>
  <summary>Defining the tests for the predicates</summary>

  ```java
  @Test
  void assertExactlyThreeLivingNeighboursForAGivenCellInAGame() {
    List<Cell> game = List.of(
      deadCell(0, 0), livingCell(0, 1), livingCell(0, 2),
      livingCell(1, 0), livingCell(1, 1), deadCell(1, 2),
      deadCell(2, 0), livingCell(2, 1), deadCell(2, 2)
    );

    assertEquals(4, 
      game.stream()
      .filter(hasExactlyThree(livingNeighboursIn(game)))
      .collect(Collectors.toList())
      .size()
    );
  }
  ```

The implementation of this predicate is relatively straight foward.

<details>
  <summary>Implementation of the predicate</summary>

  ```java
	public static Predicate<Cell> hasExactlyThree(Function<Cell, List<Cell>> findNeighbours) {
		return cell -> findNeighbours.apply(cell).size() == 3;
	}
  ```
</details>
  
</details>

Obviously, we should apply the DRY principle once more in the test class,
as we have duplicated the set-up of a game.

Finally, the other predicates are implemented analogously, so we don't
include them here for the sake of brevity.

### Applying the rules in a game by combining predicates

Eeventually we want to apply these rules to each cell in a game when
going to the next iteration:

- if a cell is dead _and_ has exactly three living neighbours, it should be
  mapped to a living cell
- if a cell is alive _and_ has less than two living neightbours _or_
  more than three living neighbours, it should be mapped to a dead cell
- All other cells should be left unchanged

So we need a means to combine predicates with _and_ and _or_.

<details>
  <summary>Specification for the <code>or()</code> predicate</summary>

  ```java
  class FunctionalExtensionsTest {
  
    private static final String AAP = "Aap";
    private static final String NOOT = "Noot";
    private static final String MIES = "Mies";
    private static final String WIM = "Wim";
    private static final String ZUS = "Zus";
    private static final String JET = "Jet";
    private static final String FILTER_VALUE = WIM;
    
    
    private static final List<String> READING_SHELF = List.of(AAP, NOOT, MIES, WIM, ZUS, JET);
    private static final Predicate<String> isWim = word -> word.equals(WIM);
    private static final Predicate<String> isMies = word -> word.equals(MIES);
    
    @Test
    void orBiFunctionCombinesPredicates() {
      List<String> filteredList = READING_SHELF
        .stream()
        .filter(or.apply(isMies, isWim))
        .collect(Collectors.toList());
    
      assertEquals(2, filteredList.size());
      assertTrue(filteredList.contains(WIM));
      assertTrue(filteredList.contains(MIES));
    }
  ```
  And the code that makes the test pass:

<details>
  <summary>Definition of the <code>or()</code> predicate</summary>

  
  ```java
	public static <T> BiFunction<Predicate<T>, Predicate<T>, Predicate<T>> or() {
		return (predicateLeft, predicateRight) -> predicateLeft.or(predicateRight);
	}
  ```
</details>

</details>

Analogously we implement the `and()` and `which()` predicates.

<details>
  <summary>Specification for the <code>and()</code> and <code>which()</code>code> predicates</summary>

  ```java
  @Test
  void andBiFunctionCombinesPredicates() {
    List<String> filteredList = READING_SHELF
      .stream()
      .filter(and.apply(isMies, isWim))
      .collect(Collectors.toList());

    assertTrue(filteredList.isEmpty());
  }
 
  @Test
  void whichFunctionCombinesPredicates() {
    List<String> filteredList = READING_SHELF
      .stream()
      .filter(which(isMies, or, isWim))
      .collect(Collectors.toList());

    assertEquals(2, filteredList.size());
    assertTrue(filteredList.contains(WIM));
    assertTrue(filteredList.contains(MIES));
  }
  ```
  And the code that makes the test pass:

<details>
  <summary>Definition of the <code>or()</code> predicate</summary>
  
  ```java
	public static <T> BiFunction<Predicate<T>, Predicate<T>, Predicate<T>> and() {
		return (predicateLeft, predicateRight) -> predicateLeft.and(predicateRight);
	}

  public static <T> Predicate<T> which(Predicate<T> leftPredicate,
			BiFunction<Predicate<T>, Predicate<T>, Predicate<T>> combiner, Predicate<T> rightPredicate) {
		return combiner.apply(leftPredicate, rightPredicate);  
  ```
</details>

</details>

We have now constructed a domain specific language with which we
can realise the snippet from the teaser listed in the beginning of 
these instructions!


```java
public static List<Cell> iterateGameboard(final List<Cell> gameboard) {
  return gameboard
      .stream()
        .map(toDeadCell(which(isLiving, and(), 
            which(hasLessThanTwo(livingNeighboursIn(gameboard)), or(), hasMoreThanThree(livingNeighboursIn(gameboard))))))
        .map(toLivingCell(which(isDead, and(), hasExactlyThree(livingNeighboursIn(gameboard)))))
        .collect(Collectors.toList());
}
```

## Putting it all together

### Setting up and displaying a game

First we need to be able to create a game of life world. And equally important,
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
   either `-` or `#`, depening on whether it is alive or not.

2. Secondly, this strongly suggests to generate a list of strings (`List<String>`)
   as output to represent a game board, so we need a mapping from `List<Cell>`
   &rarr; `List<String>`.

3. As a consequence, it would also be convenient to have a method
   that initializes a game board by using the same list of strings, `initGame(List<String>)`.

4. Finally, we can test your next iteration logic!

### 1. Mapping a cell to a string

<details>
  <summary>Testing the mapping of a cell to a character</summary>

  ```java
  @Test
  void mapLivingCellToCharacter() {
    Optional<String> cellCharacter =
      Optional
      .of(livingCell(0, 0))
      .map(mapToCharacter());

    assertEquals("#", cellCharacter.get());
  }

  @Test
  void mapDeadCellToCharacter() {
    Optional<String> cellCharacter =
      Optional
      .of(deadCell(0, 0))
      .map(mapToCharacter());

    assertEquals("-", cellCharacter.get());
  }  
  ```

  The implementation that makes these tests pass is give below.
  
<details>
  <summary>Mapping a cell to a character depending on its state</summary>

  ```java	
  public static Function<Cell, String> mapToCharacter() {
		return cell -> cell.isAlive() ? "#" : "-";
	}
  ```
  
</details>
</details>

### 2. Mapping the list of cells to a list of strings

The next challenge is that we are stuck with a list of cells,
which is one-dimensional by defition. We somehow need to convert
that into a two-dimensional representation.

We'll do so by first creating a map where the keys are the values
of the x-coordinates (i.e. the rows), and the values a list of
cells that have been mapped to their character representation that
we implemented in step 1.

<details>
  <summary>Creating a hash map with rows as key and a list of cells mapped to chars</summary>

  ```java
  Map<Integer, List<String>> rowMap = 
  board
  .stream()
  .collect(groupBy(Cell::getX, mapToCharacter()));
  ```
</details>

Next, we sort the entries of the hashmap by key value (i.e. the
x-coordinate), so that the game rows are listed in order.
Finally, we convert the list of chars to strings.

<details>
  <summary>Finalizing the board representation</summary>

  ```java
  public static List<String> boardRepresentation(final List<Cell> board) {
    return board
      .stream()
      .collect(groupBy(Cell::getX, mapToCharacter()))
      .entrySet()
      .stream()
      .sorted(byYCoordinate())
      .map(toSingleLine())
      .map(createTextLine())
      //.peek(System.out::println)
			.collect(Collectors.toList());
  }  
  ```
</details>

Note that the line containing the `peek()` statement 
may be activated to inspect the output at run-time!

### 3. Initializing a board

Finally, let's address the initialization of a game board.

<details>
  <summary>Specification for the initialization of a new board</summary>

  ```java
  class GameTest {
    private static final List<String> BLINKER_START_POSITION = List.of(
        "-----",
        "--#--", 
        "--#--", 
        "--#--",
        "-----");
  
    // ...
  
    @Test
    void createWorldWithBlinkerOscillator() {
      List<Cell> gameboard = initGame(BLINKER_START_POSITION);
      assertEquals(BLINKER_START_POSITION, boardRepresentation(gameboard));
    }
  ```

<details>
    <summary>The implementation of the <code>initGame(List&lt;String&gt;)</code> method</summary>

  ```java
    public static List<Cell> initGame(final List<String> initialState) {
  		List<Cell> game = new LinkedList<Cell>();
  		for (int x = 0; x < initialState.size(); x++) 
  			for (int y = 0; y < initialState.get(x).length(); y++) 
          game.add( initialState.get(x).charAt(y) == '#' ? livingCell(x, y) : deadCell(x,y));
  
  		return game;
    }
  ```

</details>

</details>

### 4. The iteration logic

<details>
  <summary>Specification for the initialization of a new board</summary>

  ```java
  class GameTest {
    
    // ...
    
    private static final List<String> BLINKER_END_POSITION = List.of(
        "-----",
        "--#--", 
        "--#--", 
        "--#--",
        "-----");
  
    // ...
  
    @Test
    void iterateWorldWithBlinkerOscillator() {
      List<Cell> gameboard = initGame(BLINKER_START_POSITION);
      gameboard = iterateGameboard(gameboard);
      assertEquals(BLINKER_END_POSITION, boardRepresentation(gameboard));
    }
  ```

<details>
    <summary>Finally testing the iteration logic from the teaser!</summary>

  ```java
	public static List<Cell> iterateGameboard(final List<Cell> gameboard) {
		return gameboard
				.stream()
	    		.map(toDeadCell(which(isLiving, and(), 
		    			which(hasLessThanTwo(livingNeighboursIn(gameboard)), or(), hasMoreThanThree(livingNeighboursIn(gameboard))))))
	    		.map(toLivingCell(which(isDead, and(), hasExactlyThree(livingNeighboursIn(gameboard)))))
	    		.collect(Collectors.toList());
	}
  ```

</details>

</details>
