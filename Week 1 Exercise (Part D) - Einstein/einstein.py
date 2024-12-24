# Even if you haven’t studied physics (recently or ever!), you might have heard that E = mc^2, wherein E represents energy
# (measured in Joules), m represents mass (measured in kilograms), and c represents the speed of light (measured approximately as
# 300000000 meters per second), per Albert Einstein et al. Essentially, the formula means that mass and energy are equivalent.

# In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer
# (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.

# Step 1: Ask the user for his/her input mass
mass = int(input("What is your mass (in kilograms)? "))

# Step 2: Assign the value 3000000 to c
speed = 300000000

# Step 3: Calculate the value of energy in Joules
energy = mass * (speed ** 2)

# Step 4: Print the value of energy
print(energy)
