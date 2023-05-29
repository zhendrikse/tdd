from illegal_args_exception import IllegalArgumentsException

def rank_hand(hand):
  return hand.rank().value
  
def determine_best_hand(hands):
  if len(hands) == 0:
    raise IllegalArgumentsException()
  elif len(hands) == 1:
    return hands[0]
  
  return max(hands, key = rank_hand)

  