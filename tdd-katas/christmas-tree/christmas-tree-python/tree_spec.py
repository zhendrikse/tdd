from mamba import description, it, context, before
from expects import expect, equal, raise_error, be_false, be_true

with description("Christmas tree") as self:
  with it("returns trunk when height is zero or less"):
     expect(christmas_tree(0)).to(equal(["|"]))
