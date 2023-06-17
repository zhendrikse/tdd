# Introduction

Please read the general [introduction to the stack kata](../README.md) first!

# Getting started

First, create an intial Python kata set-up as described [here](https://github.com/zhendrikse/tdd/tree/master/cookiecutter).

Next, go the the newly created project directory and consult
the provided ``README.md`` in there.

# Implementation instructions

## Delivering cans without cost

Let's first write a specification for a vending machine that delivers
nothing, whatever we ask it to deliver:

```javascript
describe("A new vending machine", function() {
    it("does not deliver anything", function () {
        let vending_machine  = new VendingMachine();
        expect(vending_machine.deliver(Choice.COKE)).to.equal(Can.NOTHING);
    })
})
```

Obviously, this fails miserably, as the both the deliver method and the
enumerations are not defined. So let's introduce them both in the 
production code

```javascript
class Choice {
  static COKE = "Coke"
}

class Can {
  static NOTHING = "No can"
}

class VendingMachine {  
  deliver(choice) {
    return Can.NOTHING
  }
}
```

We must make these definitions available to the logic in the specification
file(s), so we add 

```javascript

module.exports = {
  Can: Can,
  Choice: Choice,
  VendingMachine: VendingMachine
}
```

to the production code and add

```javascript
const { VendingMachine, Choice, Can } = require('../src/VendingMachine.js')
```

to our specifications file. 

We should have our first passing test now.

Let's try to get some coke though:

```javascript
    it("delivers Cola when coke is selected", function () {
        let vending_machine  = new VendingMachine();
        expect(vending_machine.deliver(Choice.COKE)).to.equal(Can.COLA);
    })
```

Before we continue, notice that we have two tests now that are 
completely identical, but expect different results. How do we solve this?

We solve this by configuring the vending machine with a choice, so
that we can expect a different outcome.

```javascript
    it("delivers Cola when coke is selected", function () {
        let vending_machine  = new VendingMachine();
        vending_machine.configure(Choice.COKE, Can.COLA);
        expect(vending_machine.deliver(Choice.COKE)).to.equal(Can.COLA);
    })
```

Now the vending machine must be extended just a little bit

```javascript
class VendingMachine {
  constructor() {
    this.can = Can.NOTHING
  }
  
  configure(choice, can) {
    this.can = Can.COLA
  }
  
  deliver(choice) {
    return this.can
  }
}
```

Next, identify the duplicate code (hint: in the spec file), and
eliminate it using the ``beforeEach()``

```javascript
    beforeEach(function () {
      // ...
    })
```

Let's configure a different drink

```javascript
    it("delivers a can of fanta when choice is fizzy orange", () => {
        vending_machine.configure(Choice.FIZZY_ORANGE, Can.FANTA);
        expect(vending_machine.deliver(Choice.FIZZY_ORANGE)).to.equal(Can.FANTA);
    })
```

After extending the choice and can types, we can easily make this test
pass by modifying the ``deliver()`` method slightly

```javascript
  configure(choice, can) {
    this.can = can
  }
```

In order to make the configuration more similar with the previous test,
we can add a similar line to our current test and vice versa:

```javascript
    it("delivers a can of fanta when choice is fizzy orange", () => {
        vending_machine.configure(Choice.COKE, Can.COLA);
        vending_machine.configure(Choice.FIZZY_ORANGE, Can.FANTA);
        expect(vending_machine.deliver(Choice.FIZZY_ORANGE)).to.equal(Can.FANTA);
    })
```

However, we must _very carefully_ watch the order in which we configure
the vending machine, as the latest configured can type is returned always.

So let's intentionally reverse these configuration statements now, so that
we are forced to generalize our production code:

```javascript
class VendingMachine {
  constructor() {
    this.choiceCanMap = new Map();
  }
  
  configure(choice, can) {
    this.choiceCanMap.set(choice, can);
  }
  
  deliver(choice) {
    if (this.choiceCanMap.has(choice))
      return this.choiceCanMap.get(choice)

    return Can.NOTHING
  }
}
```

Finally, note that we can actually configure the vending machine 
once for all tests

```javascript
    beforeEach(function () {
        vending_machine = new VendingMachine()
        vending_machine.configure(Choice.FIZZY_ORANGE, Can.FANTA);
        vending_machine.configure(Choice.COKE, Can.COLA);
    })
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