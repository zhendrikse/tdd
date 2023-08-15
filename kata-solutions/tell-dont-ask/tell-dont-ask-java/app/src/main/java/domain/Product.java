package domain;

import java.math.BigDecimal;
import static java.math.BigDecimal.valueOf;
import static java.math.RoundingMode.HALF_UP;

public class Product {
    public final String name;
    public final BigDecimal price;
    public final Category category;

    public Product(String name, BigDecimal price, Category category) {
        this.name = name;
        this.price = price;
        this.category = category;
    }

    public BigDecimal unitaryTax() {
        return price.divide(valueOf(100)).multiply(category.taxPercentage).setScale(2, HALF_UP);
    }

    public BigDecimal unitaryTaxedAmount() {
        return price.add(unitaryTax()).setScale(2, HALF_UP);
    }

}