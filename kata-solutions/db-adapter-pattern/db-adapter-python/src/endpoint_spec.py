from mamba import description, it, context, before
from expects import expect, equal, raise_error, have_len

from fastapi import HTTPException

from endpoint import EmployeeEndpoint
from stub_repository import StubRepoFactory
from employee import Employee

with description(EmployeeEndpoint) as self:
  with before.each:
    self.repo = StubRepoFactory.get_repo()
    self.endpoint = EmployeeEndpoint()

  with context("Health service endpoint"):
    with it("returns pong after ping"):
      expect(self.endpoint.ping()).to(equal("Pong"))

  with context("Retrieval of employees endpoint"):
    with it("returns by default all employees"):
      expect(self.endpoint.list_all_employees(repo=self.repo)).to(have_len(3))

    with it("throws an exception when ID does not exist"):
      expect(lambda: self.endpoint.get_employee_by_id("xxx", repo=self.repo)).to(raise_error(HTTPException))

    with it("returns the employee with given ID"):
      expect(
        self.endpoint.get_employee_by_id("001", repo=self.repo)).to(equal(Employee("Zeger"))) 

  with context("Adding new employees"):
    with it("adds the new employee"):
      self.endpoint.add_new_employee("Jan", "004", repo=self.repo)
      expect(
        len(self.endpoint.list_all_employees(repo=self.repo))).to(equal(4))
      expect(
        self.endpoint.get_employee_by_id("004", repo=self.repo)).to(equal(Employee("Jan")))

    with it("throws an exception when employee with given ID exists"):
      expect(lambda: self.endpoint.add_new_employee("Zeger", "001", repo=self.repo)).to(raise_error(HTTPException))

  with context("Removing employees that left"):
    with it("throws an exception when ID does not exist"):
      expect(lambda: self.endpoint.delete_employee("xxx", repo=self.repo)).to(raise_error(HTTPException))

    with it("removes and employee when it exists"):
      self.endpoint.delete_employee("003", repo=self.repo)
      expect(
        len(self.endpoint.list_all_employees(repo=self.repo))).to(equal(2))
