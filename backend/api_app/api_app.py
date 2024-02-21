from fastapi import FastAPI

from ..worker import important_function

api_app = FastAPI()

@api_app.post("/")
def bug_repro():
    res = important_function.remote()
    return {"message": res}