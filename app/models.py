from sqlalchemy import Column, Integer, String, Float, Date, DateTime, UniqueConstraint
from datetime import datetime
from app.db import Base


class TariffBox(Base):
    """
    Stores Wildberries box tariffs for each warehouse.
    Data is collected daily and historical records must be preserved.
    """

    __tablename__ = "tariff_boxes"

    id = Column(Integer, primary_key=True, index=True)

    # Date when tariffs were received from WB API
    date = Column(Date, nullable=False, index=True)

    # Warehouse name from WB response
    warehouse_name = Column(String, nullable=False, index=True)

    # Delivery coefficient for boxes
    delivery_coef = Column(Float, nullable=True)

    # Storage coefficient for boxes
    storage_coef = Column(Float, nullable=True)

    # Timestamp when the record was saved to database
    created_at = Column(DateTime, default=datetime.utcnow)

    # Prevent duplicate records for the same warehouse and date
    __table_args__ = (
        UniqueConstraint("date", "warehouse_name", name="uq_tariff_date_warehouse"),
    )
    
