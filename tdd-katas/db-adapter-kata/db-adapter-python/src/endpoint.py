from fastapi import FastAPI, HTTPException, Depends
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

app = FastAPI()
router = InferringRouter()

@cbv(router)
class EmployeeEndpoint:
    @router.get("/")
    def ping(self) -> str:
        return 'Pong'
