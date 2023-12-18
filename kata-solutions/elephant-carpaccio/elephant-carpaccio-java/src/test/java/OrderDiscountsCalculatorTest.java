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
        assertEquals(calculator.calculateDiscountValue(new InputParameters(2, 345.00, "UT")), 20.70);
    }
}


