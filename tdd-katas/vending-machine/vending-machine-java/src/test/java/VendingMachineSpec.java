import com.mscharhag.oleaster.runner.OleasterRunner;
import org.junit.runner.RunWith;
import static com.mscharhag.oleaster.runner.StaticRunnerSupport.*;
import static com.mscharhag.oleaster.matcher.Matchers.*;

@RunWith(OleasterRunner.class)
public class VendingMachineSpec {
  private VendingMachine vendingMachine;
  
  {
    describe("A vending machine", () -> {

      it("delivers nothing when the machine is choiceless", () -> {
        expect(new VendingMachine().deliver(Choice.BEER)).toEqual(Can.NOTHING);
      });
    });
  }
}