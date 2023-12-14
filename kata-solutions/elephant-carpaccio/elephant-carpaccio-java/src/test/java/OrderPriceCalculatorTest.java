
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;



class OrderPriceCalculatorTest {
    private OrderPriceCalculator calculator;

    @BeforeEach
    void createCalculatorInstance() {
        this.calculator = new OrderPriceCalculator();
        this.calculator.configure("UT", 6.85);
        this.calculator.configure("NV", 8.00);
        this.calculator.configure("TX", 6.25);
    }

    @Test 
    void calculatorShowsStartUpMessage() {
        assertEquals(calculator.getStartUpMessage(), "Welcome to the order price calculator!");
    }

    @Test
    void calculatesTaxesInUtah() {
        assertEquals(calculator.calculateTax(new InputParameters(2, 345.00, "UT")), 47.265);
    }

    @Test
    void calculatesTaxesInNevada() {
        assertEquals(calculator.calculateTax(new InputParameters(2, 345.00, "NV")), 55.20);
    }

    @Test 
    void calculatesTaxesInTexas() {
        assertEquals(calculator.calculateTax(new InputParameters(2, 345.00, "TX")), 43.125);
    }

    @Test 
    void letsUserKnowThatCurrentStateCodeIsUnsupported() {
        UnsupportedStateException thrown = assertThrows(
            UnsupportedStateException.class,
            () -> calculator.calculateTax(new InputParameters(2, 345.00, "99")),
            "Expected calculateTax() to throw, but it didn't"
         );
 
         assertTrue(thrown.getMessage().contains("Unknown state code: '99'"));
    }
}


