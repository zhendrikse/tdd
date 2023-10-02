import pandas as pnds
# import plotly.express as plotly 
import streamlit as strmlit


class Dashboard:
    def __init__(self, excel_file_name):
        self._init_webpage()
        self._dataframe = self._init_dataframe(excel_file_name)

        if 'dataframe' not in strmlit.session_state:
            strmlit.dataframe(self._dataframe)


        if 'count' not in strmlit.session_state:
            strmlit.session_state.count = 0
        if 'title' not in strmlit.session_state:
            strmlit.session_state.title = "Calculator"
        self.col1, self.col2 = strmlit.columns(2)

    def _init_webpage(self):
        # emoji's https://www.webfx.com/tools/emoji-cheat-sheet/
        strmlit.set_page_config(
            page_title = "Trein ritten dashboard", 
            page_icon = ":train",
            layout = "wide")

    def _init_dataframe(self, excel_file_name):
        return pnds.read_excel(
            io = excel_file_name,
            engine = "openpyxl",
        #     sheet_name="NS Klimaat ritten - jan-mrt 202",
        #     skiprows="3",
        #     usecols="Q59:Q4",
            nrows = 10
        )

    def add(self):
        strmlit.session_state.count += 1

    def subtract(self):
        strmlit.session_state.count -= 1

    def tester(self):
        if 'tester' not in strmlit.session_state:
            strmlit.session_state.tester = "Tester"
        else:
            strmlit.session_state.tester = "Already tested"
        with self.col2:
            strmlit.write(f"Hello from the {strmlit.session_state.tester}!")

    def render(self):
        with self.col1:
            strmlit.button("Increment", on_click=self.add)
            strmlit.button("Subtract", on_click=self.subtract)
            strmlit.write(f'Count = {strmlit.session_state.count}')
        with self.col2:
            strmlit.button('test me', on_click=self.tester)



if __name__ == '__main__':
    dashboard = Dashboard("test/ritten-jan_mar_2023.xlsx")
    dashboard.render()