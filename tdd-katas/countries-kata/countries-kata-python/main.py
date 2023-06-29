import requests
from dataclasses import dataclass
from http import HTTPStatus

API_URL = "https://restcountries.com/v3.1/all?fields=name,region,subregion,unMember,cca3,cca2,ccn3,capital,population"
HEADER = ['name', 'capital', 'region', 'subregion', 'population', 'cca3', 'cca2', 'ccn3', 'unMember']

@dataclass
class Country:
  name: str
  capital: str
  region: str
  subregion: str
  population: int
  cca3: str
  cca2: str
  ccn3: str
  unMember: bool
  
  @classmethod
  def from_json(cls, country_json):
    return Country(
        country_json.get("name").get("common"),
        country_json.get("capital"),
        country_json.get("region"),
        country_json.get("subregion"),
        country_json.get("population"),
        country_json.get("cca3"),
        country_json.get("cca2"),
        country_json.get("ccn3"),
        country_json.get("unMember"))
    
  def as_array(self):
    return [
      self.name, 
      self.capital[0] if len(self.capital) == 1 else "",
      self.region, 
      self.subregion, 
      self.population, 
      self.cca3, 
      self.cca2, 
      self.ccn3, 
      self.unMember]
 
def main():
    response = requests.get(API_URL)
    if response.status_code == HTTPStatus.OK:
        countries = [Country.from_json(country_data) for country_data in response.json()]
        csv_rows = [country.as_array() for country in countries]
        with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(HEADER)
            writer.writerows(csv_rows)
      
    elif response.status_code == HTTPStatus.NOT_FOUND:
        raise requests.exceptions.InvalidURL
    else:
        raise requests.exceptions.RequestException
      
import csv

if __name__ == "__main__":
    main()
