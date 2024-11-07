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

  public updateToday() {
    this.decrementQuality();
  }

  public updateTomorrow() {
    this.decrementQuality();
  }

  public update() {
    this.updateToday();
    this.sellIn = this.sellIn - 1;
    this.updateTomorrow();
  }
}

export class AgedBrie extends Item {
  constructor(sellIn: number, quality: number) {
    super("Aged Brie", sellIn, quality);
  }

  public updateToday() {
    this.incrementQuality();
  }

  public updateTomorrow() {
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

export class ConjuredItem extends Item {
  constructor(name: string, sellIn: number, quality: number) {
    super(name, sellIn, quality);
  }

  public updateToday() {
    if (this.sellIn == 0) {
      this.decrementQuality();
      this.decrementQuality();
    }

    if (this.sellIn == 5)
      this.decrementQuality();

    this.decrementQuality();
  }

  public updateTomorrow(): void {
    this.decrementQuality();
  }
}

export class BackstagePass extends Item {
  constructor(sellIn: number, quality: number) {
    super("Backstage passes to a TAFKAL80ETC concert", sellIn, quality);
  }

  public updateToday() {
    this.incrementQuality()
    if (this.sellIn < 11)
      this.incrementQuality()
    if (this.sellIn < 6)
      this.incrementQuality()
  }

  public updateTomorrow() {
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
