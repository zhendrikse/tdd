from typing import Protocol, List
import csv, requests
from country import Country
from http import HTTPStatus

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
  