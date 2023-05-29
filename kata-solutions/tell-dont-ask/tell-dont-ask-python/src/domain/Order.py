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
        self.status = OrderStatus.CREATED
        self.items= []
        self.currency= "EUR"
        self.total = Decimal("0.00")
        self.tax = Decimal("0.00")
        self.id = order_id

    def get_total(self):
        return self.total

    def get_currency(self):
        return self.currency

    def get_items(self):
        return self.items

    def get_tax(self):
        return self.tax

    def get_status(self):
        return self.status

    def get_id(self):
        return self.id
      
    def add_order_item(self, item: OrderItem):
        self.items.append(item)
        self.total = self.total + item.get_taxed_amount()
        self.tax= self.tax + item.get_tax()

    def approve(self):
        if self.status is OrderStatus.SHIPPED:
            raise ShippedOrdersCannotBeChangedError()

        if self.status is OrderStatus.REJECTED:
            raise RejectedOrderCannotBeApprovedError()

        self.status = OrderStatus.APPROVED

    def reject(self):
        if self.status is OrderStatus.SHIPPED:
            raise ShippedOrdersCannotBeChangedError()
            
        if self.status is OrderStatus.APPROVED:
            raise ApprovedOrderCannotBeRejectedError()

        self.status = OrderStatus.REJECTED

    def check_shipment(self):
        if self.status is OrderStatus.CREATED or self.status is OrderStatus.REJECTED:
            raise OrderCannotBeShippedError()

        if self.status is OrderStatus.SHIPPED:
            raise OrderCannotBeShippedTwiceError()

    def shipped(self):
        self.status = OrderStatus.SHIPPED
