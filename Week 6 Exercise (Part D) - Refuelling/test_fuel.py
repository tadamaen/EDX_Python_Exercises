import pytest

# Import the convert and gauge functions from the fuel package
from fuel import convert, gauge

# 1st test: Test for the convert function
def test_convert():
    assert convert("2/3") == 67
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("5/6") == 83

    # Testing for zero division error
    with pytest.raises(ZeroDivisionError):
        convert("5/0")

    # Testing for value error (X > Y)
    with pytest.raises(ValueError):
        convert("4/3")

# 2nd test: Test for the gauge function
def test_gauge():
    assert gauge(75) == "75%"
    assert gauge(90) == "90%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(98) == "98%"
    assert gauge(2) == "2%"
    assert gauge(100) == "F"
    assert gauge(0) == "E"
