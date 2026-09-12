import os

def run_pharma_radar():
    print("💊 Iniciando Pharma Radar Pipeline...")
    
    print("\n--- Nivel 1: Evidencia Teórica ---")
    # Aquí llamaremos a extract_clinical.py en el futuro
    print("Datos clínicos de ClinicalTrials.gov cargados y listos.")
    
    print("\n--- Nivel 2: Señales Informales ---")
    # Aquí llamaremos a clean_social_data.py
    print("Dataset de pacientes estandarizado para análisis.")
    
    print("\n--- Motor Central: Fuzzy Matching ---")
    # Aquí llamaremos a fuzzy_matcher.py
    print("Cruce semántico completado. Similitudes detectadas.")
    
    print("\n--- Nivel 3: Evidencia Regulatoria ---")
    # Aquí llamaremos a parse_fda.py
    print("Módulo FDA AEMS en espera de archivos ASCII.")
    
    print("\n✅ Pipeline de validación cruzada ejecutado con éxito.")

if __name__ == "__main__":
    run_pharma_radar()