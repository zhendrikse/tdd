from mamba import description, it, context, before
from expects import expect, be_empty, raise_error, have_length, be, equal
from datetime import datetime
from src.task_list import TaskList
from src.task import Task, TaskId
from src.command_handler import CommandHandler
from src.query_handler import QueryHandler

with description(TaskList) as self:
  with context("Given a new empty task list"):
    with it("contains no elements"):
      expect(TaskList().count()).to(be(0))

    with it("throws an exception when getting a task by ID"):
      expect(lambda: TaskList().get_task_by_id(TaskId(1))).to(raise_error(ValueError, "No such task"))

    with context("Adding tasks"):
      with it("has count 1 after adding one task"):
        task_list = TaskList()
        task = Task(TaskId(1), "TODO")
        task_list.add_task(task)
        expect(task_list.count()).to(be(1))

      with it("throws expection when adding a task with existing ID"):
        task_list = TaskList()
        task = Task(TaskId(1), "TODO")
        task_list.add_task(task)
        expect(
          lambda: task_list.add_task(Task(TaskId(1), "todo"))).to(raise_error(ValueError, "Duplicate ID")
        )

    with context("When sending today query"):
      with it("should return empty list"):
        expect(QueryHandler(TaskList()).handle_query("today")).to(be_empty)

    with description("When sending an empty command"):
      with it("throws an exception with empty command string"):
        expect(
          lambda: CommandHandler(TaskList()).handle_command("")
        ).to(raise_error(ValueError, "Invalid command"))

    with context("When sending a delete command"):
      with before.each:
        self.command_handler = CommandHandler(TaskList())

      with it("throws an exception when command is not followed by an ID"):
        expect(
          lambda: self.command_handler.handle_command("delete")
        ).to(raise_error(ValueError, "Invalid arguments"))     

      with it("throws an exception when no task with given ID exists"):
        expect(
          lambda: self.command_handler.handle_command("delete 1")
        ).to(raise_error(ValueError, "No such task"))

    with context("When sending a deadline command"):
      with before.each:
        self.command_handler = CommandHandler(TaskList())

      with it("throws an exception when command does not start with deadline keyword"):      
        expect(
          lambda: self.command_handler.handle_command("deedlien")
        ).to(raise_error(ValueError, "Invalid command"))

      with it("throws an exception when command is not followed by an ID"):
        expect(
          lambda: self.command_handler.handle_command("deadline")
        ).to(raise_error(ValueError, "Invalid arguments"))     

      with it("throws an exception when ID is not followed by a date"):
        expect(
          lambda: self.command_handler.handle_command("deadline 1")
        ).to(raise_error(ValueError, "Invalid arguments"))         

      with it("throws an exception when ID is not an integer"):
        expect(
          lambda: self.command_handler.handle_command("deadline a 20-11-2021")
        ).to(raise_error(ValueError))

      with it("throws an exception when date is not a date"):
        expect(
          lambda: self.command_handler.handle_command("deadline 1 ab-11-2021")
        ).to(raise_error(ValueError))

      with it("throws an exception when no task with given ID exists"):
        expect(
          lambda: self.command_handler.handle_command("deadline 1 20-11-2021")
        ).to(raise_error(ValueError, "No such task"))

  with context("Given a task list with one task"):
    with before.each:
      self.my_task_list = TaskList()
      self.my_task_list.add_tasks([Task(TaskId(1), "todo")])

    with it("has count 1"):
      expect(self.my_task_list.count()).to(be(1))

    with it("returns empty list when sent the today query"):
      expect(QueryHandler(self.my_task_list).handle_query("today")).to(be_empty)

    with context("When sent a delete command"):
      with it("deletes the single task"):
        CommandHandler(self.my_task_list).handle_command("delete 1")
        expect(self.my_task_list.count()).to(be(0))
 
    with it("throws an exception when deadline command is given wrong ID"):
      expect(
        lambda: CommandHandler(self.my_task_list).handle_command("deadline 11 20-11-2021")
      ).to(raise_error(ValueError, "No such task"))

    with context("And the deadline has been set unequal to today"):
      with before.each:
        CommandHandler(self.my_task_list).handle_command("deadline 1 20-10-2021")
      
      with it("sets the deadline for the contained task"):
        task = self.my_task_list.get_task_by_id(TaskId(1))
        deadline = datetime.strptime("20-10-2021", '%d-%m-%Y').date()
        expect(task.get_deadline()).to(equal(deadline))
        
      with it("returns empty list when sent the today query"):
        expect(QueryHandler(self.my_task_list).handle_query("today")).to(be_empty)

    with description("And the deadline has been set equal to today"):
      with it("returns list with single task due today"):
        today_as_string = datetime.today().strftime("%d-%m-%Y")
        CommandHandler(self.my_task_list).handle_command("deadline 1 " + today_as_string)
        tasks_today = QueryHandler(self.my_task_list).handle_query("today")
        expect(tasks_today).to(have_length(1))

  with context("Given a task list with two tasks"):
    with before.each:
      self.task1 = Task(TaskId(1), "todo")
      self.task2 = Task(TaskId(2), "todo")
      self.my_task_list = TaskList()
      self.my_task_list.add_tasks([self.task1, self.task2])

    with it("has count 2"):
      expect(self.my_task_list.count()).to(be(2))

    with it("retrieves second task by ID"):
      expect(self.my_task_list.get_task_by_id(TaskId(2))).to(equal(self.task2))

