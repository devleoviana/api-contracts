from fastapi import FastAPI

import models
from database import Base, engine
from schemas import CreateContract

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Contracts API")

@app.get("/")
def raiz():
    return {"message": "Contracts API working"}

@app.post("/contracts")
def create_contract(contract: CreateContract):
    return contract 