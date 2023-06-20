from mamba import description, context, it, before
from expects import expect, equal, have_len, raise_error, be_true, be_false
from hand import Hand
from card import Card
from poker_ranks import PokerRanks
from mockito import when

with description(Hand):
  with it("throws an exception when less than five cards are created"):
    expect(lambda: Hand("6C")).to(raise_error(ValueError, "Invalid number of cards"))
  with it("has 5 cards"):
    expect(Hand("6C 7C 8C 9C TC").cards).to(have_len(5))

  with context('with ace low straight'):
    with it('ranks the hand accordingly'):
      ace_low_straight = Hand("AC 2D 4H 3D 5S")
      expect(ace_low_straight.rank_hand()).to(equal(
       (PokerRanks.STRAIGHT, 5)
      ))

  with description("Ranking cards") as self:
    with it("ranks a straight flush"):
      when(Card).get_rank().thenReturn(6, 7, 8, 9, 10)
      straight_flush = Hand("6C 7C 8C 9C TC")
      expect(straight_flush.rank_cards()).to(equal([10, 9, 8, 7, 6]))
    with it("ranks a full house"):
      when(Card).get_rank().thenReturn(7, 10, 10, 10, 7)
      full_house = Hand("TD TC TH 7C 7D")
      expect(full_house.rank_cards()).to(equal([10, 10, 10, 7, 7]))

  with context("with no score"): 
    with before.each:
      self.no_score = Hand("2D 4C 6H 8D TD")
    with it('identifies one of a kind'):
      when(Card).get_rank().thenReturn(10, 8, 6, 4, 2)
      expect(self.no_score.of_a_kind(1)).to(equal(10))
    with it('does not identify four of a kind'):
      expect(self.no_score.of_a_kind(4)).to(be_false)
    with it('does not identify a flush'):
      when(Card).get_suit().thenReturn("D", "C", "H", "D", "D")
      expect(self.no_score.flush()).to(be_false)
    with it('does not identify a straight'):
      expect(self.no_score.straight()).to(be_false)
    with it("ranks with ranked cards"):
      when(self.no_score).rank_cards().thenReturn([10, 8, 6, 4, 2])
      when(self.no_score).flush().thenReturn(False)
      when(self.no_score).straight().thenReturn(False)
      when(self.no_score).of_a_kind(4).thenReturn(False)
      when(self.no_score).of_a_kind(3).thenReturn(False)
      when(self.no_score).of_a_kind(2).thenReturn(False)
      when(self.no_score).two_pair().thenReturn(False)
      expect(self.no_score.rank_hand()).to(equal(
        (PokerRanks.ONE_OF_A_KIND, [10, 8, 6, 4, 2])
      ))

  with context("with a flush"):
    with before.each:
      self.flush_10 = Hand("TD 8D 6D 5D 2D")

    with it('identifies the flush'):
      when(Card).get_suit().thenReturn("D")
      expect(self.flush_10.flush()).to(be_true)
    with it('ranks as flush with ranked cards'):
      when(self.flush_10).flush().thenReturn(True)
      when(self.flush_10).rank_cards().thenReturn([10, 8, 6, 4, 2])
      expect(self.flush_10.rank_hand()).to(equal(
        (PokerRanks.FLUSH, [10, 8, 6, 4, 2])
      ))

  with context('with straight flush'):
    with before.each:
      self.straight_flush = Hand("6C 7C 8C 9C TC")
    with it('ranks as straight flush 10'):
      when(self.straight_flush).straight().thenReturn(True)
      when(self.straight_flush).flush().thenReturn(True)
      when(self.straight_flush).rank_cards().thenReturn([10, 9, 8, 7, 6])
      expect(self.straight_flush.rank_hand()).to(equal(
        (PokerRanks.STRAIGHT_FLUSH, 10)
      ))

  with context('with straight'):
    with before.each:
      self.straight = Hand("6C 7D 8S 9C TC")
    with it('identifies the straight'):
      when(Card).get_rank().thenReturn(6, 7, 8, 9, 10)
      expect(self.straight.straight()).to(be_true)
    with it('ranks as straight 9'):
      when(self.straight).flush().thenReturn(0)
      when(self.straight).straight().thenReturn(9)
      when(self.straight).rank_cards().thenReturn([9, 8, 7, 6, 5])
      expect(self.straight.rank_hand()).to(equal(
        (PokerRanks.STRAIGHT, 9)
      ))

  with context('with four of a kind'):
    with before.each:
      self.four_of_a_kind = Hand("9D 9H 9S 9C 7D")
    with it('ranks as four of a kind, high 9'):
      when(self.four_of_a_kind).of_a_kind(1).thenReturn(11)
      when(self.four_of_a_kind).of_a_kind(4).thenReturn(9)
      expect(self.four_of_a_kind.rank_hand()).to(equal(
        (PokerRanks.FOUR_OF_A_KIND, 9, 11)
      ))

  with context('with full house'):
    with before.each:
      self.full_house = Hand("TD TC TH 7C 7D")
    with it('ranks as full house'):
      when(self.full_house).of_a_kind(2).thenReturn(7)
      when(self.full_house).of_a_kind(3).thenReturn(10)
      when(self.full_house).of_a_kind(4).thenReturn(0)
      expect(self.full_house.rank_hand()).to(equal(
        (PokerRanks.FULL_HOUSE, 10, 7)
      ))

  with context('with three of a kind'):
    with before.each:
      self.three_of_a_kind = Hand("TD 8C 8H 8S 2D")
    with it('does not identify two of a kind'):
      expect(self.three_of_a_kind.of_a_kind(2)).to(be_false)
    with it('identifies three of a kind'):
      when(Card).get_rank().thenReturn(10, 8, 8, 8, 2)
      expect(self.three_of_a_kind.of_a_kind(3)).to(equal(8))
    with it('ranks as three of a kind with ranked cards'):
      when(self.three_of_a_kind).flush().thenReturn(False)
      when(self.three_of_a_kind).straight().thenReturn(False)
      when(self.three_of_a_kind).of_a_kind(4).thenReturn(0)
      when(self.three_of_a_kind).of_a_kind(3).thenReturn(8)
      when(self.three_of_a_kind).of_a_kind(2).thenReturn(0)
      when(self.three_of_a_kind).rank_cards().thenReturn([10, 8, 8, 8, 2])
      expect(self.three_of_a_kind.rank_hand()).to(equal(
        (PokerRanks.THREE_OF_A_KIND, 8, [10, 8, 8, 8, 2])
      ))

  with context('with two pairs'):
    with before.each:
      self.two_pairs = Hand("TD 8C 8H 4S 4S")
      when(self.two_pairs).rank_cards().thenReturn([10, 8, 8, 4, 4])
    with it('identifies two pairs'):
      expect(self.two_pairs.two_pair()).to(equal((8, 4)))
    with it('ranks as two pairs with ranked cards'):
      when(self.two_pairs).flush().thenReturn(False)
      when(self.two_pairs).straight().thenReturn(False)
      when(self.two_pairs).of_a_kind(4).thenReturn(0)
      when(self.two_pairs).of_a_kind(3).thenReturn(0)
      when(self.two_pairs).two_pair().thenReturn((8,4))
      expect(self.two_pairs.rank_hand()).to(equal(
        (PokerRanks.TWO_PAIR, (8, 4), [10, 8, 8, 4, 4])
      ))

  with context('with two of a kind'):
    with before.each:
      self.two_of_a_kind = Hand("TD 8C 8H 7S 6D")
      when(self.two_of_a_kind).rank_cards().thenReturn([10, 8, 8, 7, 6])
    with it('does not identify two pairs'):
      expect(self.two_of_a_kind.two_pair()).to(be_false)
    with it('does not identify four of a kind'):
      expect(self.two_of_a_kind.of_a_kind(4)).to(be_false)
    with it('does not identify three of a kind'):
      expect(self.two_of_a_kind.of_a_kind(3)).to(be_false)
    with it('identifies two of a kind'):
      expect(self.two_of_a_kind.of_a_kind(2)).to(equal(8))
    with it('ranks as two of a kind with ranked cards'):
      when(self.two_of_a_kind).flush().thenReturn(False)
      when(self.two_of_a_kind).straight().thenReturn(False)
      when(self.two_of_a_kind).of_a_kind(4).thenReturn(0)
      when(self.two_of_a_kind).of_a_kind(3).thenReturn(0)
      when(self.two_of_a_kind).two_pair().thenReturn(False)
      when(self.two_of_a_kind).of_a_kind(2).thenReturn(8)
      expect(self.two_of_a_kind.rank_hand()).to(equal(
        (PokerRanks.TWO_OF_A_KIND, [10, 8, 8, 7, 6])
      ))








      
