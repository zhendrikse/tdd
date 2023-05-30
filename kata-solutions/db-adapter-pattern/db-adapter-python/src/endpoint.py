from fastapi import FastAPI, HTTPException, Depends
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from replit_db_repository import EmployeeRepository, ReplitRepoFactory
from employee import Employee

app = FastAPI()
router = InferringRouter()
repo = ReplitRepoFactory.get_repo


@cbv(router)
class EmployeeEndpoint:
    @router.get("/")
    def ping(self) -> str:
        return 'Pong'

    @router.get("/employees")
    def list_all_employees(self, repo: EmployeeRepository = Depends(repo)):
        return repo.all()

    @router.get("/employees/{employee_id}")
    def get_employee_by_id(self,
                           employee_id: str,
                           repo: EmployeeRepository = Depends(repo)):
        try:
            return repo.get_by_id(employee_id)
        except KeyError:
            raise HTTPException(status_code=404, detail="Item not found")

    @router.delete("/employees/{employee_id}")
    def delete_employee(self,
                        employee_id: str,
                        repo: EmployeeRepository = Depends(repo)):
        try:
            return repo.delete(employee_id)
        except KeyError:
            raise HTTPException(status_code=404, detail="Item not found")

    @router.put("/employees", status_code=201)
    def add_new_employee(self,
                         name: str,
                         employee_id: str,
                         repo: EmployeeRepository = Depends(repo)):
        try:
          repo.get_by_id(employee_id)
          raise HTTPException(status_code=403, detail="Employee exists")
        except KeyError:
          repo.add(Employee(name), employee_id)
