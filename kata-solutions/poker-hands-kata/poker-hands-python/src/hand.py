from src.poker_ranks import PokerRanks
from src.card import Card

class Hand:
  def __init__(self, cards_string: str) -> None:
    if len(cards_string.split()) != 5:
      raise ValueError("Invalid number of cards")
    self.cards = [Card(c) for c in cards_string.split()]

  def straight(self):
    ranked_cards = self.rank_cards()
    return (ranked_cards[0] - ranked_cards[4]) == 4 and len(set(ranked_cards)) == 5

  def flush(self):
    suits = [card.get_suit() for card in self.cards]
    return len(set(suits)) == 1

  def of_a_kind(self, kind_type: int, cards = None):
    ranked_cards = self.rank_cards() if cards == None else cards

    for card in ranked_cards:
      if ranked_cards.count(card) == kind_type:
        return card
    return False

  # Ranks cards in descending order
  def rank_cards(self):
    card_list = [card.get_rank() for card in self.cards]
    card_list.sort(reverse = True)
    return card_list if card_list != [14, 5, 4, 3, 2] else [5, 4, 3, 2, 1]
 
  def two_pair(self):
    ranked_cards = self.rank_cards()
    high_pair = self.of_a_kind(2)
    low_pair = self.of_a_kind(2, list(reversed(ranked_cards)))
    
    # Return false if the two pairs happen to be the same!
    return (high_pair, low_pair) if high_pair and low_pair != high_pair else False
    

  def rank_hand(self):
    if self.straight() and self.flush():
      return (PokerRanks.STRAIGHT_FLUSH, max(self.rank_cards()))
    elif self.of_a_kind(4):
      return (PokerRanks.FOUR_OF_A_KIND, self.of_a_kind(4), self.of_a_kind(1))
    elif self.of_a_kind(3) and self.of_a_kind(2):
      return (PokerRanks.FULL_HOUSE, self.of_a_kind(3), self.of_a_kind(2))
    elif self.flush():
      return (PokerRanks.FLUSH, self.rank_cards())
    elif self.straight():
      return (PokerRanks.STRAIGHT, max(self.rank_cards()))
    elif self.of_a_kind(3):
      return (PokerRanks.THREE_OF_A_KIND, self.of_a_kind(3), self.rank_cards())
    elif self.two_pair():
      return (PokerRanks.TWO_PAIR, self.two_pair(), self.rank_cards())
    elif self.of_a_kind(2):
      return (PokerRanks.TWO_OF_A_KIND, self.rank_cards())
    else:
      return (PokerRanks.ONE_OF_A_KIND, self.rank_cards())

