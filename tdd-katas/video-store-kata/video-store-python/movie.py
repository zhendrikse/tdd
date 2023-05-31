from enum import Enum

class MovieType(Enum):
  CHILDRENS = 2
  REGULAR = 0
  NEW_RELEASE = 1

class Movie:
  def __init__(self, title, priceCode):
    self._title = title
    self._priceCode = priceCode
	
  def getPriceCode (self):
    return self._priceCode
	
  def setPriceCode (self, code):
    self._priceCode = code;
	
  def getTitle (self):
    return self._title
