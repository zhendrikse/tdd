from mamba import description, it, context, before
from expects import expect, be
from gilded_rose import GildedRose, Item

with description("Generic item") as self:
    with context("When past sell date"):
        with before.each:
            self.item = Item("Foo", -1, 20)
            GildedRose([self.item]).update_quality()

        with it("decrements the sell-in date"):
            expect(self.item.sell_in).to(be(-2))

        with it("decrements quality by 1"):
            expect(self.item.quality.value).to(be(19))

    with context("When within sell date"):
        with before.each:
            self.item = Item("Foo", 2, 20)
            GildedRose([self.item]).update_quality()

        with it("decrements the sell-in date"):
            expect(self.item.sell_in).to(be(1))

        with it("decrements quality by 1"):
            expect(self.item.quality.value).to(be(19))

    with context("When quality is zero"):
        with before.each:
            self.item = Item("Foo", 1, 0)
            GildedRose([self.item]).update_quality()

        with it("decrements the sell-in date"):
            expect(self.item.sell_in).to(be(0))

        with it("keeps the quality at zero"):
            expect(self.item.quality.value).to(be(0))
