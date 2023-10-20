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

   This enables us to write our first tests:

   ```python
   TOTAL_ROWS = 10
   TOTAL_COLUMNS = 225
   TOTAL_VARIABLES = 421

   class TestDataProcessor:

     def test_get_survey_data_sheet_with_variables(self):
       assert_that(DataProcessor(StubDataReader()).get_survey_data()[1].shape, equal_to((TOTAL_VARIABLES, 2)))

     def test_get_survey_data_sheet_with_ritten(self):
       assert_that(DataProcessor(StubDataReader()).get_survey_data()[0].shape, equal_to((TOTAL_ROWS, TOTAL_COLUMNS)))
   ```
   
   Which we can make pass by implementing the `DataProcessor`

   ```python 
   class DataProcessor:
     def __init__(self, survey_data_reader: SurveyDataReader):
       self._data_reader = survey_data_reader
    
     def get_survey_data(self):
       return self._data_reader.get_sheet_by_name("NS Klimaat ritten - jan-mrt 202"),\
         self._data_reader.get_sheet_by_name("variabelen")
   ```

   Where have defined a `SurveyDataReader`

   ```python
   class SurveyDataReader(Protocol):
     def get_sheet_by_name(self, sheet_name):
       ...
   ```

   and its associated stub implementation

   ```python
   from test_data import RITTEN_DATA, VARIABLES_DATA

   class StubDataReader:
     def get_sheet_by_name(self, sheet_name):
       if sheet_name == "NS Klimaat ritten - jan-mrt 202":
         return pnds.read_json(io.StringIO(RITTEN_DATA))
       elif sheet_name == "variabelen":
         return pnds.read_json(io.StringIO(VARIABLES_DATA))
       else:
         raise Exception("Unknown test data sheet requested") 
   ```
   </details>
4. Reading the production data
   
   Obviuously, we also need an implementation of the `SurveyDataReader`
   that imports the production data

   <details>
     <summary>Reading the data from Excel</summary>

   ```python
   class ExcelDataReader:
    def __init__(self, excel_file_name):
        self._excel_file_name = excel_file_name

    def get_sheet_by_name(self, sheet_name):
        return pnds.read_excel(
            io = self._excel_file_name,
            engine = "openpyxl",
            header = 0,
            sheet_name = sheet_name)
   ```
   </details>

# 2. Structuring the data

## Selecting the appropriate columns

As we are only interested in a limited subset of all the data, we 
would first like to construct a dataframe containing the relevant
columns only:
- `Q4`, `Q4A_1`, `Q4A_2`, `Q6`, `Q8`, `HQ8`, `Q25`, `Q25A`, `Q25B`, `Q25C`, `Q25D`, `Q26`, `Q27A`, `Q27B`, `Q28A`, `Q28B`

<details>
<summary>Dataframe with selected subset of columns</summary>

The test could look like so:

```python
def test_get_data_frame_for_list_of_columns(self, data_processor):
    ritten_dataframe = data_processor.get_survey_data()[0]
    
    selected_columns = ('Q2', 'Q4', 'Q5', 'Q6')
    dataframe = data_processor.get_dataframe_for(ritten_dataframe, selected_columns)

    headers = list(dataframe)
    assert_that(headers, has_items(*selected_columns))
    assert_that(dataframe.shape, equal_to((TOTAL_ROWS, len(selected_columns))))
```

with associated implementation

```python
  def get_dataframe_for(self, ritten_dataframe, column_codes_list):
    return ritten_dataframe.loc[:, ritten_dataframe.columns.isin(column_codes_list)]
```
</details>

## Cleansing the data

In columns `Q4A_1` and `Q4A_2` there are strings "Weet ik niet", that cannot be converted to an integer. 

<details>
<summary>Cleansing strings from numerical columns</summary>

