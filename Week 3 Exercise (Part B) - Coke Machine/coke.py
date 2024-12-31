# Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations:
# 25 cents, 10 cents, and 5 cents.

# In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the
# user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed.
# Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

# Step 1: Assign the value of 50 cents to a variable to keep track
money = 50

# Step 2: Give the starting input of "Amount Due: 50"
print("Amount Due: 50")

# Step 3: Use the while loop to keep track of the amount due/change owed amount
while True:
    coin_insertion = int(input("Insert Coin: "))
    if coin_insertion == 25 or coin_insertion == 10 or coin_insertion == 5:
        money = money - coin_insertion
        if money > 0:
            print(f"Amount Due: {money}")
            continue
        else:
            print(f"Change Owed: {-money}")
            break
    else:
        print(f"Amount Due: {money}")

