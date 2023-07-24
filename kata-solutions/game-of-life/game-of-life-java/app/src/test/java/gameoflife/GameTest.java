package gameoflife;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import java.util.List;

import static gameoflife.Cell.*;
import static gameoflife.Game.*;

class GameTest {
  @Test
  void neighboursForFunction() {
    List<Cell> game = List.of(
      livingCell(0, 0),
      livingCell(0, 1),
      livingCell(0, 2),
      livingCell(1, 0),
      livingCell(1, 1),
      livingCell(1, 2),
      livingCell(2, 0),
      livingCell(2, 1),
      livingCell(2, 2)
    );

    //assertEquals(livingNeighBoursIn(game).apply(game.get(4)).size(), 8);
  } 
}