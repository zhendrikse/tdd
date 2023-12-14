import java.util.Scanner;

public class TaxDiscountCalculator {
    public String getGreeting() {
        return "Hello world";
    }

    private static String calculateTaxFor(Integer numberOfItems, Float pricePerItem, String stateCode) {
        return "0";
    }

    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("How many items: ");
            Integer numberOfItems = scanner.nextInt();

            System.out.print("Price item: ");
            Float pricePerItem = scanner.nextFloat();

            System.out.print("Two-letter state code: ");
            String stateCode = scanner.nextLine();
            

            System.out.println("The total tax is: " + TaxDiscountCalculator.calculateTaxFor(numberOfItems, pricePerItem, stateCode));
        }
    }
}
