import pandas as pnds
import plotly.express as plotly 
import streamlit as strmlit
from excel_data_reader import ExcelDataReader
from data_processor import DataProcessor

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
        data_processor = DataProcessor(ExcelDataReader(excel_file_name))
        self._ritten = data_processor.ritten
        self._overview = data_processor.combined_sheets

        # if 'dataframe' not in strmlit.session_state:
        #     strmlit.dataframe(self._ritten)

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
            options = self._ritten["Dag_treinreis"].unique(),
            default = self._ritten["Dag_treinreis"].unique()
        )
        Q2 = strmlit.sidebar.multiselect(
            "Select gender:",
            options = self._ritten[col1].unique(),
            default = self._ritten[col1].unique()
        )
        Q4 = strmlit.sidebar.multiselect(
            "Select days per week:",
            options = self._ritten[col2].unique(),
            default = self._ritten[col2].unique()
        )
        Q18D = strmlit.sidebar.multiselect(
            "Select purpose:",
            options = self._ritten[col4].unique(),
            default = self._ritten[col4].unique()
        )

        self._ritten = self._ritten.query(
            "Dag_treinreis == @Dag_treinreis & Q2 == @Q2 & Q4 == @Q4 & Q18D == @Q18D"
        )

        strmlit.dataframe(self._ritten)

    def cleanse(self):
        self._ritten = self._ritten[self._ritten[col1].isin(["Een jongen", "Een meisje"])]
        strmlit.dataframe(self._ritten)

    def plot_chart(self):
        travel_frequency_data = self._overview.value_counts("Treinreisfrequentie afgelopen 12 maanden (q4)") 
        bar_chart = plotly.bar(
            travel_frequency_data,
            #x = "count",
            #y = travel_frequency_data.index,
            #orientation = "h",
            title="<b>Travel freqency</b>",
            #color_discrete_sequence = ["#0083B8"] * len (travel_frequency_data),
            template="plotly_white"
            )
        strmlit.plotly_chart(bar_chart)
        

    def render(self):
        self._define_filters()

        with self.col1:
            strmlit.button("Increment", on_click=self.add)
            strmlit.button("Subtract", on_click=self.subtract)
            strmlit.write(f'Count = {strmlit.session_state.count}')
        with self.col2:
            strmlit.button('test me', on_click=self.tester)
            strmlit.button('Cleanse', on_click=self.cleanse)

        self.plot_chart()


if __name__ == '__main__':
    dashboard = Dashboard("test/ritten-jan_mar_2023.xlsx")
    dashboard.render()