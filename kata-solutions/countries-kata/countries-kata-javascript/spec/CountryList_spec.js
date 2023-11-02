const { CountryList } = require('../src/CountryList');
const { Country } = require('../src/Country')

const NETHERLANDS = new Country("Netherlands", "Amsterdam", 4)
const PORTUGAL = new Country("Portugal", "Lissabon", 7)
const BELGIUM = new Country("Belgium", "Brussels", 3)
const UNITED_KINGDOM = new Country("United Kingdom", "London", 10)

const COUNTRY_LIST_FOR_TESTING = [NETHERLANDS, PORTUGAL, BELGIUM, UNITED_KINGDOM]

class EmptyCountriesInputAdapterStub {
  load_all() {
    return [];
  }
}

class CountriesInputAdapterStub {
  load_all() {
    return COUNTRY_LIST_FOR_TESTING;
  }
}

describe('A list without countries (empty list)', function () {
  let countryList;

  beforeEach(function() {
    countryList = new CountryList(new EmptyCountriesInputAdapterStub());
  });

  it('should sort the empty list', function () {
    expect(countryList.sorted_by_population()).toEqual([]);
  });

  it('calculates the average population', function() {
    expect(countryList.average_population()).toEqual(0);
  });

  it('calculates the standard deviation', function() {
    expect(countryList.standard_deviation()).toEqual(0);
  });
});


describe('A list with countries', function () {
  let countryList;

  beforeEach(function() {
    countryList = new CountryList(new CountriesInputAdapterStub());
  });

  it('should sort the countries by population size', function () {
    expect(countryList.sorted_by_population()[0]).toEqual(BELGIUM);
    expect(countryList.sorted_by_population()[1]).toEqual(NETHERLANDS);
    expect(countryList.sorted_by_population()[2]).toEqual(PORTUGAL);
    expect(countryList.sorted_by_population()[3]).toEqual(UNITED_KINGDOM);
  });

  it('calculates the average population', function() {
    expect(countryList.average_population()).toEqual(6);
  });

  it('calculates the standard deviation', function() {
    expect(countryList.standard_deviation()).toBeCloseTo(2.7386, 4);
  });

  it('calculates the number of standard deviations for each country', function() {
    expect(countryList.standard_deviations_for(NETHERLANDS)).toEqual(0.73);
  });
  
  it('representes itself as nested array', function() {
    expected_output = [
       ["Belgium", "Brussels", 3, 1.10], 
       ["Netherlands", "Amsterdam", 4, 0.73], 
       ["Portugal", "Lissabon", 7, 0.37], 
       ["United Kingdom", "London", 10, 1.46]]
    expect(countryList.as_nested_array()).toEqual(expected_output);
  });
});
