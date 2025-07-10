from pyspark.sql import SparkSession
from pyspark.sql.functions import lit
import pandas as pd
import os


# Spark session
spark = SparkSession.builder.appName("GoldLayer").getOrCreate()