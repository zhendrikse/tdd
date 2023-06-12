class Stack:
  def __init__(self):
    self._size = 0
    self._elements = [-1] * 2

  def is_empty(self) -> bool:
    return self._size == 0

  def pop(self) -> int:
    if self.is_empty() == True:
      raise KeyError("Stack underflow")
    self._size -= 1
    return self._elements[self._size]

  def push(self, value:int) -> None:
    self._elements[self._size] = value
    self._size += 1
