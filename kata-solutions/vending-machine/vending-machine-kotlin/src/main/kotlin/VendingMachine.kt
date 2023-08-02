enum class Choice(private val description: String) {
  COLA("Cola choice"),
  FIZZY_ORANGE("Fizzy orange choice"),
  WATER("Water choice")
}

enum class Can(private val description: String) {
  NOTHING("No can"),
  COKE("Can of Coke"),
  FANTA("Can of Fanta")
}

class VendingMachine(
  private var choiceCanMap: HashMap<Choice, Can> = HashMap(), 
  private var choicePriceMap: HashMap<Choice, Int> = HashMap(),
  private var balanceInCents: Int = 0) {
  
  fun deliver(choice: Choice): Can {
    if (!choiceCanMap.containsKey(choice)) return Can.NOTHING

    if (choicePriceMap[choice]!! > balanceInCents) return Can.NOTHING

    balanceInCents -= choicePriceMap[choice]!!
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