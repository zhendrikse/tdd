import com.mscharhag.oleaster.runner.OleasterRunner;
import org.junit.runner.RunWith;
import static com.mscharhag.oleaster.runner.StaticRunnerSupport.*;
import static com.mscharhag.oleaster.matcher.Matchers.*;

@RunWith(OleasterRunner.class)
public class StackSpec {
  {
    describe("A new stack", () -> {

      it("is empty", () -> {
        expect(true).toBeFalse();
      });
      
    });

  }
}
