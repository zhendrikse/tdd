'use strict';

import { Item, GildedRose } from '../src/gilded-rose';
import { verify } from "approvals/lib/Providers/Jest/JestApprovals";
import { configure } from "approvals/lib/config";
import { JestReporter } from "approvals/lib/Providers/Jest/JestReporter";

function convert_items_to_string(items = [] as Array<Item>) {
  let items_as_string = items.map((item) => item.toString() + "\n")
  return items_as_string.reduce(
    (accumulator, currentValue) => accumulator + currentValue,
    "",
  );
}

describe('Gilded Rose', () => {
  beforeAll(() => {
    configure({
      reporters: [new JestReporter()],
    });
  });

  it('updates a foo item', () => {
    const items = [
      new Item("Foo", 0, 0),
      new Item("Foo", 0, 10),
      new Item("Foo", -1, 0),
      new Item("Foo", -10, 2),
      new Item("Foo", -10, 51),
      new Item("Sulfuras, Hand of Ragnaros", -1, 1),
      new Item("Sulfuras, Hand of Ragnaros", 0, 10),
      new Item("Aged Brie", -1, 0),
      new Item("Aged Brie", 0, 50),
      new Item("Backstage passes to a TAFKAL80ETC concert", 1, 0),
      new Item("Backstage passes to a TAFKAL80ETC concert", 0, 0),
      new Item("Backstage passes to a TAFKAL80ETC concert", 11, 48),
      new Item("Backstage passes to a TAFKAL80ETC concert", 11, 49),
      new Item("Backstage passes to a TAFKAL80ETC concert", 10, 48),
      new Item("Backstage passes to a TAFKAL80ETC concert", 10, 49),
      new Item("Backstage passes to a TAFKAL80ETC concert", 10, 50),
      new Item("Backstage passes to a TAFKAL80ETC concert", 5, 47),
      new Item("Backstage passes to a TAFKAL80ETC concert", 5, 48),
      new Item("Backstage passes to a TAFKAL80ETC concert", 5, 49),
      new Item("Backstage passes to a TAFKAL80ETC concert", 6, 47),
      new Item("Backstage passes to a TAFKAL80ETC concert", 0, 50)
    ];
    const gildedRose = new GildedRose(items);
    const updated_items = gildedRose.updateQuality();
    verify(convert_items_to_string(updated_items));
  });
});

