# Introduction

Please read the general [introduction to the vending machine kata](../README.md) first!

# Getting started

First,
create an initial .Net kata set-up as described [here](https://github.com/zhendrikse/tdd/tree/master/cookiecutter).

Next, go the newly created project directory and consult
the provided `README.md` in there.

# Implementation instructions

## Delivering cans without cost

Let's first write a specification for a vending machine that delivers
nothing, whatever we ask it to deliver.

<details>
  <summary>Specifying an initial vending machine</summary>

```csharp
    [Fact]
    public void VendingMachineDeliversNothingWhenChoiceIsMade()
    {
        var vendingMachine = new VendingMachine();
        Assert.Equal(Can.NOTHING, vendingMachine.Deliver(Choice.COLA));
    }
```

This fails miserably, as both the delivery method and the
enumerations are not defined. So let's introduce them both in the 
production code.

<details>
  <summary>Faking and cheating to get the test green</summary>

```csharp
namespace Kata;

public class VendingMachine
{
    public Can Deliver(Choice choice)
    {
        return Can.NOTHING;
    }
}
```

and creating enumerations for the cans

```csharp
public enum Can : ushort
{
    [Description("No can")] NOTHING,
    [Description("Can of Coke")] COKE
}
```

and choices:

```csharp
public enum Choice : ushort
{
    [Description("Cola choice")] COLA
}
```

</details>
</details>

We should have our first passing test now.

Let's try to get some coke though!

<details>
  <summary>Specifying an initial choice and can</summary>

```csharp
    [Fact]
    public void VendingMachineDeliversCokeWhenColaChoiceIsMade()
    {
        var vendingMachine = new VendingMachine();
        Assert.Equal(Can.COKE, vendingMachine.Deliver(Choice.COLA));
    }
```
</details>

Before we continue, notice that we have two tests now that are 
completely identical, but expect different results. How do we solve this?

<details>
  <summary>Making the vending machine deliver Cola</summary>
  
We solve this by configuring the vending machine with a choice, so
that we can expect a different outcome.

```csharp
    [Fact]
    public void VendingMachineDeliversCokeWhenColaChoiceIsMade()
    {
        var vendingMachine = new VendingMachine();
        vendingMachine.Configure(Choice.COLA, Can.COKE);
        Assert.Equal(Can.COKE, vendingMachine.Deliver(Choice.COLA));
    }
```

Now the vending machine must be extended just a little bit.

<details>
  <summary>Making the test pass</summary>

```csharp
public class VendingMachine
{
    private Can canOfChoice = Can.NOTHING;
  
    public void Configure(Choice choice, Can can) 
    {
        this.canOfChoice = can;
    }
  
    public Can Deliver(Choice choice)
    {
        return this.canOfChoice;
    }
}
```

Next, identify the duplicate code (hint: in the spec/test file), and
eliminate it using the ``beforeEach()``

```csharp
public class FreeDrinksVendingMachine : IDisposable
{
    private VendingMachine vendingMachine;

    public FreeDrinksVendingMachine()
    {
        vendingMachine = new VendingMachine();
    }

    public void Dispose()
    {
        // vendingMachine = (VendingMachine) null;
    }
```
</details>
</details>


Let's configure a different drink.

<details>
  <summary>Specifying another drink</summary>
  
```csharp
    [Fact]
    public void VendingMachineDeliversFantaWhenFizzyOrangeChoiceIsMade()
    {
        vendingMachine.Configure(Choice.FIZZY_ORANGE, Can.FANTA);
        Assert.Equal(Can.FANTA, vendingMachine.Deliver(Choice.FIZZY_ORANGE));
    }
```

After extending the choice and can types, we can notice that this test
already passes! That is caused by the fact we always deliver the most
recently configured choice. So by extending the configuration in our
test, the test will fail and will force us to generalize the production 
code.

```csharp
    [Fact]
    public void VendingMachineDeliversFantaWhenFizzyOrangeChoiceIsMade()
    {
        vendingMachine.Configure(Choice.FIZZY_ORANGE, Can.FANTA);
        vendingMachine.Configure(Choice.COLA, Can.COKE);
        Assert.Equal(Can.FANTA, vendingMachine.Deliver(Choice.FIZZY_ORANGE));
    }
```

So now we are forced to update the production code.

<details>
  <summary>Making the test pass</summary>
  
```csharp
public class VendingMachine
{
    private Can canOfChoice = Can.NOTHING;
    private Dictionary<Choice, Can> choiceCanMap = new Dictionary<Choice, Can>();

    public void Configure(Choice choice, Can can) 
    {
        canOfChoice = can;
        choiceCanMap[choice] = can;
    }
  
    public Can Deliver(Choice choice)
    {
        if (!choiceCanMap.ContainsKey(choice))
            return Can.NOTHING;
        
        return choiceCanMap[choice];
    }
}
```
</details>

<details>
  <summary>Applying the DRY principle</summary>

Finally, note that we can actually configure the vending machine 
once for all tests

```csharp
    public FreeDrinksVendingMachine()
    {
        vendingMachine = new VendingMachine();
        vendingMachine.Configure(Choice.FIZZY_ORANGE, Can.FANTA);
        vendingMachine.Configure(Choice.COLA, Can.COKE);
    }   

    // ...
```

This makes our first test fail, because it now actually gets 
delivered a can of Coke. But the idea of the first test was to 
test for a non-existing choice, so let's replace the ``Choice.COLA`` 
by ``Choice.BEER``. Now all three tests are green again!
</details>
</details>

## Delivering cans that cost money

Delivering a can should actually cost money! So asking for a can of coke
should not deliver anything.

<details>
  <summary>Paid machine does not deliver can of choice</summary>
  
```java
  it("delivers nothing when priced choice is coke", () -> {
    expect(vendingMachine.deliver(Choice.COKE)).toEqual(Can.NOTHING);
  });
```

Again we are facing the riddle: how can we choose a can of coke and have
a can delivered in the first set of tests, and now with the same test no
can at all??

<details>
  <summary>Solving the riddle once more</summary>

Again, we solve this by configuring the machine to deliver drinks that
cost money, bij adding a parameter to the configure method that specifies
the price in cents:

```java
    it("delivers nothing when priced choice is coke", () -> {
      vendingMachine.configure(Choice.COKE, Can.COLA, 250);
      expect(vendingMachine.deliver(Choice.COKE)).toEqual(Can.NOTHING);
    });
```

We modify the production code accordingly to make the test pass:

```java
public class VendingMachine {
    private Map<Choice, Can> choiceCanMap = new HashMap<Choice, Can>();
    private int priceInCents;
  
    public void configure(final Choice choice, final Can can, final int priceInCents) {
      this.choiceCanMap.put(choice, can);
      this.priceInCents = priceInCents;
    }
  
    public void configure(final Choice choice, final Can can) {
      configure(choice, can, 0);
    }

    public Can deliver(final Choice choice) {
      if (!this.choiceCanMap.containsKey(choice)) return Can.NOTHING;
      
      if (this.priceInCents !=0 ) return Can.NOTHING;
      
      return this.choiceCanMap.get(choice);
    }
}
```
  
</details>
  
</details>


When we enter the required amount of money, we should get our
can of choice again.

<details>
  <summary>Specification when money is inserted.</summary>
    
```java
    it("delivers can of choice when required money is inserted", () -> {
      vendingMachine.configure(Choice.COKE, Can.COLA, 250);
      vendingMachine.insert(250);
      expect(vendingMachine.deliver(Choice.COKE)).toEqual(Can.COLA);
    });

```
This forces us to modify the implementation.

<details>
  <summary>Making the test pass</summary>

```java
    public void insert(final int amountInCents) {
      this.balanceInCents = amountInCents;
    }

    public Can deliver(final Choice choice) {
      if (!choiceCanMap.containsKey(choice)) return Can.NOTHING;
      
      if (priceInCents != balanceInCents ) return Can.NOTHING;
      
      return choiceCanMap.get(choice);
    }
```
</details>

Again, we observe duplication in the specification file, which leads
to a nesting of the `describe` statements.

<details>
  <summary>Applying the DRY principle once more</summary>

```java
    describe("that requires drinks to be paid", () -> {
      beforeEach(() -> {
        vendingMachine = new VendingMachine();
        vendingMachine.configure(Choice.COKE, Can.COLA, 250);
      });    
      
      it("delivers nothing when priced choice is coke", () -> {
        expect(vendingMachine.deliver(Choice.COKE)).toEqual(Can.NOTHING);
      });

      //...
```
    
</details>
</details>

Of course, the equality sign doesn't make sense, as we also 
expect a can of choice when we pay too much.

<details>
  <summary>Paying too much</summary>

```java
  it("delivers can of choice when more than required money is inserted", () -> {
    vendingMachine.insert(300);
    expect(vendingMachine.deliver(Choice.COKE)).toEqual(Can.COLA);
  });
```

This test only requires a minor modification in the production code.

<details>
  <summary>Modification to the production code.</summary>

```java
    public Can deliver(final Choice choice) {
      if (!choiceCanMap.containsKey(choice)) return Can.NOTHING;
      
      if (priceInCents > balanceInCents ) return Can.NOTHING;
```
        
</details>
  
</details>

Obviously, we also must accommodate for different prices for the different drinks:

<details>
  <summary>Accommodating different prices for different drinks</summary>
  
```java
      it("delivers can of Fanta when required amount is inserted", () -> {
        vendingMachine.insert(200);
        vendingMachine.configure(Choice.FIZZY_ORANGE, Can.FANTA, 200);
        expect(vendingMachine.deliver(Choice.FIZZY_ORANGE)).toEqual(Can.FANTA);
      });
```

This test jumps to green immediately, but that's because the most recently
configured price is used always. As soon as we move the configuration to 
the ``beforeEach()`` step, the test fails!

<details>
  <summary>Making the test pass</summary>

  We need to introduce yet another map, namely a map between choices
and prices.

```java
public class VendingMachine {
    private Map<Choice, Can> choiceCanMap = new HashMap<Choice, Can>();
    private Map<Choice, Integer> choicePriceMap = new HashMap<Choice, Integer>();
    private int balanceInCents = 0;
  
    public void configure(final Choice choice, final Can can, final int priceInCents) {
      this.choiceCanMap.put(choice, can);
      this.choicePriceMap.put(choice, priceInCents);
    }
  
    public void configure(final Choice choice, final Can can) {
      configure(choice, can, 0);
    }

    public void insert(final int amountInCents) {
      this.balanceInCents = amountInCents;
    }

    public Can deliver(final Choice choice) {
      if (!choiceCanMap.containsKey(choice)) return Can.NOTHING;

      final int canPrice = choicePriceMap.get(choice);
      if (canPrice > balanceInCents ) return Can.NOTHING;
      
      return choiceCanMap.get(choice);
    }
}
```
  
</details>
</details>

Finaly, we expect no more cans after a can has been withdrawn, as our
balance should have shrunk.

<details>
  <summary>Forcing the balance to shrink.</summary>

```java
  it("delivers no can after a can has been delivered", () -> {
    vendingMachine.insert(200);
    vendingMachine.deliver(Choice.FIZZY_ORANGE);
    expect(vendingMachine.deliver(Choice.FIZZY_ORANGE)).toEqual(Can.NOTHING);
  });
```

<details>
  <summary>Adjusting the balance</summary>
  
So after withdrawal of a drink, the balance should be adjusted
accordingly. After some minor refactoring of the deliver method
we arrive at.

```java
public Can deliver(final Choice choice) {
  if (!choiceCanMap.containsKey(choice)) return Can.NOTHING;

  final int canPrice = choicePriceMap.get(choice);
  if (canPrice > balanceInCents ) return Can.NOTHING;
  
  balanceInCents -= canPrice;
  return choiceCanMap.get(choice);
}
```
</details>
    
</details>

# Code smells

## [Data clump](https://refactoring.guru/smells/data-clumps)

It now becomes clear that the ``choiceCanMap`` and ``choicePriceMap`` always
appear together, so let's assign them their own (data) class ``Drawer``.

<details>
  <summary>Refactoring the data clump code smell</summary>

```java
  public class Drawer {
    public final Can can;
    public final int priceInCents;

    public Drawer(Can can) {
      this(can, 0);
    }

    public Drawer(Can can, int priceInCents) {
      this.can = can;
      this.priceInCents = priceInCents;
    }
  }
```

Obviously, the tests now need to be modified slightly too:

```java
    beforeEach(() -> {
      vendingMachine = new VendingMachine();
      vendingMachine.configure(Choice.FIZZY_ORANGE, vendingMachine.new Drawer(Can.FANTA));
      vendingMachine.configure(Choice.COKE, vendingMachine.new Drawer(Can.COLA));
    });    
```
</details>

Since the members are publicly accesible, we can directly use them.
However, this immediately leads to another code smell, namely
[feature envy](https://refactoring.guru/smells/feature-envy).

<details>
  <summary>Resolving the feature envy code smell</summary>

```java
  public Can getCan(VendingMachine vendingMachine) {
    if (priceInCents > vendingMachine.balanceInCents)
      return Can.NOTHING;
    
      vendingMachine.balanceInCents -= this.priceInCents;
    return can;
  }
```

with which the ``VendingMachine`` simplifies to

```java
  public Can deliver(final Choice choice) {
    if (!this.choiceDrawerMap.containsKey(choice)) return Can.NOTHING;

    return this.choiceDrawerMap.get(choice).getCan(this);
  }
```
  
</details>

As a first step, we can move the delivery logic into the ``Drawer`` class

Note that we have now introduced a new code smell, namely
[inappropriate intimacy](https://refactoring.guru/smells/inappropriate-intimacy), 
as the drawer depends on the vending machine and vice versa.

So let's introduce a kind of cashier that has the responsibility 
of dealing with the transaction(s). To do so in small steps, we
first wrap the balance in the new class ``Cashier``, and gradually
move the logic that goes with it as well.

<details>
  <summary>Resolving the inappropriate intemacy code smell</summary>

```java
  public class Cashier {
    private int balanceInCents = 0;
  
    public void insert(final int amountInCents) {
      balanceInCents += amountInCents;
    }
  
    public boolean doesBalanceAllow(final int priceInCents) {
      return balanceInCents >= priceInCents;
    }
  
    public void buy(final int amountInCents) {
      balanceInCents -= amountInCents;
    }
```

This means that the ``Drawer`` class is no longer dependent on the
``VendingMachine`` class, but on the ``Cashier`` instead

```java
  public class Drawer {
    public final Can can;
    public final int priceInCents;

    public Drawer(Can can) {
      this(can, 0);
    }

    public Drawer(Can can, int priceInCents) {
      this.can = can;
      this.priceInCents = priceInCents;
    }

    public Can deliver(final Cashier cashier) {
      if (!cashier.doesBalanceAllow(priceInCents))
        return Can.NOTHING;
    
      cashier.buy(priceInCents);
      return can;
    }
```

with which the final production code becomes:

```java
public class VendingMachine {
  private Map<Choice, Drawer> choiceDrawerMap = new HashMap<Choice, Drawer>();
  private final Cashier cashier = new Cashier();

  public void configure(Choice choice, Drawer drawer) {
    this.choiceDrawerMap.put(choice, drawer);
  }

  public void insert(int priceInCents) {
    cashier.insert(priceInCents);
  }
  
  public Can deliver(final Choice choice) {
    if (!this.choiceDrawerMap.containsKey(choice)) return Can.NOTHING;

    return this.choiceDrawerMap.get(choice).deliver(cashier);
  }
```

</details>
