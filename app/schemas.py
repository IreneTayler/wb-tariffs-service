from pydantic import BaseModel
from datetime import date

class TariffBase(BaseModel):
    name: str
    price: float
    description: str | None = None
    valid_from: date
    valid_to: date


class TariffCreate(TariffBase):
    pass


class TariffUpdate(TariffBase):
    pass


class TariffResponse(TariffBase):
    id: int

    class Config:
        from_attributes = True
        orm_mode = True