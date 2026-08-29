# Demo Results

The repository uses synthetic data so reviewers can reproduce the flow without Azure credentials.

## Synthetic dataset

| Dataset | Rows |
|---|---:|
| Customers | 100 |
| Products | 30 |
| Transactions | 1,000 |

These numbers are intentionally small. They are **not** presented as the scale of the professional migration experience.

## Production-scale mapping

The same patterns are intended for larger workloads:

- watermark-based extraction instead of repeated full scans
- Spark distributed transformations
- Delta Lake storage
- partition/pruning strategy
- quality and reconciliation checks
- audit metadata
- controlled watermark commits

Actual production-scale metrics should be taken from the relevant professional project, not inferred from this demo.
