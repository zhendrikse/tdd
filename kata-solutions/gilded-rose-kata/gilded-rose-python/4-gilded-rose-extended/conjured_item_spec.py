from mamba import description, it, context, before
from expects import expect, be
from gilded_rose import GildedRose, ConjuredItem

with description("Given conjured items") as self:
    with context("When past sell date"):
        with before.each:
            self.item = ConjuredItem(10, 10)
            GildedRose([self.item]).update_quality()

        with it("decrements the sell-in date"):
            expect(self.item.sell_in).to(be(9))

        with it("decreases in quality twice as fast"):
            expect(self.item.quality.value).to(be(8))

