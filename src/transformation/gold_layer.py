import pandas as pd


leagues = ["premier_league"]
for league in leagues:
    # Paths
    SILVER_FILE = f"/Workspace/Repos/felipediasd@gmail.com/football-data-co-uk/data/silver/{league}/consolidated_data.parquet"
    GOLD_FILE = f"/Workspace/Repos/felipediasd@gmail.com/football-data-co-uk/data/gold/{league}/enriched_data.parquet"

    # Read Silver layer parquet file
    df_gold = pd.read_parquet(SILVER_FILE, engine="pyarrow")

    # Add new columns
    df_gold["TotalGoals"] = df_gold["FTHG"] + df_gold["FTAG"]
    df_gold["GoalDifference"] = df_gold["FTHG"] - df_gold["FTAG"]

    # Save as Gold layer parquet file
    df_gold.to_parquet(GOLD_FILE, engine="pyarrow", index=False)
    print(f"Gold layer parquet file saved to: {GOLD_FILE}")
