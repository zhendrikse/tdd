require("approvals").mocha();
var { Shop, Item } = require("../src/gilded_rose.js");

function convert_items_to_string(items) {
  data = "";
  for (item of items) 
    data += item.toString() + "\n";

  return data;
}

const items = [
  new Item("Foo", 0, 0)
];

describe("Gilded Rose", function () {
  it("should output equal to snapshot", function () {
    const gildedRose = new Shop(items);
    const updated_items = gildedRose.updateQuality();
    this.verify(convert_items_to_string(updated_items));
  });
});

