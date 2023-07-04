import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class {{ cookiecutter.kata }}Test {
    @Test 
    void appHasAGreeting() {
        {{ cookiecutter.kata }} classUnderTest = new {{ cookiecutter.kata }}();
        assertNotNull(classUnderTest.getGreeting(), "app should have a greeting");
        assertTrue(false);
    }
}
