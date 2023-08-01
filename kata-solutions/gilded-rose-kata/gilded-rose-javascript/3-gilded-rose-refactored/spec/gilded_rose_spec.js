require("approvals").mocha();
var { Shop, Item, BackstagePass, Sulfuras, AgedBrie } = require("../src/gilded_rose.js");

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
    expect(updated_items).toEqual([]);
  });
});