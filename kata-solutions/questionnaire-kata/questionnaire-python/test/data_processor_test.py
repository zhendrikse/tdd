import pytest
from hamcrest import *
import pandas as pnds

from stub_data_reader import StubRawDataReader
from data_processor import DataProcessor

ROWS_TO_READ = 10
DATA_ROW_COUNT = 225


class TestDataProcessor:
    @pytest.fixture(autouse=True)
    def data_processor(self):
        return DataProcessor(StubRawDataReader("test/ritten-jan_mar_2023.xlsx"))

    def test_replace_header_codes(self, data_processor):
        assert_that(data_processor.header_values()[3], equal_to('Treinreisfrequentie afgelopen 12 maanden (q4)'))

    def test_header_description_for_non_existing_column_code(self, data_processor):
        assert_that(data_processor.find_header_description_for('does_not_exist'), equal_to("does_not_exist"))

    def test_header_description_for_existing_column_code(self, data_processor):
        assert_that(data_processor.find_header_description_for('Q2'), equal_to("Geslacht kind (q2)"))
        assert_that(data_processor.find_header_description_for('Q59'), equal_to("Samenstelling huishouden (q59)"))

    def test_updated_dataframe_headers(self, data_processor):
        updated_frame = data_processor.combined_sheets
        headers = list(updated_frame)

        assert_that(data_processor.combined_sheets.shape, equal_to((ROWS_TO_READ, DATA_ROW_COUNT)))
        assert_that(data_processor.header_values(), equal_to(headers))

    def test_read_questionnaire(self, data_processor):
        expected_res = pnds.Series(["Een jongen", "Een jongen", "Een meisje", "Een meisje", "Wil niet zeggen", 
            "Een meisje", "Een jongen", "Een meisje", "Een meisje", "Een jongen"])
        
        assert_that(data_processor.ritten.shape, equal_to((ROWS_TO_READ, DATA_ROW_COUNT)))
        pnds.testing.assert_series_equal(data_processor.ritten['Q2'], expected_res, check_names=False)

    def test_get_data_frame_for_list_of_columns(self, data_processor):
        selected_columns = ('Q2', 'Q4', 'Q5', 'Q6')
        test_data_frame = data_processor.get_dataframe_for(selected_columns)
        assert_that(data_processor.combined_sheets.shape, equal_to((ROWS_TO_READ, DATA_ROW_COUNT)))
        expected_res = pnds.Series(["Nee", "Nee", "Nee", "Nee", "Nee", "Nee", "Nee", "Nee", "Nee", "Nee"])
        pnds.testing.assert_series_equal(test_data_frame['Q5'], expected_res, check_names=False)

    def test_merge_columns(self, data_processor):
        dataframe = data_processor.get_dataframe_for(('Q25A', 'Q25', 'Q25B'))
        dataframe = data_processor.merge_two_columns(dataframe, 'Q25', 'Q25B')

        expected_res = pnds.Series(["Fiets", "Lopend", "Fiets", "Auto", "Lopend", "Auto", "Fiets", "Auto", "Lopend", "Met de taxi, NS zonetaxi, regiotaxi"])
        pnds.testing.assert_series_equal(dataframe['Q25_Q25B'], expected_res, check_names=False)

    #def test_bla(self, data_processor):
        #print(data_processor.combined_sheets.value_counts('Grootte huishouden (q60)', normalize=True))
        #print(data_processor.combined_sheets.value_counts('Geslacht (q58)', normalize=True))
        #print(data_processor.combined_sheets.value_counts('Leeftijdscategorie (q57)', normalize=True))
        #print(data_processor.ritten.value_counts('Q65', normalize=True))

        #print(data_processor.ritten.value_counts('Q56_1', normalize=True))
        #print(data_processor.combined_sheets.value_counts("Treinreisfrequentie afgelopen 12 maanden (q4)", normalize=True))
        #print(data_processor.combined_sheets.groupby(by=["Geslacht (q58)"]).sum())

