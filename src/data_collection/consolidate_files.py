import os
import pandas as pd
from glob import glob

# Define source and destination paths
raw_folder = "/workspaces/football-data-co-uk/data/raw"
output_folder = "/workspaces/football-data-co-uk/data/processed"
os.makedirs(output_folder, exist_ok=True)

# Get all CSV files in raw folder
csv_files = glob(os.path.join(raw_folder, "*.csv"))

# Load and combine them
dataframes = []
for file in csv_files:
    print(f"Reading {file}...")
    try:
        df = pd.read_csv(file)
        df["source_file"] = os.path.basename(file)  # Optional: to track source
        dataframes.append(df)
    except Exception as e:
        print(f"Skipping {file} due to error: {e}")

# Concatenate into one DataFrame
combined_df = pd.concat(dataframes, ignore_index=True)

# Save to one CSV
output_file = os.path.join(output_folder, "football_data.csv")
combined_df.to_csv(output_file, index=False)
print(f"Consolidated file saved to: {output_file}")