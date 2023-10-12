import pytest
from hamcrest import *
from raw_data_reader import RawDataReader
import pandas as pnds

class TestRawDataReader:
    @pytest.fixture(autouse=True)
    def data_reader(self):
        return RawDataReader("test/ritten-jan_mar_2023.xlsx")

    def test_replace_header_codes(self, data_reader):
        assert_that(data_reader.header_values()[3], equal_to('Treinreisfrequentie afgelopen 12 maanden (q4)'))

    def test_header_description_for_non_existing_column_code(self, data_reader):
        assert_that(data_reader.find_header_description_for('does_not_exist'), equal_to("does_not_exist"))


    def test_header_description_for_existing_column_code(self, data_reader):
        assert_that(data_reader.find_header_description_for('Q2'), equal_to("Geslacht kind (q2)"))
        assert_that(data_reader.find_header_description_for('Q59'), equal_to("Samenstelling huishouden (q59)"))

    def test_updated_dataframe_headers(self, data_reader):
        updated_frame = data_reader.combined_sheets_dataframe()
        headers = list(updated_frame)
        assert_that(data_reader.header_values(), equal_to(headers))

    def test_read_questionnaire(self, data_reader):
        expected_res = pnds.Series([
            "Een jongen", 
            "Een jongen", 
            "Een meisje", 
            "Een meisje", 
            "Wil niet zeggen", 
            "Een meisje", 
            "Een jongen", 
            "Een meisje", 
            "Een meisje", 
            "Een jongen"])
        
        pnds.testing.assert_series_equal(data_reader._ritten['Q2'], expected_res, check_names=False)

