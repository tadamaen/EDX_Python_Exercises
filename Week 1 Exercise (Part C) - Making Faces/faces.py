# Before there were emoji, there were emoticons, whereby text like :) was a happy face and text like :( was a sad face.
# Nowadays, programs tend to convert emoticons to emoji automatically!

# In a file called faces.py, implement a function called convert that accepts a str as input and returns that same input with any :)
# # converted to 🙂 (otherwise known as a slightly smiling face) and any :( converted to 🙁 (otherwise known as a slightly frowning
# face). All other text should be returned unchanged.

# Then, in that same file, implement a function called main that prompts the user for input, calls convert on that input,
# and prints the result. You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an
# argument to input. Be sure to call main at the bottom of your file.

# Define the function convert which takes in a sentence as an input and replace :) with 🙂 and :( with 🙁 respectively
def convert(string_sentence):
    input_string = string_sentence
    input_string_one = input_string.replace(":)", "🙂")
    input_string_two = input_string_one.replace(":(", "🙁")
    return input_string_two

# Define the main function which
#    1. Prompts the user to give his/her input
#    2. Use the convert function defined earlier to replace the smiles and frowns with emojis
#    3. Print out the resulting sentence with emojis
def main():
    user_sentence = input("What do you want to say? ")
    output_sentence = convert(user_sentence)
    print(output_sentence)

# Call the main function
main()
