from pyspark.sql import DataFrame
from pyspark.sql.functions import col, to_date


def write_parquet(df: DataFrame, path: str, mode: str = "overwrite") -> None:

    df = df.withColumn("event_date", to_date(col("created_at")))

    df.write.mode(mode).option("compression", "zstd").partitionBy("event_date").parquet(path)