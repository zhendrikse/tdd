import decimal
from dataclasses import dataclass


@dataclass(frozen = True)
class Category(object):
    name: str
    tax_percentage: decimal.Decimal
