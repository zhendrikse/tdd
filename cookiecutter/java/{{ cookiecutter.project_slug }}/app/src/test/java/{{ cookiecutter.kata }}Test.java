{% if cookiecutter.rspec_syntax == "n" %}
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
{% endif %}
{% if cookiecutter.rspec_syntax == "y" %}
import com.mscharhag.oleaster.runner.OleasterRunner;
import org.junit.runner.RunWith;

import static com.mscharhag.oleaster.runner.StaticRunnerSupport.*;
import static com.mscharhag.oleaster.matcher.Matchers.*;
{% endif %}
{% if cookiecutter.rspec_syntax == "n" %}
class {{ cookiecutter.kata }}Test {
    @Test 
    void appHasAGreeting() {
        {{ cookiecutter.kata }} classUnderTest = new {{ cookiecutter.kata }}();
        assertNotNull(classUnderTest.getGreeting(), "app should have a greeting");
        assertTrue(false);
    }
}
{% endif %}
{% if cookiecutter.rspec_syntax == "y" %}
@RunWith(OleasterRunner.class)
public class VendingMachineTest {
  private VendingMachine vendingMachine;
  
  {
    describe("Given a new application", () -> {
      it("greets the user", () -> {
        {{ cookiecutter.kata }} classUnderTest = new {{ cookiecutter.kata }}();
        expect(classUnderTest.getGreeting()).toEqual("app should have a greeting");
        expect(false).toEqual(true);
      });
    });
  }
}
{% endif %}
