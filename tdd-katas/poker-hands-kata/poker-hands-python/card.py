class Card:
  def __init__(self, card: str):
    self.card = card

  def get_rank(self):
    return "--23456789TJQKA".index(self.card[0])
        
  def get_suit(self) -> str:
    return self.card[1]
