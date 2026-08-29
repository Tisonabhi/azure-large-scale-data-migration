# Design Notes

## Incremental load

The project uses a high-watermark approach:

```text
previous_watermark = control_table.last_watermark
new_watermark = source.max(updated_at)

extract:
previous_watermark < updated_at <= new_watermark

process

commit new_watermark only after success
```

This prevents a failed run from advancing the control state prematurely.

## Idempotency

Silver processing uses a business key and deterministic ordering. Re-running the same input should not create duplicate current records.

## SCD Type 2

Customer changes are represented with:

- `effective_from`
- `effective_to`
- `is_current`

When a tracked attribute changes, the existing current row is expired and a new version is inserted.

## Error handling

Invalid records are separated into quarantine with:

- source table
- run ID
- rejection reason
- ingestion timestamp
- original record fields

## Security

No credentials or connection strings belong in this repository. In a real Azure deployment, use managed identity, Key Vault and appropriate RBAC.
