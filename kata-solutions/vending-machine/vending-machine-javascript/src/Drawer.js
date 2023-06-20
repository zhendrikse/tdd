"use strict";

const { Can } = require("../src/Can.js");

class Drawer {
  constructor(can, priceInCents) {
    this.can = can;
    this.priceInCents = priceInCents;
  }

  deliver(cashier) {
    if (!cashier.doesBalanceAllow(this.priceInCents)) return Can.NOTHING;

    cashier.buy(this.priceInCents);
    return this.can;
  }
}

module.exports = {
  Drawer: Drawer,
};
