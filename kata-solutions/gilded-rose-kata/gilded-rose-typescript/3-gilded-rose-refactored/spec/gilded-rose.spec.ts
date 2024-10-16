'use strict';

import { Item, GildedRose, Sulfuras, BackstagePass, AgedBrie } from '../src/gilded-rose';
import {verify, verifyAsJson} from "approvals/lib/Providers/Jest/JestApprovals";

function convert_items_to_string(items = [] as Array<Item>) {
  let items_as_string = items.map((item) => item.toString() + "\n")
  return items_as_string.reduce(
    (accumulator, currentValue) => accumulator + currentValue,
    "",
  );
}

describe('Gilded Rose', () => {
  it('updates a foo item', () => {
    const items = [
      new Item("Foo", 0, 0),
      new Item("Foo", 0, 10),
      new Item("Foo", -1, 0),
      new Item("Foo", -10, 2),
      new Item("Foo", -10, 51),
      new Sulfuras(-1, 1),
      new Sulfuras(0, 10),
      new AgedBrie(-1, 0),
      new AgedBrie(0, 50),
      new BackstagePass(1, 0),
      new BackstagePass(0, 0),
      new BackstagePass(11, 48),
      new BackstagePass(11, 49),
      new BackstagePass(10, 48),
      new BackstagePass(10, 49),
      new BackstagePass(10, 50),
      new BackstagePass(5, 47),
      new BackstagePass(5, 48),
      new BackstagePass(5, 49),
      new BackstagePass(6, 47),
      new BackstagePass(0, 50),    
    ];
    const gildedRose = new GildedRose(items);
    const updated_items = gildedRose.updateQuality();
    verify(convert_items_to_string(updated_items));
  });
});

