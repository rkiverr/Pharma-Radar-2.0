from .db_core import SessionLocal
from .models import Drug, Symptom, Report

def create_drug(db, drug_name: str):
    """Inserts a new drug into the database if it doesn't already exist."""
    # First, check if it already exists to avoid duplicates
    existing_drug = db.query(Drug).filter(Drug.name == drug_name).first()
    if existing_drug:
        return existing_drug
        
    # If it's new, add it to the session and commit
    new_drug = Drug(name=drug_name)
    db.add(new_drug)
    db.commit()
    db.refresh(new_drug)
    return new_drug

def create_symptom(db, term: str):
    """Inserts a new formal medical symptom into the database."""
    existing_symptom = db.query(Symptom).filter(Symptom.formal_term == term).first()
    if existing_symptom:
        return existing_symptom
        
    new_symptom = Symptom(formal_term=term)
    db.add(new_symptom)
    db.commit()
    db.refresh(new_symptom)
    return new_symptom

# --- Quick Test Block ---
if __name__ == "__main__":
    db = SessionLocal()
    print("Initializing database injection test...")
    try:
        drug = create_drug(db, "Ibuprofen")
        symptom = create_symptom(db, "Dyspepsia")
        
        print(f"✅ Success! Added Drug: [{drug.id}] {drug.name}")
        print(f"✅ Success! Added Symptom: [{symptom.id}] {symptom.formal_term}")
    except Exception as e:
        print(f"❌ Transaction failed: {e}")
    finally:
        db.close()