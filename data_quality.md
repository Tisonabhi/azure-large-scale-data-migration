# Data Quality Framework

Checks implemented:

| Check | Rule | Action |
|---|---|---|
| Null transaction ID | Must not be null | Reject |
| Null customer ID | Must not be null | Reject |
| Negative amount | Amount >= 0 | Reject |
| Duplicate transaction ID | Unique business key | Deduplicate/reject |
| Valid customer status | ACTIVE/INACTIVE | Reject |
| Referential integrity | Customer must exist | Flag |

Recommended production extensions:

- Great Expectations / native expectations
- Delta constraints
- reconciliation against source counts
- SLA monitoring
- alerting through Azure Monitor
