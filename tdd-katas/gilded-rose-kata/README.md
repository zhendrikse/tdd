# About the Gilded Rose kata

![Aged Brie](./assets/aged-brie.png)

The [Gilded Rose kata](https://github.com/emilybache/GildedRose-Refactoring-Kata) is a kata about a store where goods degrade in quality as they approach their sell date:

- All items have a SellIn value which denotes the number of days we have to sell the item
- All items have a Quality value which denotes how valuable the item is
- At the end of each day our system lowers both values for every item

The item sell date and quality are daily updated by invocation of the associated `update()` method call.
Pretty simple, right? Well this is where it gets interesting:

- Once the sell by date has passed, Quality degrades twice as fast
- The Quality of an item is never negative
- "Aged Brie" actually increases in Quality the older it gets
- The Quality of an item is never more than 50
- "Sulfuras", being a legendary item, never has to be sold or decreases in Quality
- "Backstage passes", like aged brie, increases in Quality as its SellIn value approaches;
Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
Quality drops to 0 after the concert

### Eventual goal

The eventual goal of this kata is to add a new category of items, namely "Conjured" items that degrade in `Quality` twice as fast as normal items.

## Creating a golden master

Before we can touch/modify/refactor an existing code base, we first have to make sure we keep the current behaviour unaltered. To this extent, we first have to create a snapshot or so-called golden master.

![Snapshot](./assets/snapshot.png)

This is exactly what we will do in this excercise using [approval testing](https://approvaltests.com/).

## References

- Refactoring the Gilded Rose [manually versus using Sourcery](https://sourcery.ai/blog/refactoring-gilded-rose/)

