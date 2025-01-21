# Whereas most countries use a 24-hour clock, the United States tends to use a 12-hour clock. Accordingly,
# instead of “09:00 to 17:00”, many Americans would say they work “9:00 AM to 5:00 PM” (or “9 AM to 5 PM”),
# wherein “AM” is an abbreviation for “ante meridiem” and “PM” is an abbreviation for “post meridiem”,
# wherein “meridiem” means midday (i.e., noon).

# Conversion Table
# In a file called working.py, implement a function called convert that expects a str in any of the 12-hour formats
# below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00). Expect that AM and PM will be
# capitalized (with no periods therein) and that there will be a space before each. Assume that these times are
# representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.

#   9:00 AM to 5:00 PM
#   9 AM to 5 PM
#   9:00 AM to 5 PM
#   9 AM to 5:00 PM

# Raise a ValueError instead if the input to convert is not in either of those formats or if either time is invalid
# (e.g., 12:60 AM, 13:00 PM, etc.). But do not assume that someone’s hours will start ante meridiem and end post meridiem;
# someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).

# Structure working.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see
# fit, but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.


# Define the main function using the convert function below
def main():
    print(convert(input("Hours: ")))


# Define the convert function
def convert(s):

    # Bad input 1 - Incorrect formats (no to)
    if "to" not in s:
        raise ValueError
    else:

        # Split the string up using the "to" as the seperator
        elements = s.split(" to ")

        # The start time represents the string before the "to"
        start = elements[0]

        # The end time reprsents the string after the "to"
        end = elements[1]

        # Bad input 2 - Incorrect formats (no spacebars anywhere)
        if " " not in start or " " not in end:
            raise ValueError

        # Other valid inputs
        else:

            # Remove the spaces in the start and end strings
            start = start.replace(" ", "")
            end = end.replace(" ", "")

            # Two possible cases
            # Case 1: 9AM to 5PM (no :)
            # Case 2: 9:00AM to 5:00PM (got :)
            # For consistency, include :00 in the inputs fromn Case 1
            if ":" not in start:
                start = start[:-2] + ":00" + start[-2:]
            if ":" not in end:
                end = end[:-2] + ":00" + end[-2:]

            # Bad input 3 - Incorrect presentation of time (eg: 9:60 AM, 12:90 PM)
            if int(start[-4:-2]) >= 60 or int(end[-4:-2]) >= 60:
                raise ValueError

            # Other cases with correct time presentations
            else:
                # Possible input types:
                #  1. 11:00AM -> 11:00 (make the number constant at 11)
                #  2. 3:00PM -> 15:00  (increase the value of 3 by 12 to get 15)
                #  3. 4:30PM -> 16:30  (increase the value of 4 by 12 to get 16, 30 remains the same)
                #  4. 12:00AM -> 00:00 (special edge case, reduce the value by 12 to get 0 if 12 and AM)
                #  5. 12:00PM -> 12:00 (special edge case, do nothing to the value 12 if 12 and PM)

                # CASE 1: BOTH START AND END TIME ARE IN AM
                if start[-2:] == "AM" and end[-2:] == "AM":
                    start_time = int(start[:-5])
                    end_time = int(end[:-5])

                    if start_time < 10:
                        start_string = f"0{start_time}"
                    elif 10 <= start_time < 12:
                        start_string = f"{start_time}"
                    elif start_time == 12:
                        modified_time = start_time - 12
                        start_string = f"0{modified_time}"
                    else:
                        raise ValueError

                    if end_time < 10:
                        end_string = f"0{end_time}"
                    elif 10 <= end_time < 12:
                        end_string = f"{end_time}"
                    elif end_time == 12:
                        modified_time = end_time - 12
                        end_string = f"0{modified_time}"
                    else:
                        raise ValueError

                    return f"{start_string}:{start[-4:-2]} to {end_string}:{end[-4:-2]}"

                # CASE 2: START TIME IN AM AND END TIME IN PM
                elif start[-2:] == "AM" and end[-2:] == "PM":
                    start_time = int(start[:-5])
                    end_time = int(end[:-5])

                    if start_time < 10:
                        start_string = f"0{start_time}"
                    elif 10 <= start_time < 12:
                        start_string = f"{start_time}"
                    elif start_time == 12:
                        modified_time = start_time - 12
                        start_string = f"0{modified_time}"
                    else:
                        raise ValueError

                    if end_time == 12:
                        end_string = f"{end_time}"
                    elif 1 <= end_time <= 11:
                        end_time_24 = end_time + 12
                        end_string = f"{end_time_24}"
                    else:
                        raise ValueError

                    return f"{start_string}:{start[-4:-2]} to {end_string}:{end[-4:-2]}"

                # CASE 3: START TIME IN PM AND END TIME IN AM
                elif start[-2:] == "PM" and end[-2:] == "AM":
                    start_time = int(start[:-5])
                    end_time = int(end[:-5])

                    if start_time == 12:
                        start_string = f"{start_time}"
                    elif 1 <= start_time <= 11:
                        start_time_24 = start_time + 12
                        start_string = f"{start_time_24}"
                    else:
                        raise ValueError

                    if end_time < 10:
                        end_string = f"0{end_time}"
                    elif 10 <= end_time < 12:
                        end_string = f"{end_time}"
                    elif end_time == 12:
                        modified_time = end_time - 12
                        end_string = f"0{modified_time}"
                    else:
                        raise ValueError

                    return f"{start_string}:{start[-4:-2]} to {end_string}:{end[-4:-2]}"

                # CASE 4: START AND END TIME IN PM
                elif start[-2:] == "PM" and end[-2:] == "PM":
                    start_time = int(start[:-5])
                    end_time = int(end[:-5])

                    if start_time == 12:
                        start_string = f"{start_time}"
                    elif 1 <= start_time <= 11:
                        start_time_24 = start_time + 12
                        start_string = f"{start_time_24}"
                    else:
                        raise ValueError

                    if end_time == 12:
                        end_string = f"{end_time}"
                    elif 1 <= end_time <= 11:
                        end_time_24 = end_time + 12
                        end_string = f"{end_time_24}"
                    else:
                        raise ValueError

                    return f"{start_string}:{start[-4:-2]} to {end_string}:{end[-4:-2]}"

                # Bad input 4 - Wrong time units (eg: 9:00 MM, 11:30 RM)
                else:
                    raise ValueError


if __name__ == "__main__":
    main()
