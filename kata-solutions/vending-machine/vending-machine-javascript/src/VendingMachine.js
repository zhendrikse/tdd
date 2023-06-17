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

class Cashier {
  constructor() {
    this.balanceInCents = 0
  }  

  insert(amountInCents) {
    this.balanceInCents += amountInCents
  }

  doesBalanceAllow(priceInCents) {
    return this.balanceInCents >= priceInCents
  }

  buy(amountInCents) {
    this.balanceInCents -= amountInCents
  }
}

class Drawer {
  constructor(can, priceInCents) {
    this.can = can
    this.priceInCents = priceInCents
  }

  deliver(cashier) {
    if (!cashier.doesBalanceAllow(this.priceInCents))
      return Can.NOTHING
    
    cashier.buy(this.priceInCents)
    return this.can    
  }
}

class VendingMachine {
  constructor() {
    this.choiceDrawerMap = new Map()
    this.cashier = new Cashier()
  }
  
  configure(choice, can, priceInCents = 0) {
    this.choiceDrawerMap.set(choice, new Drawer(can, priceInCents))
  }

  insert(amountInCents) {
    this.cashier.insert(amountInCents)
  }
  
  deliver(choice) {
    if (!this.choiceDrawerMap.has(choice))
      return Can.NOTHING
    
    let drawer = this.choiceDrawerMap.get(choice)
    return drawer.deliver(this.cashier)
  }
}

module.exports = {
  Can: Can,
  Choice: Choice,
  VendingMachine: VendingMachine
}

