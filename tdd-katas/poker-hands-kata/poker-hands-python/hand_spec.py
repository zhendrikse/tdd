from mamba import description, context, it, before
from expects import expect, equal, have_len, raise_error, be_true, be_false
from hand import Hand
from poker_ranks import PokerRanks
from mockito import when

with description(Hand):
  with it("asserts that true equals true"):
    expect(True).to(be_true)