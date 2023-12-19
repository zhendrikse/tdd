import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;


class OrderTaxesDiscountsTest {
    private OrderPriceCalculator calculator;

    @BeforeEach
    void createCalculatorInstance() {
        this.calculator = new OrderPriceCalculator();
    }

    @Test
    void calculatesDiscountForUtah() {
        assertEquals(20.70, calculator.calculateDiscountValue(2, 345.00));
    }

    @Test
    void calculatesTaxesBasedOnDiscountForUtah() {
        calculator.configure(State.UT, 6.85, 3);

        assertEquals(45.84705, calculator.calculateTax(new InputParameters(2, 345.00, "UT")), 0.001);
    }
}