```python
def test_replace_text_in_numerical_column(self, data_processor):
    ritten_dataframe = data_processor.get_survey_data()[0]
    selected_columns = ('Q2', 'Q4A_1', 'Q4A_2')
    dataframe = data_processor.get_dataframe_for(ritten_dataframe, selected_columns)

    dataframe = data_processor.remove_text_from_numerical_columns(dataframe, ['Q4A_1', 'Q4A_2'])

    assert_that(dataframe['Q4A_1'].tolist(), not(has_item('Weet ik niet')))
    assert_that(dataframe['Q4A_2'].tolist(), not(has_item('Weet ik niet')))
```

Which can be made green by

```python
def remove_text_from_numerical_columns(self, dataframe, column_codes_list):
    for column in column_codes_list:
        new_column_values = dataframe[column].replace(
            ['Weet ik niet'], None)
        dataframe = dataframe.assign(**{column: new_column_values})
    return dataframe
```
</details>

# 3. Data preprocessing

## Finding descriptions for the headers

We need to be able to find meaningful description in the "variabelen"
sheet for the cryptic headers in the "ritten sheet", e.g.
`Q2` &rarr; "Geslacht kind (q2)".

<details>
<summary>Finding description for the headers in the ritten sheet</summary>

Let's first see what happens in case we are looking for a non-existent header value:

```python
def test_header_description_for_non_existing_column_code(self, data_processor):
    variables_dataframe = data_processor.get_survey_data()[1]
    assert_that(data_processor.find_header_description_for(
        variables_dataframe, 'does_not_exist'), equal_to("does_not_exist"))
```

We can implement this like so:

```python
def find_header_description_for(self, variables_dataframe, column_code):
    matching_row = variables_dataframe[variables_dataframe.iloc[:, 0] == column_code]
    if len(matching_row) != 1:
        return column_code
```

When we look for existing header values, we should get the value 
contained in the "variabelen" sheet:

```python
def test_header_description_for_existing_column_code(self, data_processor):
    variables_dataframe = data_processor.get_survey_data()[1]
    assert_that(data_processor.find_header_description_for(
        variables_dataframe, 'Q2'), equal_to("Geslacht kind (q2)"))
    assert_that(data_processor.find_header_description_for(
        variables_dataframe, 'Q59'), equal_to("Samenstelling huishouden (q59)"))
```

Our method should now be extended a little bit:

```python
def find_header_description_for(self, variables_dataframe, column_code):
    matching_row = variables_dataframe[variables_dataframe.iloc[:, 0] == column_code]
    if len(matching_row) != 1:
        return column_code

    row_for_header_code = matching_row.index[0]
    return variables_dataframe.iloc[row_for_header_code, 1]
```
</details>

## Combining columns

In order to get the appropriate information from the survey, we
need to be able to combine two columns, e.g. the columns `Q25` and
`Q25B` ("Vervoermiddel naar station (q25)" and "Soort vervoermiddel gebracht (q25b)").

<details>
<summary>Merging two columns into one</summary>

```python
def test_merge_columns(self, data_processor):
    ritten_dataframe = data_processor.get_survey_data()[0]
    selected_columns = ('Q25A', 'Q25', 'Q25B')
    dataframe = data_processor.get_dataframe_for(ritten_dataframe, selected_columns)
    
    dataframe = data_processor.merge_two_columns(dataframe, 'Q25', 'Q25B')

    expected_res = pnds.Series(["Fiets", "Lopend", "Fiets", "Auto", "Lopend", "Auto", "Fiets", "Auto", "Lopend", "Met de taxi, NS zonetaxi, regiotaxi"])
    pnds.testing.assert_series_equal(dataframe['Q25_Q25B'], expected_res, check_names=False)      
```

We can make this test pass with

