from dataclasses import dataclass
from math import sqrt

@dataclass
class Country:
  name: str
  capital: str
  population: int

class CountryList:
  def __init__(self, country_list = []):
    self._countries = country_list

  def average_population(self):
    return average_of([country.population for country in self._countries])

  def standard_deviation(self):
    return standard_deviation_of([country.population for country in self._countries])
    
def average_of(a_collection):
  if not a_collection: return 0
  return sum([item for item in a_collection]) / len(a_collection)

def standard_deviation_of(a_collection):
  if not a_collection: return 0
  return sqrt(sum([(item - average_of(a_collection)) ** 2 for item in a_collection]) / len(a_collection))