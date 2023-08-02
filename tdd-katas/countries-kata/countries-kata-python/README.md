# Introduction

Please read the general [introduction to the countries kata](../README.md) first!

# Getting started

Carry out the following steps in order:

1. Create an intial Python kata set-up as described
   [here](https://github.com/zhendrikse/tdd/tree/master/cookiecutter).
   Choose 'n' when prompted for the rSpec syntax. The code coverage is optional.
2. Remove the `.py` files in the `src` and `test` directories, but leave the
   `__init__.py` files untouched!

   Depending on whether you would like to start this kata as a
   refactoring exercise or start it more or less from scratch:

   **Refactoring scenario**:

   - Copy the `main.py` file into the `src` directory

   **Greenfield scenario**:

   - Copy the `country.py` file into the `src` directory
   - Copy the `countries_test.py` file into the `test` directory
3. Install dependencies
   ```
   $ poetry install
   ``` 
4. Depending on the approach chosen

   **Refactoring scenario**:

   - Run `$ python main.py` to run the program and generate a CSV file.
   - Before we change the contents of the generated CSV file to what
     is asked for, we first need to separate out the communicaton with
     the outside world, i.e. the file system and external REST API call.

   **Greenfield scenario**:

   - Run `$ ./run_tests.sh` to run the test and veriffy that all
     assertions are still valid: we are testing a real production API,
     which may well have changed by the time you are reading this!
   - The code in the `country.py` and `countries_test.py` are merely
     meant to illustrate how to get the data from the endpoint. The 
     idea is to empty both files and start from scratch indeed!

## Design considerations

We can use a nested array [to easily create a CSV file](https://www.pythontutorial.net/python-basics/python-write-csv-file/):

<details>
  <summary>Tip on how to write to CSV</summary>

```python
import csv

header = ['name', 'capital', 'region', 'subregion', 'population', 'cca3', 'cca2', 'ccn3', 'unMember']
data = [
    ['Jordan', 'Amman', 'Asia', 'Western Asia', 10203140, 'JOR', 'JO', 400, true 
],
    ['Northern Mariana Islands', 'Saipan' , 'Oceania', 'Micronesia', 57557, 'MNP', 'MP', 580, False],
    #  ...
]

with open('countries.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)
```
</details>

The domain object containing these country data may then hand over these data
to an output port.

Bearing this in mind, it makes sense to define both a `CountriesInputPort` 
and `CountriesOutputPort` that retrieve and export the required country data
from and to "the outside world" respectively.

<details>
  <summary>Possible definition of the input and output ports</summary>

```python
class CountriesOutputPort(Protocol):
  def write(self, country_list) -> None:
      pass

class CountriesInputPort(Protocol):
  def load_all(self) -> List[Country]:
      pass
```
  
</details>

To make the dependency inversion principle explicit, we include the 
ports into our domain, so that it becomes explicit that they are 
defined by and belong to our domain. 
This way, our domain really dictates the outside world what it wants 
to receive, as the interface is written as part of our domain.

Next, we can then define adapters that plug into these ports.

<details>
  <summary>Possible definition of the input and output adapters</summary>

```python
class CsvCountriesOutputAdapter:
  def write(self, country_list) -> None:
    #
    # Your implementation goes here
    #

class RestCountriesInputAdapter:
  def load_all(self) -> List[Country]:
    #
    # Your implementation goes here
    #

```
</details>

Analogously, we can plug in stub adapters in our tests.


# Instructions for the greenfield approach

Below you'll find detailed instructions in case you can't/won't implement
this kata yourself.

Let's start by writing the specifications for our domain model.

## Sorting the list

First, we are going to sort a given list of countries by the size of its population.

<details>
  <summary>Test sorting by population size</summary>

  ```python
    NETHERLANDS = Country("Netherlands", "Amsterdam", 4)
    PORTUGAL = Country("Portugal", "Lissabon", 7)
    BELGIUM = Country("Belgium", "Brussels", 3)
    UNITED_KINGDOM = Country("United Kingdom", "London", 10)

    COUNTRY_LIST_FOR_TESTING = [NETHERLANDS, PORTUGAL, BELGIUM, UNITED_KINGDOM]
    
    def test_sorted_list_by_population_size(self):
      country_list = CountryList(COUNTRY_LIST_FOR_TESTING)
      assert_that(country_list.sorted_by_population()[0], equal_to(BELGIUM))
      assert_that(country_list.sorted_by_population()[1], equal_to(NETHERLANDS))
      assert_that(country_list.sorted_by_population()[2], equal_to(PORTUGAL))
      assert_that(country_list.sorted_by_population()[3], equal_to(UNITED_KINGDOM))
  ```

<details>
  <summary>Code to make the test pass</summary>

  ```python
  def sorted_by_population(self):
    return sorted(self._countries, key=lambda x: getattr(x, 'population'))
  ```
</details>

</details>

## Calcuation of the statistics

### Average population

Let's first build some logic that calculates the average population
size given a list of countries.

<details>
  <summary>A test for the calculation of an average of an empty list</summary>

  ```python
  def test_given_an_empty_country_list_it_calculates_the_average_population(self):
    assert_that(CountryList().average_population(), equal_to(0))
  ```

<details>
  <summary>Implementation</summary>

  ```python
  def average_population(self):
    return 0
  ```
</details>
</details>

Obvisouly, we need to introduce a non-empty list to force a more generic
implementation.

<details>
  <summary>A test for the calculation of average population size</summary>

  ```python
  def test_given_a_country_list_it_calculates_the_average_population(self, country_list):
    country_list = CountryList(
         [Country("Netherlands", 4), 
          Country("Belgium", 3), 
          Country("Portugal", 7), 
          Country("United kingdom", 10)])
    assert_that(country_list.average_population(), equal_to(6))  
  ```

<details>
  <summary>Implementation</summary>

  ```python
  class CountryList:
    def __init__(self, country_list = []):
      self._countries = country_list

    def average_population(self):
      return average_of([country.population for country in self._countries])
    
  def average_of(a_collection):
    if not a_collection: return 0
    return sum([item for item in a_collection]) / len(a_collection)
  ```
</details>
</details>

### Standard deviation

Let's now calculate the standard deviation.

<details>
  <summary>A test for the calculation of the standard deviation of an empty list</summary>

  ```python
  def test_given_an_empty_country_list_it_calculates_the_standard_deviation(self):
      assert_that(CountryList().standard_deviation(), equal_to(0))
  ```

<details>
  <summary>Implementation</summary>

  ```python
  def standard_deviation(self):
    return 0
  ```
</details>
</details>

Obvisouly, we need to introduce a non-empty list to force a more generic
implementation.

<details>
  <summary>A test for the calculation of the standard deviation for population size</summary>

  ```python
  def test_given_a_country_list_it_calculates_the_standard_deviation(self, country_list):
      assert_that(country_list.standard_deviation(), close_to(2.7386, 0.0001))
  ```
where we have moved the set-up of the list with countries in a before-each method:

  ```python
  @pytest.fixture(autouse = True)
  def country_list(self):
      return CountryList(
         [Country("Netherlands", "Amsterdam", 4), 
          Country("Portugal", "Lissabon", 7), 
          Country("Belgium", "Brussels", 3), 
          Country("United Kingdom", "London", 10)])
  ```

<details>
  <summary>Implementation</summary>

  ```python
  class CountryList:
    def __init__(self, country_list = []):
      self._countries = country_list

    # ...

    def standard_deviation(self):
      return standard_deviation_of([country.population for country in self._countries])

  def standard_deviation_of(a_collection):
    if not a_collection: return 0
    return sqrt(sum([(item - average_of(a_collection)) ** 2 for item in a_collection]) / len(a_collection))
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
    return [
      round(abs(self.average_population() - country.population) / self.standard_deviation(), 2) 
      for country in self.sorted_by_population()]
  ```
</details>
</details>

## Exporting to CSV

### Preparation: list of countries as nested array

As explained in the beginning, it would be very convenient to
have the list that is going to be exported availabe as nested array.

<details>
<summary>The list of countries "knows" how to present itself as nested array</summary>

```python
  def test_country_list_as_nested_array(self, country_list):
      expected_output = [
         ["Belgium", "Brussels", 3, 1.10], 
         ["Netherlands", "Amsterdam", 4, 0.73], 
         ["Portugal", "Lissabon", 7, 0.37], 
         ["United Kingdom", "London", 10, 1.46]]
      assert_that(country_list.as_nested_array(), equal_to(expected_output))
```

<details>
  <summary>Implementation that makes the test pass</summary>

  ```python
  def as_nested_array(self):
    sorted_countries = self.sorted_by_population()
    return[[sorted_countries[i].name, 
            sorted_countries[i].capital, 
            sorted_countries[i].population, 
            self.standard_deviations_per_country()[i]] for i in range(len(self._countries))]
  ```
</details>

</details>

### A repository to export/import country data to the outside world

As outlined in the introduction, let's now define the ports (and adapters)
that take care of the communication with "the outside world".
