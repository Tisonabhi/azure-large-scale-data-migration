# Azure Large-Scale Data Migration & Lakehouse Engineering

[![CI](https://github.com/Tisonabhi/azure-large-scale-data-migration/actions/workflows/ci.yml/badge.svg)](https://github.com/Tisonabhi/azure-large-scale-data-migration/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Azure](https://img.shields.io/badge/Azure-Data%20Engineering-0078D4)
![Databricks](https://img.shields.io/badge/Databricks-PySpark-red)
![Delta Lake](https://img.shields.io/badge/Delta%20Lake-Lakehouse-00A36C)



## Why this project

The project demonstrates the engineering patterns behind a large-scale SQL Server → Azure data-platform modernization:

- Full + incremental ingestion
- Watermark-based processing
- Bronze/Silver/Gold architecture
- PySpark transformations
- Delta Lake merge/upsert patterns
- SCD Type 2
- Data-quality and quarantine handling
- Source-to-target reconciliation
- Audit metadata
- Performance optimization
- CI validation with GitHub Actions

## Architecture

![Architecture](architecture/architecture.svg)

```text
SQL Server
    |
    v
Azure Data Factory
    |
    v
ADLS Gen2 / Bronze
    |
    v
Azure Databricks + PySpark
    |
    +----> Quality / Quarantine
    |
    v
Delta Silver
    |
    v
Delta Gold
    |
    v
BI / Analytics
```

## Repository layout

```text
azure-large-scale-data-migration/
├── .github/workflows/ci.yml
├── architecture/
│   ├── architecture.md
│   └── architecture.svg
├── adf/
│   ├── pipeline_full_load.json
│   └── pipeline_incremental_load.json
├── config/
├── data/
├── databricks/
├── docs/
├── sql/
├── tests/
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── SECURITY.md
└── requirements.txt
```

## Data flow

### 1. Full load

The initial load copies source tables into the Bronze layer.

### 2. Incremental load

A source `updated_at` column is used as a high watermark:

```text
last_successful_watermark
            |
            v
updated_at > previous watermark
            |
            v
incremental extraction
            |
            v
transform + validate
            |
            v
commit target
            |
            v
advance watermark
```

The watermark is advanced only after successful downstream processing.

### 3. Silver processing

PySpark:

- casts columns to expected types
- removes invalid business keys
- rejects negative amounts
- deduplicates by transaction ID
- standardizes timestamps and dates

### 4. Gold processing

The demo creates analytics-ready daily sales metrics:

- total sales
- units sold
- active customers

### 5. SCD Type 2

Customer history uses:

- `effective_from`
- `effective_to`
- `is_current`

A changed tracked attribute expires the previous version and creates a new current version.

## Data quality

| Check | Expected rule | Handling |
|---|---|---|
| Transaction ID | Not null | Reject |
| Customer ID | Not null | Reject |
| Amount | >= 0 | Reject |
| Transaction ID | Unique | Deduplicate |
| Customer status | Valid status | Reject/flag |
| Customer reference | Must exist | Flag |

Invalid records can be routed to a quarantine dataset for investigation.

## Performance strategy

For production-scale workloads, the design emphasizes:

- early predicate filtering
- incremental extraction
- column pruning
- minimizing shuffles
- appropriate partitioning
- Delta optimization
- monitoring Spark stages for skew/spills
- avoiding driver-side `collect()`
- broadcast joins only for genuinely small dimensions

See [`docs/performance.md`](docs/performance.md).


## CI/CD

GitHub Actions runs on pushes and pull requests and:

1. sets up Python 3.11
2. validates Python syntax
3. runs lightweight tests

The workflow is intentionally credential-free and does not connect to an Azure subscription.


## Author

**Abhishek Taware**

Data Engineer | Azure Databricks | PySpark | SQL | ADF | ADLS Gen2

Portfolio: https://github.com/Tisonabhi/my-portfolio

---

### Public repository positioning

This project is intentionally designed as a **public, non-confidential demonstration** of data engineering architecture and implementation patterns. Production code and data are excluded.
