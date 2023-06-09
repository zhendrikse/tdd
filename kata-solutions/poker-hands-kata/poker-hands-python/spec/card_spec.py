from mamba import description, context, it, fit, before
from expects import expect, equal
from card import Card
from suit import Suit

with description(Card) as self:
  with context("with club ten"):
    with before.each:
      self.card = Card("TC")
    with it("extracts the suit"):
      expect(self.card.get_suit()).to(equal(Suit.CLUB))
    with it("extracts the rank"):
      expect(self.card.get_rank()).to(equal(10))
  with context("with heart 2"):
    with before.each:
      self.card = Card("2H")
    with it("extracts the suit"):
      expect(self.card.get_suit()).to(equal(Suit.HEART))
    with it("extracts the rank"):
      expect(self.card.get_rank()).to(equal(2))
