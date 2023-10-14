import pandas as pnds

class ExcelDataReader:
    def __init__(self, excel_file_name):
        self._variables = self._read_variable_sheet(excel_file_name)
        self._ritten = self._read_ns_klimaat_ritten_sheet(excel_file_name)

    @property
    def ritten(self):
        return self._ritten

    @property
    def variables(self):
        return self._variables

    def _read_variable_sheet(self, excel_file_name):
        return pnds.read_excel(
            io = excel_file_name,
            engine = "openpyxl",
            header = 0,
            sheet_name = "variabelen")

    def _read_ns_klimaat_ritten_sheet(self, excel_file_name):
        return pnds.read_excel(
            io = excel_file_name,
            engine = "openpyxl",
            # sheet_name="NS Klimaat ritten - jan-mrt 202",
            nrows = 200
        )
    