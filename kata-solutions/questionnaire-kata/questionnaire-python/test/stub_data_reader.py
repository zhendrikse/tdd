import pandas as pnds
import io

from test_data import RITTEN_DATA, VARIABLES_DATA

class StubDataReader:
  def get_sheet_by_name(self, sheet_name):
      if sheet_name == "NS Klimaat ritten - jan-mrt 202":
          return pnds.read_json(io.StringIO(RITTEN_DATA))
      elif sheet_name == "variabelen":
        return pnds.read_json(io.StringIO(VARIABLES_DATA))
      else:
        raise Exception("Unknown test data sheet requested") 