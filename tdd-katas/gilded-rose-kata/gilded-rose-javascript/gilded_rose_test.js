require('approvals')
  .mocha();
var { Shop, Item } = require('./gilded_rose.js');

function convert_items_to_string(items) {
    data = ""
    for (i = 0; i < items.length; i++) 
      data += items[i].toString() + "\n"
    return data
}

const items = [
  new Item("+5 Dexterity Vest", 10, 20),
  new Item("Aged Brie", 2, 0),
  new Item("Elixir of the Mongoose", 5, 7),
  new Item("Sulfuras, Hand of Ragnaros", 0, 80),
  new Item("Sulfuras, Hand of Ragnaros", 1, 80),
  new Item("Backstage passes to a TAFKAL80ETC concert", 15, 20),
  new Item("Backstage passes to a TAFKAL80ETC concert", 10, 51),
  new Item("Backstage passes to a TAFKAL80ETC concert", 5, 49),
  new Item("Conjured Mana Cake", 3, 6)
]

describe('Gilded Rose', function() {
  it('should output equal to snapshot', function() {
    const gildedRose = new Shop(items)
    
    gildedRose.updateQuality()
    gildedRose.updateQuality()
    const updated_items = gildedRose.updateQuality()    
    this.verify(convert_items_to_string(updated_items))
  })
})
