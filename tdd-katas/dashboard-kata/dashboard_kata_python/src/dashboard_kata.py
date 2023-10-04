import pandas as pnds
# import plotly.express as plotly 
import streamlit as strmlit

col1 = "Q2"
col2 = "Q4"
col3 = "Dag_treinreis"
col4 = "Q18D"
col5 = "LeeftCat"
col6 = "vertrekstation"
col7 = "aankomststation"

class Dashboard:
    def __init__(self, excel_file_name):
        self._init_webpage()
        self._dataframe = self._read_data(excel_file_name)

        # if 'dataframe' not in strmlit.session_state:
        #     strmlit.dataframe(self._dataframe)


        if 'count' not in strmlit.session_state:
            strmlit.session_state.count = 0
        if 'title' not in strmlit.session_state:
            strmlit.session_state.title = "Calculator"
        self.col1, self.col2 = strmlit.columns(2)

    def _init_webpage(self):
        # emoji's https://www.webfx.com/tools/emoji-cheat-sheet/
        strmlit.set_page_config(
            page_title = "Trein ritten dashboard", 
            page_icon = ":train:",
            layout = "wide")

    def _read_data(self, excel_file_name):
        dataframe = pnds.read_excel(
            io = excel_file_name,
            engine = "openpyxl",
        #     sheet_name="NS Klimaat ritten - jan-mrt 202",
        #     skiprows="3",
        #     usecols="Q2:Q4",
            nrows = 20
        )
        return dataframe[[col1, col2, col3, col4, col5, col6, col7]]

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

    def _define_filters(self):
        strmlit.sidebar.header("Please filter here:")
        Dag_treinreis = strmlit.sidebar.multiselect(
            "Select the day:",
            options = self._dataframe["Dag_treinreis"].unique(),
            default = self._dataframe["Dag_treinreis"].unique()
        )
        Q2 = strmlit.sidebar.multiselect(
            "Select gender:",
            options = self._dataframe[col1].unique(),
            default = self._dataframe[col1].unique()
        )
        Q4 = strmlit.sidebar.multiselect(
            "Select days per week:",
            options = self._dataframe[col2].unique(),
            default = self._dataframe[col2].unique()
        )
        Q18D = strmlit.sidebar.multiselect(
            "Select purpose:",
            options = self._dataframe[col4].unique(),
            default = self._dataframe[col4].unique()
        )

        self._dataframe = self._dataframe.query(
            "Dag_treinreis == @Dag_treinreis & Q2 == @Q2 & Q4 == @Q4 & Q18D == @Q18D"
        )

        strmlit.dataframe(self._dataframe)

    def cleanse(self):
        self._dataframe = self._dataframe[self._dataframe[col1].isin(["Een jongen", "Een meisje"])]
        strmlit.dataframe(self._dataframe)
        

    def render(self):
        self._define_filters()

        with self.col1:
            strmlit.button("Increment", on_click=self.add)
            strmlit.button("Subtract", on_click=self.subtract)
            strmlit.write(f'Count = {strmlit.session_state.count}')
        with self.col2:
            strmlit.button('test me', on_click=self.tester)
            strmlit.button('Cleanse', on_click=self.cleanse)


if __name__ == '__main__':
    dashboard = Dashboard("test/ritten-jan_mar_2023.xlsx")
    dashboard.render()