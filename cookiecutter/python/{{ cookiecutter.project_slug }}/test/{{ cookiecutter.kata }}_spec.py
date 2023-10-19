from mamba import description, it, context, before
from expects import expect, be, raise_error, be_true, be_false
from {{ cookiecutter.kata }} import {{ cookiecutter.kata }}


with description({{ cookiecutter.kata }}) as self:
  with context("Given a new {{ cookiecutter.kata }}"):
    with it(" expects True to equal True"):
      expect(True).to(be_false)
