import pytest
from hamcrest import *
from report_generator import ReportGenerator

class TestReportGeneration:

  def test_data_file_1(self):
    expected = """missing values: 2
highest number: 99.0
most common words: john
occurrences of most common: 4
#####
numbers: [1.0, 2.0, 99.0, 6.72, 2.0, 2.0, 2.0]
words: ['john', 'doe', 'john', 'john', 'was', 'here', 'this', 'is', 'totally', 'random', 'john']"""
    assert_that(ReportGenerator.get_report("test/data/misc_data1.txt"), equal_to(expected))

  def test_data_file_2(self):
    expected = """missing values: 3
highest number: 101.0
most common words: doe, john
occurrences of most common: 4
#####
numbers: [1.0, 2.0, 101.0, 6.72, 2.0, 2.0, 67.0, 2.0]
words: ['john', 'doe', 'john', 'john', 'doe', 'was', 'doe', 'here', 'this', 'is', 'totally', 'random', 'john', 'doe']"""
    assert_that(ReportGenerator.get_report("test/data/misc_data2.txt"), equal_to(expected))

  def test_empty_data_file(self):
    expected = """missing values: 0
highest number: None
most common words: 
occurrences of most common: 0
#####
numbers: []
words: []"""
    assert_that(ReportGenerator.get_report("test/data/empty.txt"), equal_to(expected))

