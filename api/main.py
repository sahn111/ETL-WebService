from fastapi import FastAPI
from src.service import Service
app = FastAPI()

service = Service()

@app.get("/{name}")
async def root(name : str,):
    result = service.etl(name)
    return result