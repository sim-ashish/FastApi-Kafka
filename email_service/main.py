from fastapi import FastAPI
from kafka_consumer import start_consumer_thread

app = FastAPI()

@app.on_event("startup")
def startup_event():
    start_consumer_thread()

@app.get("/")
def read_root():
    return {"message": "Email service is running"}
