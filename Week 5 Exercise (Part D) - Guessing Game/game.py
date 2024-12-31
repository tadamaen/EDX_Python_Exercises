# In a file called game.py, implement a program that:

# Prompts the user for a level. If the user does not input a positive integer, the program should prompt again.
# Randomly generates an integer between 1 and n, inclusive, using the random module.

# Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user
# again.

# If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
# If the guess is larger than that integer, the program should output Too large! and prompt the user again.
# If the guess is the same as that integer, the program should output Just right! and exit.

# Import the random package for use later on
import random

# Step 1: Prompt user for a valid integer level
while True:
    try:
        integer = int(input("Level: "))

        # If input is valid, move on to the second block of code (break the first loop)
        if integer > 0:
            break

    # If the user's input is not an integer (like string), prompt the user again
    except ValueError:
        pass

# Step 2: Generate a random number within the range of the level
random_number = random.randint(1, integer)

# Step 3: Prompt user for guesses until the correct number is guessed
while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if random_number > guess:
                print("Too small!")
            elif random_number < guess:
                print("Too large!")
            else:
                print("Just right!")
                break

        # If the guess is out of range which is negative numbers
        else:
            pass

    # Similarly, if the guess is of the wrong data type
    except ValueError:
        pass
