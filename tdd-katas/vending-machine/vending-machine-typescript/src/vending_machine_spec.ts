import { VendingMachine } from './vending_machine';
import { Choice } from './vending_machine';
import { Can } from './vending_machine';

describe("Vending machine", () => {

  it("delivers nothing when choice does not exist", () => {
    expect(new VendingMachine().deliver(Choice.BEER)).toEqual(Can.NOTHING);
  });

})