 export const Choice = {
  COLA: "Cola choice",
  BEER: "Beer choice",
  FIZZY_ORANGE: "Fizzy orange choice"
}

export const Can = {
  NOTHING: "Nothing",
  COKE: "Can of coke",
  FANTA: "Can of fanta"
}

export class VendingMachine {
  constructor() {
    this.choiceCanMap = new Map()
    this.choicePriceMap = new Map()
    this.balanceInCents = 0
  }

  provision(choice, can, priceInCents = 0) {
    this.choiceCanMap.set(choice, can)
    this.choicePriceMap.set(choice, priceInCents)
  }

  insertCoins(amountInCents) {
    this.balanceInCents = amountInCents
  }
  
  deliver(choice) {
    if (!this.choiceCanMap.has(choice)) return Can.NOTHING
    var priceOfCan = this.choicePriceMap.get(choice) 
    
    if (priceOfCan > this.balanceInCents) return Can.NOTHING
    this.balanceInCents -= priceOfCan
    return this.choiceCanMap.get(choice)
  }
}