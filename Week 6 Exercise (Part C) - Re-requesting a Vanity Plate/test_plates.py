# Import the is_valid function from the plates package
from plates import is_valid

# Possible test cases
def test_assert():
    assert is_valid("C50") == False
    assert is_valid("CS50") == True
    assert is_valid("CS500") == True
    assert is_valid("CS05") == False
    assert is_valid("AAA222") == True
    assert is_valid("MickeyMouse") == False
    assert is_valid("999heavenly") == False
    assert is_valid("CS50OK") == False
    assert is_valid("COS1000") == False
    assert is_valid("CS,50") == False
