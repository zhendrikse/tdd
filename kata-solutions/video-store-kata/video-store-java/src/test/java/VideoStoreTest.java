import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

public class VideoStoreTest {
    private static final String A_CUSTOMER_NAME = "Fred";
  
    private Customer aCustomer;
  
    @Before
    public void setUp() {
        aCustomer = new Customer(A_CUSTOMER_NAME);
    }

    @Test
    public void testSingleNewReleaseStatement() {
      aCustomer.addRental(new Rental(new NewReleaseMovie("The Cell"), 3));
      Statement statement = new Statement(aCustomer);
      assertEquals("Rental Record for " + A_CUSTOMER_NAME + "\n\tThe Cell\t9.0\nYou owed 9.0\nYou earned 2 frequent renter points\n", statement.toString());
      assertEquals("Frequent renter points", 2, statement.getFrequentRenterPoints());
      assertEquals("Total amount you owed", "9.0", statement.getTotalAmountOwedAsString());
    }

    @Test
    public void testDualNewReleaseStatement() {
      aCustomer.addRental(new Rental(new NewReleaseMovie("The Cell"), 3));
      aCustomer.addRental(new Rental(new NewReleaseMovie("The Tigger Movie"), 3));
      Statement statement = new Statement(aCustomer);
      assertEquals("Rental Record for " + A_CUSTOMER_NAME + "\n\tThe Cell\t9.0\n\tThe Tigger Movie\t9.0\nYou owed 18.0\nYou earned 4 frequent renter points\n", statement.toString());
      assertEquals("Frequent renter points", 4, statement.getFrequentRenterPoints());
      assertEquals("Total amount you owed", "18.0", statement.getTotalAmountOwedAsString());
    }

    @Test
    public void testSingleChildrensStatement() {
      aCustomer.addRental(new Rental(new ChildrensMovie("The Tigger Movie"), 3));
      Statement statement = new Statement(aCustomer);
      assertEquals("Rental Record for " + A_CUSTOMER_NAME + "\n\tThe Tigger Movie\t1.5\nYou owed 1.5\nYou earned 1 frequent renter points\n", statement.toString());
      assertEquals("Frequent renter points", 1, statement.getFrequentRenterPoints());
      assertEquals("Total amount you owed", "1.5", statement.getTotalAmountOwedAsString());
    }

    @Test
    public void testMultipleRegularStatement() {
        aCustomer.addRental(new Rental(new RegularMovie("Plan 9 from Outer Space"), 1));
        aCustomer.addRental(new Rental(new RegularMovie("8 1/2"), 2));
        aCustomer.addRental(new Rental(new RegularMovie("Eraserhead"), 3));
        Statement statement = new Statement(aCustomer);
        assertEquals("Rental Record for " + A_CUSTOMER_NAME + "\n\tPlan 9 from Outer Space\t2.0\n\t8 1/2\t2.0\n\tEraserhead\t3.5\nYou owed 7.5\nYou earned 3 frequent renter points\n", statement.toString());
      assertEquals("Frequent renter points", 3, statement.getFrequentRenterPoints());
      assertEquals("Total amount you owed", "7.5", statement.getTotalAmountOwedAsString());
    }

    private Customer customer;
}