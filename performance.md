# Performance Engineering

For large Spark workloads:

1. Filter early using source predicates/watermarks.
2. Select only required columns.
3. Avoid unnecessary `collect()` and driver-side processing.
4. Broadcast only genuinely small dimensions.
5. Reduce unnecessary shuffles.
6. Use Delta tables and appropriate table optimization.
7. Partition only on useful, reasonably selective columns.
8. Monitor Spark UI for skew, spills and long-running stages.
9. Use incremental processing instead of repeated full scans.
10. Benchmark before and after every major optimization.

For a production 11+ TB migration, sizing and performance claims should be backed by actual workload measurements rather than the synthetic sample in this repository.
