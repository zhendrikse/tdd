const { CountryList } = require('../src/CountryList');
const { Country } = require('../src/Country')

const NETHERLANDS = new Country("Netherlands", "Amsterdam", 4)
const PORTUGAL = new Country("Portugal", "Lissabon", 7)
const BELGIUM = new Country("Belgium", "Brussels", 3)
const UNITED_KINGDOM = new Country("United Kingdom", "London", 10)

const COUNTRY_LIST_FOR_TESTING = [NETHERLANDS, PORTUGAL, BELGIUM, UNITED_KINGDOM]

describe('A list without countries (empty list)', function () {
  let countryList;

  beforeEach(function() {
    countryList = new CountryList();
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
    countryList = new CountryList(COUNTRY_LIST_FOR_TESTING);
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
  
});
