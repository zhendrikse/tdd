# Introduction

Please read the general [introduction to the countries kata](../README.md) first!

# Getting started

Carry out the following steps in order:

1. Create an intial Python kata set-up as described
   [here](https://github.com/zhendrikse/tdd/tree/master/cookiecutter).
   Choose 'n' when prompted for the rSpec syntax. The code coverage is optional.
2. Remove the `.py` files in the `src` and `test` directories, but leave the
   `__init__.py` files untouched!
4. Copy the `country.py` file into the `src` directory 
5. Copy the `countries_test.py` file into the `test` directory
6. Run the test and veriffy all assertions are still valid: 
   it is testing the real API after all, which may have changed!
   ```
   $ poetry install
   $ ./run_tests.sh
   ``` 

## Running the tests

```bash
$ ./run_tests.sh
```

# Implementation

## Design considerations

We can use a nested array [to create a CSV file](https://www.pythontutorial.net/python-basics/python-write-csv-file/):

```python
import csv

header = ['name', 'capital', 'region', 'subregion', 'population', 'cca3', 'cca2', 'ccn3', 'unMember']
data = [
    ['Jordan', 'Amman', 'Asia', 'Western Asia', '10203140', 'JOR', 'JO', '400', 'true' 
],
    #  ...
]

with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)
```

Bearing this in mind, tt makes sense to define a `CountriesRestRepository` 
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

