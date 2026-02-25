import os
import requests
from sqlalchemy.orm import Session
from .crud import create_tariff
from google.oauth2 import service_account
from googleapiclient.discovery import build


WB_URL = "https://common-api.wildberries.ru/api/v1/tariffs/box"


def fetch_wb_tariffs(db: Session):
    headers = {"Authorization": os.getenv("WB_API_TOKEN")}

    response = requests.get(WB_URL, headers=headers)
    data = response.json()

    for item in data.get("tariffs", []):
        create_tariff(db, item.get("name"), item.get("price"))


SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")


def update_google_sheets(tariffs):
    credentials = service_account.Credentials.from_service_account_file(
        "service-account.json", scopes=SCOPES
    )

    service = build("sheets", "v4", credentials=credentials)
    sheet = service.spreadsheets()

    values = [["ID", "Name", "Price"]]

    for t in tariffs:
        values.append([t.id, t.name, t.price])

    body = {"values": values}

    sheet.values().update(
        spreadsheetId=SPREADSHEET_ID,
        range="Sheet1!A1",
        valueInputOption="RAW",
        body=body,
    ).execute()
