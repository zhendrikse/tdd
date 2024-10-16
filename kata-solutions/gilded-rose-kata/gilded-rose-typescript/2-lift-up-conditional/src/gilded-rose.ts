'use strict';

import internal from "stream";

export class Item {
  name: string = "";
  sellIn: number = 0;
  quality: number = 0;

  constructor(name: string, sellIn: number, quality: number) {
    this.name = name;
    this.sellIn = sellIn;
    this.quality = quality;
  }

  public incrementQuality() {
    if (this.quality < 50)
      this.quality = this.quality + 1;
  }

  public decrementQuality() {
    if (this.quality > 0)
      this.quality = this.quality - 1;
  }

  public update() {
    this.decrementQuality();
    this.sellIn = this.sellIn - 1;
    this.decrementQuality();
  }

  public toString(): string {
    return "name: " + this.name + ", sellIn: " + this.sellIn + ", quality: " + this.quality
  }
}

export class AgedBrie extends Item {
  constructor(sellIn: number, quality: number) {
    super("Aged Brie", sellIn, quality);
  }

  public update() {
    this.incrementQuality();
    this.sellIn = this.sellIn - 1;
    this.incrementQuality();
  }
}

export class Sulfuras extends Item {
  constructor(sellIn: number, quality: number) {
    super("Sulfuras, Hand of Ragnaros", sellIn, quality);
  }

  public update() {
  }
}

export class BackstagePass extends Item {
  constructor(sellIn: number, quality: number) {
    super("Backstage passes to a TAFKAL80ETC concert", sellIn, quality);
  }

  public update() {
    if (this.quality < 50)
      this.quality = this.quality + 1;
    if (this.sellIn < 11)
      if (this.quality < 50)
        this.quality = this.quality + 1;
    if (this.sellIn < 6)
      if (this.quality < 50)
        this.quality = this.quality + 1;
    
    this.sellIn = this.sellIn - 1;
    
    if (this.sellIn < 0)
      this.quality = 0;
  }
}

export class GildedRose {
  items: Array<Item>;

  constructor(items = [] as Array<Item>) {
    this.items = items;
  }

  public updateQuality(): Array<Item> {
    this.items.forEach(item => item.update());
    return this.items;
  }
}
