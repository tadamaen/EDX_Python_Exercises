# It’s not uncommon, in English, at least, to say “um” when trying to, um, think of a word.
# The more you do it, though, the more noticeable it tends to be!

# In a file called um.py, implement a function called count that expects a line of text as input as a str and
# returns, as an int, the number of times that “um” appears in that text, case-insensitively, as a word unto itself,
# not as a substring of some other word. For instance, given text like hello, um, world, the function should return 1.
# Given text like yummy, though, the function should return 0.

# Structure um.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit,
# but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.

# Import the re package
import re


# Define the main function where count function is added
def main():
    print(count(input("Text: ")))


# Define the count function
def count(s):

    # Make the entire sentence all to lower case first to iron out case issues
    s = s.lower()

    # Define a set of punctuations for removal subsequently
    punctuations = ".:,?!;"

    # Remove all the punctuations in the sentence s for simplification
    for element in s:
        if element in punctuations:
            s = s.replace(element, "")

    # Edge case - if the word is simply um (return 1 immediately)
    if "um" in s and len(s) == 2:
        count_um = 1
        return count_um

    # Other cases (like a full sentence)
    else:

        # NEW: using the re.findall method and pass it to len to count the number of "um"
        # NEW: Regex expression: \b
        # \b represents a word boundary (It does not match a character but instead matches a position in the string)
        # It helps ensure that the pattern matches only whole words or specific boundaries
        count_um = len(re.findall(r"\bum\b", s))
        return count_um


if __name__ == "__main__":
    main()
