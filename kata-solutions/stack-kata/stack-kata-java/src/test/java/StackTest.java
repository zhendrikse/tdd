import com.mscharhag.oleaster.runner.OleasterRunner;
import org.junit.runner.RunWith;
import static com.mscharhag.oleaster.runner.StaticRunnerSupport.*;
import static com.mscharhag.oleaster.matcher.Matchers.*;

@RunWith(OleasterRunner.class)
public class StackTest {
  private Stack myStack;
  private Plate myPlate;
  {
    describe("A new stack", () -> {

      beforeEach(() -> {
        myStack = new Stack();
      });

      it("is empty", () -> {
        expect(myStack.isEmpty()).toBeTrue();
      });
      
      it("throws an exception when a pop operation is applied", () -> {
        expect( () -> { myStack.pop(); } ).toThrow(RuntimeException.class);
      });

    });

    describe("A new stack with one plate pushed", () -> {

      beforeEach(() -> {
        myStack = new Stack();
        myPlate = new Plate("plate1");
        myStack.push(myPlate);
      });

      it("is not empty", () -> {
        expect(myStack.isEmpty()).toBeFalse();
      });

      it("returns the plate after a pop operation", () -> {
        expect(myStack.pop()).toEqual(myPlate);
      });

      it("is empty after a pop operation", () -> {
        myStack.pop();
        expect(myStack.isEmpty()).toBeTrue();
      });

      it("is not empty after an addition push and a subsequent pop", () -> {
         myStack.push(new Plate("plate2"));
         myStack.pop();
         expect(myStack.isEmpty()).toBeFalse();
      });

      it("returns the first plate after an additional push and two pops", () -> {
         Plate plate2 = new Plate("plate2");
         myStack.push(plate2);
        
         myStack.pop();
         Plate returnedPlate = myStack.pop();
        expect(returnedPlate).toEqual(myPlate);
      });
    });

  }
}