'use strict';

import { expect, assert } from "chai"
import { VendingMachine, Can, Choice } from "../src/vending_machine"

describe("A new VendingMachine", function() {
  let vendingMachine: VendingMachine
  
  beforeEach(() =>{
    vendingMachine = new VendingMachine();
    vendingMachine.configure(Choice.FizzyOrange, Can.Fanta)
    vendingMachine.configure(Choice.Cola, Can.Coke)
  })
  
  it("delivers nothing when choice does not exist", () => {
    expect(vendingMachine.deliver(Choice.Beer)).to.equal(Can.Nothinbg)
  })
  
  it("delivers Cola when coke is selected", () => {
    expect(vendingMachine.deliver(Choice.Cola)).to.equal(Can.Coke)
  })
  
  it("delivers Fanta when fizzy orange is selected", () => {
    expect(vendingMachine.deliver(Choice.FizzyOrange)).to.equal(Can.Fanta)
  })

  describe("that requires drinks to be paid", () => {
    beforeEach(() =>{
      vendingMachine = new VendingMachine();
      vendingMachine.configure(Choice.Cola, Can.Coke, 250);
      vendingMachine.configure(Choice.FizzyOrange, Can.Fanta, 300);
    })
    
    it("delivers no can when choice requires money", () => {
        expect(vendingMachine.deliver(Choice.Cola)).to.equal(Can.Nothinbg);
    })
    
    it("delivers can of choice when required money is inserted", () => {
        vendingMachine.insert(250);
        expect(vendingMachine.deliver(Choice.Cola)).to.equal(Can.Coke);
    })
    
    it("delivers can of choice when more than required amount is inserted", () => {
        vendingMachine.insert(300);
        expect(vendingMachine.deliver(Choice.Cola)).to.equal(Can.Coke);
    })
    
    it("delivers can of Fanta when required amount is inserted", () => {
        vendingMachine.insert(300);
        expect(vendingMachine.deliver(Choice.FizzyOrange)).to.equal(Can.Fanta);
    })
    
    it("delivers no can after a can has been delivered", () => {
        vendingMachine.insert(250);
        vendingMachine.deliver(Choice.Cola);
        expect(vendingMachine.deliver(Choice.Cola)).to.equal(Can.Nothinbg);
    })
  })
})


