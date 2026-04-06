# football-data-co-uk
Project related with site: https://www.football-data.co.uk/

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
└── football_data_uk_bronze
    └── table: streaming table
└── football_data_uk_silver
    └── table: streaming table
└── football_data_uk_gold
    └── table: materialized view
```

## Volume structure
```
/Volumes/dev/football_data_uk_raw/files/
│
├── england_premier_league/
├── spain_la_liga/
├── germany_bundesliga/
├── italy_serie_a/
└── france_ligue_1/
```


Unit Catalog development based by: <br>
`https://community.databricks.com/t5/technical-blog/how-to-structure-unity-catalog-like-a-pro-real-world-hierarchy/ba-p/120125?utm_source=copilot.com `

<br>

`https://non-neutralzero.github.io/notebook/posts/databricks-naming-convention/?utm_source=copilot.com` 

This architecture leverages Databricks Lakeflow to automate a complete end-to-end data lifecycle, moving from external web ingestion to a refined Medallion Architecture within the Lakehouse.

By using Lakeflow, you transition from manual orchestration to a unified "data-as-code" approach that handles ingestion, transformation, and scheduling in a single pane of glass.
