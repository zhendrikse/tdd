import pytest
from hamcrest import *
from {{ cookiecutter.kata }} import {{ cookiecutter.kata }}


class Test{{ cookiecutter.kata }}:

  def test_a_new_{{ cookiecutter.kata }}(self):
      assert True is False
      # Hamcrest style
      # assert_that(True, equal_to(False))
