import logging
from fastapi import HTTPException
from typing import Any
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize logger
logger = logging.getLogger("app")
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)


# Utility function to handle errors and log them
def handle_error(error: Exception, message: str = None):
    """Handle and log errors, raising an HTTPException with a detailed message."""
    logger.error(f"Error: {message if message else str(error)}")
    raise HTTPException(status_code=500, detail=message or str(error))


# Utility function to log info messages
def log_info(message: str, *args: Any):
    """Log informational messages."""
    logger.info(message, *args)


# Utility function to log debug messages
def log_debug(message: str, *args: Any):
    """Log debug messages."""
    logger.debug(message, *args)


# Utility function to log warnings
def log_warning(message: str, *args: Any):
    """Log warning messages."""
    logger.warning(message, *args)


# Utility function to load environment variables with default values
def get_env_variable(key: str, default: str = None) -> str:
    """Get the environment variable or return a default value if not found."""
    value = os.getenv(key, default)
    if not value:
        logger.warning(f"Environment variable {key} is not set.")
    return value
