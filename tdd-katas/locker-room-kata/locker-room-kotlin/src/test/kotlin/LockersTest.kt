import kotlin.test.*
import org.assertj.core.api.Assertions.*

// [ ] locker is unlocked initially
// [ ] accessing a locker outside of range is a failure
// [ ] locker can be locked by entering a pin for that locker
// [ ] locker can be unlocked by entering a the correct ping for that locker
// [ ] unlocking fails when pin is incorrect
// [ ] unlocking

// Begin met lockers en een globale lock/unlock functionaliteit
// Voordat je per locker test kan doen eerst generaliseren
// - locker data class introduceren
// - feature envy -->  handlePin in locker class
// - maak map met lockers: Map<Int, Locker>
// Nu per locker test
// 

class LockerTest {
  private var lockers = Lockers.withCapacityOf(2)
  
  @Test
  fun anInitialLockerIsUnlocked() {
    assertThat(lockers.stateOfLocker(lockerNumber = 1)).isEqualTo(LockerState.UNLOCKED)
  }

  @Test
  fun anUnlockedLockerIsLockedWithAPin() {
    lockers = lockers.enterPin(lockerNumber = 1, enteredPin = "1234")
    assertThat(lockers.stateOfLocker(lockerNumber = 1)).isEqualTo(LockerState.LOCKED)
  }

  @Test
  fun alockedLockerIsUnlockedWithTheCorrectPin() {
    lockers = lockers.enterPin(lockerNumber = 1, enteredPin = "1234")
    lockers = lockers.enterPin(lockerNumber = 1, enteredPin = "1234")
    assertThat(lockers.stateOfLocker(lockerNumber = 1)).isEqualTo(LockerState.UNLOCKED)
  }

  @Test
  fun alockedLockerRemainsLockedWithAnIncorrectPin() {
    lockers = lockers.enterPin(lockerNumber = 1, enteredPin = "1234")
    lockers = lockers.enterPin(lockerNumber = 1, enteredPin = "9999")
    assertThat(lockers.stateOfLocker(lockerNumber = 1)).isEqualTo(LockerState.LOCKED)
  }
  
  @Test
  fun lockingOneLeavesOhtersUnTouched() {
    lockers = lockers.enterPin(lockerNumber = 1, enteredPin = "1234")
    assertThat(lockers.stateOfLocker(lockerNumber = 2)).isEqualTo(LockerState.UNLOCKED)
  }
  
}

