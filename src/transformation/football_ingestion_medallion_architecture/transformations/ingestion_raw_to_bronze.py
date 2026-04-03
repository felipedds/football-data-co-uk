import dlt
from pyspark.sql.functions import current_timestamp, col


@dlt.table(
    name="dev_football_data_uk.france_ligue_1_bronze.france_ligue_1_bronze",
    comment="Raw ingestion of Ligue 1 CSV data"
)
def bronze_ligue1():

    df = (
        spark.readStream
        .format("cloudFiles")
        .option("cloudFiles.format", "csv")
        .option("header", "true")
        .option("cloudFiles.inferColumnTypes", "true")
        .option(
            "cloudFiles.schemaLocation",
            "/Volumes/dev_football_data_uk/france_ligue_1_raw/files/_schema/"
        )
        .load("/Volumes/dev_football_data_uk/france_ligue_1_raw/files/")
    )

    return df.withColumn("ingestion_time", current_timestamp()) \
             .withColumn("source_file", col("_metadata.file_path"))