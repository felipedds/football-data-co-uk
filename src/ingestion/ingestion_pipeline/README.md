# ingestion_pipeline

#### Unity Catalog structure
Catalog: dev

Schemas:
- football_data_uk_raw
- football_data_uk_bronze
- football_data_uk_silver
- football_data_uk_gold

Volume:
- dev.football_data_uk_raw.files

### Raw Folder Structure
```
/Volumes/dev/football_data_uk_raw/files/
├── england_premier_league/
├── spain_la_liga/
├── germany_bundesliga/
├── italy_serie_a/
└── france_ligue_1/
```

#### Configure schema tracking (Auto Loader)
Auto Loader requires a schema tracking location.
Path:
```/Volumes/dev/football_data_uk_raw/files/_schemas/```
This stores:
- inferred schema
- processed files metadata


This folder defines all source code for the 'ingestion_pipeline' pipeline:

- `explorations`: Ad-hoc notebooks used to explore the data processed by this pipeline.
- `transformations`: All dataset definitions and transformations.
- `utilities`: Utility functions and Python modules used in this pipeline.
