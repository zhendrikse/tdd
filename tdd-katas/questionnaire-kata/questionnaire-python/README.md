# Introduction

This kata practises Exploration Data Analysis (EDA) based on 
[a questionnaire](questionnaire.md) sent out to
questionnaire sent to train passengers in the Netherlands.

In this kata we will practice TDD for some of the steps 
that are normally to be found in a data analysis flow.

## Introduction data analysis

![Data analysis](./images/data-analysis.webp)

Let's see how the above steps are applied in this kata:

1. **Raw data**: 
   We will start with a raw data/excel file containing the answers to the questions in 
   [the questionnaire](questionnaire.md). These data need to be converted into a format
   (dataframes), in order to facilitate further data processing.
2. **Structured data**: 
   The raw data coming from the excel file is still unstructured. A couple of additional
   steps may be required to structure these data so that they can be analyzed:
   - Cleaning the Unstructured Data
   - Check to see if it should be kept or deleted
   - Choose the technology for data collection and storage based on company requirements
   - Entity Extraction
3. **Data preprocessing**: Data preprocessing is an important step in the data mining process 
   that involves cleaning and transforming raw data to make it suitable for analysis. 
   Some common steps in data preprocessing include:
   - Feature selection
   - Data Integration
   - Data Transformation
   - Data Reduction
   - Data Discretization
   - Data Normalization
4. **EDA**:
5. **Insights/reports/graphs**:

# Processing the raw data

## 1. Reading the data from CSV

1. Read the Excel from CSV
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

# Structuring the data

# Data preprocessing

# EDA

# Insights / reports / graphs

# References

- [Turn An Excel Sheet Into An Interactive Dashboard Using Python (Streamlit)](https://www.youtube.com/watch?v=Sb0A9i6d320)
- [Example Streamlit class-based application](https://learningtofly.dev/blog/streamlit-class-based-app)