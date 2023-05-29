class Employee():
  def __init__(self, name: str):
    self.name = name
          
  def __eq__(self, other): 
      if not isinstance(other, Employee):
          return NotImplemented

      return self.name == other.name # and self.bar == other.bar