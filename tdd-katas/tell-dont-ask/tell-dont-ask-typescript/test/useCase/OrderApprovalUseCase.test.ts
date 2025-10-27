import Order from "../../src/domain/Order";
import OrderStatus from "../../src/domain/OrderStatus"
import OrderApprovalRequest from "../../src/useCase/OrderApprovalRequest";
import TestOrderRepository from "../doubles/TestOrderRepository";
import OrderApprovalUseCase from "../../src/useCase/OrderApprovalUseCase";
import RejectedOrderCannotBeApprovedException from "../../src/useCase/RejectedOrderCannotBeApprovedException";
import ApprovedOrderCannotBeRejectedException from "../../src/useCase/ApprovedOrderCannotBeRejectedException";
import ShippedOrdersCannotBeChangedException from "../../src/useCase/ShippedOrdersCannotBeChangedException";

describe('OrderApprovalUseCase should', () => {
    let orderRepository: TestOrderRepository;
    let useCase: OrderApprovalUseCase;

    beforeEach(() => {
        orderRepository = new TestOrderRepository();
        useCase = new OrderApprovalUseCase(orderRepository);
    });

    test('approve existing order', () => {
        let initialOrder = new Order();
        initialOrder.status = OrderStatus.CREATED;
        initialOrder.id = 1;
        orderRepository.addOrder(initialOrder);

        let request = new OrderApprovalRequest();
        request.orderId = 1;
        request.approved = true;

        useCase.run(request);

        const savedOrder = orderRepository.getSavedOrder();
        expect(savedOrder.status).toBe(OrderStatus.APPROVED);
    });

    test('reject existing order', () => {
        let initialOrder = new Order();
        initialOrder.status = OrderStatus.CREATED;
        initialOrder.id = 1;
        orderRepository.addOrder(initialOrder);

        let request = new OrderApprovalRequest();
        request.orderId = 1;
        request.approved = false;

        useCase.run(request);

        const savedOrder = orderRepository.getSavedOrder();
        expect(savedOrder.status).toBe(OrderStatus.REJECTED);
    });

    test('not approve rejected order', () => {
        let initialOrder = new Order();
        initialOrder.status = OrderStatus.REJECTED;
        initialOrder.id = 1;
        orderRepository.addOrder(initialOrder);

        let request = new OrderApprovalRequest();
        request.orderId = 1;
        request.approved = true;

        expect(() => {useCase.run(request)}).toThrow(RejectedOrderCannotBeApprovedException);
        expect(orderRepository.getSavedOrder()).toBeUndefined();
    });

    test('not reject approved order', () => {
        let initialOrder = new Order();
        initialOrder.status = OrderStatus.APPROVED;
        initialOrder.id = 1;
        orderRepository.addOrder(initialOrder);

        let request = new OrderApprovalRequest();
        request.orderId = 1;
        request.approved = false;

        expect(() => {useCase.run(request)}).toThrow(ApprovedOrderCannotBeRejectedException);
        expect(orderRepository.getSavedOrder()).toBeUndefined();
    });

    test('not approve shipped orders', () => {
        let initialOrder = new Order();
        initialOrder.status = OrderStatus.SHIPPED;
        initialOrder.id = 1;
        orderRepository.addOrder(initialOrder);

        let request = new OrderApprovalRequest();
        request.orderId = 1;
        request.approved = true;

        expect(() => {useCase.run(request)}).toThrow(ShippedOrdersCannotBeChangedException);
        expect(orderRepository.getSavedOrder()).toBeUndefined();
    });

    test('not reject shipped orders', () => {
        let initialOrder = new Order();
        initialOrder.status = OrderStatus.SHIPPED;
        initialOrder.id = 1;
        orderRepository.addOrder(initialOrder);

        let request = new OrderApprovalRequest();
        request.orderId = 1;
        request.approved = false;

        expect(() => {useCase.run(request)}).toThrow(ShippedOrdersCannotBeChangedException);
        expect(orderRepository.getSavedOrder()).toBeUndefined();
    });

});
