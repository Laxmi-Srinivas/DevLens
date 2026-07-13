from fastapi import FastAPI
from app.routers import health
from app.routers import github
app=FastAPI()

@app.get("/")
def home():
    return {"message":"Welcome to DevLens"}

app.include_router(health.router)

app.include_router(github.router)


