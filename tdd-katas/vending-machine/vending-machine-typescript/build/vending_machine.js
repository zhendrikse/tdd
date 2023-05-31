"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.vendingMachine = exports.VendingMachine = exports.Can = exports.Choice = void 0;
var Choice;
(function (Choice) {
    Choice["COLA"] = "Cola choice";
    Choice["FIZZY_ORANGE"] = "Fizzy orange choice";
    Choice["BEER"] = "Beer choice";
})(Choice = exports.Choice || (exports.Choice = {}));
var Can;
(function (Can) {
    Can["NOTHING"] = "No can";
    Can["COKE"] = "Can of coke";
    Can["FANTA"] = "Can of fanta";
})(Can = exports.Can || (exports.Can = {}));
class VendingMachine {
    constructor() {
        this.choiceCanMap = new Map();
        this.choicePriceMap = new Map();
        this.balanceInCents = 0;
    }
    configure(choice, can, priceInCents = 0) {
        this.choiceCanMap.set(choice, can);
        this.choicePriceMap.set(choice, priceInCents);
    }
    deliver(choice) {
        if (!this.choiceCanMap.has(choice))
            return Can.NOTHING;
        const priceOfCan = this.choicePriceMap.get(choice);
        if (priceOfCan <= this.balanceInCents) {
            this.balanceInCents -= priceOfCan;
            return this.choiceCanMap.get(choice);
        }
        return Can.NOTHING;
    }
    insertCoins(amountInCents) {
        this.balanceInCents = amountInCents;
    }
}
exports.VendingMachine = VendingMachine;
exports.vendingMachine = VendingMachine;
