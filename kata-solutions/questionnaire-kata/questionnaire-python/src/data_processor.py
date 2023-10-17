import pandas as pnds
from typing import Protocol

class DataProcessor:
    def __init__(self, raw_data_reader):
        self._variables = raw_data_reader.variables
        self._ritten = raw_data_reader.ritten

    @property
    def ritten(self):
        return self._ritten

    @property
    def variables(self):
        return self._variables

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

    def get_dataframe_for(self, column_codes_list):
        return self._ritten.loc[:, self._ritten.columns.isin(column_codes_list)]

    def merge_two_columns(self, dataframe, column_1, column_2):
        # replace empty values by None
        dataframe = dataframe.replace(r'^\ *$', None, regex=True) 
        # drop two columns that are going to be merged
        dataframe_minus_cols = dataframe.drop([column_1], axis=1).drop([column_2], axis=1) #
        # new dataframe with two columns merged
        dataframe = pnds.concat([dataframe_minus_cols, dataframe[column_1].combine_first(dataframe[column_2])], 
            axis=1)
        # rename newly merged column
        dataframe.rename(columns={column_1:column_1 + "_" + column_2}, inplace=True)
        return dataframe

    @property
    def combined_sheets(self):
        new_headers = self.header_values()
        dataframe = self._ritten[0:] #take the data less the header row
        dataframe.columns = new_headers #set the header row as the df header
        return dataframe


    