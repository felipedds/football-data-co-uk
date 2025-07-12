import pandas as pd


# Paths
silver_file = "/Workspace/Repos/felipediasd@gmail.com/football-data-co-uk/data/silver/consolidated_data.parquet"
gold_file = "/Workspace/Repos/felipediasd@gmail.com/football-data-co-uk/data/gold/enriched_data.parquet"

# Read Silver layer parquet file
df_silver = pd.read_parquet(silver_file, engine="pyarrow")

# Add new columns
df_silver["TotalGoals"] = df_silver["FTHG"] + df_silver["FTAG"]
df_silver["GoalDifference"] = df_silver["FTHG"] - df_silver["FTAG"]

# Save as Gold layer parquet file
df_silver.to_parquet(gold_file, engine="pyarrow", index=False)
print(f"Gold layer parquet file saved to {gold_file}")
