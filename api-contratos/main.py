from fastapi import FastAPI

from schemas import CreateContract

app = FastAPI(title="Contracts API")

@app.get("/")
def raiz():
    return {"message": "Contracts API working"}

@app.post("/contracts")
def create_contract(contract: CreateContract):
    return contract 