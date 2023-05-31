from enum import Enum

class MovieType(Enum):
  CHILDRENS = 2
  REGULAR = 0
  NEW_RELEASE = 1

class Movie:
  def __init__(self, title, priceCode):
    self._title = title
    self._priceCode = priceCode
	
  def get_price_code (self):
    return self._priceCode
	
  def set_price_code (self, code):
    self._priceCode = code;
	
  def get_title (self):
    return self._title
