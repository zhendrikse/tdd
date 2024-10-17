import unittest
from gilded_rose import GildedRose, Item

class BackstagePassTest(unittest.TestCase):
    def test_when_past_the_sell_date(self):
        item = Item("Foo", -1, 20)
        GildedRose([item]).update_quality()
        assert str(item) == "Foo, -2, 19"
        
    def test_when_within_the_sell_date(self):
        item = Item("Foo", 2, 20)
        GildedRose([item]).update_quality()
        assert str(item) == "Foo, 1, 19"
        
    def test_when_quality_is_zero(self):
        item = Item("Foo", 1, 0)
        GildedRose([item]).update_quality()
        assert str(item) == "Foo, 0, 0"
        