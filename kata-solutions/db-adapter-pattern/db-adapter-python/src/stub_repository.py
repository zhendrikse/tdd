from employee import Employee
from repository import EmployeeRepository

class StubEmployeeRepository(EmployeeRepository):
  def __init__(self):
    self.employees_by_id = {
      "001": Employee("Zeger"),
      "002": Employee("Atharva"),
      "003": Employee("Misbah") 
    }

  def all(self) -> [Employee]:
    return self.employees_by_id.values()

  def get_by_id(self, id: str) -> Employee:
    return self.employees_by_id[id]

  def add(self, new_employee:Employee, employee_id: str) -> None:
    self.employees_by_id[employee_id] = new_employee

  def delete(self, id: str) -> None:
    self.employees_by_id.pop(id)

class StubRepoFactory:
  @staticmethod
  def get_repo() -> EmployeeRepository:
    return StubEmployeeRepository()
