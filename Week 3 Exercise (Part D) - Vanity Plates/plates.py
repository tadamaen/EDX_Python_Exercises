# In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, with your choice
# of letters and numbers instead of random ones. Among the requirements, though, are:

# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable …
# vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”

# In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements
# or Invalid if it does not. Assume that any letters in the user’s input will be uppercase. Structure your program per the below,
# wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str.
# You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).

# Step 1: Ask the user for his/her input
input_name = input("Plate: ")

# Step 2: Break the string into a list of letters
list_letters = []
numbers = "0123456789"
punctuation = ".,?! /@#$%^&*();:"
for letter in input_name:
    list_letters.append(letter)

# Step 3: Apply a series of conditionals to make the words invalid (if there are problems)
# Condition 1:
if punctuation in list_letters:
    print("Invalid")

# Condition 2: No periods, spaces, or punctuation marks are allowed
elif len(list_letters) < 2 or len(list_letters) > 6:
    print("Invalid")

# Condition 3: All vanity plates must start with at least two letters
elif 48 <= ord(list_letters[0]) <= 57 or 48 <= ord(list_letters[1]) <= 57:
    print("Invalid")

# Condition 4: Numbers cannot be used in the middle of a plate; they must come at the end
elif numbers not in list_letters:
    print("Valid")

elif 65 <= ord(list_letters[-1]) <= 90:
    print("Invalid")

# Condition 5: The first number used cannot be a ‘0’
else:
    number_ls = []
    for index, element in enumerate(list_letters):
        if element in numbers:
            number_ls.append(index)
    if list_letters[number_ls[0]] == "0":
        print("Invalid")
    else:
        print("Valid")