```python
def merge_two_columns(self, dataframe, column_1, column_2):
    # replace empty values by None
    dataframe = dataframe.replace(r'^\ *$', None, regex=True) 
    # drop two columns that are going to be merged
    dataframe_minus_cols = dataframe.drop([column_1, column_2], axis=1)
    # new dataframe with two columns merged
    dataframe = pnds.concat([dataframe_minus_cols, dataframe[column_1].combine_first(dataframe[column_2])], 
        axis=1)
    # rename newly merged column
    dataframe.rename(columns={column_1:column_1 + "_" + column_2}, inplace=True)
    return dataframe
```
</details>

## The final data set suitable for analysis

Let's finally extend the `DataProcessor` with a method that returns the 
final data set suitable for analysis:
- Containing the columns `Q4`, `Q4A_1`, `Q4A_2`, `Q6`, `Q8`, `HQ8`, `Q25`, `Q25A`, `Q25B`, `Q25C`, `Q25D`, `Q26`, `Q27A`, `Q27B`, `Q28A`, `Q28B`
- Combined columns
   - `Q25` and `Q25B` ("Vervoermiddel naar station (q25)" and "Soort vervoermiddel gebracht (q25b)")
   - `Q25C` and `Q25D` ("Soort OV naar station (q25c)" and "Soort scooter naar station (q25d)")
   - `Q27A` and `Q28A` ("Soort auto naar station (q27a)" and "Soort fiets naar station (q28a)")
   - `Q27B` and `Q28B` ("Elektrische auto (q27b)" and "Elektrische fiets of scooter (q28b)")
   - Two of the above combinations need to be combined again, namely the newly
     combined columns `Q25C_Q25D` and `Q27A_Q28A`

<details>
<summary>Final data set for analysis</summary>

In the final data set, the original 16 columns should have been merged to
eleven columns in total:

```python
def test_get_survey_data(self, data_processor):
    selected_columns = ['Q4', 'Q4A_1', 'Q4A_2', 'Q6', 'Q8', 'HQ8', 'Q25', 'Q25A', 'Q25B', 'Q25C', 'Q25D', 'Q26', 'Q27A', 'Q27B', 'Q28A', 'Q28B']
    survey_data = data_processor.get_processed_survey_data(selected_columns)
    data = survey_data[0]
    headers = survey_data[1]

    assert_that(headers.shape, equal_to((1, len(selected_columns))))
    assert_that(data.shape, equal_to((TOTAL_ROWS, 11)))
```

This turns green with

```python
def get_processed_survey_data(self, selected_columns):
    data = self.get_survey_data()
    ritten = data[0]
    variabelen = data[1]
    ritten = self.get_dataframe_for(ritten, selected_columns)
    ritten = self.merge_two_columns(ritten, 'Q25', 'Q25B')
    ritten = self.merge_two_columns(ritten, 'Q25C', 'Q25D')
    ritten = self.merge_two_columns(ritten, 'Q27A', 'Q28A')
    ritten = self.merge_two_columns(ritten, 'Q27B', 'Q28B')
    ritten = self.merge_two_columns(ritten, 'Q25C_Q25D', 'Q27A_Q28A')
    ritten = self.remove_text_from_numerical_columns(ritten, ['Q4A_1', 'Q4A_2'])

    headers = [self.find_header_description_for(variabelen, header) for header in selected_columns]
    header_description_map = dict(zip(selected_columns, headers))

    return ritten, pnds.DataFrame([header_description_map])
```

</details>


# 4. EDA

# 5. Insights / reports / graphs

# References

- [Turn An Excel Sheet Into An Interactive Dashboard Using Python (Streamlit)](https://www.youtube.com/watch?v=Sb0A9i6d320)
- [Example Streamlit class-based application](https://learningtofly.dev/blog/streamlit-class-based-app)
- [Analyze Survey Data with Python for Beginners | Pandas](https://www.youtube.com/watch?v=B-lliwc0ZMk)
- [How to Analyze Survey Data with Python for Beginners](https://www.dataquest.io/blog/how-to-analyze-survey-data-python-beginner/)
