# Import the value function from bank
from bank import value

# From test cases, we need to test:
#    1) Pass all the checks (from Exercise)
#    2) Including numbers in the words
#    3) Case-sensitivity of the words/phrases
#    4) Not allowing for entire phrase
#    5) Punctuation marks in words
#    6) EXTRA: Hello to be situated not in the beginning of the word/phrase

# 7 possible test cases to consider
def test_assert():
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("hugging") == 20
    assert value("mickey mouse") == 100
    assert value("h123456h") == 20
    assert value("hello , damaen") == 0
    assert value("welcome damaen, hello") == 100
