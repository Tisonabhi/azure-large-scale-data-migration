from pyspark.sql import functions as F

def add_ingestion_metadata(df, run_id: str):
    return (
        df.withColumn("_run_id", F.lit(run_id))
          .withColumn("_ingested_at", F.current_timestamp())
    )

# Example:
# raw = spark.read.option("header", True).csv("/mnt/landing/transactions")
# bronze = add_ingestion_metadata(raw, "demo-run-001")
# bronze.write.format("delta").mode("append").save("/mnt/bronze/transactions")
