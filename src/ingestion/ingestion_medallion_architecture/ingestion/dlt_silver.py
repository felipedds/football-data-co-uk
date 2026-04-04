from pyspark import pipelines as dp
from pyspark.sql.functions import col


@dp.table(
    name="dev_football_data_uk.france_ligue_1_silver.silver",
    comment="Cleaned Ligue 1 data (Silver layer)"
)

def silver_ligue1():
    df = dp.read_stream("dev_football_data_uk.france_ligue_1_bronze.bronze")

    return (
        df
        .dropDuplicates(["Date", "HomeTeam", "AwayTeam"]) # Remove duplicates
        .filter(col("Date").isNotNull()) # Basic Data quality
    )
