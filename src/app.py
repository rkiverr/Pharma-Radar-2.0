import streamlit as st
import pandas as pd
import os

# Configure the web page
st.set_page_config(page_title="Pharma Radar", page_icon="💊", layout="wide")

st.title("💊 Pharma Radar Dashboard")
st.markdown("### Translating real-world patient signals into regulatory intelligence.")

# Load the fuzzy matched data
DATA_PATH = "data/processed/fuzzy_matches.csv"

if os.path.exists(DATA_PATH):
    st.success("System Status: Online | Database Connected")
    
    # Read the data
    df = pd.read_csv(DATA_PATH)
    
    # Display top level metrics
    st.metric(label="Total Informal Signals Processed", value=len(df))
    
    st.subheader("Semantic Signal Translation (Social -> Clinical)")
    
    # Display the dataframe as an interactive table
    st.dataframe(df, use_container_width=True)
    
else:
    st.warning(f"Waiting for data... Please run the main pipeline first. Could not find {DATA_PATH}")