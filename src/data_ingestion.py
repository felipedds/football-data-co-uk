import os
import requests
import pandas as pd
from io import StringIO


def download_raw_data_main_leagues():
    BASE_URL = "https://www.football-data.co.uk/mmz4281"
    seasons = ["1819", "1920", "2021", "2122", "2223", "2324", "2425", "2526"]

    # League codes used by football-data.co.uk
    league_codes = {
        "premier_league": "E0",
        "la_liga": "SP1",
        "bundesliga": "D1",
        "serie_a": "I1",
        "ligue_1": "F1",
    }

    leagues = {
        "england": "premier_league",
        "spain": "la_liga",
        "germany": "bundesliga",
        "italy": "serie_a",
        "france": "ligue_1",
    }

    # Base folder where all files will be stored
    BASE_DESTINATION_FOLDER = r"C:\Users\felip\Documents\football-data-co-uk\data\raw"

    for country, league in leagues.items():

        # Create a subfolder for each league
        destination_folder = os.path.join(
            BASE_DESTINATION_FOLDER,
            f"{country}_{league}"
        )
        os.makedirs(destination_folder, exist_ok=True)

        league_code = league_codes[league]

        for season in seasons:
            file_name = f"{league_code}.csv"
            url = f"{BASE_URL}/{season}/{file_name}"
            file_path = os.path.join(
                destination_folder,
                f"{season}_{file_name}"
            )

            print(f"Fetching {url}...")
            response = requests.get(url, timeout=30)

            if response.status_code != 200:
                print(f"[{country}-{league}-{season}] Failed: {url}")
                continue

            # Load downloaded data
            new_df = pd.read_csv(
                StringIO(response.text),
                encoding="utf-8-sig"
            )

            # Clean column names
            new_df.columns = (
                new_df.columns.astype(str)
                .str.encode("utf-8", "ignore")
                .str.decode("utf-8", "ignore")
                .str.replace("ï»¿", "", regex=False)
                .str.replace("\ufeff", "", regex=False)
                .str.strip()
            )

            # Natural key for deduplication
            natural_key_cols = ["Date", "HomeTeam", "AwayTeam"]

            if os.path.exists(file_path):
                existing_df = pd.read_csv(
                    file_path,
                    encoding="utf-8-sig"
                )

                existing_df.columns = (
                    existing_df.columns.astype(str)
                    .str.encode("utf-8", "ignore")
                    .str.decode("utf-8", "ignore")
                    .str.replace("ï»¿", "", regex=False)
                    .str.replace("\ufeff", "", regex=False)
                    .str.strip()
                )

                # Identify new rows
                merged = new_df.merge(
                    existing_df,
                    on=natural_key_cols,
                    how="left",
                    indicator=True,
                    suffixes=("", "_existing"),
                )

                new_rows = merged[merged["_merge"] == "left_only"]

                if not new_rows.empty:
                    print(f"Appending {len(new_rows)} new rows to {file_path}")

                    cols_to_keep = [
                        col
                        for col in new_rows.columns
                        if not col.endswith("_existing")
                        and col != "_merge"
                    ]

                    new_rows = new_rows[cols_to_keep]

                    updated_df = (
                        pd.concat([existing_df, new_rows])
                        .drop_duplicates(
                            subset=natural_key_cols,
                            keep="last",
                        )
                    )

                    updated_df.to_csv(file_path, index=False, encoding="utf-8-sig",)
                else:
                    print(f"No new rows for {file_path}")

            else:
                print(f"Saving new file: {file_path}")
                new_df.to_csv(file_path, index=False, encoding="utf-8-sig",)


def download_raw_data_extra_leagues():
    BASE_URL = "https://www.football-data.co.uk/new"

    # League codes used by football-data.co.uk
    league_codes = {
        "campeonato_brasileiro": "BRA",
        "primera_division": "ARG",
    }

    leagues = {
        "brazil": "campeonato_brasileiro",
        "argentina": "primera_division",
    }

    # Base folder where all files will be stored
    BASE_DESTINATION_FOLDER = r"C:\Users\felip\Documents\football-data-co-uk\data\raw"

    for country, league in leagues.items():

        # Create a subfolder for each league
        destination_folder = os.path.join(BASE_DESTINATION_FOLDER, f"{country}_{league}")
        os.makedirs(destination_folder, exist_ok=True)

        league_code = league_codes[league]

        file_name = f"{league_code}.csv"
        url = f"{BASE_URL}/{file_name}"
        file_path = os.path.join(destination_folder, file_name)

        print(f"Fetching {url}...")
        response = requests.get(url, timeout=30)

        if response.status_code != 200:
            print(f"[{country}-{league}] Failed: {url}")
            continue

        # Load downloaded data
        new_df = pd.read_csv(StringIO(response.text), encoding="utf-8-sig")

        # Clean column names
        new_df.columns = (
            new_df.columns.astype(str)
            .str.encode("utf-8", "ignore")
            .str.decode("utf-8", "ignore")
            .str.replace("ï»¿", "", regex=False)
            .str.replace("\ufeff", "", regex=False)
            .str.strip()
        )

        # Natural key for deduplication
        natural_key_cols = ["Date", "HomeTeam", "AwayTeam"]

        if os.path.exists(file_path):
            existing_df = pd.read_csv(file_path, encoding="utf-8-sig")

            existing_df.columns = (
                existing_df.columns.astype(str)
                .str.encode("utf-8", "ignore")
                .str.decode("utf-8", "ignore")
                .str.replace("ï»¿", "", regex=False)
                .str.replace("\ufeff", "", regex=False)
                .str.strip()
            )

            # Identify new rows
            merged = new_df.merge(existing_df, on=natural_key_cols, how="left", indicator=True, suffixes=("", "_existing"),)

            new_rows = merged[merged["_merge"] == "left_only"]

            if not new_rows.empty:
                print(f"Appending {len(new_rows)} new rows to {file_path}")

                cols_to_keep = [col
                    for col in new_rows.columns
                    if not col.endswith("_existing") and col != "_merge"
                ]

                new_rows = new_rows[cols_to_keep]

                updated_df = (pd.concat([existing_df, new_rows]).drop_duplicates(subset=natural_key_cols, keep="last",))

                updated_df.to_csv(file_path, index=False, encoding="utf-8-sig",)
            else:
                print(f"No new rows for {file_path}")

        else:
            print(f"Saving new file: {file_path}")
            new_df.to_csv(file_path, index=False, encoding="utf-8-sig",)

#download_raw_data_main_leagues()
download_raw_data_extra_leagues()
