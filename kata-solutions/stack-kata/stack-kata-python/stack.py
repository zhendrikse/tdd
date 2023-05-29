class Stack:
  def __init__(self):
    self.size = 0
    self.element = [-1] * 2

  def is_empty(self) -> bool:
    return self.size == 0

  def pop(self) -> int:
    if self.is_empty() == True:
      raise KeyError("Stack underflow")
    self.size -= 1
    return self.element[self.size]

  def push(self, value:int) -> None:
    self.element[self.size] = value
    self.size += 1
