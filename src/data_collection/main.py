import os
import requests

# Destination folder
DEST_FOLDER = "/workspaces/football-data-co-uk/data/raw"
os.makedirs(DEST_FOLDER, exist_ok=True)

# Base URL and seasons
base_url = "https://www.football-data.co.uk/mmz4281"
seasons = ["2021", "2122", "2223", "2324", "2425"]  # Add more seasons as needed
leagues = ["E0"]  # Add more league codes like 'E1', 'D1' if needed

# Download files
for season in seasons:
    for league in leagues:
        file_name = f"{league}.csv"
        url = f"{base_url}/{season}/{file_name}"
        dest_path = os.path.join(DEST_FOLDER, f"{season}_{file_name}")
        
        print(f"Downloading {url}...")
        response = requests.get(url)
        if response.status_code == 200:
            with open(dest_path, 'wb') as f:
                f.write(response.content)
            print(f"Saved to {dest_path}")
        else:
            print(f"Failed to download {url} (Status code: {response.status_code})")