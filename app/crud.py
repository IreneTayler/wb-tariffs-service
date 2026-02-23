# Define CRUD operations to interact with the database

from sqlalchemy.orm import Session
from . import models, schemas


# Create a new tariff in the database
def create_tariff(db: Session, tariff: schemas.TariffCreate):
    db_tariff = models.Tariff(name=tariff.name, price=tariff.price)
    db.add(db_tariff)
    db.commit()
    db.refresh(db_tariff)
    return db_tariff


# Retrieve a list of tariffs from the database
def get_tariffs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tariff).offset(skip).limit(limit).all()


# Retrieve a single tariff by ID
def get_tariff(db: Session, tariff_id: int):
    return db.query(models.Tariff).filter(models.Tariff.id == tariff_id).first()
