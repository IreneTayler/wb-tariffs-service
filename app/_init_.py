# app/__init__.py

# Importing necessary components for package-wide use
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

# Set up configuration for the package
DATABASE_URL = os.getenv("DATABASE_URL", "postgres://localhost:5432/default_db")
GOOGLE_SHEET_ID = os.getenv("GOOGLE_SHEET_ID", "")
GOOGLE_SHEET_CREDENTIALS = os.getenv("GOOGLE_SHEET_CREDENTIALS", "")

# Print a message when the package is initialized (for debugging purposes)
print("Initializing the app package...")

# Define the package version
__version__ = "1.0.0"

# Import core modules to simplify access for the users
from .models import Tariff
from .crud import create_tariff, get_tariffs
from .database import SessionLocal, engine
from .google_sheets import update_google_sheet
from .services import fetch_tariff_data, save_tariff_data, update_google_sheets

# Provide easy access to the main functionality from this package
__all__ = [
    "Tariff",  # ORM model
    "create_tariff",  # CRUD function to create tariff
    "get_tariffs",  # CRUD function to get tariffs
    "SessionLocal",  # Database session
    "engine",  # Database engine
    "update_google_sheet",  # Google Sheets update function
    "fetch_tariff_data",  # Function to fetch tariff data from Wildberries API
    "save_tariff_data",  # Function to save tariff data to database
    "update_google_sheets",  # Function to update Google Sheets with tariffs
    "__version__",  # Package version
]

# Optional: Log a message when the package is initialized (helpful for debugging)
print(f"App package initialized. Version: {__version__}")
