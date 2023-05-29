from decimal import Decimal, ROUND_HALF_UP

from src.domain.Order import Order
from src.domain.OrderItem import OrderItem
from src.repository.OrderRepository import OrderRepository
from src.repository.ProductCatalog import ProductCatalog
from src.useCase.SellItemsRequest import SellItemsRequest
from src.useCase.UnknownProductError import UnknownProductError


class OrderCreationUseCase:
    def __init__(self, order_repository: OrderRepository, product_catalog: ProductCatalog):
        self.order_repository = order_repository
        self.product_catalog = product_catalog

    def run(self, request: SellItemsRequest):
        order = Order("EUR")

        for item_request in request.get_requests():
            product = self.product_catalog.get_by_name(item_request.get_product_name())

            if product is None:
                raise UnknownProductError()
            else:
              order.add_order_item(OrderItem(product, item_request.get_quantity()))



        self.order_repository.save(order)
