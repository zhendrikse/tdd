from typing import List
from task_list import TaskList
from task import Task


class QueryHandler:
  def __init__(self, tasklist:TaskList) -> None:
    self.tasklist = tasklist
  
  def handle_query(self, querty: str) -> List[Task]:
    return self.tasklist.todays_tasks()
