from dataclasses import dataclass

#@dataclass(frozen = True)
class Point:
  def __init__(self, *args):
    self.coordinates = args

  def distance_to(self, other_point):
    if len(self.coordinates) != len(other_point.coordinates):  
      raise KeyError("Incompatible dimensions")

    #
    # S o l u t i o n  w i t h  f o r - n e x t  l o o p 
    #  
    # distance = 0
    # for i in range(len(self.coordinates)):
    #    distance += abs(other_point.coordinates[i] - self.coordinates[i]) 
    # return distance

    # P y t h o n i c  s o l u t i o n
    return sum(abs(x - y) for x, y in zip(other_point.coordinates, self.coordinates))

