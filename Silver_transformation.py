from pyspark.sql import functions as F
from pyspark.sql.window import Window

def clean_transactions(df):
    typed = (
        df.withColumn("transaction_id", F.col("transaction_id").cast("long"))
          .withColumn("customer_id", F.col("customer_id").cast("long"))
          .withColumn("product_id", F.col("product_id").cast("long"))
          .withColumn("quantity", F.col("quantity").cast("int"))
          .withColumn("amount", F.col("amount").cast("decimal(18,2)"))
          .withColumn("transaction_date", F.to_date("transaction_date"))
          .withColumn("updated_at", F.to_timestamp("updated_at"))
    )

    valid = (
        typed
        .filter(F.col("transaction_id").isNotNull())
        .filter(F.col("customer_id").isNotNull())
        .filter(F.col("amount") >= 0)
    )

    window = Window.partitionBy("transaction_id").orderBy(F.col("updated_at").desc())

    return (
        valid.withColumn("_rn", F.row_number().over(window))
             .filter(F.col("_rn") == 1)
             .drop("_rn")
    )
