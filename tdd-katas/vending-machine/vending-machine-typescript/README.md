# Introduction

Please read the general [introduction to the stack kata](../README.md) first!

# Getting started

First, create an initial Typescript kata set-up as described [here](https://github.com/zhendrikse/tdd/tree/master/cookiecutter).

Next, go the newly created project directory and consult
the provided `README.md` in there.

# Implementation instructions

## Delivering cans without cost

Let's first write a specification for a vending machine that delivers
nothing, whatever we ask it to deliver:

```typescript
  it("delivers nothing when choice does not exist", () => {
    let vendingMachine = new VendingMachine()
    expect(vendingMachine.deliver(Choice.COLA)).to.equal(Can.NOTHING)
  })
```

Obviously, this fails miserably, as the both the deliver method and the
enumerations are not defined. So let's introduce them both in the 
production code

```typescript
export enum Choice {
  COLA = "Cola choice"
}

export enum Can {
  NOTHING = "No can"
}

export class VendingMachine {
    deliver(choice: Choice): Can {
      return Can.NOTHING
    }  
}
```

We must make these definitions available to the logic in the specification
file(s), so we add 

```typescript
import { VendingMachine, Can, Choice } from "../src/VendingMachine"
```

to our specifications file. We should have our first passing test now!

Let's try to get some coke though:

```typescript
  it("delivers Cola when coke is selected", () => {
    let vendingMachine = new VendingMachine()
    expect(vendingMachine.deliver(Choice.COKE)).to.equal(Can.COLA)
  })
```

Before we continue, notice that we have two tests now that are 
completely identical, but expect different results. How do we solve this?

We solve this by configuring the vending machine with a choice, so
that we can expect a different outcome.

```typescript
    it("delivers Cola when coke is selected", function () {
        let vending_machine  = new VendingMachine();
        vendingMachine.configure(Choice.COLA, Can.COKE)
        expect(vending_machine.deliver(Choice.COLA)).to.equal(Can.COKE)
    })
```

Now the vending machine must be extended just a little bit

```typescript
export class VendingMachine {
    private canToDeliver: Can
  
    constructor() {
      this.canToDeliver = Can.NOTHING
    }
  
    configure(choice: Choice, can: Can) {
      this.canToDeliver = can
    }
  
    deliver(choice: Choice): Can {
      return this.canToDeliver
    }  
}

```

Next, identify the duplicate code (hint: in the spec file), and
eliminate it using the ``beforeEach()``

```typescript
  let vendingMachine: VendingMachine;
  beforeEach(() =>{
    vendingMachine = new VendingMachine();
  })
```

Let's configure a different drink

```typescript
  it("delivers Fanta when fizzy orange is selected", () => {
    vendingMachine.configure(Choice.FIZZY_ORANGE, Can.FANTA)
    expect(vendingMachine.deliver(Choice.FIZZY_ORANGE)).to.equal(Can.FANTA)
  })
```

After extending the choice and can types, the test jumps to green.

To make the configuration more similar with the previous test,
we can add a similar line to our current test and vice versa:

```typescript
  it("delivers Fanta when fizzy orange is selected", () => {
    vendingMachine.configure(Choice.COLA, Can.COKE)
    vendingMachine.configure(Choice.FIZZY_ORANGE, Can.FANTA)
    expect(vendingMachine.deliver(Choice.FIZZY_ORANGE)).to.equal(Can.FANTA)
  })
```

However, we must _very carefully_ watch the order in which we configure
the vending machine, as the latest configured can type is returned always.

So let's intentionally reverse these configuration statements now, so that
we are forced to generalize our production code:

```typescript
export class VendingMachine {
    private choiceCanMap: Map<Choice, Can> = new Map<Choice, Can>();

    public configure(choice: Choice, can: Can): void {
      this.choiceCanMap.set(choice, can)
    }
  
    public deliver(choice: Choice): Can {
      if (!this.choiceCanMap.has(choice)) return Can.NOTHING

      return this.choiceCanMap.get(choice) as Can        
    }
}
```

Finally, note that we can actually configure the vending machine 
once for all tests

```typescript
  beforeEach(() =>{
    vendingMachine = new VendingMachine();
    vendingMachine.configure(Choice.FIZZY_ORANGE, Can.FANTA)
    vendingMachine.configure(Choice.COLA, Can.COKE)
  })
```

This makes our first test fail, because it now actually gets 
delivered a can of Coke. But the idea of the first test was to 
test for a non-existing choice, so let's replace the ``Choice.COLA`` 
by ``Choice.BEER``. Now all three tests are green again!

## Delivering cans that cost money

Delivering a can should actually cost money! So asking for a can of coke
should not deliver anything...

```typescript
    it("delivers no can when choice requires money", () => {
        expect(vendingMachine.deliver(Choice.COLA)).to.equal(Can.NOTHING);
    })
```

Again we are facing the riddle: how can we choose a can of coke and have
a can delivered in the first set of tests, and now with the same test no
can at all??

Again, we solve this by configuring the machine to deliver drinks that
cost money, bij adding a parameter to the configure method that specifies
the price in cents:

```typescript
    it("delivers no can when choice requires money", () => {
        vendingMachine.configure(Choice.COLA, Can.COKE, 250);
        expect(vendingMachine.deliver(Choice.COLA)).to.equal(Can.NOTHING);
    })
```

We modify the production code accordingly to make the test pass:

```typescript
export class VendingMachine {
    private choiceCanMap: Map<Choice, Can> = new Map<Choice, Can>()
    private priceInCents: number = 0

    public configure(choice: Choice, can: Can, priceInCents = 0): void {
      this.choiceCanMap.set(choice, can)
      this.priceInCents = priceInCents
    }
  
    public deliver(choice: Choice): Can {
      if (this.choiceCanMap.has(choice) && this.priceInCents == 0) 
        return this.choiceCanMap.get(choice) as Can

      return Can.NOTHING        
    }
}
```

When we enter the required amount of money, we should get our
can of choice again

```typescript
    it("delivers can of choice when required money is inserted", () => {
        vendingMachine.insert(250);
        vendingMachine.configure(Choice.COLA, Can.COKE, 250);
        expect(vendingMachine.deliver(Choice.COLA)).to.equal(Can.COKE);
    })
```

This forces us to modify the implementation like so

```typescript
    private balanceInCents: number = 0

    // ...
    
    public insert(amountInCents: number): void  {
      this.balanceInCents = amountInCents
    }
  
    public deliver(choice: Choice): Can {
      if (this.choiceCanMap.has(choice) && this.priceInCents == this.balanceInCents) 
        return this.choiceCanMap.get(choice) as Can

      return Can.NOTHING        
    }
```

Again, we observe duplication in the specification file, which leads
to a nesting of the ``describe`` statements

```typescript
  describe("that requires drinks to be paid", () => {
    beforeEach(() =>{
      vendingMachine = new VendingMachine();
      vendingMachine.configure(Choice.COLA, Can.COKE, 250);
    })
    
    it("delivers no can when choice requires money", () => {
        expect(vendingMachine.deliver(Choice.COLA)).to.equal(Can.NOTHING);
    })
    
    it("delivers can of choice when required money is inserted", () => {
        vendingMachine.insert(250);
        expect(vendingMachine.deliver(Choice.COLA)).to.equal(Can.COKE);
    })
  })
```

Of course, the equality sign doesn't make sense, as we also 
expect a can of choice when we pay too much

```typescript
    it("delivers can of choice when more than required amount is inserted", () => {
        vendingMachine.insert(300);
        expect(vendingMachine.deliver(Choice.COLA)).to.equal(Can.COKE);
    })
```
This test only requires a minor modification in the production code

```typescript
  deliver(choice) {
      if (this.choiceCanMap.has(choice) && this.priceInCents <= this.balanceInCents) 
        return this.choiceCanMap.get(choice) as Can
```

Obviously, we also must accommodate for different prices for the different drinks:

```typescript
    it("delivers can of Fanta when required amount is inserted", () => {
        vendingMachine.insert(300);
        vendingMachine.configure(Choice.FIZZY_ORANGE, Can.FANTA, 300);
        expect(vendingMachine.deliver(Choice.FIZZY_ORANGE)).to.equal(Can.FANTA);
    })
```

This test jumps to green immediately, but that's because the most recently
configured price is used always. As soon as we move the configuration to 
the ``beforeEach()`` step, the test fails!

So now we need to introduce yet another map, namely a map between choices
and prices.

```typescript
export class VendingMachine {
    private choiceCanMap: Map<Choice, Can> = new Map<Choice, Can>()
    private choicePriceMap: Map<Choice, number> = new Map<Choice, number>()
    private balanceInCents: number = 0

    public configure(choice: Choice, can: Can, priceInCents = 0): void {
      this.choiceCanMap.set(choice, can)
      this.choicePriceMap.set(choice, priceInCents)
    }

    public insert(amountInCents: number): void  {
      this.balanceInCents = amountInCents
    }
  
    public deliver(choice: Choice): Can {
      if (!this.choiceCanMap.has(choice))
          return Can.NOTHING

      let price = this.choicePriceMap.get(choice) as number
      if (price <= this.balanceInCents) 
        return this.choiceCanMap.get(choice) as Can

      return Can.NOTHING        
    }
}
```

Finaly, we expect no more cans after a can has been withdrawn, as our
balance should have shrunk

```typescript
    it("delivers no can after a can has been delivered", () => {
        vendingMachine.insert(250);
        vendingMachine.deliver(Choice.COLA);
        expect(vendingMachine.deliver(Choice.COLA)).to.equal(Can.NOTHING);
    })
```

So after withdrawal of a drink, the balance should be adjusted
accordingly. After some minor refactoring of the deliver method
we arrive at

```typescript
    public deliver(choice: Choice): Can {
      if (!this.choiceCanMap.has(choice))
          return Can.NOTHING

      let price = this.choicePriceMap.get(choice) as number
      if (price > this.balanceInCents) 
        return Can.NOTHING        

      this.balanceInCents -= price
      return this.choiceCanMap.get(choice) as Can
    }
```

# Code smells

## [Data clump](https://refactoring.guru/smells/data-clumps)

It now becomes clear that the ``choiceCanMap`` and ``choicePriceMap`` always
appear together, so let's assign them their own (data) class ``Drawer``

```typescript
class Drawer {
  constructor(public can: Can, public priceInCents: number) {}
}
```

Since the members are publicly accesible, we can directly use them.
However, this immediately leads to another code smell, namely
[feature envy](https://refactoring.guru/smells/feature-envy).

As a first step, we can move the delivery logic into the ``Drawer`` class

```typescript
  public getCan(vendingMachine: VendingMachine) {
    if (this.priceInCents > vendingMachine.balanceInCents)
      return Can.NOTHING
    
    vendingMachine.balanceInCents -= this.priceInCents
    return this.can
  }
```

with which the ``VendingMachine`` simplifies to

```typescript
    public deliver(choice: Choice): Can {
      if (!this.choiceDrawerMap.has(choice))
          return Can.NOTHING

      let drawer = this.choiceDrawerMap.get(choice) as Drawer
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

```typescript
class Cashier {
  constructor(private balanceInCents: number) {}  

  public insert(amountInCents: number) {
    this.balanceInCents += amountInCents
  }

  public doesBalanceAllow(priceInCents: number) {
    return this.balanceInCents >= priceInCents
  }

  public buy(amountInCents: number) {
    this.balanceInCents -= amountInCents
  }
}
```

This means that the ``Drawer`` class is no longer dependent on the
``VendingMachine`` class, but on the ``Cashier`` instead

```typescript
class Drawer {
  // ...

  deliver(cashier) {
    if (!cashier.doesBalanceAllow(this.priceInCents))
      return Can.NOTHING
    
    cashier.buy(this.priceInCents)
    return this.can    
  }
}
```

with which the code simplifies to

```typescript
class Drawer {
  constructor(public can: Can, public priceInCents: number) {}

  deliver(cashier: Cashier) {
    if (!cashier.doesBalanceAllow(this.priceInCents))
      return Can.NOTHING
    
    cashier.buy(this.priceInCents)
    return this.can    
  }
}

export class VendingMachine {
    private choiceDrawerMap: Map<Choice, Drawer> = new Map<Choice, Drawer>()
    private cashier: Cashier = new Cashier()

    public configure(choice: Choice, can: Can, priceInCents = 0): void {
      this.choiceDrawerMap.set(choice, new Drawer(can, priceInCents))
    }

    public insert(amountInCents: number): void  {
      this.cashier.insert(amountInCents)
    }
  
    public deliver(choice: Choice): Can {
      if (!this.choiceDrawerMap.has(choice))
          return Can.NOTHING

      let drawer = this.choiceDrawerMap.get(choice) as Drawer
      return drawer.deliver(this.cashier)
    }
}
```