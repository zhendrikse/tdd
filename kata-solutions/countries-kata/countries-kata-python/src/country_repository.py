from typing import Protocol
import csv

class CountriesOutputPort(Protocol):
  def write(self, country_list) -> None:
      pass

class CsvCountriesOutputAdapter:
  def write(self, country_list) -> None:
    with open('countries.csv', 'w') as file:
        writer = csv.writer(file)
        #writer.writerow(header)
        writer.writerows(country_list.as_nested_array())