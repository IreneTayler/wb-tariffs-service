from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, Base
from app import crud, schemas, services
from app import services
from app import models
from app.database import get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(title="WB Tariffs Service")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "WB Tariffs Service running"}


@app.post("/tariffs/")
def create_tariff(tariff: schemas.TariffCreate, db: Session = Depends(get_db)):
    return crud.create_tariff(db, tariff.tariff_name, tariff.price)


@app.get("/tariffs/")
def read_tariffs(db: Session = Depends(get_db)):
    return crud.get_tariffs(db)


@app.post("/sync-wb/")
def sync_wb(db: Session = Depends(get_db)):
    services.fetch_wb_tariffs(db)
    return {"message": "WB tariffs synced"}


@app.post("/export-google/")
def export_google(db: Session = Depends(get_db)):
    tariffs = db.query(models.Tariff).all()
    services.update_google_sheets(tariffs)
    return {"status": "Exported"}
