'use strict';

var expect = require('expect.js');
const { VendingMachine, Choice, Can } = require('../src/VendingMachine.js')

describe("A new vending machine", function() {
    var vending_machine;
  
    beforeEach(function () {
        vending_machine = new VendingMachine()
        vending_machine.configure(Choice.FIZZY_ORANGE, Can.FANTA);
        vending_machine.configure(Choice.COKE, Can.COLA);
    })
    
    it("does not deliver anything", function () {
        expect(vending_machine.deliver(Choice.BEER)).to.equal(Can.NOTHING);
    })
  
    it("delivers Cola when coke is selected", function () {
        expect(vending_machine.deliver(Choice.COKE)).to.equal(Can.COLA);
    })
  
    it("delivers a can of Fanta when choice is fizzy orange", () => {
        expect(vending_machine.deliver(Choice.FIZZY_ORANGE)).to.equal(Can.FANTA);
    })
})
