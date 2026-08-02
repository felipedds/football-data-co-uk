# football-data-co-uk
Project related with site: https://www.football-data.co.uk/

The name convention followed was: https://learn.microsoft.com/en-us/training/wwl-databricks/create-and-organize-objects-in-unity-catalog/2-apply-naming-conventions

```
[Python script]
        ↓
API (football-data.co.uk)
        ↓
CSV files download 
        ↓
dev (catalog)
└── football_data_uk_raw (schema)
    └── volume: files
└── football_data_uk_bronze (schema)
    └── table: streaming table
└── football_data_uk_silver (schema)
    └── table: streaming table
└── football_data_uk_gold (schema)
    └── table: materialized view
```

## Commands
```python -m venv .venv```       # Create a virtual environment
```.venv\Scripts\Activate.ps1``` # Activate it
```pip install -e .```           # Install the project and its dependencies

## Folder structure
statsbomb/
├── data/
│   ├── raw/                 # Raw data files
│   ├── processed/           # Processed data files
│   └── external/            # External datasets or data obtained from external sources
├── notebooks/               # Jupyter notebooks for data exploration, and analysis
├── src/                     # Source code
│   ├── data_collection/     # Scripts or modules for data collection
│   ├── data_preprocessing/  # Scripts or modules for data preprocessing
│   ├── feature_engineering/ # Scripts or modules for feature engineering
│   ├── modeling/            # Scripts or modules for modeling (machine learning models)
│   └── evaluation/          # Scripts for model evaluation and performance metrics
|   └── main.py 
├── reports/                 # Reports generated(HTML, PDF) from analysis and modeling
├── models/                  # Saved models or model artifacts
├── environment.yml          # Conda environment file specifying dependencies
├── README.md                # README file describing the project and its components
└── requirements.txt         # Python dependencies file (alternative to environment.yml)



Unit Catalog development based by: <br>
`https://community.databricks.com/t5/technical-blog/how-to-structure-unity-catalog-like-a-pro-real-world-hierarchy/ba-p/120125?utm_source=copilot.com `

<br>

`https://non-neutralzero.github.io/notebook/posts/databricks-naming-convention/?utm_source=copilot.com` 

This architecture leverages Databricks Lakeflow to automate a complete end-to-end data lifecycle, moving from external web ingestion to a refined Medallion Architecture within the Lakehouse.

By using Lakeflow, you transition from manual orchestration to a unified "data-as-code" approach that handles ingestion, transformation, and scheduling in a single pane of glass.
