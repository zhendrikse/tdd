'use strict';

import { expect, assert } from "chai"
import { VendingMachine, Can, Choice } from "../src/vending_machine"

describe("A new VendingMachine", function() {
  let vendingMachine: VendingMachine
  
  beforeEach(() =>{
    vendingMachine = new VendingMachine();
    vendingMachine.configure(Choice.FIZZY_ORANGE, Can.FANTA)
    vendingMachine.configure(Choice.COLA, Can.COKE)
  })
  
  it("delivers nothing when choice does not exist", () => {
    expect(vendingMachine.deliver(Choice.BEER)).to.equal(Can.NOTHING)
  })
  
  it("delivers Cola when coke is selected", () => {
    expect(vendingMachine.deliver(Choice.COLA)).to.equal(Can.COKE)
  })
  
  it("delivers Fanta when fizzy orange is selected", () => {
    expect(vendingMachine.deliver(Choice.FIZZY_ORANGE)).to.equal(Can.FANTA)
  })

  describe("that requires drinks to be paid", () => {
    beforeEach(() =>{
      vendingMachine = new VendingMachine();
      vendingMachine.configure(Choice.COLA, Can.COKE, 250);
      vendingMachine.configure(Choice.FIZZY_ORANGE, Can.FANTA, 300);
    })
    
    it("delivers no can when choice requires money", () => {
        expect(vendingMachine.deliver(Choice.COLA)).to.equal(Can.NOTHING);
    })
    
    it("delivers can of choice when required money is inserted", () => {
        vendingMachine.insert(250);
        expect(vendingMachine.deliver(Choice.COLA)).to.equal(Can.COKE);
    })
    
    it("delivers can of choice when more than required amount is inserted", () => {
        vendingMachine.insert(300);
        expect(vendingMachine.deliver(Choice.COLA)).to.equal(Can.COKE);
    })
    
    it("delivers can of Fanta when required amount is inserted", () => {
        vendingMachine.insert(300);
        expect(vendingMachine.deliver(Choice.FIZZY_ORANGE)).to.equal(Can.FANTA);
    })
    
    it("delivers no can after a can has been delivered", () => {
        vendingMachine.insert(250);
        vendingMachine.deliver(Choice.COLA);
        expect(vendingMachine.deliver(Choice.COLA)).to.equal(Can.NOTHING);
    })
  })
})


