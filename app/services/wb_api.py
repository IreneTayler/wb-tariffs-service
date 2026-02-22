import os
import requests

WB_URL = "https://common-api.wildberries.ru/api/v1/tariffs/box"

def fetch_tariffs(date: str):
    token = os.getenv("WB_API_TOKEN")

    headers = {
        "Authorization": f"Bearer {token}"
    }

    params = {
        "date": date
    }

    response = requests.get(WB_URL, headers=headers, params=params)

    if response.status_code != 200:
        raise Exception(f"WB API error: {response.text}")

    return response.json()