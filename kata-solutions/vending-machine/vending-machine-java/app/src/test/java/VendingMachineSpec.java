import com.mscharhag.oleaster.runner.OleasterRunner;
import org.junit.runner.RunWith;

import static com.mscharhag.oleaster.runner.StaticRunnerSupport.*;
import static com.mscharhag.oleaster.matcher.Matchers.*;

@RunWith(OleasterRunner.class)
public class VendingMachineSpec {
  private VendingMachine vendingMachine;

  {
    beforeEach(() -> {
      vendingMachine = new VendingMachine();
      vendingMachine.configure(Choice.FIZZY_ORANGE, vendingMachine.new Drawer(Can.FANTA));
      vendingMachine.configure(Choice.COLA, vendingMachine.new Drawer(Can.COKE));
    });    
    
    describe("A new vending machine", () -> {
      it("delivers nothing when it is still unconfigured", () -> {
        expect(vendingMachine.deliver(Choice.BEER)).toEqual(Can.NOTHING);
      });
    });
    
    it("delivers Cola when coke is selected", () -> {
      expect(vendingMachine.deliver(Choice.COLA)).toEqual(Can.COKE);
    });
    
    it("delivers Fanta when fizzy orange is selected", () -> {
      expect(vendingMachine.deliver(Choice.FIZZY_ORANGE)).toEqual(Can.FANTA);
    });

    describe("that requires drinks to be paid", () -> {
      beforeEach(() -> {
        vendingMachine = new VendingMachine();
        vendingMachine.configure(Choice.FIZZY_ORANGE, vendingMachine.new Drawer(Can.FANTA, 200));
        vendingMachine.configure(Choice.COLA, vendingMachine.new Drawer(Can.COKE, 250));
      });    
      
      it("delivers nothing when priced choice is coke", () -> {
        expect(vendingMachine.deliver(Choice.COLA)).toEqual(Can.NOTHING);
      });
      
      it("delivers can of choice when required money is inserted", () -> {
        vendingMachine.insert(250);
        expect(vendingMachine.deliver(Choice.COLA)).toEqual(Can.COKE);
      });
      
      it("delivers can of choice when more than required money is inserted", () -> {
        vendingMachine.insert(300);
        expect(vendingMachine.deliver(Choice.COLA)).toEqual(Can.COKE);
      });
      
      it("delivers can of Fanta when required amount is inserted", () -> {
        vendingMachine.insert(200);
        expect(vendingMachine.deliver(Choice.FIZZY_ORANGE)).toEqual(Can.FANTA);
      });
      
      it("delivers no can after a can has been delivered", () -> {
        vendingMachine.insert(200);
        vendingMachine.deliver(Choice.FIZZY_ORANGE);
        expect(vendingMachine.deliver(Choice.FIZZY_ORANGE)).toEqual(Can.NOTHING);
      });
      
    });
    
  }
}
