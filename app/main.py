from fastapi import FastAPI, HTTPException
from mangum import Mangum
from app.models.test_case import TestCase, TestCaseCreate
from app.actions import test_case_action

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to the Test Manager Service API, please use the /testcase endpoint to manage testcases."}


@app.post("/testcase", response_model=TestCase, status_code=201)
def create_test_case(payload: TestCaseCreate):
    return test_case_action.create_test_case(payload)


@app.get("/testcase", response_model=list[TestCase])
def get_all_test_cases():
    return test_case_action.get_all_test_cases()


@app.get("/testcase/{test_case_id}", response_model=TestCase)
def get_test_case(test_case_id: str):
    test_case = test_case_action.get_test_case(test_case_id)
    if not test_case:
        raise HTTPException(status_code=404, detail=f"Test case '{test_case_id}' not found")
    return test_case


handler = Mangum(app)
