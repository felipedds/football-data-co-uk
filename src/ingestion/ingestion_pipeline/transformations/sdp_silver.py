from pyspark import pipelines as dp
from pyspark.sql.functions import col


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

# Loop to create Silver tables
for country, league in leagues.items():

    table_name = f"{country}_{league}"
    bronze_table = f"{env}.{domain}_bronze.{table_name}"
    silver_table = f"{env}.{domain}_silver.{table_name}"

    @dp.table(
        name=silver_table,
        comment=f"Cleaned {league} data ({country}) - Silver layer"
    )
    def silver_table_fn(
        bronze_table=bronze_table
    ):
        df = dp.read_stream(bronze_table)

        return (
            df
            .dropDuplicates(["Date", "HomeTeam", "AwayTeam"])  # Remove duplicates
            .filter(col("Date").isNotNull())  # Basic data quality
        )
