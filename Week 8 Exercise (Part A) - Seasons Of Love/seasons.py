# Import all the necessary packages (datetime, sys, inflect)
from datetime import datetime, date
import sys
import inflect

p = inflect.engine()


def main():

    # Ask the user for his/her date of birth
    historical_time = input("Date Of Birth: ")

    # Catch for improper inputs, exit the system immediately
    if "-" not in historical_time:
        sys.exit("Invalid date")

    # Convert the string to a datetime object
    historical_time_adjusted = datetime.strptime(historical_time, "%Y-%m-%d")

    # Get the current date (can be any date)
    # Remove the hours, minutes and seconds from the current date
    # Similarly, convert the string to a datetime object
    current_time = date.today()
    formatted_now = current_time.strftime("%Y-%m-%d")
    formatted_now = datetime.strptime(formatted_now, "%Y-%m-%d")

    # Apply the minutes_difference function to get the time difference in minutes in number
    difference_minutes = minutes_difference(historical_time_adjusted, formatted_now)

    # Apply the convert_to_word function to print out the result in words
    time_difference = convert_to_word(difference_minutes)

    # Apply some transformation to get the exact output
    #   1. Remove the point (in case of decimals) - splitting and extracting the front portion
    #   2. Remove any and's from the phrase (be careful of thousand)
    #   3. Convert the first letter of the phrase to upper case
    time_info = time_difference.split(" point ")
    importance = time_info[0]
    importance = importance.replace(" and", "")

    # Print the final result obtained
    print(f"{importance[0].upper()}{importance[1:]} minutes")


# Define the minutes_difference function
def minutes_difference(date_one, date_two):
    # date_one and date_two are already in datetime format when the function is applied
    difference = date_two - date_one

    # Extract the total seconds (difference)
    difference_seconds = difference.total_seconds()

    # Convert to total minutes (difference) by dividing by 60
    difference_minutes = difference_seconds / 60

    return difference_minutes


# Define the convert_to_word function to change the time difference from numerical to word format
def convert_to_word(minutes):
    return p.number_to_words(minutes)

if __name__ == "__main__":
    main()
