# Introduction

Please read the general [introduction to the countries kata](../README.md) first!

## References

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
  <summary>A test for the calculation of the standard deviation for population size</summary>

  ```python
  def test_standard_deviations_per_country(self, country_list):
      assert_that(country_list.standard_deviations_per_country(), equal_to([1.10, 0.73, 0.37, 1.46]))
  ```

<details>
  <summary>Implementation that makes the test pass</summary>

  ```python
  def standard_deviations_per_country(self):
    standard_deviation = self.standard_deviation()
    return [
      round(abs(self.average_population() - country.population) / standard_deviation, 2) 
      for country in self.sorted_by_population()]
  ```
</details>
</details>

## Preparations for input and output