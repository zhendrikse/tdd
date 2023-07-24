import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import java.util.List;
// import java.util.function.BiPredicate;
import java.util.function.Predicate;
import java.util.Optional;
import java.util.stream.Collectors;

import gameoflife.Cell;
import static gameoflife.Cell.*;

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

  @Test
  void toDeadCellMapping() {
    Predicate<Cell> ifCellKillable = isLiving;
    List<Cell> mappedList = 
      List
      .of(newLivingCell())
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
      .of(newDeadCell())
      .stream()
      .map(toDeadCell(ifCellViable))
      .collect(Collectors.toList());
    
    assertFalse(mappedList.isEmpty());
    assertTrue(isDead(mappedList.get(0)));
  }
}
