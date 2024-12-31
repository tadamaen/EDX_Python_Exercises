# Suppose that you’re in the habit of making a list of items you need from the grocery store.

# In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user
# inputs control-d (which is a common way of ending one’s input to a program).
# Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the
# number of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively.

food_item_dict = {}

while True:
    # Input the food item a user buys and convert the strings to upper case for ease of displaying subsequently
    try:
        food_item = input()
        food_item = food_item.upper()

    # Exception 1: Key Error (Dummy Error not used for testing)
    except KeyError:
        print("Food item does not exist in the grocery store!")

    # Exception 2: EOF Error (For users to input ctrl-d)
    except EOFError:
        print("\n")

        # Sort the items in the dictionary by alphabetical order
        list_of_dict_key = list(food_item_dict.keys())
        list_of_dict_key.sort()
        final_dict = {i: food_item_dict[i] for i in list_of_dict_key}

        # Print the food items and the total number of each food item on each separate line
        for i in final_dict.keys():
            print(f"{final_dict[i]} {i}")

        # Break out of the loop to end the transaction
        break

    # All other cases - when the user inputs the food item but has not ended yet
    else:
        # Add a new food item to the dictionary, count from 1
        if food_item not in food_item_dict.keys():
            food_item_dict[food_item] = 1
        # Add a food item that is currently already in the dictionary, add 1
        else:
            food_item_dict[food_item] += 1
