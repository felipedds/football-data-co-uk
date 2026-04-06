import os
import requests


def download_raw_data():
    BASE_URL = "https://www.football-data.co.uk/mmz4281"
    seasons = ["1819", "1920", "2021", "2122", "2223", "2324", "2425"]

    # Map league → code
    league_codes = {
        "premier_league": "E0",
        "la_liga": "SP1",
        "bundesliga": "D1",
        "serie_a": "I1",
        "ligue_1": "F1"
    }

    # Updated structure
    environments = ["dev"]
    domain = "football_data_uk"

    leagues = {
        "england": "premier_league",
        "spain": "la_liga",
        "germany": "bundesliga",
        "italy": "serie_a",
        "france": "ligue_1"
    }

    for env in environments:
        for country, league in leagues.items():
            # Folder structure
            DESTINATION_FOLDER = (f"/Volumes/{env}/{domain}_raw/files/{country}_{league}/")
            os.makedirs(DESTINATION_FOLDER, exist_ok=True)

            league_code = league_codes[league]

            # DOWNLOAD FILES
            for season in seasons:
                file_name = f"{league_code}.csv"
                url = f"{BASE_URL}/{season}/{file_name}"
                file_path = os.path.join(
                    DESTINATION_FOLDER, f"{season}_{file_name}"
                )

                if os.path.exists(file_path):
                    print(f"Skipping: {file_path}")
                    continue

                print(f"Downloading {url}...")
                response = requests.get(url, timeout=30)

                if response.status_code == 200:
                    with open(file_path, "wb") as f:
                        f.write(response.content)
                    print(f"Saved: {file_path}")
                else:
                    print(f"Failed: {url} ({response.status_code})")
                    