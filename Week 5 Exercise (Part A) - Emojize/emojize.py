# Because emoji aren’t quite as easy to type as text, at least on laptops and desktops, some programs support “codes,”
# whereby you can type, for instance, :thumbs_up:, which will be automatically converted to 👍.

# Some programs additionally support aliases, whereby you can more succinctly type, for instance, :thumbsup:,
# which will also be automatically converted to 👍.

# In a file called emojize.py, implement a program that prompts the user for a str in English and then outputs
# the “emojized” version of that str, converting any codes (or aliases) therein to their corresponding emoji.

# Step 0: Install emoji in the terminal window
# pip install emoji

# Step 1: Import the package emoji
import emoji

# Step 2: Ask the user for his/her input
input_emoji = input("Input: ")

# Step 3: Convert the user input to the correct format before output (eg: :thumbsup:)
# Refer to the documentation for help and the correct syntax
output_emoji = emoji.emojize(f"Output: {input_emoji}" , language = 'alias')

# Step 4: Print the output of the emoji
print(output_emoji)
