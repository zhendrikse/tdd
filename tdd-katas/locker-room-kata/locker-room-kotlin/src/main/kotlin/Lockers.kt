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
