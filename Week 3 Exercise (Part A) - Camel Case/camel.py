# In some languages, it’s common to use camel case (otherwise known as “mixed case”) for variables’ names when those names comprise
# multiple words, whereby the first letter of the first word is lowercase but the first letter of each subsequent word is uppercase.

# For instance, whereas a variable for a user’s name might be called name, a variable for a user’s first name might be called
# firstName, and a variable for a user’s preferred first name (e.g., nickname) might be called preferredFirstName.

# Python, by contrast, recommends snake case, whereby words are instead separated by underscores (_), with all letters in lowercase.
# For instance, those same variables would be called name, first_name, and preferred_first_name, respectively, in Python.

# In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case and outputs the
# corresponding name in snake case. Assume that the user’s input will indeed be in camel case.

# Step 1: Ask the user for the input in camel case
camel_input = input("camelCase: ")

# Step 2: Converting to snake case
# Step 2.1: Break up the word input into individual letters
letters = []
for letter in camel_input:
    letters.append(letter)

# Step 2.2: Extract the index of all the capital letters
index_ls = []
for index, element in enumerate(letters):
    if element.isupper():
        index_ls.append(index)

# Step 2.3: Insert the underscores at the proper index of the list
for index_two, number in enumerate(index_ls):
    letters.insert(index_two + number, "_")

# Step 2.4: Combine the letters and symbols into 1 string
merged_string = ""
for letter in letters:
    merged_string += letter

# Step 2.5: Make all the letters in lower case to get to snake case
merged_string = merged_string.lower()

# Print the final output
print(merged_string)
