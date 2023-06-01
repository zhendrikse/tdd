import {VendingMachine, Can, Choice} from '../src/vending_machine.js';

describe("A vending machine", function() {
  var vendingMachine

  beforeEach(function () {
    vendingMachine = new VendingMachine()
    vendingMachine.provision(Choice.FIZZY_ORANGE, Can.FANTA)
    vendingMachine.provision(Choice.COLA, Can.COKE)
  })

  it("delivers nothing when asked for a non-existing choice", function () {
    expect(vendingMachine.deliver(Choice.BEER)).toEqual(Can.NOTHING)
  })

  it("delivers cola when asked for a can of coke", function () {
    expect(vendingMachine.deliver(Choice.COLA)).toEqual(Can.COKE)
  })

  it("delivers fanta when asked for a can of fizzy orange", function () {
    expect(vendingMachine.deliver(Choice.FIZZY_ORANGE)).toEqual(Can.FANTA)
  })

  describe("When money is required", function() {

    beforeEach(function () {
      vendingMachine.provision(Choice.FIZZY_ORANGE, Can.FANTA, 150)
      vendingMachine.provision(Choice.COLA, Can.COKE, 250)
    })
    
    it("dispenses nothing when priced coke choice is selected and no coins are inserted", function() {
      expect(vendingMachine.deliver(Choice.COLA)).toEqual(Can.NOTHING)
    })
    
    it("dispenses cola when priced coke choice is selected and required coins are inserted", () => {
      vendingMachine.insertCoins(250)
      expect(vendingMachine.deliver(Choice.COLA)).toEqual(Can.COKE)
    })

    it("dispenses cola when priced coke choice is selected and more coins than required are inserted", () => {
      vendingMachine.insertCoins(350)
      expect(vendingMachine.deliver(Choice.COLA)).toEqual(Can.COKE)
    })  
    
    it("dispenses fanta when priced fizzy orange is selected and required coins are inserted", () => {
      vendingMachine.insertCoins(150)
      expect(vendingMachine.deliver(Choice.FIZZY_ORANGE)).toEqual(Can.FANTA)
    })

    it("dispenses nothing when priced coke choice is selected twice but coins for one drink are inserted", () => {
      vendingMachine.insertCoins(250)
      vendingMachine.deliver(Choice.COLA)
      expect(vendingMachine.deliver(Choice.COLA)).toEqual(Can.NOTHING)
    })
  })
})
