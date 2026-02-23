import pytest
from unittest import mock
from app.services import fetch_tariff_data, save_tariff_data, update_google_sheets
from app.models import Tariff
from app.database import SessionLocal
from app import crud
import requests


# Mock database session
@pytest.fixture
def db_session():
    db = SessionLocal()
    yield db
    db.close()


# Test for fetch_tariff_data - mocking the Wildberries API response
def test_fetch_tariff_data():
    # Mock the requests.get method to avoid calling the actual Wildberries API
    mock_response = {
        "tariffs": [
            {"name": "Tariff 1", "price": 10.5},
            {"name": "Tariff 2", "price": 20.5},
        ]
    }

    with mock.patch(
        "requests.get",
        return_value=mock.Mock(json=mock.Mock(return_value=mock_response)),
    ):
        data = fetch_tariff_data()
        assert data == mock_response
        assert "tariffs" in data
        assert len(data["tariffs"]) == 2


# Test for save_tariff_data - mocking database insertion
def test_save_tariff_data(db_session):
    # Mock the response from fetch_tariff_data
    mock_response = {
        "tariffs": [
            {"name": "Tariff 1", "price": 10.5},
            {"name": "Tariff 2", "price": 20.5},
        ]
    }

    with mock.patch(
        "requests.get",
        return_value=mock.Mock(json=mock.Mock(return_value=mock_response)),
    ):
        # Call save_tariff_data to insert mock data into the database
        save_tariff_data(db_session)

        # Check if tariffs are inserted in the database
        tariffs = db_session.query(Tariff).all()
        assert len(tariffs) == 2
        assert tariffs[0].name == "Tariff 1"
        assert tariffs[1].price == 20.5


# Test for update_google_sheets - mocking Google Sheets API update
def test_update_google_sheets(db_session):
    # Sample tariffs data to update Google Sheets
    tariffs = [Tariff(name="Tariff 1", price=10.5), Tariff(name="Tariff 2", price=20.5)]

    # Mock the Google Sheets update request
    with mock.patch("app.google_sheets.update_google_sheet") as mock_update:
        # Call the update_google_sheets function with mocked data
        update_google_sheets(db_session, "fake_spreadsheet_id")

        # Ensure that the Google Sheets update function was called with the correct data
        mock_update.assert_called_once_with(
            "fake_spreadsheet_id", [["Tariff 1", 10.5], ["Tariff 2", 20.5]]
        )
