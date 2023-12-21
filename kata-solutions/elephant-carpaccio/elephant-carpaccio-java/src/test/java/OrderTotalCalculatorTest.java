import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;


class OrderTotalCalculatorTest {
    private OrderPriceCalculator calculator;

    @BeforeEach
    void createCalculatorInstance() {
        this.calculator = new OrderPriceCalculator();
        calculator.configureTax(State.UT, 6.85);
        calculator.configureDiscount(1000, 0);
        calculator.configureDiscount(5000, 3);
    }

    @Test 
    void calculatorShowsStartUpMessage() {
        assertEquals("Welcome to the order price calculator!", calculator.getStartUpMessage());
    }

    @Test
    void calculatesOrderValue() {
        assertEquals(690.0, calculator.calculateOrderValue(2, 345.00));
    }
    
    @Test
    void calculatesTotalOrderValue() {
        assertEquals(3575.73525, calculator.calculateGrandTotal(new InputParameters(10, 345.00, "UT")), 0.01);
    }
    
    @Test
    void calculatesRoundedTotalOrderValue() {
        assertEquals(3575.74, calculator.calculateRoundedGrandTotal(new InputParameters(10, 345.00, "UT")), 0.01);
    }

    @Test 
    void letsUserKnowThatStateCodeIsInvalid() {
        assertThrows(
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
 
         assertTrue(thrown.getMessage().contains("Unknown state code: 'NY'"));
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
}


