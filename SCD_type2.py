from pyspark.sql import functions as F

def prepare_customer_version(df):
    return (
        df.withColumn("effective_from", F.current_timestamp())
          .withColumn("effective_to", F.lit(None).cast("timestamp"))
          .withColumn("is_current", F.lit(True))
    )

# In Azure Databricks, use DeltaTable.merge() to expire the previous
# current record and insert the new version when tracked attributes change.
