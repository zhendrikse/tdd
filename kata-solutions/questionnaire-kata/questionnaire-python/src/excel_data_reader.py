import pandas as pnds

class ExcelDataReader:
    def __init__(self, excel_file_name):
        self._variables = self._read_sheet(excel_file_name, "variabelen")
        self._ritten = self._read_sheet(excel_file_name, "NS Klimaat ritten - jan-mrt 202")

    @property
    def ritten(self):
        return self._ritten

    @property
    def variables(self):
        return self._variables

    def _read_sheet(self, excel_file_name, sheet_name):
        return pnds.read_excel(
            io = excel_file_name,
            engine = "openpyxl",
            header = 0,
            sheet_name = sheet_name)
    