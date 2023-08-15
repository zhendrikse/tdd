## Make [OrderItem.java](app/src/main/java/domain/OrderItem.java) a [value object](https://medium.com/swlh/value-objects-to-the-rescue-28c563ad97c6)

Make [OrderItem.java](app/src/main/java/domain/OrderItem.java) a value object and modify [OrderCreationUseCase.java](app/src/main/java/useCase/OrderCreationUseCase.java) and
[OrderCreationUseCaseTest.java](app/src/test/java/useCase/OrderCreationUseCaseTest.java) and
accordingly.

<details>
<summary>Making <code>OrderItem.java</code> a value object</summary>

```java
public class OrderItem {
    public final Product product;
    public final int quantity;
    public final BigDecimal taxedAmount;
    public final BigDecimal tax;

    public OrderItem(Product product, int quantity, BigDecimal tax, BigDecimal taxedAmount) {
        this.product = product;
        this.quantity = quantity;
        this.taxedAmount = taxedAmount;
        this.tax = tax;
    }
}
```
</details>

## Make [Category.java](app/src/main/java/domain/Category.py) a [value object](https://medium.com/swlh/value-objects-to-the-rescue-28c563ad97c6)

Make [Category.java](app/src/main/java/domain/Category.java) a value object and modify [OrderCreationUseCaseTest.java](app/src/test/java/useCase/OrderCreationUseCaseTest.java) accordingly.

<details>
<summary>Making <code>Category.java</code> a value object</summary>

```java
public class Category {
    public final String name;
    public final BigDecimal taxPercentage;

    public Category(String name, BigDecimal taxPercentage) {
        this.name = name;
        this.taxPercentage = taxPercentage;
    }
}
```
</details>

## Make [Product.java](app/src/main/java/domain/Product.java) a [value object](https://medium.com/swlh/value-objects-to-the-rescue-28c563ad97c6)

Make [Product.py](app/src/main/java/domain/Product.java) a value object and modify [OrderCreationUseCaseTest.java](app/src/test/java/useCase/OrderCreationUseCaseTest.java) accordingly.


<details>
<summary>Making <code>Product.java</code> a value object</summary>

```java
public class Product {
    public final String name;
    public final BigDecimal price;
    public final Category category;

    public Product(String name, BigDecimal price, Category category) {
        this.name = name;
        this.price = price;
        this.category = category;
    }
}
```
</details>

## Remove setters from [Order.java](app/src/main/java/domain/Order.java)

1. Move the approve logic from [OrderApprovalUseCase.java](app/src/main/java/useCase/OrderApprovalUseCase.java) 
   to [Order.java](app/src/main/java/domain/Order.py) by first extracting the `request.is_approved()` 
   into a separate variable and then using the extract-method refactoring.
   <details>
   <summary>Moving the approval logic to <code>Order.java</code></summary>

   ```java
    public void approve(final boolean orderIsApproved) {
        if (status.equals(OrderStatus.SHIPPED)) 
            throw new ShippedOrdersCannotBeChangedException();

        if (orderIsApproved && status.equals(OrderStatus.REJECTED)) 
            throw new RejectedOrderCannotBeApprovedException();

        if (!orderIsApproved && status.equals(OrderStatus.APPROVED)) 
            throw new ApprovedOrderCannotBeRejectedException();

        status = orderIsApproved ? OrderStatus.APPROVED : OrderStatus.REJECTED;
    }
   ```
   </details>

2. Extract reject logic from approve method in [Order.java](app/src/main/java/domain/Order.java)
   <details>
   <summary>Moving the rejection logic to <code>Order.java</code></summary>

   ```java
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
   ```
   </details>

3. Create order constructor in [Order.java](app/src/main/java/domain/Order.java).
   <details>
   <summary>Create an order constructor in <code>Order.java</code></summary>

   ```java
    public Order(int id, OrderStatus status) {
        this.total = new BigDecimal("0.00");
        this.currency = "EUR";
        this.items = new ArrayList<>();
        this.tax = new BigDecimal("0.00");
        this.status = status;
        this.id = id;
    }
   ```
   </details>

   and use it in [OrderCreationUseCase.java](app/src/main/java/useCase/OrderCreationUseCase.java) and _all_ test cases. The `setId()` can now be removed from [Order.java](app/src/main/java/domain/Order.java).

