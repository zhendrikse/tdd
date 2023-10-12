import pandas as pnds
# import plotly.express as plotly 
import streamlit as strmlit
from typing import Protocol


class RawDataReader(Protocol):
    def from_excel(self, excel_file_name):
        ...

class RawDataReader:
    def __init__(self, excel_file_name):
        self._variables = self._read_variable_sheet(excel_file_name)
        self._ritten = self._read_ns_klimaat_ritten_sheet(excel_file_name)

    def get_column_by_code(self, column_code):
        return self._ritten[column_code]

    def find_header_description_for(self, column_code):
        matching_column = self._variables[self._variables.iloc[:, 0] == column_code]
        if len(matching_column) != 1:
            return column_code

        row_for_header_code = matching_column.index[0]
        return self._variables.iloc[row_for_header_code, 1]

    def header_values(self):
        headers = list(self._ritten)
        return [self.find_header_description_for(header) for header in headers]

    def combined_sheets_dataframe(self):
        new_headers = self.header_values()
        dataframe = self._ritten[1:] #take the data less the header row
        dataframe.columns = new_headers #set the header row as the df header
        return dataframe

    def _read_variable_sheet(self, excel_file_name):
        return pnds.read_excel(
            io = excel_file_name,
            engine = "openpyxl",
            header = 0,
            sheet_name = "variabelen")

    def _read_ns_klimaat_ritten_sheet(self, excel_file_name):
        return pnds.read_excel(
            io = excel_file_name,
            engine = "openpyxl",
        #    header = 0,
        #    index_col = 0,
        #    usecols = "A:Z",
        #    dtype = str, 
        #     sheet_name="NS Klimaat ritten - jan-mrt 202",
        #     skiprows="3",
        #     usecols="Q2:Q4",
            nrows = 10
        )
    