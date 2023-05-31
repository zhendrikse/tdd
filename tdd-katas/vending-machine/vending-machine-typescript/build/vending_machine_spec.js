"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const vending_machine_1 = require("./vending_machine");
const vending_machine_2 = require("./vending_machine");
const vending_machine_3 = require("./vending_machine");
describe("Vending machine", () => {
    let vendingMachine;
    beforeEach(() => {
        vendingMachine = new vending_machine_1.VendingMachine();
        vendingMachine.configure(vending_machine_2.Choice.FIZZY_ORANGE, vending_machine_3.Can.FANTA);
        vendingMachine.configure(vending_machine_2.Choice.COLA, vending_machine_3.Can.COKE);
    });
    it("delivers nothing when choice does not exist", () => {
        expect(vendingMachine.deliver(vending_machine_2.Choice.BEER)).toEqual(vending_machine_3.Can.NOTHING);
    });
    it("delivers a can of cola when choice is coke", () => {
        expect(vendingMachine.deliver(vending_machine_2.Choice.COLA)).toEqual(vending_machine_3.Can.COKE);
    });
    it("delivers a can of fanta when choice is fizzy orange", () => {
        expect(vendingMachine.deliver(vending_machine_2.Choice.FIZZY_ORANGE)).toEqual(vending_machine_3.Can.FANTA);
    });
    describe("when money is required", () => {
        beforeEach(function () {
            vendingMachine = new vending_machine_1.VendingMachine();
            vendingMachine.configure(vending_machine_2.Choice.COLA, vending_machine_3.Can.COKE, 250);
        });
        it("dispenses nothing when priced coke choice is selected and no coins are inserted", () => {
            expect(vendingMachine.deliver(vending_machine_2.Choice.COLA)).toEqual(vending_machine_3.Can.NOTHING);
        });
        it("dispenses cola when priced coke choice is selected and required coins are inserted", () => {
            vendingMachine.insertCoins(250);
            expect(vendingMachine.deliver(vending_machine_2.Choice.COLA)).toEqual(vending_machine_3.Can.COKE);
        });
        it("dispenses cola when priced coke choice is selected and more coins than required are inserted", () => {
            vendingMachine.insertCoins(350);
            expect(vendingMachine.deliver(vending_machine_2.Choice.COLA)).toEqual(vending_machine_3.Can.COKE);
        });
        it("dispenses Spa Rood when priced water is selected and required coins are inserted", () => {
            vendingMachine.configure(vending_machine_2.Choice.FIZZY_ORANGE, vending_machine_3.Can.FANTA, 150);
            vendingMachine.insertCoins(150);
            expect(vendingMachine.deliver(vending_machine_2.Choice.FIZZY_ORANGE)).toEqual(vending_machine_3.Can.FANTA);
        });
        it("dispenses nothing when priced coke choice is selected twice but coins for one drink are inserted", () => {
            vendingMachine.insertCoins(250);
            vendingMachine.deliver(vending_machine_2.Choice.COLA);
            expect(vendingMachine.deliver(vending_machine_2.Choice.COLA)).toEqual(vending_machine_3.Can.NOTHING);
        });
    });
});
