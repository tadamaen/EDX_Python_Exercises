# FOR TESTING PURPOSES

# Importing the validate function from the numb3rs package
from numb3rs import validate

# Testing the validate function (10 cases)
# Checking for
#   1. Input are all numbers and no strings
#   2. Correct length of IP address (Must be 4)
#   3. Correct number range limits (0-255)

def test_valid():
    assert validate('0.0.0.0') == True
    assert validate('255.255.255.255') == True
    assert validate('1.2.3.4') == True
    assert validate('0.0.0.1000') == False
    assert validate('255.255.255.275') == False
    assert validate('cat') == False
    assert validate('cat.dog.bird.mickey') == False
    assert validate('20.20.20.-20') == False
    assert validate('2.3.4') == False
    assert validate('10.10.10.10.10') == False
