# Introduction

Please read the general [introduction to the vending machine](../README.md) first!

# Getting started

First, create an intial Python kata set-up as described [here](https://github.com/zhendrikse/tdd/tree/master/cookiecutter).

Next, go the the newly created project directory and consult
the provided ``README.md`` in there.

# Implementation instructions

## Delivering cans without cost

Let's first write a specification for a vending machine that delivers
nothing, whatever we ask it to deliver:

```python
with description(VendingMachine) as self:
  with context("A new vending machine"):
    with it("does not deliver anything"):
        vending_machine  = VendingMachine()
        expect(vending_machine.deliver(Choice.COKE)).to(be(Can.NOTHING))
```

Obviously, this fails miserably, as the both the deliver method and the
enumerations are not defined. So let's introduce them both in the 
production code

```python
from enum import Enum

class Can(Enum):
  NOTHING = "Nothing"

class Choice(Enum):
  COKE = "Coke"
  
class VendingMachine:
  def deliver(self, choice: Choice) -> Can:
    return Can.NOTHING
```

We should have our first passing test already!

Let's try to get some coke though:

```python
    with it("delivers Cola when coke is selected"):
        vending_machine  = VendingMachine()
        expect(vending_machine.deliver(Choice.COKE)).to(be(Can.COLA))
```

Before we continue, notice that we have two tests now that are 
completely identical, but expect different results. How do we solve this?

We solve this by configuring the vending machine with a choice, so
that we can expect a different outcome.

```python
    with it("delivers Cola when coke is selected"):
        vending_machine  = VendingMachine()
        vending_machine.configure(Choice.COKE, Can.COLA)
        expect(vending_machine.deliver(Choice.COKE)).to(be(Can.COLA))
```

Now the vending machine must be extended just a little bit

```python
class VendingMachine:
  def __init__(self):
    self._can_of_choice = Can.NOTHING

  def configure(self, choice: Choice, can: Can) -> None:
    self._can_of_choice = can
    
  def deliver(self, choice: Choice) -> Can:
    return self._can_of_choice
```

Next, identify the duplicate code (hint: in the spec file), and
eliminate it using the ``before.Each:``

```python
    with beforeEach:
        self.vending_machine  = VendingMachine()
```

Let's configure a different drink

```python
    with it("delivers a can of fanta when choice is fizzy orange"):
        self.vending_machine.configure(Choice.FIZZY_ORANGE, Can.FANTA)
        expect(self.vending_machine.deliver(Choice.FIZZY_ORANGE)).to(be(Can.FANTA))
```

After extending the choice and can types, we notice that the test jumps to 
green. 


In order to make the configuration more similar with the previous test,
we can add a similar line to our current test and vice versa:

```python
    with it("delivers a can of fanta when choice is fizzy orange"):
        self.vending_machine.configure(Choice.COKE, Can.COLA)
        self.vending_machine.configure(Choice.FIZZY_ORANGE, Can.FANTA)
        expect(self.vending_machine.deliver(Choice.FIZZY_ORANGE)).to(be(Can.FANTA))
```

However, we must _very carefully_ watch the order in which we configure
the vending machine, as the latest configured can type is returned always!

So let's intentionally reverse these configuration statements now, so that
we are forced to generalize our production code:

```python
class VendingMachine:
  def __init__(self) -> None:
    self._choice_can_map: dict[Choice, Can] = {}

  def configure(self, choice: Choice, can: Can) -> None:
    self._choice_can_map[choice] = can
    
  def deliver(self, choice: Choice) -> Can:
    if not choice in self._choice_can_map:
      return Can.NOTHING
    return self._choice_can_map[choice]
```

Finally, note that we can actually configure the vending machine 
once for all tests

```python
    with before.each:
        self.vending_machine  = VendingMachine()
        self.vending_machine.configure(Choice.FIZZY_ORANGE, Can.FANTA)
        self.vending_machine.configure(Choice.COKE, Can.COLA)
```

This makes our first test fail, because it now actually gets 
delivered a can of Coke. But the idea of the first test was to 
test for a non-existing choice, so let's replace the ``Choice.COLA`` 
by ``Choice.BEER``. Now all three tests are green again!

## Delivering cans that cost money

Delivering a can should actually cost money! So asking for a can of coke
should not deliver anything...

```javascript
    it("delivers a can of fanta when choice is fizzy orange", () => {
        expect(vending_machine.deliver(Choice.COKE)).to.equal(Can.NOTHING);
    })
```

Again we are facing the riddle: how can we choose a can of coke and have
a can delivered in the first set of tests, and now with the same test no
can at all??

Again, we solve this by configuring the machine to deliver drinks that
cost money, bij adding a parameter to the configure method that specifies
the price in cents:

```javascript
    it("delivers no can when choice requires money", () => {
        vending_machine.configure(Choice.COKE, Can.COLA, 250);
        expect(vending_machine.deliver(Choice.COKE)).to.equal(Can.NOTHING);
    })
```

We modify the production code accordingly to make the test pass:

```javascript
  configure(choice, can, priceInCents = 0) {
    this.priceInCents = priceInCents
    this.choiceCanMap.set(choice, can)
  }
  
  deliver(choice) {
    if (this.choiceCanMap.has(choice) && this.priceInCents == 0)
      return this.choiceCanMap.get(choice)

    return Can.NOTHING
  }
```

When we enter the required amount of money, we should get our
can of choice again

```javascript
    it("delivers can of choice when required money is inserted", () => {
        vending_machine.insert(250);
        vending_machine.configure(Choice.COKE, Can.COLA, 250);
        expect(vending_machine.deliver(Choice.COKE)).to.equal(Can.COLA);
    })
```

This forces us to modify the implementation like so

```javascript
  constructor() {
    this.choiceCanMap = new Map()
    this.priceInCents = 0
    this.balanceInCents = 0
  }
  
  configure(choice, can, priceInCents = 0) {
    this.priceInCents = priceInCents
    this.choiceCanMap.set(choice, can)
  }

  insert(priceInCents) {
    this.balanceInCents = priceInCents
  }
  
  deliver(choice) {
    if (this.choiceCanMap.has(choice) && this.priceInCents == this.balanceInCents)
      return this.choiceCanMap.get(choice)
```

Again, we observe duplication in the specification file, which leads
to a nesting of the ``describe`` statements

```javascript
    describe("that requires drinks to be paid", () =>  {
  
      beforeEach(function () {
          vending_machine = new VendingMachine()
          vending_machine.configure(Choice.COKE, Can.COLA, 250);
      })
      
      it("delivers no can when choice requires money", () => {
          expect(vending_machine.deliver(Choice.COKE)).to.equal(Can.NOTHING);
      })
        
      it("delivers can of choice when required amount is inserted", () => {
          vending_machine.insert(250);
          expect(vending_machine.deliver(Choice.COKE)).to.equal(Can.COLA);
      })
```

Of course, the equality sign doesn't make sense, as we also 
expect a can of choice when we pay too much

```javascript
    it("delivers can of choice when more than required amount is inserted", () => {
        vending_machine.insert(300);
        expect(vending_machine.deliver(Choice.COKE)).to.equal(Can.COLA);
    })
```
This test only requires a minor modification in the production code

```javascript
  deliver(choice) {
    if (this.choiceCanMap.has(choice) && this.priceInCents <= this.balanceInCents)
```

Obviously, we also must accommodate for different prices for the different drinks:

```javascript
    it("delivers can of Fanta when required amount is inserted", () => {
        vending_machine.insert(300);
        vending_machine.configure(Choice.FIZZY_ORANGE, Can.FANTA, 300);
        expect(vending_machine.deliver(Choice.COKE)).to.equal(Can.COLA);
    })
```

This test jumps to green immediately, but that's because the most recently
configured price is used always. As soon as we move the configuration to 
the ``beforeEach()`` step, the test fails!

So now we need to introduce yet another map, namely a map between choices
and prices.

Finaly, we expect no more cans after a can has been withdrawn, as our
balance should have shrunk

```javascript
    it("delivers no can after a can has been delivered", () => {
        vending_machine.insert(250);
        vending_machine.deliver(Choice.COKE);
        expect(vending_machine.deliver(Choice.COKE)).to.equal(Can.NOTHING);
    })
```

So after withdrawal of a drink, the balance should be adjusted
accordingly. After some minor refactoring of the deliver method
we arrive at

```javascript
  deliver(choice) {
    var price = this.choicePriceMap.get(choice)
    if (!this.choiceCanMap.has(choice) || price > this.balanceInCents) 
      return Can.NOTHING

    this.balanceInCents -= price
    return this.choiceCanMap.get(choice)
  }
```

# Code smells

## [Data clump](https://refactoring.guru/smells/data-clumps)

It now becomes clear that the ``choiceCanMap`` and ``choicePriceMap`` always
appear together, so let's assign them their own (data) class ``Drawer``

```javascript
class Drawer {
  constructor(can, priceInCents) {
    this.can = can
    this.priceInCents = priceInCents
  }
}
```

Since the members are publicly accesible, we can directly use them.
However, this immediately leads to another code smell, namely
[feature envy](https://refactoring.guru/smells/feature-envy).

As a first step, we can move the delivery logic into the ``Drawwer`` class

```javascript
  getCan(vendingMachine) {
    if (this.priceInCents > vendingMachine.balanceInCents)
      return Can.NOTHING
    
    vendingMachine.balanceInCents -= this.priceInCents
    return this.can
  }
```

with which the ``VendingMachine`` simplifies to

```javascript
  deliver(choice) {
    if (!this.choiceDrawerMap.has(choice))
      return Can.NOTHING

    var drawer = this.choiceDrawerMap.get(choice)
    return drawer.getCan(this)
  }
```

Note that we have now introduced a new code smell, namely
[inappropriate intimacy](https://refactoring.guru/smells/inappropriate-intimacy), 
as the drawer depends on the vending machine and vice versa.

So let's introduce a kind of cashier that has the responsibility 
of dealing with the transaction(s). To do so in small steps, we
first wrap the balance in the new class ``Cashier``, and gradually
move the logic that goes with it as well.

```javascript
class Cashier {
  constructor() {
    this.balanceInCents = 0
  }  

  insert(amountInCents) {
    this.balanceInCents += amountInCents
  }

  doesBalanceAllow(priceInCents) {
    return this.balanceInCents >= priceInCents
  }

  buy(amountInCents) {
    this.balanceInCents -= amountInCents
  }
}
```

This means that the ``Drawer`` class is no longer dependent on the
``VendingMachine`` class, but on the ``Cashier`` instead

```javascript
class Drawer {
  constructor(can, priceInCents) {
    this.can = can
    this.priceInCents = priceInCents
  }

  deliver(cashier) {
    if (!cashier.doesBalanceAllow(this.priceInCents))
      return Can.NOTHING
    
    cashier.buy(this.priceInCents)
    return this.can    
  }
}
```