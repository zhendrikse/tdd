import decimal
import unittest

from hamcrest import assert_that, is_, has_length, calling, raises

from src.domain.Category import Category
from src.domain.OrderStatus import OrderStatus
from src.domain.Product import Product
from src.useCase.OrderCreationUseCase import OrderCreationUseCase
from src.useCase.SellItemRequest import SellItemRequest
from src.useCase.SellItemsRequest import SellItemsRequest
from src.useCase.UnknownProductError import UnknownProductError
from test.doubles.InMemoryProductCatalog import InMemoryProductCatalog
from test.doubles.TestOrderRepository import TestOrderRepository


class TestOrderCreationUseCase(unittest.TestCase):
    def setUp(self):
        self.order_repository = TestOrderRepository()

        food = Category("food", decimal.Decimal("10"))
        product1 = Product("salad", decimal.Decimal("3.56"), food)
        product2 = Product("tomato", decimal.Decimal("4.65"), food)

        productCatalog = InMemoryProductCatalog([product1, product2])
        self.use_case = OrderCreationUseCase(self.order_repository, productCatalog)

    def test_sell_multiple_items(self):
        salad_request = SellItemRequest()
        salad_request.set_product_name("salad")
        salad_request.set_quantity(2)

        tomato_request = SellItemRequest()
        tomato_request.set_product_name("tomato")
        tomato_request.set_quantity(3)

        request = SellItemsRequest()
        request.set_requests([salad_request, tomato_request])

        self.use_case.run(request)

        inserted_order = self.order_repository.get_saved_order()
        assert_that(inserted_order.get_status(), is_(OrderStatus.CREATED))
        assert_that(inserted_order.get_total(), is_(decimal.Decimal("23.20")))
        assert_that(inserted_order.get_tax(), is_(decimal.Decimal("2.13")))
        assert_that(inserted_order.get_currency(), is_("EUR"))
        assert_that(inserted_order.get_items(), has_length(2))
        assert_that(inserted_order.get_items()[0].product.name, is_("salad"))
        assert_that(inserted_order.get_items()[0].product.price, is_(decimal.Decimal("3.56")))
        assert_that(inserted_order.get_items()[0].quantity, is_(2))
        assert_that(inserted_order.get_items()[0].get_taxed_amount(), is_(decimal.Decimal("7.84")))
        assert_that(inserted_order.get_items()[0].get_tax(), is_(decimal.Decimal("0.72")))
        assert_that(inserted_order.get_items()[1].product.name, is_("tomato"))
        assert_that(inserted_order.get_items()[1].product.price, is_(decimal.Decimal("4.65")))
        assert_that(inserted_order.get_items()[1].quantity, is_(3))
        assert_that(inserted_order.get_items()[1].get_taxed_amount(), is_(decimal.Decimal("15.36")))
        assert_that(inserted_order.get_items()[1].get_tax(), is_(decimal.Decimal("1.41")))

    def test_unknown_product(self):
        request = SellItemsRequest()
        request.set_requests([])
        unknown_product_request = SellItemRequest()
        unknown_product_request.set_product_name("unknown product")
        request.get_requests().append(unknown_product_request)

        assert_that(calling(self.use_case.run).with_args(request), raises(UnknownProductError))


if __name__ == '__main__':
    unittest.main()
