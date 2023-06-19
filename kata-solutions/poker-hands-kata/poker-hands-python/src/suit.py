from enum import Enum

class Suit(Enum):
  DIAMOND = "♦"
  CLUB = "♣"
  HEART = "♥"
  SPADE = "♠"

  @staticmethod
  def from_string(suit):
    if suit in ("SPADE", "S"):
      return Suit.SPADE
    elif suit in ("HEART", "H"):
      return Suit.HEART
    elif suit in ("CLUB", "C"):
      return Suit.CLUB
    elif suit in ("DIAMOND", "D"):
      return Suit.DIAMOND
    else:
      raise NotImplementedError