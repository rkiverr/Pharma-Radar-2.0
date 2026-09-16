import requests
import pandas as pd

def fetch_clinical_trials(search_term, max_results=50): # 1. Aumentamos a 50
    """Descarga los estudios de la API."""
    base_url = "https://clinicaltrials.gov/api/v2/studies"
    params = {"query.term": search_term, "pageSize": max_results, "format": "json"}
    
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    return None

def extract_adverse_events(api_data):
    """Navega por el laberinto del JSON para extraer los efectos adversos."""
    records = []
    
    for study in api_data.get('studies', []):
        nct_id = study.get('protocolSection', {}).get('identificationModule', {}).get('nctId', 'Sin ID')
        
        events_module = study.get('resultsSection', {}).get('adverseEventsModule', {})
        
        # 2. NUEVO: Buscamos tanto eventos serios como eventos comunes (otros)
        serious_events = events_module.get('seriousEvents', [])
        other_events = events_module.get('otherEvents', [])
        
        # Juntamos ambas listas en una sola
        all_events = serious_events + other_events
        
        for event in all_events:
            term = event.get('term', 'Desconocido')
            organ_system = event.get('organSystem', 'Desconocido')
            
            records.append({
                'nct_id': nct_id,
                'adverse_event': term,
                'organ_system': organ_system
            })
            
    return records

if __name__ == "__main__":
    print("Descargando datos...")
    raw_data = fetch_clinical_trials("Ibuprofen", max_results=50)
    
    if raw_data:
        print("Extrayendo efectos adversos...")
        extracted_events = extract_adverse_events(raw_data)
        
        if extracted_events:
            df = pd.DataFrame(extracted_events)
            output_path = "data/raw/clinical_trials_ibuprofen.csv"
            df.to_csv(output_path, index=False)
            print(f"¡Listo! Se guardaron {len(df)} efectos adversos en {output_path}")
        else:
            print("No se encontraron efectos adversos.")