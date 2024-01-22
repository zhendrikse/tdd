from decimal import Decimal, ROUND_HALF_UP

from src.domain.Category import Category
from dataclasses import dataclass


@dataclass(frozen = True)
class Product(object):
    _name: str
    _price: Decimal
    _category: Category

    def get_name(self):
       return self._name
    
    def get_price(self):
       return self._price

    def unitary_tax(self):
      return Decimal(self._price / Decimal(100) * self._category.get_tax_percentage()).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    
    def unitary_taxed_amount(self):
      return Decimal(self._price + self.unitary_tax()).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
