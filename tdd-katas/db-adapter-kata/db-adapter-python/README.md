# Introduction

Please read the general [introduction to the DB adapter kata](../README.md) first!

These instructions make use of 
[Mamba](https://github.com/nestorsalceda/mamba): 
the definitive test runner for Python in combination with [expects](https://expects.readthedocs.io/en/stable/#).

# Getting started

Carry out the following steps in order:

1. Create an intial Python kata set-up as described
   [here](https://github.com/zhendrikse/tdd/tree/master/cookiecutter).
   Choose 'y' when prompted for the rSpec syntax but enter 'n' for
   the code coverage.
2. Remove the `.py` files in the `src` and `test` directories, but leave the
   `__init__.py` files untouched!
4. Copy the `employee.py`, `endpoint.py`, and `main.py` files into the `src` directory 
5. Copy the `endpoint_test.py` file into the `test` directory
6. Replace the `pyproject.toml` file in the cookier cutter generated project by
   the `pyproject.toml` in this directory. 
7. Invoke
   ```
   $ poetry install
   $ ./run_tests.sh
   ``` 

## Running the tests
First make sure you can execute the provided scenario/test for the ping endpoint:

```bash
$ ./run_tests.sh
```

## Running the application

Second, make sure the application itself can also be started by going to the shell tab and execute the following two commands:

```bash
$ cd src
$ poetry run python main.py
```

To further test the application in the remainder of this kata, first push on the pop-out button in the top-right corner of the browser pane that got visible after running the above commands. After that, you can append `/docs` in the URL-bar to the existing URL, which then takes you to the (executable) API docs (based on [Swagger OpenAPI docs](https://swagger.io/specification/)).

We won't be using the real execution of the application frequently though. We will just use it for some additional manual testing.


## Components and libraries

We are going to use an in-memory database. For those working on [replit](https://replit.com/),
we will also provide an adapter for the  
[Replit DB](https://docs.replit.com/tutorials/11-using-the-replit-database) 
as storage for simple employee records. 

The endpoint is implemented using the [FastAPI](https://fastapi.tiangolo.com/tutorial/first-steps/) framework.

# Detailed Implementation Instructions

## Our first endpoint

<details>
<summary>
Implementing an endpoint to return three employees by default
</summary>

Of course, we start by writing a test first!

```python
...
with context("Retrieval of employees endpoint"):
  with it("returns by default all employees"):
    self.endpoint = EmployeeEndpoint()
    expect(self.endpoint.list_all_employees()).to(have_len(3))
```

Add the associated endpoint:
```python
...
@router.get("/employees")
def list_all_employees(self):
  pass
```

We make the test pass in the simplest way that could possibly work by replacing the pass by returning a hard coded list of three employees. Verify the test is green and refactor the duplicate initialization of the `self.endpoint`.
  
</details>

Now let's add the scenarios for getting an employee by ID to the retrieval of employees context:

<details>
  <summary>Endpoint for getting an employee by ID</summary>

```python
...
with it("throws an exception when ID does not exist"):
  expect(lambda: self.endpoint.get_employee_by_id("xxx")).to(raise_error(HTTPException))
```

Use the following code snippet to complete the implementation that makes this test green:

```python
...
@router.get("/employees/{employee_id}")
def get_employee_by_id(self, employee_id: str):
  pass
```
</details>

Next, let's try to retrieve an existing employee by ID.

<details>
  <summary>Retrieval of an existing employee</summary>

  ```python
...
with it("returns the employee with given ID"):
  expect(
    self.endpoint.get_employee_by_id("001")).to(equal(Employee("Zeger")))
```
and modify the implementation again to make the test green.
</details>

## Creating the wrapper/adapter

Eventually, all employee data will be coming from a database. Let's bundle all these calls together into an employee repository (a term that originates from [domain driven design](https://matfrs2.github.io/RS2/predavanja/literatura/Avram%20A,%20Marinescu%20F.%20-%20Domain%20Driven%20Design%20Quickly.pdf)):

> Repositories are classes or components that encapsulate the logic required to access data sources. They centralize common data access functionality, providing better maintainability and decoupling the infrastructure or technology used to access databases from the domain model layer &#8212; [docs.microsoft.com](https://docs.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/infrastructure-persistence-layer-design).

By definition, [an adapter is polymorphic](https://stackoverflow.com/questions/51798777/what-is-polymorphic-behavior-in-adaptor-pattern), i.e. we should be able to plug in different implementations at will. In our case we want to toggle between the real connection to the database in our endpoint class and the stub implementation during testing.

So let's define the wrapper/adapter interface first, preferably in its own file:

```python
from employee import Employee
from abc import ABC,abstractmethod

class EmployeeRepository(ABC):
  @abstractmethod
  def all(self) -> [Employee]: pass

  @abstractmethod
  def get_by_id(self, id: str) -> Employee: pass
```

As the Python language does not offer us a dedicated language construct for creating interfaces, we have to opt for a fully abstract (base) class, appropriately abbreviated by `ABC` in Python.

Now we can gradually move the hard coded return values that are still present in our endpoint class to an implementation of the above (repository) adapter:

```python
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
```
It is now up to you to complete this refactoring, so that the stub data are returned via the (stub)repository adapter. For now, just instantiate the stub employee repo at the top of the endpoint file:

```python
repo = StubEmployeeRepository()
```
Now that we have the adapter in place, we can also start the polymorphic implementation of the repository interface that actually connects to the (replit) database:

```python
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
```

Obviously, we also need a kind of "toggle" to switch between the stub and the replit implementations of the (repository) adapter. 

Because of a peculiarity of the FastAPI framework, let's do this with a little factory pattern offering us a static method to create either one of the adapter implementations.

To this extent, to the stub repository we add:

```python
class StubRepoFactory:
  @staticmethod
  def get_repo() -> EmployeeRepository:
    return StubEmployeeRepository()
```

and to the replit repository we add:

```python
class ReplitRepoFactory:
  @staticmethod
  def get_repo() -> EmployeeRepository:
    return ReplitDbEmployeeRepository()
```

This means that we should update the initialization of the repository in our spec file with:

```python
self.repo = StubRepoFactory.get_repo()
``` 

In the production code, we can plug in the real thing:

```python
repo = ReplitRepoFactory.get_repo
```

#### Passing the repo on to FastAPI endpoints

The aforementioned FastAPI perculiarity means that the methods implementing our Rest endpoints have to be able to call the repository methods. This can be done in the following way:

```python
repo = ReplitRepoFactory.get_repo

@cbv(router)
class EmployeeEndpoint:

  ...
  @router.get("/employees/{employee_id}")
  def get_employee_by_id(self, 
                         employee_id: str, 
                         repo: EmployeeRepository = Depends(repo)):
```

After that, you can access the repo by calling e.g. `repo.get_by_id(employee_id)`.

**Caveat**

As soon as we add the `repo: EmployeeRepository = Depends(repo)` as argument to the calls in the endpoints, the calls in the specification file(s) need to be modifyied accordingly: `self.endpoint.get_employee_by_id("001", repo=self.repo)`

** Execrise **

It is now your task to carry through all these changes, while keeping the tests green. In the end, you should end up with a working specification (unit test set) as well as a working application. How you can verify that has extensively been explained in the beginning of this instruction file, namely in the section "Getting acquainted". Use the live documentation as described therein.


## Our second endpoint

The instructions accompanying the implementation of the first endpoints were very fine-grained. These should be sufficient to let you complete the remainder of this exercise.

Our second endpoint is going to be an endpoint that is going to remove employees that have left the company from the database:

```python
@router.delete("/employees/{employee_id}")
def delete_employee(self,
                    employee_id: str,
                    repo: EmployeeRepository = Depends(repo)):
```

Implement this endpoint:

1. writie the scenarios first (also think about what should happen when we try to delete an employee (with an ID) that does not exist)
2. make a scenarios green first (by implementing the stub) before continuing to anything else
3. implement the replit repository as well and test it by running the application and using the OpenAPI live documentation.

## Our last endpoint

Our last endpoint enables us to add new employees to the company/database.

```python
@router.put("/employees", status_code=201)
def add_new_employee(self,
                     name: str,
                     employee_id: str,
                     repo: EmployeeRepository = Depends(repo)):
```

Rinse and repeat the same steps as for the delete endpoint, bearing in mind that [PUT is idem potent](https://restfulapi.net/idempotent-rest-apis/), so throw a [HTTP 403 response](https://en.wikipedia.org/wiki/HTTP_403) when the resource already exists.

# Retrospective

After completing this exercise, you should have gained a proper understanding of how to isolate your application from the systems it is communicating with during testing. You may feel though that some questions may still remain somewhat unanswered.

First of all, the question may have popped up to which extent should the endpoints also be tested with our TDD/BDD tests. Generally speaking, we always try to test as much as soon as possible, as long as our tests remain blazingly fast. After all, we are always aspiring to feedback loops that feed as much information back to us as quickly as possible.  

At a certain point, there is a balance to be struck. By incorporating more and more actions into our scenarios/specifications, our execution times eventually become slower and slower. When practicing TDD, we usually run our specifications multiple times per minute, so as soon as we start to observe execution times of seconds or more, this becomes problematic.

In our current implementation, our tests target the layer _just below_ the endpoints. This means that the marshalling and unmarshalling of the JSON in the endpoints is not tested. Usually, we would try to incorporate that as well. This would be a further optional exercise that you could do after completing this exercise.

Second of all, although the logic in the replit repository is (and shoud remain) rather shallow, it may be argued that this needs to be tested as well. And that's correct! Only, by definition this then constitutes an integration test. TDD does not make integration tests redundant! TDD tends to make them much less needed, just to ascertain a proper functioning at the integration points with external systems.

As this course is about TDD, we leave the topic of integration tests now for what it is. That does not mean they can be skipped, of course!