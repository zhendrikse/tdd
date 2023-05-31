from enum import Enum
from dataclasses import dataclass

class MovieType(Enum):
  CHILDRENS = 2
  REGULAR = 0
  NEW_RELEASE = 1

@dataclass(frozen = True)
class Movie:
  _title: str
  _price_code: float
	
  def get_price_code (self):
    return self._price_code
	
  def set_price_code (self, code):
    self._price_code = code;
	
  def get_title (self):
    return self._title
