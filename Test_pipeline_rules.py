import csv
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class PipelineRulesTest(unittest.TestCase):
    def test_config_has_watermark(self):
        config = json.loads((ROOT / "config/pipeline_config.json").read_text())
        self.assertEqual(config["watermark_column"], "updated_at")

    def test_transaction_csv_has_required_columns(self):
        with open(ROOT / "data/transactions.csv", newline="") as f:
            reader = csv.DictReader(f)
            required = {"transaction_id", "customer_id", "product_id", "amount", "updated_at"}
            self.assertTrue(required.issubset(reader.fieldnames))

    def test_no_negative_demo_transactions(self):
        with open(ROOT / "data/transactions.csv", newline="") as f:
            rows = csv.DictReader(f)
            self.assertTrue(all(float(r["amount"]) >= 0 for r in rows))

if __name__ == "__main__":
    unittest.main()
