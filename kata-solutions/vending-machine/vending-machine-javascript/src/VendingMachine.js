'use strict';

class Choice {
  static COKE = "Coke"
  static FIZZY_ORANGE = "Fizzy orange"
  static BEER = "Beer"
}

class Can {
  static NOTHING = "No can"
  static FANTA = "Can of Fanta"
  static COLA = "Can of Cola"
}

class VendingMachine {
  constructor() {
    this.choiceCanMap = new Map()
    this.choicePriceMap = new Map()
    this.balanceInCents = 0
  }
  
  configure(choice, can, priceInCents = 0) {
    this.priceInCents = priceInCents
    this.choiceCanMap.set(choice, can)
    this.choicePriceMap.set(choice, priceInCents)
  }

  insert(priceInCents) {
    this.balanceInCents = priceInCents
  }
  
  deliver(choice) {
    var price = this.choicePriceMap.get(choice)
    if (!this.choiceCanMap.has(choice) || price > this.balanceInCents) 
      return Can.NOTHING

    this.balanceInCents -= price
    return this.choiceCanMap.get(choice)
  }
}

module.exports = {
  Can: Can,
  Choice: Choice,
  VendingMachine: VendingMachine
}

