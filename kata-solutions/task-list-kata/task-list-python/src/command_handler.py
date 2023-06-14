from typing import List
from datetime import datetime
from src.task_list import TaskList
from src.task_id import TaskId

class CommandHandler:
  def __init__(self, tasklist:TaskList) -> None:
    self.tasklist = tasklist

  def validate_agument_count(self, arguments:List[str], count: int) -> None:
      if len(arguments) != count:
        raise ValueError("Invalid arguments")

  def handle_deadline_command(self, arguments:List[str]) -> None:
      self.validate_agument_count(arguments, 3)
      task_id = TaskId(arguments[1])
      task_date = datetime.strptime(arguments[2], '%d-%m-%Y').date()
      self.tasklist.update_task(task_id, task_date)

  def handle_delete_command(self, arguments:List[str]) -> None:
      self.validate_agument_count(arguments, 2)
      task_id = TaskId(arguments[1])
      self.tasklist.delete_task(task_id)

  def handle_command(self, command: str) -> None:
    if command.startswith("deadline"):
      self.handle_deadline_command(command.split(" "))
    elif command.startswith("delete"):
      self.handle_delete_command(command.split(" "))
    else:
      raise ValueError("Invalid command")
