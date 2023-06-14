from mamba import description, it, context
from expects import expect, equal, raise_error, be_a
from src.task import TaskId, Task

with description(TaskId) as self:
  with context("Creating a task ID"):
    with it("throws an exception when ID is negative"):
      expect(lambda: TaskId(-1)).to(raise_error(ValueError, "ID cannot be negative"))

    with it("throws an exception when ID contains spaces"):
      expect(lambda: TaskId("1 2")).to(raise_error(ValueError, "ID contains spaces"))

    with it("throws an exception when ID contains non-alphanumeric chars"):
      expect(lambda: TaskId("1#2")).to(raise_error(ValueError, "ID contains special characters"))

    with it("creates a task when integer ID is non-negative"):
      expect(TaskId(0)).to(be_a(TaskId))
      expect(TaskId(0).get_value()).to(equal(0))
    
    with it("creates a task when ID is alphanumeric"):
      expect(TaskId("ab1234")).to(be_a(TaskId))
      expect(TaskId("ab1234").get_value()).to(equal("ab1234"))

    with context("Given a task ID as int"):
      with it("is equal to an equal ID"):
        expect(TaskId(123)).to(equal(TaskId(123)))
      with it("is unequal to an unequal ID"):
        expect(TaskId(123)).not_to(equal(TaskId(1)))
      with it("is unequal to another class"):
        expect(TaskId(123)).not_to(equal(Task(TaskId(0), "todo")))      

    with context("Given a task ID as string"):
      with it("is equal to an equal ID"):
        expect(TaskId("123")).to(equal(TaskId("123")))
      with it("is unequal to an unequal ID"):
        expect(TaskId("123")).not_to(equal(TaskId("1")))
      with it("is unequal to another class"):
        expect(TaskId("123")).not_to(equal(Task(TaskId(0), "todo")))      