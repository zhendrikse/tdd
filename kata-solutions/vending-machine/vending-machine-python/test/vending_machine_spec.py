from mamba import description, it, context, before
from expects import expect, be, raise_error, be_true, be_false
from vending_machine import Choice, Can, VendingMachine

with description(VendingMachine) as self:
    with context("A new vending machine"):
        with before.each:
            self.vending_machine = VendingMachine()
            self.vending_machine.configure(Choice.FIZZY_ORANGE, Can.FANTA)
            self.vending_machine.configure(Choice.COKE, Can.COLA)

        with it("does not deliver anything"):
            expect(self.vending_machine.deliver(Choice.BEER)).to(be(Can.NOTHING))

        with it("delivers Cola when coke is selected and configured"):
            expect(self.vending_machine.deliver(Choice.COKE)).to(be(Can.COLA))

        with it("delivers a can of fanta when choice is fizzy orange"):
            expect(self.vending_machine.deliver(Choice.FIZZY_ORANGE)).to(be(Can.FANTA))

        with context("that requires drinks to be paid"):
            with before.each:
                self.vending_machine = VendingMachine()
                self.vending_machine.configure(Choice.COKE, Can.COLA, 250)
                self.vending_machine.configure(Choice.FIZZY_ORANGE, Can.FANTA, 300)

            with it("delivers no can when choice requires money"):
                expect(self.vending_machine.deliver(Choice.COKE)).to(be(Can.NOTHING))

            with it("delivers can of choice when required money is inserted"):
                self.vending_machine.insert(250)
                expect(self.vending_machine.deliver(Choice.COKE)).to(be(Can.COLA))

            with it("delivers can of choice when more than required money is inserted"):
                self.vending_machine.insert(350)
                expect(self.vending_machine.deliver(Choice.COKE)).to(be(Can.COLA))

            with it("delivers can of Fanta when required amount is inserted"):
                self.vending_machine.insert(300)
                expect(self.vending_machine.deliver(Choice.FIZZY_ORANGE)).to(be(Can.FANTA))

            with it("delivers no can after a can has been delivered"):
                self.vending_machine.insert(250)
                self.vending_machine.deliver(Choice.COKE)
                expect(self.vending_machine.deliver(Choice.COKE)).to(be(Can.NOTHING))