4. Create shipping methods in [Order.java](app/src/main/java/domain/Order.java).
   <details>
   <summary>Creation of shipping methods <code>Order.java</code></summary>

   ```java
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
   ```

   so that [OrderShipmentUseCase.java](app/src/main/java/useCase/OrderShipmentUseCase.java) becomes:
  
   ```java
    public void run(OrderShipmentRequest request) {
        final Order order = orderRepository.getById(request.getOrderId());

        if (order.canBeShipped()) {
            shipmentService.ship(order);
            order.ship();
            orderRepository.save(order);
        }
    }
   ```
   </details>

5. Remove the order status paramenter from the constructor of `Order.java` and modify the 
   [OrderApprovalUseCaseTest.java](app/src/test/java/useCase/OrderApprovalUseCaseTest.java)
   and [OrderShipmentUseCaseTest.java](app/src/test/java/useCase/OrderShipmentUseCasetest.java) accordingly. 
   The `OrderStatus.CREATED` can be removed, the rejected and shipped orders have to be 
   created by mimicking the workflow from approved to shipped.

   <details>
   <summary>Mimicking the flow in the test cases</summary>

   ```java
    Order initialOrder = new Order(1);
    initialOrder.approve();
    initialOrder.ship();
   ```
   </details>
   
   Finally, remove the `setStatus()` and `setCurrency()` methods from
   [Order.java](app/src/main/java/domain/Order.java).

7. Remove `setItems()` in [Order.java](app/src/main/java/domain/Order.java)

   <details>
   <summary>Steps to remove the <code>setItems()</code> in <code>Order.java</code></summary>


   - Create an `addOrderItem()` method in [Order.java](app/src/main/java/domain/Order.java):

    ```java
    public void addOrderItem(OrderItem orderItem) {
        items.add(orderItem);
        tax = tax.add(orderItem.tax);
        total = total.add(orderItem.taxedAmount);
    }
    ```  
    and use it in the [OrderCreationUseCase](app/src/main/java/useCase/OrderCreationUseCase.java).

   - Create the following methods in [Product.java](app/src/main/java/domain/Product.java):

    ```java
    public BigDecimal unitaryTax() {
        return price.divide(valueOf(100)).multiply(category.taxPercentage).setScale(2, HALF_UP);
    }

    public BigDecimal unitaryTaxedAmount() {
        return price.add(unitaryTax()).setScale(2, HALF_UP);
    }
    ```

   - Next, in [OrderItem.java](app/src/main/java/domain/OrderItem.java) modify the constructor like so:

    ```java
    public OrderItem(Product product, int quantity) {
        this.product = product;
        this.quantity = quantity;
        this.taxedAmount = product.unitaryTaxedAmount().multiply(BigDecimal.valueOf(quantity)).setScale(2, HALF_UP);
        this.tax = product.unitaryTax().multiply(BigDecimal.valueOf(quantity));
    }
    ```
  
    The `run()` method in [OrderCreationUseCase.java](app/src/main/java/useCase/OrderCreationUseCase.py) now simplifies to:
    ```java
    public void run(SellItemsRequest request) {
        Order order = new Order(1);

        for (SellItemRequest itemRequest : request.getRequests()) {
            Product product = productCatalog.getByName(itemRequest.getProductName());

            if (product == null) 
                throw new UnknownProductException();
                
            order.addOrderItem(new OrderItem(product, itemRequest.getQuantity()));
        }

        orderRepository.save(order);
    }
    ``` 
    The tax arguments can now be removed from the `OrderItem` constructor.

   - Finally, the `set_items()`, `set_total()`, and `set_tax()` can be removed from [Order.java](app/src/main/java/domain/Order.java).
</details>

7. You may want to get rid of the primitive obsession code smell by replacing the
   "stringly typed" currency by `java.util.Currency`.

8. You may want to return an unmodifyable list in
   [OrderItem.java](app/src/main/java/OrderItem.java)
   ```java
    public List<OrderItem> getItems() {
        return Collections.unmodifiableList(items);
    }
    ```