from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Database connection URL (used inside Docker)
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@postgres:5432/tariffs"
)

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
# Base class for models
Base = declarative_base()


# Dependency for FastAPI routes
# Provides a database session and closes it after request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()