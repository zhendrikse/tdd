from typing import List
from datetime import date
from task import Task, TaskId

class TaskList:
  def __init__(self) -> None:
    self.tasks:List[Task] = []

  def add_tasks(self, tasks: List[Task]) -> None:
    for task in tasks:
      self.add_task(task)

  def add_task(self, task:Task) -> None:
    if self.has_task_with_id(task.get_id()):
      raise ValueError("Duplicate ID")
    self.tasks.append(task)

  def get_tasks_by_id(self, id:TaskId) -> List[Task]:
    return [x for x in self.tasks if (x.get_id() == id)]

  def has_task_with_id(self, id: TaskId) -> bool:
    return any(self.get_tasks_by_id(id))

  def get_task_by_id(self, task_id: TaskId) -> Task:
    if not self.has_task_with_id(task_id):
      raise ValueError("No such task")
    return self.get_tasks_by_id(task_id)[0]

  def update_task(self, task_id: TaskId, deadline: date) -> None:
      task = self.get_task_by_id(task_id)
      task.set_deadline(deadline)

  def delete_task(self, task_id: TaskId) -> None:
      task = self.get_task_by_id(task_id)
      self.tasks.remove(task)

  def count(self) -> int:
    return len(self.tasks)

  def todays_tasks(self) -> List[Task]:
    return [x for x in self.tasks if x.get_deadline() == date.today()]
    #return filter(lambda x: x.due_date == date.today(), self.tasks)
