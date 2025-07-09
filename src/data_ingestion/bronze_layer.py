from pyspark.sql import SparkSession
from pyspark.sql.functions import lit
import pandas as pd
import os


# Spark session
spark = SparkSession.builder.getOrCreate()

# Folder raw layer
RAW_FOLDER = "/Workspace/Repos/felipediasd@gmail.com/football-data-co-uk/data/raw"
BRONZE_FOLDER = "/Workspace/Repos/felipediasd@gmail.com/football-data-co-uk/data/bronze"

# Lista todos os arquivos CSV no raw folder
csv_files = [f for f in os.listdir(RAW_FOLDER) if f.endswith(".csv")]

for csv_file in csv_files:
    # Extrair metadados do nome do arquivo
    season, league_code = csv_file.split("_")
    league_code = league_code.replace(".csv", "")
    
    print(f"Processing {csv_file} for season {season}, league {league_code}...")
    
    # CSV path
    csv_path = os.path.join(RAW_FOLDER, csv_file)
    
    # Read CSV
    df = pd.read_csv(csv_path)

    # Parquet path
    parquet_path = f"{BRONZE_FOLDER}/{season}_{league_code}.parquet"

    # Save parquet file
    df.to_parquet(parquet_path, engine="pyarrow", index=False)
    print(f"Saved parquet file to {parquet_path}")

