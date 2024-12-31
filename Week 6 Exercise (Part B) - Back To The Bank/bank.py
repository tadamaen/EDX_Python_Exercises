# From the main function, apply the value function
def main():
    greeting_input = input("Greeting: ")
    money = value(greeting_input)
    print(int(money))

# Define the function value
def value(greeting):

    # Modified from Week 2 Exercise (Part B)
    # The only difference is that now we are returning instead of printing
    # Also, the output must be an integer instead of a string

    if (
        greeting.replace(" ", "").lower() == "hello"
        or greeting.replace(" ", "")[0:5].lower() == "hello"
    ):
        return 0
    elif greeting.replace(" ", "")[0].lower() == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
