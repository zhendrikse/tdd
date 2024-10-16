'use strict';

export class Item {
  name: string = "";
  sellIn: number = 0;
  quality: number = 0;

  constructor(name: string, sellIn: number, quality: number) {
    this.name = name;
    this.sellIn = sellIn;
    this.quality = quality;
  }

  public toString(): string {
    return "name: " + this.name + ", sellIn: " + this.sellIn + ", quality: " + this.quality
  }
}

export class GildedRose {
  items: Array<Item>;

  constructor(items = [] as Array<Item>) {
    this.items = items;
  }

  updateQuality() {
    this.items.forEach(item => this.updateItem(item));
    return this.items;
  }

  private updateItem(item: Item) {
    if (item.name == 'Aged Brie') {
      if (item.quality < 50)
        item.quality = item.quality + 1;
      item.sellIn = item.sellIn - 1;
      if (item.sellIn < 0)
        if (item.quality < 50)
          item.quality = item.quality + 1;
    } else {
      if (item.name == 'Backstage passes to a TAFKAL80ETC concert') {
        if (item.quality < 50) {
          item.quality = item.quality + 1;
          if (item.sellIn < 11)
            if (item.quality < 50)
              item.quality = item.quality + 1;
          if (item.sellIn < 6)
            if (item.quality < 50)
              item.quality = item.quality + 1;
        }
        item.sellIn = item.sellIn - 1;
        if (item.sellIn < 0)
          item.quality = item.quality - item.quality;
      } else if (item.name == 'Sulfuras, Hand of Ragnaros') {
        // intentionally left blank
      } else {
        if (item.quality > 0)
          item.quality = item.quality - 1;
        item.sellIn = item.sellIn - 1;
        if (item.sellIn < 0)
          if (item.quality > 0)
            item.quality = item.quality - 1;
      }
    }
  }
}

