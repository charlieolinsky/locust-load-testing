from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class LoginRequest(BaseModel):
    username: str
    password: str

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.post("/login")
def login(login_request: LoginRequest):
    return {"message": "Logged in successfully"}

@app.get("/dashboard")
def read_dashboard():
    return {"message": "Welcome to the dashboard!"}
