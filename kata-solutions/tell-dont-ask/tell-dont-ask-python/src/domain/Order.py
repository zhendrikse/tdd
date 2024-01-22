from decimal import Decimal

from src.domain.OrderStatus import OrderStatus
from src.domain.OrderItem import OrderItem
from src.useCase.ApprovedOrderCannotBeRejectedError import ApprovedOrderCannotBeRejectedError
from src.useCase.RejectedOrderCannotBeApprovedError import RejectedOrderCannotBeApprovedError
from src.useCase.ShippedOrdersCannotBeChangedError import ShippedOrdersCannotBeChangedError
from src.useCase.OrderCannotBeShippedError import OrderCannotBeShippedError
from src.useCase.OrderCannotBeShippedTwiceError import OrderCannotBeShippedTwiceError

class Order(object):
    def __init__(self, order_id:int, currency:str = "EUR"):
        self._status = OrderStatus.CREATED
        self._items= []
        self._currency= "EUR"
        self._total = Decimal("0.00")
        self._tax = Decimal("0.00")
        self._id = order_id

    def get_total(self):
        return self._total

    def get_currency(self):
        return self._currency

    def get_items(self):
        return self._items

    def get_tax(self):
        return self._tax

    def get_status(self):
        return self._status

    def get_id(self):
        return self._id
      
    def add_order_item(self, item: OrderItem):
        self._items.append(item)
        self._total = self._total + item.get_taxed_amount()
        self._tax= self._tax + item.get_tax()

    def approve(self):
        if self._status is OrderStatus.SHIPPED:
            raise ShippedOrdersCannotBeChangedError()

        if self._status is OrderStatus.REJECTED:
            raise RejectedOrderCannotBeApprovedError()

        self._status = OrderStatus.APPROVED

    def reject(self):
        if self._status is OrderStatus.SHIPPED:
            raise ShippedOrdersCannotBeChangedError()
            
        if self._status is OrderStatus.APPROVED:
            raise ApprovedOrderCannotBeRejectedError()

        self._status = OrderStatus.REJECTED

    def check_shipment(self):
        if self._status is OrderStatus.CREATED or self._status is OrderStatus.REJECTED:
            raise OrderCannotBeShippedError()

        if self._status is OrderStatus.SHIPPED:
            raise OrderCannotBeShippedTwiceError()

    def shipped(self):
        self._status = OrderStatus.SHIPPED
