import unittest
from gilded_rose import GildedRose, AgedBrie, ConjuredItem, BackstagePassesTafka

class BackstagePassTest(unittest.TestCase):
    def test_when_past_the_sell_date(self):
        item = BackstagePassesTafka(-1, 20)
        GildedRose([item]).update_quality()
        assert str(item) == "Backstage passes to a TAFKAL80ETC concert, -2, 0"

    def test_when_5_days_within_sellin_date(self):
        item = BackstagePassesTafka(5, 10)
        GildedRose([item]).update_quality()
        assert str(item) == "Backstage passes to a TAFKAL80ETC concert, 4, 13"

    def test_when_10_days_within_sellin_date(self):
        item = BackstagePassesTafka(10, 10)
        GildedRose([item]).update_quality()
        assert str(item) == "Backstage passes to a TAFKAL80ETC concert, 9, 12"

    def test_when_20_days_within_sellin_date(self):
        item = BackstagePassesTafka(20, 10)
        GildedRose([item]).update_quality()
        assert str(item) == "Backstage passes to a TAFKAL80ETC concert, 19, 11"

