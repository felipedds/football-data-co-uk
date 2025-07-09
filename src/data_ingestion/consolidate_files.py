import os
import pandas as pd
from glob import glob

# Define source and destination paths
raw_folder = "/workspaces/football-data-co-uk/data/raw"
output_folder = "/workspaces/football-data-co-uk/data/processed"
os.makedirs(output_folder, exist_ok=True)

# List of columns to keep
columns_to_keep = [
    "Div", "Date", "Time", "HomeTeam", "AwayTeam", "FTHG", "FTAG", "FTR",
    "HTHG", "HTAG", "HTR", "Referee", "HS", "AS", "HST", "AST",
    "HF", "AF", "HC", "AC", "HY", "AY", "HR", "AR"
]

# Get all CSV files in the raw folder
csv_files = glob(os.path.join(raw_folder, "*.csv"))

# Load and combine only desired columns
dataframes = []
for file in csv_files:
    print(f"Reading {file}...")
    try:
        df = pd.read_csv(file)
        # Keep only the required columns that are present in the file
        filtered_df = df[[col for col in columns_to_keep if col in df.columns]].copy()
        dataframes.append(filtered_df)
    except Exception as e:
        print(f"Skipping {file} due to error: {e}")

# Combine into one DataFrame
combined_df = pd.concat(dataframes, ignore_index=True)

# Save to CSV
output_file = os.path.join(output_folder, "football_data.csv")
combined_df.to_csv(output_file, index=False)
print(f"Consolidated file saved to: {output_file}")