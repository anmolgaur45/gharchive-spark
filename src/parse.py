from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.functions import col, from_json

from src.schema import EVENT_SCHEMA, PAYLOAD_SCHEMA

def read_raw(spark: SparkSession, path: str) -> DataFrame:
    df = spark.read.schema(EVENT_SCHEMA).json(path)
    return df

def parse_events(df: DataFrame) -> DataFrame:

    df = df.withColumn("payload_parsed", from_json(col('payload'), PAYLOAD_SCHEMA))

    df = df.select(
        col("id"),
        col("type"),
        col("created_at"),
        col("public"),
        col("actor.id").alias("actor_id"),
        col("actor.login").alias("actor_login"),
        col("repo.id").alias("repo_id"),
        col("repo.name").alias("repo_name"),
        col("payload_parsed.ref").alias("payload_ref"),
        col("payload_parsed.push_id").alias("payload_push_id"),
        col("payload_parsed.head").alias("payload_head"),
        col("payload_parsed.before").alias("payload_before"),
        col("payload_parsed.repository_id").alias("payload_repository_id"),
        col("payload_parsed.ref_type").alias("payload_ref_type"),
        col("payload_parsed.action").alias("payload_action")
    )
    return df