from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from .database import Base


class Tariff(Base):
    __tablename__ = "tariffs"

    id = Column(Integer, primary_key=True, index=True)
    tariff_name = Column(String)
    price = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
