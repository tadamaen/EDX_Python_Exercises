# Import shorten from the modified twttr code
from twttr import shorten

# Testing the twttr function using various test cases

# From test cases, we need to test:
#    1) Pass all the checks of removal of all vowels (both lower and upper case)
#    2) No replacements of vowels
#    3) Not omitting all numbers
#    4) Not omitting all punctuation
#    5) Upper and lower case integrity


# 5 possible test cases to consider
def test_assert():
    assert shorten("damaen") == "dmn"
    assert shorten("helloworld") == "hllwrld"
    assert shorten("MickeyMouse") == "MckyMs"
    assert shorten("123OKAY123can") == "123KY123cn"
    assert shorten("allbutone,allbutmany") == "llbtn,llbtmny"
