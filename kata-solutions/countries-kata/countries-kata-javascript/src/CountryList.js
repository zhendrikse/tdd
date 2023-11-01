'use strict';

class CountryList {
  constructor(countryList = []) {
    this.countryList = countryList;
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
}

module.exports = {
  CountryList: CountryList
}