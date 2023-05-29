from mamba import description, it, context, before
from expects import expect, equal, raise_error, be_false, be_true
#from game_of_life import living_cell, dead_cell, Game
  
with description("Game of life") as self:
  with context("Living cell survival"):
    
    with it("dies on one living neighbour"):
      expect(True).to(be_false)
