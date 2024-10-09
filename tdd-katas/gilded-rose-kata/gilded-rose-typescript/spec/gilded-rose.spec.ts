'use strict';

import { Item, GildedRose } from '../src/gilded-rose';

describe('Gilded Rose', () => {
  it('updates a foo item', () => {
    const gildedRose = new GildedRose([new Item('foo', 0, 0)]);
    const items = gildedRose.updateQuality();
    expect(items[0].name).toBe('foo');
    expect(items[0].sellIn).toBe(-1);
    expect(items[0].quality).toBe(0);
  });
});

