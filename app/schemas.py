from pydantic import BaseModel


class TariffCreate(BaseModel):
    tariff_name: str
    price: float


class Tariff(BaseModel):
    id: int
    tariff_name: str
    price: float

    class Config:
        orm_mode = True
