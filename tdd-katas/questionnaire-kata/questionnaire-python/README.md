# Introduction

Please read the general [introduction to the questionnaire kata](../README.md) first!

# Getting started

First, create an intial Python kata set-up as described [here](https://github.com/zhendrikse/tdd/tree/master/cookiecutter).

Next, go the the newly created project directory and consult
the provided ``README.md`` in there.

# 1. Reading the data from CSV

## Obtaining the raw data from Excel

1. Import the required libraries
   ```bash
   $ poetry add pandas
   $ poetry add ...
   ```
2. Read the Excel from CSV
   <details>
     <summary>Reading raw data from Excel</summary>

   ```python
   import pandas as pnds

   def _read_variable_sheet(self):
      return pnds.read_excel(
         io = "ritten-jan_mar_2023.xlsx",
         engine = "openpyxl",
         header = 0,
         sheet_name = "variabelen")

    def _read_ns_klimaat_ritten_sheet(self):
      return pnds.read_excel(
         io = "ritten-jan_mar_2023.xlsx",
         engine = "openpyxl",
         nrows = 20)
   ```
   </details>

# 2. Structuring the data

## Cleansing the data

In column `Q4A_1` there is a string "Weet ik niet", that cannot be converted to an integer. 

# 4. Data preprocessing

# 5. EDA

# 6. Insights / reports / graphs

# References

- [Turn An Excel Sheet Into An Interactive Dashboard Using Python (Streamlit)](https://www.youtube.com/watch?v=Sb0A9i6d320)
- [Example Streamlit class-based application](https://learningtofly.dev/blog/streamlit-class-based-app)
- [Analyze Survey Data with Python for Beginners | Pandas](https://www.youtube.com/watch?v=B-lliwc0ZMk)
- [How to Analyze Survey Data with Python for Beginners](https://www.dataquest.io/blog/how-to-analyze-survey-data-python-beginner/)
