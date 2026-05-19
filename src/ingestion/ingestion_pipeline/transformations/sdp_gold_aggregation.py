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

def create_gold(country, league):
    
    table_name = f"{country}_{league}"
    silver_table = f"{env}.{domain}_silver.{table_name}"
    gold_table = f"{env}.{domain}_gold.{table_name}"

    @dp.materialized_view(name=gold_table, comment=f"Aggregated team statistics ({league} - {country})")
    def gold():
        df = spark.read.table(silver_table)

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

# Create all tables
for country, league in leagues.items():
    create_gold(country, league)
