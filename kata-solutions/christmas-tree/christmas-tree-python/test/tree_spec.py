from mamba import description, it, context, before
from expects import expect, equal, raise_error, be_false, be_true

def pad_with_spaces(content, space_count):
  return space_count * " " + content + space_count * " "

def generate_layer(star_count, space_count):
  return pad_with_spaces("*" * star_count, space_count)

def christmas_tree(height):
  tree = [generate_layer(2 * i - 1, height - i) for i in range(1, height + 1)]
  return tree + [pad_with_spaces("|", height - 1)]

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

