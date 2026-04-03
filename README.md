# football-data-co-uk
Project related with site: https://www.football-data.co.uk/

```
[Python script]
        ↓
API (football-data.co.uk)
        ↓
CSV download
        ↓
Databricks Volume (RAW layer) [/Volumes/dev_football_data_uk/france_ligue_1_raw/files]
        ↓
Spark Declarative Pipeline (SDP)
        ↓
dev_football_data_uk.england_premier_league_bronze
dev_football_data_uk.england_premier_league_silver
dev_football_data_uk.england_premier_league_gold
```

Unit Catalog development based by: <br>
`https://community.databricks.com/t5/technical-blog/how-to-structure-unity-catalog-like-a-pro-real-world-hierarchy/ba-p/120125?utm_source=copilot.com `

<br>

`https://non-neutralzero.github.io/notebook/posts/databricks-naming-convention/?utm_source=copilot.com` 

This architecture leverages Databricks Lakeflow to automate a complete end-to-end data lifecycle, moving from external web ingestion to a refined Medallion Architecture within the Lakehouse.

By using Lakeflow, you transition from manual orchestration to a unified "data-as-code" approach that handles ingestion, transformation, and scheduling in a single pane of glass.
