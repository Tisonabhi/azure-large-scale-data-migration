from pyspark.sql import functions as F

def build_daily_sales(transactions):
    return (
        transactions
        .groupBy("transaction_date")
        .agg(
            F.sum("amount").alias("total_sales"),
            F.sum("quantity").alias("units_sold"),
            F.countDistinct("customer_id").alias("active_customers")
        )
        .orderBy("transaction_date")
    )
