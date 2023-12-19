import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;


class OrderTaxesDiscountsTest {
    private OrderPriceCalculator calculator;

    @BeforeEach
    void createCalculatorInstance() {
        this.calculator = new OrderPriceCalculator();
        calculator.configure(State.UT, 6.85, 3);
        calculator.configure(State.TX, 6.85, 7);
    }

    @Test
    void calculatesDiscountForUtah() {
        assertEquals(20.70, calculator.calculateDiscountValue(new InputParameters(2, 345.00,  "UT")));
    }

    @Test
    void calculatesTaxesBasedOnDiscountForUtah() {
        assertEquals(45.84705, calculator.calculateTax(new InputParameters(2, 345.00, "UT")), 0.001);
    }

    @Test
    void calculatesTaxesBasedOnDiscountForTexas() {
        assertEquals(43.95645, calculator.calculateTax(new InputParameters(2, 345.00, "TX")), 0.001);
    }

    @Test
    void calculatesTotalPriceBasedOnTaxesAndDiscountForTexas() {
        assertEquals(733.96, calculator.calculateRoundedTotalPrice(new InputParameters(2, 345.00, "TX")));
    }
}


