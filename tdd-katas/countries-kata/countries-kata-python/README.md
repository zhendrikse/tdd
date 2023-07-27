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

We can use a nested array [to create a CSV file](https://www.pythontutorial.net/python-basics/python-write-csv-file/):

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

with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)
```
</details>

Bearing this in mind, it makes sense to define a `CountriesRestRepository` 
that retrieves a list of all countries from the countries API. It will be
the responsibility of this repository to hand us a list of countries with
the required data fields.

To make the dependency inversion principle explicit, we could opt for an
additional `CountriesRepository` interface, that belongs to our domain. 
This way, our domain really dictates the outside world what it wants 
to receive.

Analogously, we can also define a `CsvWriter` that receives this list of 
countries, converts it into a nested array of data fields, and feeds it
to the Python `csv.writer()`.


# Instructions for the greenfield approach

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


