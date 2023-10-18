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

    def test_header_description_for_non_existing_column_code(self, data_processor):
        assert_that(data_processor.find_header_description_for('does_not_exist'), equal_to("does_not_exist"))

    def test_header_description_for_existing_column_code(self, data_processor):
        assert_that(data_processor.find_header_description_for('Q2'), equal_to("Geslacht kind (q2)"))
        assert_that(data_processor.find_header_description_for('Q59'), equal_to("Samenstelling huishouden (q59)"))

    def test_read_questionnaire(self, data_processor):
        selected_columns = ('Q2', 'Q4A_1', 'Q4A_2')
        test_dataframe = data_processor.get_dataframe_for(selected_columns)

        expected_res = pnds.Series(["Een jongen", "Een jongen", "Een meisje", "Een meisje", "Wil niet zeggen", 
            "Een meisje", "Een jongen", "Een meisje", "Een meisje", "Een jongen"])
        
        assert_that(test_dataframe.shape, equal_to((ROWS_TO_READ, len(selected_columns))))
        pnds.testing.assert_series_equal(test_dataframe['Q2'], expected_res, check_names=False)

    def test_replace_text_in_numerical_column(self, data_processor):
        selected_columns = ('Q2', 'Q4A_1', 'Q4A_2')
        test_dataframe = data_processor.get_dataframe_for(selected_columns)

        test_dataframe = data_processor.remove_text_from_numerical_columns(test_dataframe, ['Q4A_1', 'Q4A_2'])

        assert_that(test_dataframe['Q4A_1'].tolist(), not(has_item('Weet ik niet')))
        assert_that(test_dataframe['Q4A_2'].tolist(), not(has_item('Weet ik niet')))

    def test_get_data_frame_for_list_of_columns(self, data_processor):
        selected_columns = ('Q2', 'Q4', 'Q5', 'Q6')
        test_dataframe = data_processor.get_dataframe_for(selected_columns)

        headers = list(test_dataframe)
        assert_that(list(test_dataframe), has_items(*selected_columns))
        assert_that(test_dataframe.shape, equal_to((ROWS_TO_READ, len(selected_columns))))
        #pnds.testing.assert_series_equal(list(test_dataframe), pnds.Series(selected_columns), check_names=False)

        expected_res = pnds.Series(["Nee", "Nee", "Nee", "Nee", "Nee", "Nee", "Nee", "Nee", "Nee", "Nee"])
        pnds.testing.assert_series_equal(test_dataframe['Q5'], expected_res, check_names=False)

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

