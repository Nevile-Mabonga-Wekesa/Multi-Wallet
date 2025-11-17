# Import engine creator
from sqlalchemy import create_engine

# Import session factory, base for models, and Session type for type hints
from sqlalchemy.orm import sessionmaker, declarative_base, Session

# For catching database errors
from sqlalchemy.exc import SQLAlchemyError

# To read environment variable for DB connection
import os


# Get DB connection from .env or use fallback
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://neville254:Neville2022.@localhost:5432/microfinance"
)

# Initialize SQLAlchemy engine
# echo=True prints SQL queries, disable in production: echo=False
engine = create_engine(DATABASE_URL, echo=True, future=True)

# Create a session factory
SessionLocal = sessionmaker(
    autocommit=False,  # Prevents auto transaction commits
    autoflush=False,   # Avoids automatic flush before queries
    bind=engine,
    future=True
)

# Base class all ORM models will inherit from
Base = declarative_base()


# FastAPI dependency that returns a database session
# `yield` ensures safe session disposal even on error
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    except SQLAlchemyError:  # Optional handling for DB-specific errors
        db.rollback()        # Undo uncommitted transactions
        raise                # Re-throw for visibility
    finally:
        db.close()           # Always release DB connection
