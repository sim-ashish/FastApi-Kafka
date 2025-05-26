from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from kafka_producer import send_user_created_event

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str

@app.post("/register/")
def register_user(user: User):
    # Ideally, save user to DB here
    send_user_created_event(user.dict())
    return {"message": "User registered and event sent"}
