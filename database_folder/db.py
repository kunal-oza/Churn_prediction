# db.py
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Load .env file
load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL"
)

# Create SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    echo=False,        # Set True to see SQL logs in console
    pool_pre_ping=True # Avoids stale connections
)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for ORM models
Base = declarative_base()


# Dependency for FastAPI (we'll use this in main.py)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
