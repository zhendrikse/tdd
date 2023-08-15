from mamba import description, it, context, before
from expects import expect, equal, raise_error, be_false, be_true
from game_of_life import living_cell, dead_cell, Game
  
with description("Game of life") as self:
  with context("Living cell survival"):
    with before.each:
      self._cell = living_cell()
    
    with it("dies on one living neighbour"):
      expect(self._cell.next_generation([living_cell()]).is_alive()).to(be_false)

    with it("survives on two living neighbours"):
      expect(self._cell.next_generation([living_cell(), living_cell()])
             .is_alive()).to(be_true)

    with it("dies on one living and one dead neighbour"):
      expect(self._cell.next_generation([living_cell(), dead_cell()])
             .is_alive()).to(be_false)

    with it("survives on three living neighbours"):
      expect(self._cell.next_generation([living_cell(), living_cell(), living_cell()])
             .is_alive()).to(be_true)

    with it("dies on four living neighbours"):
      expect(self._cell.next_generation([living_cell(), living_cell(), living_cell(), living_cell()])
             .is_alive()).to(be_false)
      
  with context("Dead cell resurrection"):
    with before.each:
      self._cell = dead_cell()
    
    with it("remains dead with two living neighbours"):
      expect(self._cell.next_generation([living_cell(), living_cell()])
             .is_alive()).to(be_false)
    
    with it("resurrects with three living neighbours"):
      expect(self._cell.next_generation([living_cell(), living_cell(), living_cell()])
             .is_alive()).to(be_true)
      
    with it("remains dead on one dead on two living neighbours"):
      expect(dead_cell().next_generation([dead_cell(), living_cell(), living_cell()]).is_alive()).to(be_false)

with context("Neighbours in game"):
  with before.each:
    self._game = Game([
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
    ])
    
  with it("has eight neighbours for non-edge cells"):
    expect(self._game.neighbours_for(1, 1)).to(equal([1, 2, 3, 4, 6, 7, 8, 9]))
    
  with it("has five neighbours for left-edge cells"):
    expect(self._game.neighbours_for(1, 0)).to(equal([1, 2, 5, 7, 8]))
    
  with it("has five neighbours for right-edge cells"):
    expect(self._game.neighbours_for(1, 2)).to(equal([2, 3, 5, 8, 9]))
    
  with it("has five neighbours for top-edge cells"):
    expect(self._game.neighbours_for(0, 1)).to(equal([1, 3, 4, 5, 6]))
    
  with it("has five neighbours for bottom-edge cells"):
    expect(self._game.neighbours_for(2, 1)).to(equal([4, 5, 6, 7, 9]))

    
  with it("creates a new game with a next generation for all fields in a row"):
    game = Game([[living_cell(), living_cell(), living_cell()]])
    game = game.next_generation()
    expect(game.cell_at(0, 0)).to(equal(dead_cell()))
    expect(game.cell_at(0, 1)).to(equal(living_cell()))
    expect(game.cell_at(0, 2)).to(equal(dead_cell()))
    
  with it("creates a new game with a next generation for all fields in a column"):
    game = Game([
      [living_cell()], 
      [living_cell()], 
      [living_cell()]])
    game = game.next_generation()
    expect(game.cell_at(0, 0)).to(equal(dead_cell()))
    expect(game.cell_at(1, 0)).to(equal(living_cell()))
    expect(game.cell_at(2, 0)).to(equal(dead_cell()))    