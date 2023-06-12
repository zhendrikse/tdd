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
  deliver(choice: Choice): Can {
    return Can.NOTHING
  }
}

export {VendingMachine};
export {VendingMachine as vendingMachine};
