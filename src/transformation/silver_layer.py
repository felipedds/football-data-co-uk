import os
import pandas as pd
from glob import glob


def validate_dataframe(df: pd.DataFrame, required_columns: list, unique_cols: list = None) -> None:
    """
    Valida o DataFrame: checa nulos, duplicados e linhas totalmente vazias.
    :param required_columns: Colunas obrigatórias sem NULLs
    :param unique_cols: Lista de colunas que devem ser únicas (opcional)
    """
    print("Validação do DataFrame (Silver Layer):")
    
    # Checar NULLs nas colunas obrigatórias
    for col in required_columns:
        if col in df.columns:
            nulls = df[col].isnull().sum()
            print(f"  - {col}: {nulls} valores nulos")
    
    # Checar linhas duplicadas com base nas colunas únicas
    if unique_cols:
        dup_count = df.duplicated(subset=unique_cols).sum()
        print(f"  - {dup_count} registros duplicados nas colunas {unique_cols}")
    
    # Checar linhas totalmente vazias
    empty_rows = df.isnull().all(axis=1).sum()
    print(f"  - {empty_rows} linhas totalmente vazias")
    print("Validação concluída.\n")



def silver_to_gold() -> None:
    # Colunas obrigatórias para validação
    required_columns = ["Div", "Date", "Time", "HomeTeam", "AwayTeam", "FTHG", "FTAG", "FTR", "HTHG", "HTAG", "HTR", "Referee", "HS", "AS", "HST", "AST", "HF", "AF", "HC", "AC", "HY", "AY", "HR", "AR"]
    unique_cols = ["Date", "HomeTeam", "AwayTeam"]  # combinação única para cada partida

    leagues = ["premier_league"]
    for league in leagues:
        # Define source and destination paths
        BRONZE_FOLDER = f"/Workspace/Repos/felipediasd@gmail.com/football-data-co-uk/data/bronze/{league}"
        SILVER_FILE = f"/Workspace/Repos/felipediasd@gmail.com/football-data-co-uk/data/silver/{league}/consolidated_data.parquet"

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

        # Validação antes de salvar
        validate_dataframe(combined_df, required_columns, unique_cols)

        # Save the combined DataFrame as a single Parquet file
        combined_df.to_parquet(SILVER_FILE, engine="pyarrow", index=False)
        print(f"Consolidated parquet file saved to: {SILVER_FILE}")


silver_to_gold()