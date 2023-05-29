from decimal import Decimal, ROUND_HALF_UP

from src.domain.Category import Category
from dataclasses import dataclass


@dataclass(frozen = True)
class Product(object):
    name: str
    price: Decimal
    category: Category

    def unitary_tax(self):
      return Decimal(self.price / Decimal(100) * self.category.tax_percentage).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    
    def unitary_taxed_amount(self):
      return Decimal(self.price + self.unitary_tax()).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
