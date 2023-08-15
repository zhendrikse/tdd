package domain;

import java.math.BigDecimal;
import java.util.List;
import java.util.ArrayList;
import java.util.Currency;
import java.util.Collections;

import useCase.ApprovedOrderCannotBeRejectedException;
import useCase.OrderCannotBeShippedException;
import useCase.OrderCannotBeShippedTwiceException;
import useCase.RejectedOrderCannotBeApprovedException;
import useCase.ShippedOrdersCannotBeChangedException;

import static domain.OrderStatus.CREATED;
import static domain.OrderStatus.REJECTED;
import static domain.OrderStatus.SHIPPED;

public class Order {
    private BigDecimal total;
    private Currency currency;
    private List<OrderItem> items;
    private BigDecimal tax;
    private OrderStatus status;
    private int id;

    public Order(int id) {
        this.total = new BigDecimal("0.00");
        this.currency = Currency.getInstance("EUR");
        this.items = new ArrayList<>();
        this.tax = new BigDecimal("0.00");
        this.status = OrderStatus.CREATED;
        this.id = id;
    }

    public void addOrderItem(OrderItem orderItem) {
        items.add(orderItem);
        tax = tax.add(orderItem.tax);
        total = total.add(orderItem.taxedAmount);
    }

    public BigDecimal getTotal() {
        return total;
    }

    public Currency getCurrency() {
        return currency;
    }

    public List<OrderItem> getItems() {
        return Collections.unmodifiableList(items);
    }

    public BigDecimal getTax() {
        return tax;
    }

    public OrderStatus getStatus() {
        return status;
    }

    public int getId() {
        return id;
    }

    public boolean canBeShipped() {
        if (status.equals(CREATED) || status.equals(REJECTED))
            throw new OrderCannotBeShippedException();

        if (status.equals(SHIPPED))
            throw new OrderCannotBeShippedTwiceException();

        return true;
    }

    public void ship() {
        status = OrderStatus.SHIPPED;
    }

    public void reject() {
        if (status.equals(OrderStatus.SHIPPED)) 
            throw new ShippedOrdersCannotBeChangedException();

        if (status.equals(OrderStatus.APPROVED)) 
            throw new ApprovedOrderCannotBeRejectedException();

        status = OrderStatus.REJECTED;
    }

    public void approve() {
        if (status.equals(OrderStatus.SHIPPED)) 
            throw new ShippedOrdersCannotBeChangedException();

        if (status.equals(OrderStatus.REJECTED)) 
            throw new RejectedOrderCannotBeApprovedException();

        status = OrderStatus.APPROVED;
    }
}
