package gameoflife;

import java.util.function.Predicate;
import java.util.Optional;
import java.util.function.Function;

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

  public int getY() {
    return y;
  }

  @Override
  public boolean equals(Object other) {
      if (other == null) 
          return false;

      if (this == other) 
          return true;

      if (!(other instanceof Cell)) 
          return false; 

      Cell otherCell = (Cell) other;
      return x == otherCell.x && y == otherCell.y && alive == otherCell.alive;
  }

  @Override
  public int hashCode() {
    final int PRIME = 31;

    return PRIME * x + PRIME * y + (alive ? 0 : PRIME);
  }
  
  public static final Cell livingCell(final int x, final int y) {
    return new Cell(x, y, true);
  }
  
  public static final Cell deadCell(final int x, final int y) {
    return new Cell(x, y, false);
  }

  public static Predicate<Cell> isLiving = Cell::isAlive;
  
  public static Predicate<Cell> isDead = isLiving.negate();

  public static Predicate<Cell> isNeighbourOf(final Cell givenCell) {
    return cell -> 
      !cell.equals(givenCell) &&
      (Math.abs(cell.x - givenCell.x) < 2) && 
      (Math.abs(cell.y - givenCell.y) < 2); 
  }
	
  public static Function<Cell, String> mapToCharacter() {
		return cell -> cell.isAlive() ? "#" : "-";
	}
  
  public static Function<Cell, Cell> toDeadCell(Predicate<Cell> isCellKillable) {
    return cell -> Optional
      .of(cell)
      .filter(isCellKillable.negate())
			.orElse(deadCell(cell.x, cell.y));  
  }

  public static Function<Cell, Cell> toLivingCell(Predicate<Cell> isCellViable) {
    return cell -> Optional
      .of(cell)
      .filter(isCellViable.negate())
			.orElse(livingCell(cell.x, cell.y));  
  }
}
