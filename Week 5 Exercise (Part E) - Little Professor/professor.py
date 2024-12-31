# DIFFICULT QUESTION

# One of David’s first toys as a child, funny enough, was Little Professor, a “calculator” that would generate ten
# different math problems for David to solve. For instance, if the toy were to display 4 + 0 = ,
# David would (hopefully) answer with 4. If the toy were to display 4 + 1 = ,
# David would (hopefully) answer with 5. If David were to answer incorrectly, the toy would display EEE.
# And after three incorrect answers for the same problem, the toy would simply display the correct answer
# (e.g., 4 + 0 = 4 or 4 + 1 = 5).

# In a file called professor.py, implement a program that:

# Prompts the user for a level.
# If the user does not input 1, 2, or 3, the program should prompt again.
# Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative
# integer with digits. No need to support operations other than addition (+).

# Prompts the user to solve each of those problems. If an answer is not correct (or not even a number),
# the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem.
# If the user has still not answered correctly after three tries, the program should output the correct answer.

# The program should ultimately output the user’s score: the number of correct answers out of 10.
# Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and
# returns 1, 2, or 3, and generate_integer returns a randomly generated non-negative integer with level digits or
# raises a ValueError if level is not 1, 2, or 3

# Import the random package
import random


def main():
    # First, use the get_level function to prompt the user for the input level
    level_prompt = get_level()

    # Assign an initial score of 0
    score = 0

    # Since we need to ask 10 questions, use a for loop to iterate 10 times
    for i in range(10):

        # Need two random integers to perform addition of two numbers
        integer_one = generate_integer(level_prompt)
        integer_two = generate_integer(level_prompt)

        # Get the actual correct answer
        correct_answer = integer_one + integer_two

        # Set the number of attempts to 0
        attempts = 0

        # Maximum number of attempts a user can try for a question is 3, otherwise move to next question
        while attempts < 3:
            try:
                user_input_number = int(input(f"{integer_one} + {integer_two} = "))

                # Case 1: If user keys in the correct answer
                # Increment score by 1
                # Break out of the while loop to start a new attempt
                if user_input_number == correct_answer:
                    score += 1
                    break

                # Case 2: If user keys in a wrong answer (but integer)
                # Increase attempts by 1
                # Print 'EEE' to show that the answer is wrong
                else:
                    print("EEE")
                    attempts += 1

            # Case 3: If user keys in a wrong answer (not integer)
            # Increase attempts by 1
            # Print 'EEE' to show that the answer is wrong
            except ValueError:
                print("EEE")
                attempts += 1

        # When user inputs the wrong answer 3 times, show the correct answer
        # Need to exit the while loop also to start the next problem
        if attempts == 3:
            print(f"{integer_one} + {integer_two} = {correct_answer}")

    # Print out the final score obtained
    print(f"Score: {score}")


# Define the function get_level that returns an integer level (only accepts 1, 2 or 3)
def get_level():
    while True:
        try:
            level_number = int(input("Level: "))
            # Only return if the user inputs level number of 1, 2 or 3
            if level_number == 1 or level_number == 2 or level_number == 3:
                return level_number

        # Catch cases where user types in a string
        except ValueError:
            pass


# Define the function generate integer that gives a generated number based on level input number
# level 1: generates a number from 0 to 9
# level 2: generates a number from 10 to 99
# level 3: generates a number from 100 to 999


def generate_integer(level):
    # Raises value error when level input number is not 1, 2 or 3
    if level != 1 and level != 2 and level != 3:
        raise ValueError
    else:
        if level == 1:
            generated_number = random.randint(0, 9)
        elif level == 2:
            generated_number = random.randint(10, 99)
        else:
            generated_number = random.randint(100, 999)
        return generated_number


if __name__ == "__main__":
    main()
