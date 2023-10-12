
import pytest
from hamcrest import *
from dashboard_kata import Dashboard
import pandas as pnds
import plotly.express as plotly 
import streamlit as strmlit


class Testdashboard_kata_python:

    def test_a_new_dashboard(self):
        pass
        # dashboard = Dashboard("test/ritten-jan_mar_2023.xlsx") 

        # expected_res = pnds.Series([
        #     "Een jongen", 
        #     "Een jongen", 
        #     "Een meisje", 
        #     "Een meisje", 
        #     "Wil niet zeggen", 
        #     "Een meisje", 
        #     "Een jongen", 
        #     "Een meisje", 
        #     "Een meisje", 
        #     "Een jongen"])
        # pnds.testing.assert_series_equal((dashboard._dataframe['Q2']), expected_res, check_names=False)

