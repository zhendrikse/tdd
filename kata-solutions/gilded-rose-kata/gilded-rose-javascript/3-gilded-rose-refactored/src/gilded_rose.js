class Item {
  constructor(name, sellIn, quality) {
    this.name = name;
    this.sellIn = sellIn;
    this.quality = quality;
  }

  updateQualityAfterSellIn() {
    if (this.quality > 0)
      this.quality = this.quality - 1;
  }

  updateQualityBeforeSellIn() {
    if (this.quality > 0)
      this.quality = this.quality - 1;
  }

  incrementQuality() {
    if (this.quality < 50)
      this.quality = this.quality + 1;
  }

  updateProduct() {
    this.updateQualityBeforeSellIn();
    this.sellIn = this.sellIn - 1;
    this.updateQualityAfterSellIn();
  }

  toString() {
    return "name: " + this.name + ", sellIn: " + this.sellIn + ", quality: " + this.quality
  }
}

class BackstagePass extends Item {
  constructor(sellIn, quality) {
    super('Backstage passes to a TAFKAL80ETC concert', sellIn, quality);
  }

  updateQualityBeforeSellIn() {
    if (this.quality < 50) {
      this.quality = this.quality + 1;
      if (this.sellIn < 11) 
        super.incrementQuality();
      if (this.sellIn < 6) 
        super.incrementQuality();
    }
  }

  updateQualityAfterSellIn() {
    if (this.sellIn < 0) 
      this.quality = 0;
  }
}

class AgedBrie extends Item {
  constructor(sellIn, quality) {
    super('Aged Brie', sellIn, quality);
  }

  updateQualityBeforeSellIn() {
    super.incrementQuality();
  }

  updateQualityAfterSellIn() {
    super.incrementQuality();
  }
}

class Sulfuras extends Item {
  constructor(sellIn, quality) {
    super('Sulfuras, Hand of Ragnaros', sellIn, quality);
  }

  updateProduct() {
  }
}

class Shop {
  constructor(items = []) {
    this.items = items;
  }

  updateQuality() {
    for (var i = 0; i < this.items.length; i++)
      this.items[i].updateProduct();

    return this.items;
  }
}

module.exports = {
  Item,
  Sulfuras, 
  BackstagePass,
  AgedBrie,
  Shop
}
