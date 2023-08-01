from typing import Protocol, List
import csv
from country import Country

class CountriesOutputPort(Protocol):
  def write(self, country_list) -> None:
      pass

class CountriesInputPort(Protocol):
  def load_all(self) -> List[Country]:
      pass

class CsvCountriesOutputAdapter:
  def write(self, country_list) -> None:
    with open('countries.csv', 'w') as file:
        writer = csv.writer(file)
        #writer.writerow(header)
        writer.writerows(country_list.as_nested_array())

class RestCountriesInputAdapter:
  def load_all(self) -> List[Country]:
      pass
  