from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .db_core import Base, engine

class Drug(Base):
    __tablename__ = 'drugs'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    
    # Establish a relationship to the reports table
    reports = relationship("Report", back_populates="drug")

class Symptom(Base):
    __tablename__ = 'symptoms'
    
    id = Column(Integer, primary_key=True, index=True)
    formal_term = Column(String, unique=True, index=True, nullable=False)
    
    reports = relationship("Report", back_populates="symptom")

class Report(Base):
    __tablename__ = 'reports'
    
    id = Column(Integer, primary_key=True, index=True)
    informal_text = Column(String, nullable=False)
    source_tier = Column(String, nullable=False) # e.g., "Tier 2: WebMD" or "Tier 3: FDA"
    confidence_score = Column(Float, nullable=True) # From the Fuzzy Matcher
    
    # Foreign Keys linking to the drugs and symptoms tables
    drug_id = Column(Integer, ForeignKey('drugs.id'))
    symptom_id = Column(Integer, ForeignKey('symptoms.id'))
    
    # Relationships
    drug = relationship("Drug", back_populates="reports")
    symptom = relationship("Symptom", back_populates="reports")

def create_tables():
    """Generates the tables in the SQLite database based on the classes above."""
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")

if __name__ == "__main__":
    create_tables()