from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app import models

router = APIRouter(prefix="/tariffs", tags=["Tariffs"])


@router.get("/")
def get_tariffs(date: str = None, db: Session = Depends(get_db)):
    query = db.query(models.TariffBox)

    if date:
        query = query.filter(models.TariffBox.date == date)

    tariffs = query.all()

    return tariffs