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
```