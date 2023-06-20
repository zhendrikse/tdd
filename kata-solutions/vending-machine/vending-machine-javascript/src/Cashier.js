"use strict";

class Cashier {
  constructor() {
    this.balanceInCents = 0;
  }

  insert(amountInCents) {
    this.balanceInCents += amountInCents;
  }

  doesBalanceAllow(priceInCents) {
    return this.balanceInCents >= priceInCents;
  }

  buy(amountInCents) {
    this.balanceInCents -= amountInCents;
  }
}

module.exports = {
  Cashier: Cashier,
};
