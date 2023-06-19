
from mamba import description, it, context, before
from expects import expect, be, raise_error, be_true, be_false
from src.vending_machine import Choice, Can, VendingMachine

with description(VendingMachine) as self:
  with context("A new vending machine"):
    with before.each:
        self.vending_machine  = VendingMachine()
    
    with it("does not deliver anything"):
        expect(self.vending_machine.deliver(Choice.COKE)).to(be(Can.NOTHING))

    with it("delivers Cola when coke is selected and configured"):
        self.vending_machine.configure(Choice.COKE, Can.COLA)
        expect(self.vending_machine.deliver(Choice.COKE)).to(be(Can.COLA))
 
