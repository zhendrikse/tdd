import pandas as pnds

from survey_data_reader import SurveyDataReader


class DataProcessor:
    def __init__(self, survey_data_reader: SurveyDataReader):
        self._data_reader = survey_data_reader

    def find_header_description_for(self, variables_dataframe, column_code):
        matching_row = variables_dataframe[variables_dataframe.iloc[:, 0] == column_code]
        if len(matching_row) != 1:
            return column_code

        row_for_header_code = matching_row.index[0]
        return variables_dataframe.iloc[row_for_header_code, 1]
      
    def get_survey_data(self):
        return self._data_reader.get_sheet_by_name("NS Klimaat ritten - jan-mrt 202"),\
            self._data_reader.get_sheet_by_name("variabelen")

    def get_dataframe_for(self, ritten_dataframe, column_codes_list):
        return ritten_dataframe.loc[:, ritten_dataframe.columns.isin(column_codes_list)]

    def remove_text_from_numerical_columns(self, dataframe, column_codes_list):
        for column in column_codes_list:
            new_column_values = dataframe[column].replace(
                ['Weet ik niet'], None)
            dataframe = dataframe.assign(**{column: new_column_values})
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
    