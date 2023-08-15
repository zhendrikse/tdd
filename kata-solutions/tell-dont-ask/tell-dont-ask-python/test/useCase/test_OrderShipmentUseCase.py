import unittest

from hamcrest import is_, assert_that, calling, raises, none

from src.domain.Order import Order
from src.domain.OrderStatus import OrderStatus
from src.useCase.OrderCannotBeShippedError import OrderCannotBeShippedError
from src.useCase.OrderCannotBeShippedTwiceError import OrderCannotBeShippedTwiceError
from src.useCase.OrderShipmentRequest import OrderShipmentRequest
from src.useCase.OrderShipmentUseCase import OrderShipmentUseCase
from test.doubles.StubOrderRepository import StubOrderRepository
from test.doubles.StubShipmentService import StubShipmentService


class TestOrderShipmentUseCase(unittest.TestCase):
    def setUp(self):
        self.order_repository = StubOrderRepository()
        self.shipment_service = StubShipmentService()
        self.use_case = OrderShipmentUseCase(self.order_repository, self.shipment_service)

    def test_ship_approved_order(self):
        approved_order = Order(1)
        approved_order.approve()
        self.order_repository.add_order(approved_order)

        request = OrderShipmentRequest()
        request.set_order_id(1)

        self.use_case.run(request)

        assert_that(self.order_repository.get_saved_order().get_status(), is_(OrderStatus.SHIPPED))
        assert_that(self.shipment_service.get_shipped_order(), is_(approved_order))

    def test_created_orders_cannot_be_shipped(self):
        initialOrder = Order(1)
        self.order_repository.add_order(initialOrder)

        request = OrderShipmentRequest()
        request.set_order_id(1)

        assert_that(calling(self.use_case.run).with_args(request), raises(OrderCannotBeShippedError))
        assert_that(self.order_repository.get_saved_order(), is_(none()))
        assert_that(self.shipment_service.get_shipped_order(), is_(none()))

    def test_rejected_orders_cannot_be_shipped(self):
        rejected_order = Order(1)
        rejected_order.reject()
        self.order_repository.add_order(rejected_order)

        request = OrderShipmentRequest()
        request.set_order_id(1)

        assert_that(calling(self.use_case.run).with_args(request), raises(OrderCannotBeShippedError))
        assert_that(self.order_repository.get_saved_order(), is_(none()))
        assert_that(self.shipment_service.get_shipped_order(), is_(none()))

    def test_shipped_orders_cannot_be_shipped_again(self):
        shipped_order = Order(1)
        shipped_order.approve()
        shipped_order.shipped()
        self.order_repository.add_order(shipped_order)

        request = OrderShipmentRequest()
        request.set_order_id(1)

        assert_that(calling(self.use_case.run).with_args(request), raises(OrderCannotBeShippedTwiceError))
        assert_that(self.order_repository.get_saved_order(), is_(none()))
        assert_that(self.shipment_service.get_shipped_order(), is_(none()))


if __name__ == '__main__':
    unittest.main()
