import unittest

from hamcrest import *

from src.domain.Order import Order
from src.domain.OrderStatus import OrderStatus
from src.useCase.ApprovedOrderCannotBeRejectedError import ApprovedOrderCannotBeRejectedError
from src.useCase.OrderApprovalRequest import OrderApprovalRequest
from src.useCase.OrderApprovalUseCase import OrderApprovalUseCase
from src.useCase.RejectedOrderCannotBeApprovedError import RejectedOrderCannotBeApprovedError
from src.useCase.ShippedOrdersCannotBeChangedError import ShippedOrdersCannotBeChangedError
from test.doubles.StubOrderRepository import StubOrderRepository


class TestOrderApprovalUseCase(unittest.TestCase):
    def setUp(self):
        self.order_repository = StubOrderRepository()
        self.use_case = OrderApprovalUseCase(self.order_repository)

    def test_approved_existing_Order(self):
        initial_order = Order(1)
        self.order_repository.add_order(initial_order)

        request = OrderApprovalRequest(1)
        request.approve()

        self.use_case.run(request)

        saved_order = self.order_repository.get_saved_order()
        assert_that(saved_order.get_status(), is_(OrderStatus.APPROVED))

    def test_rejected_existing_order(self):
        initial_order = Order(1)
        self.order_repository.add_order(initial_order)

        request = OrderApprovalRequest(1)

        self.use_case.run(request)

        saved_order = self.order_repository.get_saved_order()
        assert_that(saved_order.get_status(), is_(OrderStatus.REJECTED))

    def test_cannot_approve_rejected_order(self):
        rejected_order = Order(1)
        rejected_order.reject()
        self.order_repository.add_order(rejected_order)

        request = OrderApprovalRequest(1)
        request.approve()

        assert_that(calling(self.use_case.run).with_args(request), raises(RejectedOrderCannotBeApprovedError))
        assert_that(self.order_repository.get_saved_order(), is_(none()))

    def test_cannot_reject_approved_order(self):
        approved_order = Order(1)
        approved_order.approve()
        self.order_repository.add_order(approved_order)

        request = OrderApprovalRequest(1)

        assert_that(calling(self.use_case.run).with_args(request), raises(ApprovedOrderCannotBeRejectedError))
        assert_that(self.order_repository.get_saved_order(), is_(none()))

    def test_shipped_orders_cannot_be_approved(self):
        shipped_order = Order(1)
        shipped_order.approve()
        shipped_order.shipped()
        self.order_repository.add_order(shipped_order)

        request = OrderApprovalRequest(1)
        request.approve()

        assert_that(calling(self.use_case.run).with_args(request), raises(ShippedOrdersCannotBeChangedError))
        assert_that(self.order_repository.get_saved_order(), is_(none()))

    def test_shipped_orders_cannot_be_rejected(self):
        shipped_order = Order(1)
        shipped_order.approve()
        shipped_order.shipped()
        self.order_repository.add_order(shipped_order)

        request = OrderApprovalRequest(1)

        assert_that(calling(self.use_case.run).with_args(request), raises(ShippedOrdersCannotBeChangedError))
        assert_that(self.order_repository.get_saved_order(), is_(none()))


if __name__ == '__main__':
    unittest.main()
