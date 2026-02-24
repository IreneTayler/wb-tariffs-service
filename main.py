from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
import os
import time
from sqlalchemy import create_engine

app = FastAPI()

DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql://postgres:password@localhost:5432/tariffs_db"
)

engine = create_engine(DATABASE_URL)


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
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        # Create a new tariff
        cur.execute(
            "INSERT INTO tariffs (tariff_name, price) VALUES (%s, %s)",
            (tariff.tariff_name, tariff.price),
        )
        conn.commit()
        cur.close()
        conn.close()
        return {"message": "Tariff created successfully"}
    except Exception as e:
        return {"error": str(e)}


@app.get("/tariffs/")
def get_tariffs():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM tariffs")
    tariffs = cur.fetchall()
    cur.close()
    conn.close()
    return {"tariffs": tariffs}


def create_table():
    # Wait DB ready
    time.sleep(5)

    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute(
        """
    CREATE TABLE IF NOT EXISTS tariffs (
        id SERIAL PRIMARY KEY,
        date DATE,
        warehouse_name TEXT,
        box_type TEXT,
        coefficient NUMERIC,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    )
    conn.commit()
    cur.close()
    conn.close()


create_table()
