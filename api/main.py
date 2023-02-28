from fastapi import FastAPI
from src.service import Service
app = FastAPI()

service = Service()

@app.get("/{name}")
async def root(name : str,):
    
    return service.get(name)