
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;



class TaxDiscountCalculatorTest {
    @Test 
    void appHasAGreeting() {
        TaxDiscountCalculator classUnderTest = new TaxDiscountCalculator();
        assertNotNull(classUnderTest.getGreeting(), "app should have a greeting");
        assertTrue(true);
    }
}


