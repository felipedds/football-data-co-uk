import pandas as pd


# Paths
SILVER_FILE = "/Workspace/Repos/felipediasd@gmail.com/football-data-co-uk/data/silver/consolidated_data.parquet"
GOLD_FILE = "/Workspace/Repos/felipediasd@gmail.com/football-data-co-uk/data/gold/enriched_data.parquet"

# Read Silver layer parquet file
df_silver = pd.read_parquet(SILVER_FILE, engine="pyarrow")

# Add new columns
df_silver["TotalGoals"] = df_silver["FTHG"] + df_silver["FTAG"]
df_silver["GoalDifference"] = df_silver["FTHG"] - df_silver["FTAG"]

# Save as Gold layer parquet file
df_silver.to_parquet(GOLD_FILE, engine="pyarrow", index=False)
print(f"Gold layer parquet file saved to {GOLD_FILE}")
