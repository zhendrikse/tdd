package domain;

import java.math.BigDecimal;
import static java.math.RoundingMode.HALF_UP;

public class OrderItem {
    public final Product product;
    public final int quantity;
    public final BigDecimal taxedAmount;
    public final BigDecimal tax;

    public OrderItem(Product product, int quantity) {
        this.product = product;
        this.quantity = quantity;
        this.taxedAmount = product.unitaryTaxedAmount().multiply(BigDecimal.valueOf(quantity)).setScale(2, HALF_UP);
        this.tax = product.unitaryTax().multiply(BigDecimal.valueOf(quantity));
    }
}
