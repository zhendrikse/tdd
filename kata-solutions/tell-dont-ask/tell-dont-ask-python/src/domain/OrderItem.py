from decimal import Decimal, ROUND_HALF_UP

from src.domain.Product import Product
from dataclasses import dataclass


@dataclass(frozen = True)
class OrderItem(object):
    _product: Product
    _quantity: int

    def get_product(self):
        return self._product
    
    def get_quantity(self):
        return self._quantity

    def get_taxed_amount(self):
        return Decimal(self._product.unitary_taxed_amount() * Decimal(self._quantity).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
        
    def get_tax(self):
        return self._product.unitary_tax() * (Decimal(self._quantity))
