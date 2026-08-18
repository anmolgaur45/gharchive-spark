from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    LongType,
    BooleanType,
    TimestampType,
)

EVENT_SCHEMA = StructType([
    StructField("id", StringType(), True),
    StructField("type", StringType(), True),
    StructField("created_at", TimestampType(), True),
    StructField("actor", StructType([
        StructField("id", LongType(), True),
        StructField("login", StringType(), True)
    ]), True),
    StructField("repo", StructType([
        StructField("name", StringType(), True),
        StructField("id", LongType(), True)
    ]), True),
    StructField("payload", StringType(), True),
    StructField("public", BooleanType(), True)
])

PAYLOAD_SCHEMA = StructType([
    StructField("ref", StringType(), True),
    StructField("push_id", LongType(), True),
    StructField("head", StringType(), True),
    StructField("before", StringType(), True),
    StructField("repository_id", LongType(), True),
    StructField("ref_type", StringType(), True),
    StructField("action", StringType(), True)
])