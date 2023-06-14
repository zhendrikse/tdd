from typing import Union

class TaskId:
  def __init__(self, id:Union[int, str]) -> None:
    self.validate_id(id)
    self.id_int = -1 if type(id) is str else id
    self.id_string = id if type(id) is str else str(id)

  def get_value(self) -> Union[int, str]:
    return self.id_string if self.id_int == -1 else self.id_int

  def validate_int_id(self, id:int) -> None:
      if id < 0:
        raise ValueError("ID cannot be negative")
  
  def validate_id(self, id:Union[int, str]) -> None:
    if type(id) is int:
      self.validate_int_id(id)
    if type(id) is str:
      self.validate_string_id(id)

  def validate_string_id(self, id:str) -> None:
    if (" " in id):
      raise ValueError("ID contains spaces")
    if not id.isalnum():
      raise ValueError("ID contains special characters")
  
  def __eq__(self, other):
    if isinstance(other, TaskId):
        return self.id_string == other.id_string
    return False