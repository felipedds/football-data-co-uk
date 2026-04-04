from pyspark import pipelines as dp
from pyspark.sql.functions import col, sum


@dp.table(
    name="dev_football_data_uk.france_ligue_1_gold.gold",
    comment="Aggregated team statistics"
)

def gold_ligue1():
    df = dp.read("dev_football_data_uk.france_ligue_1_silver.silver")

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
