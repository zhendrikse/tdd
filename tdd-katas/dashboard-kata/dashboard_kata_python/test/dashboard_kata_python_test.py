 
import pytest
from hamcrest import *
from dashboard_kata_python import dashboard_kata_python
import pandas as pnds

class Testdashboard_kata_python:

  def test_a_new_dashboard_kata_python(self):
      # Hamcrest style
      # assert_that(True, equal_to(False))

      dataframe = pnds.read_excel(
          io = "ritten-jan_mar_2023.xlsx",
          engine = "openpyxl",
          sheet_name = "", 
          skiprows = "3",
          usecols ="B:R",
          nrows = 1000
      )
      print (dataframe)


