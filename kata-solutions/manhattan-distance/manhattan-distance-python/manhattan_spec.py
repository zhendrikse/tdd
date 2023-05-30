from mamba import description, it, context, before
from expects import expect, equal, raise_error, be_false, be_true
from point import Point

def manhattan_distance(point_a, point_b):
  return point_a.distance_to(point_b)
  
with description("Manhattan distance") as self:
  with it("has zero distance to itself in one dimension"):
    expect(manhattan_distance(Point(0), Point(0))).to(equal(0))
  
  with it("has distance to a point on the right in one dimension"):
    expect(manhattan_distance(Point(0), Point(3))).to(equal(3))
  
  with it("has distance to a point on the left in one dimension"):
    expect(manhattan_distance(Point(0), Point(-3))).to(equal(3))

  with it("has zero distance to itself in two dimensions"):
    expect(manhattan_distance(Point(0, 0), Point(0, 0))).to(equal(0))
  
  with it("has distance to a point on the top right in two dimensions"):
    expect(manhattan_distance(Point(0, 0), Point(3, 4))).to(equal(7))
  
  with it("has distance to a point on the bottom left in two dimensions"):
    expect(manhattan_distance(Point(-1, -2), Point(-4, -5))).to(equal(6))
  
  with it("has distance to a point in three dimensions"):
    expect(manhattan_distance(Point(-1, -2, -3), Point(-4, -5, -6))).to(equal(9))
    
