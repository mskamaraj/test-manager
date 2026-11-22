from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Test Manager Service API, please use the /testcase endpoint to manage testcases."}