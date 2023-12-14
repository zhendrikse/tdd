
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;



class TaxDiscountCalculatorTest {
    @Test 
    void tax_for_state_utah_with_one_item_of_100_dollars() {
        Double tax = TaxDiscountCalculator.calculateTaxFor(1, 100.0, "UT");
        assertEquals(tax, 6.85);
    }
}


