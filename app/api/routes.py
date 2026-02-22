import os
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.wb_service import sync_tariffs
from app.models import TariffBox
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.db import get_db

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
    tariffs = db.query(TariffBox).all()
    return tariffs