import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Define where the SQLite database file will live
DB_DIR = "data/database"
os.makedirs(DB_DIR, exist_ok=True)
DB_PATH = os.path.join(DB_DIR, "pharma_radar.db")

# Create the SQLAlchemy Engine (echo=True prints the raw SQL it generates to the terminal, great for debugging!)
engine = create_engine(f"sqlite:///{DB_PATH}", echo=False)

# Create the Declarative Base (All our tables will inherit from this)
Base = declarative_base()

# Create a Session class to handle our database transactions (CRUD operations)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """Dependency to get the database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

if __name__ == "__main__":
    print(f"Database engine initialized. Target: {DB_PATH}")