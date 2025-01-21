# FOR TESTING PURPOSES

# Import the count function from um
from um import count

# Test cases (9 of them)
#    1. Removal of punctuation
#    2. Upper/Lowercase letters
#    3. Whether the "um" is alone or within other letters

def test_count():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("um!!") == 1
    assert count("!!um??") == 1
    assert count("UM") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
    assert count("uM mickeyummickey poolum umumumiol um ppola UM ddrfumdd") == 3
    assert count("Whatumniceday um um") == 2
