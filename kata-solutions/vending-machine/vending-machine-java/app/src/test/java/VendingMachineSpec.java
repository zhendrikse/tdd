import com.mscharhag.oleaster.runner.OleasterRunner;
import org.junit.runner.RunWith;
import static com.mscharhag.oleaster.runner.StaticRunnerSupport.*;
import static com.mscharhag.oleaster.matcher.Matchers.*;

@RunWith(OleasterRunner.class)
public class VendingMachineSpec {
  private VendingMachine vendingMachine;
  
  {
    describe("A vending machine", () -> {

      beforeEach(() -> {
        vendingMachine = new VendingMachine();
        vendingMachine.provision(Choice.FIZZY_ORANGE, vendingMachine.new Drawer(Can.FANTA));
        vendingMachine.provision(Choice.COLA, vendingMachine.new Drawer(Can.COKE));
      });

      it("delivers nothing when the machine is choiceless", () -> {
        expect(vendingMachine.deliver(Choice.BEER)).toEqual(Can.NOTHING);
      });
      
      it("delivers a can of cola when choice coke exists", () -> {
        expect(vendingMachine.deliver(Choice.COLA)).toEqual(Can.COKE);
      });

      it("delivers a can of fanta when choice fizzy orange exists", () -> {
        expect(vendingMachine.deliver(Choice.FIZZY_ORANGE)).toEqual(Can.FANTA);
      });
    });
             
    describe("A paid vending machine", () -> {

      beforeEach(() -> {
        vendingMachine = new VendingMachine();
        vendingMachine.provision(Choice.FIZZY_ORANGE, vendingMachine.new Drawer(Can.FANTA, 200));
        vendingMachine.provision(Choice.COLA, vendingMachine.new Drawer(Can.COKE, 100));
      });

      it("delivers nothing when priced choice is coke", () -> {
        expect(vendingMachine.deliver(Choice.COLA)).toEqual(Can.NOTHING);
      });

      it("delivers cola when priced choice is coke and exact amount is paid", () -> {
        vendingMachine.insertMoney(100);
        expect(vendingMachine.deliver(Choice.COLA)).toEqual(Can.COKE);
      });

      it("delivers cola when priced choice is coke and more than required amount is paid", () -> {
        vendingMachine.insertMoney(150);
        expect(vendingMachine.deliver(Choice.COLA)).toEqual(Can.COKE);
      });

      it("delivers nothing when priced choice is fizzy orange and cola amount is paid", () -> {
        vendingMachine.insertMoney(100);
        expect(vendingMachine.deliver(Choice.FIZZY_ORANGE)).toEqual(Can.NOTHING);
      });

      it("delivers nothing when priced choice is 2 x coke and one amount is paid", () -> {
        vendingMachine.insertMoney(100);
        vendingMachine.deliver(Choice.COLA);
        expect(vendingMachine.deliver(Choice.COLA)).toEqual(Can.NOTHING);
      });
    });
  }
}