# Import necessary modules
import requests
from . import crud, models, schemas
from sqlalchemy.orm import Session
from .google_sheets import update_google_sheet
import os

# URL for Wildberries API
WILDBERRIES_API_URL = "https://common-api.wildberries.ru/api/v1/tariffs/box"


# Fetch tariff data from the Wildberries API
def fetch_tariff_data():
    response = requests.get(WILDBERRIES_API_URL)
    return response.json()


# Save tariff data to the database
def save_tariff_data(db: Session):
    tariff_data = fetch_tariff_data()

    for tariff in tariff_data:
        db_tariff = schemas.TariffCreate(name=tariff["name"], price=tariff["price"])
        crud.create_tariff(db, db_tariff)


# Update Google Sheets with stored tariffs
def update_google_sheets(db: Session, spreadsheet_id: str):
    tariffs = crud.get_tariffs(db)
    data = [[tariff.name, tariff.price] for tariff in tariffs]
    update_google_sheet(spreadsheet_id, data)
