from sqlalchemy import Column, Integer, String, Float, Date
from app.db import Base


class Tariff(Base):
    __tablename__ = "tariffs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String)
    valid_from = Column(Date)
    valid_to = Column(Date)
