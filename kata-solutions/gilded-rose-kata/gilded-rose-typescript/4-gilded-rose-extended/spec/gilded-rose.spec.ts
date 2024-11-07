'use strict';

import { Item, GildedRose, Sulfuras, BackstagePass, AgedBrie, ConjuredItem } from '../src/gilded-rose';

function verifyItem(item: Item, name: string, quality: number, sellIn: number) {
  expect(item.name).toEqual(name);
  expect(item.quality).toEqual(quality);
  expect(item.sellIn).toEqual(sellIn);
}

describe('Gilded Rose', () => {
  it('should add new item', () => {
    const item = new Item('foo', 0, 0);
    const gildedRose = new GildedRose([item]);
    verifyItem(item, 'foo', 0, 0);
  });
});

describe('basic quality rules', () => {
  it('should update quality for sellin 1 day', () => {
    const item = new Item('foo', 1, 1);
    const gildedRose = new GildedRose([item]);
    gildedRose.updateQuality();
    verifyItem(item, 'foo', 0, 0);
  });

  it('should update quality 2x as fast for sellin 0 days', () => {
    const item = new Item('foo', 0, 4);
    const gildedRose = new GildedRose([item]);
    gildedRose.updateQuality();
    verifyItem(item, 'foo', 2, -1);
  });

  it('quality should never go below 0', () => {
    const item = new Item('foo', 0, 1);
    const gildedRose = new GildedRose([item]);
    gildedRose.updateQuality();
    verifyItem(item, 'foo', 0, -1);

  });
})

describe('aged brie quality', () => {

  it('quality of Aged Brie goes up', () => {
    const item = new AgedBrie(1, 1);
    const gildedRose = new GildedRose([item]);
    gildedRose.updateQuality();
    verifyItem(item, 'Aged Brie', 3, 0);
  });

  it('quality should never go above 50', () => {
    const item = new AgedBrie(1, 50);
    const gildedRose = new GildedRose([item]);
    gildedRose.updateQuality();
    verifyItem(item, 'Aged Brie', 50, 0);
  });

  it('should allow quality of aged brie to be incremented up to 50', () => {
    const item = new AgedBrie(-10, 10);
    const gildedRose = new GildedRose([item]);
    gildedRose.updateQuality();
    verifyItem(item, 'Aged Brie', 12, -11);
  });
})

describe('sulfuras quality rules', () => {
  it('should not decrease quality for sulfuras', () => {
    const item = new Sulfuras(1, 1);
    const gildedRose = new GildedRose([item]);
    gildedRose.updateQuality();
    verifyItem(item, 'Sulfuras, Hand of Ragnaros', 1, 1);
  });
})

describe('backstage pass quality rules', () => {
  it('should increase quality of backstage passes by 1 when more than 10 days remaining', () => {
    const item = new BackstagePass(11, 1);
    const gildedRose = new GildedRose([item]);
    gildedRose.updateQuality();
    verifyItem(item, 'Backstage passes to a TAFKAL80ETC concert', 2, 10);
  });

  it('should increase quality of backstage passes by 2 when more than 5 days remaining', () => {
    const item = new BackstagePass(6, 1);
    const gildedRose = new GildedRose([item]);
    gildedRose.updateQuality();
    verifyItem(item, 'Backstage passes to a TAFKAL80ETC concert', 3, 5);
  });

  it('should increase quality of backstage passes by 3 when less than 5 days remaining', () => {
    const item = new BackstagePass(3, 1);
    const gildedRose = new GildedRose([item]);
    gildedRose.updateQuality();
    verifyItem(item, 'Backstage passes to a TAFKAL80ETC concert', 4, 2);
  });

  it('should set quality of backstage passes to 0 after concert', () => {
    const item = new BackstagePass(0, 10);
    const gildedRose = new GildedRose([item]);
    gildedRose.updateQuality();
    verifyItem(item, 'Backstage passes to a TAFKAL80ETC concert', 0, -1);
  });
})

describe('conjured items', () => {
  it('should update quality for conjured sellin 1 day', () => {
    const item = new ConjuredItem("Conjured foo", 1, 2);
    const gildedRose = new GildedRose([item]);
    gildedRose.updateQuality();
    verifyItem(item, 'Conjured foo', 0, 0);
  });

  it('should update conjured quality 4x as fast for sellin 0 days', () => {
    const item = new ConjuredItem("Conjured foo", 0, 4);
    const gildedRose = new GildedRose([item]);
    gildedRose.updateQuality();
    verifyItem(item, 'Conjured foo', 0, -1);
  });

  it('conjured item quality should never go below 0', () => {
    const item = new ConjuredItem("Conjured foo", 0, 1);
    const gildedRose = new GildedRose([item]);
    gildedRose.updateQuality();
    verifyItem(item, 'Conjured foo', 0, -1);
  });

  it('should lower quality by 3 if exactly 5 days left', () => {
    const item = new ConjuredItem("Conjured foo", 5, 6);
    const gildedRose = new GildedRose([item]);
    gildedRose.updateQuality();
    verifyItem(item, 'Conjured foo', 3, 4);
  })
})