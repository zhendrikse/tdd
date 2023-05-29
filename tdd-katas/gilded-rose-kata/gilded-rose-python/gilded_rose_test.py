import unittest
from approvaltests.combination_approvals import verify_all_combinations
from gilded_rose import GildedRose, Item

class GildedRoseTest(unittest.TestCase):
    def test_add_combinatorial(self):
        names = [
            "foo"
        ]
        sellIns = [0]
        qualities = [0]
        verify_all_combinations(self.do_update_quality,
                                [names, sellIns, qualities])

    def do_update_quality(self, name: str, sellIn: int, quality: int) -> str:
        items = [Item(name, sellIn, quality)]
        app = GildedRose(items)
        app.update_quality()
        return app.items[0]


if __name__ == "__main__":
    unittest.main()
