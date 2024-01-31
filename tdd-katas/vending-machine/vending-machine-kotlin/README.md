# Introduction

Please read the general [introduction to the vending machine kata](../README.md) first!

# Getting started

First, create an initial Kotlin kata set-up as described [here](https://github.com/zhendrikse/tdd/tree/master/cookiecutter).

Next, go the newly created project directory and consult
the provided ``README.md`` in there.

# Implementation instructions

## Delivering cans without cost

Let's first write a specification for a vending machine that delivers
nothing, whatever we ask it to deliver.

<details>
  <summary>Specifying an initial vending machine</summary>

```kotlin
  @Test
  fun aNewVendingMachineDeliversNothingWhenColaIsChosen() {
      val vendingMachine = VendingMachine()
      assertEquals(vendingMachine.deliver(Choice.COLA), Can.NOTHING)
  }
```

Obviously, this fails miserably, as the both the deliver method and the
enumerations are not defined. So let's introduce them both in the 
production code.

<details>
  <summary>Faking and cheating to get the test green</summary>

```kotlin
class VendingMachine {
  fun deliver(choice: Choice): Can = Can.NOTHING
}
```

and creating enumerations for the cans

```kotlin
enum class Can(private val description: String) {
  NOTHING("No can")
}
```

and choices:

```kotlin
enum class Choice(private val description: String) {
  COLA("Cola choice")
}
```

</details>
</details>


We should have our first passing test now.

Let's try to get some coke though!


<details>
  <summary>Specifying an initial choice and can</summary>

```kotlin
  @Test
  fun aNewVendingMachineDeliversCokeWhenColaIsChosen() {
      val vendingMachine = VendingMachine()
      assertEquals(vendingMachine.deliver(Choice.COLA), Can.COKE)
  }
```
</details>

Before we continue, notice that we have two tests now that are 
completely identical, but expect different results. How do we solve this?

<details>
  <summary>Making the vending machine deliver Cola</summary>
  
We solve this by configuring the vending machine with a choice, so
that we can expect a different outcome.

```kotlin
  @Test
  fun aNewVendingMachineDeliversCokeWhenColaIsChosen() {
      val vendingMachine = VendingMachine()
      vendingMachine.configure(Choice.COLA, Can.COKE)
      assertEquals(vendingMachine.deliver(Choice.COLA), Can.COKE)
  }
```

Now the vending machine must be extended just a little bit.

<details>
  <summary>Making the test pass</summary>

```kotlin
class VendingMachine(private var canOfChoice: Can = Can.NOTHING) {
  fun deliver(choice: Choice): Can = canOfChoice

  fun configure(choice: Choice, can: Can): Unit {
    canOfChoice = can
  }
}
```

Next, identify the duplicate code (hint: in the spec/test file), and
eliminate it using the ``beforeEach()``

```kotlin
class VendingMachineTest() {
  private var vendingMachine: VendingMachine = VendingMachine()
  
  @BeforeEach
  internal fun initVendingMachine() {
      vendingMachine = VendingMachine()
  }
```
</details>
</details>


Let's configure a different drink.

<details>
  <summary>Specifying another drink</summary>
  
```kotlin
  @Test
  fun aNewVendingMachineDeliversFantaWhenFizzyOrangeIsChosen() {
      vendingMachine.configure(Choice.FIZZY_ORANGE, Can.FANTA)
      assertEquals(vendingMachine.deliver(Choice.FIZZY_ORANGE), Can.FANTA)
  }
```

After extending the choice and can types, we can notice that this test
already passes! That is cause by the fact we always deliver the most
recently configured choice. So by extending the configuration in our
test, the test will fail and will force us to generalize the production 
code.

```java
  @Test
  fun aNewVendingMachineDeliversFantaWhenFizzyOrangeIsChosen() {
      vendingMachine.configure(Choice.FIZZY_ORANGE, Can.FANTA)
      vendingMachine.configure(Choice.COLA, Can.COKE)
      assertEquals(vendingMachine.deliver(Choice.FIZZY_ORANGE), Can.FANTA)
  }
```

So now we are forced to update the production code.

<details>
  <summary>Making the test pass</summary>
  
```kotlin
class VendingMachine(private var choiceCanMap: HashMap<Choice, Can> = HashMap()) {
  fun deliver(choice: Choice): Can {
    if (!choiceCanMap.containsKey(choice)) return Can.NOTHING

    return choiceCanMap[choice]!!
  } 
  

  fun configure(choice: Choice, can: Can): Unit {
    choiceCanMap.put(choice, can)
  }
}
```
</details>

<details>
  <summary>Applying the DRY principle</summary>

Finally, note that we can actually configure the vending machine 
once for all tests

```kotlin
  @BeforeEach
  internal fun initVendingMachine() {
      vendingMachine = VendingMachine()
      vendingMachine.configure(Choice.FIZZY_ORANGE, Can.FANTA)
      vendingMachine.configure(Choice.COLA, Can.COKE)
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
  
```kotlin
  @Test
  fun aPaidVendingMachineDoesNotDeliversCokeWhenColaIsChosen() {
      assertEquals(vendingMachine.deliver(Choice.COLA), Can.NOTHING)
  }
```

Again we are facing the riddle: how can we choose a can of coke and have
a can delivered in the first set of tests, and now with the same test no
can at all??

<details>
  <summary>Solving the riddle once more</summary>

Again, we solve this by configuring the machine to deliver drinks that
cost money, bij adding a parameter to the configure method that specifies
the price in cents:

```kotlin
  @Test
  fun aPaidVendingMachineDoesNotDeliversCokeWhenColaIsChosen() {
    vendingMachine.configure(Choice.COLA, Can.COKE, 250)
    assertEquals(vendingMachine.deliver(Choice.COLA), Can.NOTHING)
  }
```

We modify the production code accordingly to make the test pass:

```kotlin
class VendingMachine(private var choiceCanMap: HashMap<Choice, Can> = HashMap(), private var canPriceInCents: Int = 0) {
  fun deliver(choice: Choice): Can {
    if (!choiceCanMap.containsKey(choice)) return Can.NOTHING

    if (canPriceInCents != 0) return Can.NOTHING

    return choiceCanMap[choice]!!
  } 
  

  fun configure(choice: Choice, can: Can, priceInCents: Int = 0): Unit {
    choiceCanMap.put(choice, can)
    canPriceInCents = priceInCents
  }
}
```
  
</details>
  
</details>


When we enter the required amount of money, we should get our
can of choice again.

<details>
  <summary>Specification when money is inserted.</summary>
    
```kotlin
  @Test
  fun aPaidVendingMachineDeliversCokeWhenColaIsPaid() {
    vendingMachine.configure(Choice.COLA, Can.COKE, 250)
    vendingMachine.insertMoney(250)
    assertEquals(vendingMachine.deliver(Choice.COLA), Can.COKE)
  }
```
This forces us to modify the implementation.

<details>
  <summary>Making the test pass</summary>

```kotlin
  fun deliver(choice: Choice): Can {
    if (!choiceCanMap.containsKey(choice)) return Can.NOTHING

    if (canPriceInCents != balanceInCents) return Can.NOTHING

    return choiceCanMap[choice]!!
  } 
  
  fun insertMoney(amountInCents:Int): Unit {
    balanceInCents = amountInCents
  }
```
</details>

Again, we observe duplication in the specification file, which leads
to a nesting of the ``describe`` statements.

<details>
  <summary>Applying the DRY principle once more</summary>

```kotlin
class PaidDrinksVendingMachineTest() {
    private var vendingMachine: VendingMachine = VendingMachine()
    
    @BeforeEach
    internal fun initVendingMachine() {
        vendingMachine = VendingMachine()
        vendingMachine.configure(Choice.COLA, Can.COKE, 250)
    }

    @Test
    fun aPaidVendingMachineDoesNotDeliversCokeWhenColaIsChosen() {
      assertEquals(vendingMachine.deliver(Choice.COLA), Can.NOTHING)
    }
  
    @Test
    fun aPaidVendingMachineDeliversCokeWhenColaIsPaid() {
      vendingMachine.insertMoney(250)
      assertEquals(vendingMachine.deliver(Choice.COLA), Can.COKE)
    }
  }  
```
    
</details>
</details>

Of course, the equality sign doesn't make sense, as we also 
expect a can of choice when we pay too much.

<details>
  <summary>Paying too much</summary>

```kotlin
    @Test
    fun aPaidVendingMachineDeliversCokeWhenColaIsOverPaid() {
      vendingMachine.insertMoney(300)
      assertEquals(vendingMachine.deliver(Choice.COLA), Can.COKE)
    }
```

This test only requires a minor modification in the production code.

<details>
  <summary>Modification to the production code.</summary>

```kotlin
  fun deliver(choice: Choice): Can {
    if (!choiceCanMap.containsKey(choice)) return Can.NOTHING

    if (canPriceInCents > balanceInCents) return Can.NOTHING
```
        
</details>
  
</details>

Obviously, we also must accommodate for different prices for the different drinks:

<details>
  <summary>Accommodating different prices for different drinks</summary>
  
```kotlin
    @Test
    fun aPaidVendingMachineDeliversFantaWhenFizzyOrangeIsPaid() {
      vendingMachine.insertMoney(200)
      vendingMachine.configure(Choice.FIZZY_ORANGE, Can.FANTA, 200)
      assertEquals(vendingMachine.deliver(Choice.FIZZY_ORANGE), Can.FANTA)
    }
```

This test jumps to green immediately, but that's because the most recently
configured price is used always. As soon as we move the configuration to 
the ``beforeEach()`` step, the test fails!

<details>
  <summary>Making the test pass</summary>

  We need to introduce yet another map, namely a map between choices
and prices.

```kotlin
class VendingMachine(
  private var choiceCanMap: HashMap<Choice, Can> = HashMap(), 
  private var choicePriceMap: HashMap<Choice, Int> = HashMap(),
  private var balanceInCents: Int = 0) {
  
  fun deliver(choice: Choice): Can {
    if (!choiceCanMap.containsKey(choice)) return Can.NOTHING

    if (choicePriceMap[choice]!! > balanceInCents) return Can.NOTHING

    return choiceCanMap[choice]!!
  } 
  
  fun insertMoney(amountInCents:Int): Unit {
    balanceInCents = amountInCents
  }

  fun configure(choice: Choice, can: Can, priceInCents: Int = 0): Unit {
    choiceCanMap.put(choice, can)
    choicePriceMap.put(choice, priceInCents)
  }
}
```
  
</details>
</details>

Finaly, we expect no more cans after a can has been withdrawn, as our
balance should have shrunk.

<details>
  <summary>Forcing the balance to shrink.</summary>

```kotlin
    @Test
    fun aPaidVendingMachineDoesNotDeliverFantaTwiceWhenOneIsPaid() {
      vendingMachine.insertMoney(200)
      vendingMachine.deliver(Choice.FIZZY_ORANGE)
      assertEquals(vendingMachine.deliver(Choice.FIZZY_ORANGE), Can.NOTHING)
    }
```

<details>
  <summary>Adjusting the balance</summary>
  
So after withdrawal of a drink, the balance should be adjusted
accordingly. After some minor refactoring of the deliver method
we arrive at.

```kotlin
  fun deliver(choice: Choice): Can {
    if (!choiceCanMap.containsKey(choice)) return Can.NOTHING

    if (choicePriceMap[choice]!! > balanceInCents) return Can.NOTHING

    balanceInCents -= choicePriceMap[choice]!!
    return choiceCanMap[choice]!!
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
