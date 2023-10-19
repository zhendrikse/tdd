# Introduction

Please read the general [introduction to the questionnaire kata](../README.md) first!

# Getting started

First, create an intial Python kata set-up as described [here](https://github.com/zhendrikse/tdd/tree/master/cookiecutter).

Next, you may want go the the newly created project directory and consult
the provided `README.md` in there.

# 1. Obtaining the raw data

This kata comes with a real-world example of a survey. The answers from
the respondents are collected in the `ritten-jan_mar_2023.xlsx` file.

Since this file is somewhat unwieldly to use in our tests (and we
shouldn't be using the file system our unit tests anyhow!), this 
kata comes with a excerpt from the `ritten-jan_mar_2023.xlsx` file:
`test_data.py`. This file can be copied into your folder containing
the unit tests.

## Obtaining the raw data from Excel

1. Copy the file `test_data.py` into the `test` folder
2. Import the required libraries
   ```bash
   $ poetry add pandas openpyxl streamlit plotly-express
   ```
3. Preparing the test data
   <details>
     <summary>Stubbing the reading from Excel</summary>

   In our tests, we can use the data from the `test_data.py` 
   file like so:

   ```python
   # Using the data from test_data.py
   import io
   import pandas as pnds
   from test_data import RITTEN_DATA, VARIABLES_DATA

   variables = pnds.read_json(io.StringIO(VARIABLES_DATA))
   ritten = pnds.read_json(io.StringIO(RITTEN_DATA))
   ```

   This enables us to write our first test:

   ```python
   TOTAL_ROWS = 10
   TOTAL_COLUMNS = 225

   class TestDataProcessor:
      def test_get_survey_data(self):
        assert_that(DataProcessor(StubDataReader()).get_survey_data().shape, equal_to((TOTAL_ROWS, TOTAL_COLUMNS)))
   ```
   
   Which we can make pass by implementing the `DataProcessor`

   ```python 
   class DataProcessor:
     def __init__(self, raw_data_reader):
       self._data_reader = raw_data_reader
    
     def get_survey_data(self):
       return self._data_reader.get_ritten_data()
   ```

   Analogously, we can test and read the other sheet `VARIABLES_DATA`.
   </details>
4. Reading the data from the `ritten-jan_mar_2023.xlsx` Excel file
   
   Let's first define a generic data reader

   ```python
   from typing import Protocol

   class DataReader(Protocol):
     def get_ritten_data(self):
       ...
    
    def get_variables_data(self):    
       ...
   ```

# 2. Structuring the data

## Cleansing the data

In column `Q4A_1` there is a string "Weet ik niet", that cannot be converted to an integer. 

# 3. Data preprocessing

# 4. EDA

# 5. Insights / reports / graphs

# References

- [Turn An Excel Sheet Into An Interactive Dashboard Using Python (Streamlit)](https://www.youtube.com/watch?v=Sb0A9i6d320)
- [Example Streamlit class-based application](https://learningtofly.dev/blog/streamlit-class-based-app)
- [Analyze Survey Data with Python for Beginners | Pandas](https://www.youtube.com/watch?v=B-lliwc0ZMk)
- [How to Analyze Survey Data with Python for Beginners](https://www.dataquest.io/blog/how-to-analyze-survey-data-python-beginner/)
