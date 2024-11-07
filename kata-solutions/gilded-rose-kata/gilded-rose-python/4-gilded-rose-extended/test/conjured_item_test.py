import unittest
from gilded_rose import GildedRose, AgedBrie, ConjuredItem, BackstagePassesTafka

class BackstagePassTest(unittest.TestCase):
    def test_when_past_the_sell_date(self):
        item = ConjuredItem("Conjured foo", 10, 10)
        GildedRose([item]).update_quality()
        assert str(item) == "Conjured foo, 9, 8"
        
