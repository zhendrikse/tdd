from hand import Hand
from poker_hands import determine_best_hand
from mamba import description, context, it, before 
from expects import expect, equal, raise_error
from illegal_args_exception import IllegalArgumentsException
from mockito import when
from poker_ranks import PokerRanks

import poker_hands

with description("Ranking hands") as self:
  with description('Given an empty set of hands'):
    with it('raises an exception'):
      expect(lambda: determine_best_hand([])) \
        .to(raise_error(IllegalArgumentsException))

  with context("Given a straight flush hand"):
    with before.each:
      self.straight_flush = Hand("6C 7C 8C 9C TC")
      when(poker_hands).rank_hand(self.straight_flush).thenReturn(PokerRanks.STRAIGHT_FLUSH.value)

    with it('returns the one and only hand as winner'):
      hands = [self.straight_flush]
      expect(determine_best_hand(hands)).to(equal(self.straight_flush))

    with context("and a full house hand"):
      with before.each:
        self.full_house = Hand("TD TC TH 7C 7D")
        when(poker_hands).rank_hand(self.full_house).thenReturn(PokerRanks.FULL_HOUSE.value)

      with it('returns the straight flush hand'):
        hands = [self.full_house, self.straight_flush]
        expect(determine_best_hand(hands)).to(equal(self.straight_flush))
      with it('returns the straight flush hand (order reversed'):
        hands = [self.straight_flush, self.full_house]
        expect(determine_best_hand(hands)).to(equal(self.straight_flush))
