import unittest
from approvaltests.combination_approvals import verify_all_combinations
from gilded_rose import GildedRose, Item


class GildedRoseTest(unittest.TestCase):
    def test_update_combinatoric(self):
        names = [
            "foo", "Aged Brie", "Sulfuras, Hand of Ragnaros",
            "Backstage passes to a TAFKAL80ETC concert"
        ]
        sellIns = [-1, 2, 6, 0, 11, 7]
        qualities = [0, 48, 49, 50, 47]
        verify_all_combinations(self.do_update_quality,
                                [names, sellIns, qualities])

    def do_update_quality(self, name: str, sellIn: int, quality: int) -> str:
        items = [Item(name, sellIn, quality)]
        app = GildedRose(items)
        app.update_quality()
        return app.items[0]


if __name__ == "__main__":
    unittest.main()
