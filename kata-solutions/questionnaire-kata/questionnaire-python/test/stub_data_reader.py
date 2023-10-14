import pandas as pnds
import io

from test_data import RITTEN_DATA, VARIABLES_DATA

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