from pyspark import pipelines as dp


# Config
env = "dev"
domain = "football_data_uk"

leagues = {
    "england": "premier_league",
    "spain": "la_liga",
    "germany": "bundesliga",
    "italy": "serie_a",
    "france": "ligue_1"
}

def create_silver(country, league):

    table_name = f"{country}_{league}"
    bronze_table = f"{env}.{domain}_bronze.{table_name}"
    silver_table = f"{env}.{domain}_silver.{table_name}"

    # Create target streaming table
    dp.create_streaming_table(name=silver_table, comment=f"Cleaned {league} data ({country}) - Silver layer")

    # Apply Auto CDC to handle deduplication
    dp.create_auto_cdc_flow(
        target=silver_table,
        source=bronze_table,
        keys=["Date", "HomeTeam", "AwayTeam"],
        sequence_by="ingestion_time",
        stored_as_scd_type=1  # Keep only latest record
    )

# Create all tables
for country, league in leagues.items():
    create_silver(country, league)
