from mamba import description, it, context, before
from expects import expect, be
from gilded_rose import GildedRose, BackstagePassesTafka

with description("Backstage pass item") as self:
    with context("When past sell date"):
        with before.each:
            self.item = BackstagePassesTafka(-1, 20)
            GildedRose([self.item]).update_quality()

        with it("decrements the sell-in date"):
            expect(self.item.sell_in).to(be(-2))

        with it("becomes worthless (quality zero)"):
            expect(self.item.quality.value).to(be(0))

    with context("When 20 days within sell date"):
        with before.each:
            self.item = BackstagePassesTafka(20, 10)
            GildedRose([self.item]).update_quality()

        with it("decrements the sell-in date"):
            expect(self.item.sell_in).to(be(19))

        with it("increases in quality one step"):
            expect(self.item.quality.value).to(be(11))

    with context("When 10 days within sell date"):
        with before.each:
            self.item = BackstagePassesTafka(10, 10)
            GildedRose([self.item]).update_quality()

        with it("decrements the sell-in date"):
            expect(self.item.sell_in).to(be(9))

        with it("increases in quality two steps"):
            expect(self.item.quality.value).to(be(12))

    with context("When 5 days within sell date"):
        with before.each:
            self.item = BackstagePassesTafka(5, 10)
            GildedRose([self.item]).update_quality()

        with it("decrements the sell-in date"):
            expect(self.item.sell_in).to(be(4))

        with it("increases in quality three steps"):
            expect(self.item.quality.value).to(be(13))

