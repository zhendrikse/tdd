package gameoflife;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;

import java.util.List;
// import java.util.function.BiPredicate;
import java.util.function.Predicate;
import java.util.Optional;
import java.util.stream.Collectors;

import gameoflife.Cell;
import static gameoflife.Cell.*;

class CellTest {
  private List<Cell> game;

  @BeforeEach
  private void setUpGame() {
    game = List.of(
      livingCell(0, 0), livingCell(0, 1), livingCell(0, 2),
      livingCell(1, 0), livingCell(1, 1), livingCell(1, 2),
      livingCell(2, 0), livingCell(2, 1), livingCell(2, 2)
    );    
  }

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
    List<Cell> mappedList = 
      List
      .of(livingCell(0, 0))
      .stream()
      .map(toDeadCell(ifCellKillable))
      .collect(Collectors.toList());
    
    assertFalse(mappedList.isEmpty());
    assertTrue(isDead(mappedList.get(0)));
  }

  @Test
  void toLivingCellMapping() {
    Predicate<Cell> ifCellViable = isDead;
    List<Cell> mappedList = 
      List
      .of(deadCell(0, 0))
      .stream()
      .map(toDeadCell(ifCellViable))
      .collect(Collectors.toList());
    
    assertFalse(mappedList.isEmpty());
    assertTrue(isDead(mappedList.get(0)));
  }

  @Test
  void filterNeighboursForGivenCenterCell() {
    assertEquals(
      game.stream()
      .filter(isNeighbourOf(game.get(4)))
      .collect(Collectors.toList())
      .size(), 8);
  }

  @Test
  void filterNeighboursForGivenLeftEdgeCell() {
    assertEquals(
      game.stream()
      .filter(isNeighbourOf(game.get(3)))
      .collect(Collectors.toList())
      .size(), 5);
  }

  @Test
  void filterNeighboursForGivenRightEdgeCell() {
    assertEquals(
      game.stream()
      .filter(isNeighbourOf(game.get(5)))
      .collect(Collectors.toList())
      .size(), 5);
  }

  @Test
  void filterNeighboursForGivenTopEdgeCell() {
    assertEquals(
      game.stream()
      .filter(isNeighbourOf(game.get(1)))
      .collect(Collectors.toList())
      .size(), 5);
  }
}
