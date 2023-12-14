public class InputParameters {
    public final int quantity;
    public final double price;
    public final State state;

    public InputParameters(final int quantity, final double price, final String state) {
        if (quantity < 1) throw new IllegalArgumentException("Quantity should be positive");
        if (price < 0) throw new IllegalArgumentException("Price should be positive");

        this.quantity = quantity;
        this.price = price;
        this.state = State.valueOf(state);
    }

    public String toString() {
        return "Quantity: " + quantity + ", Price: " + price + ", State: " + state;
    }
}
