import decimal
from dataclasses import dataclass


@dataclass(frozen = True)
class Category(object):
    _name: str
    _tax_percentage: decimal.Decimal

    def get_tax_percentage(self):
        return self._tax_percentage
