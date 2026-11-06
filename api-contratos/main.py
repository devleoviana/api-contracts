from fastapi import FastAPI

app = FastAPI(title="API de Contratos")

@app.get("/")
def raiz():
    return {"mensagem": "API de Contratos no ar"}