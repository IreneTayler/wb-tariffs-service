from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2

app = FastAPI()

DATABASE_URL = "postgresql://postgres:<12345678>@localhost:5432/tariffs_db"


def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn


class Tariff(BaseModel):
    tariff_name: str
    price: float


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.post("/create_tariff/")
def create_tariff(tariff: Tariff):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO tariffs (tariff_name, price) VALUES (%s, %s)",
        (tariff.tariff_name, tariff.price),
    )
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Tariff created successfully"}


@app.get("/tariffs/")
def get_tariffs():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM tariffs")
    tariffs = cur.fetchall()
    cur.close()
    conn.close()
    return {"tariffs": tariffs}
