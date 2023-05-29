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