import pytest
from typing import List
from hamcrest import close_to, equal_to, assert_that
from country_list import CountryList, Country
from ports_adapters import CsvCountriesOutputAdapter, RestCountriesInputAdapter

from unittest.mock import patch, mock_open, call

NETHERLANDS = Country("Netherlands", "Amsterdam", 4)
PORTUGAL = Country("Portugal", "Lissabon", 7)
BELGIUM = Country("Belgium", "Brussels", 3)
UNITED_KINGDOM = Country("United Kingdom", "London", 10)

COUNTRY_LIST_FOR_TESTING = [NETHERLANDS, PORTUGAL, BELGIUM, UNITED_KINGDOM]

class EmptyCountriesInputAdapterStub:
  def load_all(self) -> List[Country]:
      return []

class TestEmptyCountryList:
  @pytest.fixture(autouse = True)
  def country_list(self):
      return CountryList(input_port = EmptyCountriesInputAdapterStub())
  
  def test_given_an_empty_country_list_it_calculates_the_average_population(self, country_list):
      assert_that(country_list.average_population(), equal_to(0))

  def test_given_an_empty_country_list_it_calculates_the_standard_deviation(self, country_list):
      assert_that(country_list.standard_deviation(), equal_to(0))



class CountriesInputAdapterStub:
  def load_all(self) -> List[Country]:
      return COUNTRY_LIST_FOR_TESTING

class MockCountriesOutputAdapter:
  def __init__(self, adapter_under_test):
    self._adapter_under_test = adapter_under_test
    
  def write(self, country_list) -> None:
    open_mock = mock_open()
    with patch("ports_adapters.open", open_mock, create=True):
        self._adapter_under_test.write(country_list)
  
    open_mock.assert_called_with("countries.csv", "w")
    open_mock.return_value.write.assert_has_calls([
      call(BELGIUM.as_string() + ',1.1\r\n'),             
      call(NETHERLANDS.as_string() + ',0.73\r\n'),
      call(PORTUGAL.as_string() + ',0.37\r\n'),
      call(UNITED_KINGDOM.as_string() + ',1.46\r\n')])   
  
class TestFilledCountryList:
  @pytest.fixture(autouse = True)
  def country_list(self):
      return CountryList(
        CountriesInputAdapterStub(),
        MockCountriesOutputAdapter(CsvCountriesOutputAdapter()))
  
  def test_sorted_list_by_population_size(self, country_list):
      assert_that(country_list.sorted_by_population()[0], equal_to(BELGIUM))
      assert_that(country_list.sorted_by_population()[1], equal_to(NETHERLANDS))
      assert_that(country_list.sorted_by_population()[2], equal_to(PORTUGAL))
      assert_that(country_list.sorted_by_population()[3], equal_to(UNITED_KINGDOM))

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

  def test_write_to_csv(self, country_list):
    country_list.export()
