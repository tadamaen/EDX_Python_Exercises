def main():
    input_fraction = input("Fraction: ")
    perc_convert = convert(input_fraction)
    gauging = gauge(perc_convert)
    print(gauging)

# Modified from Week 4 Exercise Part A
# Split the problem into two different functions

def convert(fraction):
    elements = fraction.split(sep = "/")
    X = int(elements[0])
    Y = int(elements[1])

    # Raise ZeroDivisionError if Y == 0
    if Y == 0:
        raise ZeroDivisionError

    # Raise ValueError if X > Y
    elif X > Y:
        raise ValueError

    # Other Possible Cases
    else:
        frac = X / Y
        perc = frac * 100
        return int(round(perc, 0))

def gauge(percentage):
    if 99 <= percentage <= 100:
        return "F"
    elif 0 <= percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()

