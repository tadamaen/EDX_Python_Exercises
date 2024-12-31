# Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full,
# 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

# In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is
# an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank.
# If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains,
# output F instead to indicate that the tank is essentially full.

# If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again.
# (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.

while True:
    try:
        # Step 1: Ask the user for the fraction
        fraction = input("Fraction: ")

        # Step 2: Identify X and Y
        elements = fraction.split(sep = "/")
        X = int(elements[0])
        Y = int(elements[1])
        fraction_num = X / Y

    # 1st Exception: Handle Zero Division Error
    except ZeroDivisionError:
        print("Value of Y cannot be zero!")

    # 2nd Exception: Handle Value Error
    except ValueError:
        print("Please input valid values of X and Y!")

    # For all other valid cases, compute the fuel percentage
    else:
        # Condition to rule out inputs where Y is greater than X
        if X <= Y:
            # Condition where the fuel percentage is 99% or greater
            if 0.99 <= fraction_num <= 1:
                print("F")
            # Condition where the fuel percentage is 1% or lower
            elif 0 <= fraction_num <= 0.01:
                print("E")
            # All other conditions - 1% < fuel percentage < 99%
            else:
                perc_rounded = int(round(fraction_num * 100, 0))
                print(f"{perc_rounded}%")
            # Apply break to exit the while loop to prevent an infinite loop
            break

