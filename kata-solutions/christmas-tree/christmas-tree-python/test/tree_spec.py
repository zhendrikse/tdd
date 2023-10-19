from mamba import description, it, context, before
from expects import expect, equal, raise_error, be_false, be_true

from tree import *

with description("Christmas tree") as self:
  with it("returns trunk when height is zero or less"):
     expect(christmas_tree(0)).to(equal(["|"]))

  with it("returns a tree when height is 1"):
     expect(christmas_tree(1)).to(equal(["*", 
                                         "|"]))
 
  with it("returns a tree when height is 2"):
     expect(christmas_tree(2)).to(equal([" * ", 
                                         "***", 
                                         " | "]))
  
  with it("returns a tree when height is 3"):
     expect(christmas_tree(3)).to(equal(["  *  ", 
                                         " *** ",  
                                         "*****", 
                                         "  |  "]))

