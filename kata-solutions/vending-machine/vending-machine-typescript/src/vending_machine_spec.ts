import { VendingMachine } from './vending_machine';
import { Choice } from './vending_machine';
import { Can } from './vending_machine';

describe("Vending machine", () => {
  let vendingMachine: VendingMachine;
  beforeEach(() =>{
    vendingMachine = new VendingMachine();
    vendingMachine.configure(Choice.FIZZY_ORANGE, Can.FANTA)
    vendingMachine.configure(Choice.COLA, Can.COKE)
  })

  it("delivers nothing when choice does not exist", () => {
    expect(vendingMachine.deliver(Choice.BEER)).toEqual(Can.NOTHING);
  });

  it("delivers a can of cola when choice is coke", () => {
    expect(vendingMachine.deliver(Choice.COLA)).toEqual(Can.COKE);
  });

  it("delivers a can of fanta when choice is fizzy orange", () => {
    expect(vendingMachine.deliver(Choice.FIZZY_ORANGE)).toEqual(Can.FANTA);
  });

  
  describe("when money is required", () => {
    beforeEach(function() {
      vendingMachine = new VendingMachine()
      vendingMachine.configure(Choice.COLA, Can.COKE, 250)
    })

    it("dispenses nothing when priced coke choice is selected and no coins are inserted", () => {
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

    it("dispenses Spa Rood when priced water is selected and required coins are inserted", () => {
      vendingMachine.configure(Choice.FIZZY_ORANGE, Can.FANTA, 150)
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