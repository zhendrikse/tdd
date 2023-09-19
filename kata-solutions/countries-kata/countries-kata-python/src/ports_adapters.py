from typing import Protocol, List
import csv, requests
from country import Country
from http import HTTPStatus
from dataclasses import dataclass

@dataclass(frozen = True)
class CountriesDataDto:
  """
  A nested list of country data, for example:
    [
      ["Belgium", "Brussels", 3, 1.10], 
      ["Netherlands", "Amsterdam", 4, 0.73], 
      ["Portugal", "Lissabon", 7, 0.37], 
      ["United Kingdom", "London", 10, 1.46]
    ]
  """
  countries: List[List[str]]

class CountriesOutputPort(Protocol):
  def export(self, countries_dto: CountriesDataDto) -> None:
      ...

class CountriesInputPort(Protocol):
  def load_all(self) -> List[Country]:
      ...

class CsvCountriesOutputAdapter:
  def export(self, countries_dto) -> None:
    with open('countries.csv', 'w') as file:
        writer = csv.writer(file)
        #writer.writerow(header)
        writer.writerows(countries_dto.countries)

class RestCountriesInputAdapter:
  def country_from_json(self, country_json):
    return Country(
      country_json.get("name").get("common"),
      country_json.get("capital"),
      country_json.get("population"))
    
  def load_all(self) -> List[Country]:
    url = "https://restcountries.com/v3.1/all?fields=name,region,subregion,unMember,cca3,cca2,ccn3,capital,population"
    response = requests.get(url)
    if response.status_code != HTTPStatus.OK:
      raise RuntimeError(f"Fetching country data failed, HTTPStatus={response.status_code}")
      
    return [self.country_from_json(country_data) for country_data in response.json()]
  