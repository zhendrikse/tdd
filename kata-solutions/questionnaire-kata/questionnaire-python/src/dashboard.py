import pandas as pnds
import plotly.express as plotly 
import streamlit as strmlit
from excel_data_reader import ExcelDataReader
from data_processor import DataProcessor

class Dashboard:
    def __init__(self, excel_file_name):
        selected_columns = ['Q4', 'Q4A_1', 'Q4A_2', 'Q6', 'Q8', 'HQ8', 'Q25', 'Q25A', 'Q25B', 'Q25C', 'Q25D', 'Q26', 'Q27A', 'Q27B', 'Q28A', 'Q28B']
        data = DataProcessor(ExcelDataReader(excel_file_name)).get_survey_data(selected_columns)
        self._data = data[0]
        self._headers = data[1]

        self._init_webpage()

    def _init_webpage(self):
        # emoji's https://www.webfx.com/tools/emoji-cheat-sheet/
        strmlit.set_page_config(
            page_title = "Trein ritten dashboard", 
            page_icon = ":train:",
            layout = "wide")
        
    def _create_filter_for(self, column, filter_title):
        return strmlit.sidebar.multiselect(
            filter_title,
            options = self._data[column].unique(),
            default = self._data[column].unique()
        )

    def _render_dataframes(self):
        strmlit.sidebar.header("Please filter here:")
        Q26 = self._create_filter_for("Q26", "Duur reis naar station:")
        Q4 = self._create_filter_for("Q4", "Treinreisfrequentie de afgelopen 12 maanden:")
        Q25_Q25B = self._create_filter_for("Q25_Q25B", "Soort vervoermiddel gebracht:")
        self._data = self._data.query(
            "Q26 == @Q26 & Q4 == @Q4 & Q25_Q25B == Q25_Q25B"
        )

        strmlit.write(self._headers)
        strmlit.dataframe(self._data)

    def _create_bar_chart_for(self, column, title):
        data = self._data.value_counts(column) 
        return plotly.bar(
            data,
            #x = "count",
            #y = travel_frequency_data.index,
            #orientation = "h",
            title=title,
            template="plotly_white"
            )

    def _create_pie_chart_for(self, column, title):
        labels = self._data.value_counts(column).index
        values = self._data.value_counts(column).values
    
        return plotly.pie(
            labels = labels, 
            values = values,
            names = labels,
            title=title,
            template="plotly_white"
        )

    def _plot_charts(self):
        travel_frequency_histogram = self._create_bar_chart_for("Q4", "<b>Travel freqency</b>")
        travel_motivation_histogram = self._create_bar_chart_for("HQ8", "<b>Travel motivation</b>")

        self._col1, self._col2 = strmlit.columns(2)            
        with self._col1:
            strmlit.plotly_chart(travel_frequency_histogram)
        with self._col2:
            strmlit.plotly_chart(travel_motivation_histogram)

        strmlit.plotly_chart(self._create_pie_chart_for("Q25_Q25B", "<b>Transport to station</b>"))
        
        with self._col1:
            strmlit.plotly_chart(self._create_pie_chart_for("Q25C_Q25D_Q27A_Q28A", "<b>Own means of transport to station</b>"))
        with self._col2:
            strmlit.plotly_chart(self._create_pie_chart_for("Q27B_Q28B", "<b>With own <em>electric</em> car or bike to station</b>"))
    
    def render(self):
        self._render_dataframes()
        self._plot_charts()


if __name__ == '__main__':
    dashboard = Dashboard("../../../tdd-katas/questionnaire-kata/ritten-jan_mar_2023.xlsx")
    dashboard.render()
