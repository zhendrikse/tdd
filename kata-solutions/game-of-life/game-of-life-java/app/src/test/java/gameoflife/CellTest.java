package gameoflife;

import static gameoflife.Cell.deadCell;
import static gameoflife.Cell.isDead;
import static gameoflife.Cell.isLiving;
import static gameoflife.Cell.isNeighbourOf;
import static gameoflife.Cell.livingCell;
import static gameoflife.Cell.mapToCharacter;
import static gameoflife.Cell.toDeadCell;
import static java.util.stream.Collectors.toList;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.List;
import java.util.Optional;
import java.util.function.Predicate;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class CellTest {
  private boolean isDead(final Cell cell) {
    return !Optional.of(cell).filter(isDead).isEmpty();
  }

  private boolean isLiving(final Cell cell) {
    return !Optional.of(cell).filter(isLiving).isEmpty();
  }

  @Test 
  void isLivingPredicate() {
    assertTrue(isLiving(livingCell(0, 0)));
    assertFalse(isLiving(deadCell(0, 0)));
  }

  @Test
  void isDeadPredicate() {
    assertFalse(isDead(livingCell(0, 0)));
    assertTrue(isDead(deadCell(0, 0)));
  }

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

  @Test
  void toLivingCellMapping() {
    Predicate<Cell> ifCellViable = isDead;
    Optional<Cell> mappedList = 
      Optional
      .of(deadCell(0, 0))
      .map(toDeadCell(ifCellViable));
    
    assertFalse(mappedList.isEmpty());
    assertTrue(isDead(mappedList.get()));
  }

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
}

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
    assertEquals(8,
      game.stream()
      .filter(isNeighbourOf(game.get(4)))
      .collect(toList())
      .size());
  }

  @Test
  void filterNeighboursForGivenLeftEdgeCell() {
    assertEquals(5,
      game.stream()
      .filter(isNeighbourOf(game.get(3)))
      .collect(toList())
      .size());
  }

  @Test
  void filterNeighboursForGivenRightEdgeCell() {
    assertEquals(5, 
      game.stream()
      .filter(isNeighbourOf(game.get(5)))
      .collect(toList())
      .size());
  }

  @Test
  void filterNeighboursForGivenTopEdgeCell() {
    assertEquals(5,
      game.stream()
      .filter(isNeighbourOf(game.get(1)))
      .collect(toList())
      .size());
  }
}
