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

  def sorted_by_population(self):
    return sorted(self._countries, key=lambda x: getattr(x, 'population'))

  def average_population(self):
    return average_of([country.population for country in self._countries])

  def standard_deviation(self):
    return standard_deviation_of([country.population for country in self._countries])
  
  def standard_deviations_per_country(self):
    return [
      round(abs(self.average_population() - country.population) / self.standard_deviation(), 2) 
      for country in self.sorted_by_population()]
  
  def as_nested_array(self):
    sorted_countries = self.sorted_by_population()
    return[[sorted_countries[i].name, 
            sorted_countries[i].capital, 
            sorted_countries[i].population, 
            self.standard_deviations_per_country()[i]] for i in range(len(self._countries))]
    
def average_of(a_collection):
  if not a_collection: return 0
  return sum([item for item in a_collection]) / len(a_collection)

def standard_deviation_of(a_collection):
  if not a_collection: return 0
  return sqrt(sum([(item - average_of(a_collection)) ** 2 for item in a_collection]) / len(a_collection))