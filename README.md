Markdown
# 💊 Pharma Radar: Advanced Pharmacovigilance Pipeline

## 📖 Project Overview
Pharma Radar is an automated data engineering pipeline designed to modernize pharmacovigilance by triangulating official adverse drug reactions (ADRs) with real-world patient anecdotes.

## ⚠️ Important Note on Data
Due to Reddit API restrictions (403 errors), Tier 2 currently relies on a static Data Lake strategy. You **must** manually download the raw social data before running the pipeline.

## 🛠️ Setup & Installation
Follow these exact steps to run the project locally.

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd pharma-radar
Create and activate a virtual environment:

Windows:

Bash
python -m venv venv
.\venv\Scripts\activate
Mac/Linux:

Bash
python3 -m venv venv
source venv/bin/activate
Install the required dependencies:

Bash
pip install -r requirements.txt
📥 Data Acquisition (Crucial Step)
Before running the code, you need to populate the raw data folder:

Go to Kaggle and download the "WebMD Drug Reviews Dataset".

Extract the downloaded .csv archive.

Rename the file to webmd_reviews.csv and place it strictly inside the data/raw/ directory.

🚀 How to Run the Pipeline
You do not need to execute the extraction or cleaning scripts individually. We have a master orchestrator that handles the entire flow.

Simply run:

Bash
python src/main_pipeline.py
This script will automatically:

Tier 1: Extract theoretical clinical data.

Tier 2: Clean and standardize the WebMD dataset.

Core Engine: Run the Fuzzy Matching algorithm to translate informal language into formal medical symptoms.

Tier 3: Prepare the architecture for FDA AEMS regulatory parsing.

All processed outputs and matches will be generated and saved in the data/processed/ folder.

🗺️ Next Steps (Roadmap)
UI/UX Dashboard: Implementing a Streamlit web interface to visualize the raw and processed data seamlessly, replacing raw CSV navigation.

Tier 3 Integration: Developing the full data parser for FDA AEMS ASCII quarterly files.


---
