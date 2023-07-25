package gameoflife;

import java.util.List;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.stream.Collectors;

import static gameoflife.Cell.*;

public class Game {
  public static Function<Cell, List<Cell>> livingNeighboursIn(final List<Cell> game) {
    return cell -> game
      .stream()
			.filter(isNeighbourOf(cell))
      .filter(isLiving)
			.collect(Collectors.toList());      
  }  

	public static Predicate<Cell> hasExactlyThree(Function<Cell, List<Cell>> findNeighbours) {
		return cell -> findNeighbours.apply(cell).size() == 3;
	}

  public static Predicate<Cell> hasMoreThanThree(Function<Cell, List<Cell>> findNeighbours) {
		return cell -> findNeighbours.apply(cell).size() > 3;
	}

	public static Predicate<Cell> hasLessThanTwo(Function<Cell, List<Cell>> findNeighbours) {
		return cell -> findNeighbours.apply(cell).size() < 2;
	}
}
