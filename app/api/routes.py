import os
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.wb_service import sync_tariffs
from app.db import SessionLocal
from app.db import get_db
from app import models, schemas
from datetime import date

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/sync")
def sync_wb_tariffs(db: Session = Depends(get_db)):
    api_token = os.getenv("WB_API_TOKEN")

    if not api_token:
        raise HTTPException(status_code=500, detail="WB_API_TOKEN not set")

    result = sync_tariffs(db, api_token)
    return result


@router.get("/tariffs")
def get_tariffs(db: Session = Depends(get_db)):
    tariffs = db.query(models.Tariff).all()
    return tariffs


@router.post("/tariffs", response_model=schemas.TariffResponse)
def create_tariff(tariff: schemas.TariffCreate, db: Session = Depends(get_db)):
    data = tariff.dict()
    data["date"] = date.today()  # Set creation date automatically

    db_tariff = models.Tariff(**data)
    db.add(db_tariff)
    db.commit()
    db.refresh(db_tariff)
    return db_tariff
