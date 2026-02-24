from sqlalchemy.orm import Session
from . import models


def create_tariff(db: Session, name: str, price: float):
    tariff = models.Tariff(tariff_name=name, price=price)
    db.add(tariff)
    db.commit()
    db.refresh(tariff)
    return tariff


def get_tariffs(db: Session):
    return db.query(models.Tariff).all()
