import os
import requests
from sqlalchemy.orm import Session
from .crud import create_tariff

WB_URL = "https://common-api.wildberries.ru/api/v1/tariffs/box"


def fetch_wb_tariffs(db: Session):
    headers = {"Authorization": os.getenv("WB_API_TOKEN")}

    response = requests.get(WB_URL, headers=headers)
    data = response.json()

    for item in data.get("tariffs", []):
        create_tariff(db, item.get("name"), item.get("price"))
