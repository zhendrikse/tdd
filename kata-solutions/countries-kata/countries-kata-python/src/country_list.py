from country import Country
from math import sqrt
from ports_adapters import CsvCountriesOutputAdapter, RestCountriesInputAdapter, CountriesDTO

class CountryList:
  def __init__(self, 
               input_port = RestCountriesInputAdapter(),
               output_port = CsvCountriesOutputAdapter()):
    self._countries = input_port.load_all()
    self._output_port = output_port
  
  def sorted_by_population(self):
    return sorted(self._countries, key=lambda x: getattr(x, 'population'))

  def average_population(self):
    return average_of([country.population for country in self._countries])

  def standard_deviation(self):
    return standard_deviation_of([country.population for country in self._countries])
  
  def standard_deviations_per_country(self):
    standard_deviation = self.standard_deviation()
    return [
      round(abs(self.average_population() - country.population) / standard_deviation, 2) 
      for country in self.sorted_by_population()]

  def export_to_csv(self):
    sorted_countries = self.sorted_by_population()
    standard_deviations_per_country = self.standard_deviations_per_country()
    countries_dto = CountriesDTO([[sorted_countries[i].name, 
            sorted_countries[i].capital, 
            sorted_countries[i].population, 
            standard_deviations_per_country[i]] for i in range(len(self._countries))])
    self._output_port.export(countries_dto)
    
def average_of(a_collection):
  if not a_collection: return 0
  return sum([item for item in a_collection]) / len(a_collection)

def standard_deviation_of(a_collection):
  if not a_collection: return 0
  return sqrt(sum([(item - average_of(a_collection)) ** 2 for item in a_collection]) / len(a_collection))

def main():
    CountryList().export_to_csv()
    print("List with country data exported to countries.csv")

if __name__ == "__main__":
    main()