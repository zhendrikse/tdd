const { Country } = require('./Country');

const REST_ENDPOINT = 'https://restcountries.com/v3.1/all?fields=name,capital,population,cioc,region';

class RestCountriesInputAdapter {
  #countries = [];

  constructor(countries) {
    this.#countries = countries;
  }

  load_all() {
    return this.#countries; 
  }

  static async instance() {
    const response = await fetch(REST_ENDPOINT, {
      method: 'GET'
    });
    const responseAsJson = await response.json();
    let restCountries = JSON.parse(JSON.stringify(responseAsJson));
    return new RestCountriesInputAdapter(restCountries.map(country => new Country(country.name.common, country.capital[0], country.population)));
  }
}
  
module.exports = {
    RestCountriesInputAdapter: RestCountriesInputAdapter
}