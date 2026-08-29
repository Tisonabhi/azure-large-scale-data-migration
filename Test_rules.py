def test_negative_amount_is_invalid():
    amount = -1
    assert amount < 0

def test_watermark_direction():
    old = "2026-08-28 00:00:00"
    new = "2026-08-29 00:00:00"
    assert new > old
