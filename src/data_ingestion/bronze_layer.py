from pyspark.sql import SparkSession
from pyspark.sql.functions import lit
import pandas as pd
import os


# Spark session
spark = SparkSession.builder.getOrCreate()

# Folder raw layer
RAW_FOLDER = "/Workspace/Repos/felipediasd@gmail.com/football-data-co-uk/data/raw"

# Lista todos os arquivos CSV no raw folder
csv_files = [f for f in os.listdir(RAW_FOLDER) if f.endswith(".csv")]

for csv_file in csv_files:
    # Extrair metadados do nome do arquivo
    season, league_code = csv_file.split("_")
    league_code = league_code.replace(".csv", "")
    
    print(f"Processing {csv_file} for season {season}, league {league_code}...")
    
    # Caminho completo do arquivo CSV
    csv_path = os.path.join(RAW_FOLDER, csv_file)
    
    # Read CSV
    df = pd.read_csv(csv_path)

    # Caminho para salvar Delta
    parquet_path = f"{RAW_FOLDER}/{season}_{league_code}.parquet"
    print(f"Saved Delta table to {parquet_path}")

    # Salvar como Delta (partitioned by season and league_code)
    df.to_parquet(parquet_path, engine="pyarrow", index=False)
    print(f"Saved Delta table to {parquet_path}")

