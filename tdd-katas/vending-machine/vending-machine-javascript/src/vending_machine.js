 const Choice = {
  COLA: "Cola choice",
  BEER: "Beer choice",
  FIZZY_ORANGE: "Fizzy orange choice"
}

const Can = {
  NOTHING: "Nothing",
  COKE: "Can of coke",
  FANTA: "Can of fanta"
}

class VendingMachine {
  constructor() {
    this.canToDeliver= Can.NOTHING
    this.choiceCanMap = new Map()
  }

  provision(choice, can) {
    this.canToDeliver = can
    this.choiceCanMap.set(choice, can)
  }
  deliver(choice) {
    if (!this.choiceCanMap.has(choice)) return Can.NOTHING
    
    return this.choiceCanMap.get(choice)
  }
}