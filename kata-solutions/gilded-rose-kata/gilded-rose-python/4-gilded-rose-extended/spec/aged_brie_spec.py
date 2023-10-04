from mamba import description, it, context, before
from expects import expect, be
from gilded_rose import GildedRose, AgedBrie

with description("Given aged brie items") as self:
    with context("When past sell date"):
        with before.each:
            self.item = AgedBrie(-1, 0)
            GildedRose([self.item]).update_quality()

        with it("decrements the sell-in date"):
            expect(self.item.sell_in).to(be(-2))

        with it("increases in quality twice as fast"):
            expect(self.item.quality.value).to(be(2))

    with context("When within sell date"):
        with before.each:
            self.item = AgedBrie(1, 0)
            GildedRose([self.item]).update_quality()

        with it("decrements the sell-in date"):
            expect(self.item.sell_in).to(be(0))

        with it("increases in quality one step"):
            expect(self.item.quality.value).to(be(1))

    with context("When quality is max"):
        with before.each:
            self.item = AgedBrie(1, 50)
            GildedRose([self.item]).update_quality()

        with it("decrements the sell-in date"):
            expect(self.item.sell_in).to(be(0))

        with it("keeps quality at max"):
            expect(self.item.quality.value).to(be(50))
