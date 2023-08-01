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

class VendingMachine(private var choiceCanMap: HashMap<Choice, Can> = HashMap()) {
  fun deliver(choice: Choice): Can {
    if (!choiceCanMap.containsKey(choice)) return Can.NOTHING

    return choiceCanMap[choice]!!
  } 
  

  fun configure(choice: Choice, can: Can): Unit {
    choiceCanMap.put(choice, can)
  }
}