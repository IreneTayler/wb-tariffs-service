# Import necessary SQLAlchemy modules
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from .database import Base


# Define Tariff model for the tariffs table
class Tariff(Base):
    __tablename__ = "tariffs"

    # Define columns for the tariffs table
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    created_at = Column(DateTime, server_default=func.now())
