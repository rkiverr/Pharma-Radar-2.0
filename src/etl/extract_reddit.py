import requests
import pandas as pd

def extract_reddit_public(search_term, limit=50):
    """Busca en Reddit usando su endpoint público JSON sin necesidad de API Keys."""
    
    url = "https://www.reddit.com/search.json"
    params = {
        "q": search_term,
        "limit": limit
    }
    
    # TRUCO: Disfrazamos nuestro script con un User-Agent personalizado
    # Si no hacemos esto, Reddit nos bloqueará con un error 429
   # TRUCO 2: Un User-Agent honesto y estructurado
    headers = {
        "User-Agent": "windows:pharma-radar-script:v1.0 (by /u/TuUsuarioRealDeReddit)"
    }
    
    print(f"Buscando '{search_term}' en Reddit (vía endpoint público)...")
    response = requests.get(url, params=params, headers=headers)
    
    if response.status_code != 200:
        print(f"Error de conexión: Código {response.status_code}")
        return []
        
    data = response.json()
    records = []
    
    # Navegamos el "laberinto" del JSON de Reddit
    children = data.get("data", {}).get("children", [])
    
    for child in children:
        post = child.get("data", {})
        body_text = post.get("selftext", "")
        
        # Filtramos posts vacíos, borrados o que solo son imágenes
        if body_text and body_text not in ['[deleted]', '[removed]']:
            records.append({
                "post_id": post.get("id"),
                "subreddit": post.get("subreddit"),
                "title": post.get("title"),
                "body_text": body_text,
                "url": f"https://www.reddit.com{post.get('permalink')}"
            })
            
    return records

if __name__ == "__main__":
    # Buscamos testimonios reales sobre efectos secundarios del Ibuprofeno
    extracted_posts = extract_reddit_public("ibuprofen side effects", limit=100)
    
    if extracted_posts:
        df = pd.DataFrame(extracted_posts)
        output_path = "data/raw/reddit_ibuprofen_real.csv"
        df.to_csv(output_path, index=False)
        print(f"¡Hack exitoso! Se guardaron {len(df)} posts reales en {output_path}")
    else:
        print("No se encontraron posts con texto válido.")