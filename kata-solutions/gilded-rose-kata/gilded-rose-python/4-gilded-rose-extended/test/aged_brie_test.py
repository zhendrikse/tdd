import unittest
from gilded_rose import GildedRose, AgedBrie, ConjuredItem, BackstagePassesTafka

class AgedBrieTest(unittest.TestCase):
    def test_when_past_the_sell_date(self):
        item = AgedBrie(-1, 0)
        GildedRose([item]).update_quality()
        assert str(item) == "Aged Brie, -2, 2"

    def test_when_within_sell_date(self):
        item = AgedBrie(1, 0)
        GildedRose([item]).update_quality()
        assert str(item) == "Aged Brie, 0, 1"

    def test_when_quality_is_max(self):
        item = AgedBrie(1, 50)
        GildedRose([item]).update_quality()
        assert str(item) == "Aged Brie, 0, 50"
