import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;


class OrderTotalCalculatorTest {
    private OrderPriceCalculator calculator;

    @BeforeEach
    void createCalculatorInstance() {
        this.calculator = new OrderPriceCalculator();
    }

    @Test 
    void calculatorShowsStartUpMessage() {
        assertEquals(calculator.getStartUpMessage(), "Welcome to the order price calculator!");
    }

    @Test
    void calculatesOrderValue() {
        assertEquals(690.0, calculator.calculateOrderValue(2, 345.00));
    }
}


