from enum import Enum

class PokerRanks(Enum):
    STRAIGHT_FLUSH = 8
    FOUR_OF_A_KIND = 7
    FULL_HOUSE = 6
    FLUSH = 5
    STRAIGHT = 4
    THREE_OF_A_KIND = 3
    TWO_PAIR = 2
    TWO_OF_A_KIND = 1
    ONE_OF_A_KIND = 0