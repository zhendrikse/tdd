import pandas as pnds
import plotly.express as plotly 
import streamlit as strmlit
from excel_data_reader import ExcelDataReader
from data_processor import DataProcessor

class Dashboard:
    def __init__(self, excel_file_name):
        self._init_webpage()
        data_processor = DataProcessor(ExcelDataReader(excel_file_name))
        #self._data = data_processor.ritten
        #self._variables = data_processor.variables
        self._data = data_processor.get_dataframe_for(
            ('Q4', 'Q4A_1', 'Q4A_2', 'Q6', 'Q8', 'HQ8', 'Q25', 'Q25A', 'Q25B', 'Q25C', 'Q25D', 'Q26', 'Q27A', 'Q27B', 'Q28A', 'Q28B'))
        self._data = data_processor.merge_two_columns(self._data, 'Q25', 'Q25B')
        self._data = data_processor.merge_two_columns(self._data, 'Q25C', 'Q25D')
        self._data = data_processor.merge_two_columns(self._data, 'Q27A', 'Q28A')
        self._data = data_processor.merge_two_columns(self._data, 'Q27B', 'Q28B')
        self._data = data_processor.merge_two_columns(self._data, 'Q25C_Q25D', 'Q27A_Q28A')

        if 'dataframe' not in strmlit.session_state:
            strmlit.dataframe(self._data)

        # if 'count' not in strmlit.session_state:
        #     strmlit.session_state.count = 0
        # if 'title' not in strmlit.session_state:
        #     strmlit.session_state.title = "Calculator"
        self.col1, self.col2 = strmlit.columns(2)

    def _init_webpage(self):
        # emoji's https://www.webfx.com/tools/emoji-cheat-sheet/
        strmlit.set_page_config(
            page_title = "Trein ritten dashboard", 
            page_icon = ":train:",
            layout = "wide")

    # def add(self):
    #     strmlit.session_state.count += 1

    # def subtract(self):
    #     strmlit.session_state.count -= 1

    # def tester(self):
    #     if 'tester' not in strmlit.session_state:
    #         strmlit.session_state.tester = "Tester"
    #     else:
    #         strmlit.session_state.tester = "Already tested"
    #     with self.col2:
    #         strmlit.write(f"Hello from the {strmlit.session_state.tester}!")

    def _define_filters(self):
        strmlit.sidebar.header("Please filter here:")
        Q6 = strmlit.sidebar.multiselect(
            "Laatst gemaakte treinreis:",
            options = self._data['Q6'].unique(),
            default = self._data['Q6'].unique()
        )
        Q4 = strmlit.sidebar.multiselect(
            "Treinreisfrequentie de afgelopen 12 maanden:",
            options = self._data['Q4'].unique(),
            default = self._data['Q4'].unique()
        )
        Q25_Q25B = strmlit.sidebar.multiselect(
            "Soort vervoermiddel gebrach:",
            options = self._data['Q25_Q25B'].unique(),
            default = self._data['Q25_Q25B'].unique()
        )

        self._data = self._data.query(
            "Q6 == @Q6 & Q4 == @Q4 & Q25_Q25B == Q25_Q25B"
        )


    def cleanse(self):
        self._data = self._data[self._data[col1].isin(["Een jongen", "Een meisje"])]
        strmlit.dataframe(self._data)

    def plot_chart(self):
        travel_frequency_data = self._data.value_counts("Q4") 
        bar_chart = plotly.bar(
            travel_frequency_data,
            #x = "count",
            #y = travel_frequency_data.index,
            #orientation = "h",
            title="<b>Travel freqency</b>",
            #color_discrete_sequence = ["#0083B8"] * len (travel_frequency_data),
            template="plotly_white"
            )

        travel_motivation_data = self._data.value_counts("HQ8")
        bar_chart_2 = plotly.bar(
            travel_motivation_data,
            #x = "count",
            #y = travel_frequency_data.index,
            #orientation = "h",
            title="<b>Travel Motivation</b>",
            #color_discrete_sequence = ["#0083B8"] * len (travel_frequency_data),
            template="plotly_white"
            )

        with self.col1:
            strmlit.plotly_chart(bar_chart)
        with self.col2:
            strmlit.plotly_chart(bar_chart_2)

        labels = self._data.value_counts("Q25_Q25B").index
        values = self._data.value_counts("Q25_Q25B").values
        #labels = [label if label.strip() else "Onbekend" for label in labels]

        pie_chart = plotly.pie(
            labels = labels, 
            values = values,
            names = labels,
            title="<b>Transport to station</b>",
            template="plotly_white"
        )
        strmlit.plotly_chart(pie_chart)
        
        eigen_vervoer_labels = self._data.value_counts("Q25C_Q25D_Q27A_Q28A").index
        eigen_vervoer_values = self._data.value_counts("Q25C_Q25D_Q27A_Q28A").values
        pie_chart_vervoer = plotly.pie(
            labels = eigen_vervoer_labels, 
            values = eigen_vervoer_values,
            names = eigen_vervoer_labels,
            title="<b>Own transport to station</b>",
            template="plotly_white"
        )
        with self.col1:
            strmlit.plotly_chart(pie_chart_vervoer)
        
        electrisch_vervoer_labels = self._data.value_counts("Q27B_Q28B").index
        electrisch_vervoer_values = self._data.value_counts("Q27B_Q28B").values
        pie_chart_electrisch = plotly.pie(
            labels = electrisch_vervoer_labels, 
            values = electrisch_vervoer_values,
            names = electrisch_vervoer_labels,
            title="<b>With own electric car or bike to station</b>",
            template="plotly_white"
        )
        with self.col2:
            strmlit.plotly_chart(pie_chart_electrisch)

    def render(self):
        self._define_filters()

        # option = strmlit.selectbox(
        #     'How would you like to be contacted?',
        #     self._variables.iloc[:, 1].to_list())
        # strmlit.write('You selected:', option)

        self.plot_chart()

        # with self.col1:
        #     strmlit.button("Increment", on_click=self.add)
        #     strmlit.button("Subtract", on_click=self.subtract)
        #     strmlit.write(f'Count = {strmlit.session_state.count}')
        # with self.col2:
        #     strmlit.button('test me', on_click=self.tester)
        #     strmlit.button('Cleanse', on_click=self.cleanse)


if __name__ == '__main__':
    dashboard = Dashboard("test/ritten-jan_mar_2023.xlsx")
    dashboard.render()