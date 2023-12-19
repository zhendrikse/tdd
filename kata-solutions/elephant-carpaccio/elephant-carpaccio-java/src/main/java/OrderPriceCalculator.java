import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class OrderPriceCalculator {
    private Map<State, Double> stateTaxMap = new HashMap<>();
    private Map<State, Integer> discountsMap = new HashMap<>();

    public String getStartUpMessage() {
        return "Welcome to the order price calculator!";
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

    public static void main(String[] args) {
        final OrderPriceCalculator calculator = new OrderPriceCalculator();
        calculator.configure(State.UT, 6.85, 3);
        calculator.configure(State.NV, 8.00, 5);
        calculator.configure(State.TX, 6.25, 7);
        calculator.configure(State.AL, 4.00, 10);
        calculator.configure(State.CA, 8.25, 15);
        System.out.println(calculator.getStartUpMessage());

        final InputParameters input = calculator.readInputParameters();
        System.out.println(input);
        System.out.println("Grand total: " + calculator.calculateRoundedTotalPrice(input));
    }

    double calculateOrderValue(final int quantity, final double price) {
        return quantity * price;
    }

    double calculateTax(final InputParameters input) {
        if (!stateTaxMap.containsKey(input.state))
            throw new UnsupportedStateException("Unsupported state: '" + input.state + "'");
        
        double orderValue = calculateOrderValue(input.quantity, input.price); 
        if (discountsMap.containsKey(input.state)) 
            orderValue -= calculateDiscountValue(input);

        return orderValue * stateTaxMap.get(input.state) * 0.01;
    }


    public double calculateRoundedTotalPrice(final InputParameters input) {
        return Math.round(100 * (calculateOrderValue(input.quantity, input.price) + calculateTax(input))) / 100.0;
    }

    public void configure(final State state, final double tax) {
        stateTaxMap.put(state, tax);
    }

    double calculateDiscountValue(final InputParameters input) {
        return discountsMap.get(input.state) * 0.01 * input.quantity * input.price;
    }

    public void configure(final State state, final double tax, final int discountInPercent) {
        stateTaxMap.put(state, tax);
        discountsMap.put(state, discountInPercent);
    }
}
