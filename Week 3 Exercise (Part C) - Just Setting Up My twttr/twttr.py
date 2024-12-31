# When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels,
# much like Twitter was originally called twttr. In a file called twttr.py, implement a program that prompts the user for a
# str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

# Step 1: Ask the user for an input
user_input = input("Input: ")

# Step 2: Split the words into a list of letters
letters = []

for letter in user_input:
    letters.append(letter)

# Step 3: Filter out all the vowels
index_vowels = []
for index, letter in enumerate(letters):
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" or letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
        index_vowels.append(index)

# Step 4: Remove the vowels from the letters list
for index, number in enumerate(index_vowels):
    letters.pop(number - index)

# Step 5: Convert the list back to a string and output the string
final_string = ""
for letter in letters:
    final_string += letter

# Print the final result
print(f"Output: {final_string}")
