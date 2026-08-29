from pyspark.sql import functions as F

def run_quality_checks(df):
    return {
        "row_count": df.count(),
        "null_transaction_id": df.filter(F.col("transaction_id").isNull()).count(),
        "null_customer_id": df.filter(F.col("customer_id").isNull()).count(),
        "negative_amount": df.filter(F.col("amount") < 0).count(),
        "duplicate_transaction_ids": (
            df.groupBy("transaction_id")
              .count()
              .filter(F.col("count") > 1)
              .count()
        )
    }
