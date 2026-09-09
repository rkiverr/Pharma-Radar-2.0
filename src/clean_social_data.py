import pandas as pd
import os

def prepare_social_data(filepath, text_column, drug_column, target_drug="ibuprofen", sample_size=200):
    """Loads Kaggle data, filters by drug, and cleans the text for the Pharma Radar pipeline."""
    
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found. Make sure it is in the data/raw/ folder.")
        return None
        
    print(f"Loading data from {filepath}...")
    
    try:
        df = pd.read_csv(filepath)
    except Exception as e:
        print(f"Error reading the CSV: {e}")
        return None
    
    # Check if the columns actually exist in the file
    if drug_column not in df.columns or text_column not in df.columns:
        print(f"Error: Columns not found. Available columns are: {list(df.columns)}")
        return None

    # Filter only rows mentioning our target drug (case-insensitive)
    df_filtered = df[df[drug_column].astype(str).str.contains(target_drug, case=False, na=False)].copy()
    
    # Drop rows where the review text is empty
    df_clean = df_filtered.dropna(subset=[text_column]).copy()
    
    # Take a random sample to keep processing times fast during development
    if len(df_clean) > sample_size:
        df_clean = df_clean.sample(n=sample_size, random_state=42)
        
    # Standardize the output dataframe for the fuzzy matching phase
    final_df = pd.DataFrame({
        'post_id': range(1, len(df_clean) + 1),
        'informal_text': df_clean[text_column].astype(str)
    })
    
    return final_df

if __name__ == "__main__":
    # Update these variables based on the WebMD CSV you downloaded
    INPUT_FILE = "data/raw/webmd_reviews.csv"
    
    # You will need to change these if the Kaggle headers are named differently (e.g., "drugName" or "review")
    TEXT_COL = "Reviews" 
    DRUG_COL = "Drug"    
    
    processed_data = prepare_social_data(INPUT_FILE, TEXT_COL, DRUG_COL, target_drug="ibuprofen")
    
    if processed_data is not None:
        os.makedirs("data/processed", exist_ok=True)
        output_path = "data/processed/social_media_ready.csv"
        processed_data.to_csv(output_path, index=False)
        print(f"Success! {len(processed_data)} informal reports cleaned and saved to {output_path}")