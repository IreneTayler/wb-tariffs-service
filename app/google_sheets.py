# Import Google Sheets API client and credentials
import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


# Get Google Sheets API service client
def get_sheets_service():
    creds = Credentials.from_service_account_file(
        os.getenv("GOOGLE_SHEET_CREDENTIALS"),
        scopes=["https://www.googleapis.com/auth/spreadsheets"],
    )
    service = build("sheets", "v4", credentials=creds)
    return service


# Update Google Sheet with tariff data
def update_google_sheet(spreadsheet_id: str, data: list):
    service = get_sheets_service()
    range_ = "Sheet1!A2:B"  # Define the range for the data to be inserted
    body = {"values": data}
    request = (
        service.spreadsheets()
        .values()
        .update(
            spreadsheetId=spreadsheet_id,
            range=range_,
            valueInputOption="RAW",
            body=body,
        )
    )
    request.execute()
