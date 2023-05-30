# Retrofitting specifications  

In this repl you find the solution to the previous exercise, namely the refactored code of the Gilded Rose kata. Remember that this code has successfully been tested with the approval tests.

In this repl, the approval tests have been removed. Consequently, the code coverage has dropped back to zero. The first goal of this part of the kata is, to retrofit specifications and scenarios to the refactored code base, so that the code becomes as thoroughly tested as it was the case with the approval tests, but this time with scenarios and specifications properly describing the semantics.

When this is done, we can finally start extending the existing functionality.

## Reiterating the original specifications
![Aged brie](./assets/aged-brie.png)

In order to make sure we are going to write scenarios and specifications that [express the intent](https://martinfowler.com/bliki/BeckDesignRules.html#:~:text=%22Reveals%20intention%22%20is%20Kent's%20way,should%20be%20easy%20to%20understand.&text=Kent's%20form%20of%20expressing%20this,purpose%20was%20when%20writing%20it.) of the logic, we are going to reiterate the original kata description first.

As you may remember, we have introducted the [Gilded Rose kata](https://github.com/emilybache/GildedRose-Refactoring-Kata) as a kata about a store where goods degrade in quality as they approach their sell date:

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

## The exercises

In the following exercises, try to apply everything you have learned thus far:

- Write semantically/intent expressing scenarios and specifications
- You are not done until you have 100% coverage
- Make sure all edge cases (of the numeric values) are covered

### Exercise I

Apply the DRY principle to the given sulfuras scenarios in the sulfuras specification file.

### Exercise II

Are there more scenarios to be added to the specification of the sulfuras items? If not, why not? If so, which ones?

### Exercise III

Create scenarios and specifications for the aged brie items. When you have got 100% coverage for the aged brie item class, make sure you also get the one-off cases, by applying mutation test(s) to the `post_sell_in_quality_update()` method.
  
### Exercise IV  

Add the conjured item subclass in a TDD manner: writing the scenarios first, apply red-green-refactor, make small steps, apply Kent Beck's principles, etc.

### Exercise V 

In the original kata, the following requirement is mentioned:

> Just for clarification, an item can never have its Quality increase above 50, however "Sulfuras" is a
legendary item and as such its Quality is 80 and it never alters.

Note that our combinatortial approval tests also inevitably created "Sulfuras" items with quality other than 80. Modify the specification and production code for the "Sulfuras" items now in such a way, that the quality is initially set to 80 and can never be changed.