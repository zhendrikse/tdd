from mamba import description, it, context, before
from expects import expect, be, raise_error, be_true, be_false
from stack import Stack


with description(Stack) as self:
  with context("Given a new stack"):
    with it("True equals False"):
      expect(True).to(be_false)