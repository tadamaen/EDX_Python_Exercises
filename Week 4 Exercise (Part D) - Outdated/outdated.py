# In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY), otherwise known as
# middle-endian order, which is arguably bad design.

# Dates in that format can’t be easily sorted because the date’s year comes last instead of first.
# Try sorting, for instance, 2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any program (e.g., a spreadsheet).
# Dates in that format are also ambiguous. Harvard was founded on September 8, 1636, but 9/8/1636 could also be
# interpreted as August 9, 1636!

# Fortunately, computers tend to use ISO 8601, an international standard that prescribes that dates should be formatted
# in year-month-day (YYYY-MM-DD) order, no matter the country, formatting years with four digits, months with two
# digits, and days with two digits, “padding” each with leading zeroes as needed.

# In a file called outdated.py, implement a program that prompts the user for a date, anno Domini,
# in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be
# any of the values in the list below:

# Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format,
# prompt the user again. Assume that every month has no more than 31 days; no need to validate whether a month has
# 28, 29, 30, or 31 days.

# List of valid month names
valid_months_list_words = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
                           "October", "November", "December"]
# List of valid month numbers (1-12)
valid_months_list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# List of valid days (1-31)
valid_days_numbers = list(range(1, 32))

# Function to check if a string contains any letters
def contains_letters(s):
    return any(char.isalpha() for char in s)

# Loop to keep prompting the user until valid input is provided
while True:
    try:
        # Prompt user for date input
        date_input = input("Date: ")

        # Remove leading whitespace if present
        if date_input[0] == " ":
            date_input = date_input[1:]

        # Check if input contains either a comma (for written format) or a slash (for numeric format)
        if "," in date_input or "/" in date_input:
            # Ensure input format matches expected patterns
            if (contains_letters(date_input) == False and "/" in date_input) or (contains_letters(date_input) and "," in date_input):
                # Replace commas and slashes with spaces for easier parsing
                date_input = date_input.replace(",", "")
                date_input = date_input.replace("/", " ")

                # Split the input into individual components (month, day, year)
                elements_ls = str.split(date_input, " ")

                # Assign components to respective variables
                month = elements_ls[0]
                day = elements_ls[1]
                year = elements_ls[2]

                # If the input contains a valid month name and day number
                if (month in valid_months_list_words) and (int(day) in valid_days_numbers):
                    # Convert month name to its corresponding numeric value
                    month_index = valid_months_list_words.index(month)
                    month_number = month_index + 1
                    year = int(year)
                    day = int(day)

                    # Print the date in YYYY-MM-DD format
                    print(f"{year}-{month_number:02}-{day:02}")
                    break

                # If the input contains a valid numeric month and day
                elif (int(month) in valid_months_list_numbers) and (int(day) in valid_days_numbers):
                    month = int(month)
                    year = int(year)
                    day = int(day)

                    # Print the date in YYYY-MM-DD format
                    print(f"{year}-{month:02}-{day:02}")
                    break

    except ValueError:
        # Prompt the user to input the date correctly if an error occurs
        print("Please Input Correctly!")

