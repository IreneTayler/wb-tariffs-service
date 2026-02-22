from fastapi import FastAPI
from app.db import engine, Base
from app.routers import tariffs
from app.api.routes import router

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Include router
app.include_router(tariffs.router)

app = FastAPI(title="WB Tariffs Service")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "API is running"}