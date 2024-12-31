# One of the most popular places to eat in Harvard Square is Felipe’s Taqueria, which offers a menu of entrees,
# per the dict below, wherein the value of each key is a price in dollars:

# {
#     "Baja Taco": 4.25,
#     "Burrito": 7.50,
#     "Bowl": 8.50,
#     "Nachos": 11.00,
#     "Quesadilla": 8.50,
#     "Super Burrito": 8.50,
#     "Super Quesadilla": 9.50,
#     "Taco": 3.00,
#     "Tortilla Salad": 8.00
# }

# In a file called taqueria.py, implement a program that enables a user to place an order, prompting them for items,
# one per line, until the user inputs control-d (which is a common way of ending one’s input to a program).
# After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($)
# and formatted to two decimal places. Treat the user’s input case insensitively.
# Ignore any input that isn’t an item. Assume that every item on the menu will be titlecased.

# Step 1: Create the dictionary conaining the food items and the prices
food_items = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# Step 2: Initialize the total cost to 0 first
total_cost = 0

# Step 3: Ask the user for his/her input of food
while True:
    try:
        food_input = input("Item: ")
        food_input_title = food_input.title()
        food_price = food_items[food_input_title]

    # First Exception - Key Error (Food Item does not exist on the menu)
    except KeyError:
        print("Food item does not exist in the menu!")

    # Second Exception - EOF Error (When the user inputs Ctrl-D to break out of the loop)
    except EOFError:
        print("\n")
        break

    # All other possible cases
    else:
        # Update total cost when more food items are added
        total_cost = total_cost + food_price
        # Printing the total cost to 2dp in the correcr format
        print(f"Total: ${total_cost:.2f}")
