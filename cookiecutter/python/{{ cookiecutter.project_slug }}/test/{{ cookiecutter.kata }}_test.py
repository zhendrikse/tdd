{% if cookiecutter.rspec_syntax == "y" %}
from mamba import description, it, context, before
from expects import expect, be, raise_error, be_true, be_false
from {{ cookiecutter.kata }} import {{ cookiecutter.kata }}

with description({{ cookiecutter.kata }}) as self:
  with context("Given a new {{ cookiecutter.kata }}"):
    with it(" expects True to equal True"):
      expect(True).to(be_false)
{% endif %} {% if cookiecutter.rspec_syntax == "n" %}
import pytest
from hamcrest import *
from {{ cookiecutter.kata }} import {{ cookiecutter.kata }}

class Test{{ cookiecutter.kata }}:

  def test_a_new_{{ cookiecutter.kata }}(self):
      assert True is False
      # Hamcrest style
      # assert_that(True, equal_to(False))
{% endif %}
