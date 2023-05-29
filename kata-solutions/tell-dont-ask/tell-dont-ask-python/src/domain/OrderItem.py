from decimal import Decimal, ROUND_HALF_UP

from src.domain.Product import Product
from dataclasses import dataclass


@dataclass(frozen = True)
class OrderItem(object):
    product: Product
    quantity: int

    def get_taxed_amount(self):
        return Decimal(self.product.unitary_taxed_amount() * Decimal(self.quantity).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
        
    def get_tax(self):
        return self.product.unitary_tax() * (Decimal(self.quantity))
