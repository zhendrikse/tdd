from mamba import description, context, it, before
from expects import expect, equal
from card import Card

with description(Card) as self:
  with context("with club ten"):
    with before.each:
      self.card = Card("TC")
    with it("extracts the suit"):
      expect(self.card.get_suit()).to(equal("C"))
    with it("extracts the rank"):
      expect(self.card.get_rank()).to(equal(10))
  with context("with heart 2"):
    with before.each:
      self.card = Card("2H")
    with it("extracts the suit"):
      expect(self.card.get_suit()).to(equal("H"))
    with it("extracts the rank"):
      expect(self.card.get_rank()).to(equal(2))
