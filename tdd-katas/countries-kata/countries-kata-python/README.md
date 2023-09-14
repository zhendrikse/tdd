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
   $ poetry add requests
   $ poetry install
   ``` 
5. Depending on the approach chosen

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

This forces us to define a `Country` and a `CountryList` class:


<details>
  <summary>Code to make the test pass</summary>

  ```python
@dataclass
class Country:
    name: str
    capital: str
    population: int
  
  def as_string(self):
    return self.name + "," + self.capital + "," + str(self.population)
# ...
  
class CountryList:
    def __init__(self, countries):
        self._countries = countries
        
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
@pytest.fixture(autouse=True)
def country_list(self):
  return CountryList(COUNTRY_LIST_FOR_TESTING)

# ...

def test_given_a_country_list_it_calculates_the_average_population(self, country_list):
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
    standard_deviation = self.standard_deviation()
    return [
      round(abs(self.average_population() - country.population) / standard_deviation, 2) 
      for country in self.sorted_by_population()]
  ```
</details>
</details>

## Preparations for input and output

### Preparation 1: list of countries as nested array

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

### Preparation 2: ports to the outside world

As outlined in the introduction, let's now define the ports (and adapters)
that take care of the communication to "the outside world". We'll put
them in their own file `ports_adapters.py` for now:

```python
class CountriesOutputPort(Protocol):
  def write(self, country_list) -> None:
      pass

class CountriesInputPort(Protocol):
  def load_all(self) -> List[Country]:
      pass
```

## Import of country data

Given the above `CountriesInputPort`, we can now define
two adapters that we will use in our tests

<details>
  <summary>Input adapters for our tests</summary>

```python
class EmptyCountriesInputAdapterStub:
  def load_all(self) -> List[Country]:
      return []

class CountriesInputAdapterStub:
  def load_all(self) -> List[Country]:
      return COUNTRY_LIST_FOR_TESTING
```
</details>

Next, we can make use of these adapters in our tests:

<details>
  <summary>Modifying the tests to use the input adapters</summary>

```python
class TestEmptyCountryList:
  @pytest.fixture(autouse = True)
  def country_list(self):
      return CountryList(input_port = EmptyCountriesInputAdapterStub())

  # ...
  # Tests with empty country list
  # ...
  
class TestFilledCountryList:
  @pytest.fixture(autouse = True)
  def country_list(self):
      return CountryList(input_port = CountriesInputAdapterStub())      

  # ...
  # Tests with filled country list
  # ...
``` 

and the production code

```python
class CountryList:
  def __init__(self, input_port = RestCountriesInputAdapter()):
    self._countries = input_port.load_all()

  # ...
```

where for now

```python
class RestCountriesInputAdapter:
  def load_all(self) -> List[Country]:
      pass
```
</details>

If we want to interface to the real countries data REST endpoint, we 
may want to implement our `RestCountriesInputAdapter` all the way.

<details>
  <summary><code>RestCountriesInputAdapter</code> implementation</summary>

```python
class RestCountriesInputAdapter:
  def country_from_json(self, country_json):
    return Country(
      country_json.get("name").get("common"),
      country_json.get("capital"),
      country_json.get("population"))
    
  def load_all(self) -> List[Country]:
    url = "https://restcountries.com/v3.1/all?fields=name,region,subregion,unMember,cca3,cca2,ccn3,capital,population"
    response = requests.get(url)
    if response.status_code != HTTPStatus.OK:
      raise RuntimeError(f"Fetching country data failed, HTTPStatus={response.status_code}")
      
    return [self.country_from_json(country_data) for country_data in response.json()]
```

Note that the capital is not 100% correct still, as some countries may come with
multiple capital cities.
</details>


## Export of country data

Given the above `CountriesOutputPort`, we can now define
a mock adapters that we will use in our tests

<details>
  <summary>Output adapter for our tests</summary>

```python
class MockCountriesOutputAdapter:
  def __init__(self, adapter_under_test):
    self._adapter_under_test = adapter_under_test
    
  def write(self, country_list) -> None:
    open_mock = mock_open()
    with patch("ports_adapters.open", open_mock, create=True):
        self._adapter_under_test.write(country_list)
  
    open_mock.assert_called_with("countries.csv", "w")
    open_mock.return_value.write.assert_has_calls([
      call(BELGIUM.as_string() + ',1.1\r\n'),             
      call(NETHERLANDS.as_string() + ',0.73\r\n'),
      call(PORTUGAL.as_string() + ',0.37\r\n'),
      call(UNITED_KINGDOM.as_string() + ',1.46\r\n')])   
```
</details>

Next, we can make use of these adapters in our tests:

<details>
  <summary>Modifying the tests to use the output adapter</summary>

```python
class TestFilledCountryList:
  @pytest.fixture(autouse = True)
  def country_list(self):
      return CountryList(
        CountriesInputAdapterStub(),
        MockCountriesOutputAdapter(CsvCountriesOutputAdapter()))

  # ...
  # Tests with filled country list
  # ...

  def test_write_to_csv(self, country_list):
    country_list.export()
```

where we have implemented the `CsvCountriesOutputAdapter` as

```python
class CsvCountriesOutputAdapter:
  def write(self, country_list) -> None:
    with open('countries.csv', 'w') as file:
        writer = csv.writer(file)
        #writer.writerow(header)
        writer.writerows(country_list.as_nested_array())
```
</details>

Note that the `CountryList` class is constructed with the real-world
adapters by default

```python
class CountryList:
  def __init__(self, 
               input_port = RestCountriesInputAdapter(),
               output_port = CsvCountriesOutputAdapter()):
    self._countries = input_port.load_all()
    self._output_port = output_port
``` 

Now we can easily and confidently run our country data converter 
by e.g. adding a `main` to the `CountryList` class:

```python
def main():
    CountryList().export()
    print("List with country data exported to countries.csv")

if __name__ == "__main__":
    main()
```

and execute it with `poetry run python src/country_list.py`.
