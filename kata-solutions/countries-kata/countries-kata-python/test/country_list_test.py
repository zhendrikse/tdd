import pytest
from hamcrest import close_to, equal_to, assert_that
from country_list import CountryList, Country

class Testcountry_list:

  @pytest.fixture(autouse = True)
  def country_list(self):
      return CountryList(
         [Country("Netherlands", "Amsterdam", 4), 
          Country("Portugal", "Lissabon", 7), 
          Country("Belgium", "Brussels", 3), 
          Country("United Kingdom", "London", 10)])
  
  def test_sorted_list_by_population_size(self, country_list):
      assert_that(country_list.sorted_by_population()[0].name, equal_to("Belgium"))
      assert_that(country_list.sorted_by_population()[1].name, equal_to("Netherlands"))
      assert_that(country_list.sorted_by_population()[2].name, equal_to("Portugal"))
      assert_that(country_list.sorted_by_population()[3].name, equal_to("United Kingdom"))

  def test_given_an_empty_country_list_it_calculates_the_average_population(self):
      assert_that(CountryList().average_population(), equal_to(0))

  def test_given_an_empty_country_list_it_calculates_the_standard_deviation(self):
      assert_that(CountryList().standard_deviation(), equal_to(0))

  def test_given_a_country_list_it_calculates_the_average_population(self, country_list):
      assert_that(country_list.average_population(), equal_to(6))

  def test_given_a_country_list_it_calculates_the_standard_deviation(self, country_list):
      assert_that(country_list.standard_deviation(), close_to(2.7386, 0.0001))

  def test_standard_deviations_per_country(self, country_list):
      assert_that(country_list.standard_deviations_per_country(), equal_to([1.10, 0.73, 0.37, 1.46]))

  def test_country_list_as_nested_array(self, country_list):
      expected_output = [
         ["Belgium", "Brussels", 3, 1.10], 
         ["Netherlands", "Amsterdam", 4, 0.73], 
         ["Portugal", "Lissabon", 7, 0.37], 
         ["United Kingdom", "London", 10, 1.46]]
      assert_that(country_list.as_nested_array(), equal_to(expected_output))

