import pandas as pnds
from excel_data_reader import ExcelDataReader

class DataProcessor:
    def __init__(self, raw_data_reader):
        self._variables = raw_data_reader.variables
        self._ritten = raw_data_reader.ritten
    
    def get_survey_data(self, selected_columns):
        data = self.get_dataframe_for(selected_columns)
        data = self.merge_two_columns(data, 'Q25', 'Q25B')
        data = self.merge_two_columns(data, 'Q25C', 'Q25D')
        data = self.merge_two_columns(data, 'Q27A', 'Q28A')
        data = self.merge_two_columns(data, 'Q27B', 'Q28B')
        data = self.merge_two_columns(data, 'Q25C_Q25D', 'Q27A_Q28A')
        data = self.remove_text_from_numerical_columns(data, ['Q4A_1', 'Q4A_2'])

        headers = [self.find_header_description_for(header) for header in selected_columns]
        header_description_map = dict(zip(selected_columns, headers))

        return data, pnds.DataFrame([header_description_map])

    def get_column_by_code(self, column_code):
        return self._ritten[column_code]

    def find_header_description_for(self, column_code):
        matching_row = self._variables[self._variables.iloc[:, 0] == column_code]
        if len(matching_row) != 1:
            return column_code

        row_for_header_code = matching_row.index[0]
        return self._variables.iloc[row_for_header_code, 1]

    def get_dataframe_for(self, column_codes_list):
        return self._ritten.loc[:, self._ritten.columns.isin(column_codes_list)]

    def remove_text_from_numerical_columns(self, dataframe, column_codes_list):
        for column in column_codes_list:
            new_column_values = dataframe[column].replace(['Weet ik niet'], None)
            dataframe = dataframe.assign(**{column:new_column_values})
        return dataframe

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



    