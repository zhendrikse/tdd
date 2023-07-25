package gameoflife;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;

import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

import java.util.function.Function;

import gameoflife.Cell;
import static gameoflife.Cell.*;
import static gameoflife.Game.*;

class GameTest {
  private static final List<String> BLINKER_START_POSITION = List.of(
      "-----",
      "--#--", 
      "--#--", 
      "--#--",
      "-----");

  private static final List<String> BLINKER_END_POSITION = List.of(
      "-----",
      "-----", 
      "-###-", 
      "-----",
      "-----");

  private List<Cell> game;

  @BeforeEach
  void setUpNewGame() {
    game = List.of(
      deadCell(0, 0), livingCell(0, 1), livingCell(0, 2),
      livingCell(1, 0), livingCell(1, 1), deadCell(1, 2),
      deadCell(2, 0), livingCell(2, 1), deadCell(2, 2)
    );    
  }
  
  @Test
  void assertNumberOfLivingNeighboursInAGameForAGivenCell() {
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

  @Test
  void assertExactlyThreeLivingNeighboursForAGivenCellInAGame() {
    assertEquals(4, 
      game.stream()
      .filter(hasExactlyThree(livingNeighboursIn(game)))
      .collect(Collectors.toList())
      .size()
    );
  }

  @Test
  void assertMoreThanThreeLivingNeighboursForAGivenCellInAGame() {
    assertEquals(2, 
      game.stream()
      .filter(hasMoreThanThree(livingNeighboursIn(game)))
      .collect(Collectors.toList())
      .size()
    );
  }

  @Test
  void assertLessThanTwoLivingNeighboursForAGivenCellInAGame() {
    assertEquals(0, 
      game.stream()
      .filter(hasLessThanTwo(livingNeighboursIn(game)))
      .collect(Collectors.toList())
      .size()
    );
  }

  private List<String> boardRepresentation(List<Cell> board) {
    Map<Integer, List<String>> rowMap = 
      board
      .stream()
      .collect(groupBy(Cell::getX, mapToCharacter()));

    return rowMap
      .entrySet()
      .stream()
      .sorted(byYCoordinate())
      .map(toSingleLine())
      .map(createTextLine())
      //.peek(System.out::println)
			.collect(Collectors.toList());
  }

  @Test
  void createWorldWithBlinkerOscillator() {
    List<Cell> gameboard = initGame(BLINKER_START_POSITION);
    assertEquals(BLINKER_START_POSITION, boardRepresentation(gameboard));
  }

  @Test
  void iterateWorldWithBlinkerOscillator() {
    List<Cell> gameboard = initGame(BLINKER_START_POSITION);
    gameboard = iterateGameboard(gameboard);
    assertEquals(BLINKER_END_POSITION, boardRepresentation(gameboard));
  }
}