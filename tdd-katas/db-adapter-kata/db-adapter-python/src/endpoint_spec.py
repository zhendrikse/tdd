from mamba import description, it, context, before
from expects import expect, equal
from fastapi import HTTPException
from employee import Employee

from endpoint import EmployeeEndpoint

with description(EmployeeEndpoint) as self:
  with context("Health service endpoint"):
      with it("returns pong after ping"):
        self.endpoint = EmployeeEndpoint()
        expect(self.endpoint.ping()).to(equal("Pong"))
