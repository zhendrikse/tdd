import java.util.Scanner;

public class TaxDiscountCalculator {
    static Double calculateTaxFor(Integer numberOfItems, Double pricePerItem, String stateCode) {
        return 6.85;
    }

    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("How many items: ");
            Integer numberOfItems = scanner.nextInt();

            System.out.print("Price item: ");
            Double pricePerItem = scanner.nextDouble();

            System.out.print("Two-letter state code: ");
            String stateCode = scanner.nextLine();

            scanner.nextLine();
            

            System.out.println("The total tax is: " + TaxDiscountCalculator.calculateTaxFor(numberOfItems, pricePerItem, stateCode));
        }
    }
}
