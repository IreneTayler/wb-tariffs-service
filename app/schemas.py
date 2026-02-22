from pydantic import BaseModel


class TariffBase(BaseModel):
    name: str
    price: float
    description: str | None = None


class TariffCreate(TariffBase):
    pass


class TariffUpdate(TariffBase):
    pass


class TariffResponse(TariffBase):
    id: int

    class Config:
        from_attributes = True