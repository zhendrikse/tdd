export enum Choice {
  COLA = "Cola choice",
  FIZZY_ORANGE = "Fizzy orange choice",
  BEER = "Beer choice"
}

export enum Can {
  NOTHING = "No can",
  COKE = "Can of coke",
  FANTA = "Can of fanta"
}

class VendingMachine {
    private choiceCanMap: Map<Choice, Can> = new Map<Choice, Can>();
    private choicePriceMap: Map<Choice, number> = new Map<Choice, number>();
    private balanceInCents = 0
  
    configure(choice: Choice, can: Can, priceInCents: number = 0): void {
      this.choiceCanMap.set(choice, can)
      this.choicePriceMap.set(choice, priceInCents)
    }
  
    deliver(choice: Choice): Can {
      if (!this.choiceCanMap.has(choice)) return Can.NOTHING

      const priceOfCan = this.choicePriceMap.get(choice) as number
      if (priceOfCan <= this.balanceInCents) {
        this.balanceInCents -= priceOfCan
        return this.choiceCanMap.get(choice) as Can        
      }
      return Can.NOTHING
    }

    insertCoins(amountInCents: number): void {
      this.balanceInCents = amountInCents
    }
}

export {VendingMachine};
export {VendingMachine as vendingMachine};
