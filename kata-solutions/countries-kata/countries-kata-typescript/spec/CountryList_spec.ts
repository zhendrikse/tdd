'use strict';

import { expect } from "chai"
import { CountryList } from "../src/CountryList"
import { Country } from "../src/Country"
import { InputPort, OutputPort } from "../src/Ports";

const NETHERLANDS = new Country("Netherlands", "Amsterdam", 4)
const PORTUGAL = new Country("Portugal", "Lissabon", 7)
const BELGIUM = new Country("Belgium", "Brussels", 3)
const UNITED_KINGDOM = new Country("United Kingdom", "London", 10)

const COUNTRY_LIST_FOR_TESTING = [NETHERLANDS, PORTUGAL, BELGIUM, UNITED_KINGDOM]

class EmptyCountriesInputAdapterStub implements InputPort {
  load_all() {
    return [];
  }

  static async instance() {
    return new EmptyCountriesInputAdapterStub();
  }
}

class CountriesInputAdapterStub implements InputPort {
  load_all() {
    return COUNTRY_LIST_FOR_TESTING;
  }

  static async instance() {
    return new CountriesInputAdapterStub();
  }
}

class MockCountriesOutputAdapter implements OutputPort {
  write(countryList: string[][]) {
    let csvContent = "";

    countryList.forEach(function(rowArray) {
      let row = rowArray.join(",");
      csvContent += row + "\r\n";
    });

    expect(csvContent).to.equal("Belgium,Brussels,3,1.1\r\n" +
      "Netherlands,Amsterdam,4,0.73\r\n" +
      "Portugal,Lissabon,7,0.37\r\n" +
      "United Kingdom,London,10,1.46\r\n");
  }
}

describe('A list without countries (empty list)', () => {
  let countryList: CountryList;

  beforeEach(async () => {
    countryList = await CountryList.create_instance(await EmptyCountriesInputAdapterStub.instance(), new MockCountriesOutputAdapter());
  });

  it('should sort the empty list', () => {
    expect(countryList.sorted_by_population()).to.be.empty;
  });

  it('calculates the average population', () => {
    expect(countryList.average_population()).to.equal(0);
  });

  it('calculates the standard deviation', () => {
    expect(countryList.standard_deviation()).to.equal(0);
  });
});


describe('A list with countries', () => {
  let countryList: CountryList;

  beforeEach(async () => {
    countryList = await CountryList.create_instance(await CountriesInputAdapterStub.instance(), new MockCountriesOutputAdapter());
  });


  it('should sort the countries by population size', () => {
    expect(countryList.sorted_by_population()[0]).to.equal(BELGIUM);
    expect(countryList.sorted_by_population()[1]).to.equal(NETHERLANDS);
    expect(countryList.sorted_by_population()[2]).to.equal(PORTUGAL);
    expect(countryList.sorted_by_population()[3]).to.equal(UNITED_KINGDOM);
  });

  it('calculates the average population', () => {
    expect(countryList.average_population()).to.equal(6);
  });

  it('calculates the standard deviation', () => {
    expect(countryList.standard_deviation()).to.be.closeTo(2.7386, 4);
  });

  it('calculates the number of standard deviations for each country', () => {
    expect(countryList.standard_deviations_for(NETHERLANDS)).to.equal(0.73);
  });

  it('representes itself as nested array', () => {
    let expected_output: string[][] = [
      ["Belgium", "Brussels", String(3), String(1.10)],
      ["Netherlands", "Amsterdam", String(4), String(0.73)],
      ["Portugal", "Lissabon", String(7), String(0.37)],
      ["United Kingdom", "London", String(10), String(1.46)]]
    expect(countryList.as_nested_array()).to.eql(expected_output);
  });

  it('writes the country data to CSV', () => {
    countryList.to_csv();
  })
});

