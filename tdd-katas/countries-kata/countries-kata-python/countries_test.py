import pytest
from hamcrest import *
from country import Country
import requests, pytest
from http import HTTPStatus

API_URL = "https://restcountries.com/v3.1/all?fields=name,region,subregion,unMember,cca3,cca2,ccn3,capital,population"


class TestCountries:

  def test_a_new_Countries(self):
    response = requests.get(API_URL)
    if response.status_code == HTTPStatus.OK:
        countries = [Country.from_json(country_data) for country_data in response.json()]
        assert_that(countries, has_length(250))
        assert_that(countries[0].name, equal_to("Jordan"))
        assert_that(countries[0].region, equal_to("Asia"))
        assert_that(countries[0].subregion, equal_to("Western Asia"))
        assert_that(countries[0].unMember, is_(True))
        assert_that(countries[0].cca3, equal_to("JOR"))
        assert_that(countries[0].cca2, equal_to("JO"))
        assert_that(countries[0].ccn3, equal_to("400"))
        assert_that(countries[0].capital[0], equal_to("Amman"))
        assert_that(countries[0].population, equal_to(10203140))
      
    elif response.status_code == HTTPStatus.NOT_FOUND:
        raise requests.exceptions.InvalidURL
    else:
        raise requests.exceptions.RequestException



