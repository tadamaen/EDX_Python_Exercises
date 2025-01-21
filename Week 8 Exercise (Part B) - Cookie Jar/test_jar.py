# Tests For The Jar Class And The Respective Functions

import pytest
from jar import Jar


# TEST 1: Test for the __init__ method
# See if the ValueError is triggered if negative numbers are inputted
def test_init():
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar(-10)
    with pytest.raises(ValueError):
        Jar(-100)


# TEST 2: Test for the __str__ method
# See if the number of cookies printed out is correct when the deposit and withdraw functions are applied
def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.withdraw(5)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪"
    jar.withdraw(2)
    assert str(jar) == "🍪🍪🍪🍪🍪"
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪"


# TEST 3: Test for the deposit function
# See if the ValueError is triggered when the number of cookies added exceeds the maximum capacity of 12
def test_deposit():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(13)
    with pytest.raises(ValueError):
        jar.deposit(20)


# TEST 4: Test for the withdraw function
# See if the ValueError is triggered when cookies are removed when the initial number of cookies in jar is 0
def test_withdraw():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(1)
    with pytest.raises(ValueError):
        jar.withdraw(5)
