import os
from fastapi import FastAPI

app = FastAPI()

APP_NAME = os.getenv("APP_NAME", "app-default")
APP_ENV = os.getenv("APP_ENV", "local")

@app.get("/")
def root():
    return {
        "service": APP_NAME,
        "env": APP_ENV,
        "status": "running v2"
    }

@app.get("/health")
def health():
    return {"status": "ok"}
