---
title: Gilded rose kata
author: Zeger Hendrikse
date: 2023-09-29
css: css/neon.css
highlightTheme: github-dark
---

<!-- .slide: data-background="./images/photo-1532010940201-c31e6beacd39.jpg" -->

# The Gilded Rose kata

&nbsp;

&nbsp;

&nbsp;

&nbsp;
## by [Zeger Hendrikse](https://www.it-essence.nl/)

&nbsp;

&nbsp;


---

![Goals](./images/goals.png) <!-- .element width="25%" height="25%" -->
- <!-- .element: class="fragment" --> 
  Explain various refactoring techniques
  - <!-- .element: class="fragment" --> 
    [Creating a golden master / baseline](./approval-testing.md)
  - <!-- .element: class="fragment" --> 
    Getting acquainted with mutation testing
  - <!-- .element: class="fragment" --> 
    [Replace conditional with polymorphism](https://refactoring.guru/replace-conditional-with-polymorphism)
  - <!-- .element: class="fragment" --> 
    [Refactor Negate If](https://wiki.c2.com/?RefactorNegateIf)
  - <!-- .element: class="fragment" --> 
    [Extract method](https://wiki.c2.com/?ExtractMethod)
- <!-- .element: class="fragment" --> 
  Learn to refactor in _small_ steps
- <!-- .element: class="fragment" --> 
  The one and only useful use of code coverage &#128521;

---

### [Martin Fowler](https://martinfowler.com/): good programmers

![Martin Fowler](./images/fowler.jpg) <!-- .element width="25%" height="25%" --> 

> A fool can write code that a computer can understand.
  Good programmers write code that humans can understand.

---

## [Gilded Rose kata](https://github.com/emilybache/GildedRose-Refactoring-Kata)

### System updates items daily

* `SellIn` = number of days left to sell the item
* `Quality` = how valuable the item is
* At the end of each day both values are lowered

---

### Task: add a new category of items

* "Conjured" items degrade in `quality` twice as fast as normal items

---

<iframe frameborder="0" width="100%" height="700px" src="https://replit.com/@zwh/tdd?lite=false"></iframe>

---

## 😱 How do I even begin 😱 

```python
def update_quality(self):
  for item in self.items:
    if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
      if item.quality > 0:
        if item.name != "Sulfuras, Hand of Ragnaros":
          item.quality = item.quality - 1
    else:
      if item.quality < 50:
        item.quality = item.quality + 1
        if item.name == "Backstage passes to a TAFKAL80ETC concert":
          if item.sell_in < 11:
            if item.quality < 50:
              item.quality = item.quality + 1
...
```
---

## Start with approval tests

```python
import unittest
from approvaltests.combination_approvals import verify_all_combinations
from gilded_rose import GildedRose, Item

class GildedRoseTest(unittest.TestCase):
  def test_add_combinatorial(self):
    names = ["foo"]
    sellIns = [0]
    qualities = [0]
    verify_all_combinations(self.do_update_quality, [names, sellIns, qualities])

  def do_update_quality(self, name: str, sellIn: int, quality:int) -> str:
    items = [Item(name, sellIn, quality)]
    app = GildedRose(items)
    app.update_quality()
    return app.items[0]

if __name__ == "__main__":
    unittest.main()
```
---

## Start with all the names

- “Sulfuras, Hand of Ragnaros”
- “Aged Brie”
- “Backstage passes to a TAFKAL80ETC concert”
---

## Quality and Sell In days

- <!-- .element: class="fragment"-->
  `Quality 50`
- <!-- .element: class="fragment"-->
  `SellIn 11`
- <!-- .element: class="fragment"-->
  `SellIn -1`
- <!-- .element: class="fragment"-->
  `Quality 49` 

---

## Edge cases &amp; mutation testing

- <!-- .element: class="fragment"-->
  What if we change the "6" &rarr; "7" in line 19?
- <!-- .element: class="fragment"-->
  Add "6" to sell in 
- <!-- .element: class="fragment"-->
  What if we change the "50" &rarr; "49" in line 17? 
- <!-- .element: class="fragment"-->
  Add "48" to quality 
- <!-- .element: class="fragment"-->
  What if we change the "50" &rarr; "49" in line 20?
- Etc... <!-- .element: class="fragment"-->

---

## End result of approval tests

```python
import unittest
from approvaltests.combination_approvals import verify_all_combinations
from gilded_rose import GildedRose, Item

class GildedRoseTest(unittest.TestCase):
  def test_add_combinatorial(self):
    names = ["foo", "Aged Brie", "Sulfuras, Hand of Ragnaros", "Backstage passes to a TAFKAL80ETC concert"]
    sellIns = [-1, 2, 6, 0, 11, 7]
    qualities = [0, 48, 49, 50, 47]
    verify_all_combinations(self.do_update_quality, [names, sellIns, qualities])

  def do_update_quality(self, name: str, sellIn: int, quality:int) -> str:
    items = [Item(name, sellIn, quality)]
    app = GildedRose(items)
    app.update_quality()
    return app.items[0]

if __name__ == "__main__":
    unittest.main()
```
---

## [Extract method](https://wiki.c2.com/?ExtractMethod)

- Turn the fragment into a method whose name explains the purpose of the method

```python
def update_quality(self):
  for item in self.items:
    update_item_quality(item)
```

---

## [Refactor Negate If](https://wiki.c2.com/?RefactorNegateIf)

- Eliminate negate and "flip" the conditional

```python
if item.name == "Aged Brie" or item.name == "Backstage passes to a TAFKAL80ETC concert":
```
---

## [Lift-Up Conditional](https://www.eficode.com/blog/advanced-testing-refactoring-techniques-2) &mdash; step 1

- Create temporary `foo(self, item)` with all logic

```python
def update_item_quality(self, item):
  self.foo(item)

def foo(self, item):
  if item.name == "Aged Brie" or item.name == "Backstage passes to a TAFKAL80ETC concert":
  ...  
```

---

## [Lift-Up Conditional](https://www.eficode.com/blog/advanced-testing-refactoring-techniques-2) &mdash; step 2
  
- Add conditional

```python
def update_item_quality(self, item):
  if item.name == "Aged Brie":
    self.foo(item)
  else: 
    self.foo(item)
```

---

## [Lift-Up Conditional](https://www.eficode.com/blog/advanced-testing-refactoring-techniques-2) &mdash; step 3
  
1. <!-- .element: class="fragment"-->
   Inline `foo()`, run and inspect coverage!
2. <!-- .element: class="fragment"-->
   Remove dead code
3. <!-- .element: class="fragment"-->
   Inspect coverage of conditionals
   - Hover over to see more details 
   - Remove dead branches
4. <!-- .element: class="fragment"-->
   Take out "Agred Brie" from `else`-clause
   
---

## Rinse and repeat 

The same for the `else`-branch of "Aged Brie"

```python
else:
  if item.name == "Backstage passes to a TAFKAL80ETC concert":
    self.foo(item)
  else:
    self.foo(item)
```

---

## Rinse and repeat 

Do the same for the `else`-branch of "Backstage passes to a TAFKAL80ETC concert"

```python
else:
  if item.name == "Sulfuras, Hand of Ragnaros":
    self.foo(item)
  else:
    self.foo(item)
```

---

## Rearrange item type conditional

```python
if item.name == "Aged Brie":
  ...
elif item.name == "Backstage passes to a TAFKAL80ETC concert":
  ...
else:
  if item.name != "Sulfuras, Hand of Ragnaros":
    ...
```

---

## [Refactor Negate If](https://wiki.c2.com/?RefactorNegateIf)

```python
if item.name == "Aged Brie":
  ...
elif item.name == "Backstage passes to a TAFKAL80ETC concert":
  ...
elif item.name == "Sulfuras, Hand of Ragnaros":
  pass
else:
  ...

```

---

## [Replace conditional with polymorphism](https://refactoring.guru/replace-conditional-with-polymorphism)

---

## Introduce Aged Brie class

```python
class AgedBrieItem(Item):
  def update_quality(self) -> None:
    if self.quality < 50:
      self.quality += 1
    self.sell_in -= 1
    if self.sell_in < 0:
      if self.quality < 50:
        self.quality += 1
```

Test case

```python
def do_update_quality(self, name: str, sellIn: int, quality: int) -> str:
  if name == "Aged Brie":
    items = [AgedBrieItem(name, sellIn, quality)]
  else:
    items = [Item(name, sellIn, quality)]
```

---

## The other subclasses

```python
class BackstagePassItem(Item):
  def update_quality(self) -> None:
    if self.quality < 50:
      self.quality += 1
      if self.sell_in < 11:
        if self.quality < 50:
          self.quality += 1
      if self.sell_in < 6:
        if self.quality < 50:
          self.quality += 1

    self.sell_in -= 1
    if self.sell_in < 0:
      self.quality = 0
```

---

## The other subclasses

```python
class SulfurasItem(Item):
  def update_quality(self) -> None:
    pass
```

---

## The base class

```python
class Item:
  ...

  def update_quality(self) -> None:
    if self.quality > 0:
      self.quality -= 1
    self.sell_in -= 1
```

---

## Set name in constructor

```python
class BackstagePassItem(Item):
  def __init__(self, sell_in, quality):
    super().__init__("Backstage passes to a TAFKAL80ETC concert", sell_in, quality)
``` 

---

## Primitive obsession

```python
class Quality:
  def __init__(self, quality: int):
    self.value = quality

  def increase(self):
    if self.value < 50:
      self.value += 1

  def decrease(self):
    if self.value > 0:
      self.value -= 1
```

with

```python
class Item:
  def __init__(self, name, sell_in, quality):
    self.name = name
    self.sell_in = sell_in
    self.quality = Quality(quality)

  def __repr__(self):
    return "%s, %s, %s" % (self.name, self.sell_in, self.quality.value)
```

---

## Retrospective

- <!-- .element: class="fragment"-->
  [Mocks, stubs, fakes, spies, ...](https://martinfowler.com/articles/mocksArentStubs.html)
- <!-- .element: class="fragment"-->
  [The Clean Architecture](https://khalilstemmler.com/articles/software-design-architecture/organizing-app-logic/): how to cope with dependencies on external systems</li>
- <!-- .element: class="fragment"-->
  [London school / Detroit school of TDD](https://blog.devgenius.io/detroit-and-london-schools-of-test-driven-development-3d2f8dca71e5)
- <!-- .element: class="fragment"-->
  Developer tests his own code: the nightmare of every auditor!
