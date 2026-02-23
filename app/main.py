from fastapi import FastAPI
from app.db import engine, Base
from app.routers import tariffs
from app.api.routes import router
from app.routers.tariffs import router
from app.models.tariff import Tariff

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
