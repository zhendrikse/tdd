from replit import db
from employee import Employee
from repository import EmployeeRepository

class ReplitDbEmployeeRepository(EmployeeRepository):
  def all(self) -> [Employee]:
    return (db[employee_id] for employee_id in db.keys())

  def get_by_id(self, id: str) -> Employee:
    if db.get(id):
      return Employee(db.get(id))
    raise KeyError(id)

  def add(self, new_employee:Employee, employee_id: str) -> None:
    db[employee_id] = new_employee.name

  def delete(self, employee_id: str) -> None:
    del db[employee_id]
  
  # def toJson(self):
  #   return json.dumps(self, default=lambda o: o.__dict__)

class ReplitRepoFactory:
  @staticmethod
  def get_repo() -> EmployeeRepository:
    return ReplitDbEmployeeRepository()