from suit import Suit

class Card:
  def __init__(self, card):
    self._suit = Suit.from_string(card[1])
    self._rank = "--23456789TJQKA".index(card[0])

  def get_rank(self) -> int:
    return self._rank
        
  def get_suit(self) -> Suit:
    return self._suit

  def __repr__(self) -> str:
    return f"{self.rank}{self.suit}"