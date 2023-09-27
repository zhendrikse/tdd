import pytest
from hamcrest import *
from report_generator import ReportGenerator

#CURRENT_DIR = Path.cwd()
#DATA_DIR = CURRENT_DIR.parent / "data"
DATA_DIR = "test/data/"

DATA_FILE1 = DATA_DIR + "misc_data1.txt"
DATA_FILE2 = DATA_DIR + "misc_data2.txt"
DATA_FILE3 = DATA_DIR + "empty.txt"


expected1 = """missing values: 2
highest number: 99.0
most common words: john
occurrences of most common: 4
#####
numbers: [1.0, 2.0, 99.0, 6.72, 2.0, 2.0, 2.0]
words: ['john', 'doe', 'john', 'john', 'was', 'here', 'this', 'is', 'totally', 'random', 'john']"""

expected2 = """missing values: 3
highest number: 101.0
most common words: doe, john
occurrences of most common: 4
#####
numbers: [1.0, 2.0, 101.0, 6.72, 2.0, 2.0, 67.0, 2.0]
words: ['john', 'doe', 'john', 'john', 'doe', 'was', 'doe', 'here', 'this', 'is', 'totally', 'random', 'john', 'doe']"""

expected3 = """missing values: 0
highest number: None
most common words: 
occurrences of most common: 0
#####
numbers: []
words: []"""


class TestReportGeneration:

  def test_data_file_1(self):
      assert_that(ReportGenerator.get_report(DATA_FILE1), equal_to(expected1))

  def test_data_file_2(self):
      assert_that(ReportGenerator.get_report(DATA_FILE2), equal_to(expected2))

  def test_empty_data_file(self):
      assert_that(ReportGenerator.get_report(DATA_FILE3), equal_to(expected3))

