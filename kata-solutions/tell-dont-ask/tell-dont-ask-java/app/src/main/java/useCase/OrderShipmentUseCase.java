package useCase;

import domain.Order;
import repository.OrderRepository;
import service.ShipmentService;

public class OrderShipmentUseCase {
    private final OrderRepository orderRepository;
    private final ShipmentService shipmentService;

    public OrderShipmentUseCase(OrderRepository orderRepository, ShipmentService shipmentService) {
        this.orderRepository = orderRepository;
        this.shipmentService = shipmentService;
    }

    public void run(OrderShipmentRequest request) {
        final Order order = orderRepository.getById(request.getOrderId());

        if (order.canBeShipped()) {
            shipmentService.ship(order);
            order.ship();
            orderRepository.save(order);
        }
    }
}
