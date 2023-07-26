# Introduction

Please read the general [introduction to the vending machine](../README.md) first!

# Getting started

First, create an intial Python kata set-up as described [here](https://github.com/zhendrikse/tdd/tree/master/cookiecutter).

Next, go the the newly created project directory and consult
the provided ``README.md`` in there.

# Implementation instructions

## Delivering cans without cost

First write a specification for a vending machine that delivers
nothing, whatever we ask it to deliver.

<details>
<summary>First specification for the vending machine</summary>
  
```python
with description(VendingMachine) as self:
  with context("A new vending machine"):
    with it("does not deliver anything"):
        vending_machine  = VendingMachine()
        expect(vending_machine.deliver(Choice.COKE)).to(be(Can.NOTHING))
```
</details>

Obviously, this test fails miserably, as both the deliver method and the
enumerations are not defined. So let's introduce them both in the 
production code

<details>
<summary>Definition of <code>deliver()</code>, <code>Choice</code> and <code>Can</code> </summary>

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
</details>

We should have our first passing test already!

Next, let's write a test to get a can of coke.

<details>
<summary>Test for a can of coke</summary>

```python
with it("delivers Cola when coke is selected"):
    vending_machine  = VendingMachine()
    expect(vending_machine.deliver(Choice.COKE)).to(be(Can.COLA))
```
</details>

Before we continue, notice that we have two tests now that are 
completely identical, but expect different results. How do we solve this?


<details>
<summary>Solving identical test but expecting different results</summary>

We solve this by configuring the vending machine with a choice, so
that we can expect a different outcome.

```python
    with it("delivers Cola when coke is selected"):
        vending_machine  = VendingMachine()
        vending_machine.configure(Choice.COKE, Can.COLA)
        expect(vending_machine.deliver(Choice.COKE)).to(be(Can.COLA))
```
</details>

Now the vending machine must be modified just a little bit
to make the test pass.

<details>
  <summary>Modification to the production code to make the test pass</summary>

```python
class VendingMachine:
  def __init__(self):
    self._can_of_choice = Can.NOTHING

  def configure(self, choice: Choice, can: Can) -> None:
    self._can_of_choice = can
    
  def deliver(self, choice: Choice) -> Can:
    return self._can_of_choice
```
</details>

Next, identify the duplicate code (hint: in the spec file), and
eliminate it using the ``before.Each:``

<details>
  <summary>Applying the DRY principle</summary>

```python
    with beforeEach:
        self.vending_machine  = VendingMachine()
```
</details>

Configuring a different drink will force us to further
generlize the production code!

<details>
  <summary>Adding a test for yet another type of can</summary>

```python
    with it("delivers a can of fanta when choice is fizzy orange"):
        self.vending_machine.configure(Choice.FIZZY_ORANGE, Can.FANTA)
        expect(self.vending_machine.deliver(Choice.FIZZY_ORANGE)).to(be(Can.FANTA))
```  
</details>


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

```python
    with it("delivers no can when choice requires money"):
        expect(self.vending_machine.deliver(Choice.COKE)).to(be(Can.NOTHING))
```

Again we are facing the riddle: how can we choose a can of coke and have
a can delivered in the first set of tests, and now with the same test no
can at all??

Again, we solve this by configuring the machine to deliver drinks that
cost money, bij adding a parameter to the configure method that specifies
the price in cents:

```python
    with it("delivers no can when choice requires money"):
        self.vending_machine.configure(Choice.COKE, Can.COLA, 250)
        expect(self.vending_machine.deliver(Choice.COKE)).to(be(Can.NOTHING))
```

We modify the production code accordingly to make the test pass:

```python
  def configure(self, choice: Choice, can: Can, price_in_cents: int = 0) -> None:
    self._choice_can_map[choice] = can
    self._price_in_cents = price_in_cents
    
  def deliver(self, choice: Choice) -> Can:
    if not choice in self._choice_can_map:
      return Can.NOTHING
    return self._choice_can_map[choice] if self._price_in_cents == 0 else Can.NOTHING
```

When we enter the required amount of money, we should get our
can of choice again

```python
    with it("delivers can of choice when required money is inserted"):
        self.vending_machine.insert(250)
        self.vending_machine.configure(Choice.COKE, Can.COLA, 250)
        expect(self.vending_machine.deliver(Choice.COKE)).to(be(Can.COLA))
```

This forces us to modify the implementation of the vending machine like so

```python
  def __init__(self) -> None:
    self._choice_can_map: dict[Choice, Can] = {}
    self._price_in_cents = 0
    self._balance_in_cents = 0

  def insert(self, amount_in_cents):
    self._balance_in_cents = amount_in_cents
  
  def configure(self, choice: Choice, can: Can, price_in_cents: int = 0) -> None:
    self._choice_can_map[choice] = can
    self._price_in_cents = price_in_cents
    
  def deliver(self, choice: Choice) -> Can:
    if not choice in self._choice_can_map:
      return Can.NOTHING

    if self._balance_in_cents == self._price_in_cents:
      return self._choice_can_map[choice] 
    
    return Can.NOTHING
```

Again, we observe duplication in the specification file, which leads
to a nesting of the ``context`` statements

```python
    with context("that requires drinks to be paid"):
      with before.each:
          self.vending_machine  = VendingMachine()
          self.vending_machine.configure(Choice.COKE, Can.COLA, 250)
  
      with it("delivers no can when choice requires money"):
          expect(self.vending_machine.deliver(Choice.COKE)).to(be(Can.NOTHING))
   
      with it("delivers can of choice when required money is inserted"):
          self.vending_machine.insert(250)
          expect(self.vending_machine.deliver(Choice.COKE)).to(be(Can.COLA))
```

Of course, the equality sign doesn't make sense, as we also 
expect a can of choice when we pay too much

```python
      with it("delivers can of choice when more than required money is inserted"):
          self.vending_machine.insert(350)
          expect(self.vending_machine.deliver(Choice.COKE)).to(be(Can.COLA))
```

This test only requires a minor modification in the production code

```python
    if self._balance_in_cents >= self._price_in_cents:
      return self._choice_can_map[choice] 
```

Obviously, we also must accommodate for different prices for the different drinks:

```python
      with it("delivers can of Fanta when required amount is inserted"):
          self.vending_machine.insert(300)
          self.vending_machine.configure(Choice.FIZZY_ORANGE, Can.FANTA, 300);
          expect(self.vending_machine.deliver(Choice.FIZZY_ORANGE)).to(be(Can.FANTA))
```

This test jumps to green immediately, but that's because the most recently
configured price is used always. As soon as we move the configuration to 
the ``before.each`` step, the test fails!

So now we need to introduce yet another map, namely a map between choices
and prices.

Finaly, we expect no more cans after a can has been withdrawn, as our
balance should have shrunk

```python
      with it("delivers no can after a can has been delivered"):
          self.vending_machine.insert(250)
          self.vending_machine.deliver(Choice.COKE)
          expect(self.vending_machine.deliver(Choice.COKE)).to(be(Can.NOTHING))
```

So after withdrawal of a drink, the balance should be adjusted
accordingly. After some minor refactoring of the deliver method
we arrive at

```python
  def deliver(self, choice: Choice) -> Can:
    if not choice in self._choice_can_map:
      return Can.NOTHING

    price = self._choice_price_map[choice]
    if self._balance_in_cents >= price:
      self._balance_in_cents -= price
      return self._choice_can_map[choice] 
    
    return Can.NOTHING
  ```

# Code smells

## [Data clump](https://refactoring.guru/smells/data-clumps)

It now becomes clear that the ``_choice_can_map`` and ``_choice_price_map`` always
appear together, so let's assign them their own (data) class ``Drawer``

```python
from dataclasses import dataclass

@dataclass(frozen = True)
class Drawer:
  can: Can
  price_in_cents: int
```

Since the members are publicly accesible, we can directly use them.
However, this immediately leads to another code smell, namely
[feature envy](https://refactoring.guru/smells/feature-envy).

As a first step, we can move the delivery logic into the ``Drawer`` class

```python
  def deliver(self, vending_machine) -> Can:
    if vending_machine._balance_in_cents >= self.price_in_cents:
      vending_machine._balance_in_cents -= self.price_in_cents
      return self.can 
    
    return Can.NOTHING
```

with which the ``VendingMachine`` simplifies to

```python
  def deliver(self, choice: Choice) -> Can:
    if not choice in self._choice_drawer_map:
      return Can.NOTHING

    drawer = self._choice_drawer_map[choice]
    return drawer.deliver(self)
```

Note that we have now introduced a new code smell, namely
[inappropriate intimacy](https://refactoring.guru/smells/inappropriate-intimacy), 
as the drawer depends on the vending machine and vice versa.

So let's introduce a kind of cashier that has the responsibility 
of dealing with the transaction(s). To do so in small steps, we
first wrap the balance in the new class ``Cashier``, and gradually
move the logic that goes with it as well.

```python
class Cashier:
  def __init__(self):
    self._balance_in_cents = 0

  def insert(self, balance_in_cents: int) -> None:
    self._balance_in_cents += balance_in_cents

  def does_balance_allow(self, price_in_cents: int) -> bool:
    return self._balance_in_cents >= price_in_cents

  def buy(self, amount_in_cents: int) -> None:
    self._balance_in_cents -= amount_in_cents
```

This means that the ``Drawer`` class is no longer dependent on the
``VendingMachine`` class, but on the ``Cashier`` instead

```python
@dataclass(frozen = True)
class Drawer:
  can: Can
  price_in_cents: int

  def deliver(self, cashier: Cashier) -> Can:
    if not cashier.does_balance_allow(self.price_in_cents):
      return Can.NOTHING
    
    cashier.buy(self.price_in_cents)
    return self.can     
```