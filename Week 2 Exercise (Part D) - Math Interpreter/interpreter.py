# Python already supports math, whereby you can write code to add, subtract, multiply, or divide values and even variables.
# But let’s write a program that enables users to do math, even without knowing Python.

# In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and then calculates
# and outputs the result as a floating-point value formatted to one decimal place.
# Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:

#    x is an integer
#    y is +, -, *, or /
#    z is an integer

# For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.

# Step 1: Prompt the user for an arithmetic expression
expression = input("Expression: ")

# Step 2: Obtain the values of x, y and z respectively in the correct data type
# This can be done by breaking the expression into individual terms using string split
# Example: 1 + 1 can be broken down into 1, "+", and 1 respectively
ls = []
terms = expression.split(" ")
x = float(terms[0])
y = terms[1]
z = float(terms[2])

# Step 2: Convert the expression to integer/float and perform the arithmetic
# This can be done through conditional statements as y can only take on four values: '+", "-", "*", "/"
if y == "+":
    value_obtained = round(x + z, 1)
elif y == "-":
    value_obtained = round(x - z, 1)
elif y == "*":
    value_obtained = round(x * z, 1)
else:
    value_obtained = round(x / z, 1)

# Step 3: Print out the value obtained
print(value_obtained)
