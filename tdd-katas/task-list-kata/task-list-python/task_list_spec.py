from mamba import description, it, context
from expects import expect, be
from task_list import TaskList

with description(TaskList) as self:
  with context("Given a new empty task list"):
    with it("contains no elements"):
      expect(TaskList().count()).to(be(0))