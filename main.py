from pyexpat import model
from typing import Union
import uvicorn
from fastapi import FastAPI
import routers as route

app = FastAPI(title="House Price Prediction",
              prefix="/prediction",
              tags=["root"],)


@app.get("/")
async def root():
    return "Bonjour et bienvenue sur House Preice Prediction ML!"


app.include_router(route.router)


''' LE CHEMIN DE BASE: LA RACINE '''
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

