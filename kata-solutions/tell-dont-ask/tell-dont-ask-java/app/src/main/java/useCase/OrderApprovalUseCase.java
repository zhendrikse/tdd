package useCase;

import domain.Order;
import repository.OrderRepository;

public class OrderApprovalUseCase {
    private final OrderRepository orderRepository;

    public OrderApprovalUseCase(OrderRepository orderRepository) {
        this.orderRepository = orderRepository;
    }

    public void run(OrderApprovalRequest request) {
        final Order order = orderRepository.getById(request.getOrderId());

        if (request.isApproved())
            order.approve();
        else
            order.reject();

        orderRepository.save(order);
    }

}
