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
    this.choiceCanMap = new Map();
  }
  
  configure(choice, can) {
    this.choiceCanMap.set(choice, can);
  }
  
  deliver(choice) {
    if (this.choiceCanMap.has(choice))
      return this.choiceCanMap.get(choice)

    return Can.NOTHING
  }
}

module.exports = {
  Can: Can,
  Choice: Choice,
  VendingMachine: VendingMachine
}

