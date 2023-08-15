package domain;

import java.math.BigDecimal;

public class Category {
    public final String name;
    public final BigDecimal taxPercentage;

    public Category(String name, BigDecimal taxPercentage) {
        this.name = name;
        this.taxPercentage = taxPercentage;
    }
}
