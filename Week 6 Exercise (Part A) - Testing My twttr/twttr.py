# From the main function, apply the shorten function defined below
def main():
    user_input = input("Input: ")
    shortened_word = shorten(user_input)
    print(shortened_word)


# Define the shorten function (Similar to Week 2 Exercise Part C)
def shorten(word):

    # From Week 2 Exercise (Part C)
    letters = []

    for letter in word:
        letters.append(letter)

    index_vowels = []
    for index, letter in enumerate(letters):
        if (
            letter == "a"
            or letter == "e"
            or letter == "i"
            or letter == "o"
            or letter == "u"
            or letter == "A"
            or letter == "E"
            or letter == "I"
            or letter == "O"
            or letter == "U"
        ):
            index_vowels.append(index)

    for index, number in enumerate(index_vowels):
        letters.pop(number - index)

    final_string = ""
    for letter in letters:
        final_string += letter

    # Change to return instead of print for test purposes
    return final_string


if __name__ == "__main__":
    main()
