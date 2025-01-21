# In Season 5, Episode 23 of NUMB3RS, a supposed IP address appears on screen, 275.3.6.28, which isn’t
# actually a valid IPv4 (or IPv6) address.

# An IPv4 address is a numeric identifier that a device (or, on TV, hacker) uses to communicate on the internet,
# akin to a postal address in the real world, typically formatted in dot-decimal notation as #.#.#.#.
# But each # should be a number between 0 and 255, inclusive. Suffice it to say 275 is not in that range! If only
# NUMB3RS had validated the address in that scene!

# In a file called numb3rs.py, implement a function called validate that expects an IPv4 address as input
# as a str and then returns True or False, respectively, if that input is a valid IPv4 address or not.

# Structure numb3rs.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit,
# but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.

# Note: Solution below is NOT done in regex (no need for regex)


# Define the main function (which involves the validate function)
def main():
    print(validate(input("IPv4 Address: ")))


# Defining the validate function
def validate(ip):

    # First, split the ip string input into the corresponding elements using . as the seperator
    ip_ls = ip.split(".")

    # 1st check: If there are 4 elements in the ip_ls list (only 4 numbers allowed in IP addresses)
    # Any length not equal to 4 will be rejected immediately
    if len(ip_ls) != 4:
        return False

    # For ip_ls == 4
    else:
        try:
            # Check if all the four integers of the IP address are all in the range of 0-255
            if (
                0 <= int(ip_ls[0]) <= 255
                and 0 <= int(ip_ls[1]) <= 255
                and 0 <= int(ip_ls[2]) <= 255
                and 0 <= int(ip_ls[3]) <= 255
            ):
                return True

            # If some numbers violated the 0-255 range limit
            else:
                return False

        # If the elements in the ip_ls are composed of strings and not numbers (cannot be converted to int)
        except ValueError:
            return False


if __name__ == "__main__":
    main()
