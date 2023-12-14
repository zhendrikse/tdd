public class InputParameters {
    public final int quantity;
    public final double price;
    public final String state;

    public InputParameters(final int quantity, final double price, final String state) {
        this.quantity = quantity;
        this.price = price;
        this.state = state;
    }

    public String toString() {
        return "Quantity: " + quantity + ", Price: " + price + ", State: " + state;
    }
}
