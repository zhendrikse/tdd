'use strict';
const fs = require('fs');

const { Country } = require('../src/Country');

const REST_ENDPOINT = 'https://restcountries.com/v3.1/all?fields=name,capital,population,cioc,region';

class CountriesOutputAdapter {
  write(countrList) {
    let csvContent = "";

    countrList.forEach(function (rowArray) {
      let row = rowArray.join(",");
      csvContent += row + "\r\n";
    });

    fs.writeFileSync('countries.csv', csvContent, (err) => {
      if (err) throw err;
      console.log('countries.csv saved.');
    });
  }
}

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

class CountryList {
  // @private
  constructor(inputPort, outputPort) {
    this.countryList = inputPort.load_all();
    this.outputPort = outputPort;
  }

  static async create_instance(inputPort = RestCountriesInputAdapter, outputPort = new CountriesOutputAdapter()) {
    return new CountryList(await inputPort.instance(), outputPort);
  }

  compare(country1, country2) {
    return country1.population - country2.population
  }

  sorted_by_population() {
    return this.countryList.sort(this.compare);
  }

  sumOf(anArray) {
    return anArray.reduce((total, item) => total + item, 0);
  }

  average_population() {
    if (!this.countryList.length)
      return 0;

    var totalPopulation = this.sumOf(this.countryList.map(country => country.population));
    return totalPopulation / this.countryList.length;
  }

  standard_deviation() {
    if (!this.countryList.length)
      return 0;

    var average = this.average_population();
    var diviationsList = this.countryList.map(country => (country.population - average) * (country.population - average));
    return Math.sqrt(this.sumOf(diviationsList) / this.countryList.length)
  }

  standard_deviations_for(country) {
    var standardDeviations = Math.abs(this.average_population() - country.population) / this.standard_deviation();
    return Math.round((standardDeviations + Number.EPSILON) * 100) / 100
  }

  as_nested_array() {
    var sortedCountries = this.sorted_by_population();
    return sortedCountries.map(country => [country.name, country.capital, country.population, this.standard_deviations_for(country)]);
  }

  to_csv() {
    this.outputPort.write(this.as_nested_array());
  }
}

module.exports = {
  CountryList: CountryList
}

async function main() {
  let countryList = await CountryList.create_instance();
  countryList.to_csv();
}

if (require.main === module) {
  main();
}