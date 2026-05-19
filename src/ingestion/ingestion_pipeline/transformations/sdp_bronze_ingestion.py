from pyspark import pipelines as dp
from pyspark.sql.functions import current_timestamp, col


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

# Loop to create one table per league
for country, league in leagues.items():

    table_name = f"{country}_{league}"
    full_table_name = f"{env}.{domain}_bronze.{table_name}"

    source_path = f"/Volumes/{env}/{domain}_raw/files/{table_name}/"
    schema_path = f"/Volumes/{env}/{domain}_raw/files/_schemas/{table_name}/"
    
    @dp.table(name=full_table_name, comment=f"Raw ingestion of {league} CSV data ({country})")
    def bronze_table(table_name=table_name, source_path=source_path, schema_path=schema_path):
        df = (
            spark.readStream
            .format("cloudFiles")
            .option("cloudFiles.format", "csv")
            .option("header", "true")
            .option("cloudFiles.inferColumnTypes", "true")
            .option("cloudFiles.schemaLocation", schema_path)
            .option("cloudFiles.rescuedDataColumn", "_rescued_data")
            .load(source_path)
        )

        return (
            df.withColumn("ingestion_time", current_timestamp())
              .withColumn("source_file", col("_metadata.file_path"))
        )
        