from pyspark import pipelines as dp
from pyspark.sql.functions import col, sum


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

# Loop to create Gold tables
for country, league in leagues.items():

    table_name = f"{country}_{league}"
    silver_table = f"{env}.{domain}_silver.{table_name}"
    gold_table = f"{env}.{domain}_gold.{table_name}"

    @dp.table(
        name=gold_table,
        comment=f"Aggregated team statistics ({league} - {country})"
    )
    def gold_table_fn(silver_table=silver_table):
        df = dp.read(silver_table)

        home = df.select(
            col("HomeTeam").alias("Team"),
            col("FTHG").alias("GoalsForFullTime"),
            col("FTAG").alias("GoalsAgainstFullTime")
        )

        away = df.select(
            col("AwayTeam").alias("Team"),
            col("FTAG").alias("GoalsForFullTime"),
            col("FTHG").alias("GoalsAgainstFullTime")
        )

        combined = home.unionByName(away)

        return combined.groupBy("Team").agg(
            sum("GoalsForFullTime").alias("total_goals_scored"),
            sum("GoalsAgainstFullTime").alias("total_goals_conceded")
        )
