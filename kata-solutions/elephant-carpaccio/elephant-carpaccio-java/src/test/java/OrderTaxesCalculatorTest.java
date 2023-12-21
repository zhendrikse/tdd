import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;


class OrderTaxesCalculatorTest {
    private OrderPriceCalculator calculator;

    @BeforeEach
    void createCalculatorInstance() {
        this.calculator = new OrderPriceCalculator();
        this.calculator.configureTax(State.UT, 6.85);
        this.calculator.configureTax(State.NV, 8.00);
        this.calculator.configureTax(State.TX, 6.25);
    }

    @Test
    void calculatesTaxesInUtah() {
        assertEquals(47.265, calculator.calculateTax(new InputParameters(2, 345.00, "UT")), 0.01);
    }

    @Test
    void calculatesTaxesInNevada() {
        assertEquals(55.20, calculator.calculateTax(new InputParameters(2, 345.00, "NV")), 0.01);
    }

    @Test 
    void calculatesTaxesInTexas() {
        assertEquals(43.125, calculator.calculateTax(new InputParameters(2, 345.00, "TX")), 0.01);
    }

    @Test
    void calculatesTaxesBasedOnDiscountedPrice() {
        calculator.configureDiscount(1000, 3);
        assertEquals(267.72, calculator.calculateTax(new InputParameters(10, 345.00, "NV")), 0.01);
    }
}


