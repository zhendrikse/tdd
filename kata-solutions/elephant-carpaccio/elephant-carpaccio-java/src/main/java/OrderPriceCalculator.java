import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class OrderPriceCalculator {
    private Map<State, Double> stateTaxMap = new HashMap<>();

    public String getStartUpMessage() {
        return "Welcome to the order price calculator!";
    }

    public InputParameters readInputParameters() {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("How many items: ");
            Integer numberOfItems = scanner.nextInt();

            System.out.print("Price item: ");
            Double pricePerItem = scanner.nextDouble();

            System.out.print("Two-letter state code: ");
            String stateCode = scanner.next();

            return new InputParameters(numberOfItems, pricePerItem, stateCode);
        }
    }

    public static void main(String[] args) {
        final OrderPriceCalculator calculator = new OrderPriceCalculator();
        calculator.configure(State.UT, 6.85);
        calculator.configure(State.NV, 8.00);
        calculator.configure(State.TX, 6.25);
        calculator.configure(State.AL, 4.00);
        calculator.configure(State.CA, 8.25);
        System.out.println(calculator.getStartUpMessage());

        final InputParameters input = calculator.readInputParameters();
        System.out.println(input);
        System.out.println("Grand total: " + calculator.calculateRoundedTotalPrice(input));
    }

    Double calculateOrderValue(final int quantity, final double price) {
        return quantity * price;
    }

    Double calculateTax(final InputParameters input) {
        if (!stateTaxMap.containsKey(input.state))
            throw new UnsupportedStateException("Unsupported state: '" + input.state + "'");
        
        return calculateOrderValue(input.quantity, input.price) * stateTaxMap.get(input.state) * 0.01;
    }


    public Double calculateRoundedTotalPrice(final InputParameters input) {
        return Math.round(100 * (calculateOrderValue(input.quantity, input.price) + calculateTax(input))) / 100.0;
    }

    public void configure(final State state, final double tax) {
        stateTaxMap.put(state, tax);
    }

    Double calculateDiscountValue(final InputParameters input) {
        return 0.03 * input.quantity * input.price;
    }

    // public void configure(final State state, final double tax, final int discountInPercent) {
    //     stateTaxMap.put(state, tax);
    // }
}
