import pytest
from hamcrest import *
from country_list import CountryList, Country

class Testcountry_list:

  @pytest.fixture(autouse = True)
  def country_list(self):
      return CountryList(
         [Country("Netherlands", "Amsterdam", 4), 
          Country("Belgium", "Brussels", 3), 
          Country("Portugal", "Lissabon", 7), 
          Country("United kingdom", "London", 10)])

  def test_given_an_empty_country_list_it_calculates_the_average_population(self):
      assert_that(CountryList().average_population(), equal_to(0))

  def test_given_an_empty_country_list_it_calculates_the_standard_deviation(self):
      assert_that(CountryList().standard_deviation(), equal_to(0))

  def test_given_a_country_list_it_calculates_the_average_population(self, country_list):
      assert_that(country_list.average_population(), equal_to(6))

  def test_given_a_country_list_it_calculates_the_standard_deviation(self, country_list):
      assert_that(country_list.standard_deviation(), close_to(2.7386, 0.0001))

