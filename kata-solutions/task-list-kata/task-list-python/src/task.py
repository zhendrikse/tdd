from datetime import date
from typing import Union
from src.task_id import TaskId


class Task:
  def __init__(self, id:TaskId, description: str) -> None:
    self.id = id
    self.validate_description(description)
    self.description = description
    self.deadline = date.today()
    self.has_deadline = False

  def get_id(self) -> TaskId:
    return self.id

  def get_deadline(self) -> Union[date, None]:
    return self.deadline if self.has_deadline else None

  def set_deadline(self, due_date:date) -> None:
    self.has_deadline = True
    self.deadline = due_date

  def validate_description(self, description:str) -> None:
    if not description:
      raise ValueError("Description cannot be empty")