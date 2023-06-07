# Locker room kata

## Description

Imagine a wall with lockers in a locker room. All lockers are centrally opened and closed by a controller, where you can enter a PIN. When a locker is open, it is available and can be locked by entering a PIN. When a locker is closed, it can be opened with the PIN used to lock it. 

### Tentative TODO list

- [ ] locker is unlocked initially
- [ ] locker can be locked by entering a PIN for that locker
- [ ] locker can be unlocked by entering a the correct pin for that locker
- [ ] unlocking fails when pin is incorrect
- [ ] asking state or entering PIN for non existing locker, fails
- [ ] PIN confirm on locking a locker
- [ ] PIN on locked locker can be retried by user
- [ ] unlocking fails after two retries
- [ ] master key opens any locker

## Constraints
- Stateless
- Outside-in

## Code smells
- [Feature envy](https://refactoring.guru/smells/feature-envy)
- [Primitive obsession](https://refactoring.guru/smells/primitive-obsession)

## Techniques
- [Branch by abstraction](https://martinfowler.com/bliki/BranchByAbstraction.html)

  
# Example solution

## Initial wall with lockers

We start by specifying an initial wall with open lockers

```kotlin
@Test
fun anInitialLockerIsUnlocked() {
  var lockers = Lockers.withCapacityOf(2)
  assertThat(lockers.stateOfLocker(lockerNumber = 1))
    .isEqualTo(LockerState.UNLOCKED)
}
```

We can make this succeed by defining a ``Lockers`` class with
```kotlin
class Lockers {
  companion object {
    fun withCapacityOf(numberOfLockers: Int): Lockers = Lockers()
  }

  fun stateOfLocker(lockerNumber: Int): LockerState {
    return LockerState.UNLOCKED
  }
}
```

## Locking a locker with a PIN

Once we provide an open locker with a PIN, we mark it as locked

```kotlin
@Test
fun anUnlockedLockerIsLockedWithAPin() {
  var lockers = Lockers.withCapacityOf(2)
  lockers = lockers.enterPin(lockerNumber = 1, enteredPin = "1234")
  assertThat(lockers.stateOfLocker(1)).isEqualTo(LockerState.LOCKED)
}
```

To make this test pass (given the constraints of the kata), the 
production code could look like this

```kotlin
class Lockers (private val lockerNumber: Int = 0, private val pin: String = "") {
  companion object {
    // ...

  fun stateOfLocker(lockerNumber: Int): LockerState {
    if (pin.isNullOrEmpty()) 
      return LockerState.UNLOCKED
    return LockerState.LOCKED
  }

  fun enterPin(lockerNumber: Int, enteredPin: String): Lockers {
    return Lockers(lockerNumber, enteredPin)
  }
}
```

Finally we can apply the DRY principle in the test class by extracting the ``lockers`` variable as a private member variable.

## Providing the same PIN unlocks

Providing the same PIN, unlocks the locker:

```kotlin
@Test
fun alockedLockerIsUnlockedWithTheCorrectPin() {
  var lockers = Lockers.withCapacityOf(2)
  lockers = lockers.enterPin(lockerNumber = 1, enteredPin = "1234")
  lockers = lockers.enterPin(lockerNumber = 1, enteredPin = "1234")
  assertThat(lockers.stateOfLocker(lockerNumber = 1)).isEqualTo(LockerState.UNLOCKED)
}
```

We can make this pass by adding the following to the ``enterPin()`` method

```kotlin
  if (isOpen(lockerNumber))
    return Lockers(lockerNumber, enteredPin)
``` 

where the ``isOpen()`` private method has been introduced to obtain a more readable version of ``pin.isNullOrEmpty()``.

Of course, we want to enforce that a wrong PIN does _not_ open the locker

```kotlin
  @Test
  fun alockedLockerRemainsLockedWithAnIncorrectPin() {
    var lockers = Lockers.withCapacityOf(2)
    lockers = lockers.enterPin(lockerNumber = 1, enteredPin = "1234")
    lockers = lockers.enterPin(lockerNumber = 1, enteredPin = "9999")
    assertThat(lockers.stateOfLocker(lockerNumber = 1)).isEqualTo(LockerState.LOCKED)
  }
```

To make this pass, we have to add an additional ``if``-statement

```kotlin
fun enterPin(lockerNumber: Int, enteredPin: String): Lockers {
  if (isOpen(lockerNumber))
    return Lockers(lockerNumber, enteredPin)
  if (pin.equals(enteredPin))
    return Lockers(lockerNumber)

  return this
}
```

## Enforcing a specific locker

Obviously, we did not make a distinction between any of the lockers in the locker wall, so the following test should fail

```kotlin
@Test
fun lockingOneLeavesOhtersUnTouched() {
  lockers = lockers.enterPin(lockerNumber = 1, enteredPin = "1234")
  assertThat(lockers.stateOfLocker(lockerNumber = 2)).isEqualTo(LockerState.UNLOCKED)
}
```
In order to make this test pass, we realize we have to make too many changes.

So in a situation like this, we may want to comment out our most recently added test, and perform some prefactoring before we comment in our test again.

Let's first introduce a locker data class

```kotlin
data class Locker(val lockerNumber: Int, val pin:String = "") 
```

and gradually replace all occurrences of the ``lockerNumber`` and ``pin`` variables by wrapping them with the new ``Locker`` class and immediately thereafter extracting the variable again, so ``lockerNumber`` becomes ``Locker(lockerNumber, pin).lockerNumber`` etc.

This results in a prefactored ``Lockers`` class

```kotlin
class Lockers (private val locker: Locker) {
  companion object {
    fun withCapacityOf(numberOfLockers: Int): Lockers = Lockers(locker = Locker(1))
  }

  fun stateOfLocker(lockerNumber: Int): LockerState {
    if (isOpen(lockerNumber))
      return LockerState.UNLOCKED
    return LockerState.LOCKED
  }

  fun enterPin(lockerNumber: Int, enteredPin: String): Lockers {
    if (isOpen(lockerNumber))
      return Lockers(locker = Locker(lockerNumber, enteredPin))

    if (locker.pin.equals(enteredPin))
      return Lockers(locker = Locker(lockerNumber))
    
    return this
  }

  private fun isOpen(lockerNumber: Int): Boolean {
    return locker.pin.isNullOrEmpty()
  }
}
```

Next, we note the [Feature envy](https://refactoring.guru/smells/feature-envy) code smell, once we try to make the pin in the ``Locker`` class private

```kotlin
data class Locker(val lockerNumber: Int = 0, private val pin:String) 
```

So let's move the logic to determine whether the locker is open and the PIN code matching into this class

```kotlin
data class Locker(private val lockerNumber: Int = 0, private val pin:String = "") {
  fun canBeOpenedWith(enteredPin: String): Boolean {
    return enteredPin.equals(pin)
  }  
  
  fun isOpen(): Boolean {
    return pin.isNullOrEmpty()
  }
}
```

In addition, we want to be able enter the PIN on the locker itself, so we extend the locker class by moving that logic into the locker class itself:

```kotlin
data class Locker(private val lockerNumber: Int = 0, private val pin: Pin = "") {
  // ... 

  fun enterPin(enteredPin: Pin): Locker {
    if (isOpen()) {
      return Locker(lockerNumber, enteredPin)
    }
    if (canBeOpenedWith(enteredPin)) 
      return Locker(lockerNumber)
    return this
  }
}
```

Also note that nothing prevented us from making the ``lockerNumber`` variable private as well.

Optionally, we may want to refactor out the [primitive obsession](https://refactoring.guru/smells/primitive-obsession) code smell using e.g. a [type alias](https://www.baeldung.com/kotlin/type-aliases) and/or [optionals](https://typealias.com/guides/java-optionals-and-kotlin-nulls/). 

Finally, we enable our test and make it pass by start adding an additional map to the constructor of the ``Lockers`` class

```kotlin
class Lockers (private val locker: Locker, private val lockers: Map<Int, Locker> = HashMap()) {
  companion object {
    fun withCapacityOf(numberOfLockers: Int): Lockers = 
      Lockers(locker = Locker(1), 
              (0 .. numberOfLockers).map { it to Locker() }.toMap())
  }
```

First we make our test pass by inserting the correct map into the Lockers class 
constructor in the ``enterPin()`` method

```kotlin
  fun enterPin(lockerNumber: Int, enteredPin: Pin): Lockers {
    val lockers = lockers.map { (lckrId, locker) ->
                if (lockerNumber == lckrId)
                  Pair(lckrId, locker.enterPin(enteredPin))
                else
                  Pair(lckrId, locker)
            }.toMap()
    return Lockers(locker.enterPin(enteredPin), lockers)
  }
```

and make the ``stateOfLocker()`` function act on it

```kotlin
  fun stateOfLocker(lockerNumber: Int): LockerState {
    if (lockers[lockerNumber]!!.isOpen()) {
      return LockerState.UNLOCKED
    }
    return LockerState.LOCKED
  }
```

Our test jumps to green! So now we can apply some additional refactoring (e.g. 
the now redundant locker parameter in the constructor of the Lockers class 
can and hence should be taken out) to eventually end up with something similar like

```kotlin
typealias Pin = String

class Lockers (private val lockers: Map<Int, Locker> = HashMap()) {
  companion object {
    fun withCapacityOf(numberOfLockers: Int): Lockers = 
      Lockers((0 .. numberOfLockers).map { it to Locker() }.toMap())
  }

  fun stateOfLocker(lockerNumber: Int): LockerState {
    return lockers[lockerNumber]!!.lockerState()
  }

  fun enterPin(lockerNumber: Int, enteredPin: Pin): Lockers {
    return Lockers(
            lockers = lockers.map { (lckrId, locker) ->
                if (lockerNumber == lckrId)
                  Pair(lckrId, locker.enterPin(enteredPin))
                else
                  Pair(lckrId, locker)
            }.toMap()
    )
  }
}

data class Locker(private val pin:Pin = "") {
  private fun canBeOpenedWith(enteredPin: Pin): Boolean = enteredPin.equals(pin)
  private fun isOpen(): Boolean = pin.isNullOrEmpty()
  fun lockerState(): LockerState = if (isOpen()) LockerState.UNLOCKED else LockerState.LOCKED

  fun enterPin(enteredPin: Pin): Locker {
    if (isOpen())
      return Locker(enteredPin)
    else if (canBeOpenedWith(enteredPin))
      return Locker()
    else // Wrong PIN
      return this
  }
}
```
