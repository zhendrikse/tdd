package useCase;

import domain.Order;
import domain.OrderItem;
import domain.Product;
import repository.OrderRepository;
import repository.ProductCatalog;

public class OrderCreationUseCase {
    private final OrderRepository orderRepository;
    private final ProductCatalog productCatalog;

    public OrderCreationUseCase(OrderRepository orderRepository, ProductCatalog productCatalog) {
        this.orderRepository = orderRepository;
        this.productCatalog = productCatalog;
    }

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
}
