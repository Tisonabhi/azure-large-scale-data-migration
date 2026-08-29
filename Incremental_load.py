from pyspark.sql import functions as F

def filter_incremental(df, watermark: str):
    return df.filter(F.col("updated_at") > F.to_timestamp(F.lit(watermark)))

# Production pattern:
# 1. Read previous successful watermark.
# 2. Determine new source watermark.
# 3. Extract only the delta.
# 4. Validate and transform.
# 5. Commit target changes.
# 6. Advance watermark only after success.
