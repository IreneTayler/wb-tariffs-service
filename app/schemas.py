# Define Pydantic schemas for request and response validation

from pydantic import BaseModel


class TariffBase(BaseModel):
    name: str
    price: float


# Schema for creating a tariff
class TariffCreate(TariffBase):
    pass


# Schema for reading a tariff (includes ID)
class Tariff(TariffBase):
    id: int

    # Allow ORM compatibility
    class Config:
        orm_mode = True
