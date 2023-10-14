import pandas as pnds
from typing import Protocol

class DataProcessor:
    def __init__(self, raw_data_reader):
        self._variables = raw_data_reader.variables
        self._ritten = raw_data_reader.ritten

    @property
    def ritten(self):
        return self._ritten

    def get_column_by_code(self, column_code):
        return self._ritten[column_code]

    def find_header_description_for(self, column_code):
        matching_row = self._variables[self._variables.iloc[:, 0] == column_code]
        if len(matching_row) != 1:
            return column_code

        row_for_header_code = matching_row.index[0]
        return self._variables.iloc[row_for_header_code, 1]

    def header_values(self):
        headers = list(self._ritten)
        return [self.find_header_description_for(header) for header in headers]

    @property
    def combined_sheets(self):
        new_headers = self.header_values()
        dataframe = self._ritten[0:] #take the data less the header row
        dataframe.columns = new_headers #set the header row as the df header
        return dataframe


    