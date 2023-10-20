import pandas as pnds

class ExcelDataReader:
    def __init__(self, excel_file_name):
        self._excel_file_name = excel_file_name

    def get_sheet_by_name(self, sheet_name):
        return pnds.read_excel(
            io = self._excel_file_name,
            engine = "openpyxl",
            header = 0,
            sheet_name = sheet_name)
        