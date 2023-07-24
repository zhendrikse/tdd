package gameoflife;

import java.util.function.Predicate;
import java.util.Optional;
import java.util.function.Function;

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

  public static Predicate<Cell> isLiving = Cell::isAlive;
  
  public static Predicate<Cell> isDead = isLiving.negate();

  public static Function<Cell, Cell> toDeadCell(Predicate<Cell> isCellKillable) {
    return cell -> Optional
      .of(cell)
      .filter(isCellKillable.negate())
			.orElse(newDeadCell());  
  }

  public static Function<Cell, Cell> toLivingCell(Predicate<Cell> isCellViable) {
    return cell -> Optional
      .of(cell)
      .filter(isCellViable.negate())
			.orElse(newLivingCell());  
  }
}
