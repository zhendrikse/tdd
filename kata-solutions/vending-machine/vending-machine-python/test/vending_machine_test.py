
from mamba import description, it, context, before
from expects import expect, be, raise_error, be_true, be_false
from src.vending_machine import Choice, Can, VendingMachine

with description(VendingMachine) as self:
  with context("A new vending machine"):
    with before.each:
        self.vending_machine  = VendingMachine()
        self.vending_machine.configure(Choice.FIZZY_ORANGE, Can.FANTA)
        self.vending_machine.configure(Choice.COKE, Can.COLA)
    
    with it("does not deliver anything"):
        expect(self.vending_machine.deliver(Choice.BEER)).to(be(Can.NOTHING))

    with it("delivers Cola when coke is selected and configured"):
        expect(self.vending_machine.deliver(Choice.COKE)).to(be(Can.COLA))
 
    with it("delivers a can of fanta when choice is fizzy orange"):
        expect(self.vending_machine.deliver(Choice.FIZZY_ORANGE)).to(be(Can.FANTA))
