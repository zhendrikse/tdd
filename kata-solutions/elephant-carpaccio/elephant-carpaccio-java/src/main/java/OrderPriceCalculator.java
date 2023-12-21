import java.util.Collections;
import java.util.HashMap;
import java.util.TreeMap;
import java.util.Map;
import java.util.Scanner;
import java.util.Map.Entry;

public class OrderPriceCalculator {    
    private Map<State, Double> stateTaxMap = new HashMap<>();
    private Map<Integer, Integer> discountsMap = new TreeMap<>(Collections.reverseOrder());

    String getStartUpMessage() {
        return "Welcome to the order price calculator!";
    }

    double calculateOrderValue(final int quantity, final double price) {
        return quantity * price;
    }

    public void configureDiscount(final int upperLimit, final int percentage) {
        discountsMap.put(upperLimit, percentage);
    }

    public void configureTax(final State state, final double tax) {
        stateTaxMap.put(state, tax);
    }

    
    double calculateTotalOrderValue(final InputParameters input) {
        return calculateOrderValue(input.quantity, input.price);
    }

    public InputParameters readInputParameters() {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("How many items: ");
            Integer numberOfItems = scanner.nextInt();

            System.out.print("Price item: ");
            double pricePerItem = scanner.nextDouble();

            System.out.print("Two-letter state code: ");
            String stateCode = scanner.next();

            return new InputParameters(numberOfItems, pricePerItem, stateCode);
        }
    }

    double calculateDiscountValue(final int quantity, final double price) {
        final double orderValue = calculateOrderValue(quantity, price);
        for (Entry<Integer, Integer> entry : discountsMap.entrySet()) 
            if (orderValue >= entry.getKey()) 
                return 0.01 * entry.getValue() * orderValue;
       
        return 0.0;
    }

    double calculateGrandTotal(final InputParameters input)  {
        return calculateOrderValue(input.quantity, input.price) - calculateDiscountValue(input.quantity, input.price) + calculateTax(input);
    }
    
    double calculateTax(final InputParameters input) {
        if (!stateTaxMap.containsKey(input.state))
            throw new UnsupportedStateException("Unknown state code: '" + input.state + "'");

        final double discountedValue = calculateOrderValue(input.quantity, input.price) - calculateDiscountValue(input.quantity, input.price);
        return discountedValue * stateTaxMap.get(input.state) * 0.01;
    }

    double calculateRoundedGrandTotal(final InputParameters input) {
        return  Math.round(100 * calculateGrandTotal(input)) / 100.0;
    }

    public static void main(String[] args) {
        final OrderPriceCalculator calculator = new OrderPriceCalculator();
        calculator.configureTax(State.UT, 6.85);
        calculator.configureTax(State.NV, 8.00);
        calculator.configureTax(State.TX, 6.25);
        calculator.configureTax(State.AL, 4.00);
        calculator.configureTax(State.CA, 8.25);

        calculator.configureDiscount(1000, 3);
        calculator.configureDiscount(5000, 5);
        calculator.configureDiscount(7000, 7);
        calculator.configureDiscount(10000, 10);
        calculator.configureDiscount(50000, 15);
        
        final InputParameters input = calculator.readInputParameters();

        System.out.println(calculator.getStartUpMessage());
        System.out.println(input);
        System.out.println("Order value: " + calculator.calculateOrderValue(input.quantity, input.price));
        System.out.println("Discount: " + calculator.calculateDiscountValue(input.quantity, input.price));
        System.out.println("Tax amount: " + calculator.calculateTax(input));
        System.out.println("Grand total: " + calculator.calculateRoundedGrandTotal(input));
    }
}
