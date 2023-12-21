import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;


class OrderTaxesDiscountsTest {
    private OrderPriceCalculator calculator;

    @BeforeEach
    void createCalculatorInstance() {
        this.calculator = new OrderPriceCalculator();
        calculator.configureTax(State.UT, 6.85);
        calculator.configureTax(State.TX, 6.25);
        calculator.configureDiscount(1000, 3);
        calculator.configureDiscount(5000, 5);
        calculator.configureDiscount(7000, 7);
    }

    @Test
    void calculatesDiscountForOverrOneThousand() {
        assertEquals(103.5, calculator.calculateDiscountValue(10, 345.00), 001);
    }

    @Test
    void calculatesDiscountForUnderOneThousand() {
        assertEquals(0.0, calculator.calculateDiscountValue(2, 345.00), 001);
    }

    @Test
    void calculatesDiscountForOverFiveThousand() {
        assertEquals(345.0, calculator.calculateDiscountValue(20, 345.00), 001);
    }
    
    @Test
    void calculatesDiscountForOverSevenThousand() {
        assertEquals(603.75, calculator.calculateDiscountValue(25, 345.00), 001);
    }
}


