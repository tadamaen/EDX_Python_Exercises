# In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and
# Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.

# Step 1: Prompt the user for his/her input to the question
prompt = input("What is the answer to the Great Question of Life, the Universe, and Everthing? ")

# Step 2: Check if the user input is 42 or not using conditionals
if prompt.replace(" ", "") == "42" or prompt == 'forty-two' or prompt.lower() == 'forty two':
    print("Yes")
else:
    print("No")
