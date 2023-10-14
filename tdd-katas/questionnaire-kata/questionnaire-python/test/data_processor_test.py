import pytest
from hamcrest import *
from excel_data_reader import ExcelDataReader
from data_processor import DataProcessor
import pandas as pnds
import io

from test_data import RITTEN_DATA, VARIABLES_DATA

ROWS_TO_READ = 10
DATA_ROW_COUNT = 225

class StubRawDataReader:
    def __init__(self, excel_file_name):
        self._variables = pnds.read_json(io.StringIO(VARIABLES_DATA))
        self._ritten = pnds.read_json(io.StringIO(RITTEN_DATA))

    @property
    def ritten(self):
        return self._ritten
        
    @property
    def variables(self):
        return self._variables

class TestDataProcessor:
    @pytest.fixture(autouse=True)
    def data_reader(self):
        return DataProcessor(StubRawDataReader("test/ritten-jan_mar_2023.xlsx"))

    def test_replace_header_codes(self, data_reader):
        assert_that(data_reader.header_values()[3], equal_to('Treinreisfrequentie afgelopen 12 maanden (q4)'))

    def test_header_description_for_non_existing_column_code(self, data_reader):
        assert_that(data_reader.find_header_description_for('does_not_exist'), equal_to("does_not_exist"))

    def test_header_description_for_existing_column_code(self, data_reader):
        assert_that(data_reader.find_header_description_for('Q2'), equal_to("Geslacht kind (q2)"))
        assert_that(data_reader.find_header_description_for('Q59'), equal_to("Samenstelling huishouden (q59)"))

    def test_updated_dataframe_headers(self, data_reader):
        updated_frame = data_reader.combined_sheets
        headers = list(updated_frame)

        assert_that(data_reader.combined_sheets.shape, equal_to((ROWS_TO_READ, DATA_ROW_COUNT)))
        assert_that(data_reader.header_values(), equal_to(headers))

    def test_read_questionnaire(self, data_reader):
        expected_res = pnds.Series(["Een jongen", "Een jongen", "Een meisje", "Een meisje", "Wil niet zeggen", 
            "Een meisje", "Een jongen", "Een meisje", "Een meisje", "Een jongen"])
        
        assert_that(data_reader.ritten.shape, equal_to((ROWS_TO_READ, DATA_ROW_COUNT)))
        pnds.testing.assert_series_equal(data_reader.ritten['Q2'], expected_res, check_names=False)

    def test_bla(self, data_reader):
        print(data_reader.combined_sheets.value_counts('Grootte huishouden (q60)', normalize=True))
        print(data_reader.combined_sheets.value_counts('Geslacht (q58)', normalize=True))
        #print(data_reader.combined_sheets.value_counts('Leeftijdscategorie (q57)', normalize=True))
        #print(data_reader.ritten.value_counts('Q65', normalize=True))

        #print(data_reader.ritten.value_counts('Q56_1', normalize=True))
        print(data_reader.combined_sheets.value_counts("Treinreisfrequentie afgelopen 12 maanden (q4)", normalize=True))
        #print(data_reader.combined_sheets.groupby(by=["Geslacht (q58)"]).sum())

