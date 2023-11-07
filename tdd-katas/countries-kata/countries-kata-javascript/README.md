# Introduction

Please read the general [introduction to the countries kata](../README.md) first!

## References

Since we would like to have a `CountryList` instance filled with country data
immediately after instantiation, we are in need of a so-called asynchronous
constructor (as the a call to an external API is asynchronous by definition).

The references below contain some suggestions on how you may best approach
the implementation of an asynchronous constructor in Javascript.

- [Hexagonal architecture in Javascript](https://picostitch.com/tidbits/2021/02/hexagonal-architecture-in-javascript/)
- [Hexagonal architecture in JavaScript applications — and how it relates to Flux](https://medium.com/@Killavus/hexagonal-architecture-in-javascript-applications-and-how-it-relates-to-flux-349616d1268d#.ik8250i7s)
- [Interfaces in Java using Flow](https://flow.org/en/docs/types/interfaces)
- [The proper way to write async constructors in Javascript](https://dev.to/somedood/the-proper-way-to-write-async-constructors-in-javascript-1o8c)

# Getting started

First, create an intial Javascript kata set-up as described [here](https://github.com/zhendrikse/tdd/tree/master/cookiecutter).

Next, go the the newly created project directory and consult
the provided ``README.md`` in there.

# Implementation instructions

Below you'll find detailed instructions in case you can't/won't implement
this kata yourself.

Let's start by writing the specifications for our domain model.
We are going to make use of the example data given in 
the general [introduction to the countries kata](../README.md):

```
name,capital,population,deviation
Belgium,Brussels,3,0.40
Netherlands,Amsterdam,4,0.73
Portugal,Lissabon,7,0.37
United Kingdom,London,10,1.46 
```

## Sorting the list

First, we are going to sort a given list of countries by the size of their population.

<details>
  <summary>Test sorting by population size</summary>

```javascript
describe('A list without countries (empty list)', function () {
  it('should sort the empty list', function () {
    var countryList = new CountryList();
    expect(countryList.sorted_by_population()).toEqual([]);
  });
```

To make this test pass, we define a `CountryList` class with
the required method:

```javascript
class CountryList {
  constructor(countryList = []) {
    this.countryList = countryList;
  }

  sorted_by_population() {
    return this.countryList;
  }
```

Next, it should sort a non-empty list

```javascript
const NETHERLANDS = new Country("Netherlands", "Amsterdam", 4)
const PORTUGAL = new Country("Portugal", "Lissabon", 7)
const BELGIUM = new Country("Belgium", "Brussels", 3)
const UNITED_KINGDOM = new Country("United Kingdom", "London", 10)

const COUNTRY_LIST_FOR_TESTING = [NETHERLANDS, PORTUGAL, BELGIUM, UNITED_KINGDOM]

describe('A list with countries', function () {
  it('should sort the countries by population size', function () {
    var countryList = new CountryList(COUNTRY_LIST_FOR_TESTING);
    expect(countryList.sorted_by_population()[0]).toEqual(BELGIUM);
    expect(countryList.sorted_by_population()[1]).toEqual(NETHERLANDS);
    expect(countryList.sorted_by_population()[2]).toEqual(PORTUGAL);
    expect(countryList.sorted_by_population()[3]).toEqual(UNITED_KINGDOM);
  });
```

This forces us to define a `Country` and a `CountryList` class:

<details>
  <summary>Code to make the test pass</summary>

```javascript
class Country {
    constructor(name, capital, population) {
        this.name = name;
        this.capital = capital;
        this.population = population;
    }
}

module.exports = {
    Country: Country
}
```

```javascript
class CountryList {
  constructor(countryList = []) {
    this.countryList = countryList;
  }

  sorted_by_population() {
    return this.countryList.sort(function(country1, country2) {return country1.population - country2.population});
  }
```

which can be refactored to

```javascript
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
```
</details>

</details>

## Calculation of the statistics

### Average population

Let's first build some logic that calculates the average population
size given a list of countries.

<details>
  <summary>A test for the calculation of an average of an empty list</summary>

```javascript
describe('A list without countries (empty list)', function () {
  let countryList;

  beforeEach(function() {
    countryList = new CountryList();
  });

  // ...

  it('calculates the average population', function() {
    expect(countryList.average_population()).toEqual(0);
  });
```

We can easily make this test pass

<details>
  <summary>Implementation</summary>

```javascript
  average_population() {
    return 0;
  }
```
</details>
</details>

Obviously, we need to introduce a non-empty list to force a more generic
implementation.

<details>
  <summary>A test for the calculation of average population size</summary>

```javascript
describe('A list with countries', function () {
  let countryList;

  beforeEach(function() {
    countryList = new CountryList(COUNTRY_LIST_FOR_TESTING);
  });
  
  // ...

  it('calculates the average population', function() {
    expect(countryList.average_population()).toEqual(6);
  });  
```

<details>
  <summary>Implementation</summary>

```javascript
  average_population() {
    if (!this.countryList.length)
      return 0;

    var totalPopulation = this.sumOf(this.countryList.map(country => country.population));
    return totalPopulation / this.countryList.length;
  }
```
</details>
</details>

### Standard deviation

Let's now calculate the standard deviation.

<details>
  <summary>A test for the calculation of the standard deviation of an empty list</summary>

  ```javascript
  it('calculates the standard deviation', function() {
    expect(countryList.standard_deviation()).toEqual(0);
  });
  ```

<details>
  <summary>Implementation</summary>

  ```python
  standard_deviation() {
    return 0;
  }
  ```
</details>
</details>

Obviously, we need to introduce a non-empty list to force a more generic
implementation.

<details>
  <summary>A test for the calculation of the standard deviation for population size</summary>

  ```javascript
  it('calculates the standard deviation', function() {
    expect(countryList.standard_deviation()).toBeCloseTo(2.7386, 4);
  });
  ```

This forces us to generalize to

<details>
  <summary>Implementation</summary>

  ```javascript
  standard_deviation() {
    if (!this.countryList.length)
      return 0;

    var average = this.average_population();
    var diviationsList = this.countryList.map(country => (country.population - average) * (country.population - average));
    return Math.sqrt(this.sumOf(diviationsList) / this.countryList.length)
  }
  ```
</details>
</details>

### Standard deviation per country

As we eventually need to deliver a list of countries sorted by population size,
it would be convenient if the list with calculated standard deviations from the
main was/is sorted by population size by default. 

<details>
  <summary>A test for the standard deviation count for a country</summary>

  ```javascript
  it('calculates the number of standard deviations for each country', () => {
    expect(countryList.standard_deviations_for(NETHERLANDS)).toEqual(0.73);
  });
  ```

<details>
  <summary>Implementation that makes the test pass</summary>

  ```javascript
  standard_deviations_for(country) {
    var standardDeviations = Math.abs(this.average_population() - country.population) / this.standard_deviation();
    return Math.round((standardDeviations + Number.EPSILON) * 100) / 100
  }
  ```
</details>
</details>

## Preparations for input and output

In Javascript, a call to an external REST API is asynchronous by definition.

This means that if we want to make a call to the countries endpoint to fetch
the country data to initialize our country list, i.e. in the constructor, 
the constructor becomes asynchronous.

This poses a challenge that is described in 
[the proper way to write async constructors in Javascript](https://dev.to/somedood/the-proper-way-to-write-async-constructors-in-javascript-1o8c). We opt here for the last (and best) option described in
that post, namely to initialize the class in an `async` function like so:

```javascript
async function main() {
  let countryList = await CountryList.create_instance();
  countryList.to_csv();
}
```

This way, we _first_ wait for the `countryList` instance to
be populated with the country data coming from the country data
REST endpoint, _before_ continuing with our calls and/or operations on it.

A `countryList` instance from the `CountryList` class is then
created by invoking a static factory method. 

```javascript
class CountryList {
// @private
constructor(inputPort, outputPort) {
  this.countryList = inputPort.load_all();
  this.outputPort = outputPort;
}

static async create_instance(inputPort = RestCountriesInputAdapter, outputPort = new CsvOutputAdapter()) {
  return new CountryList(await inputPort.instance(), outputPort);
}
```

Unfortunately, Javascript does not have a means to limit the
access to a constructor to `private`, so we must rely on the 
instantiating class to create instances using the static
`create_instance()` method.

Let's first see how this works out in our tests.

## Stub input adapters in our tests

First, we define a stub to provide the `CountryList` with 
an empty list of countries.

<details>
  <summary>Stub for empty country list</summary>

  ```javascript
  class EmptyCountriesInputAdapterStub {
    load_all() {
      return []; 
    }

    static async instance() {
      return new EmptyCountriesInputAdapterStub();
    }
  }
  ```

  This is then used for the set of tests that are based on an
  empty list:

  ```javascript
  describe('A list without countries (empty list)', () => {
    let countryList;

    beforeEach(async () => {
      countryList = await CountryList.create_instance(EmptyCountriesInputAdapterStub, new MockCountriesOutputAdapter());
    });

    it('should sort the empty list', () => {
      expect(countryList.sorted_by_population()).toEqual([]);
    });

    // ...
  ```
</details>


Next, we define a stub to provide the `CountryList` with 
an empty list of countries.

<details>
  <summary>Stub for populated country list</summary>

```javascript
const NETHERLANDS = new Country("Netherlands", "Amsterdam", 4)
const PORTUGAL = new Country("Portugal", "Lissabon", 7)
const BELGIUM = new Country("Belgium", "Brussels", 3)
const UNITED_KINGDOM = new Country("United Kingdom", "London", 10)

const COUNTRY_LIST_FOR_TESTING = [NETHERLANDS, PORTUGAL, BELGIUM, UNITED_KINGDOM]

class CountriesInputAdapterStub {
  load_all() {
    return COUNTRY_LIST_FOR_TESTING; 
  }

  static async instance() {
    return new CountriesInputAdapterStub();
  }
}
```

  This is then used for the set of tests that are based on an
  populated list:

  ```javascript
  describe('A list with countries', () => {
    let countryList;

    beforeEach(async () => {
      countryList = await CountryList.create_instance(CountriesInputAdapterStub, new MockCountriesOutputAdapter());
    });


    it('should sort the countries by population size', () => {
    // ...
  ```
</details>

## Countries REST-based input adapter

We use the [fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) 
to get the countries data from the REST endpoint. 

<details>
  <summary>Implementation of the REST-based adapter</summary>

```javascript
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
```
</details>

## CSV output adapter

The output adapter doesn't necessarily need to be asynchronous,
as in addition to `fs.writeFile()` there is a
`fs.writeFileSync()` function available.

<details>
  <summary>CSV output adapter</summary>

```javascript
class CsvOutputAdapter {
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
```
</details>

In our tests, we can inject a mock that verifies the contents
that is normally written to a (CSV) file.

<details>
  <summary>A mock output adapter</summary>

```javascript

class MockCountriesOutputAdapter {
  write(countrList) {
    let csvContent = "";

    countrList.forEach(function(rowArray) {
      let row = rowArray.join(",");
      csvContent += row + "\r\n";
    });

    expect(csvContent).toEqual("Belgium,Brussels,3,1.1\r\n" +
                               "Netherlands,Amsterdam,4,0.73\r\n" +
                               "Portugal,Lissabon,7,0.37\r\n" +
                               "United Kingdom,London,10,1.46\r\n");
  }
}
```
</details>