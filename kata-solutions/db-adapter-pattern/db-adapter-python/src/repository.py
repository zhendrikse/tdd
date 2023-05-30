from employee import Employee
from abc import ABC,abstractmethod

class EmployeeRepository(ABC):
  @abstractmethod
  def all(self) -> [Employee]: pass

  @abstractmethod
  def get_by_id(self, id: str) -> Employee: pass

  @abstractmethod
  def add(self, new_employee:Employee, employee_id:str) -> None: pass

  @abstractmethod
  def delete(self, id:str) -> None: pass
