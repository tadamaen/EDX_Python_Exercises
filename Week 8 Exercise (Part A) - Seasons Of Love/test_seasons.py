# Test Cases
# Remember to convert the date from string to datetime first before asserting (if not type error will occur)

from seasons import minutes_difference
import pytest
from datetime import datetime


def test_minutes_difference():

    # Test 1
    date1 = datetime.strptime("2024-01-10 00:00:00", "%Y-%m-%d %H:%M:%S")
    date2 = datetime.strptime("2025-01-10 00:00:00", "%Y-%m-%d %H:%M:%S")
    assert minutes_difference(date1, date2) == 527040

    # Test 2
    date1 = datetime.strptime("1990-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
    date2 = datetime.strptime("2025-01-10 00:00:00", "%Y-%m-%d %H:%M:%S")
    assert minutes_difference(date1, date2) == 18421920

    # Test 3
    date1 = datetime.strptime("0963-10-26 00:00:00", "%Y-%m-%d %H:%M:%S")
    date2 = datetime.strptime("2025-01-10 00:00:00", "%Y-%m-%d %H:%M:%S")
    assert minutes_difference(date1, date2) == 558142560

    # Test 4: Invalid date format
    with pytest.raises(ValueError):
        datetime.strptime("2025/01/10 00:00:00", "%Y-%m-%d %H:%M:%S")

    # Test 5: Invalid date string
    with pytest.raises(ValueError):
        datetime.strptime("invalid-date", "%Y-%m-%d %H:%M:%S")
