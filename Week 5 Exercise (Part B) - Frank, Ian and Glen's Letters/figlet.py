# In a file called figlet.py, implement a program that:

# 1. Expects zero or two command-line arguments:
# 2. Zero if the user would like to output text in a random font.
# 3. Two if the user would like to output text in a specific font, in which case the first of the two should be -f
#    or --font, and the second of the two should be the name of the font.
# 4. Prompts the user for a str of text.
# 5. Outputs that text in the desired font.
# 6. If the user provides two command-line arguments and the first is not -f or --font or the second is not the name
#    of a font, the program should exit via sys.exit with an error message.

# Step 0: Installing the pyfiglet library
# pip install pyfiglet

# Step 1: Import the necessary Figlet module from the pyfiglet library
from pyfiglet import Figlet

figlet = Figlet()

# Step 2: Install the package sys and random
import sys
import random

# Step 3: Use conditionals to filter out bad arguments

# Bad argument 1: Wrong command line argument length
if len(sys.argv) != 1 and len(sys.argv) != 3:
    sys.exit("Invalid Usage")

# Case 1: Command line length is 3 (includes font and style)
elif len(sys.argv) == 3:

    # Bad argument 2: If the arguments are stated wrongly for the font
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        sys.exit("Invalid Usage")

    # Bad argument 3: If the name of font is not in the list of fonts in the figlet package
    elif sys.argv[2] not in figlet.getFonts():
        sys.exit("Invalid Usage")

    # All other possible cases
    else:
        user_input = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(user_input))

# Case 2: Command line length is 1 (does not include font and style)
else:
    user_input = input("Input: ")
    figlet.setFont(font=random.choice(figlet.getFonts()))
    print(figlet.renderText(user_input))
