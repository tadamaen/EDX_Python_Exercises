from working import convert
import pytest

# Test Cases Part 1:
# Test for valid outputs

def test_valid_outputs():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"
    assert convert("8:15 PM to 11 PM") == "20:15 to 23:00"
    assert convert("6 AM to 9 AM") == "06:00 to 09:00"
    assert convert("6:30 AM to 9:50 AM") == "06:30 to 09:50"
    assert convert("2 AM to 10:45 AM") == "02:00 to 10:45"
    assert convert("3 PM to 11 PM") == "15:00 to 23:00"
    assert convert("12 AM to 1:45 PM") == "00:00 to 13:45"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("3:15 PM to 10:45 PM") == "15:15 to 22:45"
    assert convert("12:12 PM to 12:45 PM") == "12:12 to 12:45"

# Test Cases Part 2:
# Test for value errors

def test_value_errors():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
    with pytest.raises(ValueError):
        convert("9:85 AM to 6:90 PM")
    with pytest.raises(ValueError):
        convert("13:00 AM - 6:00 PM")

