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
    //return this.countryList.sort(function(country1, country2) {return country1.population - country2.population});
    //return [this.countryList[2], this.countryList[0], this.countryList[1], this.countryList[3]];
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
    var diviationList = this.countryList.map(country => (country.population - average) * (country.population - average));
    return Math.sqrt(this.sumOf(diviationList) / this.countryList.length)
  }
}

module.exports = {
  CountryList: CountryList
}