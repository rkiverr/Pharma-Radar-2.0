import pandas as pd
from thefuzz import process, fuzz
import os

def load_data(clinical_path, social_path):
    """Loads the structured and unstructured data files."""
    if not os.path.exists(social_path):
        print(f"Error: Could not find {social_path}. Please run clean_social_data.py first.")
        return None, None
        
    df_social = pd.read_csv(social_path)
    
    # In a full pipeline, you would load this from clinical_path. 
    # For demonstration, we are using a mock subset of formal FDA/Clinical terms for Ibuprofen.
    df_clinical = pd.read_csv(clinical_path)
    
    return df_clinical, df_social

def match_symptoms(df_clinical, df_social, threshold=60):
    """
    Uses Levenshtein distance to find the closest formal medical term 
    for each informal patient review.
    """
    print("Starting fuzzy matching process (this may take a moment)...")
    
    formal_terms = df_clinical['adverse_event'].tolist()
    results = []
    
    for index, row in df_social.iterrows():
        informal_text = str(row['informal_text'])
        
        # thefuzz process.extractOne finds the best match from the list
        # We use token_set_ratio which is great for finding keywords inside longer sentences
        best_match = process.extractOne(
            informal_text, 
            formal_terms, 
            scorer=fuzz.token_set_ratio
        )
        
        if best_match:
            matched_term, score = best_match
            
            # Only keep matches that are above our confidence threshold
            if score >= threshold:
                results.append({
                    'post_id': row['post_id'],
                    'informal_text': informal_text,
                    'matched_formal_term': matched_term,
                    'confidence_score': score
                })
                
    return pd.DataFrame(results)

if __name__ == "__main__":
    SOCIAL_FILE = "data/processed/social_media_ready.csv"
    CLINICAL_FILE = "data/raw/clinical_trials_ibuprofen.csv"
    
    df_clinical, df_social = load_data(CLINICAL_FILE, SOCIAL_FILE)
    
    if df_clinical is not None and df_social is not None:
        matched_df = match_symptoms(df_clinical, df_social, threshold=40)
        
        output_path = "data/processed/fuzzy_matches.csv"
        matched_df.to_csv(output_path, index=False)
        
        print("\n--- Match Results Preview ---")
        print(matched_df.head(10))
        print(f"\nSuccess! Found {len(matched_df)} potential semantic matches.")
        print(f"Results saved to {output_path}")