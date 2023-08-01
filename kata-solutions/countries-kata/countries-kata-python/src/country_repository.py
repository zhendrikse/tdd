from typing import Protocol
import csv

class CountryRepository(Protocol):
  def write_to_file(self, country_list) -> None:
      pass

class CsvCountryAdapter:
  def write_to_file(self, country_list) -> None:
    with open('countries.csv', 'w') as file:
        writer = csv.writer(file)
        #writer.writerow(header)
        writer.writerows(country_list.as_nested_array())