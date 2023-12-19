import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;


class OrderTaxesCalculatorTest {
    private OrderPriceCalculator calculator;

    @BeforeEach
    void createCalculatorInstance() {
        this.calculator = new OrderPriceCalculator();
        this.calculator.configure(State.UT, 6.85);
        this.calculator.configure(State.NV, 8.00);
        this.calculator.configure(State.TX, 6.25);
    }

    @Test
    void calculatesTaxesInUtah() {
        assertEquals(47.265, calculator.calculateTax(new InputParameters(2, 345.00, "UT")));
    }

    @Test
    void calculatesTaxesInNevada() {
        assertEquals(55.20, calculator.calculateTax(new InputParameters(2, 345.00, "NV")));
    }

    @Test 
    void calculatesTaxesInTexas() {
        assertEquals(43.125, calculator.calculateTax(new InputParameters(2, 345.00, "TX")));
    }

    @Test 
    void letsUserKnowThatStateCodeIsInvalid() {
        IllegalArgumentException thrown = assertThrows(
            IllegalArgumentException.class,
            () -> calculator.calculateTax(new InputParameters(2, 345.00, "99")),
            "Expected calculateTax() to throw, but it didn't"
         );
    }

    @Test 
    void letsUserKnowThatStateCodeIsUnsupported() {
        UnsupportedStateException thrown = assertThrows(
            UnsupportedStateException.class,
            () -> calculator.calculateTax(new InputParameters(2, 345.00, "NY")),
            "Expected calculateTax() to throw, but it didn't"
         );
 
         assertTrue(thrown.getMessage().contains("Unsupported state: 'NY'"));
    }

    @Test 
    void letsUserKnowThatNonPositiveQuantityIsUnsupported() {
        IllegalArgumentException thrown = assertThrows(
            IllegalArgumentException.class,
            () -> calculator.calculateTax(new InputParameters(0, 345.00, "UT")),
            "Expected calculateTax() to throw, but it didn't"
         );
 
         assertTrue(thrown.getMessage().contains("Quantity should be positive"));
    }

    @Test 
    void letsUserKnowThatNonPositivePriceIsUnsupported() {
        IllegalArgumentException thrown = assertThrows(
            IllegalArgumentException.class,
            () -> calculator.calculateTax(new InputParameters(1, -345.00, "UT")),
            "Expected calculateTax() to throw, but it didn't"
         );
 
         assertTrue(thrown.getMessage().contains("Price should be positive"));
    }

    @Test
    void calculatesRoundedTotalPrice() {
        assertEquals(733.13, calculator.calculateRoundedTotalPrice(new InputParameters(2, 345.00, "TX")));
    }
}


