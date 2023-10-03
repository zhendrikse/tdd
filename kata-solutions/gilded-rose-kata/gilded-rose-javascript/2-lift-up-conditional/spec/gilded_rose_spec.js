require("approvals").mocha();
const { expect } = require('chai');  // Using Expect style
var { Shop, Item } = require("../src/gilded_rose.js");

function convert_items_to_string(items) {
  data = "";
  for (i = 0; i < items.length; i++) 
    data += items[i].toString() + "\n";
  return data;
}

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
  new Item("Backstage passes to a TAFKAL80ETC concert", 0, 50),
];

describe("Gilded Rose", function () {
  it("should output equal to snapshot", function () {
    const gildedRose = new Shop(items);
    const updated_items = gildedRose.updateQuality();
    this.verify(convert_items_to_string(updated_items));
  });
});

describe("Gilded Rose", function () {
  it("should output equal to snapshot without items", function () {
    const gildedRose = new Shop();
    const updated_items = gildedRose.updateQuality();
    expect(updated_items).to.deep.equal([]);
  });
});
