'use strict';

const { Drawer } = require('../src/Drawer.js')
const { Cashier } = require('../src/Cashier.js')
const { Can } = require('../src/Can.js')

class Choice {
  static COKE = "Coke"
  static FIZZY_ORANGE = "Fizzy orange"
  static BEER = "Beer"
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
  VendingMachine: VendingMachine
}

