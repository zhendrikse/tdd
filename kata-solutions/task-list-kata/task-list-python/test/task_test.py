from mamba import description, it, before, context
from expects import expect, be_none, raise_error, equal
from datetime import date
from task import Task, TaskId

with description(Task) as self:
  with context("When creating a task"):
    with it("throws an exception when ID contains non-alphanumeric chars"):
      expect(lambda: Task(TaskId("1#2"), "todo")).to(raise_error(ValueError, "ID contains special characters"))

    with it("throws an exception when description is empty"):
      expect(lambda: Task(TaskId(1), "")).to(raise_error(ValueError, "Description cannot be empty"))

  with description("When setting a deadline on a task") as self:
    with before.each:
      self.task = Task(TaskId(0), "todo")
    
    with it("does not have any deadline beforehand"):
      expect(self.task.get_deadline()).to(be_none)
    
    with it("has deadline set"):
      self.task.set_deadline(date.today())
      expect(self.task.get_deadline()).to(equal(date.today()))
