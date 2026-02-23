from sqlalchemy import Column, Integer, String, Float, Date, DateTime, UniqueConstraint
from datetime import datetime
from app.db import Base


class Tariff(Base):
    __tablename__ = "tariffs"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, index=True)

    warehouse_name = Column(String, nullable=False)
    delivery_coef = Column(Float, nullable=False)
    storage_coef = Column(Float, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)
