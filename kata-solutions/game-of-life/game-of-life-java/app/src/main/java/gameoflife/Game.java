package gameoflife;

import java.util.Comparator;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.LinkedList;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.stream.Collector;
import java.util.stream.Collectors;

import static gameoflife.Cell.*;
import static gameoflife.FunctionalExtensions.*;

public class Game {
  public static Function<Cell, List<Cell>> livingNeighboursIn(final List<Cell> game) {
    return cell -> game
      .stream()
			.filter(isNeighbourOf(cell))
      .filter(isLiving)
			.collect(Collectors.toList());      
  }  

  public static List<Cell> initGame(final List<String> initialState) {
		List<Cell> game = new LinkedList<Cell>();
		for (int x = 0; x < initialState.size(); x++) {
			for (int y = 0; y < initialState.get(x).length(); y++) {
        if (initialState.get(x).charAt(y) == '#') 
  				game.add(livingCell(x, y));
        else
          game.add(deadCell(x, y));
			}
		}

		return game;
  }
  
	public static List<Cell> iterateGameboard(final List<Cell> gameboard) {
		return gameboard
				.stream()
	    		.map(toDeadCell(which(isLiving, and(), 
		    			which(hasLessThanTwo(livingNeighboursIn(gameboard)), or(), hasMoreThanThree(livingNeighboursIn(gameboard))))))
	    		.map(toLivingCell(which(isDead, and(), hasExactlyThree(livingNeighboursIn(gameboard)))))
	    		.collect(Collectors.toList());
	}
  
  public static Function<Entry<Integer, List<String>>, List<String>> toSingleLine() {
		return (entry) -> entry.getValue();
	}

	public static Function<List<String>, String> createTextLine() {
		return (list) -> list.stream().collect(Collectors.joining(""));
	}

	public static Comparator<Entry<Integer, List<String>>> byYCoordinate() {
		return (entry1, entry2) -> Integer.compare(entry1.getKey(), entry2.getKey());
	}

	public static Collector<Cell, ?, Map<Integer, List<String>>> groupBy(Function<Cell, Integer> supplier,
			Function<Cell, String> mapper) {
		return Collectors.groupingBy(supplier, Collectors.mapping(mapper, Collectors.toList()));
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
