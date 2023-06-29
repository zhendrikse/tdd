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

   **Greenfield scenario**:

   - Run `$ ./run_tests.sh` to run the test and veriffy that all
     assertions are still valid: we are testing a real production API,
     which may well have changed by the time you are reading this!

# Implementation

## Design considerations

We can use a nested array [to create a CSV file](https://www.pythontutorial.net/python-basics/python-write-csv-file/):

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

