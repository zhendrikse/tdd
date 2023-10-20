import pytest
from hamcrest import *
import io
import pandas as pnds

from data_processor import DataProcessor
from stub_data_reader import StubDataReader

TOTAL_ROWS = 10
TOTAL_COLUMNS = 225
TOTAL_VARIABLES = 421


class TestDataProcessor:
    @pytest.fixture(autouse=True)
    def data_processor(self):
        return DataProcessor(StubDataReader())
    
    def _dataframe_for_columns(self, selected_columns, data_processor):
        ritten_dataframe = data_processor.get_survey_data()[0]
        return data_processor.get_dataframe_for(ritten_dataframe, selected_columns)
    
    def test_get_survey_data_sheet_with_variables(self, data_processor):
        variables_dataframe = data_processor.get_survey_data()[1]
        assert_that(variables_dataframe.shape, equal_to((TOTAL_VARIABLES, 2)))

    def test_get_survey_data_sheet_with_ritten(self, data_processor):
        assert_that(data_processor.get_survey_data()[0].shape, equal_to((TOTAL_ROWS, TOTAL_COLUMNS)))

    def test_header_description_for_non_existing_column_code(self, data_processor):
        variables_dataframe = data_processor.get_survey_data()[1]
        assert_that(data_processor.find_header_description_for(
            variables_dataframe, 'does_not_exist'), equal_to("does_not_exist"))

    def test_header_description_for_existing_column_code(self, data_processor):
        variables_dataframe = data_processor.get_survey_data()[1]
        assert_that(data_processor.find_header_description_for(
            variables_dataframe, 'Q2'), equal_to("Geslacht kind (q2)"))
        assert_that(data_processor.find_header_description_for(
            variables_dataframe, 'Q59'), equal_to("Samenstelling huishouden (q59)"))
        
    def test_get_data_frame_for_list_of_columns(self, data_processor):
        selected_columns = ['Q2', 'Q4', 'Q5', 'Q6']
        dataframe = self._dataframe_for_columns(selected_columns, data_processor)

        headers = list(dataframe)
        assert_that(headers, has_items(*selected_columns))
        assert_that(dataframe.shape, equal_to((TOTAL_ROWS, len(selected_columns))))

        # Assert one column
        expected_res = pnds.Series(
            ["Nee", "Nee", "Nee", "Nee", "Nee", "Nee", "Nee", "Nee", "Nee", "Nee"])
        pnds.testing.assert_series_equal(dataframe['Q5'], expected_res, check_names=False)

    def test_replace_text_in_numerical_column(self, data_processor):
        dataframe = self._dataframe_for_columns(['Q2', 'Q4A_1', 'Q4A_2'], data_processor)

        dataframe = data_processor.remove_text_from_numerical_columns(dataframe, ['Q4A_1', 'Q4A_2'])

        assert_that(dataframe['Q4A_1'].tolist(), not(has_item('Weet ik niet')))
        assert_that(dataframe['Q4A_2'].tolist(), not(has_item('Weet ik niet')))

    def test_merge_columns(self, data_processor):
        dataframe = self._dataframe_for_columns(['Q25A', 'Q25', 'Q25B'], data_processor)
        
        dataframe = data_processor.merge_two_columns(dataframe, 'Q25', 'Q25B')

        expected_res = pnds.Series(["Fiets", "Lopend", "Fiets", "Auto", "Lopend", "Auto", "Fiets", "Auto", "Lopend", "Met de taxi, NS zonetaxi, regiotaxi"])
        pnds.testing.assert_series_equal(dataframe['Q25_Q25B'], expected_res, check_names=False)

    def test_get_survey_data(self, data_processor):
        selected_columns = ['Q4', 'Q4A_1', 'Q4A_2', 'Q6', 'Q8', 'HQ8', 'Q25', 'Q25A', 'Q25B', 'Q25C', 'Q25D', 'Q26', 'Q27A', 'Q27B', 'Q28A', 'Q28B']
        survey_data = data_processor.get_processed_survey_data(selected_columns)
        data = survey_data[0]
        headers = survey_data[1]

        assert_that(headers.shape, equal_to((1, len(selected_columns))))
        assert_that(data.shape, equal_to((TOTAL_ROWS, 11)))
        