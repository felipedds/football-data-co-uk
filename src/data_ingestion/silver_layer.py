import os
import pandas as pd
from glob import glob

# Define source and destination paths
BRONZE_FOLDER = "/Workspace/Repos/felipediasd@gmail.com/football-data-co-uk/data/bronze"
OUTPUT_FILE = "/Workspace/Repos/felipediasd@gmail.com/football-data-co-uk/data/silver/consolidated_data.parquet"

# List of columns to keep
columns_to_keep = [
    "Div", "Date", "Time", "HomeTeam", "AwayTeam", "FTHG", "FTAG", "FTR", "HTHG", "HTAG", "HTR",
    "Referee", "HS", "AS", "HST", "AST", "HF", "AF", "HC", "AC", "HY", "AY", "HR", "AR"
]

# Get all Parquet files in the bronze folder
parquet_files = glob(os.path.join(BRONZE_FOLDER, "*.parquet"))

# Load and combine only desired columns
combined_df = pd.DataFrame()

for file in parquet_files:
    print(f"Reading {file}...")
    try:
        df = pd.read_parquet(file, engine="pyarrow")
        # Keep only required columns that exist in the file
        filtered_df = df[[col for col in columns_to_keep if col in df.columns]].copy()
        combined_df = pd.concat([combined_df, filtered_df], ignore_index=True)
    except Exception as e:
        print(f"Skipping {file} due to error: {e}")

# Save the combined DataFrame as a single Parquet file
combined_df.to_parquet(OUTPUT_FILE, engine="pyarrow", index=False)
print(f"Consolidated parquet file saved to: {OUTPUT_FILE}")
