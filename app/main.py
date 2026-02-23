# Import FastAPI and necessary dependencies
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import crud, models, schemas, database, services
from typing import List
import os

# Initialize FastAPI app
app = FastAPI()


# Dependency to get the DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Endpoint to sync tariffs (fetch from Wildberries API and update DB and Google Sheets)
@app.post("/sync-tariffs/")
def sync_tariffs(db: Session = Depends(get_db)):
    services.save_tariff_data(db)
    services.update_google_sheets(db, os.getenv("GOOGLE_SHEET_ID"))
    return {"message": "Tariffs synced successfully!"}


# Endpoint to retrieve tariffs from the database
@app.get("/tariffs/", response_model=List[schemas.Tariff])
def read_tariffs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_tariffs(db=db, skip=skip, limit=limit)
