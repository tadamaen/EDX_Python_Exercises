# Bitcoin is a form of digital currency, otherwise known as cryptocurrency. Rather than rely on a central authority
# like a bank, Bitcoin instead relies on a distributed network, otherwise known as a blockchain, to record transactions.

# Because there’s demand for Bitcoin (i.e., users want it), users are willing to buy it, as by exchanging one
# currency (e.g., USD) for Bitcoin.

# In a file called bitcoin.py, implement a program that:
# Expects the user to specify as a command-line argument the number of Bitcoins, n,
# that they would like to buy. If that argument cannot be converted to a float, the program should exit via sys.exit
# with an error message.

# Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json,
# which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float

# Import the necesary packages
import sys
import requests

# Bad Input 1: If the length of the argument is wrong (too few or too many)
if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

# If the number of arguments added is correct
else:
    try:
        # Try converting the input to a float
        float_price = float(sys.argv[1])

        # Get the request using requests.get to obtain the json file
        request = requests.get(
            "https://api.coindesk.com/v1/bpi/currentprice.json", stream=True
        )
        json_file = request.json()

        # Obtain the USD Current price from the nested dictionaries
        usd_rate_str = json_file["bpi"]["USD"]["rate"]

        # Need to remove the comma first before converting to a float to prevent ValueError
        usd_rate_str = usd_rate_str.replace(",", "")

        # Convert the string to a float before performing calculations
        usd_rate_flt = float(usd_rate_str)

        # Multiply the value obtained from the dict by value in sys.argv[1]
        bitcoin_price = usd_rate_flt * float_price

    # If the input given in sys.argv[1] is a string
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # Bad Input 2: To catch any requests error (Optional)
    except requests.RequestException:
        sys.exit()

    # If all works, print the final bitcoin price in 4dp
    else:
        print(f"${bitcoin_price:,.4f}")
