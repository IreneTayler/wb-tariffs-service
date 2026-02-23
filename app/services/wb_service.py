import requests
from datetime import date
from sqlalchemy.orm import Session
from app.models import Tariff


WB_TARIFFS_URL = "https://common-api.wildberries.ru/api/v1/tariffs/box"


def to_float(value):
    """
    Safely convert a value to float.
    Returns 0.0 if conversion fails.
    """
    try:
        if value is None or value == "":
            return 0.0
        return float(value)
    except (ValueError, TypeError):
        return 0.0


def fetch_tariffs(api_token: str):
    """
    Fetch tariffs data from Wildberries API.
    Returns list of warehouses tariffs and date.
    """

    headers = {"Authorization": api_token}

    params = {"date": date.today().isoformat()}

    response = requests.get(WB_TARIFFS_URL, headers=headers, params=params, timeout=30)

    response.raise_for_status()

    data = response.json()

    # Correct structure:
    # response -> data -> warehouseList
    tariffs = data.get("response", {}).get("data", {}).get("warehouseList", [])

    return tariffs, params["date"]


def save_tariffs(db: Session, tariffs: list, tariff_date: str):
    """
    Save tariffs into database.
    Before saving, remove existing records for the same date.
    Returns number of saved records.
    """

    # Delete existing data for this date (prevent duplicates)
    db.query(Tariff).filter(Tariff.date == tariff_date).delete()
    db.commit()

    saved_count = 0

    for item in tariffs:
        # Safety check
        if not isinstance(item, dict):
            continue

        tariff = Tariff(
            date=tariff_date,
            warehouse_name=item.get("warehouseName"),
            delivery_coef=to_float(item.get("boxDeliveryCoefExpr")),
            storage_coef=to_float(item.get("boxStorageCoefExpr")),
        )

        db.add(tariff)
        saved_count += 1

    db.commit()

    return saved_count


def sync_tariffs(db: Session, api_token: str):
    """
    Full synchronization process:
    1. Fetch data from WB API
    2. Save to database
    3. Return result
    """

    if not api_token:
        raise ValueError("WB_API_TOKEN is empty")

    tariffs, tariff_date = fetch_tariffs(api_token)

    if not tariffs:
        return {"saved": 0, "message": "No tariffs received"}

    saved_count = save_tariffs(db, tariffs, tariff_date)

    return {"saved": saved_count, "date": tariff_date}
